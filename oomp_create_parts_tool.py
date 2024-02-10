import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    # screwdriver bits
    #define a part 
    part_details = {}
    part_details["classification"] = "tool"
    part_details["type"] = "screw_driver_bit"
    part_details["size"] = ["quarter_inch_drive_100_mm_depth"]
    part_details["color"] = [""]
    part_details["description_main"] = ["hex_head"]
    part_details["description_extra"] = ["2_mm","2_5_mm"]
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    parts.append(part_details)

    

    

    
    oomp.add_parts(parts, **kwargs)
    