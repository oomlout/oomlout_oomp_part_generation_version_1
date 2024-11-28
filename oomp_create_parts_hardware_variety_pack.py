import oomp
import copy

def load_parts(**kwargs):
    print(f"  loading parts {__name__}")
    
    parts = []

    
    # standard
    if True:
        part_details = {}
        part_details["classification"] = "hardware"
        part_details["type"] = "variety_pack"
        part_details["size"] = "screw_flat_head"
        part_details["color"] = ""    
        part_details["description_main"] = "m_1_4_and_m_1_7_and_m_2_5_and_m_3_short_length"
        part_details["description_extra"] = "philips_drive"
        part_details["manufacturer"] = "nexsync"
        part_details["part_number"] = ""
        part_details["part_number_distributor_aliexpress"] = "1005008013912576"
        part_details["link_aliepress"] = f"https://www.aliexpress.com/item/{part_details["part_number_distributor_aliexpress"]}.html"
        part_details["kicad_reference"] = ""
        part_details["search_term_aliexpress"] = "720 PCS Small Computer Screws Assortment Kit, Black Tiny Eyeglass Screws, PC & Laptop SSD Hard Drive CPU Cooler Screw"
        parts.append(part_details)    

    
    
    oomp.add_parts(parts, **kwargs)
    