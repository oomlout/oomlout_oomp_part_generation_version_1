import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    part_details = {}
    part_details["classification"] = "book"
    part_details["type"] = ""
    part_details["size"] = ""
    part_details["color"] = ""
    part_details["description_main"] = ""
    part_details["description_extra"] = ""
    part_details["manufacturer"] = ""
    part_details["part_number"] = ""

    default_empty = part_details.copy()

    
    #activty
    if True:
        current_item = {"type": "activity"}
        sizes = []
        sizes.append("math")
        sizes.append("colouring")
        sizes.append("puzzle")
        sizes.append("drawing")
        sizes.append("")
        
        for size in sizes:
            part = copy.deepcopy(default_empty)
            part.update(current_item)            
            part["size"] = size
            parts.append(copy.deepcopy(part))

    #chapter
    if True:
        current_item = {"type": "chapter"}
        sizes = []
        sizes.append("princess")
        sizes.append("dog")
        sizes.append("adult")
        sizes.append("teen")
        sizes.append("child")
        sizes.append("roald_dahl")
        sizes.append("")        
        for size in sizes:
            part = copy.deepcopy(default_empty)
            part.update(current_item)            
            part["size"] = size
            parts.append(copy.deepcopy(part))

    #cook
    if True:
        current_item = {"type": "cook"}
        sizes = []
        sizes.append("vegetarian")
        sizes.append("vegan")
        sizes.append("meat")
        sizes.append("fish")
        sizes.append("child")
        sizes.append("dessert")
        sizes.append("")        
        for size in sizes:
            part = copy.deepcopy(default_empty)
            part.update(current_item)            
            part["size"] = size
            parts.append(copy.deepcopy(part))

    #looking book
    if True:
        current_item = {"type": "looking"}
        sizes = []
        sizes.append("animals")
        sizes.append("vehicles")
        sizes.append("nature")
        sizes.append("transport")
        sizes.append("food")
        sizes.append("musical_programme")
        sizes.append("foreign_language")
        sizes.append("")        
        for size in sizes:
            part = copy.deepcopy(default_empty)
            part.update(current_item)            
            part["size"] = size
            parts.append(copy.deepcopy(part))

    #picture book
    if True:
        current_item = {"type": "picture"}
        sizes = []
        sizes.append("")        
        for size in sizes:
            part = copy.deepcopy(default_empty)
            part.update(current_item)            
            part["size"] = size
            parts.append(copy.deepcopy(part))
    
    #poetry
    if True:
        current_item = {"type": "poetry"}
        sizes = []
        sizes.append("")        
        for size in sizes:
            part = copy.deepcopy(default_empty)
            part.update(current_item)            
            part["size"] = size
            parts.append(copy.deepcopy(part))

    #on the way out
    if True:
        current_item = {"type": "on_the_way_out"}
        sizes = []
        sizes.append("")
        
        for size in sizes:
            part = copy.deepcopy(default_empty)
            part.update(current_item)            
            part["size"] = size
            parts.append(copy.deepcopy(part))

        
            


   
    oomp.add_parts(parts, **kwargs)
    