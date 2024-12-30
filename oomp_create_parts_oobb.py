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
        #print(part_id)
        part = things[part_id]
        size = part["type"]
        
        wid = part.get("width", 0)
        hei = part.get("height", 0)
        thick = part.get("thickness", 0)
        description_main = f"{wid}_width_{hei}_height_{thick}_depth"
        #remove anything after "ex_" in the description
        
        size = part["size"] #different in oobb
        
        attributes = ["width","height","diameter","thickness"]
        description_main = ""
        for attribute in attributes:
            test_value = part.get(attribute, "")
            if test_value != "":
                #if it's a list
                if isinstance(test_value, list):
                    attribute_new = ""
                    for value in test_value:
                        attribute_new += f"{value}_"
                    test_value = attribute_new[:-1]
                if description_main != "":
                    description_main += "_"
                attribute_name = attribute
                if attribute == "thickness":
                    attribute_name = "mm_depth"
                description_main += f"{test_value}_{attribute_name}"
        
        #remove anything after "ex_" in the description
        string_extra = ""
        tests = ["bearing","shaft","extra","bearing_name","radius_name","depth","oring_type"]
        for test in tests:
            if test in part:
                deet = part.get(test, "")
                #if it's a list
                if isinstance(deet, list):
                    attribute_new = ""
                    for value in deet:
                        attribute_new += f"{value}_"
                    deet = attribute_new[:-1]
                if deet != "":
                    if string_extra != "":
                        string_extra += "_"
                    string_extra += f"{deet}_{test}"        
                    string_extra.replace(".0_","_")
                    string_extra.replace(".","d")
        description_extra = string_extra

        part_details = {}
        part_details["classification"] = "oobb"
        part_details["type"] = "part"
        part_details["size"] = size
        part_details["color"] = ""
        
        part_details["description_main"] = description_main
        part_details["description_extra"] = description_extra
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        
        id_parts = ["classification","type","size","color","description_main","description_extra","manufacturer","part_number"]
        id = ""
        for id_part in id_parts:
            value = part_details.get(id_part, "")
            if value != "":
                id += f"{part_details[id_part]}_"
        id = id[:-1]
        id = id.replace(".0_","_")
        id = id.replace(".","d")
        part_details["id"] = id 
        if "part_part" in id:
            print(part_details)
        


        parts.append(part_details)
        

    
    oomp.add_parts(parts, make_files=make_files)
    