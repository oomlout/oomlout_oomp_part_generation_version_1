import shutil
import os
import oom_git

types = {}
types[""] = {}
types[""]["files"] = ["working.yaml", "working.json", "base.yaml"]
types["_image"] = {}
types["_image"]["files"] = ["image.jpg","image_300.jpg","image_600.jpg","image_reference.jpg","image_reference_300.jpg","image_reference_600.jpg","drawing_300.png","drawing_600.png","dimension_300.png","dimension_600.png"]
types["_drawing"] = {}
types["_drawing"]["files"] = ["drawing.cdr","drawing.png","drawing.svg", "drawing.pdf", "dimension.cdr","dimension.png", "dimension.svg", "dimension.pdf"]
types["_three_d_model"] = {}
types["_three_d_model"]["files"] = ["working.stl","working.scad"]
types["_datasheet"] = {}
types["_datasheet"]["files"] = ["datasheet.pdf"]



def main(**kwargs):

    git = True

    releases = {"computer","electrical","electronic", "hardware", "mechanical", "oobb", "packaging", "storage", "tool"}
    releases = {"electronic"}
    directory_source = "parts"
    for typ_id in types:
        typ = types[typ_id]
        for release in releases:
            directory_output = f"outputs/oomp_base_{release}{typ_id}/parts"
            print(f"copying {release} to {directory_output}")
            #go through all directories in directory_source
            for directory in os.listdir(directory_source):
                directory_full_source = os.path.join(directory_source, directory)
                directory_full_output = os.path.join(directory_output, directory)
                #if the directory is not in the release, then delete it
                if directory.startswith(release):
                    #print(f"copying {directory}")
                    #make directory
                    if not os.path.exists(directory_full_output):
                        os.makedirs(directory_full_output)
                    files_to_copy = typ["files"]
                    for file in files_to_copy:
                        file_full_source = os.path.join(directory_full_source, file)
                        file_full_output = os.path.join(directory_full_output, file)
                        if os.path.exists(file_full_source):
                            if file_full_source.endswith("working.yaml"):
                                make_yaml_base(file_full_source, file_full_output)
                            shutil.copy(file_full_source, file_full_output)
                            print(f"copying {file_full_source} to {file_full_output}")
            typ_extra = ""
            if typ_id != "":
                typ_extra = f"{typ_id}"
            directory = f"outputs/oomp_base_{release}{typ_extra}"
            if git:
                try:
                    oom_git.push_to_git(directory=directory, comment=f"adding {release} {typ_id}")
                except Exception as e:
                    print(e)
                    print(f"could not push {directory}")
                except OSError as e:
                    print(e)
                    print(f"could not push {directory}")


def make_yaml_base(file_full_source, file_full_output):
    file_full_destination = file_full_output.replace("working.yaml", "base.yaml")
    filter_values = []
    filter_values.append("classification")
    filter_values.append("type")
    filter_values.append("size")
    filter_values.append("color")
    filter_values.append("description_main")
    filter_values.append("description_extra")
    filter_values.append("manufacturer")
    filter_values.append("part_number")
    filter_values.append("id")


    import yaml
    file_yaml = file_full_source
    with open(file_yaml, "r") as infile:
        part = yaml.load(infile, Loader=yaml.FullLoader)
    
    part_new = {}
    for filter_value in filter_values:
        part_new[filter_value] = part[filter_value]
    file_yaml = file_full_destination
    with open(file_yaml, "w") as outfile:
        print(f"writing base {file_yaml}")
        yaml.dump(part_new, outfile, indent=4)
    return part                
        





if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)