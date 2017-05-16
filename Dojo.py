from Models.person import Person, Fellow, Staff
from Models.Room import Room, Office, LivingSpace


#class dojo as our controlre
class Dojo(object):
    def __init__(self):
        self.rooms = []
        self.offices = []
        self.living_spaces = []
        self.allocated = []
        self.unallocated = []

     # creates a new room if one with the same name and purpose exists
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
                if purpose == "OFFICE" or purpose == "office":
                    room = Office(room_name.upper())
                    self.offices.append(room)
                    self.rooms.append(room)
                    print("{} {} created".format(room.room_name, room.purpose))
                    return "Room Created"
                # creates Livingspace if purpose is livingspace
                elif purpose == "LIVINGSPACE" or purpose == "livingspace":
                    room = LivingSpace(room_name.upper())
                    self.living_spaces.append(room)
                    self.rooms.append(room)
                    print("{} {} created".format(room.room_name, room.purpose))
                    return "Room Created"
                    # Prints a prompt if purpose is not a valid purpose\
                else:
                    print("{} is not a valid room type.".format(purpose))
        # Prints a prompt if room_name is not an integer
        else:
            print("Room names should be strings")
            return "Room names should be strings"
