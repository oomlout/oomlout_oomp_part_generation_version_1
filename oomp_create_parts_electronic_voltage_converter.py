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
        part_details["description_main"] = "25_mm_width_10_mm_length_green_pcb"
        part_details["description_extra"] = "24_volt_max_input"
        part_details["manufacturer"] = "aliexpress"
        part_details["part_number"] = ""
        part_details["short_name"] = ""    
        part_details["notes"] = []
        parts.append(part_details)

        l298_default = copy.deepcopy(part_details)


    oomp.add_parts(parts, make_files=make_files)
    