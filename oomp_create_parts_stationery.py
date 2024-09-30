import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    # stationery
    #     clips
    part_details = {}
    part_details["classification"] = "stationery"
    part_details["type"] = "clip_binder"
    part_details["size"] = ["100_mm_width"]
    part_details["color"] = ["metal"]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""
    #add amazon distributor
    part_details["distributor_amazon"] = "B075YQ93CC"    
    part_details["distributor_amazon_link"] = "https://www.amazon.co.uk/dp/B075YQ93CC"
    parts.append(part_details) 


    oomp.add_parts(parts, make_files=make_files)
    