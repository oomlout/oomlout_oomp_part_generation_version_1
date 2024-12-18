import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []
   

    # mcu
    #      atmega328p
    #             pro_mini
    if True:
        part_details = {}
        part_details["description"] = "A mini usb port free arduino compatible breakout" 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board_mcu"
        part_details["size"] = "pro_mini"
        part_details["color"] = ""
        part_details["description_main"] = "atmega328p_arduino_compatible"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        pins = {}
        pins["pin_1"] = ({"name": "tx1", "number": "1", "type": "signal"})
        pins["pin_2"] = ({"name": "rx0", "number": "2", "type": "signal"})
        pins["pin_3"] = ({"name": "rst", "number": "3", "type": "signal"})
        pins["pin_4"] = ({"name": "gnd", "number": "4", "type": "power"})
        pins["pin_5"] = ({"name": "d2", "number": "5", "type": "signal"})
        pins["pin_6"] = ({"name": "d3", "number": "6", "type": "signal"})
        pins["pin_7"] = ({"name": "d4", "number": "7", "type": "signal"})
        pins["pin_8"] = ({"name": "d5", "number": "8", "type": "signal"})
        pins["pin_9"] = ({"name": "d6", "number": "9", "type": "signal"})
        pins["pin_10"] = ({"name": "d7", "number": "10", "type": "signal"})
        pins["pin_11"] = ({"name": "d8", "number": "11", "type": "signal"})
        pins["pin_12"] = ({"name": "d9", "number": "12", "type": "signal"})
        pins["pin_13"] = ({"name": "d10", "number": "13", "type": "signal"})
        pins["pin_14"] = ({"name": "d11", "number": "14", "type": "signal"})
        pins["pin_15"] = ({"name": "d12", "number": "15", "type": "signal"})
        pins["pin_16"] = ({"name": "d13", "number": "16", "type": "signal"})
        pins["pin_17"] = ({"name": "a0", "number": "17", "type": "power"})
        pins["pin_18"] = ({"name": "a1", "number": "18", "type": "signal"})
        pins["pin_19"] = ({"name": "a2", "number": "19", "type": "signal"})
        pins["pin_20"] = ({"name": "a3", "number": "20", "type": "signal"})
        pins["pin_21"] = ({"name": "vcc", "number": "21", "type": "signal"})
        pins["pin_22"] = ({"name": "rst", "number": "22", "type": "signal"})
        pins["pin_23"] = ({"name": "gnd", "number": "23", "type": "signal"})
        pins["pin_24"] = ({"name": "vin", "number": "24", "type": "signal"})
        pins["pin_25"] = ({"name": "a6", "number": "25", "type": "signal"})
        pins["pin_26"] = ({"name": "a7", "number": "26", "type": "signal"})
        pins["pin_27"] = ({"name": "a4", "number": "27", "type": "power"})
        pins["pin_28"] = ({"name": "a5", "number": "28", "type": "signal"})
        pins["pin_29"] = ({"name": "black", "number": "29", "type": "gnd"})
        pins["pin_30"] = ({"name": "gnd", "number": "30", "type": "power"})
        pins["pin_31"] = ({"name": "vcc", "number": "30", "type": "power"})
        pins["pin_32"] = ({"name": "rx0", "number": "30", "type": "power"})
        pins["pin_33"] = ({"name": "tx1", "number": "30", "type": "power"})
        pins["pin_34"] = ({"name": "green", "number": "30", "type": "power"})
        
        part_details["pins"] = pins
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)

    #            shennie
    if True:
        part_details = {}
        part_details["description"] = "A popular arduino compatible atmega328 board from aliexpress" 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board_mcu"
        part_details["size"] = ["shennie"]
        part_details["color"] = [""]
        part_details["description_main"] = "atmega328p_arduino_compatible"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        pins = {}
        pins["pin_1"] = ({"name": "tx1", "number": "1", "type": "signal"})
        pins["pin_2"] = ({"name": "rx0", "number": "2", "type": "signal"})
        pins["pin_3"] = ({"name": "rst", "number": "3", "type": "signal"})
        pins["pin_4"] = ({"name": "gnd", "number": "4", "type": "power"})
        pins["pin_5"] = ({"name": "d2", "number": "5", "type": "signal"})
        pins["pin_6"] = ({"name": "d3", "number": "6", "type": "signal"})
        pins["pin_7"] = ({"name": "d4", "number": "7", "type": "signal"})
        pins["pin_8"] = ({"name": "d5", "number": "8", "type": "signal"})
        pins["pin_9"] = ({"name": "d6", "number": "9", "type": "signal"})
        pins["pin_10"] = ({"name": "d7", "number": "10", "type": "signal"})
        pins["pin_11"] = ({"name": "d8", "number": "11", "type": "signal"})
        pins["pin_12"] = ({"name": "d9", "number": "12", "type": "signal"})
        pins["pin_13"] = ({"name": "d10", "number": "13", "type": "signal"})
        pins["pin_14"] = ({"name": "d11", "number": "14", "type": "signal"})
        pins["pin_15"] = ({"name": "d12", "number": "15", "type": "signal"})
        pins["pin_16"] = ({"name": "d13", "number": "16", "type": "signal"})
        pins["pin_17"] = ({"name": "3v3", "number": "17", "type": "power"})
        pins["pin_18"] = ({"name": "ref", "number": "18", "type": "signal"})
        pins["pin_19"] = ({"name": "a0", "number": "19", "type": "signal"})
        pins["pin_20"] = ({"name": "a1", "number": "20", "type": "signal"})
        pins["pin_21"] = ({"name": "a2", "number": "21", "type": "signal"})
        pins["pin_22"] = ({"name": "a3", "number": "22", "type": "signal"})
        pins["pin_23"] = ({"name": "a4", "number": "23", "type": "signal"})
        pins["pin_24"] = ({"name": "a5", "number": "24", "type": "signal"})
        pins["pin_25"] = ({"name": "a6", "number": "25", "type": "signal"})
        pins["pin_26"] = ({"name": "a7", "number": "26", "type": "signal"})
        pins["pin_27"] = ({"name": "5v", "number": "27", "type": "power"})
        pins["pin_28"] = ({"name": "rst", "number": "28", "type": "signal"})
        pins["pin_29"] = ({"name": "gnd", "number": "29", "type": "gnd"})
        pins["pin_30"] = ({"name": "vin", "number": "30", "type": "power"})
        part_details["pins"] = pins
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)

        shennie_default = copy.deepcopy(part_details)


        #usb_c version
        part_details = copy.deepcopy(shennie_default)
        part_details["description_extra"] = "usb_c_type"
        parts.append(part_details)

        part_details = copy.deepcopy(shennie_default)
        part_details["description_extra"] = "breakout_screw_terminal_3_5_mm_pitch"
        parts.append(part_details)

        part_details = copy.deepcopy(shennie_default)
        part_details["description_extra"] = "breakout_arduino_uno_short_footprint"
        parts.append(part_details)
        
        part_details = copy.deepcopy(shennie_default)
        part_details["description_extra"] = "breakout_cnc_shield"
        parts.append(part_details)

    #           uno
    if True:
        part_details = {}
        part_details["description"] = "An arduino compatible breakout in the Arduino Uno short size format, pfavoured by aliexpress vendors sometimes" 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board_mcu"
        part_details["size"] = "uno_short"
        part_details["color"] = ""
        part_details["description_main"] = "atmega328p_arduino_compatible"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        pins = {}
        pins["pin_1"] = ({"name": "reset", "number": "1", "type": "signal"})
        pins["pin_2"] = ({"name": "3v3", "number": "2", "type": "signal"})
        pins["pin_3"] = ({"name": "5v", "number": "3", "type": "signal"})
        pins["pin_4"] = ({"name": "gnd", "number": "4", "type": "power"})
        pins["pin_5"] = ({"name": "gnd", "number": "5", "type": "signal"})
        pins["pin_6"] = ({"name": "vin", "number": "6", "type": "signal"})
        pins["pin_7"] = ({"name": "a0", "number": "7", "type": "signal"})
        pins["pin_8"] = ({"name": "a1", "number": "8", "type": "signal"})
        pins["pin_9"] = ({"name": "a2", "number": "9", "type": "signal"})
        pins["pin_10"] = ({"name": "a3", "number": "10", "type": "signal"})
        pins["pin_11"] = ({"name": "a4", "number": "11", "type": "signal"})
        pins["pin_12"] = ({"name": "a5", "number": "12", "type": "signal"})
        pins["pin_13"] = ({"name": "d0_rx", "number": "13", "type": "signal"})
        pins["pin_14"] = ({"name": "d1_tx", "number": "14", "type": "signal"})
        pins["pin_15"] = ({"name": "d2", "number": "15", "type": "signal"})
        pins["pin_16"] = ({"name": "d3", "number": "16", "type": "signal"})
        pins["pin_17"] = ({"name": "d4", "number": "17", "type": "power"})
        pins["pin_18"] = ({"name": "d5", "number": "18", "type": "signal"})
        pins["pin_19"] = ({"name": "d6", "number": "19", "type": "signal"})
        pins["pin_20"] = ({"name": "d7", "number": "20", "type": "signal"})
        pins["pin_21"] = ({"name": "d8", "number": "21", "type": "signal"})
        pins["pin_22"] = ({"name": "d9", "number": "22", "type": "signal"})
        pins["pin_23"] = ({"name": "d10", "number": "23", "type": "signal"})
        pins["pin_24"] = ({"name": "d11", "number": "24", "type": "signal"})
        pins["pin_25"] = ({"name": "d12", "number": "25", "type": "signal"})
        pins["pin_26"] = ({"name": "d13", "number": "26", "type": "signal"})
        pins["pin_27"] = ({"name": "gnd", "number": "27", "type": "power"})
        pins["pin_28"] = ({"name": "aref", "number": "28", "type": "signal"})        
        
        part_details["pins"] = pins
        #used below
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)
        
        #uses uno_short pin naming
        part_details = {}
        part_details["description"] = "An arduino compatible breakout in the Arduino Uno short size format, pfavoured by aliexpress vendors sometimes" 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board_mcu"
        part_details["size"] = "uno_rev_1"
        part_details["color"] = ""
        part_details["description_main"] = "atmega328p_arduino_compatible"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        pins = copy.deepcopy(pins)        
        part_details["pins"] = pins
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)

        part_details = {}
        part_details["description"] = "An arduino compatible breakout in the Arduino Uno size format" 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board_mcu"
        part_details["size"] = "uno_rev_3"
        part_details["color"] = ""
        part_details["description_main"] = "atmega328p_arduino_compatible"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        pins = {}
        pins["pin_1"] = ({"name": "not_connected", "number": "1", "type": "signal"})
        pins["pin_2"] = ({"name": "ioref", "number": "2", "type": "signal"})
        pins["pin_3"] = ({"name": "reset", "number": "3", "type": "signal"})
        pins["pin_4"] = ({"name": "3v3", "number": "4", "type": "signal"})
        pins["pin_5"] = ({"name": "5v", "number": "5", "type": "signal"})
        pins["pin_6"] = ({"name": "gnd", "number": "6", "type": "power"})
        pins["pin_7"] = ({"name": "gnd", "number": "7", "type": "signal"})
        pins["pin_8"] = ({"name": "vin", "number": "8", "type": "signal"})
        pins["pin_9"] = ({"name": "a0", "number": "9", "type": "signal"})
        pins["pin_10"] = ({"name": "a1", "number": "10", "type": "signal"})
        pins["pin_11"] = ({"name": "a2", "number": "11", "type": "signal"})
        pins["pin_12"] = ({"name": "a3", "number": "12", "type": "signal"})
        pins["pin_13"] = ({"name": "a4", "number": "13", "type": "signal"})
        pins["pin_14"] = ({"name": "a5", "number": "14", "type": "signal"})
        pins["pin_15"] = ({"name": "d0_rx", "number": "15", "type": "signal"})
        pins["pin_16"] = ({"name": "d1_tx", "number": "16", "type": "signal"})
        pins["pin_17"] = ({"name": "d2", "number": "17", "type": "signal"})
        pins["pin_18"] = ({"name": "d3", "number": "18", "type": "signal"})
        pins["pin_19"] = ({"name": "d4", "number": "19", "type": "power"})
        pins["pin_20"] = ({"name": "d5", "number": "20", "type": "signal"})
        pins["pin_21"] = ({"name": "d6", "number": "21", "type": "signal"})
        pins["pin_22"] = ({"name": "d7", "number": "22", "type": "signal"})
        pins["pin_23"] = ({"name": "d8", "number": "23", "type": "signal"})
        pins["pin_24"] = ({"name": "d9", "number": "24", "type": "signal"})
        pins["pin_25"] = ({"name": "d10", "number": "25", "type": "signal"})
        pins["pin_26"] = ({"name": "d11", "number": "26", "type": "signal"})
        pins["pin_27"] = ({"name": "d12", "number": "27", "type": "signal"})
        pins["pin_28"] = ({"name": "d13", "number": "28", "type": "signal"})
        pins["pin_29"] = ({"name": "gnd", "number": "29", "type": "power"})
        pins["pin_30"] = ({"name": "aref", "number": "30", "type": "signal"})
        pins["pin_31"] = ({"name": "sda_d18", "number": "31", "type": "signal"})
        pins["pin_32"] = ({"name": "scl_d19", "number": "32", "type": "signal"})
        
        part_details["pins"] = pins
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)

    #      espressif 32c
    
    #            devkitc
    if True:
        part_details = {}
        part_details["description"] = "Devkitc pinout version of espresif esp32 breakout." 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board_mcu"
        part_details["size"] = "esp32_38_pin_devkitc"
        part_details["color"] = ""
        part_details["description_main"] = "espressif_esp32"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        pins = {}        
        pins["pin_1"] = ({"name": "3v3", "number": "1", "type": "signal"})
        pins["pin_2"] = ({"name": "enable", "number": "2", "type": "signal"})
        pins["pin_3"] = ({"name": "vp", "number": "3", "type": "signal"})
        pins["pin_4"] = ({"name": "vn2", "number": "4", "type": "power"})
        pins["pin_5"] = ({"name": "io34", "number": "5", "type": "signal"})
        pins["pin_6"] = ({"name": "io35", "number": "6", "type": "signal"})
        pins["pin_7"] = ({"name": "io32", "number": "7", "type": "signal"})
        pins["pin_8"] = ({"name": "io33", "number": "8", "type": "signal"})
        pins["pin_9"] = ({"name": "io25", "number": "9", "type": "signal"})
        pins["pin_10"] = ({"name": "io26", "number": "10", "type": "signal"})
        pins["pin_11"] = ({"name": "io27", "number": "11", "type": "signal"})
        pins["pin_12"] = ({"name": "io14", "number": "12", "type": "signal"})
        pins["pin_13"] = ({"name": "io12", "number": "13", "type": "signal"})
        pins["pin_14"] = ({"name": "gnd", "number": "14", "type": "signal"})
        pins["pin_15"] = ({"name": "io13", "number": "15", "type": "signal"})
        pins["pin_16"] = ({"name": "d2", "number": "16", "type": "signal"})
        pins["pin_17"] = ({"name": "d3", "number": "17", "type": "power"})
        pins["pin_18"] = ({"name": "cmd", "number": "18", "type": "signal"})
        pins["pin_19"] = ({"name": "5v", "number": "19", "type": "signal"})
        pins["pin_20"] = ({"name": "clk", "number": "20", "type": "signal"})
        pins["pin_21"] = ({"name": "d0", "number": "21", "type": "signal"})
        pins["pin_22"] = ({"name": "d1", "number": "22", "type": "signal"})
        pins["pin_23"] = ({"name": "io15", "number": "23", "type": "signal"})
        pins["pin_24"] = ({"name": "io2", "number": "24", "type": "signal"})
        pins["pin_25"] = ({"name": "io0", "number": "25", "type": "signal"})
        pins["pin_26"] = ({"name": "io4", "number": "26", "type": "signal"})
        pins["pin_27"] = ({"name": "io16", "number": "27", "type": "power"})
        pins["pin_28"] = ({"name": "io17", "number": "28", "type": "signal"})
        pins["pin_29"] = ({"name": "io5", "number": "29", "type": "gnd"})
        pins["pin_30"] = ({"name": "io18", "number": "30", "type": "power"})
        pins["pin_31"] = ({"name": "io19", "number": "31", "type": "signal"})
        pins["pin_32"] = ({"name": "gnd", "number": "32", "type": "signal"})
        pins["pin_33"] = ({"name": "io21", "number": "33", "type": "signal"})
        pins["pin_34"] = ({"name": "rx", "number": "34", "type": "signal"})
        pins["pin_35"] = ({"name": "tx", "number": "35", "type": "signal"})
        pins["pin_36"] = ({"name": "io22", "number": "36", "type": "signal"})
        pins["pin_37"] = ({"name": "io23", "number": "37", "type": "signal"})
        pins["pin_38"] = ({"name": "gnd", "number": "38", "type": "signal"})
        part_details["pins"] = pins
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)

        #wroom
        part_details = {}
        part_details["description"] = "Wroom pinout version of espresif esp32 breakout." 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board_mcu"
        part_details["size"] = "esp32_30_pin"
        part_details["color"] = ""
        part_details["description_main"] = "espressif_esp32"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        pins = {}
        pins["pin_1"] = ({"name": "en", "number": "1", "type": ""})
        pins["pin_2"] = ({"name": "vp", "number": "2", "type": ""})
        pins["pin_3"] = ({"name": "vin", "number": "3", "type": ""})
        pins["pin_4"] = ({"name": "d34", "number": "4", "type": ""})
        pins["pin_5"] = ({"name": "d35", "number": "5", "type": ""})
        pins["pin_6"] = ({"name": "d32", "number": "6", "type": ""})
        pins["pin_7"] = ({"name": "d33", "number": "7", "type": ""})
        pins["pin_8"] = ({"name": "d25", "number": "8", "type": ""})
        pins["pin_9"] = ({"name": "d26", "number": "9", "type": ""})
        pins["pin_10"] = ({"name": "d27", "number": "10", "type": ""})
        pins["pin_11"] = ({"name": "d14", "number": "11", "type": ""})
        pins["pin_12"] = ({"name": "d12", "number": "12", "type": ""})
        pins["pin_13"] = ({"name": "d13", "number": "13", "type": ""})
        pins["pin_14"] = ({"name": "gnd", "number": "14", "type": ""})
        pins["pin_15"] = ({"name": "vin", "number": "15", "type": ""})
        pins["pin_16"] = ({"name": "3v3", "number": "16", "type": ""})
        pins["pin_17"] = ({"name": "gnd", "number": "17", "type": ""})
        pins["pin_18"] = ({"name": "d15", "number": "18", "type": ""})
        pins["pin_19"] = ({"name": "d2", "number": "19", "type": ""})
        pins["pin_20"] = ({"name": "d4", "number": "20", "type": ""})
        pins["pin_21"] = ({"name": "rx2", "number": "21", "type": ""})
        pins["pin_22"] = ({"name": "tx2", "number": "22", "type": ""})        
        pins["pin_23"] = ({"name": "d5", "number": "23", "type": ""})
        pins["pin_24"] = ({"name": "d18", "number": "24", "type": ""})
        pins["pin_25"] = ({"name": "d19", "number": "25", "type": ""})
        pins["pin_26"] = ({"name": "d21", "number": "26", "type": ""})
        pins["pin_27"] = ({"name": "rx0", "number": "27", "type": ""})
        pins["pin_28"] = ({"name": "tx0", "number": "28", "type": ""})
        pins["pin_29"] = ({"name": "d22", "number": "29", "type": ""})
        pins["pin_30"] = ({"name": "d23", "number": "30", "type": ""})
        part_details["pins"] = pins
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)

    #      raspberry pi 2040
    #            pico
    if True:
        part_details = {}
        part_details["description"] = "" 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board_mcu"
        part_details["size"] = "pico"
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        pins = {}
        pins["pin_1"] = ({"name": "gp0", "number": "1", "type": "signal"})
        pins["pin_2"] = ({"name": "gp1", "number": "2", "type": "signal"})
        pins["pin_3"] = ({"name": "gnd", "number": "3", "type": "signal"})
        pins["pin_4"] = ({"name": "gp2", "number": "4", "type": "power"})
        pins["pin_5"] = ({"name": "gp3", "number": "5", "type": "signal"})
        pins["pin_6"] = ({"name": "gp4", "number": "6", "type": "signal"})
        pins["pin_7"] = ({"name": "gp5", "number": "7", "type": "signal"})
        pins["pin_8"] = ({"name": "gnd", "number": "8", "type": "signal"})
        pins["pin_9"] = ({"name": "gp6", "number": "9", "type": "signal"})
        pins["pin_10"] = ({"name": "gp7", "number": "10", "type": "signal"})
        pins["pin_11"] = ({"name": "gp8", "number": "11", "type": "signal"})
        pins["pin_12"] = ({"name": "gp9", "number": "12", "type": "signal"})
        pins["pin_13"] = ({"name": "gnd", "number": "13", "type": "signal"})
        pins["pin_14"] = ({"name": "gp10", "number": "14", "type": "signal"})
        pins["pin_15"] = ({"name": "gp11", "number": "15", "type": "signal"})
        pins["pin_16"] = ({"name": "gp12", "number": "16", "type": "signal"})
        pins["pin_17"] = ({"name": "gp13", "number": "17", "type": "power"})
        pins["pin_18"] = ({"name": "gnd", "number": "18", "type": "signal"})
        pins["pin_19"] = ({"name": "gp14", "number": "19", "type": "signal"})
        pins["pin_20"] = ({"name": "gp15", "number": "20", "type": "signal"})
        pins["pin_21"] = ({"name": "gp16", "number": "21", "type": "signal"})
        pins["pin_22"] = ({"name": "gp17", "number": "22", "type": "signal"})
        pins["pin_23"] = ({"name": "gnd", "number": "23", "type": "signal"})
        pins["pin_24"] = ({"name": "gp18", "number": "24", "type": "signal"})
        pins["pin_25"] = ({"name": "gp19", "number": "25", "type": "signal"})
        pins["pin_26"] = ({"name": "gp20", "number": "26", "type": "signal"})
        pins["pin_27"] = ({"name": "gp21", "number": "27", "type": "power"})
        pins["pin_28"] = ({"name": "gnd", "number": "28", "type": "signal"})
        pins["pin_29"] = ({"name": "gp22", "number": "29", "type": "gnd"})
        pins["pin_30"] = ({"name": "run", "number": "30", "type": "power"})
        pins["pin_31"] = ({"name": "a0", "number": "31", "type": "signal"})
        pins["pin_32"] = ({"name": "a1", "number": "32", "type": "signal"})
        pins["pin_33"] = ({"name": "gnd_adc", "number": "33", "type": "signal"})
        pins["pin_34"] = ({"name": "a2", "number": "34", "type": "signal"})
        pins["pin_35"] = ({"name": "vref", "number": "35", "type": "signal"})
        pins["pin_36"] = ({"name": "3v3_out", "number": "36", "type": "signal"})
        pins["pin_37"] = ({"name": "3v3_enable", "number": "37", "type": "signal"})
        pins["pin_38"] = ({"name": "gnd", "number": "38", "type": "signal"})
        pins["pin_39"] = ({"name": "vsys", "number": "39", "type": "signal"})
        pins["pin_40"] = ({"name": "vbus", "number": "40", "type": "signal"})
        part_details["pins"] = pins
        pins_pico = copy.deepcopy(pins)
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []


        pico_default = copy.deepcopy(part_details)

        chips = []
        chips.append("raspberry_pi_2040")
        chips.append("raspberry_pi_2350")

        extras = []
        extras.append("")
        extras.append("wifi")
        extras.append("header_attached")
        extras.append("wifi_header_attached")

        for chip in chips:
            for extra in extras:
                part_details = copy.deepcopy(pico_default)
                part_details["description_main"] = chip
                part_details["description_extra"] = extra
                parts.append(part_details)


        #3_5 mm pitch screw terminal 55 mm x 73 mm
        part_details = copy.deepcopy(pico_default)
        part_details["color"] = "screw_terminal"
        part_details["description_main"] = "55_mm_width_73_mm_height_purple_pcb_3_5_mm_pitch_terminal"
        part_details["description_extra"] = ""
        parts.append(part_details)

        
        #3_5 mm pitch screw terminal 55 mm x 73 mm
        part_details = copy.deepcopy(pico_default)
        part_details.pop("pins","")
        part_details["color"] = "robotic"
        part_details["description_main"] = "42_mm_width_64_mm_height_green_pcb"
        part_details["description_extra"] = "simply_robtoics_motor_driver_board_for_raspberry_pi_pico"
        part_details["manufacturer"] = "kitronik"
        part_details["part_number"] = "5348"
        part_details["link_distributor_kitronik"] = "https://kitronik.co.uk/products/5348-kitronik-simply-robotics-for-raspberry-pi-pico"
        parts.append(part_details)

    # motor driver
    #       dc motor
    # l298n
    if True:
        part_details = {}
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board_motor_driver"
        part_details["size"] = ["l298n"]
        part_details["color"] = ["dual_h_bridge"]
        part_details["description_main"] = "25_mm_width_21_mm_length_red_pcb"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = ""
        part_details["short_name"] = ""        
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)

        l298_default = copy.deepcopy(part_details)

    # l9110s    
        part_details = {}
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board_motor_driver"
        part_details["size"] = ["l9110s"]
        part_details["color"] = ["dual_h_bridge"]
        part_details["description_main"] = "29_mm_width_24_mm_length_blue_pcb_5_08_mm_pitch_screw_terminal"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = ""
        part_details["short_name"] = ""        
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)

        l9110s_default = copy.deepcopy(part_details)

    # drv8833
        part_details = {}
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board_motor_driver"
        part_details["size"] = ["drv8833"]
        part_details["color"] = ["dual_h_bridge"]
        part_details["description_main"] = "18_mm_width_16_mm_length_black_pcb"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = ""
        part_details["part_number_distributor_aliexpress"] = "1005006282457232"
        part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details["part_number_distributor_aliexpress"]}.html"
        part_details["short_name"] = ""
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)



    #      stepper motor
    #           step stick
    if True:
        part_details = {}
        part_details["description"] = "A common breakout format for a stepper motor driver" 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board_motor_driver"
        part_details["size"] = ["step_stick"]
        part_details["color"] = [""]
        part_details["description_main"] = "stepper_motor"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["short_name"] = ""
        pins = {}
        pins["pin_1"] = ({"name": "en", "number": "1", "type": "signal"})
        pins["pin_2"] = ({"name": "ms1", "number": "2", "type": "signal"})
        pins["pin_3"] = ({"name": "ms2", "number": "3", "type": "signal"})
        pins["pin_4"] = ({"name": "ms3", "number": "4", "type": "power"})
        pins["pin_5"] = ({"name": "rst", "number": "5", "type": "signal"})
        pins["pin_6"] = ({"name": "slp", "number": "6", "type": "signal"})
        pins["pin_7"] = ({"name": "step", "number": "7", "type": "signal"})
        pins["pin_8"] = ({"name": "dir", "number": "8", "type": "signal"})
        pins["pin_9"] = ({"name": "gnd", "number": "9", "type": "signal"})
        pins["pin_10"] = ({"name": "vdd", "number": "10", "type": "signal"})
        pins["pin_11"] = ({"name": "1b", "number": "11", "type": "signal"})
        pins["pin_12"] = ({"name": "1a", "number": "12", "type": "signal"})
        pins["pin_13"] = ({"name": "2a", "number": "13", "type": "signal"})
        pins["pin_14"] = ({"name": "2b", "number": "14", "type": "signal"})
        pins["pin_15"] = ({"name": "gnd", "number": "15", "type": "signal"})
        pins["pin_16"] = ({"name": "vmot", "number": "16", "type": "signal"})
        part_details["pins"] = pins
        part_details["kicad_reference"] = "BB"
        part_details["notes"] = []
        parts.append(part_details)

    #           makerbase mks_servo42c
    if True:
        part_details = {}
        part_details["description"] = "A closed loop stepper motor controller" 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board_motor_driver"
        part_details["size"] = ["nema_17_39_mm_width_39_mm_height"]
        part_details["color"] = [""]
        part_details["description_main"] = "stepper_motor"
        part_details["description_extra"] = "closed_loop"
        part_details["manufacturer"] = "makerbase"
        part_details["part_number"] = "mks_servo42c"
        part_details["short_name"] = ""
        part_details["notes"] = []
        parts.append(part_details)



    #           servo tester
    if True:
        part_details = {}
        part_details["description"] = "A servo tester" 
        part_details["classification"] = "electronic"
        part_details["type"] = "breakout_board_servo_tester"
        part_details["size"] = ["32_mm_width_28_mm_height"]
        part_details["color"] = [""]
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = "hw_141"
        part_details["short_name"] = ""
        part_details["notes"] = []
        parts.append(part_details)

    oomp.add_parts(parts, make_files=make_files)
    