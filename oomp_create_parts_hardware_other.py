import oomp
import copy

def load_parts(**kwargs):
    print(f"  loading parts {__name__}")
    
    parts = []

    # shelf peg
    if True:
        part_details = {}
        part_details["classification"] = "hardware"
        part_details["type"] = "shelf_support_peg"
        part_details["size"] = "5_mm"
        part_details["color"] = ""    
        part_details["description_main"] = "plastic"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""

        part_details["distributor_amazon"] = "B0CC1YRZP6"
        part_details["distributor_amazon_link"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
        part_details["price_1_distributor_amazon"] = 6.99/20/1.2

        parts.append(part_details)    

    # picture hanging hook
    if True:
        #5 mm width, 24 mm height, 8 mm depth, 9000 g weight capacity
        part_details = {}
        part_details["classification"] = "hardware"
        part_details["type"] = "hook_picture_hanging"
        part_details["size"] = ""
        part_details["color"] = "brass"    
        part_details["description_main"] = "5_mm_width_24_mm_height_8_mm_depth"
        part_details["description_extra"] = "9000_g_weight_capacity"
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""

        part_details["distributor_amazon"] = "B0CSBNN2R1"
        part_details["distributor_amazon_link"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
        parts.append(part_details)

        # 5 mm width, 26 mm height, 9 mm depth, 13500 g weight capacity
        part_details = copy.deepcopy(part_details)
        part_details["description_main"] = "5_mm_width_26_mm_height_9_mm_depth"
        part_details["description_extra"] = "13500_g_weight_capacity"
        parts.append(part_details)

        # 6_5 mm width, 36 mm height, 12 mm depth, 22500 g weight capacity
        part_details = copy.deepcopy(part_details)
        part_details["description_main"] = "6_5_mm_width_36_mm_height_12_mm_depth"
        part_details["description_extra"] = "22500_g_weight_capacity"
        parts.append(part_details)





    oomp.add_parts(parts, **kwargs)
    