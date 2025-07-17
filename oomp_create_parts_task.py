import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "task"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = part_details.copy()

    
    if True:
        
        #cleaning      
        current_item = {"type": "printer", "size": "inkjet", "color": "cleaning"}
        description_mains = []
        description_mains.append("syringe_and_small_cleaner")
        description_mains.append("large_claner_and_funnel")
        description_mains.append("overflow")
        for description_main in description_mains:
            part = copy.deepcopy(default_empty)
            part.update(current_item)            
            part["description_main"] = description_main
            parts.append(copy.deepcopy(part))

        #filling
        current_item = {"type": "printer", "size": "inkjet", "color": "ink_filling"}
        description_mains = []
        description_mains.append("sublimation_ecotank")
        description_mains.append("dtf_epson_stylus_pro_4800")
        for description_main in description_mains:
            part = copy.deepcopy(default_empty)
            part.update(current_item)            
            part["description_main"] = description_main
            parts.append(copy.deepcopy(part))
        
        

        
            


   
    oomp.add_parts(parts, **kwargs)
    