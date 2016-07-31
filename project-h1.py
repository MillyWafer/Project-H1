import names
import json
import os
from colored import fg, attr

os.system("clear")

rooms_json = open("rooms.json").read()
rooms = json.loads(rooms_json)["rooms"]


def print_room(room_id):
	room = rooms[room_id]
	print
	print "%s%s%s%s" % (fg("red_3b"), attr("bold"), room['name'], attr("reset"))
	print room['sdescrip']
	print
	print "%s%s%s" % (fg("turquoise_2"), "Exits:", attr("reset"))
	dirs = {
		"N": "North", "S": "South", "E": "East", "W": "West",
		"NE": "Northeast","NW": "Northwest", "SE": "Southeast", "SW": "Southwest",
		"U": "Up", "D": "Down"
		}
	for exit in room["exits"]:
		print dirs[exit["dir"]]
	print

room_id = 0
name = names.get_name()
print "\"Goodmorning, %s. Time to get ready for work.\"" % name
print "You wake up in Your Bedroom. Your spousal unit is still asleep."
while True:
	room = rooms[room_id]
	print_room(room_id)
	
	cmd = raw_input("%s%s%s: " % (fg("chartreuse_1"), name, attr("reset")))
	cmd = cmd.upper()
	cmd = cmd.replace("NORTH", "N")
	cmd = cmd.replace("SOUTH", "S")
	cmd = cmd.replace("EAST", "E")
	cmd = cmd.replace("WEST", "W")
	cmd = cmd.replace("LOOK", "L")

	for exit in room["exits"]:
		if cmd == exit["dir"]:
			room_id = exit["room_id"]
	if cmd == "L":
		print room['ldescrip']
