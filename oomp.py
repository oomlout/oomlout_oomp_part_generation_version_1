
import oomp_create_parts
import oomp_kicad_footprint
import oomp_kicad_symbol
import oomp_short_code
import oomp_short_name

import oomp_distributors
import oomp_manufacturers
import oomp_packaging
import oomp_extra_details

import os
import oom_markdown
import oom_git

import copy

parts = {}
parts_md5 = {}
parts_md5_5 = {}
parts_md5_6 = {}
parts_md5_6_alpha = {}
parts_md5_10 = {}
parts_short_code = {}




names_of_main_elements = ["classification", "type", "size", "color", "description_main", "description_extra", "manufacturer", "part_number"]


def clone_data_files():
    repo_list = []
    repo_list.append("https://github.com/oomlout/oomlout_oomp_footprint_bot")
    repo_list.append("https://github.com/oomlout/oomlout_oomp_symbol_bot")
    repo_list.append("https://github.com/oomlout/oomlout_oomp_project_bot")

    #if tmp/ doesn't exist create it
    
    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    for repo in repo_list:
        #clone repo using os.system to tmp/repo_name
        print(f"cloning {repo}")
        
        repo_name = repo.split('/')[-1] 
        directory = "tmp"     
        oom_git.clone(repo=repo, directory=directory)
        oom_git.pull(directory=directory)




def load_parts(**kwargs):
    global add_part_filter
    from_yaml = kwargs.get("from_yaml", True)
    from_pickle = kwargs.get("from_pickle", False)
    filter = kwargs.get("filter", "")
    add_part_filter = filter
    if from_pickle:
        print ("loading parts from pickle")
        oomp_create_parts.load_parts_from_pickle(**kwargs)
        #load extra dicts
        load_extra_dicts()
    elif from_yaml:
        print ("loading parts from yaml")
        oomp_create_parts.load_parts_from_yaml(**kwargs)
    else:
        print ("loading parts from module")
        oomp_create_parts.load_parts(**kwargs)
        
def load_extra_dicts():
    global parts_md5
    global parts_md5_5
    global parts_md5_6
    global parts_md5_6_alpha
    global parts_md5_10
    global parts_short_code
    for part in parts:
        part = part.lower()
        parts_md5[parts[part]["md5"]] = parts[part]
        parts_md5_5[parts[part]["md5_5"]] = parts[part]
        parts_md5_6[parts[part]["md5_6"]] = parts[part]
        parts_md5_6_alpha[parts[part]["md5_6_alpha"]] = parts[part]
        parts_md5_10[parts[part]["md5_10"]] = parts[part]
        parts_short_code[parts[part]["short_code"]] = parts[part]


def save_parts(**kwargs):
    oomp_create_parts.save_parts_to_yaml(**kwargs)
    oomp_create_parts.save_parts_to_pickle(**kwargs)

def save_parts_to_individual_yaml_files(**kwargs):
    oomp_create_parts.save_parts_to_individual_yaml_files(**kwargs)

def create_parts_readme_old():
    print("creating parts readme")
    #create a file called parts_readme.md that links to all the parts in the parts directory
    readme = ""
    readme += "# Parts\n"
    readme += "\n"
    for part in parts:
        readme += f"[{parts[part]['name']}](parts/{parts[part]['id']}/readme.md)\n"
    with open("readme_parts.md", "w") as outfile:
        outfile.write(readme)

    


