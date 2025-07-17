import oomp
import oom_git

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


    
    oomp.load_parts(from_yaml=False, make_files=True, filter=filter)
    oomp.save_parts()
    oomp.save_parts_to_individual_yaml_files()



    #oom_git.push_to_git(comment=comment)

if __name__ == "__main__":
    #boolean_generate_releases = True
    boolean_generate_releases = False



    kwargs = {}

    #filter = ""
    #filter = "appliance"
    #filter = "bearing"
    #filter = "clothes"
    #filter = "computer"
    #filter = ["category","ikea"]
    #filter = "decorating"
    #filter = "electrical"
    #filter = "electronic_consumer"
    #filter = "exercise_equipment"
    #filter = "food"
    #filter = "ikea"
    #filter = "hardware_magnet"
    #filter = "hardware_screw"
    #filter = "hardware_ball_bearing"
    #filter = "household"
    #filter = "mechanical"    
    #filter = "oobb"
    #filter = "storage"
    #filter =  "breakout_board"
    #filter = "electronic"
    #filter = "electronic_battery"
    #filter = "electronic_breakout_board"
    #filter = "electronic_screw_terminal"
    #filter = "lighting"
    #filter = "mechanical_motor"
    #filter = "packaging"
    #filter = "printer"
    #filter = "project"
    #filter = "paper"
    #filter = "remote_control"
    #filter = "robot_vacuum"
    #filter = "robot_arm"
    filter = "task"
    #filter = "three_d_printer"
    #filter = "tool"
    #filter = "toy"
    #filter = "video_game_console"
    #filter = "vinyl"
    #filter = "vinyl_cutter"
    #filter = "warehouse"
    #filter = "wood"



    #filter = "aluminium_extrusion"
    #filter = "self_tapping"

    kwargs["filter"] = filter
    main(**kwargs)

    #wait
    #input("Press Enter to continue...")

    if boolean_generate_releases:
        import action_generate_releases
        action_generate_releases.main()
