import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    #4 digit 7 segment display
    if True:
        part_details = {}
        part_details["classification"] = "electronic" 
        part_details["type"] = "display"
        part_details["size"] = "4_digit_7_segment_9_mm_height"
        part_details["color"] = ""
        part_details["description_main"] = "42_mm_width_24_mm_height_blue_pcb"
        part_details["description_extra"] = "i2c_addressable"
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["part_number_exact"] = ""
        part_details["short_name"] = "" 

        current_default = copy.deepcopy(part_details)

        colours = [""]

        for colour in colours:
            part_details = copy.deepcopy(current_default)
            part_details["color"] = colour

        parts.append(part_details)

    #16x2 lcd
    if True:
        part_details = {}
        part_details["classification"] = "electronic" 
        part_details["type"] = "display"
        part_details["size"] = "16_x_2_character"
        part_details["color"] = "black_on_green"
        part_details["description_main"] = "80_mm_width_36_mm_height"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["part_number_exact"] = ""
        part_details["short_name"] = ""  




    oomp.add_parts(parts, make_files=make_files)
    