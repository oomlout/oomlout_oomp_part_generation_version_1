import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    #flange
    if True:
        part_details = {}
        part_details["classification"] = "mechanical"
        part_details["type"] = "coupler"
        part_details["size"] = "flange"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  
        
        part_default = copy.deepcopy(part_details)

        description_mains = [3,4,5,6,8,10,12,14,16,18,20]

        for description_main in description_mains:
            part_details = copy.deepcopy(part_default)
            part_details["description_main"] = f"{description_main}_mm_bore"
            parts.append(part_details)
        

    oomp.add_parts(parts, make_files=make_files)
    