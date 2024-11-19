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
    part_details["classification"] = "electronic"
    part_details["type"] = "battery_box"
    part_details["size"] = ["dewalt_xr"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "aliexpress"
    part_details["part_number"] = "diy_200"
    part_details["part_number_exact"] = "DIY-200"
    part_details["short_name"] = "Dewalt XR Battery Holder"  
    part_details["distributors"] = []
    parts.append(part_details)    

    
    #dewalt 

    oomp.add_parts(parts, make_files=make_files)
    