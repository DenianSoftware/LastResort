#!/home/boss/LastResort/venv/bin/python3
import arguably
import os
from datetime import date
import string

@arguably.command
def lastresort(github):
    """Last Resort - a right tool for coming doomsday."""
    if(github):
        print("cloning repos from 'repos.txt'...")
        os.system(f"mkdir repos")
        if(github):
            with open("repos.txt", 'r') as file:
                for repo in file:
                    os.system(f"git clone {repo}")

if __name__ == "__main__":
    arguably.run()
