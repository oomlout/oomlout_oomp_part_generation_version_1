import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    # amazon fire tablets
    part_details = {}
    part_details["classification"] = "camera"
    part_details["type"] = "cctv_dome"
    part_details["size"] = ["140_mm"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    parts.append(part_details)



    

    
    oomp.add_parts(parts, **kwargs)
    