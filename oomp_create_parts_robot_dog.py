import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "robot_dog"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = part_details.copy()

    
    #unitree
    if True:
        
        current = {}
        current["type"] = "unitree"
        current["size"] = "go2"
        description_mains = []
        description_mains.append("air")
        description_mains.append("pro")
        description_mains.append("x")
        description_mains.append("edu")
        description_mains.append("controller")

        for description_main in description_mains:
            part_details = copy.deepcopy(default_empty)
            part_details.update(current)
            part_details["description_main"] = description_main
            parts.append(part_details)

        
        
            


   
    oomp.add_parts(parts, **kwargs)
    