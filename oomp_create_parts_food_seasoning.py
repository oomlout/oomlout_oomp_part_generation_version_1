import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    # spice
    if True:
        part_details = {}
        part_details["classification"] = "food"
        part_details["type"] = "seasoning"
        part_details["size"] = "spice"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        current_default_spice = copy.deepcopy(part_details)


        #make a box of bags
        part_details = copy.deepcopy(part_details)       
        part_details["size"] = ""
        part_details["description_extra"] = "100_gram_bag"
        part_details["name_short"] = "Box of Spice Bags"
        part_details["manufacturer"] = ""
        parts.append(part_details)


        part_details = copy.deepcopy(current_default_spice)
        part_details["size"] = "herb"
        current_default_herb = copy.deepcopy(part_details)

        #update dicts
        updates = []
        bag_update = {}
        bag_update["description_extra"] = "100_gram_bag"
        bag_update["manufacturer"] = ""
        updates.append(bag_update)

        schwartz_update = {}
        schwartz_update["manufacturer"] = "schwartz"
        schwartz_update["description_extra"] = "44_mm_diameter_100_mm_depth_bottle"
        updates.append(schwartz_update)

        tesco_update = {}
        tesco_update["manufacturer"] = "tesco"
        tesco_update["description_extra"] = "42_mm_width_42_mm_height_100_mm_depth_bottle"
        updates.append(tesco_update)

        #plain
        plain_update = {}
        updates.append(plain_update)
        
        spices = []
        #old
        if False:
            spices.append("empty")        
            spices.append("allspice_ground")
            spices.append("cardamom")
            spices.append("cayenne_pepper")
            spices.append("chilli_flakes")
            spices.append("chilli_powder")
            spices.append("cinnamon_ground")
            spices.append("cloves")
            spices.append("corriander_ground")
            spices.append("cumin_ground")
            spices.append("curry_powder")        
            spices.append("fennel_seeds")
            spices.append("garam_masala")
            spices.append("ginger_ground")
            spices.append("mustard_seed")
            spices.append("nutmeg_ground")
            spices.append("paprika")
            spices.append("paprika_smoked")
            spices.append("turmeric")
            spices.append("zaatar")
        #new
        if True:
            #spices.append("crushed_chilli_jalapeno_grinder")
            spices.append("chilli_jalapeno_hot")
            spices.append("chilli_birds_eye")
            spices.append("chilli_powder_mild")
            spices.append("chilli_crushed")
            spices.append("chilli_powder_hot")
            spices.append("chilli_powder_chipotle")
            spices.append("chilli_flakes")
            spices.append("chilli_cayenne")

            spices.append("curry_powder_tandoori")
            spices.append("curry_powder_tikka")
            spices.append("curry_powder_medium")
            spices.append("curry_powder_hot")
            spices.append("curry_powder_mild")

            spices.append("garlic_granules_roasted")
            spices.append("garlic_minced")
            #spices.append("garlic_grinder")
            spices.append("garlic_powder")
            spices.append("garlic_granules")
            spices.append("onion_granules")
            spices.append("onion_powder")

            #spices.append("pickling_spice")
            spices.append("sesame_seed_black")
            spices.append("sesame_seed")
            spices.append("sumac")
            spices.append("star_anise")
            spices.append("paprika_smoked")
            spices.append("saffron")
            spices.append("paprika")            
            spices.append("paprika_hot")
            spices.append("ras_el_hanout")
            #spices.append("pilau_rice_seasoning")
            spices.append("poppy_seeds")
            spices.append("coriander_ground")
            spices.append("coriander_seeds")
            spices.append("mixed_spice")
            spices.append("mustard_seeds")
            spices.append("nutmeg_ground")
            spices.append("nutmeg_whole")
            spices.append("cloves_whole")
            spices.append("caraway_seeds")
            spices.append("onion_seed_black")
            spices.append("cinnamon_stick")
            spices.append("cinnamon_ground")
            spices.append("allspice_ground")
            spices.append("cloves_ground")
            spices.append("cardamom_pod")
            spices.append("cumin_seeds")
            spices.append("cumin_ground")
            spices.append("fenugreek")
            spices.append("juniper_berries")
            spices.append("fennel_seed")
            spices.append("garam_masala")


        for spice in spices:
            for upd in updates:
                part_details = copy.deepcopy(current_default_spice)
                part_details["description_main"] = spice
                part_details["description"] = spice.replace("_", " ")
                part_details["name_short"] = spice.replace("_", " ").title()
                part_details.update(upd)
                parts.append(part_details)

        #herbs
        herbs = []
        if False:
            herbs.append("basil")
            herbs.append("bay_leaves")
            herbs.append("chives")
            herbs.append("coriander")
            herbs.append("dill")
            herbs.append("garlic_powder")
            herbs.append("marjoram")
            herbs.append("mint")
            herbs.append("onion_granules")        
            herbs.append("onion_powder")
            herbs.append("oregano")
            herbs.append("parsley")
            herbs.append("rosemary")
            herbs.append("sage")
            herbs.append("taragon")
            herbs.append("thyme")
        if True:
            herbs.append("rosemary")
            herbs.append("parsley_flat_leaf")
            herbs.append("sage")
            herbs.append("thyme")
            herbs.append("tarragon")
            herbs.append("mixed_herbs")
            herbs.append("mint")
            herbs.append("oregano")
            herbs.append("lemongrass")
            herbs.append("marjoram")
            herbs.append("bouquet_garni")
            herbs.append("italian_herb_mix")
            herbs.append("chives")
            herbs.append("coriander")
            herbs.append("coriander_seed")
            herbs.append("bay_leaves")
            herbs.append("herbes_de_provence")
            herbs.append("dill")

        for herb in herbs:
            for upd in updates:
                part_details = copy.deepcopy(current_default_herb)
                part_details["description_main"] = herb
                part_details["description"] = herb.replace("_", " ")
                part_details["name_short"] = herb.replace("_", " ").title()
                part_details.update(upd)
                parts.append(part_details)
        
        #salt and peppers
        if True:
            salt_and_peppers = []
            salt_and_peppers.append("salt_sea")
            salt_and_peppers.append("salt-pink_himalayan")
            salt_and_peppers.append("salt_garlic")
            salt_and_peppers.append("salt_celery")

            #salt_and_peppers.append("black_peppercorn_grinder")
            salt_and_peppers.append("peppercorn_black")
            salt_and_peppers.append("peppercorn_rainbow")
            salt_and_peppers.append("peppercorn_szechuan")

            salt_and_peppers.append("pepper_black_ground")
            salt_and_peppers.append("pepper_white_ground")
            salt_and_peppers.append("pepper_black_ground_coarse")
            #salt_and_peppers.append("black_and_red_pepper")
            #salt_and_peppers.append("garlic_pepper")



            for salt_and_pepper in salt_and_peppers:
                for upd in updates:
                    part_details = copy.deepcopy(current_default_spice)
                    part_details["size"] = "salt_and_pepper"
                    part_details["description_main"] = salt_and_pepper
                    part_details["description"] = salt_and_pepper.replace("_", " ")
                    part_details["name_short"] = salt_and_pepper.replace("_", " ").title()
                    part_details.update(upd)
                    parts.append(part_details)

        #old salt and pepper
        if False:

            #salt_and_pepper
            part_details = copy.deepcopy(current_default_spice)
            part_details["size"] = "salt_and_pepper"
            current_default_salt_and_pepper = copy.deepcopy(part_details)

            current_default_salt_and_pepper = copy.deepcopy(part_details)
            schwartz_default_saltr_and_pepper = copy.deepcopy(current_default_salt_and_pepper)
            schwartz_default_saltr_and_pepper["manufacturer"] = "schwartz"
            schwartz_default_saltr_and_pepper["description_extra"] = "44_mm_diameter_100_mm_height_bottle"  
            
            #salt_and_pepper
            if True:
                #salt
                part_details = copy.deepcopy(schwartz_default_saltr_and_pepper)
                part_details["description_main"] = "salt_table"
                part_details["description"] = "salt"
                part_details["name_short"] = "Salt"
                parts.append(part_details)

                #saxa 750 g
                part_details = copy.deepcopy(part_details)
                part_details["description_extra"] = "750_gram_70_mm_diameter_200_mm_height_plastic_bottle"
                part_details["manufacturer"] = "saxa"
                part_details["name_short"] = "Salt Saxa"
                parts.append(part_details)

                #black pepercorn scwartz
                part_details = copy.deepcopy(schwartz_default_saltr_and_pepper)
                part_details["description_main"] = "black_peppercorn"
                part_details["description"] = "black_peppercorn"
                part_details["name_short"] = "Black Peppercorn"
                parts.append(part_details)

                #black pepper ground
                part_details = copy.deepcopy(schwartz_default_saltr_and_pepper)
                part_details["description_main"] = "black_pepper_ground"
                part_details["description"] = "black_pepper_ground"
                part_details["name_short"] = "Black Pepper Ground"
                parts.append(part_details)

                #white_pepper
                part_details = copy.deepcopy(schwartz_default_saltr_and_pepper)
                part_details["description_main"] = "white_pepper"
                part_details["description"] = "white_pepper"
                part_details["name_short"] = "White Pepper"
                parts.append(part_details)

        #stock
        if True:
            part_details = copy.deepcopy(current_default_spice)
            part_details["size"] = "stock"
            current_default_stock = copy.deepcopy(part_details)

            #schwartz
            schwartz_default_stock = copy.deepcopy(current_default_stock)
            schwartz_default_stock["manufacturer"] = "schwartz"
            schwartz_default_stock["description_extra"] = "44_mm_diameter_100_mm_height_bottle"  

            #stock
            stock = []
            stock.append("beef")
            stock.append("chicken")
            stock.append("fish")
            stock.append("vegetable")

            description_extras = []
            description_extras.append("oxo_cube")
            description_extras.append("oxo_cube_12_pack")

            for st in stock:
                for de in description_extras:
                    part_details = copy.deepcopy(schwartz_default_stock)
                    part_details["description_main"] = st
                    part_details["description_extra"] = de
                    part_details["description"] = st
                    part_details["name_short"] = st.title()
                    parts.append(part_details)
            

    oomp.add_parts(parts, **kwargs)
    