import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []
   
    #barrel jack to terminal strip
    if True:
        #define a part    
        part_details = {}
        part_details = {}
        part_details["classification"] = "electronic"
        part_details["type"] = "connector"
        part_details["size"] = "screw_terminal_5_mm_pitch_2_pin"
        part_details["color"] = ""    
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "L"
        part_details["part_number"] = ""
        part_details["kicad_reference"] = "L"

        current_default = copy.deepcopy(part_details)

        description_mains = []
        description_mains.append("2_1_mm_barrel_plug")
        description_mains.append("2_1_mm_barrel_socket")

        for description_main in description_mains:
            part_details = copy.deepcopy(current_default)
            part_details["description_main"] = description_main
            parts.append(part_details)




    #banana plugs
    if True:
        #define a part    
        part_details = {}
        part_details["classification"] = "electronic"
        part_details["type"] = "connector"
        part_details["size"] = "banana_style_4_mm"
        part_details["color"] = ""    
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        

        part_banana_plug_base = copy.deepcopy(part_details)

        colors = ["mix","red", "black", "green", "yellow", "blue"]

        description_mains = []
        description_mains.append("banana_plug_plastic_basic")
        description_mains.append("banana_socket_panel_mount_basic")
        description_mains.append("banana_socket_and_spade_connect_panel_mount")

        for description_main in description_mains:
            for color in colors:
                part_details = copy.deepcopy(part_banana_plug_base)
                part_details["description_main"] = description_main
                part_details["color"] = color
                parts.append(part_details)

        #

    

    #wago
    if True:
        #define a part    
        part_details = {}
        part_details = {}
        part_details["classification"] = "electronic"
        part_details["type"] = "connector"
        part_details["size"] = ["wago_221"]
        part_details["color"] = [""]    
        part_details["description_extra"] = ""
        part_details["kicad_reference"] = "L"

        part_wago_base = copy.deepcopy(part_details)

        #2 pole
        part_details = copy.deepcopy(part_wago_base)
        part_details["description_main"] = ["2_pole"]
        part_details["manufacturer"] = "wago"
        part_details["part_number"] = "221_412"
        part_details["part_number_exact"] = "221-412"    
        part_details["distributor_screwfix"] = "8421R"
        part_details["distributor_screwfix_link"] = "https://www.screwfix.com/p/8421r"
        parts.append(part_details)

        #3 pole
        part_details = copy.deepcopy(part_wago_base)
        part_details["description_main"] = ["3_pole"]
        part_details["manufacturer"] = "wago"
        part_details["part_number"] = "221_413"
        part_details["part_number_exact"] = "221-413"
        part_details["distributor_screwfix"] = "2803R"
        part_details["distributor_screwfix_link"] = "https://www.screwfix.com/p/2803r"
        parts.append(part_details)

        #5 pole
        part_details = copy.deepcopy(part_wago_base)
        part_details["description_main"] = ["5_pole"]
        part_details["manufacturer"] = "wago"
        part_details["part_number"] = "221_415"
        part_details["part_number_exact"] = "221-415"    
        part_details["distributor_screwfix"] = "5201R"
        part_details["distributor_screwfix_link"] = "https://www.screwfix.com/p/5201r"
        parts.append(part_details)
        
        #2 pole inline
        part_details = copy.deepcopy(part_wago_base)
        part_details["description_main"] = ["2_pole_inline"]
        part_details["manufacturer"] = "wago"
        part_details["part_number"] = "221_2411"
        part_details["part_number_exact"] = "221-2411"    
        part_details["distributor_screwfix"] = "148RU"
        part_details["distributor_screwfix_link"] = "https://www.screwfix.com/p/148ru"
        parts.append(part_details)

    
       

    oomp.add_parts(parts, **kwargs)
    