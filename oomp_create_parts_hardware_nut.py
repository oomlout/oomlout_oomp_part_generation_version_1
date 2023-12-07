import oomp

def load_parts(**kwargs):
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "hardware"
    part_details["type"] = ["nut"]    
    part_details["size"] = ["1_mm", "1_5_mm", "2_mm","2_5_mm","2_7_mm","3_mm","4_mm","5_mm","6_mm","8_mm"]
    part_details["color"] = [""]    
    part_details["description_main"] = ["", "flanged", "locking"]    
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = ""
    parts.append(part_details)    


    
    oomp.add_parts(parts, **kwargs)
    