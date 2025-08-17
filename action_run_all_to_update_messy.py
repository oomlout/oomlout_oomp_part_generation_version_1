import os
import subprocess
import time



def main(**kwargs):

    mode = 'full'
    #mode = 'fast'

    filt = ""
    filt = "warehouse"

    repo_names = {}
    current_names = []
    current_names.append('oomlout_oomp_version_1_only_yaml')
    current_names.append('oomlout_oomp_current_version_messy')    
    repo_names['full'] = current_names

    current_names = []
    current_names.append('oomlout_oomp_version_1_test_fast_only_yaml')
    current_names.append('oomlout_oomp_version_1_test_fast_messy')
    repo_names['fast'] = current_names

    all_repos = []
    for key in repo_names:
        all_repos += repo_names[key]
    repo_names['all'] = all_repos




    # Store the start time 
    start_time = time.time()

    # Run the creation process skip of going fast
    if True and mode == 'full':
        pass
        os.chdir('C:\\gh\\oomlout_oomp_part_generation_version_1')
        if filt == "":
            print('Running full setup without filter')
            subprocess.run(['python', 'action_setup_full.py'])
        else:
            print(f'Running full setup with filter: {filt}')
            subprocess.run(['python', 'action_setup_full.py', '-f', filt])
        subprocess.run(['git', 'add', '*'])
        subprocess.run(['git', 'commit', '-a', '-m', 'Full run through'])
        subprocess.run(['git', 'push'])


    #delete the old oomp
    if True:
        print('Deleting old oomp')
        #directory_to_delete = []
        #directory_to_delete.append('z:\\oomlout_oomp_current_version_messy')
        #directory_to_delete.append('z:\\oomlout_oomp_version_1_only_yaml')
        directory_to_delete = []
        for repo_name in all_repos:
            directory_to_delete.append(f'z:\\{repo_name}')  
        delete_directory(directory_to_delete)

        


    #run only_yaml
    if True:
        #add  Z:\oomlout_oomp_current_version_messy to python path
        if mode == 'full':
            repo_name = 'oomlout_oomp_version_1_only_yaml'
        elif mode == 'fast':
            repo_name = 'oomlout_oomp_version_1_test_fast_only_yaml'

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
            if filt == "":
                print('Running build without filter')
                os.chdir(directory_current)
                subprocess.run(['python', 'action_build_oomp.py'])
            else:
                print(f'Running build with filter: {filt}')
                os.chdir(directory_current)
                subprocess.run(['python', 'action_build_oomp.py', '-f', filt])

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
        if mode == 'full':
            repo_name = 'oomlout_oomp_version_1_messy'
        elif mode == 'fast':
            repo_name = 'oomlout_oomp_version_1_test_fast_messy'
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
        #if directory exists
        if not os.path.exists(directory):
            print(f'{directory} does not exist')
        else:
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

            # remvove empty directory
            if not os.path.exists(directory):
                    print(f'{directory} does not exist')
            else:
                print(f'Waiting 20 seconds before trying to remove empty directory {directory}')
                time.sleep(20)
                try:
                    os.rmdir(directory)
                except Exception as e:
                    #try os.system
                    command = f'rmdir /s /q {directory}'
                    print(f'Running command: {command}')
                    result = os.system(command)
                    if result != 0:
                        print(f'Failed to remove empty directory {directory}')
                        pass#time.sleep(30)
            


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)