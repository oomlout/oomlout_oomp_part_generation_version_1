import oomp
import oom_git
import copy

def main(**kwargs):
    filter = kwargs.get("filter", "")
    

    #git = True
    git = False


    if git:
        repos = []
        repos.append(["https://github.com/oomlout/oomlout_oomp_footprint_bot","tmp/"])
        repos.append(["https://github.com/oomlout/oomlout_oomp_project_bot","tmp/"])
        repos.append(["https://github.com/oomlout/oomlout_oomp_symbol_bot","tmp/"])

        repos.append(["https://github.com/oomlout/oomlout_oomp_symbol_all_the_kicad_symbols","c:/gh/"])
        repos.append(["https://github.com/oomlout/oomlout_oomp_footprint_all_the_kicad_footprints","c:/gh/"])


        for repo in repos:
            directory = repo[1]
            oom_git.clone(repo=repo[0], directory=directory)


    import time
    times = []

    time_start_start = time.time()

    time_start = time.time()
    time_name = "oomp.load_parts"
    print(f"starting {time_name}")    
    oomp.load_parts(from_yaml=False, make_files=True, filter=filter)
    time_end = time.time()
    hour = (time_end - time_start) / 3600
    minutes = (time_end - time_start) / 60
    print(f"{time_name} took {hour} hours or {minutes} minutes")
    time_entry = {"time_name": time_name, "time": time_end - time_start}
    times.append(time_entry)


    time_start = time.time()
    time_name = "oomp.save_parts"    
    print(f"starting {time_name}")
    oomp.save_parts()
    time_end = time.time()
    hour = (time_end - time_start) / 3600
    minutes = (time_end - time_start) / 60
    print(f"{time_name} took {hour} hours or {minutes} minutes")
    time_entry = {"time_name": time_name, "time": time_end - time_start}
    times.append(time_entry)

    time_start = time.time()
    time_name = "oomp.save_parts_to_individual_yaml_files"
    print(f"starting {time_name}")    
    oomp.save_parts_to_individual_yaml_files()
    time_end = time.time()
    hour = (time_end - time_start) / 3600
    minutes = (time_end - time_start) / 60
    print(f"{time_name} took {hour} hours or {minutes} minutes")
    time_entry = {"time_name": time_name, "time": time_end - time_start}
    times.append(time_entry)

    time_end_end = time.time()
    time_name = "total time"
    hour = (time_end_end - time_start_start) / 3600
    minutes = (time_end_end - time_start_start) / 60
    
    time_entry = {"time_name": time_name, "time": time_end_end - time_start_start}
    times.append(time_entry)

    print("time summary")
    for time_entry in times:
        print(f"{time_entry['time_name']} took {time_entry['time']} seconds")



    #oom_git.push_to_git(comment=comment)


if __name__ == "old__main__":
    #boolean_generate_releases = True
    boolean_generate_releases = False



    kwargs = {}

    filter = ""
    #filter = "bearing"
    #filter = "computer"
    #filter = "ikea"
    #filter = "hardware"
    #filter = "mechanical"    
    #filter = "oobb_part_tray"
    #filter = "storage"
    #filter =  "breakout_board"
    #filter = "electronic"
    #filter = "lighting"
    #filter = "packaging"
    #filter = "paper"
    #filter = "three_d_printer"
    #filter = "tool"
    #filter = "wood"

    #filter = "aluminium_extrusion"
    #filter = "self_tapping"

    kwargs["filter"] = filter
    main(**kwargs)


    if boolean_generate_releases:
        import action_generate_releases
        action_generate_releases.main()


if __name__ == "__main__":        
    import argparse
    parser = argparse.ArgumentParser(description="Run OOMP setup with optional filter.")
    parser.add_argument("-f", "--filter", type=str, default="", help="Filter for parts to load (default: all parts).")
    args = parser.parse_args()
    kwargs = copy.deepcopy(vars(args))
    print(f"Running with filter: {kwargs['filter']}")
    main(**kwargs)