import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    #sizes
    #basic        
    sizes = []
    size_aa =  ("aa_size_14_mm_diameter_50_mm_depth")
    sizes.append(size_aa)
    size_aaa =  ("aaa_size_10_mm_diameter_44_mm_depth")
    sizes.append(size_aaa)
    size_c =  ("c_size_26_mm_diameter_50_mm_depth")
    sizes.append(size_c)
    size_d =  ("d_size_34_mm_diameter_61_mm_depth")
    sizes.append(size_d)
    size_9_volt =  ("9_volt_15_mm_width_16_mm_height_48_mm_depth")
    sizes.append(size_9_volt)
    
    #extra
    size_18650 =  ("18650_size_18_mm_diameter_65_mm_depth")
        
        
    # basic
    if True:
        part_details = {}
        part_details["classification"] = "electronic"
        part_details["type"] = "battery"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["part_number_exact"] = ""
        part_details["short_name"] = ""  
        
        
        battery_basic_default = copy.deepcopy(part_details)

        for size in sizes:
            part_details = copy.deepcopy(battery_basic_default)
            part_details["size"] = size
            part_details["color"] = "alkaline_1_5_volt_non_rechargable"            
            parts.append(part_details)

        
        
        
    #lithium
    if True:
        part_details = copy.deepcopy(battery_basic_default)        
        part_details["color"] = "lithium_3_7_volt_rechargable"        

        lithium_pigtail_default = copy.deepcopy(part_details)

        sizes = []
        sizes.append(size_aa)
        sizes.append(size_18650)

        description_mains = []
        description_mains.append("")
        description_mains.append("pigtail_crimp_housing_2_5_mm_jst_sm_latching_2_pin_socket")

        for size in sizes:
            for description_main in description_mains:
                part_details = copy.deepcopy(lithium_pigtail_default)
                part_details["size"] = size
                part_details["description_main"] = description_main
                parts.append(part_details)

    oomp.add_parts(parts, make_files=make_files)
    