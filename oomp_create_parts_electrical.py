import oomp
import copy 

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    # box
    part_details = {}
    part_details["classification"] = "electrical"
    part_details["type"] = "light_panel"
    part_details["size"] = ["600_mm_x_600_mm"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "baumatic"
    part_details["part_number"] = "bx_lc6060_36w"
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)    

    
    # panel_mount
    part_details = {}
    part_details["classification"] = "electrical"
    part_details["type"] = "light_panel"
    part_details["size"] = ["600_mm_x_600_mm"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "baumatic"
    part_details["part_number"] = "bx_lc6060_36w"
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)    

    # light fixing hook
    part_details = {}
    part_details["classification"] = "electrical"
    part_details["type"] = "light_fixing_hardware_hook"
    part_details["size"] = ["68_mm_width"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""
    #adding amazon
    part_details["distributor_amazon"] = "B0BLYVQBV7"
    part_details["link_distributor_amazon"] = "https://www.amazon.co.uk/dp/B0BLYVQBV7"
    part_details["price_1_distributor_amazon"] = 6.99/5/1.2
    #current_price
    part_details["price_1"] = part_details["price_1_distributor_amazon"]
    parts.append(part_details)


    #wall wart
    part_details = {}
    part_details["classification"] = "electrical"
    part_details["type"] = "wall_wart"
    part_details["size"] = "240_volt_input"
    part_details["color"] = "uk_socket"
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""
    
    current_default = copy.deepcopy(part_details)

    description_mains = []
    #5v 4 amp
    description_mains.append("5_volt_4_amp_output")
    #9 v 600 ma
    description_mains.append("9_volt_0_6_amp_output")
    #12 v 2 amp
    description_mains.append("12_volt_2_amp_output")

    for description_main in description_mains:
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = description_main
        parts.append(part_details)
        




    oomp.add_parts(parts, make_files=make_files)
    