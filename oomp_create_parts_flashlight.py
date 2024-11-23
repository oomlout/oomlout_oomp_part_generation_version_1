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
        part_details["classification"] = "flashlight"
        part_details["type"] = ""
        part_details["size"] = "cob_led"
        part_details["color"] = ""
        part_details["description_main"] = "45_mm_width_61_mm_length"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)



        

    




    
    oomp.add_parts(parts, **kwargs)
    