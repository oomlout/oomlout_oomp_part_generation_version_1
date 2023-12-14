import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    
    # c5 deep
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "cardboard_box_postal_tabs"
    part_details["size"] = ["c5_229_mm_x_162_mm_x_50_mm"]
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
    part_details["width_internal"] = ["215 mm"]
    part_details["height_internal"] = ["155 mm"]
    part_details["depth_internal"] = ["50 mm"]
    
    # c6 deep
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "cardboard_box_postal_tabs"
    part_details["size"] = ["c6_162_mm_x_114_mm_x_50_mm"]
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
    
    #imperial
    # 7 x 5 x 2
    # c5 deep
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "cardboard_box_postal_tabs"
    part_details["size"] = ["imperial_7_in_x_5_in_x_2_in"]
    part_details["color"] = ["brown"]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["cost_per"] = "£0.54"
    part_details["cost_per_ebay"] = "£1.44"
    part_details["link_purchase"] = ["ebay.co.uk/itm/233048701153?var=532550738565","https://www.tinyboxcompany.co.uk/1-piece-a6-mailing-gift-box-kraft-natural-fmkra6"]
    part_details["width_internal"] = ["178 mm"]
    part_details["height_internal"] = ["131 mm"]
    part_details["depth_internal"] = ["55 mm"]
    


    parts.append(part_details)    


    oomp.add_parts(parts, make_files=make_files)
    