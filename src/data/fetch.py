#!/usr/bin/env python3

# Hacky script to fetch all the DIAL applications.
# Has to parse a google sheet directly...

import requests
import json

url = 'https://spreadsheets.google.com/feeds/cells/1H-gvsMf3K651F7zpFsdICAJu8fXuNNLFgNfnn-Ukq_c/1/public/values?alt=json-in-script'

def fetch_dial_applications():

    r = requests.get(url)
    gd = r.text
    # We need to strip out gdata.io.handleScriptLoaded([data]) container
    start = len('gdata.io.handleScriptLoaded(')
    end = -2
    sheet = json.loads(gd[start:end])

    # Get everything in order
    predata = {}
    for cell in sheet['feed']['entry']:
        cell = cell['gs$cell']
        if cell['row'] != '1':
            row = int(cell['row'])
            if row not in predata:
                predata[row] = {}
            # We don't care about the contact name.
            if cell['col'] == '1':
                predata[row].update({'company': cell['$t']})
            elif cell['col'] == '3':
                predata[row].update({'name': cell['$t']})
            # clean up stray ones
            if predata[row] == {}:
                del predata[row]

    # Clean up for output
    output = {}
    for _, item in predata.items():
        output[item['name']] = item['company']
    return output


if __name__ == "__main__":
    print(json.dumps(fetch_dial_applications()))
