import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []
    

    #caliper
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "measure_caliper_digital"
        part_details["size"] = "150_mm_length"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "mitutoyo"
        part_details["part_number_exact"] = "MIT500-196-30"
        part_details["part_number"] = part_details["part_number_exact"].lower().replace("-","_").replace(" ","_").replace(".","_")
        part_details["part_number_distributor_amazon"] = "B00IG46NL2"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/gp/product/{part_details['part_number_distributor_amazon']}"
        parts.append(part_details)

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


    # screwdriver
    #define a part 
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "screw_driver_precision_powered"
        part_details["size"] = "17_mm_diameter_160_mm_depth"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "xiaomi"
        part_details["part_number"] = ""

        default_current = copy.deepcopy(part_details)

        part_details = copy.deepcopy(default_current)
        part_details["diameter"] = 17
        part_details["depth"] = 160
        parts.append(part_details)

        part_details = copy.deepcopy(default_current)
        part_details["description_main"] = "set"
        part_details["width"] = 75
        part_details["height"] = 202
        part_details["depth"] = 26
        
        parts.append(part_details)
        
    

    # screwdriver bits
    #define a part 
    if True:      

        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "screw_driver_bit"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        
        default_screwdriver_bit = copy.deepcopy(part_details)

        #100 mm depth
        if True:
            part_details = copy.deepcopy(default_screwdriver_bit)
            part_details["size"] = "quarter_inch_drive_100_mm_depth"
            default_current = copy.deepcopy(part_details)

            #hex_head
            description_extras = ["2_mm","2_5_mm","3_mm","4_mm","5_mm","6_mm"]
            for description_extra in description_extras:
                part_details = copy.deepcopy(default_current)
                part_details["description_main"] = "hex_head"
                part_details["description_extra"] = description_extra
                part_details["part_number_distributor_aliexpress"] = "1005007111223127"
                part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['part_number_distributor_aliexpress']}.html"
                parts.append(part_details)

        #150 mm depth
        if True:
            part_details = copy.deepcopy(default_screwdriver_bit)
            part_details["size"] = "quarter_inch_drive_150_mm_depth"
            default_current = copy.deepcopy(part_details)

            #hex_head
            description_extras = ["1_5_mm","2_mm", "2_5_mm","3_mm","4_mm","5_mm","6_mm"]
            for description_extra in description_extras:
                part_details = copy.deepcopy(default_current)
                part_details["description_main"] = "hex_head"
                part_details["description_extra"] = description_extra
                part_details["part_number_distributor_aliexpress"] = "1005007848287320"
                part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['part_number_distributor_aliexpress']}.html"
                parts.append(part_details)
            




    # tape measure
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "measure_tape_measure"
        part_details["size"] = "5000_mm_length"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "stanley"
        part_details["part_number"] = "1_30_696"
        part_details["part_number_exact"] = "1-30-696"
        part_details["part_number_distributor_amazon"] = "B000Y8W54C"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/gp/product/{part_details['part_number_distributor_amazon']}"
        part_details["oobb_tool_holder_shape"] = "cube"
        part_details["oobb_tool_holder_width"] = 78
        part_details["oobb_tool_holder_height"] = 74
        part_details["oobb_tool_holder_depth"] = 42

        parts.append(part_details)

        
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "measure_tape_measure"
        part_details["size"] = "3000_mm_length"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "stanley"
        part_details["part_number"] = "0_30_686"
        part_details["part_number_exact"] = "0-30-686"
        part_details["part_number_distributor_amazon"] = "B0009VX1ZQ"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/gp/product/{part_details['part_number_distributor_amazon']}"
        part_details["oobb_tool_holder_shape"] = "cube"
        part_details["oobb_tool_holder_width"] = 65
        part_details["oobb_tool_holder_height"] = 60
        part_details["oobb_tool_holder_depth"] = 30 
        
        parts.append(part_details)


    # tool box

    # timer
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "timer"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = ["80_mm_diameter_30_mm_depth_black"]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["part_number_distributor_amazon"] = "B07VNWZCZH"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/gp/product/{part_details['part_number_distributor_amazon']}"
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
    