import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

       
    #dyson
    if True:

        #main vacuums
        sizes = ["dyson_v6", "dyson_v7", "dyson_v8", "dyson_v10", "dyson_v11"]
        for size in sizes:
            part_details = {}
            part_details["classification"] = "appliance"
            part_details["type"] = "vacuum_cleaner"
            part_details["size"] = size
            part_details["color"] = ""
            part_details["description_main"] = ""
            part_details["description_extra"] = ""
            part_details["manufacturer"] = "dyson"
            part_number = size.replace("dyson_", "")
            part_details["part_number"] = part_number
            parts.append(part_details)    
    
        #v6 cleaning heads
        description_mains = ["motorhead_tool", "combination_tool", "crevice_tool", "mini_motorhead_tool", "precision_tool"]
        for description_main in description_mains:
            part_details = {}
            part_details["classification"] = "appliance"
            part_details["type"] = "vacuum_cleaner"
            part_details["size"] = "dyson_v6"
            part_details["color"] = ""
            part_details["description_main"] = description_main
            part_details["description_extra"] = ""
            part_details["manufacturer"] = "dyson"
            part_details["part_number"] = f""
            parts.append(part_details)



    oomp.add_parts(parts, make_files=make_files)
    