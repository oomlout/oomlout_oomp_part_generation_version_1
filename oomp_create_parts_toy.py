import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #green car
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
        part_details["link_distributor_amzon"] = f"https://www.amazon.com/dp/{part_details['distributor_amazon']}"
        parts.append(part_details)    

   
        


    oomp.add_parts(parts, make_files=make_files)
    