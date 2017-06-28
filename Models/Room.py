from abc import ABCMeta, abstractmethod

"""class Room"""


class Room(object):

    # making class person an abstract class.
    __metaclass__ = ABCMeta

    def __init__(self, room_name=" ", purpose=None,
                 max_capacity=None, occupants=[]):
        self.room_name = room_name
        self.purpose = purpose
        self.max_capacity = max_capacity
        self.occupants = []
"""class office a subclass of Room"""


class Office(Room):

    def __init__(self, room_name=" ", purpose="office", occupants=[],
                 max_capacity=6):
        # instanceiated super class room
        Room.__init__(self, room_name, purpose,
                      occupants, max_capacity)
        self.purpose = "office"
        self.max_capacity = 6


# class LivingSpace a subclass of Room
class LivingSpace(Room):

    def __init__(self, room_name=" ", purpose="living_space",
                 occupants=[], max_capacity=4):
        # instanceiated super class Room
        Room.__init__(self, room_name, purpose,
                      occupants, max_capacity)
        self.purpose = "living_space"
        self.max_capacity = 4
