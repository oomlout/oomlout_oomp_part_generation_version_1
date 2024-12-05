import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    base = {}
    base["classification"] = "paper"
    base["type"] = "sheet"    
    base["color"] = ""
    base["description_main"] = ""
    base["description_extra"] = ""
    base["manufacturer"] = ""
    base["part_number"] = ""    

    # a sizes
    
    #a0
    part_details = base.copy()
    part_details["size"] = "a0_841_mm_width_1189_mm_height"
    part_details["width"] = "841 mm"
    part_details["height"] = "1189 mm"
    parts.append(part_details)

    #a1
    part_details = base.copy()
    part_details["size"] = "a1_594_mm_width_841_mm_height"
    part_details["width"] = "594 mm"
    part_details["height"] = "841 mm"
    parts.append(part_details)

    #a2
    part_details = base.copy()
    part_details["size"] = "a2_420_mm_width_594_mm_height"
    part_details["width"] = "420 mm"
    part_details["height"] = "594 mm"
    parts.append(part_details)

    #a3
    part_details = base.copy()
    part_details["size"] = "a3_297_mm_width_420_mm_height"
    part_details["width"] = "297 mm"
    part_details["height"] = "420 mm"
    parts.append(part_details)


    #a4
    part_details = base.copy()
    part_details["size"] = "a4_210_mm_width_297_mm_height"
    part_details["width"] = "210 mm"
    part_details["height"] = "297 mm"    
    parts.append(part_details)

    base_a4 = part_details.copy()

    # 100 gram bright white
    if True:
        part_details = base_a4.copy()
        part_details["description_main"] = "100_grams_per_meter_square"
        part_details["description_extra"] = "160_cie"
        part_details["manufacturer"] = "mondi"
        part_details["part_number"] = "a4_26626" 
        part_details["part_number_exact"] = "A4-26626"
        part_details["upc"] = "9003974411965"
        #distributor
        # amazon
        part_details["distributor_amazon"] = "B000J6A58M"
        part_details["link_distributor_amazon"] = "https://www.amazon.co.uk/Color-Copy-Premium-Ream-Wrapped-CCW0324/dp/B000J6A58M"
        part_details["price_1_distributor_amazon"] = 16.99/500/1.2
        # viking_direct
        part_details["distributor_viking_direct"] = "12320"
        part_details["distributor_viking_direct_link"] = "https://www.viking-direct.co.uk/en/p/12320"
        part_details["price_1_distributor_viking_direct"] = 12.31/500/1.2
        part_details["distributor_viking_note"] = "free delivery over 59 pounds"
        # current price
        part_details["price_1"] = part_details["price_1_distributor_viking_direct"]
        parts.append(part_details)

    # 160 gram bright white
    if True:
        part_details = base_a4.copy()
        part_details["description_main"] = "160_grams_per_meter_square"
        part_details["description_extra"] = "160_cie"
        part_details["manufacturer"] = "mondi"
        part_details["part_number"] = "a4_26742" 
        part_details["part_number_exact"] = "A4-26742"
        part_details["upc"] = "9003974416373"
        #distributor
        # amazon
        part_details["distributor_amazon"] = "B000KJOBK6"
        part_details["link_distributor_amazon"] = "https://www.amazon.co.uk/dp/B000KJOBK6"
        part_details["price_1_distributor_amazon"] = 14.49/250/1.2
        # viking_direct
        part_details["distributor_viking_direct"] = "73160"
        part_details["distributor_viking_direct_link"] = "https://www.viking-direct.co.uk/en/p/73160"
        part_details["price_1_distributor_viking_direct"] = 8.80/250/1.2
        part_details["distributor_viking_note"] = "free delivery over 59 pounds"
        # current price
        part_details["price_1"] = part_details["price_1_distributor_viking_direct"]
        parts.append(part_details)

    # 250 gram 
    if True:
        part_details = base_a4.copy()
        part_details["description_main"] = "250_grams_per_meter_square"
        #distributor
        # amazon
        part_details["distributor_amazon"] = "B0CHG4S5G6"
        part_details["link_distributor_amazon"] = "https://www.amazon.co.uk/A4-100sheet-Cardstock-Invitations-Stationary-Scrapbook/dp/B0CHG4S5G6"
        part_details["price_1_distributor_amazon"] = 7.99/100/1.2
        # viking_direct
        part_details["distributor_rapid_online"] = "06-0930"
        part_details["distributor_rapid_online_link"] = "https://www.rapidonline.com/rapid-a4-card-white-pack-of-100-06-0930"
        part_details["price_1_distributor_rapid_online"] = 13.03/100/1.2
        # current price
        part_details["price_1"] = part_details["price_1_distributor_rapid_online"]
        parts.append(part_details)



    #a5
    part_details = base.copy()
    part_details["size"] = "a5_148_mm_width_210_mm_height"
    part_details["width"] = "148 mm"
    part_details["height"] = "210 mm"
    parts.append(part_details)

    #a6
    part_details = base.copy()
    part_details["size"] = "a6_105_mm_width_148_mm_height"
    part_details["width"] = "105 mm"
    part_details["height"] = "148 mm"
    parts.append(part_details)

    #a7
    part_details = base.copy()
    part_details["size"] = "a7_74_mm_width_105_mm_height"
    part_details["width"] = "74 mm"
    part_details["height"] = "105 mm"
    parts.append(part_details)

    #a8
    part_details = base.copy()
    part_details["size"] = "a8_52_mm_width_74_mm_height"
    part_details["width"] = "52 mm"
    part_details["height"] = "74 mm"
    parts.append(part_details)

    #poters
    
    # 460 mm x 640 mm
    part_details = base.copy()
    part_details["size"] = "460_mm_width_640_mm_height"
    part_details["width"] = "460 mm"
    part_details["height"] = "640 mm"
    parts.append(part_details)

    # 510 mm x 750 mm
    part_details = base.copy()
    part_details["size"] = "510_mm_width_750_mm_height"
    part_details["width"] = "510 mm"
    part_details["height"] = "750 mm"
    parts.append(part_details)


    oomp.add_parts(parts, **kwargs)
    