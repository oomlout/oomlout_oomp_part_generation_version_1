import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "hardware"
    part_details["type"] = "ziptie"
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = part_details.copy()

    
    #base
    if True:
        sizes = ["tiny", "small", "medium", "large", "extra_large"]

        description_mains = ["", "releasable", "with_mounting_hole", "standard"]
        for size in sizes:
            part_details = default_empty.copy()
            part_details["size"] = size
            parts.append(part_details)
    

        
            


   
    oomp.add_parts(parts, **kwargs)
    