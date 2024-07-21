import oomp

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    # dell monitors
    part_details = {}
    part_details["classification"] = "computer"
    part_details["type"] = "monitor"
    part_details["size"] = ["508_mm_screen_diagonal"]
    part_details["color"] = [""]
    part_details["description_main"] = "1680_pixel_width_1050_pixel_height"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "dell"
    part_details["part_number"] = "e2009wt"
    part_details["width"] = "470 mm"
    part_details["height"] = "308 mm"
    part_details["depth"] = "65 mm"
    parts.append(part_details)

    
    part_details = {}
    part_details["classification"] = "computer"
    part_details["type"] = "monitor"
    part_details["size"] = ["558_8_mm_screen_diagonal"]
    part_details["color"] = [""]
    part_details["description_main"] = "1920_pixel_width_1080_pixel_height"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "dell"
    part_details["part_number"] = "e2211hb"
    part_details["width"] = "513 mm"
    part_details["height"] = "305 mm"
    part_details["depth"] = "60 mm"
    parts.append(part_details)

    # vesa mounts
    part_details = {}
    part_details["classification"] = "computer"
    part_details["type"] = "monitor_mount"
    part_details["size"] = ["vesa"]
    part_details["color"] = [""]
    part_details["description_main"] = "100_mm_width_100_mm_height"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    parts.append(part_details)



    
    oomp.add_parts(parts, **kwargs)
    