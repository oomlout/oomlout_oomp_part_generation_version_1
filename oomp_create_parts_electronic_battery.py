import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

        
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
        part_details["distributors"] = ""
        
        battery_basic_default = copy.deepcopy(part_details)

        sizes = []
        sizes.append("aa_14_mm_diameter_50_mm_depth")

    
    oomp.add_parts(parts, make_files=make_files)
    