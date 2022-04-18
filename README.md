OTA Testing procedure

# Flash device 

import os
os.fsformat('/flash')

# Reboot device
Press reset button on Lopy4

# Upload program

# Start OTA in REPL
from gitDeploy import gitDeploy 
filesToKeep=["secrets.py"]
ignoreUpload=[".gitignore", "LICENSE", "README.md"]
gd = gitDeploy("Palmen98", "MicroPythonOTA", filesToKeep, ignoreUpload)
gitDeploy.deploy(gd)