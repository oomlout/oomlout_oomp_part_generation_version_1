REM 
REM NO LONGER USED
REM




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

