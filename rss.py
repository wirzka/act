from datetime import datetime
import xml.etree.ElementTree as ET
import requests
import pprint
import json
import csv

class RSS():

    def __init__(self, url, xml):
        # setting up
        self._url = url
        self._xml = xml
        self._json = 'csirtita_'
        # list to store output
        self.l = []

    def RSS2XML(self):

        # taking the RSS feed
    	res = requests.get(self._url)
        # putting the response on file
    	with open(self._xml, 'wb') as f:
    		f.write(res.content)

    def XMLParser(self):
        # reading the xml file
        xmlParsed = ET.parse(self._xml)

        # retrieving the root
        root = xmlParsed.getroot()

        # iterating the titles
        for item in root.iter('title'):
            title = item.text
            '''
                The CSIRT alert is structured as follow:
                ['Title describing the alert', (ALXX/XXXXXX/CSIRT-ITA)']
                So we are taking only the titles with lenght of 2
            '''
            if len(title.splitlines()) == 2:
                # adding the line on the list for later
                self.l.append(title.splitlines())
                #  printing the line
                pprint.pprint(title.splitlines())

    def Cont2File(self):
        # retrieve today date and formatting it
        today = datetime.today().strftime('%Y-%m-%d')
        # backing the filename
        filename = self._json + today + '.json'
        # writing JSON data on the file
        with open(filename, 'w') as oF:
             oF.write(json.dumps(self.l))
