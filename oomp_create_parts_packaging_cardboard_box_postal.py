import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    # c4 deep
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "cardboard_box_postal_tabs"
    part_details["size"] = ["c4_324_mm_width_229_mm_height_50_mm_depth"]
    part_details["color"] = ["brown"]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["cost_per"] = "£1"
    part_details["cost_per_ebay"] = "£1.44"
    part_details["cost_per_10"] = "£1.44"
    part_details["cost_per_50"] = "£1.00"
    part_details["cost_per_100"] = "£0.53"
    part_details["link_purchase"] = ["https://www.ebay.co.uk/itm/174043294174?var=474501502317","https://ecopostalpack.co.uk/product/c4-extra-deep-pip-style-ecofriendly-cardboard-postal-mail-small-parcelgift-box/"]
    part_details["width_internal"] = ["325 mm"]
    part_details["height_internal"] = ["230 mm"]
    part_details["depth_internal"] = ["50 mm"]
    parts.append(part_details)    
    
    # c5 deep
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "cardboard_box_postal_tabs"
    part_details["size"] = ["c5_229_mm_width_162_height_x_50_mm_depth"]
    part_details["color"] = ["brown"]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["cost_per"] = "£0.50"
    part_details["cost_per_ebay"] = "£1.44"
    part_details["cost_per_10"] = "£1.44"
    part_details["cost_per_50"] = "£0.612"
    part_details["cost_per_100"] = "£0.456"
    part_details["link_purchase"] = ["ebay.co.uk/itm/174060319073","https://www.rajapack.co.uk/cardboard-boxes/document-printer-boxes/a5-brown-flat-postal-boxes_OFF_UK_0205.html?"]
    part_details["width_internal"] = ["220 mm"]
    part_details["height_internal"] = ["160 mm"]
    part_details["depth_internal"] = ["50 mm"]
    parts.append(part_details)    
    
    # c6 deep
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "cardboard_box_postal_tabs"
    part_details["size"] = ["c6_162_mm_width_114_mm_height_50_mm_depth"]
    part_details["color"] = ["brown"]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["cost_per"] = "£0.67"
    part_details["cost_per_ebay"] = "£1.44"
    part_details["cost_per_500"] = "£0.518"
    part_details["link_purchase"] = ["https://www.ebay.co.uk/itm/174060319073?var=474544173601","https://www.eco-craft.co.uk/deep-postal-box-c6.html"]
    part_details["width_internal"] = ["160 mm"]
    part_details["height_internal"] = ["110 mm"]
    part_details["depth_internal"] = ["50 mm"]
    parts.append(part_details)    
    
    #imperial
    # 7 x 5 x 2
    # c5 deep
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "cardboard_box_postal_tabs"
    part_details["size"] = ["imperial_7_in_width_5_in_height_2_in_depth"]
    part_details["color"] = ["brown"]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["cost_per"] = "£0.54"
    part_details["cost_per_ebay"] = "£1.44"
    part_details["link_purchase"] = ["ebay.co.uk/itm/233048701153?var=532550738565","https://www.tinyboxcompany.co.uk/1-piece-a6-mailing-gift-box-kraft-natural-fmkra6"]
    part_details["width_internal"] = ["175 mm"]
    part_details["height_internal"] = ["142 mm"]
    part_details["depth_internal"] = ["55 mm"]
    parts.append(part_details)    


    # cardboard roll
    #    300 mm width
    
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "cardboard_roll"
    part_details["size"] = ["300_mm_width_75000_mm_length_3_5_mm_depth"]
    part_details["color"] = ["kraft"]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "rajapack"
    part_details["part_number"] = "cp300"
    part_details["short_name"] = ""  
    part_details["cost_per"] = "£23.10"    
    part_details["link_purchase"] = ["https://www.rajapack.co.uk/protective-packaging/paper-packaging/corrugated-cardboard-rolls_PDT05562.html"]
    parts.append(part_details)

    #cardboard pieces
    if True:
        #insert for bolt tin two per tin
        part_details = {}
        part_details["classification"] = "packaging"
        part_details["type"] = "cardboard_roll"
        part_details["size"] = ["56_mm_width_136_mm_length_3_5_mm_depth"]
        part_details["color"] = ["kraft"]
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "oomlout"
        part_details["part_number"] = "bolt_tin_pad_1"
        part_details["short_name"] = ""  
        part_details["cost_per"] = "£0.02"    
        part_details["link_purchase"] = [""]
        parts.append(part_details)

        sheet_base = copy.deepcopy(part_details)

        #wrapper
        part_details = copy.deepcopy(sheet_base)
        part_details["size"] = ["200_mm_width_344_mm_length_3_5_mm_depth"]
        parts.append(part_details)



    oomp.add_parts(parts, make_files=make_files)
    