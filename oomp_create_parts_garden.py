import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    extras = ["","seed_packet"]

    
    for extra in extras:
        #flower
        if True:
            part_details = {}
            part_details["classification"] = "garden"
            part_details["type"] = "plant"
            part_details["size"] = "flower"
            part_details["color"] = ""
            part_details["description_main"] = ""
            part_details["description_extra"] = ""
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["short_name"] = ""  
             

            default_flower = part_details
        
            #cosmos
            part_details = copy.deepcopy(default_flower)
            part_details["color"] = "cosmos"
            part_details["description_main"] = "apricotta"
            part_details["description_extra"] = extra
            part_details["distributor_sutton_seeds"] = "111300"
            part_details["link_distributor_sutton_seeds"] = f"https://www.suttons.co.uk/flower-seeds/cosmos-apricotta-seeds_mh11840"
            parts.append(part_details)    

            #daisy
            part_details = copy.deepcopy(default_flower)
            part_details["color"] = "daisy"
            part_details["description_main"] = "ox_eye"
            part_details["description_extra"] = extra
            part_details["distributor_sutton_seeds"] = "142036"
            part_details["link_distributor_sutton_seeds"] = f"https://www.suttons.co.uk/oxeye-daisy-seeds_mh-53149"

            #lupin
            part_details = copy.deepcopy(default_flower)
            part_details["color"] = "lupin"
            part_details["description_main"] = "mix_gallery"
            part_details["description_extra"] = extra
            part_details["distributor_sutton_seeds"] = "142035"

            #mix
            part_details = copy.deepcopy(default_flower)
            part_details["color"] = "mix"
            part_details["description_main"] = "wildflower_honeybee_mix"
            part_details["description_extra"] = extra
            part_details["distributor_sutton_seeds"] = "140000"
            part_details["link_distributor_sutton_seeds"] = f"https://www.suttons.co.uk/SUSGWE56/wildflower-honeybee-mix-seeds_mh-53182"

            #poached_egg
            part_details = copy.deepcopy(default_flower)
            part_details["color"] = "poached_egg"
            part_details["description_main"] = "main"
            part_details["description_extra"] = extra
            part_details["distributor_sutton_seeds"] = "142008"
            part_details["link_distributor_sutton_seeds"] = f"https://www.suttons.co.uk/SUDM2/lupin-gallery-mix-seeds_mh-623"

            #rudebeckia
            part_details = copy.deepcopy(default_flower)
            part_details["color"] = "rudebeckia"
            part_details["description_main"] = "viviani"
            part_details["description_extra"] = extra
            part_details["distributor_sutton_seeds"] = "130260"
            part_details["link_distributor_sutton_seeds"] = f"https://www.suttons.co.uk/flower-seeds/rudbeckia-viviani-seeds_mh11893"
            parts.append(part_details)    

            #sweet pea
            part_details = copy.deepcopy(default_flower)
            part_details["color"] = "sweet_pea"
            part_details["description_main"] = "scentsational_mix"
            part_details["description_extra"] = extra
            part_details["distributor_sutton_seeds"] = "133275"
            part_details["link_distributor_sutton_seeds"] = f"https://www.suttons.co.uk/SUSGWE348/sweet-pea-scentsational-mix-seeds_mh13761"
            parts.append(part_details)  

            #teasel
            part_details = copy.deepcopy(default_flower)
            part_details["color"] = "teasel"
            part_details["description_main"] = "main"  
            part_details["description_extra"] = extra
            part_details["distributor_sutton_seeds"] = "142025"
            part_details["link_distributor_sutton_seeds"] = f"https://www.suttons.co.uk/SUSGWE184/teasel-seeds-for-pollinators_mh-53151"

        #herb
        if True:
            part_details = {}
            part_details["classification"] = "garden"
            part_details["type"] = "plant"
            part_details["size"] = "herb"
            part_details["color"] = ""
            part_details["description_main"] = ""
            part_details["description_extra"] = ""
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["short_name"] = ""  
             

            default_herb = part_details
        
            #basil
            part_details = copy.deepcopy(default_herb)
            part_details["color"] = "basil"
            part_details["description_main"] = "lime_mrs_burns"
            part_details["description_extra"] = extra
            part_details["distributor_sutton_seeds"] = "142005"
            part_details["link_distributor_sutton_seeds"] = f"https://www.suttons.co.uk/SUSGWE46/basil-lime-mrs-burns-seeds-for-pollinators_mh-52300"
            parts.append(part_details)    

            #dill
            part_details = copy.deepcopy(default_herb)
            part_details["color"] = "dill"
            part_details["description_main"] = "main"
            part_details["description_extra"] = extra
            part_details["distributor_sutton_seeds"] = "142038"
            part_details["link_distributor_sutton_seeds"] = f"https://www.suttons.co.uk/SUSGWE56/dill-herb-seeds_mh-52849"

            #oregano
            part_details = copy.deepcopy(default_herb)
            part_details["color"] = "oregano"
            part_details["description_main"] = "main"
            part_details["description_extra"] = extra
            part_details["distributor_sutton_seeds"] = "142017"
            part_details["link_distributor_sutton_seeds"] = f"https://www.suttons.co.uk/SUSGWE184/oregano-seeds-for-pollinators_mh-52697"

            #thyme
            part_details = copy.deepcopy(default_herb)
            part_details["color"] = "thyme"
            part_details["description_main"] = "orange_scented"
            part_details["description_extra"] = extra
            part_details["distributor_sutton_seeds"] = "142002"
            part_details["link_distributor_sutton_seeds"] = f"https://www.suttons.co.uk/SUSGWE184/thyme-orange-scented-seeds-for-pollinators_mh-52305"




        #tree
        if True:
            part_details = {}
            part_details["classification"] = "garden"
            part_details["type"] = "plant"
            part_details["size"] = "tree"
            part_details["color"] = ""
            part_details["description_main"] = ""
            part_details["description_extra"] = ""
            part_details["manufacturer"] = ""
            part_details["part_number"] = ""
            part_details["short_name"] = ""  
             

            default_tree = part_details
        
            #palm
            part_details = copy.deepcopy(default_tree)
            part_details["color"] = "palm"
            part_details["description_main"] = "trachycarpus_fortunei"
            part_details["description_extra"] = extra
            part_details["distributor_sutton_seeds"] = "105005"
            part_details["link_distributor_sutton_seeds"] = f"https://www.suttons.co.uk/flower-seeds/trachycarpus-fortunei-seeds_mh13516"
            parts.append(part_details)    



    oomp.add_parts(parts, make_files=make_files)
    