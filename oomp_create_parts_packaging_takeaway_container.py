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
    parts.append(part_details)  


    oomp.add_parts(parts, make_files=make_files)
    