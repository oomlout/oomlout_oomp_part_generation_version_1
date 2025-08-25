import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "wire_cable"
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = part_details.copy()

    
    #activty
    if True:
        current_item = {"size": "adapter"}
        colors = []
        #screw terminal
        if True:
            colors.append("adapter_screw_terminal")
            colors.append("extender")
            description_mains = []
            #type_a
            description_mains.append("to_usb_type_a_plug")
            description_mains.append("to_usb_type_a_socket")
            #type_b
            description_mains.append("to_usb_type_b_plug")
            description_mains.append("to_usb_type_b_socket")
            #type_b_micro
            description_mains.append("to_usb_type_b_micro_plug")
            description_mains.append("to_usb_type_b_micro_socket")
            #type_b_mini
            description_mains.append("to_usb_type_b_mini_plug")
            description_mains.append("to_usb_type_b_mini_socket")
            #type_c        
            description_mains.append("to_usb_type_c_plug")
            description_mains.append("to_usb_type_c_socket")
            #rj45
            description_mains.append("to_rj45_ethernet_plug")
            description_mains.append("to_rj45_ethernet_socket")        
            #3.5mm audio
            description_mains.append("to_3.5mm_audio_4_pole_socket")
            description_mains.append("to_3.5mm_audio_4_pole_plug")
            #rca
            description_mains.append("to_rca_socket")
            description_mains.append("to_rca_plug")
            #db9 serial
            description_mains.append("to_db9_serial_socket")
            description_mains.append("to_db9_serial_plug")
            #hdmi
            description_mains.append("to_hdmi_plug")
            description_mains.append("to_hdmi_socket")
            for color in colors:
                for description_main in description_mains:
                    part_details = copy.deepcopy(default_empty)
                    part_details.update(current_item)
                    part_details["color"] = color
                    part_details["description_main"] = description_main                
                    parts.append(part_details)


    oomp.add_parts(parts, **kwargs)
    