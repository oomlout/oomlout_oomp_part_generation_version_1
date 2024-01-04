import oomp

def load_parts(**kwargs):
    print(f"  loading parts {__name__}")
    
    parts = []

    # screw_flat_head black hex head
    if True:
        extras_sizes = {}
        extras_sizes["m3_id_7_mm_od"] = [4,5,6,8,10,12,15,20,25,30]
        
        
        for size in extras_sizes:
            part_details = {}
            part_details["classification"] = "hardware"
            part_details["type"] = ["spacer"]
            sizes = [size]
            part_details["size"] = []
            for size in sizes:
                part_details["size"].append(f"{size}")
            part_details["color"] = ["nylon_white"]
            lengths = extras_sizes[size]
            part_details["description_main"] = []
            for length in lengths:
                part_details["description_main"].append(f"{length}_mm_length")
            part_details["description_extra"] = ""
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["kicad_reference"] = ""
            parts.append(part_details)    
    

    
    oomp.add_parts(parts, **kwargs)
    