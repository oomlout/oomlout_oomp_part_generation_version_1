import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    # tinware tins
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "tin_hinged_lid"
    part_details["size"] = ["169_mm_width_130_mm_height_18_mm_depth_350_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "tinware_direct"
    part_details["part_number"] = "t4066"        
    part_details["price_1"] = "£0.79"    
    part_details["price_10"] = "£0.79"    
    part_details["price_current"] = "£0.79"
    part_details["link_purchase"] = ["https://tinwaredirect.com/products/silver-rectangular-stationery-tins-with-hinged-lid?variant=1726837358619"]
    part_details["width_internal"] = ["165 mm"]
    part_details["height_internal"] = ["124 mm"]
    part_details["depth_internal"] = ["18 mm"]
    parts.append(part_details)    


    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "tin_hinged_lid"
    part_details["size"] = ["a5_220_mm_width_160_mm_height_25_mm_depth_450_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "tinware_direct"
    part_details["part_number"] = "t4005"        
    part_details["price_1"] = "£1.25"
    part_details["price_10"] = "£1.25"    
    part_details["price_current"] = "£1.25"
    part_details["link_purchase"] = ["https://tinwaredirect.com/products/silver-rectangular-stationery-tins-with-hinged-lid?variant=1726838210587"]
    part_details["width_internal"] = ["215 mm"]
    part_details["height_internal"] = ["156 mm"]
    part_details["depth_internal"] = ["21 mm"]
    parts.append(part_details)    
    

    #shop bought ones

    # quality street 2024
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "tin_plastic"
    part_details["size"] = ["octagon_225_mm_width_225_mm_height_80_mm_depth_2500_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "quality_street"
    part_details["part_number"] = "2024"        
    part_details["price_1"] = ""
    part_details["price_10"] = ""    
    part_details["price_current"] = ""
    part_details["link_purchase"] = [""]
    part_details["width_internal"] = ["214 mm"]
    part_details["height_internal"] = ["214 mm"]
    part_details["depth_internal"] = ["70 mm"]
    parts.append(part_details)    
    


    oomp.add_parts(parts, make_files=make_files)
    