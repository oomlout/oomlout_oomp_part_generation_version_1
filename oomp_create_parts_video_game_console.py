import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "video_game_console"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = copy.deepcopy(part_details)

    types = []
    types.append("nintendo_entertainment_system")
    types.append("super_nintendo_entertainment_system")
    types.append("nintendo_64")
    types.append("nintendo_switch")
    types.append("playstation")    
    types.append("sega_genesis")
    description_mains = []
    description_mains.append("console")
    description_mains.append("controller")
    description_mains.append("controller_usb")
    description_extras = [""]

    for type in types:
        for description_main in description_mains:
            for description_extra in description_extras:
                part = copy.deepcopy(default_empty)
                part["type"] = type
                part["description_main"] = description_main
                part["description_extra"] = description_extra
                parts.append(part)





    oomp.add_parts(parts, make_files=make_files)
    