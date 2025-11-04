import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    #card_trading
    if True:
        part_details = {}
        part_details["classification"] = "card_trading"
        part_details["type"] = ""
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""

        default_empty = part_details.copy()

        types = ["sport_baseball", "sport_basketball", "sport_football_american", "sport_football_soccer", "sport_hockey"]
        for typ in types:
            part_details = default_empty.copy()
            part_details["type"] = typ
            parts.append(part_details)

    #card_game
    if True:
        part_details = {}
        part_details["classification"] = "card_game"
        part_details["type"] = ""
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""

        default_empty = part_details.copy()

        #pokemon
        if True:
            part_details = default_empty.copy()
            part_details["type"] = "pokemon"            

            parts.append(part_details)

        #magic the gathering
        if True:
            part_details = default_empty.copy()
            part_details["type"] = "magic_the_gathering"            
            parts.append(part_details)



    oomp.add_parts(parts, **kwargs)
    