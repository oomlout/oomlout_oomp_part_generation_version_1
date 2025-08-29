import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "camping"
    part_details["type"] = ""
    part_details["color"] = ""
    part_details["size"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""


    current_default = copy.deepcopy(part_details)

    #tent
    if True:
        part_details = current_default.copy()
        part_details["type"] = "tent"
        current_default = part_details.copy()
        
        colors = ["tent", "tent_peg"]
        for color in colors:
            part_details = copy.deepcopy(current_default)
            part_details["color"] = color
            part_details["size"] = ""
            part_details["description_main"] = ""
            part_details["description_extra"] = ""
            parts.append(part_details.copy())

    #sleeping bag
    if True:
        part_details = current_default.copy()
        part_details["type"] = "sleeping_bag"
        current_default = part_details.copy()

        colors = ["double", "single"]

        for color in colors:
            part_details = copy.deepcopy(current_default)
            part_details["color"] = color
            part_details["size"] = ""
            part_details["description_main"] = ""
            part_details["description_extra"] = ""
            parts.append(part_details.copy())

    #kitchen
    if True:
        part_details = current_default.copy()
        part_details["type"] = "kitchen"
        current_default = part_details.copy()

        colors = ["cookware", "utensils", "plate", "cup", "bowl", "cutting_board", "knife"]

        for color in colors:
            part_details = copy.deepcopy(current_default)
            part_details["color"] = color
            part_details["size"] = ""
            part_details["description_main"] = ""
            part_details["description_extra"] = ""
            parts.append(part_details.copy())

    
    
            


   
    oomp.add_parts(parts, **kwargs)
    