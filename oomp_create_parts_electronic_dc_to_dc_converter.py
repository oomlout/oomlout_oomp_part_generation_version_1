import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "dc_to_dc_converter"
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = part_details.copy()

    
    #buck_style
    if True:
        current_item = copy.deepcopy(part_details)
        current_item["size"] = "buck_style"

        default_local = copy.deepcopy(default_empty)
        #color 300 watt 20 amp
        current_item["color"] = "300_watt_20_amp"
        #description_main 52 mm width 60 mm length blue pcb
        current_item["description_main"] = "52_mm_width_60_mm_length_blue_pcb"
        current_item["description_extra"] = ""
        current_item["manufacturer"] = "aliexpress"
        current_item_mounting_hole_width = 39
        current_item["mounting_hole_width"] = current_item_mounting_hole_width
        current_item_mounting_hole_length = 53
        current_item["mounting_hole_length"] = current_item_mounting_hole_length
        current_item_mounting_hole_size = "m3"
        current_item["mounting_hole_size"] = current_item_mounting_hole_size

        parts.append(current_item)
        

    #buck_boost_style
            
            #boost_style
    

        
            


   
    oomp.add_parts(parts, **kwargs)
    