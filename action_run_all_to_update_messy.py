import os
import subprocess
import time

# Store the start time 
start_time = time.time()

# Run the full process
os.chdir(r'C:\gh\oomlout_oomp_part_generation_version_1')
subprocess.run(['python', 'action_setup_full.py'])
subprocess.run(['git', 'add', '*'])
subprocess.run(['git', 'commit', '-a', '-m', 'Full run through'])
subprocess.run(['git', 'push'])





#add  Z:\oomlout_oomp_current_version_messy to python path
os.chdir(r'Z:\oomlout_oomp_version_1_messy')
subprocess.run(['python', 'action_build_oomp.py'])

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

"""
REM store the start time
set start_time=%time%
REM run the full process
cd C:\gh\oomlout_oomp_part_generation_version_1
python action_setup_full.py
git add *
git commit -a -m "Full run through"
git push
z:
cd Z:\oomlout_oomp_current_version_messy
python action_build_oomp.py
git add *
git commit -a -m "Full run through"
git push
REM store the end time
set end_time=%time%
REM subtract end time from start time
set /a elapsed_time=%end_time%-%start_time%
REM print the elapsed time
echo %elapsed_time%
"""
