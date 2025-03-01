import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    

    parts = []

    part_details = {}
    part_details['classification'] = 'electronic'
    part_details['type'] = 'breakout_board_sensor'
    part_details['size'] = 'accelerometer'
    part_details['color'] = 'bosch_bma400'
    part_details['description_main'] = ''
    part_details['description_extra'] = ''
    part_details['manufacturer'] = 'sparkfun'
    part_details['part_number'] = 'sen_21208'
    repo_name = 'oomlout_oomp_source_electronic_breakout_board_sensor_accelerometer_bosch_bma400_sparkfun_sen_21208'
    repo_name = repo_name[:99]
    part_details['oomp_repo'] = f'http://github.com/oomlout/{repo_name}'
    parts.append(part_details)

    part_details = {}
    part_details['classification'] = 'electronic'
    part_details['type'] = 'breakout_board_sensor'
    part_details['size'] = 'accelerometer'
    part_details['color'] = 'bosch_bma400'
    part_details['description_main'] = ''
    part_details['description_extra'] = ''
    part_details['manufacturer'] = 'sparkfun'
    part_details['part_number'] = 'sen_21208'
    repo_name = 'oomlout_oomp_source_electronic_breakout_board_sensor_accelerometer_bosch_bma400_sparkfun_sen_21208'
    repo_name = repo_name[:99]
    part_details['oomp_repo'] = f'http://github.com/oomlout/{repo_name}'
    parts.append(part_details)


    part_details = {}
    part_details['classification'] = 'electronic'
    part_details['type'] = 'breakout_board_sensor'
    part_details['size'] = 'accelerometer'
    part_details['color'] = 'analog_devices_adxl343'
    part_details['description_main'] = ''
    part_details['description_extra'] = ''
    part_details['manufacturer'] = 'adafruit'
    part_details['part_number'] = '4097'
    repo_name = 'oomlout_oomp_source_electronic_breakout_board_sensor_accelerometer_analog_devices_adxl343_adafruit_4097'
    repo_name = repo_name[:99]
    part_details['oomp_repo'] = f'http://github.com/oomlout/{repo_name}'
    parts.append(part_details)

    


    oomp.add_parts(parts, make_files=make_files)
    