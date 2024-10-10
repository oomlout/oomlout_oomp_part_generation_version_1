import oomp

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
        pass

    oomp.add_parts(parts, **kwargs)
    