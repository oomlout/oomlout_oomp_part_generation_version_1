import oomp

def load_parts(**kwargs):
    print(f"  loading parts {__name__}")
    
    parts = []

    #nylon_white_standoff
    if True:
        extras_sizes = {}
        extras_sizes["m3"] = [6,9,12,15,20,25,30]
        # bolt
        for size in extras_sizes:
            part_details = {}
            part_details["classification"] = "hardware"
            part_details["type"] = ["standoff"]
            sizes = [size]
            part_details["size"] = []
            for size in sizes:
                part_details["size"].append(f"{size}")
            part_details["color"] = [""]
            lengths = extras_sizes[size]
            part_details["description_main"] = []
            for length in lengths:
                part_details["description_main"].append(f"{length}_mm_length")
            part_details["description_extra"] = "nut_and_nut"
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["kicad_reference"] = ""
            parts.append(part_details)    
 
    




    oomp.add_parts(parts, **kwargs)
    