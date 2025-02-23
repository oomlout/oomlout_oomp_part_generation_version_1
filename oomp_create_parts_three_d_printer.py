import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    

    part_details = {}
    part_details["classification"] = "three_d_printer"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = part_details

    parts = []

    #nozzle
    if True:
        part_details = copy.deepcopy(default_empty)
        part_details["type"] = "nozzle"

        default_current = part_details

        sizes = []
        sizes.append("volcano_1_75_mm_filament")
        
        colors = ["brass"]

        description_mains = ["0_2_mm_diameter_nozzle","0_4_mm_diameter_nozzle","0_6_mm_diameter_nozzle","0_8_mm_diameter_nozzle","1_0_mm_diameter_nozzle","1_2_mm_diameter_nozzle"]

        for size in sizes:
            for color in colors:
                for description_main in description_mains:
                    part_details = copy.deepcopy(default_current)
                    part_details["size"] = size
                    part_details["color"] = color
                    part_details["description_main"] = description_main
                    parts.append(part_details)

    # ptfe
    if True:
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
    