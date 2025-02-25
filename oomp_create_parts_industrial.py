import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    

    parts = []

    part_details = {}
    part_details["classification"] = "industrial"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = copy.deepcopy(part_details)

    #mixeds
    if True:
        types = [""]

        for type in types:
            part_details = copy.deepcopy(default_empty)        
            part_details["type"] = type            
            part_details["description_main"] = "mixed"
            parts.append(part_details)

    


    oomp.add_parts(parts, make_files=make_files)
    