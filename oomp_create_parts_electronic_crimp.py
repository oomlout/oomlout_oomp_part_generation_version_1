import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    
    # bootlace
    # 0.55 mm
    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "crimp_bootlace_ferrule"
    part_details["size"] = ["0_55_mm_diameter_wire","0_8_mm_diameter_wire","1_mm_diameter_wire"]
    part_details["color"] = ["brown","orange","red","white","gray","blue","green","black","yellow"]
    part_details["description_main"] = ["8_mm_length"]
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = ""
    #add the part to the list of parts
    parts.append(part_details)



    oomp.add_parts(parts, make_files=make_files)
    