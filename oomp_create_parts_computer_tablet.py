import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    

    parts = []

    part_details = {}
    part_details["classification"] = "computer_tablet"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = copy.deepcopy(part_details)

    #kindle paperwhite
    if True:
        part_details = copy.deepcopy(default_empty)        
        part_details["type"] = "kindle_paperwhite"
        part_details["size"] = ""        
        part_details["manufacturer"] = "amazon"        

        generations = ["1","2","3","4","5","6","7","8","9","10","11"]

        for generation in generations:
            part_details = copy.deepcopy(part_details)
            part_details["description_main"] = f"{generation}_generation"
            parts.append(part_details)

        



    oomp.add_parts(parts, make_files=make_files)
    