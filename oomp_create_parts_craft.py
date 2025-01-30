import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "craft"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = ""
    default_craft =  copy.deepcopy(part_details)


    #bead
    if True:
        #mixed bead
        part_details = copy.deepcopy(default_craft)
        part_details["type"] = "bead"
        part_details["size"] = "medium_thread_hole"
        
        default_current = copy.deepcopy(part_details)


        #mixed
        part_details = copy.deepcopy(default_current)
        part_details["description_main"] = "mixed"
        parts.append(part_details)

        part_details = copy.deepcopy(default_craft)
        part_details["type"] = "bead"
        part_details["size"] = "iron_melt"

        default_current = copy.deepcopy(part_details)
        #ikea pyssla
        part_details = copy.deepcopy(default_current)
        part_details["description_main"] = "ikea_pyssla_style"
        part_details["description_extra"] = "600_gram_bottle"
        part_details["manufacturer"] = "ikea"
        part_details["part_number_exact"] = "501.285.72"
        part_details["part_number"] = part_details["part_number_exact"].lower().replace("-","_").replace(" ","_").replace(".","_")
        part_details["distributor_part_number_ikea"] = part_details["part_number_exact"]
        part_details["link_distributor_ikea"] = "https://www.ikea.com/gb/en/p/pyssla-beads-mixed-colours-50128572/"
        parts.append(part_details)

    #paint
    if True:
        part_details = copy.deepcopy(default_craft)
        part_details["type"] = "paint"
        part_details["size"] = "acrylic"

        default_current = copy.deepcopy(part_details)

        #ikea solfagel
        part_details = copy.deepcopy(default_current)
        part_details["description_main"] = "ikea_solfagel_style"
        part_details["description_extra"] = "375_millilitre_bottle_set"
        part_details["manufacturer"] = "ikea"
        part_details["part_number_exact"] = "105.442.37"
        part_details["part_number"] = part_details["part_number_exact"].lower().replace("-","_").replace(" ","_").replace(".","_")
        part_details["distributor_part_number_ikea"] = part_details["part_number_exact"]
        part_details["link_distributor_ikea"] = "https://www.ikea.com/gb/en/p/solfagel-acrylic-paint-mixed-colours-10544237/"
        parts.append(part_details)

    #rubber stamp
    if True:
        part_details = copy.deepcopy(default_craft)
        part_details["type"] = "rubber_stamp"
        part_details["size"] = "medium"

        default_current = copy.deepcopy(part_details)

        #mixed
        part_details = copy.deepcopy(default_current)
        part_details["description_main"] = "mixed"
        
        parts.append(part_details)

    #sticker
    if True:
        part_details = copy.deepcopy(default_craft)
        part_details["type"] = "sticker"
        part_details["size"] = "sheet"

        default_current = copy.deepcopy(part_details)

        #mixed
        part_details = copy.deepcopy(default_current)
        part_details["description_main"] = "mixed"        
        parts.append(part_details)

    oomp.add_parts(parts, make_files=make_files)
    