def add_parts(parts,**kwargs):
    parts_full_list = []
    #expand the parts list into parts_processed, make this a list of permutations of the part using itertools
    import itertools

    # Initialize an empty dictionary for lists
    my_dict_lists = {}

    # Convert all the dictionary values to lists but only use the keys in names_of_main_elements
    
    for part in parts:

        #test if any elelment in the part is a list
        list_in_part = False
        # get all the dict values that aren't in names_of_main_elements 
        not_main_elements = {}
        for key, value in part.items():
            if key not in names_of_main_elements:
                not_main_elements[key] = (part[key])
        
        for key, value in part.items():
            if isinstance(value, list):
                list_in_part = True
        if list_in_part:
            for key, value in part.items():
                #only check if the key is in names_of_main_elements
                if key in names_of_main_elements:
                    # Check if the value is a string
                    if isinstance(value, str):
                        # If it is, convert it to a list and add to the new dictionary
                        my_dict_lists[key] = [value]
                    else:
                        # If it's not a string, we assume it's a list and add it to the new dictionary as is
                        my_dict_lists[key] = value

            # Prepare a list to hold the combinations
            combinations = []

            # The itertools.product function takes any number of arguments, 
            # but we have a list of lists, so we need to "unpack" this list 
            # into separate arguments using the * operator.
            # This will generate a Cartesian product of the given lists,
            # i.e., all possible combinations of the elements in the lists.
            for combo in itertools.product(*my_dict_lists.values()):
                # Add each combination to our list of combinations
                combinations.append(combo)

            # Print all combinations
            for combo in combinations:
                part_full = {}
                part_full["classification"] = combo[0]
                part_full["type"] = combo[1]
                part_full["size"] = combo[2]
                part_full["color"] = combo[3]
                part_full["description_main"] = combo[4]
                part_full["description_extra"] = combo[5]
                part_full["manufacturer"] = combo[6]
                part_full["part_number"] = combo[7]
                part_full["not_main_elements"] = not_main_elements
                part_full.update(kwargs)    
                parts_full_list.append(part_full)
                #add_part(classification=combo[0], type=combo[1], size=combo[2], color=combo[3], description_main=combo[4], description_extra=combo[5], manufacturer=combo[6], part_number=combo[7], not_main_elements=not_main_elements, **kwargs)
        else:
            part_full = {}
            part_full["classification"] = part["classification"]
            part_full["type"] = part["type"]
            part_full["size"] = part["size"]
            part_full["color"] = part["color"]
            part_full["description_main"] = part["description_main"]
            part_full["description_extra"] = part["description_extra"]
            part_full["manufacturer"] = part["manufacturer"]
            part_full["part_number"] = part["part_number"]
            part_full["not_main_elements"] = not_main_elements
            part_full.update(kwargs)  
            parts_full_list.append(part_full)
            #add_part(classification=part["classification"], type=part["type"], size=part["size"], color=part["color"], description_main=part["description_main"], description_extra=part["description_extra"], manufacturer=part["manufacturer"], part_number=part["part_number"], not_main_elements=not_main_elements, **kwargs)

    #go through each item in parts_full_list and run it through add_part but use threading on 6 cores
    import threading
    threads = []
    for part in parts_full_list:
        thread = threading.Thread(target=add_part, kwargs=part)
        threads.append(thread)
        thread.start()




add_part_filter = ""

cnt = 1

