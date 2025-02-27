import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    parts = load_parts_old(parts)    

    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "led"
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = copy.deepcopy(part_details)

    #filament
    if True:
        colours = []
        colours.append("warm_white")
        colours.append("red")
        colours.append("green")
        colours.append("blue")
        colours.append("yellow")
        colours.append("pink")

        lengths = []
        lengths.append("38_mm")
        lengths.append("60_mm")
        lengths.append("80_mm")
        lengths.append("95_mm")
        lengths.append("130_mm")
        lengths.append("145_mm")
        lengths.append("185_mm")
        lengths.append("260_mm")
        lengths.append("300_mm")

        for colour in colours:
            for length in lengths:
                part_details = copy.deepcopy(default_empty)
                part_details["type"] = "led"
                part_details["size"] = "filament_3_volt"
                part_details["color"] = colour
                part_details["description_main"] = f"{length}_length"
                part_details["part_number_distriubutor_adafruit"] = "5509"
                part_details["link_distributor_adafruit"] = f"https://www.adafruit.com/product/{part_details['part_number_distriubutor_adafruit']}"
                part_details["part_number_distriubutor_aliexpress"] = "1005006222719149"
                part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['part_number_distriubutor_aliexpress']}.html"
                parts.append(part_details)


    #strip
    if True:
        voltages = []
        voltages.append("5_volt")
        voltages.append("12_volt")
        voltages.append("24_volt")

        widths = []
        widths.append("3_mm")
        widths.append("5_mm")
        widths.append("8_mm")

        colours = []
        colours.append("warm_white")
        colours.append("red")
        colours.append("green")
        colours.append("blue")
        colours.append("yellow")
        colours.append("pink")

        lengths = []
        lengths.append("500_mm")
        lengths.append("1000_mm")
        lengths.append("2000_mm")
        lengths.append("3000_mm")
        lengths.append("5000_mm")

        description_extras = []
        description_extras.append("320_leds_per_meter")
        description_extras.append("")

        for voltage in voltages:
            for width in widths:
                for colour in colours:
                    for length in lengths:
                        for description_extra in description_extras:
                            part_details = copy.deepcopy(default_empty)
                            part_details["type"] = "led"
                            part_details["size"] = f"strip_{voltage}_{width}_width"
                            part_details["color"] = colour
                            part_details["description_main"] = f"{length}_length"
                            part_details["description_extra"] = description_extra
                            part_details["part_number_distriubutor_aliexpress"] = "1005007532172895"
                            part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['part_number_distriubutor_aliexpress']}.html"
                            parts.append(part_details)




    oomp.add_parts(parts, **kwargs)
    
def load_parts_old(parts):


    #define a part 
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "led"
    part_details["size"] = ["3_mm","5_mm","10_mm","0201","0402","0603","0805","1206"]
    part_details["color"] = ["","red","green","blue","yellow","white"]
    part_details["description_main"] = ["","tint","clear"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["kicad_reference"] = "L"
    parts.append(part_details)

    #addressable
    #      xinglight
    #            1010    
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "led"
    part_details["size"] = ["1010"]
    part_details["color"] = ["rgb"]
    part_details["description_main"] = ["ws2812b"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "xinglight"
    part_details["part_number"] = "1010rgbc"
    part_details["kicad_reference"] = "L"
    parts.append(part_details)        
    pins = {}
    pins["pin_1"] = ({"name": "do", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "vdd", "number": "2", "type": "power"})
    pins["pin_3"] = ({"name": "gnd", "number": "3", "type": "power"})
    pins["pin_4"] = ({"name": "sdi", "number": "4", "type": "signal"})
    part_details["pins"] = pins
    
    #            5050
    #                  https://www.lcsc.com/product-detail/Light-Emitting-Diodes-LED_Worldsemi-WS2812B-B_C114586.html
    part_details = {}
    part_details["classification"] = "electronic"
    part_details["type"] = "led"
    part_details["size"] = ["5050"]
    part_details["color"] = ["rgb"]
    part_details["description_main"] = ["ws2812b"]
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "worldsemi"
    part_details["part_number"] = "ws2812b_b_w"
    part_details["kicad_reference"] = "L"
    parts.append(part_details)        
    pins = {}
    pins["pin_1"] = ({"name": "vdd", "number": "1", "type": "signal"})
    pins["pin_2"] = ({"name": "dout", "number": "2", "type": "power"})
    pins["pin_3"] = ({"name": "vss", "number": "3", "type": "power"})
    pins["pin_4"] = ({"name": "din", "number": "4", "type": "signal"})
    part_details["pins"] = pins

    return parts