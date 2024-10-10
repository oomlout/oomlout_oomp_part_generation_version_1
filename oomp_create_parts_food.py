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
        part_details["description_extra"] = "cravendale_filtered"
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







        

    




    
    oomp.add_parts(parts, **kwargs)
    