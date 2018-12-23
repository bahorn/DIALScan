import requests
import json

import DIAL

# Checks all the apps available.
class Probe:
    def __init__(self, uri, appList):
        self.appList = appList
        self.rest = DIAL.rest(uri)

    def checkAllApps(self):
        result = []
        for app in self.appList.keys():
            app_found = self.rest.checkApp(app)
            if app_found:
                result.append({ app:app_found })

        return result

if __name__ == "__main__":
    appList = json.load(open('../data/applications.json'))
    p = Probe('http://192.168.1.222:8009/apps/', appList)
    print(p.checkAllApps())
