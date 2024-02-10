import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    # surface pros
    #define a part 
    part_details = {}
    part_details["classification"] = "computer"
    part_details["type"] = "tablet"
    part_details["size"] = ["microsoft_surface"]
    part_details["color"] = [""]
    part_details["description_main"] = ["pro_3","pro_7","pro_5"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    parts.append(part_details)

    #webcams
    part_details = {}
    part_details["classification"] = "computer"
    part_details["type"] = "webcam"
    part_details["size"] = ["external"]
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "microsoft"
    part_details["part_number"] = "hd_3000"
    parts.append(part_details)


    

    
    oomp.add_parts(parts, **kwargs)
    