import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    

    parts = []

    part_details = {}
    part_details["classification"] = "exercise_equipment"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = copy.deepcopy(part_details)

    #bike_stationary
    if True:
        part_details = copy.deepcopy(default_empty)        
        part_details["type"] = "bike_stationary"
            
        default_current = part_details

        detail_default_current = {}

        #series
        details = [] 
        #fiskbo
        if True:
            #white
            #base bike
            detail = copy.deepcopy(detail_default_current)
            detail.update({"size": "peloton_bike",
                            "description_main":"",
                            "description_extra": "", 
                            "manufacturer": "peloton"})
            details.append(detail)
            detail = copy.deepcopy(detail_default_current)
            detail.update({ "size": "peloton_bike",
                            "description_main":"screen",
                            "description_extra": "third_generation", 
                            "manufacturer": "peloton"})
            details.append(detail)
            

        for detail in details:
            part_details = copy.deepcopy(default_current)
            part_details.update(detail)
            part_number_exact = part_details.get("part_number_exact", "")
            part_number = part_number_exact.replace(".", "_")
            part_details["part_number"] = part_number
            link_distributor_ikea = f"https://www.ikea.com/gb/en/search/?q={part_number_exact}"
            part_details["link_distributor_ikea"] = link_distributor_ikea
            parts.append(part_details)

    oomp.add_parts(parts, make_files=make_files)
    