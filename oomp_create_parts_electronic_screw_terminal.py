import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part     
    # 3_5 mm green screw terminals
    if True:
        decription_mains = ["2_pin", "3_pin", "4_pin", "5_pin", "6_pin", "7_pin", "8_pin", "9_pin", "10_pin"]


        for description_main in decription_mains:
            part_details = {}
            part_details["classification"] = "electronic"
            part_details["type"] = "screw_terminal"
            part_details["size"] = "3_5_mm_pitch"
            part_details["color"] = "green"
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

        
        
    oomp.add_parts(parts, make_files=make_files)
    