def add_part(**kwargs):
    global cnt
    global add_part_filter
    make_files = kwargs.get("make_files", True)

    #pop out the not_main_elements from kwargs
    not_main_elements = kwargs.pop("not_main_elements")
    #add them back as regular keys
    for key, value in not_main_elements.items():
        kwargs[key] = value

    ## get id
    import copy
    add_part_filters = copy.deepcopy(add_part_filter)
    if not isinstance(add_part_filters, list):
        add_part_filters = [add_part_filters] 
    id = get_id(**kwargs)
    for add_part_filter in add_part_filters:
        if add_part_filter in id:
            
            
            
            ## add part to dict
            #print("    adding part " + id)
            

            #add formated taxonomy
            types = ["classification", "type", "size", "color", "description_main", "description_extra", "manufacturer", "part_number"]
            formats = ["upper","capital","first_letter","first_letter_upper"]
            for typ in types:
                for format in formats:
                    kwargs[f"{typ}_{format}"] = kwargs[typ]
                    first_letter = ""
                    if kwargs[typ] != "":
                        first_letter = kwargs[typ][0]
                    if format == "upper":
                        kwargs[f"{typ}_{format}"] = kwargs[typ].upper()
                    if format == "capital":
                        
                        value = kwargs[typ].replace("_", " ").title()
                        value = value.replace(" X ", " x ")
                        value = value.replace("Mm", "mm")
                        for i in range(1,10):
                            for j in range(1,10):
                                src_value = f"{i} {j}"
                                dst_value = f"{i}.{j}"
                                value = value.replace(src_value, dst_value)
                        kwargs[f"{typ}_{format}"] = value
                    if format == "first_letter":
                        kwargs[f"{typ}_{format}"] = first_letter
                    if format == "first_letter_upper":
                        kwargs[f"{typ}_{format}"] = first_letter.upper()


            #add id as a keyed item to kwargs
            kwargs["id"] = id
            clas = kwargs.get("classification","none")
            ###add_id_start
            id_no_class = id.replace(f"{clas}_","")        
            kwargs["id_no_class"] = id_no_class
            typ = kwargs.get("type","none")
            id_no_type = id_no_class.replace(f"{typ}_","")        
            kwargs["id_no_type"] = id_no_type
            siz = kwargs.get("size","none")
            id_no_size = id_no_type.replace(f"{siz}_","")
            kwargs["id_no_size"] = id_no_size

            kwargs["oomp_key"] = f'oomp_{id}'
            github_link = f"https://github.com/oomlout/oomlout_oomp_version_1_messy/tree/main/parts/{id}" 
            kwargs["link_github"] = github_link
            kwargs["link_main"] = github_link
            kwargs["link_redirect"] = github_link

            
            #add the directory
            kwargs["directory"] = f'parts/{id}'

            ## add_id_end

            ## add_name_start

            #add name, the name is the id with proper capitalization and _ replaced with ' '
            kwargs["name"] = id.replace("_", " ").title()
            name_no_class = id_no_class.replace("_", " ").title()
            kwargs["name_no_class"] = name_no_class
            name_no_type = id_no_type.replace("_", " ").title()
            kwargs["name_no_type"] = name_no_type
            name_no_size = id_no_size.replace("_", " ").title()
            kwargs["name_no_size"] = name_no_size

            ## add_name_end

            #add short code from a get_short_code function
            kwargs["short_code"] = oomp_short_code.get_short_code(**kwargs)
            kwargs["short_code_upper"] = kwargs["short_code"].upper()
            parts_short_code[kwargs["short_code"]] = kwargs["id"]
            
            # add short name from a get_short_name function
            short_name = oomp_short_name.get_short_name(**kwargs)
            if short_name != "":
                kwargs["short_name"] = short_name


            #add distributors from a function get_distributors in oomp_distributors.py
            kwargs = oomp_distributors.get_distributors(**kwargs)

            kwargs = oomp_manufacturers.get_manufacturers(**kwargs)

            kwargs = oomp_packaging.get_packaging(**kwargs)

            kwargs = oomp_extra_details.get_extra_details(**kwargs)

            # add_md5_start

            #add a md5 hash of the id as a keyed item to kwargs
            import hashlib
            kwargs["md5"] = hashlib.md5(id.encode()).hexdigest()
            #trim md5 to 6 and add it as md5_6
            kwargs["md5_5"] = kwargs["md5"][0:5]
            kwargs["md5_5_upper"] = kwargs["md5"][0:5].upper()
            #add to md5_5 dict
            parts_md5_5[kwargs["md5_5"]] = id
            md5_6 = kwargs["md5"][0:6]
            kwargs["md5_6"] = md5_6
            kwargs["md5_6_upper"] = kwargs["md5_6"].upper()

            md5_6_alpha = hex_to_base36(kwargs["md5_6"])
            kwargs["md5_6_alpha"] = md5_6_alpha
            kwargs["md5_6_alpha_upper"] = kwargs["md5_6_alpha"].upper()
            
            
            parts_md5_6[kwargs["md5_6"]] = id
            kwargs["md5_10"] = kwargs["md5"][0:10]
            kwargs["md5_10_upper"] = kwargs["md5_10"].upper()
            parts_md5_10[kwargs["md5_10"]] = id
            
            ###### add_oomp_moji start

            # oomp_word
            import oomp_word
            oomp_word_value = oomp_word.get_oomp_word(md5_6, style="string")
            kwargs["oomp_word"] = oomp_word_value
            kwargs["oomp_word_list"] = oomp_word.get_oomp_word(md5_6, style="list")
            kwargs["oomp_word_emoji"] = oomp_word.get_oomp_word(md5_6, style="emoji")
            kwargs["oomp_word_emoji_list"] = oomp_word.get_oomp_word(md5_6, style="emoji_list")

            ##### add_oomp_moji enf

            ### add useful name variants
            #      classification
            #      type
            typ = kwargs["type"]
            type_first_letter = ""
            if typ != "":
                type_first_letter = kwargs["type"][0]
            kwargs["type_first_letter"] = type_first_letter
            kwargs["type_first_letter_upper"] = type_first_letter.upper()
            kwargs["type_upper"] = kwargs["type"].upper()
            kwargs["type_capital"] = kwargs["type"].replace("_", " ").title()
            #      size
            #remove all charachters that aren't numbers
            size_only_numbers = ''.join(i for i in kwargs["size"] if i.isdigit())
            kwargs["size_only_numbers"] = size_only_numbers
            size_only_numbers_no_zeros = size_only_numbers.lstrip("0")
            kwargs["size_only_numbers_no_zeros"] = str(size_only_numbers_no_zeros).replace("0","")
            #      color
            color = kwargs["color"]
            kwargs["color_upper"] = color.upper()
            #first letter
            color_first_letter = ""
            if color != "":
                color_first_letter = color[0]
            kwargs["color_first_letter"] = color_first_letter
            kwargs["color_first_letter_upper"] = color_first_letter.upper()
            
            #      description_main
            working_desc = kwargs["description_main"]
            working_desc = working_desc.replace("2d54","")
            description_only_numbers = ''.join(i for i in kwargs["description_main"] if i.isdigit())
            kwargs["description_only_numbers"] = description_only_numbers
            description_only_numbers_short = ""
            if description_only_numbers == "":
                description_only_numbers = 0
            don = int(description_only_numbers)
            if don < 1000:
                description_only_numbers_short = str(don)
            elif don < 10000:
                w = str(round(don) / 1000)
                w =w.replace(".", "")
                if w[1] != "0":
                    description_only_numbers_short = w[0] + "k" + w[1]
                    pass
                else:
                    description_only_numbers_short = w[0] + "k"
                    pass
            elif don < 100000:
                w = str(round(don / 1000))
                description_only_numbers_short = w + "k"
                pass
            elif don < 1000000:
                w = str(round(don / 1000))
                description_only_numbers_short = w + "k"
                pass
            else:
                w = str(round(don) / 100000)
                w =w.replace(".", "")
                if w[1] != "0":
                    description_only_numbers_short = w[0] + "M" + w[1]
                    pass
                else:
                    description_only_numbers_short = w[0] + "M"
                    pass            
            
            replacements = []
            replacements.append(["nano_farad", "nf"])
            replacements.append(["micro_farad", "uf"])
            replacements.append(["pico_farad", "pf"])
            replacement_extra = ""
            for replacement in replacements:
                if replacement[0] in id:
                    replacement_extra = replacement[1]

            if description_only_numbers_short == 0 or description_only_numbers_short == "0" or description_only_numbers_short == "":
                description_only_numbers_short = " "
            
            description_only_numbers_short += replacement_extra
            kwargs["description_only_numbers_short"] = description_only_numbers_short

            name_no_size_short_number = kwargs["name_no_size"]
            if description_only_numbers_short != " ":            
                name_no_size_short_number = name_no_size_short_number.replace(description_only_numbers, description_only_numbers_short)        
            kwargs["name_no_size_short"] = name_no_size_short_number

            
            
            description_or_color = f"{color_first_letter.upper()}{description_only_numbers_short}"
            kwargs["description_or_color"] = description_or_color
            kwargs["description_or_color_upper"] = description_or_color.upper()
            
            #      description_extra




            kwargs = get_markdown_summaries(**kwargs)

            pass

            ## print part nicely indented by six spaces
            ### print("      " + str(kwargs).replace(", ", ",\n      "))

            if make_files:
                ######### file stuff
                directory_parts = "parts"
                if make_files != True:
                    directory_parts = make_files

                ## make a directory in /parts for the part the name is its id
                import os
                folder = f"{directory_parts}/" + id
                if not os.path.exists(folder):
                    try:
                        os.makedirs(folder)
                    except Exception as e:
                        print(f"Error creating directory {folder}: {e}")
                        return
                
                ## write the part working in json to the directory name the file working.json
                import json
                with open(f"{directory_parts}/" + id + "/working.json", "w") as outfile:
                    pass
                    #json.dump(kwargs, outfile, indent=4)
                ## write the part working in yaml to the directory name the file working.json
                
                file_types = ["datasheet.pdf", "image.jpg", "image_reference.jpg"]
                #for each file type look in the src directory for a file named (id)_(file_type) if it exists copy it to the parts directory as the file_type name
                for file_type in file_types:
                    import os.path
                    if os.path.isfile("src/" + id + "_" + file_type):
                        import shutil
                        shutil.copy(f"src/" + id + "_" + file_type, f"{directory_parts}/" + id + "/" + file_type)

            

                ### eda stuff
                kwargs = oomp_kicad_footprint.get_footprints(**kwargs)
                kwargs = oomp_kicad_symbol.get_symbols(**kwargs)

                
                import yaml
                import copy
                p2 = copy.deepcopy(kwargs)
                p2.pop("make_files", None)
                p2.pop("counter", None)

                with open(f"{directory_parts}/" + id + "/working.yaml", "w") as outfile:
                    yaml.dump(p2, outfile, indent=4)


            parts[id] = kwargs
        else:
            print("    skipping part " + id)
            pass
    cnt += 1
    if cnt % 100 == 0:
        print(f".", end="")

