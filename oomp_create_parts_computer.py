import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "computer"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = part_details.copy()

    # video conferencing
    if True:
        #webex
        if True:
            #spark board 55
            part_details = copy.deepcopy(default_empty)
            part_details["type"] = "video_conferencing"
            part_details["size"] = "screen"
            part_details["color"] = ""
            part_details["description_main"] = "spark_board_55"
            part_details["description_extra"] = "1240_mm_width_830_mm_height_105_mm_depth"
            part_details["manufacturer"] = "cisco"
            part_details["part_number_exact"] = "SPARK-BOARD55-K9"
            part_details["part_number"] = part_details["part_number_exact"].lower().replace("-", "_")
            part_details["link_distributor_cisco"] = "https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-board/series.html"
            parts.append(part_details)

            
            #room 55
            part_details = copy.deepcopy(default_empty)
            part_details["type"] = "video_conferencing"
            part_details["size"] = "screen"
            part_details["color"] = ""
            part_details["description_main"] = "room_55"
            part_details["description_extra"] = "1240_mm_width_830_mm_height_105_mm_depth"
            part_details["manufacturer"] = "cisco"
            part_details["part_number_exact"] = "CS-ROOM55-K9"
            part_details["part_number"] = part_details["part_number_exact"].lower().replace("-", "_")
            part_details["link_distributor_cisco"] = "https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-55/model.html"
            parts.append(part_details)

            #room 55 stand
            part_details = copy.deepcopy(default_empty)
            part_details["type"] = "video_conferencing"
            part_details["size"] = "screen"
            part_details["color"] = ""
            part_details["description_main"] = "room_55_floor_stand"
            part_details["description_extra"] = ""
            part_details["manufacturer"] = "cisco"
            part_details["part_number"] = "CS-ROOM55-FSK="
            part_details["part_number"] = part_details["part_number"].lower().replace("-", "_").replace("=", "")
            part_details["link_distributor_cisco"] = "https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-55/model.html"
            parts.append(part_details)

            #room 55 wall mount
            part_details = copy.deepcopy(default_empty)
            part_details["type"] = "video_conferencing"
            part_details["size"] = "screen"
            part_details["color"] = ""
            part_details["description_main"] = "room_55_wall_mount"
            part_details["description_extra"] = ""
            part_details["manufacturer"] = "cisco"
            part_details["part_number"] = "CS-ROOM55-WMK="
            part_details["part_number"] = part_details["part_number"].lower().replace("-", "_").replace("=", "")
            part_details["link_distributor_cisco"] = "https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-55/model.html"
            parts.append(part_details)

            #room kit
            part_details = copy.deepcopy(default_empty)
            part_details["type"] = "video_conferencing"
            part_details["size"] = "camera_and_speaker"
            part_details["color"] = ""
            part_details["description_main"] = "room_kit"
            part_details["description_extra"] = "700_mm_width_105_mm_height_90_mm_depth"
            part_details["manufacturer"] = "cisco"
            part_details["part_number_exact"] = "CS-KIT-K9"
            part_details["part_number"] = part_details["part_number_exact"].lower().replace("-", "_")
            part_details["link_distributor_cisco"] = "https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit/model.html"
            parts.append(part_details)

            #quad_camera
            part_details = copy.deepcopy(default_empty)
            part_details["type"] = "video_conferencing"
            part_details["size"] = "camera_and_speaker"
            part_details["color"] = ""
            part_details["description_main"] = "quad_camera"
            part_details["description_extra"] = "950_mm_width_120_mm_height_103_mm_depth"
            part_details["manufacturer"] = "cisco"
            part_details["part_number_exact"] = "TTC8-10"
            part_details["part_number"] = part_details["part_number_exact"].lower().replace("-", "_")
            part_details["link_distributor_cisco"] = "https://www.webex.com/us/en/devices/cameras/cisco-quad-camera.html"
            parts.append(part_details)

            #sx10 
            part_details = copy.deepcopy(default_empty)
            part_details["type"] = "video_conferencing"
            part_details["size"] = "camera"
            part_details["color"] = ""
            part_details["description_main"] = "sx10"
            part_details["description_extra"] = ""
            part_details["manufacturer"] = "cisco"
            part_details["part_number_exact"] = "TTC7-22"
            part_details["part_number"] = part_details["part_number_exact"].lower().replace("-", "_")
            part_details["link_distributor_cisco"] = "https://www.cisco.com/c/en/us/support/collaboration-endpoints/telepresence-sx10-quick-set/model.html"
            parts.append(part_details)

            #dx80
            part_details = copy.deepcopy(default_empty)
            part_details["type"] = "video_conferencing"
            part_details["size"] = "screen"
            part_details["color"] = ""
            part_details["description_main"] = "dx80"
            part_details["description_extra"] = "512_mm_width_565_mm_height_89_mm_depth"
            part_details["manufacturer"] = "cisco"
            part_details["part_number"] = ""
            parts.append(part_details)

        #jam board
        if True:
            part_details = copy.deepcopy(default_empty)
            part_details["type"] = "video_conferencing"
            part_details["size"] = "screen"
            part_details["color"] = ""
            part_details["description_main"] = "jamboard"
            part_details["description_extra"] = "1352_mm_width_823_mm_height_88_mm_depth"
            part_details["manufacturer"] = "google"
            part_details["part_number"] = ""
            parts.append(part_details)

            #stand
            part_details = copy.deepcopy(default_empty)
            part_details["type"] = "video_conferencing"
            part_details["size"] = "stand"
            part_details["color"] = ""
            part_details["description_main"] = "jamboard_stand"
            part_details["description_extra"] = "1330_mm_width_1422_mm_height_962_mm_depth"
            part_details["manufacturer"] = "google"
            part_details["part_number"] = ""
            parts.append(part_details)

            #wall_mount
            part_details = copy.deepcopy(default_empty)
            part_details["type"] = "video_conferencing"
            part_details["size"] = "wall_mount"
            part_details["color"] = ""
            part_details["description_main"] = "jamboard_wall_mount"            
            part_details["manufacturer"] = "google"            
            part_details["part_number"] = ""
            parts.append(part_details)


    # webcams

    # amazon fire tablets
    if True:
        part_details = {}
        part_details["classification"] = "computer"
        part_details["type"] = "tablet"
        part_details["size"] = ["amazon_fire"]
        part_details["color"] = [""]
        part_details["description_main"] = "max_11"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "amazon"
        part_details["part_number"] = "kfsnwi"
        part_details["width"] = "259.1 mm"
        part_details["height"] = "163.7 mm"
        part_details["depth"] = "7.5 mm"
        parts.append(part_details)


    # surface pros
    if True:
        #define a part 
        part_details = {}
        part_details["classification"] = "computer"
        part_details["type"] = "tablet"
        part_details["size"] = ["microsoft_surface"]
        part_details["color"] = [""]
        part_details["description_main"] = "pro_3"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "microsoft"
        part_details["part_number"] = "1631"
        parts.append(part_details)

        #define a part 
        part_details = {}
        part_details["classification"] = "computer"
        part_details["type"] = "tablet"
        part_details["size"] = ["microsoft_surface"]
        part_details["color"] = [""]
        part_details["description_main"] = "pro_3"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "microsoft"
        part_details["part_number"] = "model_1631"
        parts.append(part_details)

        
        part_details = {}
        part_details["classification"] = "computer"
        part_details["type"] = "tablet"
        part_details["size"] = ["microsoft_surface"]
        part_details["color"] = [""]
        part_details["description_main"] = "pro_4"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "microsoft"
        part_details["part_number"] = "model_1724"
        parts.append(part_details)

        
        part_details = {}
        part_details["classification"] = "computer"
        part_details["type"] = "tablet"
        part_details["size"] = ["microsoft_surface"]
        part_details["color"] = [""]
        part_details["description_main"] = "pro_5"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "microsoft"
        part_details["part_number"] = "model_1796"
        parts.append(part_details)

        
        part_details = {}
        part_details["classification"] = "computer"
        part_details["type"] = "tablet"
        part_details["size"] = ["microsoft_surface"]
        part_details["color"] = [""]
        part_details["description_main"] = "pro_7"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "microsoft"
        part_details["part_number"] = "model_1866"
        parts.append(part_details)

        #define a part 
        part_details = {}
        part_details["classification"] = "computer"
        part_details["type"] = "docking_station"
        part_details["size"] = ["microsoft_surface"]
        part_details["color"] = [""]
        part_details["description_main"] = [""]
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "microsoft"
        part_details["part_number"] = "1661"
        parts.append(part_details)
        
        #define a part 
        part_details = {}
        part_details["classification"] = "computer"
        part_details["type"] = "power_supply"
        part_details["size"] = ["microsoft_surface"]
        part_details["color"] = [""]
        part_details["description_main"] = ["docking_station"]
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "microsoft"
        part_details["part_number"] = "model_1749"
        parts.append(part_details)
        
        part_details = {}
        part_details["classification"] = "computer"
        part_details["type"] = "power_supply"
        part_details["size"] = ["microsoft_surface"]
        part_details["color"] = [""]
        part_details["description_main"] = ["standalone"]
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "microsoft"
        part_details["part_number"] = "model_1625"
        parts.append(part_details)

        

    #webcams
    if True:
        part_details = {}
        part_details["classification"] = "computer"
        part_details["type"] = "webcam"
        part_details["size"] = ["external"]
        part_details["color"] = [""]
        part_details["description_main"] = [""]
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "microsoft"
        part_details["part_number"] = "hd_3000_model_1492"
        parts.append(part_details)

        part_details = {}
        part_details["classification"] = "computer"
        part_details["type"] = "webcam"
        part_details["size"] = "external"
        part_details["color"] = ""
        part_details["description_main"] = "telepresence_precisionhd_usb_camera"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "cisco"
        part_details["part_number_exact"] = "TTC8-03"
        part_details["part_number"] = part_details["part_number_exact"].lower().replace("-", "_")
        part_details["link_distributor_cisco"] = ""
        parts.append(part_details)


        

    
    oomp.add_parts(parts, **kwargs)
    