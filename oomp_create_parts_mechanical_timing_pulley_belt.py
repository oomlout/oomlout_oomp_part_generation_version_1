import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #gt2 belts
    if True:
        part_details = {}
        part_details["classification"] = "mechanical"
        part_details["type"] = "timing_belt"
        part_details["size"] = "2gt_2_mm_pitch"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  
        
        part_default = copy.deepcopy(part_details)

        colors = []
        colors.append("6_mm_belt_width")

        teeth = []
        start = 100
        max = 200
        step = 2
        for i in range(start,max,step):
            teeth.append(i)

        for color in colors:
            for tooth in teeth:
                part_details = copy.deepcopy(part_default)
                part_details["color"] = color
                part_details["description_main"] = f"{tooth}_teeth_{tooth*2}_mm_circumference"
                parts.append(part_details)

        #2gt pulley
        if True:
            part_details = {}
            part_details["classification"] = "mechanical"
            part_details["type"] = "timing_pulley"
            part_details["size"] = "2gt_2_mm_pitch"
            part_details["color"] = ""
            part_details["description_main"] = ""
            part_details["description_extra"] = ""
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["short_name"] = ""
            
            part_default = copy.deepcopy(part_details)

            colors = []
            colors.append("6_mm_belt_width")

            descrpiption_mains = [12,14,15,16,17,18,19,20,21,22,24,25,26,30,36,60,72,100]

            descrpiption_extras = []
            descrpiption_extras.append("3_mm_bore")            
            descrpiption_extras.append("5_mm_bore")
            descrpiption_extras.append("6_mm_bore")
            descrpiption_extras.append("8_mm_bore")

            for color in colors:
                for description_main in descrpiption_mains:
                    for description_extra in descrpiption_extras:
                        part_details = copy.deepcopy(part_default)
                        part_details["color"] = color
                        part_details["description_main"] = f"{description_main}_teeth"
                        part_details["description_extra"] = description_extra
                        parts.append(part_details)


    oomp.add_parts(parts, make_files=make_files)
    