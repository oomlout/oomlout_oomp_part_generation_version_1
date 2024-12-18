import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    for part_id in oomp.parts:
        part = oomp.parts[part_id]
        pass

        category_items = []

        part_details = {}
        classification = part.get("classification", "")        
        typ = part.get("type", "")
        size = part.get("size", "")
        color = part.get("color", "")        

        part_details["classification"] = ""
        part_details["type"] = ""
        part_details["size"] = ""    
        part_details["color"] = ""
        part_details["description_main"] = ""
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["part_number_exact"] = ""
        
        
        
        part_details["classification"] = "category"
        part_details["type"] = classification
        description = f"category_{classification}"
        short_name = description.replace("_","").capitalize()
        part_details["description"] = description
        part_details["short_name"] = short_name
        category_items.append(copy.deepcopy(part_details))

        part_details["size"] = typ
        description = f"category_{classification}"
        short_name = description.replace("_","").capitalize()
        part_details["description"] = description
        part_details["short_name"] = short_name
        category_items.append(copy.deepcopy(part_details))
        

        part_details["color"] = size
        description = f"category_{classification}"
        short_name = description.replace("_","").capitalize()
        part_details["description"] = description
        part_details["short_name"] = short_name
        category_items.append(copy.deepcopy(part_details))

        #part_details["description_main"] = color
        #description = f"category_{classification}"
        #short_name = description.replace("_","").capitalize()
        #part_details["description"] = description
        #part_details["short_name"] = short_name
        #category_items.append(copy.deepcopy(part_details))

        
        
        #check if a part details where classification, type size and color and description main mathc if unique add to list
        for category_item in category_items:
            unique = True
            for part in parts:
                
                if part["classification"] == category_item["classification"]:
                    if part["type"] == category_item["type"]:
                        if part["size"] == category_item["size"]:
                            if part["color"] == category_item["color"]:
                                #if part["description_main"] == category_item["description_main"]:
                                unique = False  
            if unique:
                parts.append(category_item)

    #for each part add varius description_extra
    extras = []
    extras.append("tote")
    extras.append("cubby_box")
    #extras.append("cube_box_cardboard")
    #extras.append("takeaway_container_1000_ml")
    #extras.append("takeaway_container_500_ml")
    #extras.append("takeaway_container_round")
    #extras.append("shelf")
    #extras.append("")
    parts2 = copy.deepcopy(parts)
    for part in parts:
        parts2.append(part)
        for extra in extras:
            part_details = copy.deepcopy(part)
            part_details["description_extra"] = extra
            parts2.append(part_details)

    parts = parts2
                

        



    oomp.add_parts(parts, **kwargs)
    