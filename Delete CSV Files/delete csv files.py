# purpose of this code is to wipe downloaded csv files to clear space

import os

# set the os path to the downloads folder
download_folder = os.path.expanduser("~")+"/Downloads/"

# filter through downloads folder and look for .csv files
filelist = [ f for f in os.listdir(download_folder) if f.endswith(".csv") ]
for f in filelist:
    os.remove(os.path.join(download_folder, f))
