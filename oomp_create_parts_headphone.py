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

    #bose
    if True:
        part_details = copy.deepcopy(default_empty)
        part_details["type"] = "bose_qc35"
        part_details["description_main"] = "main"        
        part_details["manufacturer"] = "bose"
        part_details["part_number"] = "qc35"
        parts.append(part_details)





    oomp.add_parts(parts, make_files=make_files)
    