
import importlib
import oomp
import yaml
from multiprocessing import Pool
import copy

part_types = []

cnt_error = 0

cnt_gen = 1

part_types.append("aluminium_extrusion")

part_types.append("appliance_vacuum_cleaner")

part_types.append("archive")

part_types.append("camera")

part_types.append("computer")
part_types.append("computer_monitor")
part_types.append("computer_tablet")

part_types.append("craft")

part_types.append("decorating")
part_types.append("dish")

part_types.append("hardware_aluminium_extrusion")    
part_types.append("hardware_bearing")
part_types.append("hardware_bolt") # also set screw
part_types.append("hardware_nut")
part_types.append("hardware_other")
part_types.append("hardware_screw")
part_types.append("hardware_spacer")
part_types.append("hardware_standoff")
part_types.append("hardware_washer")
part_types.append("hardware_variety_pack")

part_types.append("industrial")

part_types.append("electrical")

part_types.append("electronic_battery")
part_types.append("electronic_battery_box")
part_types.append("electronic_breakout_board")
part_types.append("electronic_button")
part_types.append("electronic_capacitor")
part_types.append("electronic_connector")
part_types.append("electronic_crimp")
part_types.append("electronic_crimp_housing")
part_types.append("electronic_crystal")
part_types.append("electronic_diode")
part_types.append("electronic_display")
part_types.append("electronic_header")
part_types.append("electronic_heatshrink")
part_types.append("electronic_ic")
part_types.append("electronic_interposer")
part_types.append("electronic_led")
part_types.append("electronic_mounting_hole")
part_types.append("electronic_nettie")
part_types.append("electronic_pmic")
part_types.append("electronic_potentiometer")
part_types.append("electronic_prototyping")
part_types.append("electronic_resistor")
part_types.append("electronic_screw_terminal")
part_types.append("electronic_socket")
part_types.append("electronic_voltage_converter")
part_types.append("electronic_wire_pigtail")

part_types.append("exercise_equipment")

part_types.append("flashlight")

part_types.append("food")
part_types.append("food_seasoning")

part_types.append("furniture")
part_types.append("furniture_ikea")

part_types.append("garden")

part_types.append("household")

part_types.append("mechanical_coupler")
part_types.append("mechanical_gear")
part_types.append("mechanical_motor")
part_types.append("mechanical_solenoid")
part_types.append("mechanical_timing_pulley_belt")
part_types.append("mechanical_wheel")

part_types.append("oobb")

part_types.append("company_oomlout")


part_types.append("packaging_bag")
part_types.append("packaging_cardboard_box_postal")
part_types.append("packaging_elastic_band")
part_types.append("packaging_label")
part_types.append("packaging_takeaway_container")
part_types.append("packaging_tin")

part_types.append("paper")

part_types.append("phone")
#printer
part_types.append("printer")

part_types.append("remote_control")

part_types.append("robot_arm")
part_types.append("robot_vacuum")

#stationary
part_types.append("stationery")

part_types.append("storage")

part_types.append("three_d_printer")
part_types.append("three_d_printer_filament")
part_types.append("three_d_printer_printer")


part_types.append("tool")

part_types.append("toy")

part_types.append("warehouse")

part_types.append("wood_timber_cls")

#must be last
part_types.append("project_github")




for type in part_types:    
    importlib.import_module(f'oomp_create_parts_{type}')

def load_parts(**kwargs):
    print("loading parts from modules")
    filter = kwargs.get('filter', "")
    for type in part_types:
        #if filter isn't an array make it one
        filters = []
        if not isinstance(filter, list):
            filters = [filter]
        if filter == "":
            filters = [""]

        filters = copy.deepcopy(filters)
        for filter in filters:
            if filter in type:
                if type == "project_github":
                    try:
                        importlib.import_module(f'oomp_create_parts_{type}').load_parts(**kwargs)
                    except:
                        print("project_github not available")
                        print("project_github not available")
                        print("project_github not available")
                        print("project_github not available")
                        print("project_github not available")
                        import time
                        time.sleep(10)
                        return
                importlib.import_module(f'oomp_create_parts_{type}').load_parts(**kwargs)
    
    #add category making last
    if "category" in filters or "" in filters:
        print("creating category parts")
        importlib.import_module(f'oomp_create_parts_category').load_parts(**kwargs)


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
    threading = True
    if threading:
        save_parts_to_individual_yaml_files_threading()
    else:
        save_parts_to_individual_yaml_files()

def save_parts_to_individual_yaml_files(**kwargs):
    global cnt_error, cnt_gen
    print("saving parts to yaml")
    import yaml
    try:
        for part_id in oomp.parts:
            part = oomp.parts[part_id]
            del part['make_files']
            yaml_file = f"parts/{part_id}/working.yaml"
            if not os.path.exists(f"parts/{part_id}"):
                yaml_file = f"parts_source/{part_id}/working.yaml"
            with open(yaml_file, "w") as outfile:
                #print(f"writing {yaml_file}")
                if cnt_gen % 100 == 0:
                    print(".", end="")
                yaml.dump(part, outfile, indent=4)
                cnt_gen += 1
    except Exception as e:
        print(e)
        cnt_error += 1
    cnt_gen += 1



def save_part_to_yaml(args):
    part, yaml_file = args
    with open(yaml_file, 'w') as file:
        yaml.dump(part, file)

def save_parts_to_individual_yaml_files_threading(parts_list):
    tasks = []
    for part_id in parts_list:
        part = oomp.parts[part_id]
        del part['make_files']
        yaml_file = f"parts/{part_id}/working.yaml"
        
        if not os.path.exists(f"parts/{part_id}"):
            yaml_file = f"parts_source/{part_id}/working.yaml"
        
        tasks.append((part, yaml_file))

    with Pool() as pool:
        pool.map(save_part_to_yaml, tasks)