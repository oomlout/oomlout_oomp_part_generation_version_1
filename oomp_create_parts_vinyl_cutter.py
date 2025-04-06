import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "vinyl_cutter"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = part_details.copy()

    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "joy"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = "JCTR101"
    part_details["part_number"] = part_details["part_number_exact"].lower().replace(" ", "_").replace("-", "_")
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())


    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "personal"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = "CRV001"
    part_details["part_number"] = part_details["part_number_exact"].lower().replace(" ", "_").replace("-", "_")
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())

    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "expression"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = "CREX001"
    part_details["part_number"] = part_details["part_number_exact"].lower().replace(" ", "_").replace("-", "_")
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())

    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "expression_2"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = "CREX002"
    part_details["part_number"] = part_details["part_number_exact"].lower().replace(" ", "_").replace("-", "_")
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())

    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "mini"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = "CMNI001"
    part_details["part_number"] = part_details["part_number_exact"].lower().replace(" ", "_").replace("-", "_")
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())

    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "explore"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = "CXPL001"
    part_details["part_number"] = part_details["part_number_exact"].lower().replace(" ", "_").replace("-", "_")
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())

    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "explore_one"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = "CXPL101"
    part_details["part_number"] = part_details["part_number_exact"].lower().replace(" ", "_").replace("-", "_")
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())

    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "explore_air"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = "CXPL201"
    part_details["part_number"] = part_details["part_number_exact"].lower().replace(" ", "_").replace("-", "_")
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())

    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "explore_air_2"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = "CXPL202"
    part_details["part_number"] = part_details["part_number_exact"].lower().replace(" ", "_").replace("-", "_")
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())

    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "maker"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = "CXPL301"
    part_details["part_number"] = part_details["part_number_exact"].lower().replace(" ", "_").replace("-", "_")
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())

    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "joy"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = "JCTR101"
    part_details["part_number"] = part_details["part_number_exact"].lower().replace(" ", "_").replace("-", "_")
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())

    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "explore_3"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = "CXPL203"
    part_details["part_number"] = part_details["part_number_exact"].lower().replace(" ", "_").replace("-", "_")
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())

    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "maker_3"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = "CXPL303"
    part_details["part_number"] = part_details["part_number_exact"].lower().replace(" ", "_").replace("-", "_")
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())

    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "venture"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = ""
    part_details["part_number"] = ""
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())

    part_details = default_empty.copy()
    part_details["type"] = "vinyl_cutter"
    part_details["size"] = "cricut"
    part_details["color"] = ""
    part_details["description_main"] = "joy_xtra"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "cricut"
    part_details["part_number_exact"] = ""
    part_details["part_number"] = ""
    part_details["link_distributor_cricut"] = ""
    parts.append(part_details.copy())

        

    
    oomp.add_parts(parts, **kwargs)
    