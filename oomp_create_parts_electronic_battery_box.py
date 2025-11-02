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
        part_details["classification"] = "electronic"
        part_details["type"] = "battery_box"
        part_details["size"] = "dewalt_xr"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = "diy_200"
        part_details["part_number_exact"] = "DIY-200"
        part_details["part_number_distributor_aliexpress"] = "1005005544254172"
        part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details["part_number_distributor_aliexpress"]}.html"
        part_details["short_name"] = "Dewalt XR Battery Holder"  
        parts.append(part_details)  

        
        part_details = {}
        part_details["classification"] = "electronic"
        part_details["type"] = "battery_box"
        part_details["size"] = "dewalt_tower_style"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = ""
        part_details["part_number_exact"] = ""
        part_details["part_number_distributor_aliexpress"] = "1005006020674006"
        part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details["part_number_distributor_aliexpress"]}.html"
        part_details["short_name"] = "Dewalt Tower Style Battery Holder"  
        parts.append(part_details)    
        
        part_details = {}
        part_details["classification"] = "electronic"
        part_details["type"] = "battery_box"
        part_details["size"] = "dewalt_xr"
        part_details["color"] = ""
        part_details["description_main"] = "usb_c_output"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = "wtl200"
        part_details["part_number_exact"] = "WTL200"
        part_details["part_number_distributor_aliexpress"] = "1005004999187666"
        part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details["part_number_distributor_aliexpress"]}.html"
        part_details["short_name"] = "Dewalt XR Battery USB Charger"  
        parts.append(part_details)    

    
    #ryobi
    if True:
        
        part_details = {}
        part_details["classification"] = "electronic"
        part_details["type"] = "battery_box"
        part_details["size"] = "ryobi_one_plus"
        part_details["color"] = ""
        part_details["description_main"] = "partial_top_cover_bare_wire_style"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = ""
        part_details["part_number_exact"] = ""
        part_details["part_number_distributor_aliexpress"] = "1005004221410788"
        part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details["part_number_distributor_aliexpress"]}.html"
        part_details["short_name"] = "Ryobi Plus One Battery Holder"  
        parts.append(part_details)   

    #pcb mount 16340
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "battery_holder"
    part_details["size"] = "16340"
    part_details["color"] = "single"
    part_details["description_main"] = "pcb_mount"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = "16340 Single Cell PCB Mount"
    parts.append(part_details)

    #dewalt 

    oomp.add_parts(parts, make_files=make_files)
    