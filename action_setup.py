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



    #oom_git.push_to_git(comment=comment)

if __name__ == "__main__":
    kwargs = {}

    filter = ""
    filter = "oobb"

    kwargs["filter"] = filter
    main(**kwargs)