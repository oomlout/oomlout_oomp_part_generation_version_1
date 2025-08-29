import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "scent"

    current_default = copy.deepcopy(oomp.default_part_details)

    #accesories, storage, scents
    types = []
    types.append("accesory")
    types.append("storage")
    types.append("scent")

    for typ in types:
        part_details = current_default.copy()
        part_details["type"] = typ
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)
    

    
    
            


   
    oomp.add_parts(parts, **kwargs)
    