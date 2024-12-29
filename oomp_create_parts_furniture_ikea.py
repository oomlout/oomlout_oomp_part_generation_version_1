import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    # ikea
    #   billy
    if True:
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_billy"
        part_details["color"] = "white"
        part_details["description_main"] = ""
        part_details["description_extra"] = "800_mm_width_2370_mm_height_280_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "591_822_01"
        part_details["width"] = "800 mm"
        part_details["height"] = "2370 mm"
        part_details["depth"] = "280 mm"
        parts.append(part_details)


        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_billy"
        part_details["color"] = "white"
        part_details["description_main"] = ""
        part_details["description_extra"] = "800_mm_width_2020_mm_height_280_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "002_638_50"
        part_details["width"] = "800 mm"
        part_details["height"] = "2020 mm"
        part_details["depth"] = "280 mm"
        parts.append(part_details)

        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_billy"
        part_details["color"] = "white"
        part_details["description_main"] = ""
        part_details["description_extra"] = "800_mm_width_2020_mm_height_400_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "904_019_32"
        part_details["width"] = "800 mm"
        part_details["height"] = "2020 mm"
        part_details["depth"] = "400 mm"
        parts.append(part_details)


        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_billy"
        part_details["color"] = "white"
        part_details["description_main"] = ""
        part_details["description_extra"] = "400_mm_width_2020_mm_height_280_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "502_638_38"
        part_details["width"] = "400 mm"
        part_details["height"] = "2020 mm"
        part_details["depth"] = "280 mm"
        parts.append(part_details)


        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_billy"
        part_details["color"] = "white"
        part_details["description_main"] = ""
        part_details["description_extra"] = "800_mm_width_1060_mm_height_280_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "302_638_44"
        part_details["width"] = "800 mm"
        part_details["height"] = "1060 mm"
        part_details["depth"] = "280 mm"
        parts.append(part_details)

        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_billy"
        part_details["color"] = "white"
        part_details["description_main"] = ""
        part_details["description_extra"] = "400_mm_width_1060_mm_height_280_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "802_638_32"
        part_details["width"] = "400 mm"
        part_details["height"] = "1060 mm"
        part_details["depth"] = "280 mm"
        parts.append(part_details)

        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf_extender"
        part_details["size"] = "ikea_billy"
        part_details["color"] = "white"
        part_details["description_main"] = ""
        part_details["description_extra"] = "800_mm_width_350_mm_height_280_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "402_638_53"
        part_details["width"] = "800 mm"
        part_details["height"] = "350 mm"
        part_details["depth"] = "280 mm"
        parts.append(part_details)

    #   havsta
    if True:    
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "cabinet"
        part_details["size"] = "ikea_havsta"
        part_details["color"] = "white"
        part_details["description_main"] = ""
        part_details["description_extra"] = "810_mm_width_890_mm_height_470_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "005_292_42"
        part_details["width"] = "810 mm"
        part_details["height"] = "890 mm"
        part_details["depth"] = "470 mm"
        parts.append(part_details)

    # hejne
    if True:    
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_hejne"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = "780_mm_width_1710_mm_height_310_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "390_314_11"
        part_details["width"] = "780 mm"
        part_details["height"] = "1710 mm"
        part_details["depth"] = "310 mm"
        parts.append(part_details)

    # gorm
    if True:    
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_gorm"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = "780_mm_width_1740_mm_height_350_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = ""
        part_details["width"] = "780 mm"
        part_details["height"] = "1740 mm"
        part_details["depth"] = "350 mm"
        parts.append(part_details)


    #   kallax
    if True:
        #5 by 5
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_kallax"
        part_details["color"] = "white"
        part_details["description_main"] = "5_cell_width_5_cell_height"
        part_details["description_extra"] = "1820_mm_width_1820_mm_height_390_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "703_015_37"
        part_details["width"] = "1820 mm"
        part_details["height"] = "1820 mm"
        part_details["depth"] = "390 mm"
        parts.append(part_details)

        
        # 4 by 4
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_kallax"
        part_details["color"] = ["white"]
        part_details["description_main"] = "4_cell_width_4_cell_height"
        part_details["description_extra"] = "1470_mm_width_1470_mm_height_390_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "302_758_61"
        part_details["width"] = "1470 mm"
        part_details["height"] = "1470 mm"
        part_details["depth"] = "390 mm"
        parts.append(part_details)

        # 3 by 4
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_kallax"
        part_details["color"] = "white"
        part_details["description_main"] = "3_cell_width_4_cell_height"
        part_details["description_extra"] = "1120_mm_width_1470_mm_height_390_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "104_099_32"
        part_details["width"] = "1120 mm"
        part_details["height"] = "1470 mm"
        part_details["depth"] = "390 mm"
        parts.append(part_details)


        # 2 by 4
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_kallax"
        part_details["color"] = "white"
        part_details["description_main"] = "2_cell_width_4_cell_height"
        part_details["description_extra"] = "770_mm_width_1470_mm_height_390_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "802_758_87"
        part_details["width"] = "770 mm"
        part_details["height"] = "1470 mm"
        part_details["depth"] = "390 mm"
        parts.append(part_details)

        #1 by 4
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_kallax"
        part_details["color"] = "white"
        part_details["description_main"] = "1_cell_width_4_cell_height"
        part_details["description_extra"] = "390_mm_width_1470_mm_height_390_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "002_758_48"
        part_details["width"] = "390 mm"
        part_details["height"] = "1470 mm"
        part_details["depth"] = "390 mm"
        parts.append(part_details)

        #2 by 2
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_kallax"
        part_details["color"] = "white"
        part_details["description_main"] = "2_cell_width_2_cell_height"
        part_details["description_extra"] = "770_mm_width_770_mm_height_390_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "202_758_14"
        part_details["width"] = "770 mm"
        part_details["height"] = "770 mm"
        part_details["depth"] = "390 mm"
        parts.append(part_details)

        #2 by 1
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "shelf"
        part_details["size"] = "ikea_kallax"
        part_details["color"] = "white"
        part_details["description_main"] = "2_cell_width_1_cell_height"
        part_details["description_extra"] = "770_mm_width_390_mm_height_390_mm_depth"
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = "903_015_55"
        part_details["width"] = "770 mm"
        part_details["height"] = "390 mm"
        part_details["depth"] = "390 mm"
        parts.append(part_details)

        
    #lighting
    if True:
        #slattbo
        part_details = {}
        part_details["classification"] = "lighting"
        part_details["type"] = "pendant"
        part_details["size"] = ["ikea_slattbo"]
        part_details["color"] = ["copper"]
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)

    #   varde
    if True:    
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "kitchen_unit_freestanding"
        part_details["size"] = "ikea_varde"
        part_details["color"] = ""
        part_details["description_main"] = "dual_drawer"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = ""
        part_details["width"] = ""
        part_details["height"] = ""
        part_details["depth"] = ""
        part_details["width_drawer"] = ""
        #parts.append(part_details)
    
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "kitchen_unit_freestanding"
        part_details["size"] = "ikea_varde"
        part_details["color"] = ""
        part_details["description_main"] = "triple_drawer"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "ikea"
        part_details["part_number"] = ""
        part_details["width"] = ""
        part_details["height"] = ""
        part_details["depth"] = ""
        #parts.append(part_details)


        

    




    
    oomp.add_parts(parts, **kwargs)
    