import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    sizes = []
    #1x1
    sizes.append("25_mm_width_25_mm_length")
    #1.5x1
    sizes.append("38_1_mm_width_25_4_mm_length")
    #2x1
    sizes.append("50_8_mm_width_25_4_mm_length")
    #2x2
    sizes.append("50_8_mm_width_50_8_mm_length")
    #3x2
    sizes.append("76_2_mm_width_50_8_mm_length")
    #3x3
    sizes.append("76_2_mm_width_76_2_mm_length")
    #4x4
    sizes.append("101_6_mm_width_101_6_mm_length")
    #6x4
    sizes.append("152_4_mm_width_101_6_mm_length")

    styles = ["direct_thermal_style", "transfer_thermal_style"]

    for size in sizes:
        for style in styles:
            part_details = {}
            part_details["classification"] = "packaging"
            part_details["type"] = "label"
            part_details["size"] = size
            part_details["color"] = "white"
            part_details["description_main"] = "paper"
            part_details["description_extra"] = style
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["short_name"] = ""  
            parts.append(copy.deepcopy(part_details))
     
    
    


    oomp.add_parts(parts, make_files=make_files)
    