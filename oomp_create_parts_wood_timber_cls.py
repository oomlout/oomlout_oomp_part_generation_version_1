import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    # 3x2
    part_details = {}
    part_details["classification"] = "wood"
    part_details["type"] = "timber_cls"
    part_details["size"] = ["38_mm_width_63_mm_height_2400_mm_depth"]
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ["three by two", "3x2", "two by three", "2x3"]
    parts.append(part_details)

    
    # 4x2 timber cls
    part_details = {}
    part_details["classification"] = "wood"
    part_details["type"] = "timber_cls"
    part_details["size"] = ["38_mm_width_89_mm_height_2400_mm_depth"]
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = [""]    
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ["four by two", "4x2", "two by four", "2x4"]
    parts.append(part_details)


    

    
    oomp.add_parts(parts, **kwargs)
    