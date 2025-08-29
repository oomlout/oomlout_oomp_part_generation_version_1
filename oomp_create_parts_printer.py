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

    oomp.add_parts(parts, make_files=make_files)
    