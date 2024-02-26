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
    part_details["classification"] = "mechanical"
    part_details["type"] = "motor_geared"
    part_details["size"] = ["tt"]
    part_details["color"] = [""]
    part_details["description_main"] = "standard"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    parts.append(part_details)    
    
    #motor_stepper
    part_details = {}
    part_details["classification"] = "mechanical"
    part_details["type"] = "motor_stepper"
    part_details["size"] = ["nema_17"]
    part_details["color"] = [""]
    part_details["description_main"] = "42_mm_width_42_mm_height_48_mm_depth"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    parts.append(part_details)    
    

    # motor_with_encoder
    #      

    # motor_with_encoder
    #      cricut_maker_compatible
    part_details = {}
    part_details["classification"] = "mechanical"
    part_details["type"] = "motor_with_encoder"
    part_details["size"] = ["30_mm_diameter"]
    part_details["color"] = [""]
    part_details["description_main"] = "cricut_maker_compatible"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    parts.append(part_details)    


    


    oomp.add_parts(parts, make_files=make_files)
    