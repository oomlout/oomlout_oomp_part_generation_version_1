import oomp

def load_parts(**kwargs):
    print(f"  loading parts {__name__}")
    
    parts = []

    extras_sizes = {}
    extras_sizes["2_mm"] = [6,8,10,12]
    extras_sizes["2_5_mm"] = [4,5,6,8,10,20]
    extras_sizes["3_mm"] = [5,6,8,10,12,16,20,25,30,35,40,50]
    extras_sizes["4_mm"] = [4,6,8,10,12,14,16,20,25,30,35,40,45,50,60,65,70,75]
    extras_sizes["5_mm"] = [6,8,10,12,14,16,20,25,30,35,40,45,50,60,65,70,75,80,90,100,110,120]
    extras_sizes["6_mm"] = [8,12,16,20,25,30,35,40,45,50,60,65,70,80,90,100]
    # bolt
    for size in extras_sizes:
        part_details = {}
        part_details["classification"] = "hardware"
        part_details["type"] = ["screw_socket_cap"]
        sizes = [size]
        part_details["size"] = []
        for size in sizes:
            part_details["size"].append(f"{size}_mm")
        part_details["color"] = ["black"]
        lengths = extras_sizes[size]
        part_details["description_main"] = []
        for length in lengths:
            part_details["description_main"].append(f"{length}_mm")
        part_details["description_extra"] = "hex_head"
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["kicad_reference"] = ""
        parts.append(part_details)    
    
    extras_sizes = {}
    extras_sizes["3_mm"] = [6,8,10,12,16,20,25,30,35]
    extras_sizes["4_mm"] = [6,8,10,12,16,20,25,30,35,40]    
    # bolt
    for size in extras_sizes:
        part_details = {}
        part_details["classification"] = "hardware"
        part_details["type"] = ["screw_countersunk"]
        sizes = [size]
        part_details["size"] = []
        for size in sizes:
            part_details["size"].append(f"{size}_mm")
        part_details["color"] = ["black"]
        lengths = extras_sizes[size]
        part_details["description_main"] = []
        for length in lengths:
            part_details["description_main"].append(f"{length}_mm")
        part_details["description_extra"] = "hex_head"
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["kicad_reference"] = ""
        parts.append(part_details)    
    
    
    oomp.add_parts(parts, **kwargs)
    