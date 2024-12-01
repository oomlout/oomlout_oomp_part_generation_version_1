import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 
    # motor_geared
    #      n20
    if True:
        part_details = {}
        part_details["classification"] = "mechanical"
        part_details["type"] = "motor_geared"
        part_details["size"] = "n20"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  


        n20_default = copy.deepcopy(part_details)
        voltages = ["3_volt", "6_volt", "12_volt"]
        rpms = [15, 30, 50, 60, 100, 200, 300, 500, 1000] 
        shafts = ["3_mm_diameter_10_mm_length_d_shape_shaft"]

        for voltage in voltages:
            for rpm in rpms:
                for shaft in shafts:
                    part_details = copy.deepcopy(n20_default)
                    part_details["color"] = f"{voltage}"
                    part_details["description_main"] = f"{rpm}_rpm"
                    part_details["description_extra"] = shaft
                    parts.append(part_details)

        # n20 holder
        part_details = copy.deepcopy(n20_default)
        part_details["size"] = "n20_holder"
        part_details["description_main"] = "35_mm_width_12_mm_height_24_mm_depth"

        parts.append(part_details)    

    #servo_remote_control
    if True:
        part_details = {}
        part_details["classification"] = "mechanical"
        part_details["type"] = "motor_servo_remote_control"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  

        servo_default = copy.deepcopy(part_details)

        sizes = ["micro", "mini", "standard", "large"]
        for size in sizes:
            part_details = copy.deepcopy(servo_default)
            part_details["description_main"] = size
            parts.append(part_details)

        #sg90
        part_details = copy.deepcopy(servo_default)
        part_details["size"] = "micro"
        servo_micro_default = copy.deepcopy(part_details)
        descriptions = ["sg90", "mg90s"]
        for description in descriptions:
            part_details = copy.deepcopy(servo_micro_default)
            part_details["description_main"] = description
            parts.append(part_details)

        #sg90 pcb
        part_details = copy.deepcopy(servo_default)
        part_details["size"] = "micro"
        part_details["description_main"] = "sg90"
        part_details["description_extra"] = "pcb"
        parts.append(part_details)
        


    #motor_stepper
    if True:
        part_details = {}
        part_details["classification"] = "mechanical"
        part_details["type"] = "motor_stepper"
        part_details["size"] = "nema_17"
        part_details["color"] = ""
        part_details["description_main"] = "42_mm_width_42_mm_height_48_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  
        parts.append(part_details)    

    #      tt
    if True:
        part_details = {}
        part_details["classification"] = "mechanical"
        part_details["type"] = "motor_geared"
        part_details["size"] = "tt"
        part_details["color"] = ""
        part_details["description_main"] = "standard"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  
        parts.append(part_details)    
        

    # motor_with_encoder
    #      
    if True:
        # motor_with_encoder
        #      cricut_maker_compatible
        part_details = {}
        part_details["classification"] = "mechanical"
        part_details["type"] = "motor_with_encoder"
        part_details["size"] = "30_mm_diameter"
        part_details["color"] = ""
        part_details["description_main"] = "cricut_maker_compatible"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  
        parts.append(part_details)    


        


    oomp.add_parts(parts, make_files=make_files)
    