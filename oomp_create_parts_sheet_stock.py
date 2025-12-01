import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "sheet_stock"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = part_details.copy()


    description_mains_default = []
    description_mains_default.append("")
    description_mains_default.append("2440_mm_width_1220_mm_height")
    description_mains_default.append("600_mm_width_400_mm_height")
    
    
    #mdf
    if True:
        current_item = {"type": "mdf"}
        sizes = []
        sizes.append("3mm_depth")
        
        description_mains = copy.deepcopy(description_mains_default)
        
        manufacturers = []
        manufacturers.append("")
        manufacturers.append("medite")

        for size in sizes:
            for description_main in description_mains:
                for manufacturer in manufacturers:
                    part = copy.deepcopy(default_empty)
                    part.update(current_item)            
                    part["size"] = size
                    part["description_main"] = description_main
                    parts.append(copy.deepcopy(part))

    #acrylic
    if True:
        current_item = {"type": "acrylic"}
        sizes = []
        sizes.append("3mm_depth")
        sizes.append("6mm_depth")
        
        description_mains = copy.deepcopy(description_mains_default)
        
        colors = []
        colors.append("")
        colors.append("clear")
        colors.append("black")
        colors.append("white")
        colors.append("red")
        colors.append("blue")
        colors.append("green")
        colors.append("yellow")

        manufacturers = []
        manufacturers.append("")
        manufacturers.append("perspex")

        for size in sizes:
            for description_main in description_mains:
                for color in colors:
                    for manufacturer in manufacturers:
                        part = copy.deepcopy(default_empty)
                        part.update(current_item)            
                        part["size"] = size
                        part["color"] = color
                        part["description_main"] = description_main
                        part["manufacturer"] = manufacturer
                        parts.append(copy.deepcopy(part))

    #plywood
    if True:
        current_item = {"type": "plywood"}
        sizes = []
        sizes.append("3mm_depth")
        sizes.append("6mm_depth")
        sizes.append("12mm_depth")
        sizes.append("18mm_depth")
        
        description_mains = copy.deepcopy(description_mains_default)
        

        for size in sizes:
            for description_main in description_mains:                
                part = copy.deepcopy(default_empty)
                part.update(current_item)            
                part["size"] = size
                part["description_main"] = description_main                
                parts.append(copy.deepcopy(part))       


   
    oomp.add_parts(parts, **kwargs)
    