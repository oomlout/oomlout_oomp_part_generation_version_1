import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## size chart https://www.bouncerubberbands.com/news/the-ultimate-guide-to-rubber-band-sizes

    
    
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "elastic_band"
    part_details["size"] = ["size_85"]
    part_details["color"] = ["natural"]
    part_details["description_main"] = ["12_mm_width_100_mm_length"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    
    parts.append(part_details)    


    oomp.add_parts(parts, make_files=make_files)
    