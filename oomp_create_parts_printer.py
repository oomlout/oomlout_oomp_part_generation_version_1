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

    #epson workforce
    if True:
        # --- Mobile A4 (WF) ---
        parts.append({
            "classification": "WorkForce",
            "type": "Mobile Inkjet Printer",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_100w",
            "short_name": "Epson WorkForce WF-100W",
            "description_chat_gpt": "Portable A4 inkjet with built-in battery for mobile printing.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 128,
            "nozzle_count_per_colour": 42,
            "total_colours": 4,
            "original_rrp_gbp": 249.99,
            "compatible_ink_bottles": ["T2661", "T2670"],
            "ink_type": "pigment_black_dye_colour",
            "features": ["wireless", "battery", "usb_charging"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "Mobile Inkjet Printer",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_110w",
            "short_name": "Epson WorkForce WF-110W",
            "description_chat_gpt": "Updated portable A4 printer with Wi-Fi and USB charging.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 279.99,
            "compatible_ink_bottles": ["266", "267"],
            "ink_type": "pigment_black_dye_colour",
            "features": ["wireless", "wifi_direct", "battery_option", "usb"]
        })

        # --- Early A4 WF single/multi-function (16/18/27-series DURABrite) ---
        parts.append({
            "classification": "WorkForce",
            "type": "Single-Function Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2010w",
            "short_name": "Epson WorkForce WF-2010W",
            "description_chat_gpt": "Compact single-function A4 inkjet with Wi-Fi for home/small office.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 128,
            "nozzle_count_per_colour": 42,
            "total_colours": 4,
            "original_rrp_gbp": 99.99,
            "compatible_ink_bottles": ["16", "16XL"],
            "ink_type": "pigment",
            "features": ["wifi", "usb", "manual_duplex"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2510wf",
            "short_name": "Epson WorkForce WF-2510WF",
            "description_chat_gpt": "Entry-level 4-in-1 (print/scan/copy/fax) for home offices.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 128,
            "nozzle_count_per_colour": 42,
            "total_colours": 4,
            "original_rrp_gbp": 79.99,
            "compatible_ink_bottles": ["16", "16XL"],
            "ink_type": "pigment",
            "features": ["wifi", "fax", "adf", "usb"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2520nf",
            "short_name": "Epson WorkForce WF-2520NF",
            "description_chat_gpt": "4-in-1 with Ethernet and fax for wired small offices.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 128,
            "nozzle_count_per_colour": 42,
            "total_colours": 4,
            "original_rrp_gbp": 89.99,
            "compatible_ink_bottles": ["16", "16XL"],
            "ink_type": "pigment",
            "features": ["ethernet", "fax", "adf", "usb"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2530wf",
            "short_name": "Epson WorkForce WF-2530WF",
            "description_chat_gpt": "Wireless 4-in-1 with ADF; compact and affordable.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 128,
            "nozzle_count_per_colour": 42,
            "total_colours": 4,
            "original_rrp_gbp": 89.99,
            "compatible_ink_bottles": ["16", "16XL"],
            "ink_type": "pigment",
            "features": ["wifi", "fax", "adf", "usb"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2540wf",
            "short_name": "Epson WorkForce WF-2540WF",
            "description_chat_gpt": "4-in-1 with both Wi-Fi and Ethernet for multi-PC setups.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 128,
            "nozzle_count_per_colour": 42,
            "total_colours": 4,
            "original_rrp_gbp": 99.99,
            "compatible_ink_bottles": ["16", "16XL"],
            "ink_type": "pigment",
            "features": ["wifi", "ethernet", "fax", "adf"]
        })

        # --- WF-26xx / 27xx A4 (16-series) ---
        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2630wf",
            "short_name": "Epson WorkForce WF-2630WF",
            "description_chat_gpt": "Affordable 4-in-1 with Wi-Fi and remote print services.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 79.99,
            "compatible_ink_bottles": ["16", "16XL"],
            "ink_type": "pigment",
            "features": ["wifi", "fax", "adf", "airprint"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2650dwf",
            "short_name": "Epson WorkForce WF-2650DWF",
            "description_chat_gpt": "4-in-1 with auto duplex and Wi-Fi Direct.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 99.99,
            "compatible_ink_bottles": ["16", "16XL"],
            "ink_type": "pigment",
            "features": ["duplex", "wifi", "wifi_direct", "fax", "adf"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2660dwf",
            "short_name": "Epson WorkForce WF-2660DWF",
            "description_chat_gpt": "4-in-1 with NFC and touchscreen for easy mobile printing.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 119.99,
            "compatible_ink_bottles": ["16", "16XL"],
            "ink_type": "pigment",
            "features": ["duplex", "nfc", "touchscreen", "wifi", "ethernet"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2750dwf",
            "short_name": "Epson WorkForce WF-2750DWF",
            "description_chat_gpt": "Compact duplex 4-in-1 with LCD screen for home offices.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 99.99,
            "compatible_ink_bottles": ["16", "16XL"],
            "ink_type": "pigment",
            "features": ["duplex", "wifi", "lcd", "adf", "fax"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2760dwf",
            "short_name": "Epson WorkForce WF-2760DWF",
            "description_chat_gpt": "PrecisionCore variant of WF-2750 with faster output.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 400,
            "nozzle_count_per_colour": 128,
            "total_colours": 4,
            "original_rrp_gbp": 129.99,
            "compatible_ink_bottles": ["16", "16XL"],
            "ink_type": "pigment",
            "features": ["duplex", "wifi", "ethernet", "touchscreen"]
        })

        # --- WF-28xx A4 (603/604/503 inks) ---
        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2810dwf",
            "short_name": "Epson WorkForce WF-2810DWF",
            "description_chat_gpt": "Basic 4-in-1 with LCD, Wi-Fi, and auto duplex.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 79.99,
            "compatible_ink_bottles": ["603", "603XL"],
            "ink_type": "pigment_black_dye_colour",
            "features": ["duplex", "wifi", "lcd", "fax", "adf"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2830dwf",
            "short_name": "Epson WorkForce WF-2830DWF",
            "description_chat_gpt": "4-in-1 with 30-page ADF, duplex and wireless printing.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 79.99,
            "compatible_ink_bottles": ["603", "603XL"],
            "ink_type": "pigment_black_dye_colour",
            "features": ["duplex", "adf", "wifi", "usb", "fax"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2850dwf",
            "short_name": "Epson WorkForce WF-2850DWF",
            "description_chat_gpt": "Compact 4-in-1 with colour screen and auto duplexing.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 89.99,
            "compatible_ink_bottles": ["603", "603XL"],
            "ink_type": "pigment_black_dye_colour",
            "features": ["duplex", "wifi", "lcd", "adf", "fax"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2860dwf",
            "short_name": "Epson WorkForce WF-2860DWF",
            "description_chat_gpt": "Sleek 4-in-1 with PrecisionCore, 150-sheet tray and 6.1cm touchscreen.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 400,
            "nozzle_count_per_colour": 128,
            "total_colours": 4,
            "original_rrp_gbp": 129.99,
            "compatible_ink_bottles": ["502", "502XL"],
            "ink_type": "pigment_black_dye_colour",
            "features": ["duplex", "touchscreen", "wifi", "nfc", "adf"]
        })

        # Newer WF-29xx (604 / 503 inks)
        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2910dwf",
            "short_name": "Epson WorkForce WF-2910DWF",
            "description_chat_gpt": "Modern 4-in-1 A4 inkjet focused on affordability and ease.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 84.99,
            "compatible_ink_bottles": ["604", "604XL"],
            "ink_type": "pigment_black_dye_colour",
            "features": ["duplex", "wifi", "usb", "adf", "fax"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2930dwf",
            "short_name": "Epson WorkForce WF-2930DWF",
            "description_chat_gpt": "4-in-1 with 30-page ADF and 3.7cm LCD for productivity.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 89.99,
            "compatible_ink_bottles": ["604", "604XL"],
            "ink_type": "pigment_black_dye_colour",
            "features": ["duplex", "wifi", "adf", "lcd", "fax"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2935dwf",
            "short_name": "Epson WorkForce WF-2935DWF",
            "description_chat_gpt": "Retail variant of WF-2930 with same core features.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 89.99,
            "compatible_ink_bottles": ["604", "604XL"],
            "ink_type": "pigment_black_dye_colour",
            "features": ["duplex", "wifi", "adf", "fax", "lcd"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2950dwf",
            "short_name": "Epson WorkForce WF-2950DWF",
            "description_chat_gpt": "4-in-1 with auto duplex and Epson Smart Panel support.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 180,
            "nozzle_count_per_colour": 59,
            "total_colours": 4,
            "original_rrp_gbp": 99.99,
            "compatible_ink_bottles": ["604", "604XL"],
            "ink_type": "pigment_black_dye_colour",
            "features": ["duplex", "wifi", "smartpanel_app", "adf", "fax"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2960dwf",
            "short_name": "Epson WorkForce WF-2960DWF",
            "description_chat_gpt": "High-speed 4-in-1 with PrecisionCore and 6.1cm touchscreen.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 400,
            "nozzle_count_per_colour": 128,
            "total_colours": 4,
            "original_rrp_gbp": 129.99,
            "compatible_ink_bottles": ["503", "503XL"],
            "ink_type": "pigment_black_dye_colour",
            "features": ["duplex", "touchscreen", "adf", "wifi", "ethernet"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_2965dwf",
            "short_name": "Epson WorkForce WF-2965DWF",
            "description_chat_gpt": "Variant of WF-2960 with dual paper trays for extra capacity.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 400,
            "nozzle_count_per_colour": 128,
            "total_colours": 4,
            "original_rrp_gbp": 139.99,
            "compatible_ink_bottles": ["503", "503XL"],
            "ink_type": "pigment_black_dye_colour",
            "features": ["duplex", "dual_trays", "touchscreen", "adf", "wifi"]
        })

        # --- WorkForce A4 Pro mid/high (27/34/79-series pigment) ---
        parts.append({
            "classification": "WorkForce Pro",
            "type": "Single-Function Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_3010dw",
            "short_name": "Epson WorkForce WF-3010DW",
            "description_chat_gpt": "A4 single-function with duplex and Wi-Fi/Ethernet.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 384,
            "nozzle_count_per_colour": 128,
            "total_colours": 4,
            "original_rrp_gbp": 139.99,
            "compatible_ink_bottles": ["18", "18XL"],
            "ink_type": "pigment",
            "features": ["duplex", "ethernet", "wifi"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_3520dwf",
            "short_name": "Epson WorkForce WF-3520DWF",
            "description_chat_gpt": "Fast 4-in-1 with duplex ADF and 250-sheet tray.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 384,
            "nozzle_count_per_colour": 128,
            "total_colours": 4,
            "original_rrp_gbp": 149.99,
            "compatible_ink_bottles": ["27", "27XL"],
            "ink_type": "pigment",
            "features": ["duplex_print_scan", "ethernet", "wifi", "adf", "fax"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_3540dtwf",
            "short_name": "Epson WorkForce WF-3540DTWF",
            "description_chat_gpt": "Flagship 4-in-1 with dual trays and large touch panel.",
            "printhead_technology": "Micro Piezo",
            "nozzle_count_black": 384,
            "nozzle_count_per_colour": 128,
            "total_colours": 4,
            "original_rrp_gbp": 199.99,
            "compatible_ink_bottles": ["27", "27XL"],
            "ink_type": "pigment",
            "features": ["dual_trays", "duplex_adf", "ethernet", "wifi", "touchscreen"]
        })

        parts.append({
            "classification": "WorkForce Pro",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_3640dtwf",
            "short_name": "Epson WorkForce Pro WF-3640DTWF",
            "description_chat_gpt": "WorkForce Pro 4-in-1 with PrecisionCore and dual trays.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 256,
            "total_colours": 4,
            "original_rrp_gbp": 179.99,
            "compatible_ink_bottles": ["27", "27XL"],
            "ink_type": "pigment",
            "features": ["precisioncore", "duplex_print_scan", "dual_trays", "wifi", "ethernet"]
        })

        parts.append({
            "classification": "WorkForce Pro",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_4720dwf",
            "short_name": "Epson WorkForce Pro WF-4720DWF",
            "description_chat_gpt": "Compact Pro 4-in-1 with fast 18ppm and 250-sheet tray.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 149.99,
            "compatible_ink_bottles": ["34", "34XL"],
            "ink_type": "pigment",
            "features": ["duplex", "wifi", "nfc", "250_sheet_tray", "adf"]
        })

        parts.append({
            "classification": "WorkForce Pro",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_4730dtwf",
            "short_name": "Epson WorkForce Pro WF-4730DTWF",
            "description_chat_gpt": "High-capacity dual-tray variant for busier offices.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 199.99,
            "compatible_ink_bottles": ["34", "34XL", "34XXL"],
            "ink_type": "pigment",
            "features": ["dual_trays", "duplex", "wifi_ethernet", "adf", "touchscreen"]
        })

        parts.append({
            "classification": "WorkForce Pro",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_4740dtwf",
            "short_name": "Epson WorkForce Pro WF-4740DTWF",
            "description_chat_gpt": "Top A4 Pro with 50-sheet duplex ADF and 10.9cm touchscreen.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 249.99,
            "compatible_ink_bottles": ["34", "34XL", "34XXL"],
            "ink_type": "pigment",
            "features": ["dual_trays", "duplex_adf_50", "touchscreen", "nfc", "ethernet"]
        })

        # Pro single/4-in-1 with 79-series DURABrite Pro
        parts.append({
            "classification": "WorkForce Pro",
            "type": "Single-Function Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_5110dw",
            "short_name": "Epson WorkForce Pro WF-5110DW",
            "description_chat_gpt": "A4 single-function Pro with PCL/PS and high-yield inks.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 179.99,
            "compatible_ink_bottles": ["79XL", "79XXL"],
            "ink_type": "pigment",
            "features": ["duplex", "ethernet", "pcl_ps", "high_capacity_tray"]
        })

        parts.append({
            "classification": "WorkForce Pro",
            "type": "Single-Function Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_5190dw",
            "short_name": "Epson WorkForce Pro WF-5190DW",
            "description_chat_gpt": "Network single-function with security features and PIN print.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 199.99,
            "compatible_ink_bottles": ["79XL", "79XXL"],
            "ink_type": "pigment",
            "features": ["duplex", "gigabit_ethernet", "pin_print", "pcl_ps"]
        })

        parts.append({
            "classification": "WorkForce Pro",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_5620dwf",
            "short_name": "Epson WorkForce Pro WF-5620DWF",
            "description_chat_gpt": "4-in-1 Pro with fast duplex scanning and 50-sheet ADF.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 249.99,
            "compatible_ink_bottles": ["79XL", "79XXL"],
            "ink_type": "pigment",
            "features": ["duplex_print_scan", "adf_50", "ethernet", "large_yield_inks"]
        })

        parts.append({
            "classification": "WorkForce Pro",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_5690dwf",
            "short_name": "Epson WorkForce Pro WF-5690DWF",
            "description_chat_gpt": "Managed-print ready Pro MFP with security and remote admin.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 299.99,
            "compatible_ink_bottles": ["79XL", "79XXL"],
            "ink_type": "pigment",
            "features": ["duplex", "security_features", "remote_admin", "adf", "fax"]
        })

        # Pro high-volume A4 (6090/6590) — departmental class
        parts.append({
            "classification": "WorkForce Pro",
            "type": "Single-Function Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_6090dw",
            "short_name": "Epson WorkForce Pro WF-6090DW",
            "description_chat_gpt": "High-speed single-function with 500-sheet tray and options.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 349.99,
            "compatible_ink_bottles": ["XL_Black_10k", "XL_Colour_5k"],
            "ink_type": "pigment",
            "features": ["duplex", "pcl_ps", "xl_inks", "optional_tray"]
        })

        parts.append({
            "classification": "WorkForce Pro",
            "type": "All-in-One Inkjet",
            "size": "a4",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_6590dwf",
            "short_name": "Epson WorkForce Pro WF-6590DWF",
            "description_chat_gpt": "Enterprise-class A4 MFP with very high yield inks.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 649.99,
            "compatible_ink_bottles": ["replaceable_ink_pack_black_~10k", "colour_~7.5k"],
            "ink_type": "pigment",
            "features": ["duplex_scan_print", "large_touch", "secure_print", "ldap", "fax"]
        })

        # --- A3 / A3+ WF (27 / 405 DURABrite) ---
        parts.append({
            "classification": "WorkForce",
            "type": "Single-Function Inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_7110dtw",
            "short_name": "Epson WorkForce WF-7110DTW",
            "description_chat_gpt": "A3+ single-function with dual trays and duplex printing.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 256,
            "total_colours": 4,
            "original_rrp_gbp": 179.99,
            "compatible_ink_bottles": ["27", "27XL"],
            "ink_type": "pigment",
            "features": ["a3_plus", "duplex", "ethernet", "wifi"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_7610dwf",
            "short_name": "Epson WorkForce WF-7610DWF",
            "description_chat_gpt": "Versatile A3+ 4-in-1 with 250-sheet tray and rear feed.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 256,
            "total_colours": 4,
            "original_rrp_gbp": 249.99,
            "compatible_ink_bottles": ["27", "27XL"],
            "ink_type": "pigment",
            "features": ["a3_copy_scan", "duplex_adf", "wifi", "ethernet", "fax"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_7620dtwf",
            "short_name": "Epson WorkForce WF-7620DTWF",
            "description_chat_gpt": "A3+ 4-in-1 with two front cassettes plus rear feed.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 256,
            "total_colours": 4,
            "original_rrp_gbp": 299.99,
            "compatible_ink_bottles": ["27", "27XL"],
            "ink_type": "pigment",
            "features": ["dual_trays", "a3_duplex_scan", "wifi", "ethernet", "fax"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_7710dwf",
            "short_name": "Epson WorkForce WF-7710DWF",
            "description_chat_gpt": "A3+ 4-in-1 with 35-sheet duplex ADF and touchscreen.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 256,
            "total_colours": 4,
            "original_rrp_gbp": 199.99,
            "compatible_ink_bottles": ["27XL", "27XXL"],
            "ink_type": "pigment",
            "features": ["a3_plus", "duplex_scan_copy", "wifi_direct", "ethernet", "touchscreen"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_7720dtwf",
            "short_name": "Epson WorkForce WF-7720DTWF",
            "description_chat_gpt": "Dual-tray version of WF-7710 for flexible A3 media handling.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 256,
            "total_colours": 4,
            "original_rrp_gbp": 249.99,
            "compatible_ink_bottles": ["27XL", "27XXL"],
            "ink_type": "pigment",
            "features": ["dual_a3_trays", "duplex_adf", "wifi_nfc", "ethernet", "fax"]
        })

        # Latest-gen A3+ WF with 405 inks
        parts.append({
            "classification": "WorkForce",
            "type": "Single-Function Inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_7310dtw",
            "short_name": "Epson WorkForce WF-7310DTW",
            "description_chat_gpt": "A3+ single-function with two 250-sheet trays and fast draft speeds.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 256,
            "total_colours": 4,
            "original_rrp_gbp": 179.99,
            "compatible_ink_bottles": ["405", "405XL", "405XXL"],
            "ink_type": "pigment",
            "features": ["a3_plus", "duplex", "dual_trays", "wifi", "ethernet"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_7830dtwf",
            "short_name": "Epson WorkForce WF-7830DTWF",
            "description_chat_gpt": "A3+ 4-in-1 with high-speed printing and dual trays.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 199.99,
            "compatible_ink_bottles": ["405", "405XL"],
            "ink_type": "pigment",
            "features": ["dual_trays", "a3_duplex_scan", "wifi_direct", "ethernet", "adf_50"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_7835dtwf",
            "short_name": "Epson WorkForce WF-7835DTWF",
            "description_chat_gpt": "Retail configuration of WF-7830 with second cassette.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 219.99,
            "compatible_ink_bottles": ["405", "405XL", "405XXL"],
            "ink_type": "pigment",
            "features": ["dual_trays", "touchscreen", "adf", "wifi", "fax"]
        })

        parts.append({
            "classification": "WorkForce",
            "type": "All-in-One Inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_7840dtwf",
            "short_name": "Epson WorkForce WF-7840DTWF",
            "description_chat_gpt": "Flagship A3+ 4-in-1 with triple input, duplex scan and 405 XXL inks.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 249.99,
            "compatible_ink_bottles": ["405", "405XL", "405XXL"],
            "ink_type": "pigment",
            "features": ["triple_input", "duplex_scan", "10.9cm_touchscreen", "ethernet", "fax"]
        })

        # --- Pro A3+ departmental (T75xx / ink packs) ---
        parts.append({
            "classification": "WorkForce Pro",
            "type": "Single-Function Inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_8010dw",
            "short_name": "Epson WorkForce Pro WF-8010DW",
            "description_chat_gpt": "A3+ workgroup printer with ultra-high capacity cartridges and expandable trays.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 399.99,
            "compatible_ink_bottles": ["T7541","T7542","T7543","T7544","T7551","T7552","T7553","T7554"],
            "ink_type": "pigment",
            "features": ["a3_plus", "duplex", "pcl_ps", "optional_trays", "gigabit_ethernet"]
        })

        parts.append({
            "classification": "WorkForce Pro",
            "type": "Single-Function Inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_8090dw",
            "short_name": "Epson WorkForce Pro WF-8090DW",
            "description_chat_gpt": "Higher-end A3+ single-function with very high-yield ink packs.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 499.99,
            "compatible_ink_bottles": ["T7561","T7562","T7563","T7564"],
            "ink_type": "pigment",
            "features": ["a3_plus", "replaceable_ink_packs", "lcd", "gigabit_ethernet"]
        })

        parts.append({
            "classification": "WorkForce Pro",
            "type": "All-in-One Inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_8510dwf",
            "short_name": "Epson WorkForce Pro WF-8510DWF",
            "description_chat_gpt": "A3+ MFP with LDAP, optional HDD for forms and robust duty cycle.",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 799.99,
            "compatible_ink_bottles": ["T7481","T7482","T7483","T7484"],
            "ink_type": "pigment",
            "features": ["a3_copy_scan", "duplex_adf", "large_touchscreen", "fax", "security"]
        })

        parts.append({
            "classification": "WorkForce Pro",
            "type": "All-in-One Inkjet",
            "size": "a3",
            "color": "color",
            "manufacturer": "epson",
            "part_number": "wf_8590dwf",
            "short_name": "Epson WorkForce Pro WF-8590DWF",
            "description_chat_gpt": "Flagship A3+ Pro with Replaceable Ink Pack System (very high yields).",
            "printhead_technology": "PrecisionCore",
            "nozzle_count_black": 800,
            "nozzle_count_per_colour": 800,
            "total_colours": 4,
            "original_rrp_gbp": 1499.99,
            "compatible_ink_bottles": ["Ink_Pack_System"],
            "ink_type": "pigment",
            "features": ["a3_print_copy_scan", "rips_ink_packs", "finishing_options", "advanced_security", "gigabit_lan"]
        })


    oomp.add_parts(parts, make_files=make_files)
    