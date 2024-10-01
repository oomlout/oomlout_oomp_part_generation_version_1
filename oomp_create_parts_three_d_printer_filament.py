import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    #print_time]
    part_details = {}
    part_details["classification"] = "three_d_printer"
    part_details["type"] = "printing"
    part_details["size"] = ["low_quality"]
    part_details["color"] = [""]
    part_details["description_main"] = "minute"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["price_per"] = 0
    part_details["price_per_gram"] = 0
    part_details["price_current"] = 0
    part_details["price_per_kilogram"] = 0
    parts.append(part_details)    
    
    # printers
    part_details = {}
    part_details["classification"] = "three_d_printer"
    part_details["type"] = "printer"
    part_details["size"] = [""]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "wanhao"
    part_details["part_number"] = "dupicator_i3_plus"
    part_details["short_name"] = ""  
    parts.append(part_details)    
    part_details = {}
    part_details["classification"] = "three_d_printer"
    part_details["type"] = "printer"
    part_details["size"] = [""]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "anycubic"
    part_details["part_number"] = "vyper"
    part_details["short_name"] = ""  
    parts.append(part_details)    

    # 3dqf filament
    part_details = {}
    part_details["classification"] = "three_d_printer"
    part_details["type"] = "filament"
    part_details["size"] = "1_75_mm"
    part_details["color"] = "pla_aqua"
    part_details["description_main"] = "reel"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "3dqf"
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["price_per"] = 18.99 / 1000 / 1.2
    part_details["price_per_gram"] = 18.99 / 1000 / 1.2
    part_details["price_current"] = 18.99 / 1000 / 1.2
    part_details["price_per_kilogram"] = 18.99 / 1.2
    part_details["weight"] = 1
    part_details["link_purchase"] = "https://www.3dqf.co.uk/product-page/aqua-1-75mm-uk-made-3d-printer-filament"
    parts.append(part_details)    
    
    
    part_details = {}
    part_details["classification"] = "three_d_printer"
    part_details["type"] = "filament"
    part_details["size"] = "1_75_mm"
    part_details["color"] = "pla_plus_black"
    part_details["description_main"] = "reel"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "3dqf"
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["price_per"] = 20.99 / 1000 / 1.2
    part_details["price_per_gram"] = 20.99 / 1000 / 1.2
    part_details["price_current"] = 20.99 / 1000 / 1.2
    part_details["price_per_kilogram"] = 20.99 / 1.2
    part_details["weight"] = 1
    part_details["link_purchase"] = "https://www.3dqf.co.uk/product-page/deep-black-pla-plus-1-75mm-uk-made-3d-printer-filament"
    parts.append(part_details)    
    
    
    part_details = {}
    part_details["classification"] = "three_d_printer"
    part_details["type"] = "filament"
    part_details["size"] = "1_75_mm"
    part_details["color"] = "pla_eco_black"
    part_details["description_main"] = "reel"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "3dqf"
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["price_per_1"] = 15.99 / 1000 / 1.2
    part_details["price_per_100"] = 9.99 / 1000 / 1.2
    part_details["price_per_gram"] = part_details["price_per_100"]
    part_details["price_per"] = part_details["price_per_100"]
    part_details["price_current"] = 15.99 / 1000 / 1.2
    part_details["price_per_kilogram"] = 15.99 / 1.2
    part_details["weight"] = 1
    part_details["link_purchase"] = "https://www.3dqf.co.uk/product-page/copy-of-eco-pla-10-pack-1-75mm-uk-made-3d-printer-filament-1kg"
    parts.append(part_details)    

    
    part_details = {}
    part_details["classification"] = "three_d_printer"
    part_details["type"] = "filament"
    part_details["size"] = "1_75_mm"
    part_details["color"] = "pla_eco_blue_light"
    part_details["description_main"] = "reel"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "3dqf"
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["price_per_1"] = 15.99 / 1000 / 1.2
    part_details["price_per_100"] = 9.99 / 1000 / 1.2
    part_details["price_per_gram"] = part_details["price_per_100"]
    part_details["price_per"] = part_details["price_per_100"]
    part_details["price_current"] = 15.99 / 1000 / 1.2
    part_details["price_per_kilogram"] = 15.99 / 1.2
    part_details["weight"] = 1
    part_details["link_purchase"] = "https://www.3dqf.co.uk/product-page/copy-of-eco-pla-10-pack-1-75mm-uk-made-3d-printer-filament-1kg"
    parts.append(part_details) 

    oomp.add_parts(parts, make_files=make_files)
    