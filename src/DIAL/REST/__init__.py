import requests
import xml.etree.ElementTree as ET

class DIALServer:
    def __init__(self, uri):
        self.uri = uri

    # Verify an App actually exists
    def checkApp(self, app):
        return bool(self.info(app))

    # Get the apps met info.
    def info(self, app):
        # Define the XML namespace
        ns = {
            'dial': 'urn:dial-multiscreen-org:schemas:dial'
        }

        r = requests.get(self._URL(app))
        try:
            body = ET.fromstring(r.text)
        except:
            return {}
        # Name
        name = body.find('dial:name', ns).text
        # Status
        state = body.find('dial:state', ns).text
        # options
        options = {}
        try:
            options = body.find('dial:options', ns).attrib
        except:
            pass
        # Link - deprecated in version >2.1
        link = {}
        try:
            link = body.find('dial:link', ns).attrib
        except:
            pass

        return {
            'name': name,
            'state': state,
            'options': options,
            'link': link
        }

    # Force stop, only works if the service allows stops
    def stop(self, app):
        r = requests.delete(self._URL(app))
        return {}

    # Pass options to the app
    def start(self, app, options):
        r = requests.post(self._URL(app), options)
        return {}

    def _URL(self, app):
        return '{}{}'.format(self.uri, app)

if __name__ == "__main__":
    p = DIALServer('http://192.168.1.222:8009/apps/')
    print(p.info('Netflix'))
