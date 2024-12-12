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
        part_details["classification"] = "remote_control"
        part_details["type"] = "electronic_speed_controller"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = "1_amp_12_mm_width_8_5_mm_height_green_pcb"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = ""        
        part_details["part_number_distributor_aliexpress"] = "1005006080168104"
        part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details["part_number_distributor_aliexpress"]}.html"
        part_details["short_name"] = "ESC 1 amp"  
        parts.append(part_details)    
    

    oomp.add_parts(parts, make_files=make_files)
    