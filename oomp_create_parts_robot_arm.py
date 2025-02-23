import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    

    parts = []

    part_details = {}
    part_details["classification"] = "robot_arm"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = copy.deepcopy(part_details)

    #denso
    if True:
        part_details = copy.deepcopy(default_empty)        
        part_details["type"] = "denso"
        part_details["size"] = "vm_60b1d"
        part_details["description_main"] = "arm"
        parts.append(part_details)

    #controller
    part_details = {}
    part_details["classification"] = "robot_arm_controller"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = copy.deepcopy(part_details)

    #denso
    if True:
        part_details = copy.deepcopy(default_empty)        
        part_details["type"] = "denso"
        part_details["size"] = "rc5"
        part_details["description_main"] = "controller"
        parts.append(part_details)


    oomp.add_parts(parts, make_files=make_files)
    