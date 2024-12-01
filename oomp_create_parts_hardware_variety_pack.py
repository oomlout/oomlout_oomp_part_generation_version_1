import oomp
import copy

def load_parts(**kwargs):
    print(f"  loading parts {__name__}")
    
    parts = []

    
    #electronic jst
    if True:
        part_details = {}
        part_details["classification"] = "hardware"
        part_details["type"] = "variety_pack"
        part_details["size"] = "electronic_crimp_housing_header_2_5_mm_jst_xh"
        part_details["color"] = ""    
        part_details["description_main"] = "with_pre_crimped_cable"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = ""
        part_details["part_number_distributor_aliexpress"] = "1005006126557275"
        part_details["link_aliepress"] = f"https://www.aliexpress.com/item/{part_details["part_number_distributor_aliexpress"]}.html"
        part_details["kicad_reference"] = ""
        part_details["search_term_aliexpress"] = "2.54mm XH Connector Socket Kit with Pre-Crimped Cable Wire 2/3/4/5/6/7 Pin Housing JST Adapter Cable Male and Female Compatible"
        parts.append(part_details)

    # screw_flat_head
    if True:
        part_details = {}
        part_details["classification"] = "hardware"
        part_details["type"] = "variety_pack"
        part_details["size"] = "screw_flat_head"
        part_details["color"] = "720_pieces"    
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
    