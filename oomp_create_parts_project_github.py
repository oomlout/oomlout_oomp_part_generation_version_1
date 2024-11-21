import os
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
    #authentcate first
    #make sure to fetch all pages
    run = True
    page = 1
    
    #token notes
    # generate here
    # https://github.com/settings/personal-access-tokens/new
    # set as GITHUB_TOKEN
    #set GITHUB_TOKEN_LOW_ACCESS= {token}

    while run:
        print(f"loading github page {page}")
        import requests
        token_github = os.getenv("GITHUB_TOKEN_LOW_ACCESS")
        if token_github is None:
            print("GITHUB_TOKEN not set")
        url_base = f"https://api.github.com/users/{username_github}/repos"
        url = f"{url_base}?page={page}"      
        headers = {
            "Authorization": f"token {token_github}"
        }
        response = requests.get(url, headers=headers)
        repos = response.json()
        pass
        if len(repos) == 0:
            run = False
        else:
            #loop through the repos
            for repo in repos:            
                url = repo["html_url"]
                name = url.split("/")[-1]
                name_fixed = name.lower().replace(" ", "_")
                name_fixed = name_fixed.replace("-", "_")
                part_details = {}
                part_details["classification"] = "project"
                part_details["type"] = "github"
                part_details["size"] = f"{username_github}"
                part_details["color"] = f"{name_fixed}"
                part_details["description_main"] = ""
                part_details["description_extra"] = ""
                part_details["manufacturer"] = ""
                part_details["part_number"] = ""
                part_details["link_redirect"] = url
                part_details["link_github"] = url
                parts.append(part_details)
        page += 1
        



        

    




    
    oomp.add_parts(parts, **kwargs)

#testing    
#kwargs=  {}
#load_parts(**kwargs)