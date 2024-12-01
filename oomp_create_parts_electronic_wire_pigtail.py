import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    # basic
    if True:
        sizes = []
        sizes.append("crimp_housing_2_5_mm_jst_sm_latching_2_pin_plug")
        sizes.append("crimp_housing_2_5_mm_jst_sm_latching_2_pin_socket")
        
        for size in sizes:
            part_details = {}
            part_details["classification"] = "electronic"
            part_details["type"] = "wire_pigtail"
            part_details["size"] = size
            part_details["color"] = "black_and_red_color"
            part_details["description_main"] = "100_mm_length"
            part_details["description_extra"] = ""
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["part_number_exact"] = ""
            part_details["short_name"] = ""  
            parts.append(part_details)    
        
        
        
    
    oomp.add_parts(parts, make_files=make_files)
    