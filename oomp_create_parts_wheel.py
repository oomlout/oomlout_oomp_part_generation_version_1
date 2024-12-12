import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

       
    #dewalt
    if True:
        part_details = {}
        part_details["classification"] = "wheel"
        part_details["type"] = "toy"
        part_details["size"] = "n20_motor_3_mm_d_shaft"
        part_details["color"] = ""
        part_details["description_main"] = "34_mm diameter_6_5_mm_wide_rubber"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = ""        
        part_details["part_number_distributor_aliexpress"] = "1005006487040075"
        part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details["part_number_distributor_aliexpress"]}.html"
        part_details["short_name"] = "Wheel 34mm Diameter 6.5mm Wide N20 Motor"  
        parts.append(part_details)    
    

    oomp.add_parts(parts, make_files=make_files)
    