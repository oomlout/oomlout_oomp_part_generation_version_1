import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "hardware"
    part_details["type"] = "magnet"
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = part_details.copy()

    #disc magnet
    if True:
        size_list = []
        size_list.append([3,13])
        size_list.append([6,1.5])
        size_list.append([6,6])
        size_list.append([10,2])
        size_list.append([12,1])
        
        size_list.append([10,1])
        
        size_list.append([15,1])
        size_list.append([20,1])

        for magnet_size in size_list:
            part_details = default_empty.copy()
            part_details["size"] = "cylinder"
            part_details["color"] = ""
            part_details["description_main"] = f"{str(magnet_size[0])}_mm_diameter_{str(magnet_size[1])}_mm_depth"
            part_details["diameter"] = magnet_size[0]
            part_details["thickness"] = magnet_size[1]
            part_details["depth"] = magnet_size[1]
            parts.append(part_details.copy())

    # countersunk disc
    if True:
        size_list = []
        #8,3, m3
        size_list.append([8,3,"m3"])
        size_list.append([15,3,"m3"])
        size_list.append([15,2,"m3"])

        for magnet_size in size_list:
            part_details = default_empty.copy()
            part_details["size"] = "disc"

            part_details["color"] = f"{str(magnet_size[2])}_countersunk_disc"
            part_details["description_main"] = f"{str(magnet_size[0])}_mm_diameter_{str(magnet_size[1])}_mm_depth"
            part_details["diameter"] = magnet_size[0]
            part_details["thickness"] = magnet_size[1]
            part_details["depth"] = magnet_size[1]
            parts.append(part_details.copy())

    # rectangule magnet
    if True:
        size_list = []
        size_list.append([20,3,1.5])
        size_list.append([20,10,3])
        size_list.append([29,9.5,1.5])
        size_list.append([29,9.5,4])
        size_list.append([29,9.5,9])
        size_list.append([19.45,5,3])
        size_list.append([20,6,1.5])

        size_list.append([5,5,5])


        for magnet_size in size_list:
            part_details = default_empty.copy()
            part_details["size"] = "rectangle"
            part_details["color"] = ""
            part_details["description_main"] = f"{str(magnet_size[0]).replace(".","_")}_mm_length_{str(magnet_size[1]).replace(".","_")}_mm_width_{str(magnet_size[2]).replace(".","_")}_mm_depth"
            part_details["length"] = magnet_size[0]
            part_details["width"] = magnet_size[1]
            part_details["thickness"] = magnet_size[2]
            part_details["depth"] = magnet_size[2]            
            parts.append(part_details.copy())

    #donut magnet
    if True:
        size_list = []
        size_list.append([6,3,3])
        #5,1,1.5
        size_list.append([5,1,1.5])

        for magnet_size in size_list:
            part_details = default_empty.copy()
            part_details["size"] = "donut"
            part_details["color"] = "m3_donut"
            part_details["description_main"] = f"{str(magnet_size[0]).replace(".","_")}_mm_diameter_{str(magnet_size[1]).replace(".","_")}_mm_hole_diameter_{str(magnet_size[2]).replace(".","_")}_mm_depth"
            part_details["diameter"] = magnet_size[0]
            part_details["hole_diameter"] = magnet_size[1]
            part_details["thickness"] = magnet_size[2]
            parts.append(part_details.copy())

    #
            

    #pot magnet
    if True:
        size_list = []
        size_list.append([32,15,"m5"])
        size_list.append([10,11_5,"m3"])
        size_list.append([16,11_5,"m4"])

        for magnet_size in size_list:
            part_details = default_empty.copy()
            part_details["size"] = "pot"
            part_details["color"] = "m3_pot"
            part_details["description_main"] = f"{str(magnet_size[0])}_mm_diameter_{str(magnet_size[1])}_mm_depth_{str(magnet_size[2])}_hole"
            parts.append(part_details.copy())
        

    
    oomp.add_parts(parts, **kwargs)
    