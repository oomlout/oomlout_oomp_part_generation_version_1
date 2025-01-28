import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

        
    #google_pixel
    if True:
        part_details = {}
        part_details["classification"] = "phone"
        part_details["type"] = "android"
        part_details["size"] = "google_pixel"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = "" 
        
        default_google_pixel =  copy.deepcopy(part_details)
        
        
        #pixel 4
        part_details = copy.deepcopy(default_google_pixel)
        part_details["description_main"] = "pixel_4"
        part_details["description_extra"] = "69_mm_width_148_mm_height_9_mm_depth"
        part_details["short_name"] = "Google Pixel 4"
        parts.append(part_details)

        #pixel 5
        part_details = copy.deepcopy(default_google_pixel)
        part_details["description_main"] = "pixel_5"
        part_details["description_extra"] = "71_mm_width_145_mm_height_8_mm_depth"
        part_details["short_name"] = "Google Pixel 5"
        parts.append(part_details)

        #pixel 6
        part_details = copy.deepcopy(default_google_pixel)
        part_details["description_main"] = "pixel_6"
        part_details["description_extra"] = "75_mm_width_159_mm_height_9_mm_depth"
        part_details["short_name"] = "Google Pixel 6"
        parts.append(part_details)

        #pixel 7
        part_details = copy.deepcopy(default_google_pixel)
        part_details["description_main"] = "pixel_7"
        part_details["description_extra"] = "74_mm_width_156_mm_height_9_mm_depth"
        part_details["short_name"] = "Google Pixel 7" 
        parts.append(part_details)  


            

            
        
            

    oomp.add_parts(parts, make_files=make_files)
    