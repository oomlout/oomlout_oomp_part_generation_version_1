import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    # ikea
    #   billy
    if True:
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = ["ikea_billy"]
        part_details["color"] = ["white"]
        part_details["description_main"] = "800_mm_width_2370_mm_height_280_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "591_822_01"
        part_details["width"] = "800 mm"
        part_details["height"] = "2370 mm"
        part_details["depth"] = "280 mm"
        parts.append(part_details)


        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = ["ikea_billy"]
        part_details["color"] = ["white"]
        part_details["description_main"] = "800_mm_width_2020_mm_height_280_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "002_638_50"
        part_details["width"] = "800 mm"
        part_details["height"] = "2020 mm"
        part_details["depth"] = "280 mm"
        parts.append(part_details)

        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = ["ikea_billy"]
        part_details["color"] = ["white"]
        part_details["description_main"] = "800_mm_width_2020_mm_height_400_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "904_019_32"
        part_details["width"] = "800 mm"
        part_details["height"] = "2020 mm"
        part_details["depth"] = "400 mm"
        parts.append(part_details)


        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = ["ikea_billy"]
        part_details["color"] = ["white"]
        part_details["description_main"] = "400_mm_width_2020_mm_height_280_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "502_638_38"
        part_details["width"] = "400 mm"
        part_details["height"] = "2020 mm"
        part_details["depth"] = "280 mm"
        parts.append(part_details)


        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = ["ikea_billy"]
        part_details["color"] = ["white"]
        part_details["description_main"] = "800_mm_width_1060_mm_height_280_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "302_638_44"
        part_details["width"] = "800 mm"
        part_details["height"] = "1060 mm"
        part_details["depth"] = "280 mm"
        parts.append(part_details)

        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = ["ikea_billy"]
        part_details["color"] = ["white"]
        part_details["description_main"] = "400_mm_width_1060_mm_height_280_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "802_638_32"
        part_details["width"] = "400 mm"
        part_details["height"] = "1060 mm"
        part_details["depth"] = "280 mm"
        parts.append(part_details)

        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf_extender"
        part_details["size"] = ["ikea_billy"]
        part_details["color"] = ["white"]
        part_details["description_main"] = "800_mm_width_350_mm_height_280_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "402_638_53"
        part_details["width"] = "800 mm"
        part_details["height"] = "350 mm"
        part_details["depth"] = "280 mm"
        parts.append(part_details)

    #   havsta
    if True:    
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "cabinet"
        part_details["size"] = ["ikea_havsta"]
        part_details["color"] = ["white"]
        part_details["description_main"] = "810_mm_width_890_mm_height_470_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "005_292_42"
        part_details["width"] = "810 mm"
        part_details["height"] = "890 mm"
        part_details["depth"] = "470 mm"
        parts.append(part_details)

    




    




    
    oomp.add_parts(parts, **kwargs)
    