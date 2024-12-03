import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []


    #cleaning products
    if True:
        part_details = {}
        part_details["classification"] = "household_cleaning"
        part_details["type"] = "cleaner_spray"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = "ineos_multi_room_cleaner_rhubarb_and_pommegranate"
        part_details["description_extra"] = "750_ml_bottle"
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)


    # animal
    if True:
        part_details = {}
        part_details["classification"] = "household_toy"
        part_details["type"] = ["animal","dinosaur"]
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = "to_sort"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)

    # ball
    if True:
        part_details = {}
        part_details["classification"] = "household_toy"
        part_details["type"] = "ball"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = "to_sort"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)

    # building
    if True:
        part_details = {}
        part_details["classification"] = "household_toy"
        part_details["type"] = "building"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = "to_sort"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)

    # craft
    if True:
        part_details = {}
        part_details["classification"] = "household_toy"
        part_details["type"] = "craft"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = "to_sort"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)

    # doll
    if True:
        part_details = {}
        part_details["classification"] = "household_toy"
        part_details["type"] = ["doll", "doll_sylvanian_family", "doll_barbie", "doll_baby"]
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = "to_sort"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)

    # educational
    if True:
        part_details = {}
        part_details["classification"] = "household_toy"
        part_details["type"] = "educational"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = "to_sort"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)

    # fidget
    if True:
        part_details = {}
        part_details["classification"] = "household_toy"
        part_details["type"] = "fidget"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = "to_sort"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)
    
    # game
        if True:
            part_details = {}
            part_details["classification"] = "household_toy"
            part_details["type"] = "game"
            part_details["size"] = [""]
            part_details["color"] = [""]
            part_details["description_main"] = "to_sort"
            part_details["description_extra"] = ""
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            parts.append(part_details)
    
    # pretend
    if True:
        part_details = {}
        part_details["classification"] = "household_toy"
        part_details["type"] = ["pretend", "pretend_job", "pretend_kitchen", "pretend_kitchen_food", "pretend_kitchen_dish", "pretend_kitchen_utensil", "pretend_pet"]
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = "to_sort"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)

    # puzzle
    if True:
        part_details = {}
        part_details["classification"] = "household_toy"
        part_details["type"] = "puzzle"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = "to_sort"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)  

    # stuffie
    if True:
        part_details = {}
        part_details["classification"] = "household_toy"
        part_details["type"] = "stuffie"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = "to_sort"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)


    
    oomp.add_parts(parts, **kwargs)
    