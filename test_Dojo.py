from unittest import TestCase
from Dojo import Dojo
class TestDojo(TestCase):
	def setUp(self):
		# create an instance of class Dojo
		self.dojo = Dojo()
	def test_create_room(self):
		#Test if room is succesfully created
		self.assertEqual(self.dojo.create_room("Nairobi", "OFFICE"),
			"Room Created")
		self.assertEqual(self.dojo.create_room("Mombasa", "LIVINGSPACE"),
			"Room Created")

	def test_room_only_created_once(self):
		#Test for room duplication
		self.dojo.create_room("Eldoret", "OFFICE")
		self.assertEqual(self.dojo.create_room("Eldoret", "OFFICE"),
    		"{} already exists in dojo.".format("Eldoret"))

	def test_if_room_name_is_valid(self):
		#Test valid room name
		self.assertEqual(self.dojo.create_room(
			123, "OFFICE"), "Room names should be strings")

	def test_add_person(self):
		#test for adittion of a person or persons
		self.dojo.create_room("Accra", "OFFICE")
		self.dojo.create_room("Bujumbura", "LIVINGSPACE")
		self.assertEqual(self.dojo.add_person("Denis", "Juma", "STAFF",
			"N"), "Staff Added")
		self.assertEqual(self.Dojo.add_person("Denis", "Kola", "FELLOW",
			"N"), "Fellow Added")
		self.assertEqual(self.dojo.add_person("Victor", "Wamocha", "FELLOW",
			"Y"),"Fellow Added and LivingSpace Allocated")

	def test_add_duplicating_person(self):
		#Test if person is  added once
		self.dojo.add_person("CHRISTINE", "JUMA", "STAFF", "N")
		self.assertEqual(self.dojo.add_person("Christine", "Juma", "STAFF", "N"),
			"{} Exists in Amity.".format("CHRISTINE JUMA"))
	def test_if_person_name_is_valid(self):
		#Test if person name is valid
		self.assertEqual(self.dojo.add_person(123, 123, "STAFF", "N"),
			"person's names should be strings")







