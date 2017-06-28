import random
from os import path
import sys
sys.path.append(path.dirname(path.abspath(__file__)))

from Models.person import Person, Fellow, Staff
from Models.Room import Room, Office, LivingSpace
from Models.database import People, Rooms, Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Column, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import exc


class Dojo(object):
    def __init__(self):
        self.rooms = []
        self.offices = []
        self.living_spaces = []
        self.allocated = []
        self.unallocated = []

    def create_room(self, room_name, purpose):
        """ method create room to add new rooms to dojo"""
        # checks room_name and purpose are strings
        if (isinstance(room_name, str) and isinstance(purpose, str)):
            # checks if room is already allocated
            if [room for room in self.rooms
               if room_name.upper() == room.room_name.upper()]:
                print("{} already Exists in Dojo.".format(room_name.upper()))
                return "{} already Exists in Dojo.".format(room_name.upper())
            else:
                # Creates office if purpose is office
                if purpose.upper() == "OFFICE":
                    room = Office(room_name.upper())
                    self.offices.append(room)
                    self.rooms.append(room)
                    print("{} {} created".format(room.room_name, room.purpose))
                    return "Room Created"
                # creates Livingspace if purpose is livingspace
                elif purpose.upper() == "LIVINGSPACE":
                    room = LivingSpace(room_name.upper())
                    self.living_spaces.append(room)
                    self.rooms.append(room)
                    print("{} {} created".format(room.room_name, room.purpose))
                    return "Room Created"
                    # Prints a prompt if purpose is not a valid purpose
                else:
                    print("{} is not a valid room type.".format(purpose))
        # Prints a prompt if room_name is not an integer
        else:
            print("Room names should be strings")
            return "Room names should be strings"

    def add_person(self, first_name, second_name, role, wants_accomodation):
        """Check if the names provided are strings before proceeding"""
        if (isinstance(first_name, str) and isinstance(second_name, str)):
            # Changes all the names passed into uppercase and join them
            person_name = first_name.upper() + " " + second_name.upper()
            # Creates a list of people allocated rooms
            # and filter it with the persons name to check if he/she
            # was allocated a room
            allocated = [allocated for allocated in self.allocated
                         if person_name.upper() == allocated.
                         person_name.upper()]
            # Creates a list of of people not allocated rooms
            # and filter it with the persons name to check if he/she
            # was not allocated a room
            unallocated = [unallocated for unallocated in self.unallocated
                           if person_name.upper() == unallocated.
                           person_name.upper()]
            person = allocated or unallocated
            # If a person is found in allocated or unallocated room list
            # it prints the prompt bellow
            if person:
                print("{} Exists in Dojo.".format(person_name))
                return "{} Exists in Dojo.".format(person_name)

            # If a person is not in allocated list and also not in
            # unallocated list, add person to the system
            else:
                # If a person is a fellow and does not want living space
                # add him/her as fellow and dont provide living space
                if role.upper() == "FELLOW" and wants_accomodation == "N":
                    person = Fellow(person_name)
                    self.allocate_office(person)
                    return "Fellow Added"
                # If a person is a fellow and does not want living space
                # add him/her as fellow and provide living space
                elif role.upper() == "FELLOW" and wants_accomodation == "Y":
                    person = Fellow(person_name)
                    self.allocate_office(person)
                    self.allocate_living_space(person)
                    return "Fellow Added and LivingSpace Allocated"
                # If a person is a staff and does not want living space
                # add him/her as staff and dont provide living space
                elif role.upper() == "STAFF" and wants_accomodation == "N":
                    person = Staff(person_name)
                    self.allocate_office(person)
                    return "Staff Added"
                # If a person is a staff and does want living space
                # add him/her as staff and dont provide living space
                elif role.upper() == "STAFF" and wants_accomodation == "Y":
                    person = Staff(person_name)
                    self.allocate_office(person)
                    print("Staff Added and Allocated Office Only")
                    return "Staff Added and Allocated Office Only"
                # If role is not defined
                else:
                    print("either '{}' or '{}'is not a valid option."
                          .format(role, wants_accomodation))

        # If name is integer print and return the prompt bellow
        else:
            print("person's names should be strings")
            return "person's names should be strings"

    def allocate_office(self, person):
        """ This method allocates an office to a person"""
        try:
            # Check if there are offices with space and
            # if there are, allocate space
            if self.offices:
                room = [room for room in self.offices if len(
                    room.occupants) < 6]
                # randomly chooses an office
                office = random.choice(room)
                # Adds the person to the occupants list of the office
                office.occupants.append(person)
                # Adds the person to the allocated list
                self.allocated.append(person)
                print("{} allocated office {}".format(person.person_name,
                                                      office.room_name))
                return "Office Allocated"
            # If offices are full
            else:
                # does not assign office space and add the person
                # on a waiting list
                self.unallocated.append(person)

                print("No Office available now, {} placed in waiting list ".
                      format(person.person_name))
                return "No Office Available"
        except IndexError:
            self.unallocated.append(person)
            print("No Office available now, {} placed in waiting list ".
                  format(person.person_name))

    def allocate_living_space(self, person):
        try:
            # Check if there are living spaces with space
            # and if there are, allocate space
            if self.living_spaces:
                room = [room for room in self.living_spaces if len(
                    room.occupants) < 4]
                # randomly chooses a living space
                living = random.choice(room)
                # Adds the person to the occupants list of the office
                living.occupants.append(person)
                print("and allocated livingspace {}".format(living.room_name))
            # If living spaces are full
            else:
                # Doesnt allocate room but adds person on a witing list
                self.unallocated.append(person)
                print("No living space now, {} placed in waiting list"
                      .format(person.person_name))

        except IndexError:
            self.unallocated.append(person)
            print("No living space available now, {} placed in waiting list "
                  .format(person.person_name))

    def print_room(self, room_name):
        room = [room for room in self.rooms if room_name.upper() ==
                room.room_name.upper()]
        # if rooom exists print the occupants
        if room:
            room = room[0]
            print("\n{}'s OCCUPANTS".format(room.room_name.upper()))
            print("----" * 10)
            for person in room.occupants:
                print(person.person_name)
            print("----" * 10)
            return "Print room successful"
        # if room does not exist
        else:
            print("{} does not exist in dojo".format(room_name.upper()))
            return "Room does not exist"

    def print_unallocated(self, filename):
        """ Print a list of unallocated people """
        # check if anyone is in the unallocated list
        Unallocated = list(set(self.unallocated))
        if not self.unallocated:
            print("No Member in Unallocated")
            return "No Member in Unallocated"
        if filename:
            with open(filename, 'w') as f:
                print("\n UNALLOCATED MEMBERS")
                print("----" * 10)
                for person in Unallocated:
                    record = person.person_name + " "
                    record += person.role + " "
                    record += "\n"
                    print(record)
                    print("----" * 10)
                    f.write(record)
                print("operation success")
                return "operation success"

    def print_allocations(self, filename):
        if not self.rooms:
            print("No Rooms to Show")
            return "No Rooms"
        output = " "
        for room in self.rooms:
            if len(room.occupants):
                output += room.room_name.upper() + '\n'
                output += "--" * 60 + '\n'
                for occupant in room.occupants:
                    output += occupant.person_name + ", "
                output += ("\n\n")

        if filename:
            with open(filename, 'w') as f:
                f.write(output)
                print(output)
            print("operation sucessful")
            return "operation sucessful"

    def reallocate_person(self, first_name, last_name, room_name):
        """ method to reallocate a person to another room """
        try:
            person_name = first_name.upper() + " " + last_name.upper()
            # Assigns allocated variable a single element list containing
            # a persons object that has the same person_name property
            # like the one provide above if He/she has been allocated a room
            allocated = [allocated for allocated in self.allocated if
                         person_name.upper() == allocated.person_name.upper()]
            # Assighns room variable a single element  list containing the
            # room object that has the same room_name property like the one
            # provided if the room is already created.
            room = [room for room in self.rooms if room_name.upper() ==
                    room.room_name.upper()]
            person = allocated
            # Check if a person is on the system
            if not person:
                print("Add {} to Dojo first".format(person_name))
                return "Add {} to Dojo first".format(person_name)
            # check if the room exists
            elif not room:
                print("{} is not a room in Dojo".format(room_name))
                return "{} is not a room in Dojo".format(room_name)
            # Check if the person is already an occupant in that room
            elif [occupant for occupant in room[0].occupants
                  if person_name == occupant.person_name]:
                print("{} is already in {}".format(
                    person_name, room[0].room_name))
                return "{} is already in {}".format(person_name,
                                                    room[0].room_name)
            # Check if room has space available
            elif (room[0].purpose == "office" and len(room[0].occupants) == 6):
                print("{} is full.".format(room[0].room_name))
                return "Room is Full"

            elif (room[0].purpose == "living_space" and
                  len(room[0].occupants) == 4):
                print("{} is full.".format(room[0].room_name))
                return"Room is Full"

            else:
                # Finds occupants current room
                current_room = [room for room in self.rooms if person[
                    0] in room.occupants]
                # Checks if occupant's current room is the same as the one
                # that he is to be reallocated then reallocates occupant
                if current_room[0].purpose == room[0].purpose:
                    room[0].occupants.append(person[0])
                    current_room[0].occupants.remove(person[0])
                    person[0].current_room = room[0].room_name
                    print("{} was moved from {} to {}".format(
                        person[0].person_name, current_room[0].room_name,
                        room[0].room_name))
                    return "Reallocated Successfully"

                else:
                    print("Can Only Reallocate to Room with" +
                          "Purpose as Current Room")
                    return "Choose Appropriate Room Type"
        except Exception as e:
            print("Error Occured, Try Later")

    def load_people(self, filename):
        """ This method adds people to rooms from a text file """

        try:
            if filename:  # check if file exists
                try:
                    with open(filename, 'r') as f:  # opens file
                        # read lines and save in list called people
                        people = f.readlines()
                    # iterate through each element in the list and load them
                    for person in people:
                        params = person.split() + ["N"]
                        self.add_person(params[0], params[
                                        1], params[2], params[3])
                    print("People Successfully Loaded")
                    return "People Successfully Loaded"

                except IndexError:
                    print("Data not consistent")
                    return "Data not consistent"
        except FileNotFoundError:
            print("File Not Found")
            return "File Not Found"

    def save_state(self, database_name="dojo_database.db"):
        """ method to save all data in the app into SQLite database """

        try:
            if database_name:
                engine = create_engine('sqlite:///{}'.format(database_name))
                Base.metadata.create_all(engine)
            else:
                engine = create_engine('sqlite:///dojo_database.db')
                Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()

            for table in Base.metadata.sorted_tables:
                session.execute(table.delete())
                session.commit()
            all_people = list(set(self.allocated + self.unallocated))
            for person in all_people:
                rooms_allocated = " "
                for room in self.rooms:
                    if person in room.occupants:
                        rooms_allocated += room.room_name + "  "
                person = People(Name=person.person_name, Role=person.role,
                                Room_allocated=rooms_allocated)
                session.add(person)

            for room in self.rooms:
                people = " "
                for occupant in room.occupants:
                    people += occupant.person_name + "  "
                room = Rooms(Name=room.room_name,
                             Purpose=room.purpose, Occupants=people)

                session.add(room)
            session.commit()
            session.close()
            print("Data Saved Successfully")
            return "Data Saved"
        except exc.SQLAlchemyError:
            session.rollback()
            print("Error Saving to DB")

    def load_state(self, database_name):
        """ method to load data from database into the app """

        try:
            engine = create_engine('sqlite:///{}'.format(database_name))
            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()

            # Load room data
            Query = session.query(Rooms.Name, Rooms.Purpose, Rooms.Occupants)
            for room_name, purpose, occupants in Query:
                individuals = occupants.split("  ")
                individuals.remove("")
                if purpose == "office":
                    room = Office(room_name)
                    for individual in individuals:
                        person = Person(individual)
                        room.occupants.append(person)
                    self.offices.append(room)
                    self.rooms.append(room)
                elif purpose == "living_space":
                    room = LivingSpace(room_name)
                    for individual in individuals:
                        person = Person(individual)
                        room.occupants.append(person)
                    self.living_spaces.append(room)
                    self.rooms.append(room)

            # Load People data
            Query = session.query(People.Name,
                                  People.Role, People.Room_allocated)
            for person_name, role, rooms_allocated in Query:
                number = len(rooms_allocated.split("  "))
                if role == "FELLOW":
                    person = Fellow(person_name)
                    if number == 3:
                        self.allocated.append(person)
                    elif number == 2:
                        self.unallocated.append(person)
                        self.allocated.append(person)
                    else:
                        self.unallocated.append(person)
                else:
                    person = Staff(person_name)
                    if number == 2:
                        self.allocated.append(person)
                    else:
                        self.unallocated.append(person)

            print("Data Successfully Loaded to App")
            return "Data Successfully Loaded to App"

        except exc.SQLAlchemyError:
            print("Invalid database name")
            return "Invalid Database Name"
