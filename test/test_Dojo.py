#!/usr/bin/python3
import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import random

from ..Dojo import Dojo



class TestDojo(unittest.TestCase):
    def setUp(self):
        # create an instance of class Dojo
        self.dojo = Dojo()

    def test_create_room(self):
        # Test if room is succesfully created
        self.assertEqual(self.dojo.create_room("Nairobi", "OFFICE"),
                         "Room Created")
        self.assertEqual(self.dojo.create_room("Moyale", "LIVINGSPACE"),
                         "Room Created")

    def test_Create_room_room_only_created_once(self):
        # Test for room duplication
        self.dojo.create_room("Eldoret", "OFFICE")
        self.dojo.create_room("Kampala", "OFFICE")
        self.assertEqual(self.dojo.create_room("eldoret", "OFFICE"),
                         "{} already Exists in Dojo.".format("ELDORET"))

    def test_create_room_room_name_is_a_string(self):
        # Test valid room name
        self.assertEqual(self.dojo.create_room(
                         890, "OFFICE"), "Room names should be strings")

    def test_add_person(self):
        # test for adittion of a person or persons
        self.dojo.create_room("Accra", "OFFICE")
        self.dojo.create_room("Bujumbura", "LIVINGSPACE")
        self.assertEqual(self.dojo.add_person("Denis", "Juma", "STAFF",
                         "N"), "Staff Added")
        self.assertEqual(self.dojo.add_person("Denis", "Kola", "FELLOW",
                         "N"), "Fellow Added")
        self.assertEqual(self.dojo.add_person("Victor", "Wamocha", "FELLOW",
                         "Y"), "Fellow Added and LivingSpace Allocated")

    def test_add_person_duplicating_person(self):
        # Test if person is  added once even if the names are in diffrent cases
        self.dojo.add_person("CHRISTINE", "JUMA", "STAFF", "N")
        self.assertEqual(self.dojo.add_person("Christine", "Juma", "STAFF",
                         "N"),
                         "{} Exists in Dojo.".format("CHRISTINE JUMA"))

    def test_if_person_name_is_a_string(self):
        # Test if person name is valid
        self.assertEqual(self.dojo.add_person(678, 123, "STAFF", "N"),
                         "person's names should be strings")

    def test_staff_gets_accomodation(self):
        # Test if staff can be given accomodation
        self.dojo.create_room("BUSIA", "OFFICE")
        self.dojo.create_room("bungoma", "LIVINGSPACE")
        self.assertEqual(
            self.dojo.add_person("Sharon", "Akinyi", "STAFF",
                                 "Y"),
            "Staff Added and Allocated Office Only")

    def test_print_room_existing_room(self):
        # test if an existing room can be printed
        self.dojo.create_room("Kangundo", "OFFICE")
        self.assertEqual(self.dojo.print_room("Kangundo"),
                         "Print room successful")

    def test_print_room_nonexisting_room(self):
        # test if a non existing room can be printed
        self.assertEqual(self.dojo.print_room("Kirinyaga"),
                         "Room does not exist")

    def test_print_allocations_to_file(self):
        # Test that Allocated rooms can be printed to specified file name
        self.dojo.create_room("Voi", "OFFICE")
        self.dojo.add_person("Martin", "Katami", "STAFF", "N")
        self.assertEqual(self.dojo.print_allocations(
            "data.txt"), "operation sucessful")

    def test_print_allocations_while_there_are_no_rooms(self):
        # Test that allocations not printed if no rooms available in Dojo
        self.assertEqual(self.dojo.print_allocations("data.txt"), "No Rooms")

    def test_print_unallocated_with_no_members_unallocated(self):
        # Test that unallocated list is not printed
        # if no members are available"
        self.dojo.create_room("Malaba", "OFFICE")
        self.dojo.add_person("Sylvia", "Makinia", "STAFF", "N")
        self.dojo.add_person("James", "Mambo", "fellow", "N")
        self.assertEqual(self.dojo.print_unallocated(self),
                         "No Member in Unallocated")

    def test_realocate_person_not_in_Dojo(self):
        # Test if a person not in Dojo can be reallocated
        self.dojo.create_room("DONHOLM", "OFFICE")
        self.assertEqual(self.dojo.reallocate_person("PETTER", "KENETH",
                                                     "DONHOLM"),
                         "Add {} to Dojo first".format("PETTER KENETH"))

    def test_reallocate_person_to_unavailable_room(self):
        # Test IF person can  be reallocated to unavailable room
        self.dojo.create_room("NAIROBI", "OFFICE")
        self.dojo.add_person("ALPHA", "KIGEN", "STAFF", "N")
        self.assertEqual(self.dojo.reallocate_person("ALPHA", "KIGEN",
                         "CAIRO"),
                         "{} is not a room in Dojo".format("CAIRO"))

    def test_reallocate_is_successful(self):
        # Test if person is successfully reallocated
        self.dojo.create_room("KITUI", "OFFICE")
        self.dojo.add_person("Denis", "Kwanusu", "STAFF", "N")
        self.dojo.create_room("Bomas", "OFFICE")
        self.assertEqual(self.dojo.reallocate_person(
                         "DENIS", "KWANUSU", "BOMAS"),
                         "Reallocated Successfully")

    def test_reallocate_to_appropriate_room_type(self):
        # Test person reallocated to room type as current room
        self.dojo.create_room("Accra", "OFFICE")
        self.dojo.add_person("DENIS", "KWANUSU", "STAFF", "N")
        self.dojo.create_room("Unono", "LIVINGSPACE")
        self.assertEqual(self.dojo.reallocate_person(
                         "DENIS", "KWANUSU", "UNONO"),
                         "Choose Appropriate Room Type")

    def test_reallocate_person_to_same_room(self):
        # Test when person is reallocated to same room
        self.dojo.create_room("Accra", "OFFICE")
        self.dojo.add_person("DENIS", "KWANUSU", "STAFF", "N")
        self.assertEqual(self.dojo.reallocate_person(
                         "DENIS", "KWANUSU", "Accra"),
                         "DENIS KWANUSU is already in ACCRA")

    def test_reallocate_from_office_to_livingspace(self):
        # Test that member can not be reallocated from office
        # to livingspace and vice versa
        self.dojo.create_room("Accra", "OFFICE")
        self.dojo.create_room("Unono", "LIVINGSPACE")
        self.dojo.add_person("DENIS", "KWANUSU", "STAFF", "N")
        self.assertEqual(self.dojo.reallocate_person(
                         "DENIS", "KWANUSU", "Unono"),
                         "Choose Appropriate Room Type")

    def test_reallocate_person_to_full_room(self):
        # Test that person can not be reallocated to already full room"""
        self.dojo.create_room("RAVIN", "OFFICE")
        self.dojo.add_person("MARTIN", "TUNGE", "FELLOW", "N")
        self.dojo.add_person("CHARLSE", "ODUK", "STAFF", "N")
        self.dojo.add_person("SHARON", "OWINO", "FELLOW", "N")
        self.dojo.add_person("GRACE", "KUKUBO", "FELLOW", "N")
        self.dojo.add_person("BOB", "COLIMORE", "STAFF", "N")
        self.dojo.add_person("BIBI", "TOP", "FELLOW", "N")
        self.dojo.create_room("AFRICA", "OFFICE")
        self.dojo.add_person("James", "Otieno", "FELLOW", "N")
        self.assertEqual(self.dojo.reallocate_person(
                         "James", "Otieno", "Ravin"), "Room is Full")

    def test_load_people_from_textfile(self):
        # Test if people are successfully loaded to the app from text file
        self.assertEqual(self.dojo.load_people(
                         "data1.txt"), "People Successfully Loaded")

    def test_load_people_from_inconsistent_textfile(self):
        # Test if you can load inconsistent data to app from text file
        self.assertEqual(self.dojo.load_people(
                         "people.txt"), "Data not consistent")

    def test_load_people_from_non_existing_textfile(self):
        # Test if you can load data to app from unexisting text file
        self.assertEqual(self.dojo.load_people("p.txt"), "File Not Found")

    def test_save_state_default_database(self):
        # Test data successfully saved to default database
        self.dojo.add_person("BOB", "COLIMORE", "STAFF", "N")
        self.dojo.add_person("BIBI", "TOP", "FELLOW", "N")
        self.dojo.create_room("AFRICA", "OFFICE")
        self.dojo.add_person("James", "Otieno", "FELLOW", "N")
        self.assertEqual(self.dojo.save_state(), "Data Saved")

    def test_save_state_valid_database(self):
        # Test data successfully loaded from default database to app
        self.dojo.add_person("BOB", "COLIMORE", "STAFF", "N")
        self.dojo.add_person("BIBI", "TOP", "FELLOW", "N")
        self.dojo.create_room("AFRICA", "OFFICE")
        self.dojo.add_person("James", "Otieno", "FELLOW", "N")
        self.assertEqual(self.dojo.save_state("dojo_test_database.db"),
                         "Data Saved")

    def test_load_state_from_valid_database(self):
        # Test data successfully loaded from specified database to app
        self.dojo.create_room("RAVIN", "OFFICE")
        self.dojo.add_person("MARTIN", "TUNGE", "FELLOW", "N")
        self.dojo.add_person("CHARLSE", "ODUK", "STAFF", "N")
        self.dojo.add_person("SHARON", "OWINO", "FELLOW", "N")
        self.dojo.save_state("dojo_test_database.db")
        self.assertEqual(self.dojo.load_state("dojo_test_database.db"),
                         "Data Successfully Loaded to App")

    def test_allocate_unallocated_office_works(self):
        """Test that it allocates people who are not allocated officess
            an office"""
        self.dojo.add_person("DAISY", "GUDA", "STAFF", "N")
        self.dojo.create_room("SHELL", "OFFICE")
        self.dojo.add_person("UHURU", "KENYATA", "FELLOW", "Y")
        self.assertEqual(self.dojo.allocate_unallocated_office("Daisy",
                         "Guda"), "DAISY GUDA allocated office SHELL")
        self.assertEqual(self.dojo.allocate_unallocated_office("Uhuru",
                         "Kenyata"), "UHURU KENYATA already has an OFFICE")

    def test_allocate_unallocated_office_not_allocate_not_in_dojo(self):
        """Test that it does not allocate people who are not in dojo
            offices"""
        self.dojo.create_room("SHELL", "OFFICE")
        self.assertEqual(self.dojo.allocate_unallocated_office("Fred",
                         "Orina"), "FRED ORINA is not in dojo")

    def test_allocate_unallocated_livingspace_works(self):
        """Test that it allocates people who are not allocated officess
            an office"""
        self.dojo.create_room("SHELL", "OFFICE")
        self.dojo.add_person("DAISY", "GUDA", "fellow", "Y")
        self.dojo.create_room("BAT", "LIVINGSPACE")
        self.dojo.add_person("UHURU", "KENYATA", "FELLOW", "Y")
        self.assertEqual(self.dojo.allocate_unallocated_livingspace("Daisy",
                         "Guda"), "DAISY GUDA allocated LIVINGSPACE BAT")
        self.assertEqual(self.dojo.allocate_unallocated_livingspace("Uhuru",
                         "Kenyata"), "UHURU KENYATA already has a LIVINGSPACE")

    def test_allocate_unallocated_livingspace_not_allocate_not_in_dojo(self):
        """Test that it does not allocate people who are not in dojo
            livingspaces"""
        self.dojo.create_room("SHELL", "LIVINGSPACE")
        self.assertEqual(self.dojo.allocate_unallocated_livingspace("Fred",
                         "Orina"), "FRED ORINA is not in dojo")


if __name__ == "__main__":
    unittest.main(exit=False)
