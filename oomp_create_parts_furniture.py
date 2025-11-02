import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    # ikea
    #   billy
    if True:
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "table"
        part_details["size"] = "oomlout"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = "2440_mm_width_1220_mm_height"
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)



    #bisley drawers
    if True:
        part_details = {}
        part_details["classification"] = "furniture"
        part_details["type"] = "drawer_unit"
        part_details["size"] = "bisley"
        part_details["color"] = "a4_drawer_size"
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "bisley"
        part_details["part_number"] = ""

        details_current = copy.deepcopy(part_details)

        description_mains = []
        description_mains.append("single_drawer")
        description_mains.append("15_drawer_unit")

        for description_main in description_mains:
            part_details = copy.deepcopy(details_current)
            part_details["description_main"] = description_main
            parts.append(part_details)

    




    
    oomp.add_parts(parts, **kwargs)
    