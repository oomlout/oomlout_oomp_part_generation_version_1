import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    
    # panel_mount
    part_details = {}
    part_details["classification"] = "electrical"
    part_details["type"] = "light_panel"
    part_details["size"] = ["600_mm_x_600_mm"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "baumatic"
    part_details["part_number"] = "bx_lc6060_36w"
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)    

    
    oomp.add_parts(parts, make_files=make_files)
    