def hex_to_base36(hex_value):
    # Convert the hex value to an integer
    decimal_value = int(hex_value, 16)

    # Encode the integer as base36
    base36_value = ''
    while decimal_value > 0:
        decimal_value, remainder = divmod(decimal_value, 36)
        base36_digit = '0123456789abcdefghijklmnopqrstuvwxyz'[remainder]
        base36_value = base36_digit + base36_value

    return base36_value


def get_id(**kwargs):
    #concate all the elements in kwargs from names_of_main_elements with '_' and return the string if the element isn't '' include it
    id = ""
    for name in names_of_main_elements:
        if kwargs[name] != "":
            id += kwargs[name] + "_"
    #remove the trailing '_'
    id = id[:-1]
    return id


def search_for_matching_parts(**kwargs):    
    matches = kwargs.get("matches", {})
    return_value = []
    if matches != {}:
        for part_id in parts:
            part = parts[part_id]
            match = True
            for key, value in matches.items():
                if part[key] != value:
                    match = False
            if match:
                #print(part_id)
                return_value.append(part_id)
    return return_value


def search_for_part_id(search,**kwargs):
    # test if in parts
    search = search.replace("oomp_","")
    return_value = parts.get(search, "")
    if return_value == "":
        #grab from short code
        for part_id in parts:
            if parts[part_id]["short_code"] == search:
                return_value = parts[part_id]
    
    try:
        return_value = return_value.get("id","")
    except:
        print(f"error getting id for {search}")
        return_value = ""
    return return_value


