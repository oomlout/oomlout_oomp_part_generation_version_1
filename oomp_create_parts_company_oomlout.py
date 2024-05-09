import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    # electrical
    part_details = {}
    part_details["classification"] = "company_oomlout"
    part_details["type"] = "product"
    part_details["size"] = ["prototyping_tin"]
    part_details["color"] = [""]
    part_details["description_main"] = ["hardware_screw_countersunk_m3_black_hex_head_version_1"]
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = "oomlout"
    part_details["part_number"] = "ptcs3bhv1"
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    