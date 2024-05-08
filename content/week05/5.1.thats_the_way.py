from pathlib import Path
import re

# using regex to match the prefix of a filename
def thats_the_way (path):
    return [f.name for f in  Path(path).iterdir() if f.is_file() and re.match(r'^deep.*$',f.name)]

def main():
    print(thats_the_way("images"))


