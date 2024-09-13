import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

    ## color used for chip type

    
    # nisbet containers
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_rectangle"
    part_details["size"] = ["1000_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "nisbet_fiesta"
    part_details["part_number"] = "large_dm183"
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)    

    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_rectangle"
    part_details["size"] = ["650_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "nisbet_fiesta"
    part_details["part_number"] = "medium_dm182"
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)  

    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_rectangle"
    part_details["size"] = ["500_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "nisbet_fiesta"
    part_details["part_number"] = "small_dm181"
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details) 

    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_circle"
    part_details["size"] = ["150_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "nisbet_fiesta"
    part_details["part_number"] = "ct083"
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)        

    #sauce pots
    
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_circle"
    part_details["size"] = ["60_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = "heavy_duty"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "satco"
    part_details["part_number"] = ""
    part_details["short_name"] = ""  
    part_details["distributors"] = []
    parts.append(part_details)  

    # sauce pots attached lids
    
    # majestic 1 oz
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_circle"
    part_details["size"] = ["30_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = "hinged_lid"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "majestic"
    part_details["part_number"] = "05385_pv11"
    part_details["short_name"] = ""  
    part_details["upc_number"] = "5028181053863"
    part_details["weight"] = "3.14 g"
    part_details["cost_per"] = "£0.0276"
    part_details["cost_per_ebay"] = "£0.11"
    part_details["cost_per_100"] = "£0.0276"
    part_details["cost_per_1000"] = "£0.0276"
    part_details["link_purchase"] = ["https://www.cooksmill.co.uk/hinged-sauce-container-1oz-(pack-50)","https://www.ebay.co.uk/itm/175662239573?var=475027888766"]
    part_details["oomlout_mechanical_hole_cutout_size"] ="46 mm"
    part_details["oomlout_mechanical_hole_cutout_top_size"] ="49 mm"    
    part_details["oomlout_mechanical_hole_cutout_lip_size"] ="46 mm"
    part_details["oomlout_mechanical_hole_cutout_12_mm_lift"] ="44 mm"
    parts.append(part_details)  

    #majestic 2 oz
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_circle"
    part_details["size"] = ["60_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = "hinged_lid"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "majestic"
    part_details["part_number"] = "05390_pv22"
    part_details["short_name"] = ""  
    part_details["upc_number"] = "5028181053917"
    part_details["weight"] = "4.19 g"
    part_details["cost_per"] = "£0.0324"
    part_details["cost_per_ebay"] = "£0.11"
    part_details["cost_per_100"] = "£0.0324"
    part_details["cost_per_1000"] = "£0.0324"
    part_details["link_purchase"] = ["https://www.cooksmill.co.uk/majestic-hinged-sauce-container-2oz-(pack-50)","https://www.ebay.co.uk/itm/175662239573?var=475027888760"]
    part_details["oomlout_mechanical_hole_cutout_size"] ="59 mm"
    part_details["oomlout_mechanical_hole_cutout_top_size"] ="61 mm"    
    part_details["oomlout_mechanical_hole_cutout_lip_size"] ="59 mm"
    part_details["oomlout_mechanical_hole_cutout_12_mm_lift"] ="55 mm"
    parts.append(part_details)  

    #4 oz
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_circle"
    part_details["size"] = ["120_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = "hinged_lid"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "majestic"
    part_details["part_number"] = "05390_pv44"
    part_details["short_name"] = ""  
    part_details["upc_number"] = ""
    part_details["weight"] = "7.53 g"
    part_details["cost_per"] = "£0.0324"
    part_details["cost_per_ebay"] = "£0.11"
    part_details["cost_per_100"] = "£0.073"
    part_details["cost_per_1000"] = "£0.057"
    part_details["link_purchase"] = ["https://www.amazon.co.uk/dp/B071P1XVLT?psc=1&smid=A2RGWAHP8GK42C&ref_=chk_typ_imgToDp","https://www.ebay.co.uk/itm/175662239573?var=475027888760"]
    part_details["oomlout_mechanical_hole_cutout_size"] ="66 mm"
    part_details["oomlout_mechanical_hole_cutout_top_size"] ="69 mm"    
    part_details["oomlout_mechanical_hole_cutout_lip_size"] ="66 mm"
    part_details["oomlout_mechanical_hole_cutout_12_mm_lift"] ="57 mm"
    parts.append(part_details)  

    # systempak
    
    #2030slc
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_circle"
    part_details["size"] = ["1000_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = "124_mm_diameter_124_mm_height_tamper_evident"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "systempak"
    part_details["part_number"] = "2030slc"
    part_details["short_name"] = ""
    part_details["upc_number"] = ""
    part_details["weight"] = "36 g"
    part_details["cost_per"] = "£0.246" # # 64.95 / 264 = 0.246
    part_details["link_purchase"] = ["https://systempak.net/product/1000ml-round-122mm-diameter-slimline-tamper-evident-container-and-lids/"]    
    part_details["box_quantity"] = "264"
    part_details["note"] = "only available by the pallet"
    parts.append(part_details)


    #2021
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_circle"
    part_details["size"] = ["870_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = "118_mm_diameter_125_mm_height_tamper_evident"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "systempak"
    part_details["part_number"] = "2021"
    part_details["short_name"] = ""
    part_details["upc_number"] = ""
    part_details["weight"] = "32 g"
    part_details["cost_per"] = "£0.326" # # 74.95 / 230 = 0.326
    part_details["link_purchase"] = ["https://systempak.net/product/870ml-x-118od-round-plastic-tamper-proof-food-containers-and-lids/"]
    part_details["box_quantity"] = "230"
    part_details["note"] = "only available by the pallet"
    parts.append(part_details)

    #254
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_circle"
    part_details["size"] = ["670_ml"]
    part_details["color"] = [""]
    part_details["description_main"] = "105_mm_diameter_100_mm_height_tamper_evident"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "systempak"
    part_details["part_number"] = "254"
    part_details["short_name"] = ""
    part_details["upc_number"] = ""
    part_details["weight"] = "35 g"
    part_details["cost_per"] = "£0.199" # # 62.95 / 316 = 0.199
    part_details["link_purchase"] = ["https://systempak.net/product/670ml-round-105mm-diameter-tamper-evident-containers-and-lids/"]
    part_details["box_quantity"] = "316"
    parts.append(part_details)

    # 253
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_circle"
    part_details["size"] = ["660_ml"]
    part_details["color"] = [""]
    ###### don't know the height!
    #part_details["description_main"] = "95_mm_diameter_100_mm_height_tamper_evident"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "systempak"
    part_details["part_number"] = "253"
    part_details["short_name"] = ""
    part_details["upc_number"] = ""
    part_details["weight"] = "35 g"
    part_details["cost_per"] = "£0.178" # # 77.95 / 410 = 0.178
    part_details["link_purchase"] = ["https://systempak.net/product/660ml-round-95mm-diameter-tamper-evident-containers-and-lids/"]
    part_details["box_quantity"] = "410"
    #parts.append(part_details)

    #2026
    part_details = {}
    part_details["classification"] = "packaging"
    part_details["type"] = "takeaway_container_circle"
    part_details["size"] = ["1000_ml"]
    part_details["color"] = [""]    
    part_details["description_main"] = "131_mm_diameter_120_mm_height_tamper_evident"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "systempak"
    part_details["part_number"] = "2026"
    part_details["short_name"] = ""
    part_details["upc_number"] = ""
    part_details["weight"] = "41 g"
    part_details["cost_per"] = "£0.299" # # 58.96 / 197 = 0.299
    part_details["link_purchase"] = ["https://systempak.net/product/1000ml-round-131mm-diameter-tamper-evident-containers-with-handles-and-lids/"]
    part_details["box_quantity"] = "197"
    parts.append(part_details)






    oomp.add_parts(parts, make_files=make_files)
    