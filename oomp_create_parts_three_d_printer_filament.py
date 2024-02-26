import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    # motor_geared
    #      tt
    part_details = {}
    part_details["classification"] = "three_d_printer"
    part_details["type"] = "filament"
    part_details["size"] = ["1_75_mm"]
    part_details["color"] = ["pla_aqua", "pla_plus_black"]
    part_details["description_main"] = "reel"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "3dqf"
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    parts.append(part_details)    
    
    


    oomp.add_parts(parts, make_files=make_files)
    