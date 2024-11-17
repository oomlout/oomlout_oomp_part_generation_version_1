import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    #print_time]
    part_details = {}
    part_details["classification"] = "robot_vacuum"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = "roomba"
    part_details["part_number"] = "520"
    part_details["short_name"] = "Roomba 520"  
    parts.append(part_details)    
    
    roomba_base = copy.deepcopy(part_details)
    
    part_details = copy.deepcopy(roomba_base)
    part_details["part_number"] = "530"
    part_details["short_name"] = "Roomba 530"  
    parts.append(part_details)    

    part_details = copy.deepcopy(roomba_base)
    part_details["part_number"] = "540"
    part_details["short_name"] = "Roomba 540"
    parts.append(part_details)


    #parts
    
    part_details = {}
    part_details["classification"] = "robot_vacuum"
    part_details["type"] = "part"
    part_details["size"] = "robot_vacuum_roomba_500_series"
    part_details["color"] = "motor"
    part_details["description_main"] = "wheel"
    part_details["description_extra"] = "left_side"
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = "Roomba 500 Motor Wheel Left Side"  
    parts.append(part_details)    

    part_details = copy.deepcopy(part_details)
    part_details["description_extra"] = "right_side"
    part_details["short_name"] = "Roomba 500 Motor Wheel Right Side"
    parts.append(part_details)

    part_details = {}
    part_details["classification"] = "robot_vacuum"
    part_details["type"] = "part"
    part_details["size"] = "robot_vacuum_roomba_500_series"
    part_details["color"] = "sub_assembly"
    part_details["description_main"] = "caster_wheel"
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""
    part_details["short_name"] = "Roomba 500 Caster Wheel"  
    parts.append(part_details)    
   



    oomp.add_parts(parts, make_files=make_files)
    