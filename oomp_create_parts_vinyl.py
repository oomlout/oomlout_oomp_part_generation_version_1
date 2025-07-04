import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    base = {}
    base["classification"] = "vinyl"
    base["size"] = ""
    base["type"] = ""    
    base["color"] = ""
    base["description_main"] = ""
    base["description_extra"] = ""
    base["manufacturer"] = ""
    base["part_number"] = ""    

    default_empty = copy.deepcopy(base)

    # a sizes
    
    #a0
    part_details = base.copy()
    part_details["description_extra"] = "a0_841_mm_width_1189_mm_height"
    part_details["width"] = "841 mm"
    part_details["height"] = "1189 mm"
    parts.append(part_details)

    #a1
    part_details = base.copy()
    part_details["description_extra"] = "a1_594_mm_width_841_mm_height"
    part_details["width"] = "594 mm"
    part_details["height"] = "841 mm"
    parts.append(part_details)

    #a2
    part_details = base.copy()
    part_details["description_extra"] = "a2_420_mm_width_594_mm_height"
    part_details["width"] = "420 mm"
    part_details["height"] = "594 mm"
    parts.append(part_details)

    #a3
    part_details = base.copy()
    part_details["description_extra"] = "a3_297_mm_width_420_mm_height"
    part_details["width"] = "297 mm"
    part_details["height"] = "420 mm"
    parts.append(part_details)


    #a4    
    part_details = base.copy()
    part_details["description_extra"] = "a4_210_mm_width_297_mm_height"
    part_details["width"] = "210 mm"
    part_details["height"] = "297 mm"    
    parts.append(part_details)
    base_a4 = part_details.copy()


    #roll
    part_details = base.copy()
    part_details["description_extra"] = "1260_mm_width_roll"
    part_details["width"] = "1260 mm"    
    parts.append(part_details)

    base_roll = part_details.copy()

    
    # 100 gram bright white
    if True:        
        bases = []
        bases.append(base_a4.copy())
        bases.append(base_roll.copy())

        colors = []
        colors.append("white")
        colors.append("clear")
        colors.append("white_weave")
        colors.append("gold")
        colors.append("purple")
        colors.append("green_matte")
        colors.append("green")
        colors.append("orange_matte")
        colors.append("yellow")
        colors.append("red")

        for base in bases:
            for color in colors:
                part_details = default_empty.copy()
                part_details.update(base)
                part_details["color"] = color                
                parts.append(part_details)


        
        
    


    oomp.add_parts(parts, **kwargs)
    