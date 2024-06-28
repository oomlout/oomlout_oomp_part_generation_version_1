import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    base = {}
    base["classification"] = "paper"
    base["type"] = "sheet"    
    base["color"] = [""]
    base["description_main"] = ""
    base["description_extra"] = ""
    base["manufacturer"] = ""
    base["part_number"] = ""    

    # a sizes
    
    #a0
    part_details = base.copy()
    part_details["size"] = ["a0_841_mm_width_1189_mm_height"]
    part_details["width"] = "841 mm"
    part_details["height"] = "1189 mm"
    parts.append(part_details)

    #a1
    part_details = base.copy()
    part_details["size"] = ["a1_594_mm_width_841_mm_height"]
    part_details["width"] = "594 mm"
    part_details["height"] = "841 mm"
    parts.append(part_details)

    #a2
    part_details = base.copy()
    part_details["size"] = ["a2_420_mm_width_594_mm_height"]
    part_details["width"] = "420 mm"
    part_details["height"] = "594 mm"
    parts.append(part_details)

    #a3
    part_details = base.copy()
    part_details["size"] = ["a3_297_mm_width_420_mm_height"]
    part_details["width"] = "297 mm"
    part_details["height"] = "420 mm"
    parts.append(part_details)


    #a4
    part_details = base.copy()
    part_details["size"] = ["a4_210_mm_width_297_mm_height"]
    part_details["width"] = "210 mm"
    part_details["height"] = "297 mm"    
    parts.append(part_details)

    #a5
    part_details = base.copy()
    part_details["size"] = ["a5_148_mm_width_210_mm_height"]
    part_details["width"] = "148 mm"
    part_details["height"] = "210 mm"
    parts.append(part_details)

    #a6
    part_details = base.copy()
    part_details["size"] = ["a6_105_mm_width_148_mm_height"]
    part_details["width"] = "105 mm"
    part_details["height"] = "148 mm"
    parts.append(part_details)

    #a7
    part_details = base.copy()
    part_details["size"] = ["a7_74_mm_width_105_mm_height"]
    part_details["width"] = "74 mm"
    part_details["height"] = "105 mm"
    parts.append(part_details)

    #a8
    part_details = base.copy()
    part_details["size"] = ["a8_52_mm_width_74_mm_height"]
    part_details["width"] = "52 mm"
    part_details["height"] = "74 mm"
    parts.append(part_details)

    #poters
    
    # 460 mm x 640 mm
    part_details = base.copy()
    part_details["size"] = ["460_mm_width_640_mm_height"]
    part_details["width"] = "460 mm"
    part_details["height"] = "640 mm"
    parts.append(part_details)

    # 510 mm x 750 mm
    part_details = base.copy()
    part_details["size"] = ["510_mm_width_750_mm_height"]
    part_details["width"] = "510 mm"
    part_details["height"] = "750 mm"
    parts.append(part_details)


    oomp.add_parts(parts, **kwargs)
    