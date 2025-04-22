import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    #item
    part_details = {}
    part_details["classification"] = "clothes"
    part_details["type"] = "item"
    part_details["size"] = ""                       #type of garment
    part_details["color"] = ""                      #size
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = part_details.copy()

    # basic items
    if True:
        sizes = []
        sizes.append("t_shirt")
        sizes.append("jumper")
        sizes.append("socks")
        sizes.append("pants")
        sizes.append("hat")
        sizes.append("gloves")
        sizes.append("scarf")
        sizes.append("belt")
        sizes.append("coat")
        sizes.append("shorts")
        sizes.append("swimwear")
        sizes.append("underwear")
        sizes.append("sweatshirt")
        sizes.append("pajama_top")
        sizes.append("pajama_bottom")
        sizes.append("sweater")

        colors = []
        colors.append("small")
        colors.append("medium")
        colors.append("large")
        colors.append("extra_large")
        colors.append("extra_small")
        colors.append("double_extra_large")
        colors.append("triple_extra_large")
        

        for size in sizes:
            for color in colors:
                part_details = default_empty.copy()
                part_details["size"] = size
                part_details["color"] = f"color_{color}"
                part_details["description_main"] = f""
                parts.append(part_details.copy())
            

    oomp.add_parts(parts, **kwargs)