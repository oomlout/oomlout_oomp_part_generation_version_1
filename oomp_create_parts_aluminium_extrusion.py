import oomp
import copy

def load_parts(**kwargs):
    print(f"  loading parts {__name__}")
    
    parts = []

    # standard
    if True:
        part_details = {}
        part_details["classification"] = "aluminium extrusion"
        part_details["type"] = "2020"
        part_details["size"] = ""
        part_details["color"] = ""    
        part_details["description_main"] = ""    
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["kicad_reference"] = ""
        part_default = copy.deepcopy(part_details)
        
        
        part_details = copy.deepcopy(part_default)

        part_details["link_buy"] = "https://www.aluminium-profile.co.uk/20x20-aluminium-profile-kjn992888"
        parts.append(part_details)    

        

        lengths = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

        for length in lengths:
            part_details = copy.deepcopy(part_default)        
            part_default["description_main"] = f"{length}_mm_length"
            parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    