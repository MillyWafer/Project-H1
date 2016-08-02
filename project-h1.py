import names
import json
import re
import os
from colored import fg, attr

os.system("clear")

rooms_json = open("rooms.json").read()
rooms = json.loads(rooms_json)["rooms"]

characters_json = open("characters.json").read()
characters = json.loads(characters_json)["characters"]

objects_json = open("objects.json").read()
objects = json.loads(objects_json)["objects"]


def print_object(object_id):
    obj = "%s%s%s" % (fg("purple_4a"), objects[object_id]['name'],
                      attr("reset"))
    return obj


def match_object(match):
    object_id = int(match.group(1))
    return print_object(object_id)


def print_room(room_id):
    room = rooms[room_id]
    print "%s%s%s%s" % (fg("red_3b"), attr("bold"),
                        room['name'], attr("reset"))

    # replace {OBJXXX} with object name in short description
    sdescrip = re.sub("{OBJ(\d+)}", match_object, room['sdescrip'])

    print sdescrip
    
    space = True
    for character in characters:
        if character["room_id"] == room_id:
            if space == True:
                print
                space = False
            print "%s%s%s is here." % (fg(character["color"]),
                                       character["name"], attr("reset"))

    print
    print "%s%s%s" % (fg("turquoise_2"), "Exits:", attr("reset"))
    dirs = {
        "N": "North", "S": "South", "E": "East", "W": "West",
        "NE": "Northeast", "NW": "Northwest",
        "SE": "Southeast", "SW": "Southwest",
        "U": "Up", "D": "Down"
        }
    for exit in room["exits"]:
        print dirs[exit["dir"]]
    print

chip_clr = fg("pale_green_1b")
player_clr = fg("green_3b")

room_id = 0
name = names.get_name()
print ("%s\"Good morning, %s%s%s. Time to get ready for work.\"%s" %
       (chip_clr, player_clr, name, chip_clr, attr("reset")))

print "You wake up in Your Bedroom. Your Spousal Unit is still asleep."
prev_room_id = -1
while True:
    room = rooms[room_id]
    if prev_room_id != room_id:
        print_room(room_id)
        prev_room_id = room_id

    cmd = raw_input("%s%s%s: " % (player_clr, name, attr("reset")))
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
        # replace {OBJXXX} with object name in long description
        ldescrip = re.sub("{OBJ(\d+)}", match_object, room['ldescrip'])

        print ldescrip

    print