def generate_readme_old(**kwargs):
    #generate a readme.md file for the part
    readme = ""
    readme += "# " + kwargs["name"] + "\n"
    readme += "\n"
    readme += "## Description\n"
    readme += "\n"
    readme += "## Properties\n"
    readme += "\n"
    
    ## datasheet
    ### add datasheet link if datasheet.pdf is a file in the parts directory
    import os.path
    if os.path.isfile("parts/" + kwargs["id"] + "/datasheet.pdf"):
        readme += "\n"
        readme += "![Datasheet](datasheet.pdf)\n"
    readme += "\n"
    
    ## images 
    readme += "## Image\n"
    readme += "\n"
    images = ["image.jpg", "image_reference.jpg"]
    ### add images if any of the image files exist
    for image in images:
        if os.path.isfile("parts/" + kwargs["id"] + "/" + image):
            readme += "\n"
            #add image use an f string
            readme += f"![{kwargs['name']} image]({image})\n"
            readme += "\n"
    
    ## add all values in the dict to a table
    readme += "\n"
    readme += "## Values\n"
    readme += "\n"
    readme += "| Key | Value |\n"
    readme += "| --- | --- |\n"
    for key, value in kwargs.items():
        #if the value is a list add each value on a new line, also handle it if its a dict also handle if its a nested list or dict
        if isinstance(value, list):
            value_string = ""
            for item in value:
                #add a way to unwrap nested lists and dicts
                if isinstance(item, list):
                    value_string += "<br>"
                    for subitem in item:
                        value_string += f"  - {subitem}\n"
                elif isinstance(item, dict):
                    value_string += "<br>"
                    for subitem in item:
                        value_string += f"  - {subitem}: {item[subitem]}<br>"
                else:
                    value_string += f"  - {item}<br>"
                
        readme += "| " + key + " | " + str(value) + " |\n"
    readme += "\n"  

    ## add notes
    readme += "## Notes\n"
    readme += "\n"
    return readme



