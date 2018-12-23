import requests
from . import ssdp
import xml.etree.ElementTree as ET

def discover():
    ns = {
        'upnp': 'urn:schemas-upnp-org:device-1-0'
    }

    results = []
    discovered = ssdp.discover('urn:dial-multiscreen-org:service:dial:1')
    for service in discovered:
        r = requests.get(service.location)
        application_url = r.headers.get('Application-URL')
        body = ET.fromstring(r.text)
        device = body.find('upnp:device', ns)
        friendlyName = device.find('upnp:friendlyName', ns).text
        manufacturer = device.find('upnp:manufacturer', ns).text
        model = device.find('upnp:modelName', ns).text
        udn = device.find('upnp:UDN', ns).text
        results.append({
            'application-url': application_url,
            'friendlyName': friendlyName,
            'manufacturer': manufacturer,
            'model': model,
            'udn': udn
        })
    return results
