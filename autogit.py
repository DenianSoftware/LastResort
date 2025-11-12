#!venv/bin/python3

import arguably
import os
from datetime import date
import string
from git import Repo

@arguably.command
def autogit(*, _dir="repos", _list="repos.txt"):
        """autogit.py - clone repos from a text file"""
        print(f"cloning repos from '{_list}'...")
        if os.path.isdir(_dir):
                pass
        else:
                os.system(f"mkdir {_dir}")
        with open(_list, 'r') as file:
                        for repo in file:
                                clean_repo = repo.strip()
                                repo_name = clean_repo.split('.git')[0].split('/')[-1]
                                
                                print(f"cloning {clean_repo}...")
                                try:
                                        Repo.clone_from(clean_repo, os.path.join(_dir, repo_name))
                                except Exception as e:
                                        print(f"an error occured while cloning {clean_repo}:\n {e}")
                                else:
                                        print("done!")
if __name__ == "__main__":
    arguably.run()
