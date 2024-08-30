
import importlib
import oomp

part_types = []

part_types.append("camera")

part_types.append("computer")
part_types.append("computer_monitor")

part_types.append("hardware_aluminium_extrusion")    
part_types.append("hardware_bearing")
part_types.append("hardware_bolt") # also set screw
part_types.append("hardware_nut")
part_types.append("hardware_screw")
part_types.append("hardware_spacer")
part_types.append("hardware_standoff")
part_types.append("hardware_washer")

part_types.append("electrical")

part_types.append("electronic_battery_box")
part_types.append("electronic_breakout_board")
part_types.append("electronic_button")
part_types.append("electronic_capacitor")
part_types.append("electronic_connector")
part_types.append("electronic_crimp")
part_types.append("electronic_crimp_housing")
part_types.append("electronic_crystal")
part_types.append("electronic_diode")
part_types.append("electronic_header")
part_types.append("electronic_ic")
part_types.append("electronic_interposer")
part_types.append("electronic_led")
part_types.append("electronic_mounting_hole")
part_types.append("electronic_nettie")
part_types.append("electronic_pmic")
part_types.append("electronic_potentiometer")
part_types.append("electronic_prototyping")
part_types.append("electronic_resistor")
part_types.append("electronic_socket")

part_types.append("food")

part_types.append("furniture_ikea")

part_types.append("household")

part_types.append("mechanical_motor")

part_types.append("oobb")

part_types.append("company_oomlout")


part_types.append("packaging_bag")
part_types.append("packaging_cardboard_box_postal")
part_types.append("packaging_label")
part_types.append("packaging_takeaway_container")
part_types.append("packaging_tin")

part_types.append("paper")



part_types.append("storage")

part_types.append("three_d_printer_filament")

part_types.append("tool")



for type in part_types:
    importlib.import_module(f'oomp_create_parts_{type}')

def load_parts(**kwargs):
    print("loading parts from modules")
    filter = kwargs.get('filter', "")
    for type in part_types:
        if filter in type:
            importlib.import_module(f'oomp_create_parts_{type}').load_parts(**kwargs)


def load_parts_from_yaml(**kwargs):
    print("loading parts from yaml")
    import yaml
    with open("parts.yaml", "r") as infile:
        parts = yaml.load(infile, Loader=yaml.FullLoader)
    oomp.parts = parts

import os

def load_parts_from_pickle(**kwargs):
    print("loading parts from pickle")
    import pickle
    file_pickle = "tmp/parts.pickle"
    if not os.path.exists(file_pickle):
        file_pickle = "c:/gh/oomlout_oomp_part_src/tmp/parts.pickle"
        if not os.path.exists(file_pickle):
            print(f"file {file_pickle} does not exist")
            return
    with open(file_pickle, "rb") as infile:
        parts = pickle.load(infile)
    oomp.parts = parts

def save_parts_to_yaml(**kwargs):
    print("saving parts to yaml")
    import yaml
    with open("parts.yaml", "w") as outfile:
        yaml.dump(oomp.parts, outfile, indent=4)

def save_parts_to_pickle(**kwargs):
    print("saving parts to pickle")
    import pickle
    file_pickle = "tmp/parts.pickle"
    with open(file_pickle, "wb") as outfile:
        pickle.dump(oomp.parts, outfile)

def save_parts_to_individual_yaml_files(**kwargs):
    print("saving parts to yaml")
    import yaml
    for part_id in oomp.parts:
        part = oomp.parts[part_id]
        del part['make_files']
        yaml_file = f"parts/{part_id}/working/working.yaml"
        with open(yaml_file, "w") as outfile:
            print(f"writing {yaml_file}")
            yaml.dump(part, outfile, indent=4)