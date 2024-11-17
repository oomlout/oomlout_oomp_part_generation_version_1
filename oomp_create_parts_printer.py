import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    #print_time]
    part_details = {}
    part_details["classification"] = "printer"
    part_details["type"] = "all_in_one_inkjet"
    part_details["size"] = ["a4"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "canon"
    part_details["part_number"] = "ts5350"
    part_details["short_name"] = "Printer Canon TS5350"  
    parts.append(part_details)    
    
   

    oomp.add_parts(parts, make_files=make_files)
    