import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    
    #      diode    
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "diode"
    part_details["size"] = ["sod_123"]
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = "package_marking_t4"
    part_details["manufacturer"] = ""
    part_details["part_number"] = "1n4148w"
    part_details["kicad_reference"] = "D"
    parts.append(part_details)
    
    #      shottky
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "diode_schottky"
    part_details["size"] = ["sod_123"]
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = "package_marking_b2"
    part_details["manufacturer"] = ""
    part_details["part_number"] = "mbr0520"
    part_details["kicad_reference"] = "D"
    parts.append(part_details)

    
    oomp.add_parts(parts, **kwargs)
    