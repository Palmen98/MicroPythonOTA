#poll

from HTTPClient import HTTPClient
import json
#https://api.github.com/repos/dntoll/MicropythonGitDeploy
pollerClient = HTTPClient('api.github.com', secrets.basicAuthentication)

response = pollerClient.get("/repos/Palmen98/MicroPythonOTA")
jsonObject = json.loads(response.body)
print(jsonObject["pushed_at"])