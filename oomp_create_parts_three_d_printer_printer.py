import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    #print_time]
    if True:
        part_details = {}
        part_details["classification"] = "three_d_printer"
        part_details["type"] = "printing"
        part_details["size"] = ["low_quality"]
        part_details["color"] = [""]
        part_details["description_main"] = "minute"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""  
        part_details["price_per"] = 0
        part_details["price_per_gram"] = 0
        part_details["price_current"] = 0
        part_details["price_per_kilogram"] = 0
        parts.append(part_details)    
    
    # printers
    if True:
    
        #anycubic
        if True:
            part_details = {}
            part_details["classification"] = "three_d_printer"
            part_details["type"] = "printer"
            part_details["size"] = [""]
            part_details["color"] = [""]
            part_details["description_main"] = ""
            part_details["description_extra"] = ""
            part_details["manufacturer"] = "anycubic"
            part_details["part_number"] = "vyper"
            part_details["short_name"] = ""  
            parts.append(part_details)    

            #spare part
            if True:
                #spare parts
                #anycubic vyper category
                part_details = {}
                part_details["classification"] = "three_d_printer"
                part_details["type"] = "spare_part"
                part_details["size"] = ["anycubic_vyper"]
                part_details["color"] = ["category"]   
                
                #anycubic vyper hotend
                part_details = {}
                part_details["classification"] = "three_d_printer"
                part_details["type"] = "spare_part"
                part_details["size"] = ["anycubic_vyper"]
                part_details["color"] = [""]
                part_details["description_main"] = "hotend"
                part_details["description_extra"] = ""
                part_details["manufacturer"] = ""
                part_details["part_number"] = ""
                part_details["short_name"] = "Anycubic Vyper Hotend"
                parts.append(part_details)

        #bambu
        if True:
            part_details = {}
            part_details["classification"] = "three_d_printer"
            part_details["type"] = "printer"
            part_details["size"] = [""]  
            part_details["color"] = [""]  
            part_details["description_main"] = ""
            part_details["description_extra"] = ""
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["short_name"] = ""  
            
            bambu_default = copy.deepcopy(part_details)

            models = ["bambu_lab_a1", "bambu_lab_a1_mini", "bambu_lab_p1s", "bambu_lab_p1p"]
            for model in models:
                part_details = copy.deepcopy(bambu_default)
                part_details["size"] = model
                parts.append(part_details)

        #wanhao
        if True:
            part_details = {}
            part_details["classification"] = "three_d_printer"
            part_details["type"] = "printer"
            part_details["size"] = "wanhao_duplicator_i3_plus"
            part_details["color"] = ""
            part_details["description_main"] = ""
            part_details["description_extra"] = ""
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["short_name"] = ""  
            parts.append(part_details)    
    



    oomp.add_parts(parts, make_files=make_files)
    