def generate_readme(**kwargs):
    
    overwrite = kwargs.get("overwrite",False)
    filename = kwargs.get("filename",None)
    #get directory from filename
    directory = os.path.dirname(filename) 
    readme_file = os.path.join(directory,"readme.md")
    print(f"generating readme for {directory}")
    #create a deep copy of kwargs
    import copy
    p2 = copy.deepcopy(kwargs)
    p2["directory"] = directory
    readme = get_readme(**p2)

    #write readme file
    #as unicode
    with open(readme_file, 'w', encoding='utf-8') as text_file:
        text_file.write(readme)


def get_readme(**kwargs):
    directory = kwargs.get("directory","none")

    
    import copy
    p2 = copy.deepcopy(kwargs)
    yaml_file = p2.get("directory", "none") + "/working.yaml"
    if os.path.exists(yaml_file):
        import yaml
        with open(yaml_file, 'r') as stream:
            try:
                yaml_dict = yaml.load(stream, Loader=yaml.FullLoader)
            except:
                print("yaml file error")
                readme += "yaml file error"
                return readme
        #if yaml dict is a list then take the first element
        if isinstance(yaml_dict, list):
            yaml_dict = yaml_dict[0]

        #add yaml dict to kwargs
        p2.update(yaml_dict=yaml_dict)

        readme = "# OOMP Part  \n"
        p2["readme"] = readme
        readme += get_intro(**p2)
        ###### part
        p2["readme"] = readme
        readme += get_part(**p2)
        ###### symbol
        p2["readme"] = readme
        readme += get_symbol(**p2)
        ###### footprint
        p2["readme"] = readme
        readme += get_footprint(**p2)
        ###### images
        p2["readme"] = readme
        readme += get_images(**p2)



        return readme
    else:
        print( "no yaml file found")
        readme += "no yaml file found"
        return readme

def get_intro(**kwargs):
    yaml_dict = kwargs.get("yaml_dict",{})
    yd = yaml_dict
    ###### introduction
    name = yd.get("name","none")
    oomp_key = yd.get("oomp_key","none")
    readme = ""
    readme += f'## {name}  \n'
    readme += f'  \n'
    readme += f'oomp key: {oomp_key}  \n'
    readme += f'  \n'
    
    return readme

