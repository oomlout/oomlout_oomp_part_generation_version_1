import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "hardware"
    part_details["type"] = "ball_bearing"
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = copy.deepcopy(part_details)

    sizes = ["1_mm","1_5_mm","2_mm","2_5_mm","3_mm","3_5_mm","4_mm","4_5_mm","5_mm","5_5_mm","6_mm","6_5_mm","7_mm","7_5_mm","8_mm","8_5_mm","9_mm","9_5_mm","10_mm","11_mm","12_mm","13_mm","14_mm","15_mm","16_mm","17_mm","18_mm","19_mm","20_mm"]

    #basic
    if True:
        for size in sizes:
            part_details = copy.deepcopy(default_empty)
            part_details["size"] = size
            parts.append(part_details)
        



    oomp.add_parts(parts, make_files=make_files)
    