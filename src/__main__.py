import argparse
import json
import logging

logging.basicConfig(level=logging.ERROR)

import DIAL
import probe

def main():
    appList = json.load(open('./src/data/applications.json'))
    logging.info('Using SSDP to discover nodes')
    nodes = DIAL.discover()
    logging.info('Found {} nodes'.format(len(nodes)))
    for node in nodes:
        print('Name: {}\nManufacturer: {}\nModel: {}'.format(
            node['friendlyName'],
            node['manufacturer'],
            node['model']
        ))
        url = node['application-url']
        logging.info('Probing {}'.format(url))
        p = probe.Probe(url, appList)
        availableApps = p.checkAllApps()
        for app in availableApps:
            print('Found: {}'.format(app))

    logging.info('Done')
if __name__ == "__main__":
    main()
