import os
import subprocess
import time



def main(**kwargs):
    # Store the start time 
    start_time = time.time()

    # Run the creation process
    if True:
        pass
        os.chdir('C:\\gh\\oomlout_oomp_part_generation_version_1')
        subprocess.run(['python', 'action_setup_full.py'])
        subprocess.run(['git', 'add', '*'])
        subprocess.run(['git', 'commit', '-a', '-m', 'Full run through'])
        subprocess.run(['git', 'push'])


    #delete the old oomp
    if True:
        print('Deleting old oomp')
        directory_to_delete = []
        directory_to_delete.append('z:\\oomlout_oomp_current_version_messy')
        directory_to_delete.append('z:\\oomlout_oomp_version_1_only_yaml')
        delete_directory(directory_to_delete)

        


    #run only_yaml
    if True:
        #add  Z:\oomlout_oomp_current_version_messy to python path
        repo_name = 'oomlout_oomp_version_1_only_yaml'
        repo_url = f"https://github.com/oomlout/{repo_name}"
        directory_current = f'Z:\\{repo_name}'
        
        #git clone
        if True:
            os.chdir('Z:\\')
            subprocess.run(['git', 'clone', repo_url])
        
        #delete parts directory
        if True:
            directory_parts = f"{directory_current}\\parts"
            delete_directory(directory_parts)

        #run the build
        if True:
            os.chdir(directory_current)
            subprocess.run(['python', 'action_build_oomp.py'])

        #commit
        if True:
            subprocess.run(['git', 'add', '*'])
            subprocess.run(['git', 'commit', '-a', '-m', 'Full run through'])
            subprocess.run(['git', 'push'])
            
        #delete the directory
        if True:    
            delete_directory(directory_current)
            pass


    #run messy
    if True:
        #add  Z:\oomlout_oomp_current_version_messy to python path
        repo_name = 'oomlout_oomp_version_1_messy'
        repo_url = f"https://github.com/oomlout/{repo_name}"
        directory_current = f'Z:\\{repo_name}'
        
        
        #git clone
        if True:
            os.chdir('Z:\\')
            subprocess.run(['git', 'clone', repo_url])

        #delete parts directory
        if True:
            directory_parts = f"{directory_current}\\parts"
            delete_directory(directory_parts)
        
        #run the build
        if True:
            os.chdir(directory_current)
            subprocess.run(['python', 'action_build_oomp.py'])

        #commit
        if True:
            subprocess.run(['git', 'add', '*'])
            subprocess.run(['git', 'commit', '-a', '-m', 'Full run through'])
            subprocess.run(['git', 'push'])


    # Store the end time
    end_time = time.time()

    # Calculate and print the elapsed time
    elapsed_time = end_time - start_time
    hours = int(elapsed_time // 3600)
    minutes = int(elapsed_time - hours * 3600) // 60
    seconds = int(elapsed_time - hours * 3600 - minutes * 60)

    print(f'Elapsed time: {hours} hours, {minutes} minutes, {seconds} seconds')

import shutil
import os
import subprocess
import time

def delete_directory(directory_to_delete):
    # If not an array, make it one
    if not isinstance(directory_to_delete, list):
        directory_to_delete = [directory_to_delete]
    for directory in directory_to_delete:
        try:
            print(f'Deleting {directory}')
            # Delete directory and all files and subdirectories within using os.system in Windows
            result = os.system(f'rmdir /s /q {directory}')
            if result != 0:
                raise Exception(f'Failed to delete {directory}')
        except Exception as e:
            print(e)
            try:
                shutil.rmtree(directory)
            except Exception as shutil_error:
                print(f'Failed to delete {directory} using shutil: {shutil_error}')


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)