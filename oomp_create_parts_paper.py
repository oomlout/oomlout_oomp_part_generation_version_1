import oomp
import copy

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

    default_empty = copy.deepcopy(base)

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

    #letter size
    part_details = base.copy()
    part_details["size"] = "letter_216_mm_width_279_mm_height"
    part_details["width"] = "216 mm"
    part_details["height"] = "279 mm"
    parts.append(part_details)

    base_letter = part_details.copy()   

    
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


    #koala brand
    if True:
        #glossy
        if True:
            #souble sided glossy 120 gsm
            part_details = base_a4.copy()
            part_details["description_main"] = "120_grams_per_meter_square"
            part_details["description_extra"] = "double_sided_glossy_style_inkjet_printer"
            part_details["manufacturer"] = "koala"        
            #amazon
            part_details["distributor_amazon"] = "B07L5MMXD4"
            part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
            part_details["price_1_distributor_amazon"] = 9.99/100/1.2
            #current price
            part_details["price_1"] = part_details["price_1_distributor_amazon"]
            parts.append(part_details)

            #double sided glossy 180 gram inkjet
            part_details = base_a4.copy()
            part_details["description_main"] = "180_grams_per_meter_square"
            part_details["description_extra"] = "double_sided_glossy_style_inkjet_printer"
            part_details["manufacturer"] = "koala"
            #amazon
            part_details["distributor_amazon"] = "B07L5NSWR8"
            part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
            part_details["price_1_distributor_amazon"] = 11.99/100/1.2
            #current price
            part_details["price_1"] = part_details["price_1_distributor_amazon"]
            parts.append(part_details)

            #double sided 240 gsm
            part_details = base_a4.copy()
            part_details["description_main"] = "240_grams_per_meter_square"
            part_details["description_extra"] = "double_sided_glossy_style_inkjet_printer"
            part_details["manufacturer"] = "koala"
            #amazon
            part_details["distributor_amazon"] = "B07L5LDZD7"
            part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
            part_details["price_1_distributor_amazon"] = 13.99/100/1.2
            #current price
            part_details["price_1"] = part_details["price_1_distributor_amazon"]
            parts.append(part_details)


        #matte
        if True:
            #120 gsm double sided matte
            part_details = base_a4.copy()
            part_details["description_main"] = "120_grams_per_meter_square"
            part_details["description_extra"] = "double_sided_matte_style_laser_printer"
            part_details["manufacturer"] = "koala"
            #amazon
            part_details["distributor_amazon"] = "B07VYKP55S"
            part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
            part_details["price_1_distributor_amazon"] = 7.99/100/1.2
            #current price
            part_details["price_1"] = part_details["price_1_distributor_amazon"]
            parts.append(part_details)

            #double sided matte 140 gsm inkjet
            part_details = base_a4.copy()
            part_details["description_main"] = "140_grams_per_meter_square"
            part_details["description_extra"] = "double_sided_matte_style_inkjet_printer"
            part_details["manufacturer"] = "koala"
            #amazon
            part_details["distributor_amazon"] = "B07KN4HVQS"
            part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
            part_details["price_1_distributor_amazon"] = 9.99/100/1.2
            #current price
            part_details["price_1"] = part_details["price_1_distributor_amazon"]
            parts.append(part_details)

            #double sided matte 200 gsm
            part_details = base_a4.copy()
            part_details["description_main"] = "200_grams_per_meter_square"
            part_details["description_extra"] = "double_sided_matte_style_laser_printer"
            part_details["manufacturer"] = "koala"
            #amazon
            part_details["distributor_amazon"] = "B07VYJKZ6F"
            part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
            part_details["price_1_distributor_amazon"] = 9.99/100/1.2
            #current price
            part_details["price_1"] = part_details["price_1_distributor_amazon"]
            parts.append(part_details)




            #250 gsm double sided matte
            part_details = base_a4.copy()
            part_details["description_main"] = "250_grams_per_meter_square"
            part_details["description_extra"] = "double_sided_matte_style_laser_printer"
            part_details["manufacturer"] = "koala"
            #amazon
            part_details["distributor_amazon"] = "B07VVDL79C"
            part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
            part_details["price_1_distributor_amazon"] = 10.79/100/1.2
            #current price
            part_details["price_1"] = part_details["price_1_distributor_amazon"]
            parts.append(part_details)



        #sticker sheet
        if True:
            #a4 glossy sticker sheet
            part_details = base_a4.copy()
            part_details["description_main"] = "sticker_sheet"
            part_details["description_extra"] = "single_sided_glossy_style_inkjet_printer_paper_material"
            part_details["manufacturer"] = "koala"
            #amazon
            part_details["distributor_amazon"] = "B082XKGBF4"
            part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
            part_details["price_1_distributor_amazon"] = 12.99/100/1.2
            #current price
            part_details["price_1"] = part_details["price_1_distributor_amazon"]
            parts.append(part_details)

            #gmcraft
            if True:
                #glossy plastic                
                part_details = base_a4.copy()
                part_details["description_main"] = "sticker_sheet"
                part_details["description_extra"] = "glossy_style_inkjet_printer_plastic_material"
                part_details["manufacturer"] = "gmcraft"
                #amazon
                part_details["distributor_amazon"] = "B0BMLTJDQK"
                part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
                part_details["price_1_distributor_amazon"] = 8.70/10/1.2
                #current price
                part_details["price_1"] = part_details["price_1_distributor_amazon"]
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


    #envelope
    if True:
        base = {}
        base["classification"] = "paper"
        base["type"] = "envelope"    
        base["color"] = ""
        base["description_main"] = ""
        base["description_extra"] = ""
        base["manufacturer"] = ""
        base["part_number"] = ""

        #c4
        part_details = base.copy()
        w = 324
        h = 229
        name = "c4"
        note = f"fits_a4_sheet"
        part_details["size"] = f"{name}_size_{w}_mm_width_{h}_mm_height_{note}"
        part_details["width"] = f"{w} mm"
        part_details["height"] = f"{h} mm"
        part_details["short_name"] = "C4 Envelope"
        parts.append(part_details)

        #c5
        part_details = base.copy()
        w = 229
        h = 162
        name = "c5"
        note = f"fits_a5_sheet"
        part_details["size"] = f"{name}_size_{w}_mm_width_{h}_mm_height_{note}"
        part_details["width"] = f"{w} mm"
        part_details["height"] = f"{h} mm"
        part_details["short_name"] = "C5 Envelope"
        parts.append(part_details)

        #c6
        part_details = base.copy()
        w = 162
        h = 114
        name = "c6"
        note = f"fits_a6_sheet"
        part_details["size"] = f"{name}_size_{w}_mm_width_{h}_mm_height_{note}"
        part_details["width"] = f"{w} mm"
        part_details["height"] = f"{h} mm"
        part_details["short_name"] = "C6 Envelope"
        parts.append(part_details)

        #c7
        part_details = base.copy()
        w = 114
        h = 81
        name = "c7"
        note = f"fits_a7_sheet"
        part_details["size"] = f"{name}_size_{w}_mm_width_{h}_mm_height_{note}"
        part_details["width"] = f"{w} mm"
        part_details["height"] = f"{h} mm"
        part_details["short_name"] = "C7 Envelope"
        parts.append(part_details)

        #dl
        part_details = base.copy()
        w = 220
        h = 110
        name = "dl"
        note = f"fits_a4_sheet_folded_in_thirds"
        part_details["size"] = f"{name}_size_{w}_mm_width_{h}_mm_height_{note}"
        part_details["width"] = f"{w} mm"
        part_details["height"] = f"{h} mm"
        part_details["short_name"] = "DL Envelope"
        parts.append(part_details)






    oomp.add_parts(parts, **kwargs)
    