import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    
    # panel_mount
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "button"
    part_details["size"] = ["11_mm"]
    part_details["color"] = ["panel_mount"]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)


    # surface_mount
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "button"
    part_details["size"] = ["3_5_mm_x_6_mm_x_2_5_mm"]
    part_details["color"] = ["surface_mount"]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)

    #switches
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "switch_slide"
    part_details["size"] = ["2_8_mm_x_8_mm_x_1_4_mm","2_54_header"]
    part_details["color"] = ["surface_mount"]
    part_details["description_main"] = "single_pole_double_throw"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)
    

    #keypad
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "button_keypad"
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = "16_key_118_5_mm_width_118_5_mm_height_11_mm_depth"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "storm_interface"
    part_details["part_number"] = "2k16t10"
    part_details["short_name"] = ""  
    part_details["link"] = "https://www.storm-interface.com/ixp/keypads/2000-series/2000-series-16-key-telephone.html"
    parts.append(part_details)



    oomp.add_parts(parts, make_files=make_files)
    