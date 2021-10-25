import os

import requests

from .disformers import DisFormersBot

__version__ = "0.0.6"
print("DisFormers version:",__version__)
r = requests.get(url="https://pypi.org/pypi/disformers/json")
if r.status_code == 200:
    project = r.json()
    if __version__ != project['info']['version']:
        print("Found a new version! Updating to new version..")
        os.system("pip install -U disformers")
        print("Suceessfully updated. Please restart bot.")
    else:
        print("No new updates.")
else:
    print("No new updates.")