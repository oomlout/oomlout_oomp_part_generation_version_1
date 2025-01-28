import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    # stationery
    #     clips
    if True:
        #           100 mm
        part_details = {}
        part_details["classification"] = "stationery"
        part_details["type"] = "clip_binder"
        part_details["size"] = "100_mm_width"
        part_details["color"] = "metal"
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        #add amazon distributor
        
        part_details["distributor_amazon"] = "B075YQ93CC"    
        part_details["link_distributor_amazon"] = "https://www.amazon.co.uk/dp/B075YQ93CC"
        part_details["price_1_distributor_amazon"] = 9.93/10/1.2
        parts.append(part_details) 

        #           38 mm
        part_details = {}
        part_details["classification"] = "stationery"
        part_details["type"] = "clip_binder"
        part_details["size"] = "38_mm_width"
        part_details["color"] = "metal"
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        #add amazon distributor

        part_details["distributor_amazon"] = "B07VHPV47Q"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
        part_details["price_1_distributor_amazon"] = 3.99/12/1.2
        parts.append(part_details)

    #pencil_crayon
    if True:
        part_details = {}
        part_details["classification"] = "stationery"
        part_details["type"] = "pencil_crayon"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        #add amazon distributor

        default_current =  copy.deepcopy(part_details)
        part_details["description_main"] = "ikea_solfagel_style_24_color_set"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "ikea"
        part_details["part_number_exact"] = "205.442.32"
        part_details["part_number"] = part_details["part_number_exact"].lower().replace("-","_").replace(" ","_").replace(".","_")
        part_details["distributor_part_number_ikea"] = part_details["part_number_exact"]
        part_details["link_distributor_ikea"] = "https://www.ikea.com/gb/en/p/solfagel-coloured-pencil-mixed-colours-20544232/"
        parts.append(part_details)


    oomp.add_parts(parts, make_files=make_files)
    