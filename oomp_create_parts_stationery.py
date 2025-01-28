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

    #felt_tip_pen
    if True:
        part_details = {}
        part_details["classification"] = "stationery"
        part_details["type"] = "felt_tip_pen"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        default_current =  copy.deepcopy(part_details)
    
        #amazon basic fabric
        part_details = copy.deepcopy(default_current)
        part_details["type"] = "felt_tip_pen_fabric"
        part_details["description_extra"] = "amazon_basic_8_color_set"
        part_details["description_main"] = "13_mm_diameter_140_mm_length"
        part_details["manufacturer"] = "amazon_basic"
        #part_details["part_number_exact"] = "469800"
        #part_details["part_number"] = part_details["part_number_exact"].lower().replace("-","_").replace(" ","_").replace(".","_")
        part_details["part_number"] = ""
        part_details["distributor_part_number_amazon"] = "B09MS59NGN"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_part_number_amazon']}"
        parts.append(part_details)
        

        #giotto
        part_details = copy.deepcopy(default_current)
        part_details["description_extra"] = "giotto_style_12_color_set"
        part_details["description_main"] = "16_mm_diameter_150_mm_length"
        part_details["manufacturer"] = "giotto"
        #part_details["part_number_exact"] = "469800"
        #part_details["part_number"] = part_details["part_number_exact"].lower().replace("-","_").replace(" ","_").replace(".","_")
        part_details["part_number"] = ""
        part_details["distributor_part_number_amazon"] = "B00MPCT2RI"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_part_number_amazon']}"
        parts.append(part_details)
        
        #giotto
        part_details = copy.deepcopy(default_current)
        part_details["description_extra"] = "50_color_set"
        part_details["description_main"] = "7_mm_diameter_130_mm_length"
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["distributor_part_number_amazon"] = "B085CKP544"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_part_number_amazon']}"
        parts.append(part_details)
        


        #bic
        part_details = copy.deepcopy(default_current)
        part_details["description_extra"] = "bic_style_18_color_set"
        part_details["description_main"] = "8_5_mm_diameter_150_mm_length"
        part_details["manufacturer"] = "bic"
        #part_details["part_number_exact"] = "942002"
        #part_details["part_number"] = part_details["part_number_exact"].lower().replace("-","_").replace(" ","_").replace(".","_")
        part_details["part_number"] = ""
        part_details["distributor_part_number_amazon"] = "B002047E7Q"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_part_number_amazon']}"
        parts.append(part_details)

        #balco art jumbo maler
        part_details = copy.deepcopy(default_current)
        part_details["description_extra"] = "balco_art_jumbo_maler_style_12_color_set"
        part_details["description_main"] = "19_mm_diameter_115_mm_length_triangle_shape"
        parts.append(part_details)

        #paint stick
        part_details = copy.deepcopy(default_current)
        part_details["type"] = "paint_stick"
        part_details["description_extra"] = "little_brian_style_12_color_set"
        part_details["description_main"] = "20_mm_diameter_90_mm_length"
        part_details["manufacturer"] = "little_brian"
        #part_details["part_number_exact"] = "LBS12"
        #part_details["part_number"] = part_details["part_number_exact"].lower().replace("-","_").replace(" ","_").replace(".","_")
        part_details["part_number"] = ""
        part_details["distributor_part_number_amazon"] = "B01A78UJUU"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_part_number_amazon']}"

    #glue
    if True:
        part_details = {}
        part_details["classification"] = "stationery"
        part_details["type"] = "glue_stick"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        default_current =  copy.deepcopy(part_details)
        
        #elmers 40g purple
        part_details = copy.deepcopy(default_current)
        part_details["description_main"] = "40_gram_30_mm_diameter_120_mm_length"
        part_details["description_extra"] = "purple"
        part_details["manufacturer"] = "elmers"
        part_details["part_number"] = ""
        part_details["distributor_part_number_amazon"] = "B08PCLDDWW"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_part_number_amazon']}"
        parts.append(part_details)

    #modeling_clay
    if True:
        part_details = {}
        part_details["classification"] = "stationery"
        part_details["type"] = "modeling_clay"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""

        default_current =  copy.deepcopy(part_details)
        
        
        part_details = copy.deepcopy(default_current)
        part_details["description_extra"] = "12_color_set"
        part_details["description_main"] = "generic"
        part_details["manufacturer"] = "the_art_box"
        part_details["part_number"] = ""
        part_details["distributor_part_number_amazon"] = "B00BGERNOU"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_part_number_amazon']}"
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
        default_current =  copy.deepcopy(part_details)
        
        #ikea solfagel
        part_details = copy.deepcopy(default_current)
        part_details["description_extra"] = "ikea_solfagel_style_24_color_set"
        part_details["description_main"] = "7_5_mm_diameter_175_mm_length"
        part_details["manufacturer"] = "ikea"
        part_details["part_number_exact"] = "205.442.32"
        part_details["part_number"] = part_details["part_number_exact"].lower().replace("-","_").replace(" ","_").replace(".","_")
        part_details["distributor_part_number_ikea"] = part_details["part_number_exact"]
        part_details["link_distributor_ikea"] = "https://www.ikea.com/gb/en/p/solfagel-coloured-pencil-mixed-colours-20544232/"
        parts.append(part_details)

        #crayola
        part_details = copy.deepcopy(default_current)
        part_details["description_extra"] = "crayola_style_50_color_set"
        part_details["description_main"] = "7_5_mm_diameter_175_mm_length"
        part_details["manufacturer"] = "crayola"
        #part_details["part_number_exact"] = "68-8020"
        #part_details["part_number"] = part_details["part_number_exact"].lower().replace("-","_").replace(" ","_").replace(".","_")
        part_details["part_number"] = ""
        part_details["distributor_part_number_amazon"] = "B00000J0S3"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_part_number_amazon']}"
        parts.append(part_details)

    oomp.add_parts(parts, make_files=make_files)
    