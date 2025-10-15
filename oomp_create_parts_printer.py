import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    #print_time]
    part_details = {}
    part_details["classification"] = "printer"
    part_details["type"] = "all_in_one_inkjet"
    part_details["size"] = "a4"
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "canon_pixma"
    part_details["part_number"] = "ts5350"
    part_details["short_name"] = "Printer Canon TS5350"  
    parts.append(part_details)    
    
   
    
    part_details = {}
    part_details["classification"] = "printer"
    part_details["type"] = "inkjet"
    part_details["size"] = "a4"
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "hewlett_packard"
    part_details["part_number"] = "officejet_1000_mobile"
    part_details["short_name"] = "Printer HP Officejet 1000 Mobile"  
    parts.append(part_details) 


    part_details = {}
    part_details["classification"] = "printer"
    part_details["type"] = "inkjet"
    part_details["size"] = "photo"
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "epson_picturemate"
    part_details["part_number"] = "personal_photo_lab"
    part_details["short_name"] = "Printer Epson Picturemate Personal Photo Lab"  
    parts.append(part_details) 


    #epson
    if True:
        #ecotank
        if True:
            part_numbers = []
            part_numbers.append("et_2650")
            part_numbers.append("et_2750")
            part_numbers.append("et_2810")

            for part_number in part_numbers:
                part_details = {}
                part_details["classification"] = "printer"
                part_details["type"] = "inkjet"
                part_details["size"] = "a4"
                part_details["color"] = ""
                part_details["description_main"] = ""
                part_details["description_extra"] = ""
                part_details["manufacturer"] = "epson_ecotank"
                part_details["part_number"] = part_number
                part_details["short_name"] = "" 
                parts.append(copy.deepcopy(part_details))

    #uv printers
    if True:
        part_details = {}
        part_details["classification"] = "printer"
        part_details["type"] = "uv"
        part_details["size"] = "a3"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "generic"
        part_details["part_number_exact"] = "DEM-JET-UV3"
        part_details["part_number"] = part_details["part_number_exact"].replace("-", "_").replace(" ", "_").lower()
        part_details["short_name"] = "Anycubic UV Printer"  
        parts.append(part_details)

    #big printers
    if True:
        #mutoh valuejet vj-1304
        part_details = {}
        part_details["classification"] = "printer"
        part_details["type"] = "inkjet"
        part_details["size"] = "reel"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "mutoh"
        part_details["part_number_exact"] = "VJ-1304"
        part_details["part_number"] = part_details["part_number_exact"].replace("-", "_").replace(" ", "_").lower()
        part_details["short_name"] = "Mutoh ValueJet VJ-1304"
        parts.append(part_details)

        
        #epson stylus pro 4800
        part_details = {}
        part_details["classification"] = "printer"
        part_details["type"] = "inkjet"
        part_details["size"] = "a2"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "epson"
        part_details["part_number_exact"] = "Stylus Pro 4800"
        part_details["part_number"] = part_details["part_number_exact"].replace("-", "_").replace(" ", "_").lower()
        part_details["short_name"] = "Epson Stylus Pro 4800"
        parts.append(part_details)

        
        #add the parts to oomp\hewlet packard designjet 650c
        part_details = {}
        part_details["classification"] = "printer"
        part_details["type"] = "inkjet"
        part_details["size"] = "reel"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "hewlett_packard"
        part_details["part_number_exact"] = "Designjet 650C"
        part_details["part_number"] = part_details["part_number_exact"].replace("-", "_").replace(" ", "_").lower()
        part_details["short_name"] = "Hewlett Packard Designjet 650C"
        parts.append(part_details)

    #digital duplicator
    if True:
        #mutoh valuejet vj-1304
        part_details = {}
        part_details["classification"] = "printer"
        part_details["type"] = "digital_duplicator"
        part_details["size"] = "a4"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "duplo"
        part_details["part_number_exact"] = "DP-21S"
        part_details["part_number"] = part_details["part_number_exact"].replace("-", "_").replace(" ", "_").lower()
        part_details["short_name"] = ""
        parts.append(part_details)

    #ink        
    if True:
        #epson ecotank
        if True:
            #102
            description_mains = []
            description_mains.append("multipack")
            description_mains.append("black_bottle_127_ml")
            description_mains.append("cyan_bottle_70_ml")
            description_mains.append("magenta_bottle_70_ml")
            description_mains.append("yellow_bottle_70_ml")
            for desc_main in description_mains:
                part_details = {}
                part_details["classification"] = "printer"
                part_details["type"] = "ink"
                part_details["size"] = "epson"
                part_details["color"] = "ecotank"
                part_details["description_main"] = desc_main
                part_details["description_extra"] = ""
                part_details["manufacturer"] = "epson"
                part_details["part_number_exact"] = "102"
                part_details["part_number"] = part_details["part_number_exact"].replace("-", "_").replace(" ", "_").lower()
                # amazon
                part_details["distributor_amazon"] = "B08BXSR45Z"
                part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
                parts.append(copy.deepcopy(part_details))

            #104
            description_mains = []
            description_mains.append("multipack")
            description_mains.append("black_bottle_65_ml")
            description_mains.append("cyan_bottle_65_ml")
            description_mains.append("magenta_bottle_65_ml")
            description_mains.append("yellow_bottle_65_ml")

            for desc_main in description_mains:
                part_details = {}
                part_details["classification"] = "printer"
                part_details["type"] = "ink"
                part_details["size"] = "inkjet_paper"
                part_details["color"] = "ecotank"
                part_details["description_main"] = desc_main
                part_details["description_extra"] = ""
                part_details["manufacturer"] = "epson"
                part_details["part_number_exact"] = "104"
                part_details["part_number"] = part_details["part_number_exact"].replace("-", "_").replace(" ", "_").lower()
                # amazon
                part_details["distributor_amazon"] = "B08BXT7Z6J"
                part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
                parts.append(copy.deepcopy(part_details))


        #sublimation ink
        if True:
            #a_sub sublimation
            description_mains = []
            description_mains.append("multipack")
            description_mains.append("black_bottle_120_ml")
            description_mains.append("cyan_bottle_120_ml")
            description_mains.append("magenta_bottle_120_ml")
            description_mains.append("yellow_bottle_120_ml")

            for desc_main in description_mains:
                part_details = {}
                part_details["classification"] = "printer"
                part_details["type"] = "ink"
                part_details["size"] = "inkjet_sublimation"
                part_details["color"] = ""
                part_details["description_main"] = desc_main
                part_details["description_extra"] = ""
                part_details["manufacturer"] = "a_sub"
                part_details["part_number"] = ""
                # amazon
                part_details["distributor_amazon"] = "B08D9HWXKM"
                part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['distributor_amazon']}"
                parts.append(copy.deepcopy(part_details))

        #ecosolvent
        if True:
            description_mains = []
            description_mains.append("multipack")
            description_mains.append("cyan_bottle_70_ml")
            description_mains.append("magenta_bottle_70_ml")
            description_mains.append("yellow_bottle_70_ml")
            description_mains.append("black_bottle_70_ml")


            for desc_main in description_mains:
                part_details = {}
                part_details["classification"] = "printer"
                part_details["type"] = "ink"
                part_details["size"] = "ecosolvent"
                part_details["color"] = ""
                part_details["description_main"] = desc_main
                part_details["description_extra"] = ""
                part_details["manufacturer"] = "ocbestjet"                
                part_details["part_number"] = ""
                parts.append(copy.deepcopy(part_details))


    #chad ecotank research
    if True:
        

        # --- First-generation EcoTank / L-series (UK) ---
        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "l_355",
            "short_name": "EcoTank L355",
            "description_chat_gpt": "A4 3-in-1 printer (Print/Scan/Copy).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 249.99,
            "compatible_ink_bottles": ["664"],
            "ink_type": "dye",
            "features": []
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "l_555",
            "short_name": "EcoTank L555",
            "description_chat_gpt": "A4 4-in-1 (Print/Scan/Copy/Fax).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 329.99,
            "compatible_ink_bottles": ["664"],
            "ink_type": "dye",
            "features": ["fax", "adf"]
        })

        # --- Early ET-2000 / ET-4000 series ---
        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_2500",
            "short_name": "EcoTank ET-2500",
            "description_chat_gpt": "A4 3-in-1 (Print/Scan/Copy).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 229.99,
            "compatible_ink_bottles": ["664"],
            "ink_type": "dye",
            "features": []
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_2550",
            "short_name": "EcoTank ET-2550",
            "description_chat_gpt": "A4 3-in-1 (Print/Scan/Copy).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 249.00,
            "compatible_ink_bottles": ["664"],
            "ink_type": "dye",
            "features": ["wifi"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_4500",
            "short_name": "EcoTank ET-4500",
            "description_chat_gpt": "A4 4-in-1 (Print/Scan/Copy/Fax) with ADF.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 269.00,
            "compatible_ink_bottles": ["664"],
            "ink_type": "dye",
            "features": ["fax", "adf", "wifi"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_4550",
            "short_name": "EcoTank ET-4550",
            "description_chat_gpt": "A4 4-in-1 (Print/Scan/Copy/Fax) with duplex and ADF.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 369.00,
            "compatible_ink_bottles": ["664"],
            "ink_type": "dye",
            "features": ["fax", "adf", "duplex", "ethernet", "wifi"]
        })

        # --- ET-2600 / 2700 / 3600 family ---
        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_2600",
            "short_name": "EcoTank ET-2600",
            "description_chat_gpt": "A4 3-in-1 (Print/Scan/Copy).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 199.00,
            "compatible_ink_bottles": ["664"],
            "ink_type": "dye",
            "features": ["wifi"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_2650",
            "short_name": "EcoTank ET-2650",
            "description_chat_gpt": "A4 3-in-1 (Print/Scan/Copy).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 249.00,
            "compatible_ink_bottles": ["664"],
            "ink_type": "dye",
            "features": ["wifi"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_3600",
            "short_name": "EcoTank ET-3600",
            "description_chat_gpt": "A4 3-in-1 (Print/Scan/Copy) with duplex.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 399.00,
            "compatible_ink_bottles": ["664"],
            "ink_type": "dye",
            "features": ["duplex", "ethernet", "wifi"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_2700",
            "short_name": "EcoTank ET-2700",
            "description_chat_gpt": "A4 3-in-1 (Print/Scan/Copy).",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 229.00,
            "compatible_ink_bottles": ["102"],
            "ink_type": "dye",
            "features": ["wifi"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_2750",
            "short_name": "EcoTank ET-2750",
            "description_chat_gpt": "A4 3-in-1 (Print/Scan/Copy) with duplex.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 299.00,
            "compatible_ink_bottles": ["102"],
            "ink_type": "dye",
            "features": ["duplex", "wifi"]
        })

        # --- ET-2710 / 28xx family (EcoFit 104 bottles) ---
        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_2710",
            "short_name": "EcoTank ET-2710",
            "description_chat_gpt": "A4 3-in-1 (Print/Scan/Copy).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 199.00,
            "compatible_ink_bottles": ["104"],
            "ink_type": "dye",
            "features": ["wifi"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_2810",
            "short_name": "EcoTank ET-2810",
            "description_chat_gpt": "A4 3-in-1 (Print/Scan/Copy).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 179.00,
            "compatible_ink_bottles": ["104"],
            "ink_type": "dye",
            "features": ["wifi"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_2820",
            "short_name": "EcoTank ET-2820",
            "description_chat_gpt": "A4 3-in-1 (Print/Scan/Copy).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 239.99,
            "compatible_ink_bottles": ["104"],
            "ink_type": "dye",
            "features": ["wifi", "lcd"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_2850",
            "short_name": "EcoTank ET-2850",
            "description_chat_gpt": "A4 3-in-1 (Print/Scan/Copy) with duplex.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 269.00,
            "compatible_ink_bottles": ["104"],
            "ink_type": "dye",
            "features": ["duplex", "wifi", "lcd"]
        })

        # --- ET-3700 / 4700 family ---
        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_3700",
            "short_name": "EcoTank ET-3700",
            "description_chat_gpt": "A4 3-in-1 with duplex and larger tanks.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 400,
            "nozzle_count_per_colour": 128,
            "total_colours": 4,
            "original_rrp_gbp": 349.00,
            "compatible_ink_bottles": ["102"],
            "ink_type": "dye",
            "features": ["duplex", "ethernet", "wifi", "lcd"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_3750",
            "short_name": "EcoTank ET-3750",
            "description_chat_gpt": "A4 3-in-1 with duplex and ADF.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 400,
            "nozzle_count_per_colour": 128,
            "total_colours": 4,
            "original_rrp_gbp": 429.00,
            "compatible_ink_bottles": ["102"],
            "ink_type": "dye",
            "features": ["duplex", "adf", "ethernet", "wifi", "lcd"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_4700",
            "short_name": "EcoTank ET-4700",
            "description_chat_gpt": "A4 4-in-1 with ADF and fax.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 229.00,
            "compatible_ink_bottles": ["104"],
            "ink_type": "dye",
            "features": ["fax", "adf", "wifi", "lcd"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_4750",
            "short_name": "EcoTank ET-4750",
            "description_chat_gpt": "A4 4-in-1 with ADF, fax, and duplex.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 400,
            "nozzle_count_per_colour": 128,
            "total_colours": 4,
            "original_rrp_gbp": 449.00,
            "compatible_ink_bottles": ["102"],
            "ink_type": "dye",
            "features": ["fax", "adf", "duplex", "ethernet", "wifi", "touchscreen"]
        })

        # --- ET-4800/4850/4950 (2021+) ---
        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_4800",
            "short_name": "EcoTank ET-4800",
            "description_chat_gpt": "A4 4-in-1 with ADF and fax (entry).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 249.00,
            "compatible_ink_bottles": ["104"],
            "ink_type": "dye",
            "features": ["fax", "adf", "wifi", "lcd"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_4850",
            "short_name": "EcoTank ET-4850",
            "description_chat_gpt": "A4 4-in-1 with ADF, fax, duplex, touchscreen.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 400,
            "nozzle_count_per_colour": 128,
            "total_colours": 4,
            "original_rrp_gbp": 399.00,
            "compatible_ink_bottles": ["102"],
            "ink_type": "dye",
            "features": ["fax", "adf", "duplex", "ethernet", "wifi", "touchscreen"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_4950",
            "short_name": "EcoTank ET-4950",
            "description_chat_gpt": "A4 4-in-1 with ADF, fax, duplex (newer variant).",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 400,
            "nozzle_count_per_colour": 128,
            "total_colours": 4,
            "original_rrp_gbp": 429.00,
            "compatible_ink_bottles": ["102"],
            "ink_type": "dye",
            "features": ["fax", "adf", "duplex", "ethernet", "wifi", "touchscreen"]
        })

        # --- Business A4 EcoTank Pro (pigment 113 inks) ---
        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_5150",
            "short_name": "EcoTank ET-5150",
            "description_chat_gpt": "A4 business 3-in-1 (duplex, high speed, pigment).",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 349.00,
            "compatible_ink_bottles": ["113"],
            "ink_type": "pigment",
            "features": ["duplex", "ethernet", "wifi", "lcd"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_5170",
            "short_name": "EcoTank ET-5170",
            "description_chat_gpt": "A4 business 3-in-1 (duplex, higher speed, pigment).",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 379.00,
            "compatible_ink_bottles": ["113"],
            "ink_type": "pigment",
            "features": ["duplex", "ethernet", "wifi", "touchscreen"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_5180",
            "short_name": "EcoTank ET-5180",
            "description_chat_gpt": "A4 business 3-in-1 (fast, duplex, pigment).",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 399.00,
            "compatible_ink_bottles": ["113"],
            "ink_type": "pigment",
            "features": ["duplex", "ethernet", "wifi", "touchscreen", "adf"]
        })

        # --- Business A4 Pro high-duty (5800/5850/5880) ---
        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_5800",
            "short_name": "EcoTank ET-5800",
            "description_chat_gpt": "A4 high-speed 4-in-1 business model (pigment).",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 699.00,
            "compatible_ink_bottles": ["113"],
            "ink_type": "pigment",
            "features": ["duplex", "adf", "ethernet", "wifi", "touchscreen", "dual_tray"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_5850",
            "short_name": "EcoTank ET-5850",
            "description_chat_gpt": "A4 high-speed 4-in-1 business with higher duty.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 799.00,
            "compatible_ink_bottles": ["113"],
            "ink_type": "pigment",
            "features": ["duplex", "adf", "ethernet", "wifi", "touchscreen", "dual_tray"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_5880",
            "short_name": "EcoTank ET-5880",
            "description_chat_gpt": "A4 high-speed 4-in-1 with extra capacity.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 899.00,
            "compatible_ink_bottles": ["113"],
            "ink_type": "pigment",
            "features": ["duplex", "adf", "ethernet", "wifi", "touchscreen", "dual_tray"]
        })

        # --- Photo EcoTank (5- and 6-colour) ---
        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_7700",
            "short_name": "EcoTank ET-7700",
            "description_chat_gpt": "A4 photo 5-colour all-in-one (pigment BK + dye CMY + photo BK).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 360,
            "nozzle_count_per_colour": 59,
            "total_colours": 5,
            "original_rrp_gbp": 549.00,
            "compatible_ink_bottles": ["105", "106"],
            "ink_type": "mixed",
            "features": ["sd_slot", "duplex", "lcd", "wifi"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_7750",
            "short_name": "EcoTank ET-7750",
            "description_chat_gpt": "A3 photo 5-colour all-in-one (pigment BK + dye CMY + photo BK).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 360,
            "nozzle_count_per_colour": 59,
            "total_colours": 5,
            "original_rrp_gbp": 699.00,
            "compatible_ink_bottles": ["105", "106"],
            "ink_type": "mixed",
            "features": ["duplex", "sd_slot", "lcd", "wifi"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_8500",
            "short_name": "EcoTank ET-8500",
            "description_chat_gpt": "A4 photo 6-colour all-in-one (pigment BK + dye PBK, C, M, Y, Gray).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 360,  # per colour bank
            "nozzle_count_per_colour": 360,
            "total_colours": 6,
            "original_rrp_gbp": 699.00,
            "compatible_ink_bottles": ["114"],
            "ink_type": "mixed",
            "features": ["duplex", "sd_slot", "touchscreen", "wifi", "cd_dvd_print"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_8550",
            "short_name": "EcoTank ET-8550",
            "description_chat_gpt": "A3+ photo 6-colour all-in-one (pigment BK + dye PBK, C, M, Y, Gray).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 360,
            "nozzle_count_per_colour": 360,
            "total_colours": 6,
            "original_rrp_gbp": 799.00,
            "compatible_ink_bottles": ["114"],
            "ink_type": "mixed",
            "features": ["duplex", "sd_slot", "touchscreen", "wifi", "cd_dvd_print"]
        })

        # --- Wide-format office (A3+) ---
        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_14000",
            "short_name": "EcoTank ET-14000",
            "description_chat_gpt": "A3+ single-function printer (print-only).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 360,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 429.00,
            "compatible_ink_bottles": ["664"],
            "ink_type": "dye",
            "features": ["a3_plus"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_15000",
            "short_name": "EcoTank ET-15000",
            "description_chat_gpt": "A3+ 4-in-1 (Print/Scan/Copy/Fax) compact.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 400,
            "nozzle_count_per_colour": 128,
            "total_colours": 4,
            "original_rrp_gbp": 599.00,
            "compatible_ink_bottles": ["102"],
            "ink_type": "dye",
            "features": ["a3_plus", "duplex", "adf", "fax", "ethernet", "wifi", "lcd"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_16150",
            "short_name": "EcoTank ET-16150",
            "description_chat_gpt": "A3+ single-function (print-only) high-speed, pigment.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 619.00,
            "compatible_ink_bottles": ["113"],
            "ink_type": "pigment",
            "features": ["a3_plus", "duplex", "ethernet", "wifi", "lcd"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_16600",
            "short_name": "EcoTank ET-16600",
            "description_chat_gpt": "A3+ 4-in-1 office model (pigment) with ADF and duplex.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 256,
            "total_colours": 4,
            "original_rrp_gbp": 1099.99,
            "compatible_ink_bottles": ["113"],
            "ink_type": "pigment",
            "features": ["a3_plus", "duplex", "adf", "fax", "ethernet", "wifi", "touchscreen"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson_ecotank",
            "part_number": "et_16650",
            "short_name": "EcoTank ET-16650",
            "description_chat_gpt": "A3+ 4-in-1 office (pigment) higher-speed variant.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 256,
            "total_colours": 4,
            "original_rrp_gbp": 1299.00,
            "compatible_ink_bottles": ["113"],
            "ink_type": "pigment",
            "features": ["a3_plus", "duplex", "adf", "fax", "ethernet", "wifi", "touchscreen"]
        })

        # --- Monochrome EcoTank ---
        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "mono",
            "manufacturer": "epson_ecotank",
            "part_number": "et_m1120",
            "short_name": "EcoTank ET-M1120",
            "description_chat_gpt": "A4 mono print-only (ultra low running cost).",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 0,
            "total_colours": 1,
            "original_rrp_gbp": 199.99,
            "compatible_ink_bottles": ["110"],
            "ink_type": "pigment",
            "features": ["wifi"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "mono",
            "manufacturer": "epson_ecotank",
            "part_number": "et_m2170",
            "short_name": "EcoTank ET-M2170",
            "description_chat_gpt": "A4 mono 3-in-1 (Print/Scan/Copy) with duplex.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 400,
            "nozzle_count_per_colour": 0,
            "total_colours": 1,
            "original_rrp_gbp": 249.00,
            "compatible_ink_bottles": ["111"],
            "ink_type": "pigment",
            "features": ["duplex", "ethernet", "wifi", "lcd"]
        })

        parts.append({
            "classification": "printer",
            "type": "inkjet",
            "size": "a4",
            "color": "mono",
            "manufacturer": "epson_ecotank",
            "part_number": "et_m3170",
            "short_name": "EcoTank ET-M3170",
            "description_chat_gpt": "A4 mono 4-in-1 (Print/Scan/Copy/Fax) with duplex.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 0,
            "total_colours": 1,
            "original_rrp_gbp": 349.00,
            "compatible_ink_bottles": ["111"],
            "ink_type": "pigment",
            "features": ["fax", "adf", "duplex", "ethernet", "wifi", "lcd"]
        })

        

    oomp.add_parts(parts, make_files=make_files)
    