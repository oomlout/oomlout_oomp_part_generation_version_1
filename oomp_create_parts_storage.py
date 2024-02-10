import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    # sockerbit

    part_details = {}
    part_details["classification"] = "storage"
    part_details["type"] = "box_warehouse"
    part_details["size"] = ["sockerbit"]
    part_details["color"] = [""]
    part_details["description_main"] = "190_mm_wide_150_mm_height_260_mm_depth"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "ikea"
    part_details["part_number"] = "503_161_82"
    part_details["short_name"] = ""  
    
    parts.append(part_details)    


    oomp.add_parts(parts, make_files=make_files)
    