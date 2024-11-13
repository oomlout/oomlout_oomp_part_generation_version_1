import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    # kite packaging plain
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "bag_grip_seal"
    part_details["size"] = ["45_micron_thickness"]
    part_details["color"] = ["clear"]
    part_details["description_main"] = "88_mm_width_114_mm_height"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "kite_packaging"
    part_details["part_number"] = "pbr3_5_x_4_5_kite"
    part_details["short_name"] = ""  
    part_details["cost_per"] = "£0.007"
    part_details["cost_per_10"] = "£0.0244"
    part_details["cost_per_1000"] = "£0.007"
    part_details["link_purchase"] = ["kitepackaging.co.uk/scp/resealable-grip-seal-bags/plain-grip-seal-bags/"]
    part_details["width_internal"] = ["88 mm"]
    part_details["height_internal"] = ["114 mm"]
    parts.append(part_details)    
    
    # kite packaging premium
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "bag_grip_seal"
    part_details["size"] = ["75_micron_thickness"]
    part_details["color"] = ["clear"]
    part_details["description_main"] = "88_mm_width_114_mm_height"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "kite_packaging"
    part_details["part_number"] = "pbrh3_5_x_4_5"
    part_details["short_name"] = ""  
    part_details["cost_per"] = "£0.0172"
    part_details["cost_per_10"] = "£0.0315"
    part_details["cost_per_1000"] = "£0.0172"
    part_details["link_purchase"] = ["https://www.kitepackaging.co.uk/scp/resealable-grip-seal-bags/heavy-duty-grip-seal-bags/"]
    part_details["width_internal"] = ["88 mm"]
    part_details["height_internal"] = ["114 mm"]
    parts.append(part_details)    
    

    #oomlout
    if True:
        part_details = {}
        part_details["classification"] = "packaging"
        part_details["type"] = "bag_grip_seal"
        part_details["size"] = ["100_micron_thickness"]
        part_details["color"] = ["clear_front_silver_back"]
        part_details["description_main"] = "115_mm_width_170_mm_height"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  
        parts.append(part_details)    
        

    oomp.add_parts(parts, make_files=make_files)
    