import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []
   

    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "prototyping_breadboard"
    part_details["size"] = ["800_point","400_point"]
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = ""
    parts.append(part_details)
    

    #prototyping wire

    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "prototyping_jumper_wire"
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    
    part_details_base = part_details.copy()

    sizes = ["2_54_mm_dupont_socket_to_socket","2_54_mm_dupont_plug_to_plug","2_54_mm_dupont_plug_to_socket"]
    colors = ["rainbow_color"]
    description_mains = ["","40_multiple"]
    description_extras = ["200_mm_length"]
    for size in sizes:
        for color in colors:
            for description_main in description_mains:
                for description_extra in description_extras:
                    part_details = part_details_base.copy()
                    part_details["size"] = size
                    part_details["color"] = color
                    part_details["description_main"] = description_main
                    part_details["description_extra"] = description_extra
                    parts.append(part_details)

    oomp.add_parts(parts, **kwargs)
    