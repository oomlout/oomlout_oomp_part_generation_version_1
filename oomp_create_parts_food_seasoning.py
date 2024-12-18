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

        
        




        spices = []
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
        herbs.append("basil")
        herbs.append("bay_leaves")
        herbs.append("chives")
        herbs.append("coriander")
        herbs.append("dill")
        herbs.append("garlic_powder")
        herbs.append("marjoram")
        herbs.append("mint")
        herbs.append("onion_granules")
        herbs.append("oregano")
        herbs.append("parsley")
        herbs.append("rosemary")
        herbs.append("sage")
        herbs.append("taragon")
        herbs.append("thyme")

        for herb in herbs:
            for upd in updates:
                part_details = copy.deepcopy(current_default_herb)
                part_details["description_main"] = herb
                part_details["description"] = herb.replace("_", " ")
                part_details["name_short"] = herb.replace("_", " ").title()
                part_details.update(upd)
                parts.append(part_details)
        
        
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


    oomp.add_parts(parts, **kwargs)
    