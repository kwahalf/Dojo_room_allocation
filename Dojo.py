import random
from Models.person import Person, Fellow, Staff
from Models.Room import Room, Office, LivingSpace


class Dojo(object):
    def __init__(self):
        self.rooms = []
        self.offices = []
        self.living_spaces = []
        self.allocated = []
        self.unallocated = []

    def create_room(self, room_name, purpose):
        #checks room_name and purpose are strings
        if (isinstance(room_name, str) and isinstance(purpose, str)):
            #checks if room is already allocated
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
        # Check if the names provided are strings before proceeding
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
        # check if
        if not self.unallocated:
            print("No Member in Unallocated")
            return "No Member in Unallocated"
        if filename:
            with open(filename, 'w') as f:
                print("\n UNALLOCATED MEMBERS")
                print("----" * 10)
                for person in self.unallocated:
                    person_name = "\n" + person.person_name
                    print(person_name)
                    print("----" * 10)
                    f.write(person_name)
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
                print (output)
            print("operation sucessful")
            return "operation sucessful"

