import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    

    parts = []

    part_details = {}
    part_details["classification"] = "decorating"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = copy.deepcopy(part_details)

    #picture_frame
    if True:
        part_details = copy.deepcopy(default_empty)        
        part_details["type"] = "picture_frame"
            
        default_current = part_details

        detail_default_current = {}

        #series
        details = [] 
        #fiskbo
        if True:
            #white
            #100 x 150
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "ikea_fiskbo", "description_main":"100_mm_width_150_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": "002.956.53"})
            details.append(detail)
            #130 x 180
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "ikea_fiskbo", "description_main":"130_mm_width_180_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": "902.956.63"})
            details.append(detail)
            #210 x 300
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "ikea_fiskbo", "description_main":"210_mm_width_300_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": "803.003.73"})
            details.append(detail)
            #300 x 400
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "ikea_fiskbo", "description_main":"300_mm_width_400_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": "103.003.95"})
            details.append(detail)
            #400 x 500
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "ikea_fiskbo", "description_main":"400_mm_width_500_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": "003.003.86"})
            details.append(detail)
            #500 x 700 white
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "ikea_fiskbo", "description_main":"500_mm_width_700_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": "603.003.74"})
            details.append(detail)            
        #knoppang
        if True:
            #white
            #130 x 180
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "ikea_knopppang", "description_main":"130_mm_width_180_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": "103.871.24"})
            details.append(detail)
            #210 x 300
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "ikea_knopppang", "description_main":"210_mm_width_300_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": "503.871.22"})
            details.append(detail)
            #230 x 230
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "ikea_knopppang", "description_main":"230_mm_width_230_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": ""})
            details.append(detail)
            #300 x 400
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "ikea_knopppang", "description_main":"300_mm_width_400_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": "903.871.20"})
            details.append(detail)
            #400 x 500
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size":
             "ikea_knopppang", "description_main":"400_mm_width_500_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": "503.871.36"})
            details.append(detail)
            #500 x 700 white
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "ikea_knopppang", "description_main":"500_mm_width_700_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": "703.871.40"})
            details.append(detail)
            #610 x 910 white
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "ikea_knopppang", "description_main":"610_mm_width_910_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": "104.296.52"})
            details.append(detail)

        #ribba
        if True:
            #300 x 400
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "ikea_ribba", "description_main":"300_mm_width_400_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": ""})
            details.append(detail)
            #400 x 500
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "ikea_ribba", "description_main":"400_mm_width_500_mm_height","description_extra": "white", "manufacturer": "ikea", "part_number_exact": ""})
            details.append(detail)

        for detail in details:
            part_details = copy.deepcopy(default_current)
            part_details.update(detail)
            part_number_exact = part_details.get("part_number_exact", "")
            if part_number_exact != "":
                part_number = part_number_exact.replace(".", "_")        
                part_details["part_number"] = part_number
                link_distributor_ikea = f"https://www.ikea.com/gb/en/search/?q={part_number_exact}"
                part_details["link_distributor_ikea"] = link_distributor_ikea
            else:
                part_details.pop("part_number_exact", None)
            parts.append(part_details)

    oomp.add_parts(parts, make_files=make_files)
    