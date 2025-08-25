import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "tool"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = copy.deepcopy(part_details)

    #caliper
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "measure_caliper_digital"
        part_details["size"] = "150_mm_length"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "mitutoyo"
        part_details["part_number_exact"] = "MIT500-196-30"
        part_details["part_number"] = part_details["part_number_exact"].lower().replace("-","_").replace(" ","_").replace(".","_")
        part_details["part_number_distributor_amazon"] = "B00IG46NL2"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/gp/product/{part_details['part_number_distributor_amazon']}"
        parts.append(part_details)

    # chiller
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "water_chiller"
        part_details["size"] = ["420_mm_width_350_mm_height_500_mm_depth"]
        part_details["color"] = [""]
        part_details["description_main"] = [""]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = "hpc_laser"
        part_details["part_number"] = "cw4000"
        parts.append(part_details)

    
    # diy tool
    if True:
        #   drill and imact driver
        if True:
            #       dewalt
            if True:
                #drill_hammer
                part_details = {}
                part_details["classification"] = "tool"
                part_details["type"] = "drill_hammer"
                part_details["size"] = ["18_volt_dewalt_tower"]
                part_details["color"] = [""]
                part_details["description_main"] = [""]
                part_details["description_extra"] = [""]
                part_details["manufacturer"] = "dewalt"
                part_details["part_number"] = "dc988"
                parts.append(part_details)
            
                part_details = copy.deepcopy(default_empty)
                part_details["type"] = "drill_hammer"
                part_details["size"] = "18_volt_dewalt_xr"
                part_details["manufacturer"] = "dewalt"
                part_details["part_number"] = "dcd778"
                part_details["part_number_distributor_amazon"] = "B07YSH4N1H"
                part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/gp/product/{part_details['part_number_distributor_amazon']}"
                part_details["link_distributor_dewalt"] = f"https://www.dewalt.co.uk/product/dcd778l2t-qw/18v-xr-brushless-hammer-drill-driver-2-x-4-ah?tid="
                parts.append(part_details)

                #imapact_driver
                part_details = copy.deepcopy(default_empty)
                part_details["type"] = "impact_driver"
                part_details["size"] = "18_volt_dewalt_xr"
                part_details["manufacturer"] = "dewalt"
                part_details["part_number"] = "dcf787"
                part_details["part_number_distributor_amazon"] = "B08S3RVHT8"
                part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/gp/product/{part_details['part_number_distributor_amazon']}"
                part_details["link_distributor_dewalt"] = f"https://www.dewalt.co.uk/product/dcf787n-xj/18v-xr-brushless-impact-driver-bare-unit"

                
                parts.append(part_details)


            #       ryobi
            if True:            
                part_details = {}
                part_details["classification"] = "tool"
                part_details["type"] = "drill_hammer"
                part_details["size"] = ["18_volt_ryobi_one"]
                part_details["color"] = [""]
                part_details["description_main"] = [""]
                part_details["description_extra"] = [""]
                part_details["manufacturer"] = "ryobi"
                part_details["part_number"] = "r18pd3"
                parts.append(part_details)

        # level
        if True:
            part_details = copy.deepcopy(default_empty)
            part_details["type"] = "level"
            part_details["size"] = ""
            part_details["color"] = ""
            part_details["description_main"] = "boat_level_230_mm_width_38_mm_height_15_mm_depth"
            part_details["description_extra"] = ""
            part_details["manufacturer"] = "draper"            
            part_details["part_number"] = "69563" 
            part_details["part_number_distributor_amazon"] = "B0001KA1A8"
            part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/gp/product/{part_details['part_number_distributor_amazon']}"
            part_details["link_distributor_draper"] = f"https://www.drapertools.com/product/69563/boat-spirit-level-230mm/"
            parts.append(part_details)
    
    
        # stud finder
        if True:
            part_details = copy.deepcopy(default_empty)
            part_details["type"] = "stud_finder"
            part_details["size"] = ""
            part_details["color"] = ""
            part_details["description_main"] = "70_mm_width_150_mm_height_35_mm_depth"
            part_details["description_extra"] = ""
            part_details["manufacturer"] = "stanley"
            part_details["part_number"] = "sth77404"            
            parts.append(part_details)
    
    # electrical
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "electrical_meter_clamp"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = [""]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = "aneng"
        part_details["part_number"] = "st180"
        parts.append(part_details)

    # knife
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "knife_utility"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = ["17_mm_blade"]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)

        #bin disposal can
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "knife_utility_blade_disposal_can"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = [""]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = "olfa"
        part_details["part_number"] = "dc_3"
        part_details["part_number_exact"] = "DC-3"
        parts.append(part_details)

    #laser cutter
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "laser_cutter"
        part_details["size"] = ["1200_mm_width_900_mm_height"]
        part_details["color"] = [""]
        part_details["description_main"] = [""]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = "hpc_laser"
        part_details["part_number"] = "1290"
        parts.append(part_details)


    # scale
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "scale"
        part_details["size"] = ["76_mm_width_114_mm_height_20_mm_depth"]
        part_details["color"] = [""]
        part_details["description_main"] = ["200_gram_capacity", "1000_gram_capacity"]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = "jewelry_scale"
        parts.append(part_details)

        
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "scale"
        part_details["size"] = ["70_mm_width_120_mm_height_40_mm_depth"]
        part_details["color"] = [""]
        part_details["description_main"] = ["200_gram_capacity"]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = "jewelry_scale"
        parts.append(part_details)


        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "scale"
        part_details["size"] = ["67_mm_width_120_mm_height_18_mm_depth"]
        part_details["color"] = [""]
        part_details["description_main"] = ["500_gram_capacity"]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = "jewelry_scale"
        parts.append(part_details)


    # screwdriver
    #define a part 
    if True:
        
        #multi_driver
        if True:
            part_details = copy.deepcopy(default_empty)
            part_details["type"] = "screw_driver_multi_driver"
            part_details["size"] = "full_size"
            part_details["manufacturer"] = "picquic"
            part_details_base_current = copy.deepcopy(part_details)
            
            #picquic
            if True:     
                description_mains = ["", "sixpac_plus_model", "hex_calibre_sae_model", "hex_calibre_metric_model",  "super_eight_plus_model",]
                for description_main in description_mains:
                    part_details = copy.deepcopy(part_details_base_current)
                    part_details["description_main"] = description_main
                    parts.append(part_details)
            
            #precision
            part_details = copy.deepcopy(part_details_base_current)
            part_details["size"] = "precision_size"
            part_details_base_current = copy.deepcopy(part_details)
            if True:
                description_mains = ["teeny_turner_model"]
                for description_main in description_mains:
                    part_details = copy.deepcopy(part_details_base_current)
                    part_details["description_main"] = description_main
                    parts.append(part_details)
                

                



        

        #precision
        if True:
            part_details = copy.deepcopy(default_empty)            
            part_details["type"] = "screw_driver_precision"

            default_current = copy.deepcopy(part_details)

            #wera kraftform micro
            part_details = copy.deepcopy(default_current)            
            part_details["manufacturer"] = "wera"
            default_wera_precision = copy.deepcopy(part_details)

            details = []            
            
            #2054 series hex head
            # 05118060001	0.7	-	40	97	3.0	1 9/16"	
            # 05118062001	0.9	-	40	97	3.0	1 9/16"	
            # 05118064001	1.3	-	40	97	3.0	1 9/16"	
            # 05118066001	1.5	-	60	97	3.0	2 3/8"	
            # 05118068001	2	-	60	97	3.0	2 3/8"	
            # 05118070001	2.5	-	60	97	4.0	2 3/8"	
            # 05118072001	3.0	-	60	97	4.0	2 3/8"	

            detail_default_current = {}
            detail_default_current["link_distributor_wera"] = "https://products.wera.de/en/screwdrivers_series_kraftform_micro_2054_micro.html"
            #0.7 mm, 05118060001            
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "hex_head_0_7_mm", "series": "2054", "part_number": "05118060001", "blade_length": 40, "blade_diameter": 3.0, "handle_length": 97})
            details.append(detail)
            #0.9 mm, 05118062001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "hex_head_0_9_mm", "series": "2054", "part_number": "05118062001", "blade_length": 40, "blade_diameter": 3.0, "handle_length": 97})
            details.append(detail)
            #1.3 mm, 05118064001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "hex_head_1_3_mm", "series": "2054", "part_number": "05118064001", "blade_length": 40, "blade_diameter": 3.0, "handle_length": 97})
            details.append(detail)
            #1.5 mm, 05118066001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "hex_head_1_5_mm", "series": "2054", "part_number": "05118066001", "blade_length": 60, "blade_diameter": 3.0, "handle_length": 97})
            details.append(detail)
            #2 mm 05118068001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "hex_head_2_mm", "series": "2054", "part_number": "05118068001", "blade_length": 60, "blade_diameter": 3.0, "handle_length": 97})
            details.append(detail)
            #2.5 mm 05118070001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "hex_head_2_5_mm", "series": "2054", "part_number": "05118070001", "blade_length": 60, "blade_diameter": 4.0, "handle_length": 97})
            details.append(detail)
            #3 mm 05118072001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "hex_head_3_mm", "series": "2054", "part_number": "05118072001", "blade_length": 60, "blade_diameter": 4.0, "handle_length": 97})
            details.append(detail)
            
            #2035 series slotted head
            # 05117990001	0.16	0.8	40	97	2.0	1/32"	1 9/16"	
            # 05117991001	0.18	1.0	40	97	2.0	0.04"	1 9/16"	
            # 05117992001	0.20	1.2	40	97	2.0	0.05"	1 9/16"	
            # 05118002001	0.23	1.5	40	97	2.0	1/16"	1 9/16"	
            # 05118003001	0.23	1.5	60	97	2.0	1/16"	2 3/8"	
            # 05118000001	0.25	1.2	40	97	2.0	0.05"	1 9/16"	
            # 05117993001	0.30	1.8	40	97	2.0	0.07"	1 9/16"	
            # 05118004001	0.30	1.8	60	97	2.0	0.07"	2 3/8"	
            # 05117997001	0.35	2.5	40	97	2.5	3/32"	1 9/16"	
            # 05118005001	0.40	2.0	40	97	2.5	5/64"	1 9/16"	
            # 05118006001	0.40	2.0	60	97	2.5	5/64"	2 3/8"	
            # 05117994001	0.40	2.5	50	97	2.5	3/32"	2"	
            # 05118008001	0.40	2.5	80	97	2.5	3/32"	3 1/8"	
            # 05117995001	0.50	3.0	50	97	3.0	1/8"	2"	
            # 05118010001	0.50	3.0	80	97	3.0	1/8"	3 1/8"	
            # 05118012001	0.60	3.5	80	97	4.0	9/64"	3 1/8"	
            # 05118014001	0.80	4.0	80	97	4.0	5/32"	3 1/8"
            
            detail_default_current = {}
            detail_default_current["link_distributor_wera"] = "https://products.wera.de/en/screwdrivers_series_kraftform_micro_2035_micro.html"            
            #0.8, 05117990001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_0_8_mm", "series": "2035", "part_number": "05117990001", "blade_length": 40, "blade_diameter": 2.0, "handle_length": 97})            
            details.append(detail)
            #1.0, 05117991001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_1_0_mm", "series": "2035", "part_number": "05117991001", "blade_length": 40, "blade_diameter": 2.0, "handle_length": 97})
            details.append(detail)
            #1.2, 05117992001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_1_2_mm", "series": "2035", "part_number": "05117992001", "blade_length": 40, "blade_diameter": 2.0, "handle_length": 97})
            details.append(detail)
            #1.5, 05118002001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_1_5_mm", "series": "2035", "part_number": "05118002001", "blade_length": 40, "blade_diameter": 2.0, "handle_length": 97})
            details.append(detail)
            #1.5 60 mm length, 05118003001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_1_5_mm", "series": "2035", "part_number": "05118003001", "blade_length": 60, "blade_diameter": 2.0, "handle_length": 97})
            details.append(detail)
            #1.8 05117993001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_1_8_mm", "series": "2035", "part_number": "05117993001", "blade_length": 40, "blade_diameter": 2.0, "handle_length": 97})
            details.append(detail)
            #1.8 60 mm length, 05118004001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_1_8_mm", "series": "2035", "part_number": "05118004001", "blade_length": 60, "blade_diameter": 2.0, "handle_length": 97})
            details.append(detail)
            #2.5 05117997001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_2_5_mm", "series": "2035", "part_number": "05117997001", "blade_length": 40, "blade_diameter": 2.5, "handle_length": 97})
            details.append(detail)
            #2.0 05118005001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_2_0_mm", "series": "2035", "part_number": "05118005001", "blade_length": 40, "blade_diameter": 2.5, "handle_length": 97})
            details.append(detail)
            #2.0 60 mm length, 05118006001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_2_0_mm", "series": "2035", "part_number": "05118006001", "blade_length": 60, "blade_diameter": 2.5, "handle_length": 97})
            details.append(detail)
            #2.5 50 mm length, 05117994001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_2_5_mm", "series": "2035", "part_number": "05117994001", "blade_length": 50, "blade_diameter": 2.5, "handle_length": 97})
            details.append(detail)
            #2.5 80 mm length, 05118008001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_2_5_mm", "series": "2035", "part_number": "05118008001", "blade_length": 80, "blade_diameter": 2.5, "handle_length": 97})
            details.append(detail)
            #3.0 50 mm length, 05117995001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_3_0_mm", "series": "2035", "part_number": "05117995001", "blade_length": 50, "blade_diameter": 3.0, "handle_length": 97})
            details.append(detail)
            #3.0 80 mm length, 05118010001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_3_0_mm", "series": "2035", "part_number": "05118010001", "blade_length": 80, "blade_diameter": 3.0, "handle_length": 97})
            details.append(detail)
            #3.5 80 mm length, 05118012001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_3_5_mm", "series": "2035", "part_number": "05118012001", "blade_length": 80, "blade_diameter": 4.0, "handle_length": 97})
            details.append(detail)
            #4.0 80 mm length, 05118014001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "slotted_head_4_0_mm", "series": "2035", "part_number": "05118014001", "blade_length": 80, "blade_diameter": 4.0, "handle_length": 97})
            details.append(detail)

            #2067 series torx head
            # 05118035001	TX 1	40	97	2.0	1 9/16"	
            # 05118036001	TX 2	40	97	2.0	1 9/16"	
            # 05118037001	TX 3	40	97	2.0	1 9/16"	
            # 05118039001	TX 4	40	97	2.5	1 9/16"	
            # 05118040001	TX 5	40	97	3.0	1 9/16"	
            # 05118042001	TX 6	40	97	3.0	1 9/16"

            detail_default_current = {}
            detail_default_current["link_distributor_wera"] = "https://products.wera.de/en/screwdrivers_series_kraftform_micro_2067_torx.html"            
            #TX 1, 05118035001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "torx_head_1", "series": "2067", "part_number": "05118035001", "blade_length": 40, "blade_diameter": 2.0, "handle_length": 97})
            details.append(detail)
            #TX 2, 05118036001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "torx_head_2", "series": "2067", "part_number": "05118036001", "blade_length": 40, "blade_diameter": 2.0, "handle_length": 97})
            details.append(detail)
            #TX 3, 05118037001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "torx_head_3", "series": "2067", "part_number": "05118037001", "blade_length": 40, "blade_diameter": 2.0, "handle_length": 97})
            details.append(detail)
            #TX 4, 05118039001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "torx_head_4", "series": "2067", "part_number": "05118039001", "blade_length": 40, "blade_diameter": 2.5, "handle_length": 97})
            details.append(detail)
            #TX 5, 05118040001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "torx_head_5", "series": "2067", "part_number": "05118040001", "blade_length": 40, "blade_diameter": 3.0, "handle_length": 97})
            details.append(detail)
            #TX 6, 05118042001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "torx_head_6", "series": "2067", "part_number": "05118042001", "blade_length": 40, "blade_diameter": 3.0, "handle_length": 97})
            details.append(detail)

            #2055 series pozidriv head
            # 05118030001	PZ 0	60	97	3.0	2 3/8"	
            # 05118032001	PZ 1	80	97	4.0	3 1/16"

            detail_default_current = {}
            detail_default_current["link_distributor_wera"] = "https://products.wera.de/en/screwdrivers_series_kraftform_micro_2055_pz.html"                        
            #PZ 0, 05118030001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "pozidriv_head_0", "series": "2055", "part_number": "05118030001", "blade_length": 60, "blade_diameter": 3.0, "handle_length": 97})
            details.append(detail)
            #PZ 1, 05118032001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "pozidriv_head_1", "series": "2055", "part_number": "05118032001", "blade_length": 80, "blade_diameter": 4.0, "handle_length": 97})
            details.append(detail)
            #2050 series philips head
            # 05345290001 	PH 000	40	97	1.5/2.5	1 9/16"	
            # 05118019001 	PH 00	40	97	1.8/2.5	1 9/16"	
            # 05118020001 	PH 00	60	97	2.5	2 3/8"	
            # 05118026001 	PH 0	40	97	3.0	1 9/16"	
            # 05118022001 	PH 0	60	97	3.0	2 3/8"	
            # 05118023001	    PH 1	60	97	4.0	2 3/8"	
            # 05118024001     PH 1	80	97	4.0	3 1/8"


            detail_default_current = {}
            detail_default_current["link_distributor_wera"] = "https://products.wera.de/en/screwdrivers_series_kraftform_micro_2050_ph_micro.html"                                    
            #PH 000, 05345290001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "philips_head_000", "series": "2050", "part_number": "05345290001", "blade_length": 40, "blade_diameter": 1.5, "handle_length": 97})
            details.append(detail)
            #PH 00, 05118019001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "philips_head_00", "series": "2050", "part_number": "05118019001", "blade_length": 40, "blade_diameter": 1.8, "handle_length": 97})
            details.append(detail)
            #PH 00, 05118020001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "philips_head_00", "series": "2050", "part_number": "05118020001", "blade_length": 60, "blade_diameter": 2.5, "handle_length": 97})
            details.append(detail)
            #PH 0, 05118026001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "philips_head_0", "series": "2050", "part_number": "05118026001", "blade_length": 40, "blade_diameter": 3.0, "handle_length": 97})
            details.append(detail)
            #PH 0, 05118022001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "philips_head_0", "series": "2050", "part_number": "05118022001", "blade_length": 60, "blade_diameter": 3.0, "handle_length": 97})
            details.append(detail)
            #PH 1, 05118023001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "philips_head_1", "series": "2050", "part_number": "05118023001", "blade_length": 60, "blade_diameter": 4.0, "handle_length": 97})
            details.append(detail)
            #PH 1, 05118024001
            detail = copy.deepcopy(detail_default_current)
            detail.update({"head": "philips_head_1", "series": "2050", "part_number": "05118024001", "blade_length": 80, "blade_diameter": 4.0, "handle_length": 97})
            details.append(detail)

            for detail in details:
                part_details = copy.deepcopy(default_wera_precision)
                blade_length = detail["blade_length"]
                dep = 97 + blade_length
                part_details["size"] = f"kraftform_micro_style_18_mm_diameter_{dep}_mm_depth"                
                part_details["description_main"] = f"{detail['head']}"
                part_details["part_number"] = f"{detail['series']}_series_{detail['part_number']}"
                parts.append(part_details)





            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

        #precision_powered
        if True:
            part_details = {}
            part_details["classification"] = "tool"
            part_details["type"] = "screwdriver_precision_powered"
            part_details["size"] = "17_mm_diameter_160_mm_depth"
            part_details["color"] = ""
            part_details["description_main"] = ""
            part_details["description_extra"] = ""
            part_details["manufacturer"] = "xiaomi"
            part_details["part_number"] = ""

            default_current = copy.deepcopy(part_details)

            part_details = copy.deepcopy(default_current)
            part_details["diameter"] = 17
            part_details["depth"] = 160
            parts.append(part_details)

            part_details = copy.deepcopy(default_current)
            part_details["description_main"] = "set"
            part_details["width"] = 75
            part_details["height"] = 202
            part_details["depth"] = 26
            
            parts.append(part_details)
            
        

    # screwdriver bits
    #define a part 
    if True:      

        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "screwdriver_bit"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        
        default_screwdriver_bit = copy.deepcopy(part_details)

        #100 mm depth
        if True:
            part_details = copy.deepcopy(default_screwdriver_bit)
            part_details["size"] = "quarter_inch_drive_100_mm_depth"
            default_current = copy.deepcopy(part_details)

            #hex_head
            description_extras = ["2_mm","2_5_mm","3_mm","4_mm","5_mm","6_mm","8_mm"]
            for description_extra in description_extras:
                part_details = copy.deepcopy(default_current)
                part_details["description_main"] = "hex_head"
                part_details["description_extra"] = description_extra
                part_details["part_number_distributor_aliexpress"] = "1005007111223127"
                part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['part_number_distributor_aliexpress']}.html"
                parts.append(part_details)

            #phillips
            description_extras = ["ph0_2_mm","ph0_3_mm","ph1_2_5_mm","ph1_3_5_mm","ph1_4_mm","ph1_4_5_mm","ph1_5_mm","ph2_4_mm","ph2_4_5_mm","ph2_5_mm","ph2_6_mm"]
            for description_extra in description_extras:
                part_details = copy.deepcopy(default_current)
                part_details["description_main"] = "phillips_head"
                part_details["description_extra"] = description_extra
                part_details["part_number_distributor_aliexpress"] = "1005002383044569"
                part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['part_number_distributor_aliexpress']}.html"
                parts.append(part_details)

            #slot
            description_extras = ["1_6_mm","2_mm","2_5_mm","3_mm","4_mm","5_mm","6_mm"]
            for description_extra in description_extras:
                part_details = copy.deepcopy(default_current)
                part_details["description_main"] = "slot_head"
                part_details["description_extra"] = description_extra
                part_details["part_number_distributor_aliexpress"] = "1005002307522502"
                part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['part_number_distributor_aliexpress']}.html"
                parts.append(part_details)

        #150 mm depth
        if True:
            part_details = copy.deepcopy(default_screwdriver_bit)
            part_details["size"] = "quarter_inch_drive_150_mm_depth"
            default_current = copy.deepcopy(part_details)

            #hex_head
            description_extras = ["1_5_mm","2_mm", "2_5_mm","3_mm","4_mm","5_mm","6_mm"]
            for description_extra in description_extras:
                part_details = copy.deepcopy(default_current)
                part_details["description_main"] = "hex_head"
                part_details["description_extra"] = description_extra
                part_details["part_number_distributor_aliexpress"] = "1005006923093945"
                part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['part_number_distributor_aliexpress']}.html"
                parts.append(part_details)
            

    #syringe
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "syringe"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        
        default_syringe = copy.deepcopy(part_details)

        description_mains = ["1_ml", "3_ml", "5_ml", "10_ml", "20_ml", "50_ml", "60_ml", "100_ml", "250_ml", "500_ml"]
        description_extras = []
        description_extras.append("")
        description_extras.append("flat_top_style")
        description_extras.append("ring_top_style")
        for description_main in description_mains:
            for description_extra in description_extras:
                part_details = copy.deepcopy(default_syringe)
                part_details["description_main"] = description_main
                part_details["description_extra"] = description_extra
                parts.append(part_details)

    # tape measure
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "measure_tape_measure"
        part_details["size"] = "5000_mm_length"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "stanley"
        part_details["part_number"] = "1_30_696"
        part_details["part_number_exact"] = "1-30-696"
        part_details["part_number_distributor_amazon"] = "B000Y8W54C"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/gp/product/{part_details['part_number_distributor_amazon']}"
        part_details["oobb_tool_holder_shape"] = "cube"
        part_details["oobb_tool_holder_width"] = 78
        part_details["oobb_tool_holder_height"] = 74
        part_details["oobb_tool_holder_depth"] = 42

        parts.append(part_details)

        
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "measure_tape_measure"
        part_details["size"] = "3000_mm_length"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "stanley"
        part_details["part_number"] = "0_30_686"
        part_details["part_number_exact"] = "0-30-686"
        part_details["part_number_distributor_amazon"] = "B0009VX1ZQ"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/gp/product/{part_details['part_number_distributor_amazon']}"
        part_details["oobb_tool_holder_shape"] = "cube"
        part_details["oobb_tool_holder_width"] = 65
        part_details["oobb_tool_holder_height"] = 60
        part_details["oobb_tool_holder_depth"] = 30 
        
        parts.append(part_details)


    # tool box

    # timer
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "timer"
        part_details["size"] = [""]
        part_details["color"] = [""]
        part_details["description_main"] = ["80_mm_diameter_30_mm_depth_black"]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["part_number_distributor_amazon"] = "B07VNWZCZH"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/gp/product/{part_details['part_number_distributor_amazon']}"
        parts.append(part_details)

    # vibratory_bowl
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "vibratory_bowl"
        part_details["size"] = ["tabletop"]
        part_details["color"] = [""]
        part_details["description_main"] = [""]
        part_details["description_extra"] = [""]
        part_details["manufacturer"] = "mettler_toledo"
        part_details["part_number"] = "lv11"
        parts.append(part_details)

    
    #garden tools
    if True:
        part_details = {}
        part_details["classification"] = "tool"
        part_details["type"] = "garden_tool"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        
        default_current = copy.deepcopy(part_details)

        #secaturs fiskar p91
        part_details = copy.deepcopy(default_current)
        part_details["description_main"] = "secateurs_anvil"
        part_details["manufacturer"] = "fiskars"
        part_details["part_number"] = "p91"
        parts.append(part_details)
        
    
    

    
    oomp.add_parts(parts, **kwargs)
    