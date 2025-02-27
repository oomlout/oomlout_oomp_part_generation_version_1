import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    

    parts = []

    part_details = {}
    part_details["classification"] = "electronic_consumer"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = copy.deepcopy(part_details)

    # usb charger
    if True:
        part_details = copy.deepcopy(default_empty)
        part_details["type"] = "charger_usb"
        part_details["size"] = "4_port"
        part_details["description_main"] = "91_5_mm_width_59_mm_height_29_5_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "ravpower"
        part_details["part_number_exact"] = "RP-PC024"
        part_details["part_number"] = part_details["part_number_exact"].replace("-","_").lower()
        part_details["link_distributor_ravpower"] = "https://cdn.shopify.com/s/files/1/0257/5656/5579/files/RP-PC024_User_Manual.pdf?28651"
        parts.append(part_details)

    


    oomp.add_parts(parts, make_files=make_files)
    