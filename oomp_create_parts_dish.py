import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    # ikea
    if True:
        part_details = {}
        part_details["classification"] = "dish"
        part_details["type"] = ""
        part_details["size"] = "ikea_oftast"
        part_details["color"] = "white"
        part_details["manufacturer"] = "ikea"

        ikea_ofstat_base = copy.deepcopy(part_details)

        part_details = copy.deepcopy(ikea_ofstat_base)
        part_details["description_main"] = "plate"
        part_details["description_extra"] = "250_mm_diameter"        
        part_details["part_number"] = "302_589_13"
        part_details["part_number_exact"] = part_details["part_number"].replace("_", ".")
        parts.append(part_details)

        #190 mm plate
        part_details = copy.deepcopy(ikea_ofstat_base)
        part_details["description_main"] = "plate"
        part_details["description_extra"] = "190_mm_diameter"
        part_details["part_number"] = "603_189_39"
        part_details["part_number_exact"] = part_details["part_number"].replace("_", ".")
        parts.append(part_details)

        #200 mm deep plate
        part_details = copy.deepcopy(ikea_ofstat_base)
        part_details["description_main"] = "plate_deep"
        part_details["description_extra"] = "200_mm_diameter"
        part_details["part_number"] = "003_189_42"
        part_details["part_number_exact"] = part_details["part_number"].replace("_", ".")
        parts.append(part_details)

        #110 mm bowl
        part_details = copy.deepcopy(ikea_ofstat_base)
        part_details["description_main"] = "bowl"
        part_details["description_extra"] = "110_mm_diameter"
        part_details["part_number"] = "904_671_12"
        part_details["part_number_exact"] = part_details["part_number"].replace("_", ".")
        parts.append(part_details)

        #150 mm bowl
        part_details = copy.deepcopy(ikea_ofstat_base)
        part_details["description_main"] = "bowl"
        part_details["description_extra"] = "150_mm_diameter"
        part_details["part_number"] = "802_589_15"
        part_details["part_number_exact"] = part_details["part_number"].replace("_", ".")
        parts.append(part_details)

        #230 mm serving bowl
        part_details = copy.deepcopy(ikea_ofstat_base)
        part_details["description_main"] = "bowl_serving"
        part_details["description_extra"] = "230_mm_diameter"
        part_details["part_number"] = "702_589_16"
        part_details["part_number_exact"] = part_details["part_number"].replace("_", ".")
        parts.append(part_details)

        
    # pyrex
    if True:
        part_details = {}
        part_details["classification"] = "dish"
        part_details["type"] = "baking"
        part_details["size"] = "pyrex"
        part_details["color"] = ""
        part_details["manufacturer"] = "pyrex"

        pyrex_base = copy.deepcopy(part_details)

        #bowls
        if True:            
            # 500 ml 14 cm bowl
            part_details = copy.deepcopy(pyrex_base)
            part_details["description_main"] = "bowl"
            part_details["description_extra"] = "500_ml_140_mm_diameter"
            part_details["part_number"] = "178B000"
            part_details["part_number_exact"] = part_details["part_number"]
            #link
            part_details["link_distributor_pyrex"] = "https://pyrex.co.uk/products/classic-glass-bowl-high-resistance?variant=14730280632355"
            parts.append(part_details)

            # 1000 ml 17 cm bowl
            part_details = copy.deepcopy(pyrex_base)
            part_details["description_main"] = "bowl"
            part_details["description_extra"] = "1000_ml_170_mm_diameter"
            part_details["part_number"] = "179B000"
            part_details["part_number_exact"] = part_details["part_number"]
            #link
            part_details["link_distributor_pyrex"] = "https://pyrex.co.uk/products/classic-glass-bowl-high-resistance?variant=14730280665123"
            parts.append(part_details)


            # 2000 ml 21 cm bowl
            part_details = copy.deepcopy(pyrex_base)
            part_details["description_main"] = "bowl"
            part_details["description_extra"] = "2000_ml_210_mm_diameter"
            part_details["part_number"] = "180B000"
            part_details["part_number_exact"] = part_details["part_number"]
            #link
            part_details["link_distributor_pyrex"] = "https://pyrex.co.uk/products/classic-glass-bowl-high-resistance?variant=14730280697891"
            parts.append(part_details)

            # 3000 ml 24 cm bowl
            part_details = copy.deepcopy(pyrex_base)
            part_details["description_main"] = "bowl"
            part_details["description_extra"] = "3000_ml_240_mm_diameter"
            part_details["part_number"] = "181B000"
            part_details["part_number_exact"] = part_details["part_number"]
            #link
            part_details["link_distributor_pyrex"] = "https://pyrex.co.uk/products/classic-glass-bowl-high-resistance?variant=14730280730659"
            parts.append(part_details)

        #caserole dishes
        if True:
            # 1000 ml 180 mm diameter 70 mm depth
            part_details = copy.deepcopy(pyrex_base)
            part_details["description_main"] = "caserole_dish_round"
            part_details["description_extra"] = "1000_ml_180_mm_diameter_70_mm_depth"
            part_details["part_number"] = "207A000"
            part_details["part_number_exact"] = part_details["part_number"]
            #link
            part_details["link_distributor_pyrex"] = "https://pyrex.co.uk/products/glass-round-casserole-high-resistance?variant=14730280566819"
            parts.append(part_details)

            # 1600 ml 200 mm diameter 80 mm depth
            part_details = copy.deepcopy(pyrex_base)
            part_details["description_main"] = "caserole_dish_round"
            part_details["description_extra"] = "1600_ml_200_mm_diameter_80_mm_depth"
            part_details["part_number"] = "204A000"
            part_details["part_number_exact"] = part_details["part_number"]
            #link
            part_details["link_distributor_pyrex"] = "https://pyrex.co.uk/products/glass-round-casserole-high-resistance?variant=14730280534051"
            parts.append(part_details)

            # 2300 ml 220 mm diameter 80 mm depth
            part_details = copy.deepcopy(pyrex_base)
            part_details["description_main"] = "caserole_dish_round"
            part_details["description_extra"] = "2300_ml_220_mm_diameter_80_mm_depth"
            part_details["part_number"] = "208A000"
            part_details["part_number_exact"] = part_details["part_number"]
            #link
            part_details["link_distributor_pyrex"] = "https://pyrex.co.uk/products/glass-round-casserole-high-resistance?variant=14730280599587"
            parts.append(part_details)

            # 3700 ml 270 mm diameter 100 mm depth
            part_details = copy.deepcopy(pyrex_base)
            part_details["description_main"] = "caserole_dish_round"
            part_details["description_extra"] = "3700_ml_270_mm_diameter_100_mm_depth"
            part_details["part_number"] = "118A000"
            part_details["part_number_exact"] = part_details["part_number"]
            #link
            part_details["link_distributor_pyrex"] = "https://pyrex.co.uk/products/glass-round-casserole-high-resistance?variant=39702806560803"
            parts.append(part_details)


            








        

    




    
    oomp.add_parts(parts, **kwargs)
    