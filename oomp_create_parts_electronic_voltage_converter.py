import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []


    # voktage_converter
    #       dc motor
    # l298n
    if True:
        part_details = {}
        part_details["classification"] = "electronic"
        part_details["type"] = "voltage_converter_buck"
        part_details["size"] = "variable_output_voltage"
        part_details["color"] = "3_amp_max_output"
        part_details["description_main"] = "20_mm_width_10_mm_length_green_pcb"
        part_details["description_extra"] = "12_volt_max_input"
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = ""
        part_details["short_name"] = ""    
        part_details["notes"] = []
        part_details["distributor_aliexpress"] = "1005007092498838"
        part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['distributor_aliexpress']}.html"
        parts.append(part_details)


        
        part_details = {}
        part_details["classification"] = "electronic"
        part_details["type"] = "voltage_converter_buck"
        part_details["size"] = ""
        part_details["color"] = "3_amp_max_output"
        part_details["description_main"] = "23_mm_width_17_mm_length_green_pcb"
        part_details["description_extra"] = "12_volt_max_input"
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = ""
        part_details["short_name"] = ""    
        part_details["notes"] = []
        part_details["distributor_aliexpress"] = "1005006982841208"
        part_details["link_distributor_aliexpress"] = f"https://www.aliexpress.com/item/{part_details['distributor_aliexpress']}.html"
        
        
        sizes = ["3_3_volt", "5_volt", "9_volt", "12_volt"]
        for size in sizes:
            part_details = copy.deepcopy(part_details)
            part_details["size"] = size
        
        parts.append(part_details)


    oomp.add_parts(parts, make_files=make_files)
    