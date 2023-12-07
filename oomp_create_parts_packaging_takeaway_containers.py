import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    
    # nisbet containers
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_rectangle"
    part_details["size"] = ["1000_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "nisbet_fiesta"
    part_details["part_number"] = "large_dm183"
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)    

    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_rectangle"
    part_details["size"] = ["650_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "nisbet_fiesta"
    part_details["part_number"] = "medium_dm182"
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)  

    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_rectangle"
    part_details["size"] = ["500_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "nisbet_fiesta"
    part_details["part_number"] = "small_dm181"
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details) 

    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_circle"
    part_details["size"] = ["150_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "nisbet_fiesta"
    part_details["part_number"] = "ct083"
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)        

    #sauce pots
    
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_circle"
    part_details["size"] = ["60_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = "heavy_duty"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "satco"
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)  

    oomp.add_parts(parts, make_files=make_files)
    