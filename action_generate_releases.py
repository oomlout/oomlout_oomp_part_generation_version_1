import shutil
import os


types = {}
types[""] = {}
types[""]["files"] = ["working.yaml", "working.json"]
types["_image"] = {}
types["_image"]["files"] = ["working.jpg"]

def main(**kwargs):
    releases = {"electronic", "hardware"}
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
                            #print(f"copying {file_full_source} to {file_full_output}")

                
        





if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)