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
    part_details["type"] = "heatshrink_2_to_1_shrink_ratio"
    part_details["size"] = ["101_6_mm_internal_diameter","76_2_mm_internal_diameter","50_8_mm_internal_diameter","38_1_mm_internal_diameter","32_mm_internal_diameter,""25_4_mm_internal_diameter","19_mm_internal_diameter","12_7_mm_internal_diameter","9_5_mm_internal_diameter","6_4_mm_internal_diameter","3_2_mm_internal_diameter","2_4_mm_internal_diameter","1_6_mm_internal_diameter","1_2_mm_internal_diameter"]
    part_details["color"] = ["black","brown","orange","red","white","gray","blue","green","black","yellow","clear"]
    part_details["description_main"] = ["30000_mm_length","25_mm_length","15_mm_length","10_mm_length"]
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = ""
    #add the part to the list of parts
    parts.append(part_details)



    oomp.add_parts(parts, make_files=make_files)
    