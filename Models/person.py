from abc import ABCMeta, abstractmethod


# Class Person
class Person(object):
    # making class person an abstract class.
    __metaclass__ = ABCMeta

    def __init__(self, person_name, person_id=None,
                 role=None, wants_accomodation=None):
        self.person_name = person_name
        self.id = person_id
        self.role = role
        self.wants_accomodation = wants_accomodation


#Class Fellow inherits from class person
class Fellow(Person):
    def __init__(self, person_name, person_id=None,
                 role="FELLOW", wants_accomodation=""):
        # instanceiated super class Person
        Person.__init__(self, person_name, person_id, wants_accomodation)
        self.role = "FELLOW"


#Class Staff inherits from class person
class Staff(Person):
    def __init__(self, person_name, person_id=None,
                 role="STAFF", wants_accomodation="N"):
        # instanceiated super class Person
        Person.__init__(self, person_name, person_id, wants_accomodation)
        self.role = "STAFF"
        self.wants_accomodation = "N"
