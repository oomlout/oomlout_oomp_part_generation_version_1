import oomp
import csv

def load_parts(**kwargs):
    print(f"  loading parts {__name__}")
    
    file_csv = "source/oomp_bearing_sizes.csv"
    bearings = []
    with open(file_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: 
            bearings.append(row)
    parts = []

    for bearing in bearings:
        part_details = {}
        part_details["classification"] = "hardware"
        part_details["type"] = f"bearing"
        part_details["size"] = f"{bearing['series']}_series"
        part_details["color"] = f"{bearing['size']}_size"
        id = bearing['id'].replace(".","_")
        od = bearing['od'].replace(".","_")
        depth = bearing['width'].replace(".","_")    
        part_details["description_main"] = f"{id}_mm_id_{od}_mm_od_{depth}_mm_depth"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        
        parts.append(part_details)    


    
    oomp.add_parts(parts, **kwargs)
    