def get_part(**kwargs):
    yaml_dict = kwargs.get("yaml_dict",{})
    yd = yaml_dict
    
    oomp_key = yd.get("oomp_key","none")
    short_code = yd.get("short_code","none")
    name = yd.get("name","none")
    id = yd.get("id","none")
    classification = yd.get("classification","none")
    typ = yd.get("type","none")
    size = yd.get("size","none")
    color = yd.get("color","none")
    description_main = yd.get("description_main","none")
    description_extra = yd.get("description_extra","none")
    manufacturer = yd.get("manufacturer","none")
    part_number = yd.get("part_number","none")
    md5_10 = yd.get("md5_10","none")
    md5_5 = yd.get("md5_5","none")
    md5 = yd.get("md5","none")

    readme = "### Part Details  \n"
    ###### board
    image_link = oom_markdown.get_link_image_scale(image="working.jpg",resolution="600")
    readme += f'  \n'
    readme += f'{image_link}  \n'
    #oom_kicad.get_footprint_pin_names(filename=footprint_filename)
    table_array = []
    readme += f'  \n'
    readme += f'#### Important Bits  \n'
    table_array.append(["name", name])
    table_array.append(["full id", id])
    table_array.append(["short code", short_code])   
    table_array.append(["short link<br>(not yet working)", f'http://oom.lt/{short_code}<br>http://oom.lt/{md5_5}'])   
    table_array.append(["oomp key", oomp_key])
    table_array.append(["md5_5", md5_5])
    table_array.append(["md5_10", md5_10])
    table_array.append(["md5", md5])
    

    readme+=oom_markdown.get_table(data=table_array)
    readme += f'#### ID Composition  \n'
    table_array = []
    table_array.append(["1 classification", classification])
    table_array.append(["2 type", typ])
    table_array.append(["3 size", size])
    table_array.append(["4 color", color])
    table_array.append(["5 description main", description_main])
    table_array.append(["6 description extra", description_extra])
    table_array.append(["7 manufacturer", manufacturer])
    table_array.append(["8 part number", part_number])
    readme+=oom_markdown.get_table(data=table_array)

    return readme

def get_symbol(**kwargs):
    yaml_dict = kwargs.get("yaml_dict",{})
    yd = yaml_dict
    
    readme = ""
    readme += f'### Symbol  \n'

    symbols = yd.get("symbol",[])
    for symbol in symbols:
        directory = symbol.get("directory","none")
        link = symbol.get("link","none")
        oomp_key = symbol.get("oomp_key","none")
        table_array = []
        table_array.append(["oomp_key", oomp_key])
        table_array.append(["link", link])
        table_array.append(["directory", directory])   
        readme += oom_markdown.get_table(data=table_array)
    return readme

def get_footprint(**kwargs):
    yaml_dict = kwargs.get("yaml_dict",{})
    yd = yaml_dict
    
    readme = ""
    readme += f'### Footprint  \n'

    symbols = yd.get("footprint",[])
    for symbol in symbols:
        directory = symbol.get("directory","none")
        link = symbol.get("link","none")
        oomp_key = symbol.get("oomp_key","none")
        table_array = []
        table_array.append(["oomp_key", oomp_key])
        table_array.append(["link", link])
        table_array.append(["directory", directory])   
        readme += oom_markdown.get_table(data=table_array)

    return readme

def get_images(**kwargs):
    
    directory = kwargs.get("directory","none")
    readme = "### Images  \n"

    #get all images in directory
    import glob
    images = glob.glob(directory + "\\*.png")
    images += glob.glob(directory + "\\*.jpg")
    images += glob.glob(directory + "\\*.jpeg")
    for image in images:
        #grab the filename split after the last _
        test = image.split("_")[-1]
        digit_test = test[1:3].isdigit()
        if not digit_test:
            just_filename = os.path.basename(image)
            image_link = oom_markdown.get_link_image_scale(image=just_filename)

            readme += f'  \n'
            readme += f'{image_link}  \n'





    return readme



