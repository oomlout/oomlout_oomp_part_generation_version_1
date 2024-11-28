import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    # bakery
    if True:
        part_details = {}
        part_details["classification"] = "food"
        part_details["type"] = "bakery"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""        

        current_default = copy.deepcopy(part_details)

        # 86084011	Jackson's Multigrain Brown Bloomer	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "bread"
        part_details["description_extra"] = "multigrain_brown_bloomer"
        part_details["manufacturer"] = "jackson"        
        part_details["part_number_distributor_ocado"] = "86084011"
        part_details["description"] = "Jackson's Multigrain Brown Bloomer"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=86084011"
        parts.append(part_details)

        # 511143011	M&S Soft Tortilla Wraps	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "tortilla_wrap"
        part_details["description_extra"] = "soft"
        part_details["part_number_distributor_ocado"] = "511143011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=511143011"
        part_details["description"] = "M&S Soft Tortilla Wraps"
        parts.append(part_details)

    # bean
    if True:
        part_details = {}
        part_details["classification"] = "food"
        part_details["type"] = "bean"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        
        current_default = copy.deepcopy(part_details)

       
        part_details = copy.deepcopy(current_default)
        
        part_details["description_main"] = "chickpea"
        part_details["description_extra"] = "tin_400_gram"
        part_details["name_short"] = "Chickenpeas"
        parts.append(part_details)

        #kidney beans
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "kidney_bean"
        part_details["description_extra"] = "tin_400_gram"
        part_details["name_short"] = "Kidney Beans"
        parts.append(part_details)

        #adzuki
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "adzuki_bean"
        part_details["description_extra"] = "tin_400_gram"
        part_details["name_short"] = "Adzuki Beans"

        #elpaso refried beans
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "refried_bean"
        part_details["description_extra"] = "tin_435_gram"
        part_details["manufacturer"] = "elpaso"
        part_details["name_short"] = "Refried Beans"
        parts.append(part_details)

    # baking
    if True:
        part_details = {}
        part_details["classification"] = "food"
        part_details["type"] = "baking"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""        
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        
        current_default = copy.deepcopy(part_details)

        # flour

        part_details = copy.deepcopy(current_default)
        part_details["size"] = "flour"
        part_details["color"] = "white"
        part_details["description"] = "flour_white"
        part_details["name_short"] = "Flour White"
        parts.append(part_details)

        #self raising
        part_details = copy.deepcopy(current_default)
        part_details["size"] = "flour"
        part_details["color"] = "self_raising"
        part_details["description"] = "flour_self_raising"
        part_details["name_short"] = "Flour Self Raising"
        parts.append(part_details)

        part_details = copy.deepcopy(current_default)
        part_details["size"] = "flour"
        part_details["color"] = "corn"
        part_details["description"] = "flour_corn"
        part_details["name_short"] = "Flour Corn"
        parts.append(part_details)

        #double o
        part_details = copy.deepcopy(current_default)
        part_details["size"] = "flour"
        part_details["color"] = "pasta_double_zero"
        part_details["description"] = "flour_pasta_double_zero"
        part_details["name_short"] = "Flour Pasta Double Zero"
        parts.append(part_details)

        #whole wheat
        part_details = copy.deepcopy(current_default)
        part_details["size"] = "flour"
        part_details["color"] = "whole_wheat"
        part_details["description"] = "flour_whole_wheat"
        part_details["name_short"] = "Flour Whole Wheat"
        parts.append(part_details)

        
        # sugar

        part_details = copy.deepcopy(current_default)
        part_details["size"] = "sugar"
        part_details["color"] = "caster"
        part_details["description"] = "sugar_caster"
        part_details["name_short"] = "Sugar Caster"
        parts.append(part_details)

        part_details = copy.deepcopy(current_default)
        part_details["size"] = "sugar"
        part_details["color"] = "granulated"
        part_details["description"] = "sugar_granulated"
        part_details["name_short"] = "Sugar Granulated"
        parts.append(part_details)
        
        part_details = copy.deepcopy(current_default)
        part_details["size"] = "sugar"
        part_details["color"] = "granulated_golden"
        part_details["description"] = "sugar_granulated_golden"
        part_details["name_short"] = "Sugar Golden Granulated Coffee"
        parts.append(part_details)

        part_details = copy.deepcopy(current_default)
        part_details["size"] = "sugar"
        part_details["color"] = "icing"
        part_details["description"] = "sugar_icing"
        part_details["name_short"] = "Sugar Icing"
        parts.append(part_details)

        part_details = copy.deepcopy(current_default)
        part_details["size"] = "sugar"
        part_details["color"] = "light_brown"
        part_details["description"] = "sugar_light_brown"
        part_details["name_short"] = "Sugar Light Brown"
        parts.append(part_details)

        part_details = copy.deepcopy(current_default)
        part_details["size"] = "sugar"
        part_details["color"] = "muscavado"
        part_details["description"] = "sugar_muscavado"
        part_details["name_short"] = "Sugar Muscavado"
        parts.append(part_details)

    #condiment
    if True:
        part_details = {}
        part_details["classification"] = "food"
        part_details["type"] = "condiment"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        
        current_default = copy.deepcopy(part_details)

        part_details = copy.deepcopy(current_default)
        part_details["color"] = "jam"
        part_details["description_main"] = "strawberry"
        part_details["description_extra"] = "jar_370_gram"
        part_details["manufacturer"] = "bonne_maman"
        part_details["name_short"] = "Strawberry Jam"
        parts.append(part_details)

        jam_default = copy.deepcopy(part_details)
        jam_default["description_main"] = ""

        #apricot
        part_details = copy.deepcopy(jam_default)
        part_details["description_main"] = "apricot"
        part_details["name_short"] = "Apricot Jam"
        parts.append(part_details)

        #marmalade
        part_details = copy.deepcopy(jam_default)
        part_details["description_main"] = "marmalade"
        part_details["name_short"] = "Marmalade"
        parts.append(part_details)

        #raspberrry
        part_details = copy.deepcopy(jam_default)
        part_details["description_main"] = "raspberry"
        part_details["name_short"] = "Raspberry Jam"
        parts.append(part_details)

        #ketchup
        part_details = copy.deepcopy(current_default)
        part_details["color"] = "savoury"
        part_details["description_main"] = "ketchup"
        part_details["description_extra"] = "bottle_squeeze_910_gram"
        part_details["manufacturer"] = "heinz"
        part_details["name_short"] = "Ketchup"
        parts.append(part_details)


        #salsa
        part_details = copy.deepcopy(current_default)
        part_details["color"] = "savoury"
        part_details["description_main"] = "salsa_red"
        part_details["description_extra"] = "jar_240_gram"
        part_details["manufacturer"] = "herdez"
        part_details["name_short"] = "Salsa Red"
        parts.append(part_details)

        salsa_default = copy.deepcopy(part_details)
        salsa_default["description_main"] = ""

        #salsa_green
        part_details = copy.deepcopy(salsa_default)
        part_details["description_main"] = "salsa_green"
        part_details["name_short"] = "Salsa Green"
        parts.append(part_details)

        #salad dressing
        part_details = copy.deepcopy(current_default)
        part_details["color"] = "salad_dressing"
        part_details["description_main"] = "ranch"
        part_details["description_extra"] = "bottle_250_ml"
        part_details["manufacturer"] = "newmans_own"
        part_details["name_short"] = "Ranch Salad Dressing"
        parts.append(part_details)




    # dairy
    if True:
        part_details = {}
        part_details["classification"] = "food"
        part_details["type"] = "dairy"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        
        current_default = copy.deepcopy(part_details)

        part_details = copy.deepcopy(current_default)
        part_details["size"] = "2000_ml"
        part_details["description_main"] = "milk_semi_skim"
        part_details["description_extra"] = "filtered"
        part_details["manufacturer"] = "cravendale"
        part_details["part_number_distributor_ocado"] = "24581011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=24581011"        
        parts.append(part_details)

        # 57293011	Ocado Large Free Range Eggs	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "eggs"
        part_details["description_extra"] = "large_free_range_six"
        part_details["part_number_distributor_ocado"] = "57293011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=57293011"
        part_details["description"] = "Ocado Large Free Range Eggs"
        parts.append(part_details)
        
        # 31833011	Cathedral City Mature Cheddar Cheese	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "cheese"
        part_details["description_extra"] = "mature_cheddar"
        part_details["manufacturer"] = "cathedral_city"
        part_details["part_number_distributor_ocado"] = "31833011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=31833011"
        part_details["description"] = "Cathedral City Mature Cheddar Cheese"
        parts.append(part_details)

    # drink
    if True:
        part_details = {}
        part_details["classification"] = "food"
        part_details["type"] = "drink"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        
        current_default = copy.deepcopy(part_details)

        # 24081011	Ocado Still Spring Water	04/10/2024
        part_details = copy.deepcopy(current_default)
        #size coffee
        part_details["size"] = "coffee"
        part_details["color"] = "instant"
        part_details["description_main"] = "espresso"
        part_details["description_extra"] = "jar_95_gram"
        part_details["manufacturer"] = "nescafe"
        part_details["name_short"] = "Instant Coffee Espresso"
        parts.append(part_details)

        part_details = copy.deepcopy(current_default)
        #size coffee
        part_details["size"] = "coffee"
        part_details["color"] = "ground_filter"
        part_details["description_main"] = "classic"
        part_details["description_extra"] = "tin_250_gram"
        part_details["manufacturer"] = "illy"
        part_details["name_short"] = "Ground Coffee Classic"
        parts.append(part_details)


    # fruit
    if True:
        part_details = {}
        part_details["classification"] = "food"
        part_details["type"] = "fruit"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        
        current_default = copy.deepcopy(part_details)

        # 518257011	M&S Pink Lady Apples	08/04/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "apple"
        part_details["description_extra"] = "pink_lady"
        part_details["part_number_distributor_ocado"] = "518257011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=518257011"
        part_details["description"] = "M&S Pink Lady Apples"
        parts.append(part_details)

        #banana
        part_details = copy.deepcopy(current_default)
        part_details["size"] = "bunch"        
        part_details["description_main"] = "banana"
        part_details["part_number_distributor_ocado"] = "44855011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=44855011"
        part_details["description"] = "Ocado Bananas"
        parts.append(part_details)

    # meat
    if True:
        part_details = {}
        part_details["classification"] = "food"
        part_details["type"] = "meat"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        
        current_default = copy.deepcopy(part_details)

        # 523896011	M&S Select Farms British 12 Pork Chipolatas	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "sausages"
        part_details["description_extra"] = "pork_chipolatas"
        part_details["part_number_distributor_ocado"] = "523896011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=523896011"
        part_details["description"] = "M&S Select Farms British 12 Pork Chipolatas"
        parts.append(part_details)

        #tinned tuna
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "tuna_in_sunflower_oil"
        part_details["description_extra"] = "tin_125_gram"
        part_details["name_short"] = "Tuna in Sunflower Oil"
        parts.append(part_details)

    # pantry_imgredient
    if True:
        part_details = {}
        part_details["classification"] = "food"
        part_details["type"] = "pantry"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        
        current_default = copy.deepcopy(part_details)
        
        part_details = copy.deepcopy(current_default)
        part_details["color"] = "ingredient"
        part_details["description_main"] = "coconut_milk"
        part_details["description_extra"] = "tin_400_ml"
        parts.append(part_details)

    # pantry prepared    
    if True:

        part_details = {}
        part_details["classification"] = "food"
        part_details["type"] = "pantry"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""


        #pasta sauce
        part_details = copy.deepcopy(current_default)
        part_details["color"] = "prepared"
        part_details["description_main"] = "pasta_sauce_tomato_and_roasted_garlic"
        part_details["description_extra"] = "jar_350_gram"
        part_details["manufacturer"] = "loyd_grossman"
        part_details["name_short"] = "Pasta Sauce Tomato and Roasted Garlic"
        parts.append(part_details)

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

        #schwartz default
        part_details = copy.deepcopy(part_details)
        part_details["description_extra"] = "44_mm_diameter_100_mm_height_bottle"
        part_details["manufacturer"] = "schwartz"
        
        schwartz_default_spice = copy.deepcopy(part_details)

        #spice
        if True:

            # paprika
            part_details = copy.deepcopy(schwartz_default_spice)
            part_details["size"] = "paprika"
            part_details["description"] = "paprika"
            part_details["name_short"] = "Paprika"
            parts.append(part_details)

            #corriander_ground
            part_details = copy.deepcopy(schwartz_default_spice)
            part_details["size"] = "corriander_ground"
            part_details["description"] = "corriander_ground"
            part_details["name_short"] = "Corriander Ground"
            parts.append(part_details)

            #cumin_ground
            part_details = copy.deepcopy(schwartz_default_spice)
            part_details["size"] = "cumin_ground"
            part_details["description"] = "cumin_ground"
            part_details["name_short"] = "Cumin Ground"
            parts.append(part_details)

            #fennel_seeds
            part_details = copy.deepcopy(schwartz_default_spice)
            part_details["size"] = "fennel_seeds"
            part_details["description"] = "fennel_seeds"
            part_details["name_short"] = "Fennel Seeds"
            parts.append(part_details)

            #garam_masala
            part_details = copy.deepcopy(schwartz_default_spice)
            part_details["size"] = "garam_masala"
            part_details["description"] = "garam_masala"
            part_details["name_short"] = "Garam Masala"
            parts.append(part_details)

            #paprika_smoked
            part_details = copy.deepcopy(schwartz_default_spice)
            part_details["size"] = "paprika_smoked"
            part_details["description"] = "paprika_smoked"
            part_details["name_short"] = "Paprika Smoked"
            parts.append(part_details)

            #zatar
            part_details = copy.deepcopy(schwartz_default_spice)
            part_details["size"] = "zatar"
            part_details["description"] = "zatar"
            part_details["name_short"] = "Zatar"
            parts.append(part_details)

            #turmeric
            part_details = copy.deepcopy(schwartz_default_spice)
            part_details["size"] = "turmeric"
            part_details["description"] = "turmeric"
            part_details["name_short"] = "Turmeric"
            parts.append(part_details)


        
        #herb default
        part_details = copy.deepcopy(current_default)
        part_details["size"] = "herb"

        current_default_herb = copy.deepcopy(part_details)

        #schwartz default
        part_details = copy.deepcopy(current_default)
        part_details["size"] = "herb"
        part_details["description_extra"] = "44_mm_diameter_100_mm_height_bottle"
        part_details["manufacturer"] = "schwartz"
        schwartz_default_herb = copy.deepcopy(part_details)

        #herb
        if True:
            #basil
            part_details = copy.deepcopy(schwartz_default_herb)
            part_details["description_main"] = "basil"
            part_details["description"] = "basil"
            part_details["name_short"] = "Basil"
            parts.append(part_details)

            #bay leaves
            part_details = copy.deepcopy(schwartz_default_herb)
            part_details["description_main"] = "bay_leaves"
            part_details["description"] = "bay_leaves"
            part_details["name_short"] = "Bay Leaves"
            parts.append(part_details)

            #dill
            part_details = copy.deepcopy(schwartz_default_herb)
            part_details["description_main"] = "dill"
            part_details["description"] = "dill"
            part_details["name_short"] = "Dill"
            parts.append(part_details)

            #thyme
            part_details = copy.deepcopy(schwartz_default_herb)
            part_details["description_main"] = "thyme"
            part_details["description"] = "thyme"
            part_details["name_short"] = "Thyme"
            parts.append(part_details)

            #onion_granules
            part_details = copy.deepcopy(schwartz_default_herb)
            part_details["description_main"] = "onion_granules"
            part_details["description"] = "onion_granules"
            part_details["name_short"] = "Onion Granules"
            parts.append(part_details)

            #rosemary
            part_details = copy.deepcopy(schwartz_default_herb)
            part_details["description_main"] = "rosemary"
            part_details["description"] = "rosemary"
            part_details["name_short"] = "Rosemary"
            parts.append(part_details)

            #parsley
            part_details = copy.deepcopy(schwartz_default_herb)
            part_details["description_main"] = "parsley"
            part_details["description"] = "parsley"
            part_details["name_short"] = "Parsley"
            parts.append(part_details)

            #sage
            part_details = copy.deepcopy(schwartz_default_herb)
            part_details["description_main"] = "sage"
            part_details["description"] = "sage"
            part_details["name_short"] = "Sage"
            parts.append(part_details)

            #taragon
            part_details = copy.deepcopy(schwartz_default_herb)
            part_details["description_main"] = "taragon"
            part_details["description"] = "taragon"
            part_details["name_short"] = "Taragon"
            parts.append(part_details)

            #garlic_powder
            part_details = copy.deepcopy(schwartz_default_herb)
            part_details["description_main"] = "garlic_powder"
            part_details["description"] = "garlic_powder"
            part_details["name_short"] = "Garlic Powder"
            parts.append(part_details)

            #

        #salt_and_pepper
        part_details = copy.deepcopy(current_default)
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

    # starch
    if True:
        part_details = {}
        part_details["classification"] = "food"
        part_details["type"] = "starch"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        
        current_default = copy.deepcopy(part_details)
        
        # breadcrumb
        part_details = copy.deepcopy(current_default)
        part_details["size"] = "breadcrumb"
        part_details["color"] = "panko"
        part_details["description"] = "breadcrumb_panko"
        part_details["name_short"] = "Breadcrumb Panko"
        parts.append(part_details)

        #couscous
        part_details = copy.deepcopy(current_default)
        part_details["size"] = "couscous"
        part_details["color"] = ""
        part_details["description"] = "couscous"
        part_details["name_short"] = "Couscous"
        parts.append(part_details)

        part_details = copy.deepcopy(current_default)
        part_details["size"] = "couscous"
        part_details["color"] = "giant"
        part_details["description"] = "couscous_giant"
        part_details["name_short"] = "Couscous Giant"
        parts.append(part_details)

        # oats
        part_details = copy.deepcopy(current_default)
        part_details["size"] = "oats"
        part_details["color"] = "porridge"
        part_details["description"] = "oats_porridge"
        part_details["name_short"] = "Oats Porridge"
        parts.append(part_details)

        # pasta
        part_details = copy.deepcopy(current_default)
        part_details["size"] = "pasta"
        part_details["color"] = "penne"
        part_details["description"] = "pasta_penne"
        part_details["name_short"] = "Pasta Penne"
        parts.append(part_details)

        part_details = copy.deepcopy(current_default)
        part_details["size"] = "pasta"
        part_details["color"] = "spaghetti"
        part_details["description"] = "pasta_spaghetti"
        part_details["name_short"] = "Pasta Spaghetti"
        parts.append(part_details)

        spaghetti_default = copy.deepcopy(part_details)

        part_details = copy.deepcopy(spaghetti_default)
        part_details["description_extra"] = "box_500_gram"
        part_details["manufacturer"] = "barilla"
        part_details["name_short"] = "Pasta Spaghetti Box"
        parts.append(part_details)

        part_details = copy.deepcopy(current_default)
        part_details["size"] = "pasta"
        part_details["color"] = "fusilli"
        part_details["description"] = "pasta_fusilli"
        part_details["name_short"] = "Pasta Fusilli"
        parts.append(part_details)

        fusilli_default = copy.deepcopy(part_details)

        part_details = copy.deepcopy(fusilli_default)
        part_details["description_extra"] = "box_500_gram"
        part_details["manufacturer"] = "barilla"
        parts.append(part_details)
        


        # rice
        
        part_details = copy.deepcopy(current_default)
        part_details["size"] = "rice"
        part_details["color"] = "dong_bei"
        part_details["description"] = "rice_dong_bei"
        part_details["name_short"] = "Rice Dong Bei"
        parts.append(part_details)

        part_details = copy.deepcopy(current_default)
        part_details["size"] = "rice"
        part_details["color"] = "basmati"
        part_details["description"] = "rice_basmati"
        part_details["name_short"] = "Rice Basmati"
        parts.append(part_details)

        part_details = copy.deepcopy(current_default)
        part_details["size"] = "rice"
        part_details["color"] = "brown_short_grain"
        part_details["description"] = "rice brown short grain"
        part_details["name_short"] = "Rice Brown Short Grain"
        parts.append(part_details)





    # vegetable
    if True: 
        # vegetable
        part_details = {}
        part_details["classification"] = "food"
        part_details["type"] = "vegetable"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        

        current_default = copy.deepcopy(part_details)

        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "cucumber"
        part_details["part_number_distributor_ocado"] = "240875011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=240875011"
        parts.append(part_details)


        # 517789011	M&S Perfectly Ripe Medium Hass Avocados	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "avocado"
        part_details["part_number_distributor_ocado"] = "517789011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=517789011"
        part_details["description"] = "M&S Perfectly Ripe Medium Hass Avocados"
        parts.append(part_details)

        # 517944011	M&S Rosa Vine Tomatoes 	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "tomato"
        part_details["description_extra"] = "rosa_vine"
        part_details["part_number_distributor_ocado"] = "517944011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=517944011"
        part_details["description"] = "M&S Rosa Vine Tomatoes"
        parts.append(part_details)

        # 518580011	Cook With M&S Coriander	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "coriander"
        part_details["part_number_distributor_ocado"] = "518580011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=518580011"
        part_details["description"] = "Cook With M&S Coriander"
        parts.append(part_details)

        # 518090011	M&S Iceberg Lettuce	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "lettuce"
        part_details["description_extra"] = "iceberg"
        part_details["part_number_distributor_ocado"] = "518090011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=518090011"
        part_details["description"] = "M&S Iceberg Lettuce"
        parts.append(part_details)

        # 527614011	M&S Chinese Leaf	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "chinese_leaf"
        part_details["part_number_distributor_ocado"] = "527614011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=527614011"
        part_details["description"] = "M&S Chinese Leaf"
        parts.append(part_details)

        # 517984011	M&S Piccolo Vine Tomatoes	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "tomato_cherry"
        part_details["description_extra"] = "piccolo"
        part_details["part_number_distributor_ocado"] = "517984011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=517984011"
        part_details["description"] = "M&S Piccolo Vine Tomatoes"
        parts.append(part_details)

        # 517767011	Cook With M&S Dill	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "dill"
        part_details["part_number_distributor_ocado"] = "517767011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=517767011"
        part_details["description"] = "Cook With M&S Dill"
        parts.append(part_details)

        # 59106011	Ocado Broccoli	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "broccoli"
        part_details["part_number_distributor_ocado"] = "59106011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=59106011"
        part_details["description"] = "Ocado Broccoli"
        parts.append(part_details)

        # 528414011	M&S Red Peppers	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "pepper"
        part_details["description_extra"] = "red"
        part_details["part_number_distributor_ocado"] = "528414011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=528414011"
        part_details["description"] = "M&S Red Peppers"
        parts.append(part_details)

        # 518655011	M&S Carrots	04/10/2024
        part_details = copy.deepcopy(current_default)
        part_details["description_main"] = "carrot"
        part_details["part_number_distributor_ocado"] = "518655011"
        part_details["link_distributor_ocado"] = "https://www.ocado.com/search?entry=518655011"
        part_details["description"] = "M&S Carrots"
        parts.append(part_details)


        #canned items
        current_default = copy.deepcopy(part_details)
        #198 gram tin
        part_details = copy.deepcopy(current_default)
        part_details["size"] = ""
        part_details["description_main"] = "sweetcorn"
        part_details["description_extra"] = "tin_198_gram"
        part_details["name_short"] = "Sweetcorn"
        parts.append(part_details)

        part_details = copy.deepcopy(current_default)
        #340 gram tin
        part_details["description_main"] = "sweetcorn"
        part_details["description_extra"] = "tin_340_gram"
        part_details["name_short"] = "Sweetcorn"
        parts.append(part_details)


        #tin of tomatoes
        part_details = copy.deepcopy(current_default)
        part_details["size"] = ""
        part_details["description_main"] = "tomatoes"
        part_details["description_extra"] = "tin_400_gram"
        part_details["manufacturer"] = "cirio"
        part_details["name_short"] = "Tomatoes Tinned"
        parts.append(part_details)



        

    




    
    oomp.add_parts(parts, **kwargs)
    