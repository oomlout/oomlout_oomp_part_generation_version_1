import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #casters
    if True:
        part_details = {}
        part_details["classification"] = "mechanical"
        part_details["type"] = "wheel"
        part_details["size"] = "caster"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  
        
        part_default = part_details

        #100 mm red     
        part_details = copy.deepcopy(part_default)
        part_details["description_main"] = "100_mm_diameter_red_rubber_wheel"
        part_details["description_extra"] = "93_mm_width_62_mm_height_bracket_m8_mounting_hole"
        part_details["short_name"] = "Caster Wheel 100mm Red"  
        parts.append(part_details)

        #100 mm white plastice
        part_details = copy.deepcopy(part_default)
        part_details["description_main"] = "100_mm_diameter_white_plastic_wheel"
        part_details["description_extra"] = "105_mm_width_85_mm_height_bracket_m8_mounting_hole"
        part_details["short_name"] = "Caster Wheel 100mm White"
        parts.append(part_details)

        #25 mm
        part_details = copy.deepcopy(part_default)
        part_details["description_main"] = "25_mm_diameter_brown_plastic_wheel"
        part_details["description_extra"] = "39_mm_width_33_mm_height_bracket_m4_mounting_hole"
        part_details["short_name"] = "Caster Wheel 25mm Black"
        part_details["part_number_distributor_amazon"] = "B0B83T6G8P"
        part_details["link_buy"] = f"https://www.amazon.com/dp/{part_details['part_number_distributor_amazon']}"
        parts.append(part_details)

        #10 mm diameter roller ball
        part_details = copy.deepcopy(part_default)
        part_details["description_main"] = "10_mm_diameter_roller_plastic"
        part_details["description_extra"] = "deodorant_roller"
        part_details["short_name"] = "Roller Ball 10mm Diameter"
        parts.append(part_details)

    #n20 wheel
    if True:
        part_details = {}
        part_details["classification"] = "mechanical"
        part_details["type"] = "wheel"
        part_details["size"] = "3_mm_diameter_d_shape_shaft"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  
        
        part_default = copy.deepcopy(part_details)

        part_details = copy.deepcopy(part_default)
        part_details["description_main"] = "34_mm_diameter_9_mm_depth"
        part_details["name_short"] = "Wheel 34mm Diameter 3 mm D Shape Shaft" 
        parts.append(part_details)

        part_details = copy.deepcopy(part_default)
        part_details["description_main"] = "80_mm_diameter_10_mm_depth"
        part_details["name_short"] = "Wheel 80mm Diameter 3 mm D Shape Shaft"
        part_details["part_number_distributor_pololu"] = "1434"
        part_details["link_distributor_pololu"] = f"https://www.pololu.com/product/{part_details['part_number_distributor_pololu']}"
        parts.append(part_details)
    


    oomp.add_parts(parts, make_files=make_files)
    