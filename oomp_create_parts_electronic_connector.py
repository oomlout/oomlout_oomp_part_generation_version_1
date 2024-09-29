import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []
   

    #define a part    
    part_details = {}
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "connector"
    part_details["size"] = ["wago_221"]
    part_details["color"] = [""]    
    part_details["description_extra"] = ""
    part_details["kicad_reference"] = "L"

    part_wago_base = copy.deepcopy(part_details)

    #2 pole
    part_details = copy.deepcopy(part_wago_base)
    part_details["description_main"] = ["2_pole"]
    part_details["manufacturer"] = "wago"
    part_details["part_number"] = "221_412"
    part_details["part_number_exact"] = "221-412"    
    part_details["distributor_screwfix"] = "8421R"
    part_details["distributor_screwfix_link"] = "https://www.screwfix.com/p/8421r"
    parts.append(part_details)

    #3 pole
    part_details = copy.deepcopy(part_wago_base)
    part_details["description_main"] = ["3_pole"]
    part_details["manufacturer"] = "wago"
    part_details["part_number"] = "221_413"
    part_details["part_number_exact"] = "221-413"
    part_details["distributor_screwfix"] = "2803R"
    part_details["distributor_screwfix_link"] = "https://www.screwfix.com/p/2803r"
    parts.append(part_details)

    #5 pole
    part_details = copy.deepcopy(part_wago_base)
    part_details["description_main"] = ["5_pole"]
    part_details["manufacturer"] = "wago"
    part_details["part_number"] = "221_415"
    part_details["part_number_exact"] = "221-415"    
    part_details["distributor_screwfix"] = "5201R"
    part_details["distributor_screwfix_link"] = "https://www.screwfix.com/p/5201r"
    parts.append(part_details)
    
    #2 pole inline
    part_details = copy.deepcopy(part_wago_base)
    part_details["description_main"] = ["2_pole_inline"]
    part_details["manufacturer"] = "wago"
    part_details["part_number"] = "221_2411"
    part_details["part_number_exact"] = "221-2411"    
    part_details["distributor_screwfix"] = "148RU"
    part_details["distributor_screwfix_link"] = "https://www.screwfix.com/p/148ru"
    parts.append(part_details)

    
    

    oomp.add_parts(parts, **kwargs)
    