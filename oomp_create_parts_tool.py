import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    # electrical
    part_details = {}
    part_details["classification"] = "tool"
    part_details["type"] = "electrical_meter_clamp"
    part_details["size"] = [""]
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = "aneng"
    part_details["part_number"] = "st180"
    parts.append(part_details)

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

    # scale
    part_details = {}
    part_details["classification"] = "tool"
    part_details["type"] = "scale"
    part_details["size"] = ["76_mm_width_114_mm_height_20_mm_depth"]
    part_details["color"] = [""]
    part_details["description_main"] = ["200_gram_capacity", "1000_gram_capacity"]
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = "aliexpress"
    part_details["part_number"] = "jewelry_scale"
    parts.append(part_details)


    # vibratory_bowl
    part_details = {}
    part_details["classification"] = "tool"
    part_details["type"] = "vibratory_bowl"
    part_details["size"] = ["tabletop"]
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = "mettler_toledo"
    part_details["part_number"] = "lv11"
    parts.append(part_details)

    

    # diy tool
    #   drill
    #       dewalt
    part_details = {}
    part_details["classification"] = "tool"
    part_details["type"] = "drill_hammer"
    part_details["size"] = ["18_volt_dewalt_tower"]
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = "dewalt"
    part_details["part_number"] = "dc988"
    parts.append(part_details)
    #       ryobi
    part_details = {}
    part_details["classification"] = "tool"
    part_details["type"] = "drill_hammer"
    part_details["size"] = ["18_volt_ryobi_one"]
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = "ryobi"
    part_details["part_number"] = "r18pd3"
    parts.append(part_details)

    
    #laser cutter
    part_details = {}
    part_details["classification"] = "tool"
    part_details["type"] = "laser_cutter"
    part_details["size"] = ["1200_mm_width_900_mm_height"]
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = "hpc_laser"
    part_details["part_number"] = "1290"
    parts.append(part_details)

    # chiller
    part_details = {}
    part_details["classification"] = "tool"
    part_details["type"] = "water_chiller"
    part_details["size"] = ["420_mm_width_350_mm_height_500_mm_depth"]
    part_details["color"] = [""]
    part_details["description_main"] = [""]
    part_details["description_extra"] = [""]
    part_details["manufacturer"] = "hpc_laser"
    part_details["part_number"] = "cw4000"
    parts.append(part_details)


    

    
    oomp.add_parts(parts, **kwargs)
    