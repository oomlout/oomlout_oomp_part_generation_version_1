import oomp
import oom_git

def main(**kwargs):
    filter = kwargs.get("filter", "")
    

    yanml_file_folder = r"C:\gh\oomp_part_generation_1_web_interface\parts_source"

    parts = []

    
    
    
    make_files = kwargs.get("make_files", True)

    #load all the yaml files in 
    import glob
    import os
    import yaml
    yaml_files = glob.glob(os.path.join(yanml_file_folder, "*.yaml"))
    for yaml_file in yaml_files:
        with open(yaml_file, 'r') as f:
            yaml_parts = yaml.safe_load(f)            
            parts.append(yaml_parts)

    
    oomp.add_parts(parts, make_files=make_files)

    oomp.save_parts()
    oomp.save_parts_to_individual_yaml_files()



    #oom_git.push_to_git(comment=comment)

if __name__ == "__main__":
    kwargs = {}

    filter = ""

    kwargs["filter"] = filter
    main(**kwargs)
