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
        sizes = ["3_5_mm_pitch", "5_mm_pitch"]

        for description_main in decription_mains:
            for size in sizes:
                part_details = {}
                part_details["classification"] = "electronic"
                part_details["type"] = "screw_terminal"
                part_details["size"] = size
                part_details["color"] = "green"
                part_details["description_main"] = description_main
                part_details["description_extra"] = ""
                part_details["manufacturer"] = ""
                part_details["part_number"] = ""
                part_details["part_number_exact"] = ""
                part_details["short_name"] = ""  
                parts.append(copy.deepcopy(part_details))
        
        

        
        
    oomp.add_parts(parts, make_files=make_files)
    