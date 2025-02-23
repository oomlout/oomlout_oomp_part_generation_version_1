import oomp
import copy

def load_parts(**kwargs):
    print(f"  loading parts {__name__}")
    
    parts = []

    
    #screw_countersunk pozi drive
    if True:
        extras_sizes = {}
        extras_sizes["m2"] = [4,5,6,8,10,12,16]
        extras_sizes["m2_5"] = [5,6,8,10,12,16,20]
        extras_sizes["m3"] = [5,6,8,10,12,16,20,25]
        extras_sizes["m3_5"] = [8,10,12,16]
        extras_sizes["m4"] = [6,8,10,12,16,20,25,30,40,50,60]
        extras_sizes["m5"] = [8,10,12,14,16,20,25,30,35,40,50,60,70,80,100]
        extras_sizes["m6"] = [10,12,16,20,25,30,40,100,120]    
        for size in extras_sizes:
            part_details = {}
            part_details["classification"] = "hardware"
            part_details["type"] = ["screw_countersunk"]
            sizes = [size]
            part_details["size"] = []
            for size in sizes:
                part_details["size"].append(f"{size}")
            part_details["color"] = ["bright_zinc_plated"]
            lengths = extras_sizes[size]
            part_details["description_main"] = []
            for length in lengths:
                part_details["description_main"].append(f"{length}_mm_length")
            part_details["description_extra"] = "pozidrive_head"
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["kicad_reference"] = ""
            parts.append(part_details)    
    
    
    # screw_countersunk black hex head
    if True:
        extras_sizes = {}
        extras_sizes["m2"] = [3,5,6,8,10,12,14,16,20,22,25]
        extras_sizes["m3"] = [4,5,6,8,10,12,16,20,25,30,35]
        extras_sizes["m4"] = [6,8,10,12,16,20,25,30,35,40]    
        
        for size in extras_sizes:
            part_details = {}
            part_details["classification"] = "hardware"
            part_details["type"] = ["screw_countersunk"]
            sizes = [size]
            part_details["size"] = []
            for size in sizes:
                part_details["size"].append(f"{size}")
            part_details["color"] = ["black"]
            lengths = extras_sizes[size]
            part_details["description_main"] = []
            for length in lengths:
                part_details["description_main"].append(f"{length}_mm_length")
            part_details["description_extra"] = "hex_head"
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["kicad_reference"] = ""
            parts.append(part_details)    
    


    # screw_countersunk black phillips head
    if True:
        extras_sizes = {}        
        extras_sizes["m1_4"] = [3,4,5,6,8,10]
        extras_sizes["m1_5"] = [3,4,5,6,8,10]
        extras_sizes["m1_6"] = [3,4,5,6,8,10]
        extras_sizes["m2"] = [3,4,5,6,7,8,10,12,14,16,18,20,22,25,30]
        
        for size in extras_sizes:
            part_details = {}
            part_details["classification"] = "hardware"
            part_details["type"] = ["screw_countersunk"]
            sizes = [size]
            part_details["size"] = []
            for size in sizes:
                part_details["size"].append(f"{size}")
            part_details["color"] = ["black"]
            lengths = extras_sizes[size]
            part_details["description_main"] = []
            for length in lengths:
                part_details["description_main"].append(f"{length}_mm_length")
            part_details["description_extra"] = "phillips_head"
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["kicad_reference"] = ""
            parts.append(part_details)    
    
    # screw_flat_head black phillips
    if True:
        extras_sizes = {}
        extras_sizes["m2"] = [3,4,5,6,8,10,12,14,16,20,22,25]
        extras_sizes["m2_5"] = [3,4,5,6,8,10,12,14,16,20,22,25]
        extras_sizes["m3"] = [4,5,6,8,10,12,14,16,18,20,22,25,30]
        extras_sizes["m4"] = [5,6,8,10,12,14,16,18,20,22,25,30,35,40]
        extras_sizes["m5"] = [6,8,10,12,14,16,18,20,22,25,30,35,40]
        extras_sizes["m6"] = [6,8,10,12,14,16,18,20,22,25,30,35,40,45,50]
        
        heads = ["phillips_head", "hex_head"]

        for size in extras_sizes:
            for head in heads:
                part_details = {}
                part_details["classification"] = "hardware"
                part_details["type"] = ["screw_flat_head"]
                sizes = [size]
                part_details["size"] = []
                for size in sizes:
                    part_details["size"].append(f"{size}")
                part_details["color"] = ["black"]
                lengths = extras_sizes[size]
                part_details["description_main"] = []
                for length in lengths:
                    part_details["description_main"].append(f"{length}_mm_length")
                part_details["description_extra"] = head
                part_details["manufacturer"] = ""
                part_details["part_number"] = ""
                part_details["kicad_reference"] = ""
                parts.append(part_details)    
    
        
    #screw_grub
    if True:
        colors = []
        colors.append("black")
        colors.append("stainless_steel")

        extras_sizes = {}
        extras_sizes["m1_6"] = [2,2.5,3,4,5,8]
        extras_sizes["m2"] = [2,2.5,3,4,5,6,8,10,12,14]
        extras_sizes["m2_5"] = [2,2.5,3,4,5,6,8,10,12,14]
        extras_sizes["m3"] = [2,2.5,3,4,5,6,8,10,12,14,16,18,20]
        extras_sizes["m4"] = [3,4,5,6,8,10,12,14,16,18,20]
        extras_sizes["m5"] = [3,4,5,6,8,10,12,14,16,18,20,25,30,35]
        extras_sizes["m6"] = [6,8,10,12,14,16,18,20,30,40]
        
        part_details = {}
        part_details["classification"] = "hardware"
        part_details["type"] = "screw_grub"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = "hex_head"
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""

        default_screw_grub = part_details

        import copy

        for color in colors:
            for size in extras_sizes:
                part_details = copy.deepcopy(default_screw_grub)
                part_details["color"] = color
                part_details["size"] = size
                default_current = part_details                
                lengths = extras_sizes[size]
                for length in lengths:
                    part_details = copy.deepcopy(default_current)
                    length_string = str(length)
                    length_string = length_string.replace(".","_")                    
                    part_details["description_main"] = f"{length_string}_mm_length"
                    parts.append(part_details)
        
    #screw_machine_screw pozi drive
    if True:
        extras_sizes = {}
        extras_sizes["m2"] = [4,6,8,10,12]
        extras_sizes["m3"] = [4,5,6,8,10,12,16,20,25,30,35,40]
        extras_sizes["m3_5"] = [5,8,10,12,16,20,25]
        extras_sizes["m4"] = [5,6,8,10,12,16,20,25,30,35,40,45,50,60,70,80,90,100]
        extras_sizes["m5"] = [6,8,10,12,14,16,20,25,30,35,40,50,60,80,100]
        extras_sizes["m6"] = [8,10,12,16,20,25,30,35,40,100,120]    
        for size in extras_sizes:
            part_details = {}
            part_details["classification"] = "hardware"
            part_details["type"] = ["screw_machine_screw"]
            sizes = [size]
            part_details["size"] = []
            for size in sizes:
                part_details["size"].append(f"{size}")
            part_details["color"] = [""]
            lengths = extras_sizes[size]
            part_details["description_main"] = []
            for length in lengths:
                part_details["description_main"].append(f"{length}_mm_length")
            part_details["description_extra"] = "pozidrive_head"
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["kicad_reference"] = ""
            parts.append(part_details)    
    
    #screw_machine_screw phillips nylon_white
    if True:
        extras_sizes = {}
        extras_sizes["m3"] = [12,16,20,25]
        for size in extras_sizes:
            part_details = {}
            part_details["classification"] = "hardware"
            part_details["type"] = ["screw_machine_screw"]
            sizes = [size]
            part_details["size"] = []
            for size in sizes:
                part_details["size"].append(f"{size}")
            part_details["color"] = ["nylon_white"]
            lengths = extras_sizes[size]
            part_details["description_main"] = []
            for length in lengths:
                part_details["description_main"].append(f"{length}_mm_length")
            part_details["description_extra"] = "phillips_head"
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["kicad_reference"] = ""
            parts.append(part_details)    

    #screw_self_tapping_phillips
    if True:
        extras_sizes = {}
        extras_sizes["m1"] = [3,5]
        extras_sizes["m1_2"] = [3,5,8]
        extras_sizes["m1_4"] = [3,5,8,10]
        extras_sizes["m1_7"] = [5,8,10,12,16]
        extras_sizes["m2"] = [5,8,12,16,20]
        extras_sizes["m2_3"] = [5,6,8,10,12,16,20]
        
        for size in extras_sizes:
            part_details = {}
            part_details["classification"] = "hardware"
            part_details["type"] = ["screw_self_tapping"]
            sizes = [size]
            part_details["size"] = []
            for size in sizes:
                part_details["size"].append(f"{size}")
            part_details["color"] = ["black"]
            lengths = extras_sizes[size]
            part_details["description_main"] = []
            for length in lengths:
                part_details["description_main"].append(f"{length}_mm_length")
            part_details["description_extra"] = "phillips_head"
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["kicad_reference"] = ""
            parts.append(part_details)    
    

    #screw_socket_cap
    if True:
        extras_sizes = {}
        extras_sizes["m2"] = [3,4,5,6,8,10,12,14,16,18,20,25]
        extras_sizes["m2_5"] = [4,5,6,8,10,12,16,20,25]
        extras_sizes["m3"] = [5,6,8,10,12,18,16,20,25,30,35,40,45,50,60]
        extras_sizes["m4"] = [4,6,8,10,12,14,16,20,25,30,35,40,45,50,60,65,70,75]
        extras_sizes["m5"] = [6,8,10,12,14,16,20,25,30,35,40,45,50,60,65,70,75,80,90,100,110,120]
        extras_sizes["m6"] = [8,12,16,20,25,30,35,40,45,50,60,65,70,80,90,100]    
        for size in extras_sizes:
            part_details = {}
            part_details["classification"] = "hardware"
            part_details["type"] = ["screw_socket_cap"]
            sizes = [size]
            part_details["size"] = []
            for size in sizes:
                part_details["size"].append(f"{size}")
            part_details["color"] = ["black"]
            lengths = extras_sizes[size]
            part_details["description_main"] = []
            for length in lengths:
                part_details["description_main"].append(f"{length}_mm_length")
            part_details["description_extra"] = "hex_head"
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["kicad_reference"] = ""
            parts.append(part_details)    
    
    #screw_thread_forming_phillips
    if True:
        extras_sizes = {}
        extras_sizes["m2_3"] = [6]
        extras_sizes["m2_5"] = [6]
        extras_sizes["m2_6"] = [6]
        for size in extras_sizes:
            part_details = {}
            part_details["classification"] = "hardware"
            part_details["type"] = ["screw_thread_forming"]
            sizes = [size]
            part_details["size"] = []
            for size in sizes:
                part_details["size"].append(f"{size}")
            part_details["color"] = ["black"]
            lengths = extras_sizes[size]
            part_details["description_main"] = []
            for length in lengths:
                part_details["description_main"].append(f"{length}_mm_length")
            part_details["description_extra"] = "phillips_head"
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["kicad_reference"] = ""
            parts.append(part_details)    
    
    #add corefix
    if True:
        part_details = {}
        part_details["classification"] = "hardware"
        part_details["type"] = "screw_wood"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = "10_mm_diameter_100_mm_length"
        part_details["description_extra"] = "pozidrive_head"
        part_details["manufacturer"] = "corefix"
        part_details["part_number"] = ""
        part_details["short_name"] = ""        
        part_details["part_number_exact"] = ""    
        part_details["distributor_screwfix"] = "344hg"
        part_details["distributor_screwfix_link"] = f"https://www.screwfix.com/p/{part_details['distributor_screwfix']}"
        parts.append(part_details)


        part_details = {}
        part_details["classification"] = "hardware"
        part_details["type"] = "screw_wood"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = "10_mm_diameter_120_mm_length"
        part_details["description_extra"] = "pozidrive_head"
        part_details["manufacturer"] = "corefix"
        part_details["part_number"] = ""
        part_details["short_name"] = ""        
        part_details["part_number_exact"] = ""    
        part_details["distributor_screwfix"] = "401hg"
        part_details["distributor_screwfix_link"] = f"https://www.screwfix.com/p/{part_details['distributor_screwfix']}"
        parts.append(part_details)



    #add screwtite screws
    if True:
        part_details = {}
        part_details["classification"] = "hardware"
        part_details["type"] = "screw_wood"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = "3_5_mm_diameter_50_mm_length"
        part_details["description_extra"] = "pozidrive_head"
        part_details["manufacturer"] = "screw_tite_two"
        part_details["part_number"] = "726FY"
        part_details["short_name"] = ""
        parts.append(part_details)

        import copy
        screwtire_base = copy.deepcopy(part_details)

        part_details = copy.deepcopy(screwtire_base)
        part_details["description_main"] = "3_5_mm_diameter_30_mm_length"
        part_details["part_number"] = "488FY"
        parts.append(part_details)

        #5mm x 100 mm
        part_details = copy.deepcopy(screwtire_base)
        part_details["description_main"] = "5_mm_diameter_100_mm_length"
        part_details["part_number"] = "486FY"
        parts.append(part_details)

        # 5 mm 90 mm
        part_details = copy.deepcopy(screwtire_base)
        part_details["description_main"] = "5_mm_diameter_90_mm_length"
        part_details["part_number"] = "800FY"
        parts.append(part_details)



    
    oomp.add_parts(parts, **kwargs)
    