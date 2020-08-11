from datetime import datetime
import xml.etree.ElementTree as ET
import requests
import pprint
import json
import csv

class RSS():

    def __init__(self, url):
        self._url = url
        self._xml = 'csirtita.xml'
        self._json = 'csirtita_'
        self.l = []

    def RSS2XML(self):
    	res = requests.get(self._url)

    	with open(self._xml, 'wb') as f:
    		f.write(res.content)

    def XMLParser(self):
        it = ET.parse(self._xml)
        root = it.getroot()
        for item in root.iter('title'):
            testo = item.text
            if len(testo.splitlines()) == 2:
                self.l.append(testo.splitlines())
        # pprint.pprint(json.dumps(self.l))

    def Cont2File(self):
        today = datetime.today().strftime('%Y-%m-%d')
        filename = self._json + today + '.json'
        # print(filename)
        with open(filename, 'w') as oF:
             oF.write(json.dumps(self.l))
