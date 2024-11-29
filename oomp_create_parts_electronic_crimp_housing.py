import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    
    #dupont
    if True:
        #headers up to 40 pin
        #define a part 
        part_details = {}
        part_details["classification"] = "electronic"
        part_details["type"] = "crimp_housing"
        part_details["size"] = ["2_54_mm"]
        part_details["color"] = ["black"]
        part_details["description_main"] = []
        # add 1- 40 _pin
        for pin_count in range(1, 21):
            part_details["description_main"].append(f"{pin_count}_pin")
        part_details["description_extra"] = ["dupont"]
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["kicad_reference"] = "CRHO"
        #add the part to the list of parts
        parts.append(part_details)

    #jst
    if True:
        #      2_5 sm
        part_details = {}
        part_details["classification"] = "electronic"
        part_details["type"] = "crimp_housing"
        part_details["size"] = "2_5_mm_jst_sm_latching"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["kicad_reference"] = "CONN"
        
        pins = [1,2,3,4,5,6,7,8,9,10]
        description_extras = ["plug","socket"]
            
        for pin_count in pins:
            for description_extra in description_extras:
                part_details["description_main"] = f"{pin_count}_pin"
                part_details["description_extra"] = description_extra
                parts.append(part_details) 


    oomp.add_parts(parts, make_files=make_files)
    