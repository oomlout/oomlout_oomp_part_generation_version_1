import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    # parts
    part_details = {}
    part_details["classification"] = "three_d_printer"
    part_details["type"] = "part"
    part_details["size"] = "filament"
    part_details["color"] = "generic"
    part_details["description_main"] = "ptfe_tube"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    parts.append(part_details)    

    
    part_details = {}
    part_details["classification"] = "three_d_printer"
    part_details["type"] = "part"
    part_details["size"] = "filament"
    part_details["color"] = "generic"
    part_details["description_main"] = "ptfe_tube_connector_push_lock"
    part_details["description_extra"] = "m6"
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    parts.append(part_details)    
    
    part_details = {}
    part_details["classification"] = "three_d_printer"
    part_details["type"] = "part"
    part_details["size"] = "filament"
    part_details["color"] = "generic"
    part_details["description_main"] = "ptfe_tube_connector_push_lock"
    part_details["description_extra"] = "m10"
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    parts.append(part_details)    
    
    
    
    oomp.add_parts(parts, make_files=make_files)
    