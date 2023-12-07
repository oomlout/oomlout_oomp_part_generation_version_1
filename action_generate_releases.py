import shutil
import os
import oom_git

types = {}
types[""] = {}
types[""]["files"] = ["working.yaml", "working.json"]
types["_image"] = {}
types["_image"]["files"] = ["image.jpg","image_reference.jpg"]
types["_drawing"] = {}
types["_drawing"]["files"] = ["drawing.cdr"]
types["_three_d_model"] = {}
types["_three_d_model"]["files"] = ["working.stl","working.scad"]
types["_datasheet"] = {}
types["_datasheet"]["files"] = ["datasheet.pdf"]

def main(**kwargs):

    git = True

    releases = {"electronic", "hardware", "packaging"}
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
                            shutil.copy(file_full_source, file_full_output)
                            print(f"copying {file_full_source} to {file_full_output}")
        typ_extra = ""
        if typ_id != "":
            typ_extra = f"{typ_id}"
        directory = f"outputs/oomp_base_{release}{typ_extra}"
        if git:
            try:
                oom_git.push_to_git(directory=directory, comment=f"adding {release} {typ_id}")
            except e as Exception:
                print(e)
                print(f"could not push {directory}")


                
        





if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)