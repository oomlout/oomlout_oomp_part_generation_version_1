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
        part_details["type"] = "table"
        part_details["size"] = "oomlout"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = "2440_mm_width_1220_mm_height"
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)



        

    




    
    oomp.add_parts(parts, **kwargs)
    