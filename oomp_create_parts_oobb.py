import oomp
import pickle

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    

    # basic
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "header"
    part_details["size"] = ["oobb"]
    part_details["color"] = ["basic","i2c"]
    part_details["description_main"] = ["single","double","triple"]
    part_details["description_extra"] = "through_hole_right_angle"
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)

    
    #load from file
    folder_things = "C:/gh/oomlout_oobb_version_4"
    file_pickle = f"{folder_things}/temporary/things.pickle"
    with open(file_pickle, "rb") as infile:
        things = pickle.load(infile)

    for part_id in things:
        part = things[part_id]
        part_details = {}
        part_details["classification"] = "oobb"
        part_details["type"] = "part"
        part_details["size"] = "oobb"
        part_details["color"] = ""
        id = part["id"]
        id = id.replace("oobb_","")

        part_details["description_main"] = f"{id}"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        part_details["distributors"] = []  
        parts.append(part_details)
        

    
    oomp.add_parts(parts, make_files=make_files)
    