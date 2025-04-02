import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "hardware"
    part_details["type"] = "magnet"
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = part_details.copy()

    # countersunk disc
    if True:
        size_list = []
        size_list.append([15,3])
        size_list.append([15,2])

        for magnet_size in size_list:
            part_details = default_empty.copy()
            part_details["size"] = "disc"
            part_details["color"] = "m3_countersunk"
            part_details["description_main"] = f"{magnet_size[0]}_mm_diameter_{magnet_size[1]}_mm_depth"
            parts.append(part_details.copy())



        

    
    oomp.add_parts(parts, **kwargs)
    