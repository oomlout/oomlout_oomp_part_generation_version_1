import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "toy"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = copy.deepcopy(part_details)

    #ball
    if True:
        part_details = {}
        part_details["classification"] = "toy"
        part_details["type"] = "ball"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  

        default_current = copy.deepcopy(part_details)

        #small mixed
        part_details = copy.deepcopy(default_current)
        part_details["size"] = "small"
        part_details["description_main"] = "mixed"
        parts.append(part_details)

    #bubbles
    if True:
        part_details = {}
        part_details["classification"] = "toy"
        part_details["type"] = "bubble"
        part_details["size"] = "wand"
        part_details["color"] = ""
        part_details["description_main"] = "33_mm_diameter_370_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  
        part_details["distributor_amazon"] = "B0CLSHKHM1"
        part_details["link_distributor_amazon"] = f"https://www.amazon.com/dp/{part_details['distributor_amazon']}"
        parts.append(part_details)    

    #musical_instrument
    if True:
        part_details = {}
        part_details["classification"] = "toy"
        part_details["type"] = "musical_instrument"
        part_details["size"] = "ukulele"
        part_details["color"] = ""
        part_details["description_main"] = "170_mm_width_550_mm_height_55_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  
        parts.append(part_details)

    #figurine
    if True:
        part_details = {}
        part_details["classification"] = "toy"
        part_details["type"] = "figurine"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  

        default_current = copy.deepcopy(part_details)

        #branded
        #squishmallow
        part_details = copy.deepcopy(default_current)
        part_details["size"] = "branded"
        part_details["color"] = "squismallow"
        part_details["description_main"] = "small"
        parts.append(part_details)

        #num_nom
        part_details = copy.deepcopy(default_current)
        part_details["size"] = "branded"
        part_details["color"] = "num_nom"
        part_details["description_main"] = "mixed"    
        parts.append(part_details)


        #small animal
        part_details = copy.deepcopy(default_current)
        part_details["size"] = "small"
        part_details["description_main"] = "animal_mixed"
        parts.append(part_details)

        #medium animal
        part_details = copy.deepcopy(default_current)
        part_details["size"] = "medium"
        part_details["description_main"] = "animal_mixed"
        parts.append(part_details)

        #mixed
        part_details = copy.deepcopy(default_current)
        part_details["description_main"] = "mixed"
        parts.append(part_details)

    #gem and rock and mineral
    if True:
        part_details = {}
        part_details["classification"] = "toy"
        part_details["type"] = "gem_rock_mineral"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  

        default_current = copy.deepcopy(part_details)

        #gem
        part_details = copy.deepcopy(default_current)
        part_details["description_main"] = "collection_mixed"
        parts.append(part_details)


    #mixed
    if True:
        part_details = {}
        part_details["classification"] = "toy"
        part_details["type"] = "mixed"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  

        default_current = copy.deepcopy(part_details)

        part_details = copy.deepcopy(default_current)
        part_details["description_main"] = "party_bag_toy_mixed"

        parts.append(part_details)

    #remote_control
    if True:

        #aliexpress ones
        if True:
            part_details = {}
            part_details["classification"] = "toy"
            part_details["type"] = "remote_control"
            part_details["size"] = "2_4_ghz_controller"
            part_details["color"] = ""
            part_details["description_main"] = "stunt_car_green_95_mm_width_80_mm_height_40_mm_depth"
            part_details["description_extra"] = ""
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["short_name"] = ""  
            part_details["distributor_amazon"] = "B09FSFP7H2"
            part_details["link_distributor_amazon"] = f"https://www.amazon.com/dp/{part_details['distributor_amazon']}"
            parts.append(part_details)    
            
            part_details = {}
            part_details["classification"] = "toy"
            part_details["type"] = "remote_control"
            part_details["size"] = "2_4_ghz_controller"
            part_details["color"] = ""
            part_details["description_main"] = "stunt_car_green_165_mm_width_155_mm_height_75_mm_depth"
            part_details["description_extra"] = ""
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["short_name"] = ""  
            part_details["distributor_aliexpress"] = "1005006841176949"
            part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['distributor_aliexpress']}.html"
            parts.append(part_details)    

        #building block compatible
        if True:
            part_details = copy.deepcopy(default_empty)
            part_details["classification"] = "toy"
            part_details["type"] = "remote_control"
            part_details["size"] = "building_block_compatible"
            part_details["description_main"] = "4_channel_battery_included_32_mm_width_64_mm_height_30_mm_depth"
            part_details["distributor_aliexpress"] = "1005007006131635"
            part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['distributor_aliexpress']}.html"
            parts.append(part_details)

            part_details = copy.deepcopy(default_empty)
            part_details["classification"] = "toy"
            part_details["type"] = "remote_control"
            part_details["size"] = "building_block_compatible"
            part_details["description_main"] = "1_channel_battery_and_motor_included_24_mm_width_56_mm_height_32_mm_depth"
            part_details["distributor_aliexpress"] = "1005007142691134"
            part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['distributor_aliexpress']}.html"
            parts.append(part_details)

            #2_channel
            part_details = copy.deepcopy(default_empty)
            part_details["classification"] = "toy"
            part_details["type"] = "remote_control"
            part_details["size"] = "building_block_compatible"
            part_details["description_main"] = "2_channel_32_mm_width_32_mm_height_38_mm_depth"
            part_details["distributor_aliexpress"] = "1005003984563566"
            part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['distributor_aliexpress']}.html"
            parts.append(part_details)




    #digger
    if True:
        part_details = {}
        part_details["classification"] = "toy"
        part_details["type"] = "remote_control"
        part_details["size"] = "2_4_ghz_controller"
        part_details["color"] = ""
        part_details["description_main"] = "excavator_300_mm_width_105_mm_height_150_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "yi_gong_toys"
        part_details["part_number"] = "bc1044"
        part_details["part_number_exact"] = "BC1044"
        part_details["short_name"] = ""  
        part_details["distributor_aliexpress"] = "1005007659407993"
        part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['distributor_aliexpress']}.html"
        #amazon
        part_details["distributor_amazon"] = "B0D3KQQX6G"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
        parts.append(part_details) 

    #mechano
    if True:
        part_details = {}
        part_details["classification"] = "toy"
        part_details["type"] = "mechano"
        part_details["size"] = "car_remote_control"
        part_details["color"] = ""
        part_details["description_main"] = "lambourghini_huracan_green"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "mechano"
        part_details["part_number"] = ""
        part_details["short_name"] = ""  
        parts.append(part_details)    

        


    oomp.add_parts(parts, make_files=make_files)
    