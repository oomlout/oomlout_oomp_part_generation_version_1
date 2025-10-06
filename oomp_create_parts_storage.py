import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    #bow_warehouse
    if True:

        # sockerbit
        part_details = {}
        part_details["classification"] = "storage"
        part_details["type"] = "box_warehouse"
        part_details["size"] = ["sockerbit"]
        part_details["color"] = [""]
        part_details["description_main"] = "190_mm_width_150_mm_height_260_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "503_161_82"
        part_details["short_name"] = ""      
        parts.append(part_details) 

        # ware house bins  
        #   rajapack

        part_details = {}
        part_details["classification"] = "storage"
        part_details["type"] = "box_warehouse"
        part_details["size"] = [""]
        part_details["color"] = ["cardboard"]
        part_details["description_main"] = "51_mm_width_112_mm_height_301_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "rajapack"
        part_details["part_number"] = "rbac11"
        part_details["short_name"] = ""       
        parts.append(part_details) 

        part_details = {}
        part_details["classification"] = "storage"
        part_details["type"] = "box_warehouse"
        part_details["size"] = [""]
        part_details["color"] = ["cardboard"]
        part_details["description_main"] = "101_mm_width_112_mm_height_301_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "rajapack"
        part_details["part_number"] = "rbac12"
        part_details["short_name"] = ""       
        parts.append(part_details) 

        part_details = {}
        part_details["classification"] = "storage"
        part_details["type"] = "box_warehouse"
        part_details["size"] = [""]
        part_details["color"] = ["cardboard"]
        part_details["description_main"] = "151_mm_width_112_mm_height_301_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "rajapack"
        part_details["part_number"] = "rbac13"
        part_details["short_name"] = ""
        parts.append(part_details) 

        part_details = {}
        part_details["classification"] = "storage"
        part_details["type"] = "box_warehouse"
        part_details["size"] = [""]
        part_details["color"] = ["cardboard"]
        part_details["description_main"] = "201_mm_width_112_mm_height_301_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "rajapack"
        part_details["part_number"] = "rbac14"
        part_details["short_name"] = ""
        parts.append(part_details)

        part_details = {}
        part_details["classification"] = "storage"
        part_details["type"] = "box_warehouse"
        part_details["size"] = [""]
        part_details["color"] = ["cardboard"]
        part_details["description_main"] = "151_mm_width_112_mm_height_401_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "rajapack"
        part_details["part_number"] = "rbac16"
        part_details["short_name"] = ""
        parts.append(part_details)


        # oomlout special size
        part_details = {}
        part_details["classification"] = "storage"
        part_details["type"] = "box_warehouse"
        part_details["size"] = [""]
        part_details["color"] = ["cardboard"]
        part_details["description_main"] = "122_mm_width_110_mm_height_175_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "oomlout"
        part_details["part_number"] = "box_1"
        part_details["short_name"] = ""
        parts.append(part_details)
        




    #bin bag
    if True:
        part_details = {}
        part_details["classification"] = "storage"
        part_details["type"] = "bin_bag"
        part_details["size"] = ["50_micron_thickness"]
        part_details["color"] = ["black"]
        part_details["description_main"] = "700_mm_width_1070_mm_height_70_litre_capacity"
        part_details["description_extra"] = "wheelie_bin_liner"
        part_details["manufacturer"] = "rajapack"
        part_details["part_number"] = "bprs7050"
        part_details["short_name"] = ""      
        parts.append(part_details)    


        part_details = {}
        part_details["classification"] = "storage"
        part_details["type"] = "bin_bag"
        part_details["size"] = ["60_micron_thickness"]
        part_details["color"] = ["black"]
        part_details["description_main"] = "736_mm_width_990_mm_height_70_litre_capacity"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "kite_packaging"
        part_details["part_number"] = "rs240_182939"
        part_details["part_number_exact"] = "RS240-182939"

        part_details["short_name"] = ""      
        parts.append(part_details)    

    ##jar
    if True:
        # kilner jars
        if True:
    
            # 3000 ml depth 280 ml diameter 140 mm
            part_details = {}
            part_details["classification"] = "storage"
            part_details["type"] = "jar_clip_top_kilner"
            part_details["size"] = [""]
            part_details["color"] = [""]
            part_details["description_main"] = "3000_ml_capacity_140_mm_diameter_280_mm_depth"
            part_details["description_extra"] = ""
            part_details["manufacturer"] = "kilner"
            part_details["part_number"] = "0025_494"
            part_details["part_number_exact"] = "0025.494"
            part_details["link_short_1"] = "kilner_3_litre"
            part_details["link_short_2"] = "kilner3l"
            part_details["link_short_3"] = "kilner3liter"

            parts.append(part_details)

            # 1500 ml depth 230 ml diameter 110 mm
            part_details = {}
            part_details["classification"] = "storage"
            part_details["type"] = "jar_clip_top_kilner"
            part_details["size"] = [""]
            part_details["color"] = [""]
            part_details["description_main"] = "1500_ml_capacity_110_mm_diameter_230_mm_depth"
            part_details["description_extra"] = ""
            part_details["manufacturer"] = "kilner"
            part_details["part_number"] = "0025_492"
            part_details["part_number_exact"] = "0025.492"
            part_details["link_short_1"] = "kilner_1_5_litre"
            part_details["link_short_2"] = "kilner15l"
            part_details["link_short_3"] = "kilner15liter"
            parts.append(part_details)

            # 1000 ml depth 180 ml diameter 110 mm
            part_details = {}
            part_details["classification"] = "storage"
            part_details["type"] = "jar_clip_top_kilner"
            part_details["size"] = [""]
            part_details["color"] = [""]
            part_details["description_main"] = "1000_ml_capacity_110_mm_diameter_180_mm_depth"
            part_details["description_extra"] = ""
            part_details["manufacturer"] = "kilner"
            part_details["part_number"] = "0025_491"
            part_details["part_number_exact"] = "0025.491"
            part_details["link_short_1"] = "kilner_1_litre"
            part_details["link_short_2"] = "kilner1l"
            part_details["link_short_3"] = "kilner1liter"
            parts.append(part_details)
    

    oomp.add_parts(parts, make_files=make_files)
    