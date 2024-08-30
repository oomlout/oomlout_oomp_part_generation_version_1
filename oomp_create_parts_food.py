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
        part_details["description_main"] = ""
        part_details["description_extra"] = "800_mm_width_2370_mm_height_280_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "591_822_01"
        part_details["width"] = "800 mm"
        part_details["height"] = "2370 mm"
        part_details["depth"] = "280 mm"
        parts.append(part_details)






        

    




    
    oomp.add_parts(parts, **kwargs)
    