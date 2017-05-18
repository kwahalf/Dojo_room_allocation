# Dojo_room_allocation
Dojo is an app used to register and allocate rooms randomly to Andelans. Each Andelan must be assigned an office and only Fellows are elegible to be allocated living spaces

# Instalation:

$ md Dojo
$ cd Dojo
$ git clone https://github.com/kwahalf/Dojo_room_allocation
$ cd Dojo_room_allocation

# Install Requirements

 pip install requierd pacakes listed in requirements.txt

# Start the app on the terminal

  AppView.py -i
  
# The App has the following functionalities:

create_room (<room_type>)(<room_name> )...
Takes two arguments for an instance i.e room_name and purpose. Multiple rooms can also be created at the same time

create_room kabete office
create_room kitale office bungoma office kakamega livingspace

add_person <first_name> <second_name> <FELLOW|STAFF> [wants_accommodation]
Adds a fellow or staff into the application by providing the first_name, second_name, role or wants_accomodation

add_person Denis Juma fellow --a=Y
add_person Victor wamocha fellow --a=N
add_person Christine Juma staff

print_room <room_name>
This command prints the room name and the names of occupants in the room

print_room kakamega
