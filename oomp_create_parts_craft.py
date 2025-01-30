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


    #pencil_crayon
    if True:
        part_details = copy.deepcopy(default_craft)
        part_details["type"] = "bead"
        part_details["size"] = "iron_melt"

        default_current = copy.deepcopy(part_details)

        #ikea solfagel
        part_details = copy.deepcopy(default_current)
        part_details["description_extra"] = "ikea_pyssla_style"
        part_details["description_main"] = "600_gram_bottle"
        part_details["manufacturer"] = "ikea"
        part_details["part_number_exact"] = "501.285.72"
        part_details["part_number"] = part_details["part_number_exact"].lower().replace("-","_").replace(" ","_").replace(".","_")
        part_details["distributor_part_number_ikea"] = part_details["part_number_exact"]
        part_details["link_distributor_ikea"] = "https://www.ikea.com/gb/en/p/pyssla-beads-mixed-colours-50128572/"
        parts.append(part_details)


    oomp.add_parts(parts, make_files=make_files)
    