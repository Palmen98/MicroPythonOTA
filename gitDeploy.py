try:
    from MicropythonGitDeploy.HTTPClient import HTTPClient
    from MicropythonGitDeploy.GitHubClient import GitHubClient
    from MicropythonGitDeploy.LoPyFileSaver import LoPyFileSaver
except:
    #this to make sure it works with main.py in this library for testing
    from HTTPClient import HTTPClient
    from GitHubClient import GitHubClient
    from LoPyFileSaver import LoPyFileSaver
import secrets
import machine
import _thread
import time

class gitDeploy:

    def __init__(self, username, repoName, filesToKeep, ignoreTheseFiles):
        self.username = username
        self.repoName = repoName
        self.filesToKeep = filesToKeep
        self.ignoreTheseFiles = ignoreTheseFiles


    def deploy(self):
        print('Starting to measure time')
        start_time = time.time()
        c = HTTPClient('api.github.com', secrets.basicAuthentication)
        client = GitHubClient(c, self.username, self.repoName)
        
        fs = LoPyFileSaver(HTTPClient('raw.githubusercontent.com', secrets.basicAuthentication), self.filesToKeep, self.ignoreTheseFiles)
        fs.removeOldFiles()

        for f in client.files:
            fs.downloadAndSave(f.clientDirectory, f.name, f.url)
        end_time = time.time()
        print(end_time - start_time)
        machine.reset()
