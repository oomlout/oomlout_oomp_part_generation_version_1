import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    # ikea
    #   billy
    if True:
        part_details = {}
        part_details["classification"] = "dish"
        part_details["type"] = ""
        part_details["size"] = "ikea_oftast"
        part_details["color"] = "white"
        part_details["manufacturer"] = "ikea"

        ikea_ofstat_base = copy.deepcopy(part_details)

        part_details = copy.deepcopy(ikea_ofstat_base)
        part_details["description_main"] = "plate"
        part_details["description_extra"] = "250_mm_diameter"        
        part_details["part_number"] = "302_589_13"
        part_details["part_number_exact"] = part_details["part_number"].replace("_", ".")
        parts.append(part_details)

        #190 mm plate
        part_details = copy.deepcopy(ikea_ofstat_base)
        part_details["description_main"] = "plate"
        part_details["description_extra"] = "190_mm_diameter"
        part_details["part_number"] = "603_189_39"
        part_details["part_number_exact"] = part_details["part_number"].replace("_", ".")
        parts.append(part_details)

        #200 mm deep plate
        part_details = copy.deepcopy(ikea_ofstat_base)
        part_details["description_main"] = "plate_deep"
        part_details["description_extra"] = "200_mm_diameter"
        part_details["part_number"] = "003_189_42"
        part_details["part_number_exact"] = part_details["part_number"].replace("_", ".")
        parts.append(part_details)

        #110 mm bowl
        part_details = copy.deepcopy(ikea_ofstat_base)
        part_details["description_main"] = "bowl"
        part_details["description_extra"] = "110_mm_diameter"
        part_details["part_number"] = "904_671_12"
        part_details["part_number_exact"] = part_details["part_number"].replace("_", ".")
        parts.append(part_details)

        #150 mm bowl
        part_details = copy.deepcopy(ikea_ofstat_base)
        part_details["description_main"] = "bowl"
        part_details["description_extra"] = "150_mm_diameter"
        part_details["part_number"] = "802_589_15"
        part_details["part_number_exact"] = part_details["part_number"].replace("_", ".")
        parts.append(part_details)

        #230 mm serving bowl
        part_details = copy.deepcopy(ikea_ofstat_base)
        part_details["description_main"] = "bowl_serving"
        part_details["description_extra"] = "230_mm_diameter"
        part_details["part_number"] = "702_589_16"
        part_details["part_number_exact"] = part_details["part_number"].replace("_", ".")

        

        







        

    




    
    oomp.add_parts(parts, **kwargs)
    