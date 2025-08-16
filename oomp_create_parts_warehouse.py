import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []
      
        
    # tote    
    if True:
        sizes = ["oomlout_owner"]
        colors = ["tote_burgundy", "box_cubby_short", "box_cubby_long", "box_cube","tote_small"]
    
        description_mains = []
        count = 200
        for i in range(count):
            description_mains.append(f"{i}")


        part_details = {}
        part_details["classification"] = "warehouse"
        part_details["type"] = "storage_container"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["part_number_exact"] = ""
        part_details["short_name"] = ""  

        current_default = copy.deepcopy(part_details)
        
        for size in sizes:
            for color in colors:
                for description_main in description_mains:
                    part_details = copy.deepcopy(current_default)
                    part_details["size"] = size
                    part_details["color"] = color
                    part_details["description_main"] = description_main
                    parts.append(part_details)

    
    #location          
    if True:
        #site
        types = ["location_home"]
        #room
        sizes = []
        current_site = "home_site"
        current_room = "kitchen_new_room"
        #location
        locations = []
        locations.append([current_site, current_room, "back_wall_kallax_unit",2,4])
        locations.append([current_site, current_room, "back_wall_magazine_holder_unit",1,3])
        locations.append([current_site, current_room, "back_wall_box_cubby_short_unit",4,6])
        locations.append([current_site, current_room, "back_wall_cupboard_pantry_1_unit",1,3])
        locations.append([current_site, current_room, "back_wall_cupboard_pantry_2_unit",1,3])
        locations.append([current_site, current_room, "back_wall_cupboard_pantry_3_unit",1,3])
        locations.append([current_site, current_room, "back_wall_cupboard_pantry_4_unit",1,3])
        locations.append([current_site, current_room, "fridge_unit",4,2])
        locations.append([current_site, current_room, "fridge_door_unit",3,2])
        locations.append([current_site, current_room, "island_fridge_side_unit",2,3])
        locations.append([current_site, current_room, "island_table_side_unit",3,3])
   
        part_details = {}
        part_details["classification"] = "warehouse"
        part_details["type"] = "storage_location"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["part_number_exact"] = ""
        part_details["short_name"] = ""  

        current_default = copy.deepcopy(part_details)
        
        for location in locations:
            size = location[0]            
            color = location[1]
            description_main = location[2]
            row = location[3]
            column = location[4]
            for i in range(1, row+1):
                for j in range(1, column+1):
                    part_details = copy.deepcopy(current_default)
                    part_details["size"] = size
                    part_details["color"] = color
                    part_details["description_main"] = description_main
                    part_details["description_extra"] = f"{i}_{j}"
                    parts.append(part_details)            
        
        
        
    

    oomp.add_parts(parts, make_files=make_files)
    