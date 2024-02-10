import oomp

def load_parts(**kwargs):
    print(f"  loading parts {__name__}")
    
    parts = []

    # standard
    if True:
        part_details = {}
        part_details["classification"] = "hardware"
        part_details["type"] = ["aluminium_extrusion"]
        part_details["size"] = ["2020"]
        part_details["color"] = ["grey"]    
        part_details["description_main"] = ["","890_mm_length"]    
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["kicad_reference"] = ""
        parts.append(part_details)    


    oomp.add_parts(parts, **kwargs)
    