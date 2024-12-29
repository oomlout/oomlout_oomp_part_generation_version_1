import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    

    #define a part 

       
    #escs
    if True:
        part_details = {}
        part_details["classification"] = "remote_control"
        part_details["type"] = "electronic_speed_controller"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = "1_amp_12_mm_width_8_5_mm_height_green_pcb"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = ""        
        part_details["part_number_distributor_aliexpress"] = "1005006080168104"
        part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details["part_number_distributor_aliexpress"]}.html"
        part_details["short_name"] = "ESC 1 amp"  


        description_extras = ["","wire_attached"]

        for description_extra in description_extras:
            part_details = copy.deepcopy(part_details)
            part_details["description_extra"] = description_extra
            parts.append(part_details)

        
    
    #transmitter kit
    if True:
        kits = []
        
        part_details = {}
        part_details["classification"] = "remote_control"
        part_details["type"] = "transmitter_receiver_kit"
        part_details["size"] = "2_4_ghz_4_channel"
        part_details["color"] = "car_style_grip_black"
        part_details["description_main"] = "kit_retail_packaging"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""   
        current_default = copy.deepcopy(part_details)

        #aliexpress 1
        part_details = copy.deepcopy(current_default)
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = "ga_4h_tx"   
        part_details["part_number_exact"] = "GA-4H-TX"   
        part_details["part_number_distributor_aliexpress"] = "1005005061265278"
        part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details["part_number_distributor_aliexpress"]}.html"
        part_details["part_number_distributor_amazon"] = "B0D8686DBH"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details["part_number_distributor_amazon"]}"
        part_details["short_name"] = "Transmitter Kit 4 Channel"  
        parts.append(part_details)
        kits.append(copy.deepcopy(part_details))

        #aliexpress 2
        part_details = copy.deepcopy(current_default)
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = "ds_4a"
        part_details["part_number_exact"] = "DS-4A"
        part_details["part_number_distributor_aliexpress"] = "1005006041694540"
        part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['part_number_distributor_aliexpress']}.html"
        part_details["part_number_distributor_amazon"] = "B0CH8G9NJ5"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['part_number_distributor_amazon']}"
        part_details["short_name"] = "Transmitter Kit 4 Channel"
        parts.append(part_details)
        kits.append(copy.deepcopy(part_details))

        #aliexpress 3
        part_details = copy.deepcopy(current_default)
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = "91803g_vt"
        part_details["part_number_exact"] = "91803G-VT"
        part_details["part_number_distributor_aliexpress"] = "32985435030"
        part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['part_number_distributor_aliexpress']}.html"
        part_details["part_number_distributor_amazon"] = "B08MQ4GK2B"
        part_details["link_distributor_amazon"] = f"https://www.amazon.co.uk/dp/{part_details['part_number_distributor_amazon']}"
        part_details["short_name"] = "Transmitter Kit 4 Channel"
        parts.append(part_details)
        kits.append(copy.deepcopy(part_details))

        #hobbyking
        part_details = copy.deepcopy(current_default)
        part_details["size"] = "2_4_ghz_6_channel"
        part_details["manufacturer"] = "turnigy"
        part_details["part_number"] = "t6a_v2"
        part_details["part_number_exact"] = "T6A-V2"
        part_details["part_number_distributor_hobbyking"] = "T6A-V2"
        part_details["link_distributor_hobbyking"] = f"https://hobbyking.com/en_us/turnigy-t6a-v2-afhds-mode-2-2-4ghz-6ch-transmitter-w-receiver.html"
        part_details["short_name"] = "Transmitter Kit 6 Channel"
        parts.append(part_details)
        kits.append(copy.deepcopy(part_details))
        
        for kit in kits:
            current_default = copy.deepcopy(kit)
            #receiver
            part_details = copy.deepcopy(current_default)
            part_details["description_main"] = "receiver_full"
            parts.append(part_details)

            #receiver_pcb
            part_details = copy.deepcopy(current_default)
            part_details["description_main"] = "receiver_pcb"
            parts.append(part_details)

            #transmitter_full
            part_details = copy.deepcopy(current_default)
            part_details["description_main"] = "transmitter_full"
            parts.append(part_details)

            #transmitter_pcb
            part_details = copy.deepcopy(current_default)
            part_details["description_main"] = "transmitter_pcb"
            parts.append(part_details)


        

    oomp.add_parts(parts, make_files=make_files)
    