def get_markdown_summaries(**kwargs):
    import oom_markdown
    id = kwargs.get("id","none")
    name = kwargs.get("name","none")
    github_link = kwargs.get("github_link","none")
    short_code = kwargs.get("short_code","none")

    distributors = kwargs.get("distributors",[])
    manufacturers = kwargs.get("manufacturers",[])

    pass
    """
    short code (link)"""

    short_link = oom_markdown.get_link(link=f"{github_link}",text=f"{short_code}")
    id_link = oom_markdown.get_link(link=f"{github_link}",text=f"{id}")
    name_link = oom_markdown.get_link(link=f"{github_link}",text=f"{name}")

    distributor_link = ""
    max_dist = 6
    if len(distributors) > 0:
        for x in range(min(len(distributors),max_dist)):
            distributor_1_name = distributors[x]["name"]
            distributor_1_link = distributors[x]['link']
            distributor_1_note = ""
            if "note" in distributors[x]:
                distributor_1_note = f"- {distributors[x]['note']['reason_short']}"
            distributor_1_part_number = distributors[x]['part_number']
            text = f"{distributor_1_name} - {distributor_1_part_number}{distributor_1_note}"
            distributor_link += oom_markdown.get_link(link=f"{distributor_1_link}",text=f"{text}<br>")
    if len(distributors) > max_dist:
        text += f"and {len(distributors)-max_dist} more"
        link = github_link
        distributor_link += oom_markdown.get_link(link=f"{link}",text=f"{text}<br>")

    ## do the same for manufacturers
    manufacturer_link = ""
    manufacturer_link_no_search = ""
    max_manu = 6
    if len(manufacturers) > 0:
        
        for x in range(min(len(manufacturers),max_dist)):
            manufacturer_1_name = manufacturers[x]["name"]
            manufacturer_1_link = manufacturers[x]['link']
            manufacturer_1_part_number = manufacturers[x]['part_number']
            manufacturer_1_note = ""
            if "note" in manufacturers[x]:
                manufacturer_1_note = f"- {manufacturers[x]['note']['reason_short']}"
            
            search_types = {}
            search_types["lcsc"] ={
                                    "name": "lcsc",
                                    "letter": "L",
                                    "search_link_front":"https://www.lcsc.com/search?q=",
                                    "search_link_back":"",
            }
            search_types["digikey"] ={
                                    "name": "digikey",
                                    "letter": "D",
                                    "search_link_front":"https://www.digikey.com/en/products?keywords=",
                                    "search_link_back":""
            }
            search_types["mouser"] ={
                                    "name": "mouser",
                                    "letter": "M",
                                    "search_link_front":"https://www.mouser.com/Search/Refine?Keyword=",
                                    "search_link_back":""
            }
            search_types["newark"] ={
                                    "name": "newark",
                                    "letter": "N",
                                    "search_link_front":"https://www.newark.com/search?st=",
                                    "search_link_back":"",
            }
            search_types["szlcsc"] ={
                                    "name": "szlcsc",
                                    "letter": "SZ",
                                    "search_link_front":"https://so.szlcsc.com/global.html?k=",
                                    "search_link_back":""
            }

            search_links = ""
            
            for search_type in search_types:
                text = f"({search_types[search_type]['letter']})"
                link = f"{search_types[search_type]['search_link_front']}{manufacturer_1_part_number}{search_types[search_type]['search_link_back']}"
                
                search_links += oom_markdown.get_link(link=f"{link}",text=f"{text}  ")

            text = f"{manufacturer_1_name} - {manufacturer_1_part_number}{manufacturer_1_note}"
            manufacturer_link += oom_markdown.get_link(link=f"{manufacturer_1_link}",text=f"{text}")            
            manufacturer_link += f" {search_links}<br>"
            
            manufacturer_link_no_search += oom_markdown.get_link(link=f"{manufacturer_1_link}",text=f"{text}")            
            
            

    if len(manufacturers) > max_dist:
        text += f"and {len(manufacturers)-max_dist} more"
        link = github_link
        manufacturer_link += oom_markdown.get_link(link=f"{link}",text=f"{text}<br>")






    markdown_full = f"{id_link}<br>{short_link}<br>{name_link}<br>{distributor_link}<br>{manufacturer_link}"
    markdown_short = f"{id_link}<br>{distributor_link}<br>{manufacturer_link_no_search}"
    
    

    kwargs["markdown_full"] = markdown_full
    kwargs["markdown_short"] = markdown_short


    return kwargs


    