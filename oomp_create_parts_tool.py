import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []
    
    # chiller
    if True:
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

    
    # diy tool
    #   drill
    if True:
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

    
    # electrical
    if True:
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

    # knife
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "knife_utility"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = ["17_mm_blade"]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)

        #bin disposal can
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "knife_utility_blade_disposal_can"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = [""]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = "olfa"
        part_details["part_number"] = "dc_3"
        part_details["part_number_exact"] = "DC-3"
        parts.append(part_details)

    #laser cutter
    if True:
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


    # scale
    if True:
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

        
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "scale"
        part_details["size"] = ["70_mm_width_120_mm_height_40_mm_depth"]
        part_details["color"] = [""]
        part_details["description_main"] = ["200_gram_capacity"]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = "jewelry_scale"
        parts.append(part_details)


        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "scale"
        part_details["size"] = ["67_mm_width_120_mm_height_18_mm_depth"]
        part_details["color"] = [""]
        part_details["description_main"] = ["500_gram_capacity"]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = "jewelry_scale"
        parts.append(part_details)


    # screwdriver bits
    #define a part 
    if True:
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


    # tape measure
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "measure_tape_measure"
        part_details["size"] = ["5000_mm_length"]
        part_details["color"] = [""]
        part_details["description_main"] = [""]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = "stanley"
        part_details["part_number"] = "1_30_696"
        part_details["part_number_esact"] = "1-30-696"
        parts.append(part_details)

    
    # vibratory_bowl
    if True:
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

    

    
    

    
    oomp.add_parts(parts, **kwargs)
    