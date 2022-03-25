#setup internet connection
import secrets
from gitDeploy import gitDeploy
from DeployServer import DeployServer
from wlanhelper import wlanhelper

filesToKeep=["secrets.py"]
ignoreUpload=[".gitmodules", ".gitignore", 'pymakr.conf', "LICENSE", "README.md"]
gd = gitDeploy("Palmen98", "MicroPythonOTA", filesToKeep, ignoreUpload)

wlan = wlanhelper()
ds = DeployServer(gd, wlan, 80)

print(wlan.ifconfig()[0])

