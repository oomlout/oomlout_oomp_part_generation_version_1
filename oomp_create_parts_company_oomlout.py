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
    part_details["description_main"] = ["hardware_screw_countersunk_m3_black_hex_head"]
    part_details["description_extra"] = ["version_1"]
    part_details["manufacturer"] = "oomlout"
    part_details["part_number"] = "ptcs3bhv1"
    parts.append(part_details)

    # electrical
    part_details = {}
    part_details["classification"] = "company_oomlout"
    part_details["type"] = "product"
    part_details["size"] = ["prototyping_tin"]
    part_details["color"] = [""]
    part_details["description_main"] = ["hardware_screw_socket_cap_m3_black_hex_head","hardware_screw_countersunk_socket_cap_m2_5_black_hex_head","electronic_crimp_bootlace_ferrule_mixed","electronic_crimp_bootlace_ferrule_0_55_mm_diameter_wire_rainbow_8_mm_length","electronic_led_5_mm_rainbow_tint","electronic_heatshrink_2_to_1_shrink_ratio_mixed"]
    part_details["description_extra"] = ["version_1"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    parts.append(part_details)

    oomp.add_parts(parts, **kwargs)
    