import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []

    #oomlout

    username_github = "oomlout"

    #use the github api to get a list of public repositories for username_github
    import requests
    url = f"https://api.github.com/users/{username_github}/repos"
    response = requests.get(url)
    repos = response.json()

    #loop through the repos
    for repo in repos:
        url = repo["html_url"]
        name = url.split("/")[-1]
        name_fixed = name_fixed.lower().replace(" ", "_")
        name_fixed = name_fixed().replace("-", "_")
        part_details = {}
        part_details["classification"] = "project"
        part_details["type"] = "github"
        part_details["size"] = ""
        part_details["color"] = ""
        part_details["description_main"] = f"{username_github}_{name_fixed}"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        part_details["link_redirect"] = url
        parts.append(part_details)
        



        

    




    
    oomp.add_parts(parts, **kwargs)

#testing    
#kwargs=  {}
#load_parts(**kwargs)