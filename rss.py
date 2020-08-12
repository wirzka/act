from datetime import datetime
import xml.etree.ElementTree as ET
import requests
import pprint
import json
import csv

class RSS():

    def __init__(self, url,
                 xml, json):
        # setting up
        self._url = url
        self._xml = xml
        self._json = json
        # list to store output
        self.l = []

    def RSS2XML(self):
        # taking the RSS feed
        try:
            res = requests.get(self._url)
        except:
            print("Check your connection, check if the URL is correct..")# putting the response on file
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
                ['Title describing the alert', (XXXX/YYMMDD/CSIRT-ITA)']
                So we are taking only the titles with lenght of 2
            '''
            if len(title.splitlines()) == 2:
                # adding the line on the list for later
                splitted = title.splitlines()
                self.l.append(title.splitlines())
                #  printing the line
                print(" - {} {}".format(splitted[1],splitted[0]))


    def Cont2File(self):
        # retrieve today date and formatting it
        today = datetime.today().strftime('%Y-%m-%d')
        # backing the filename
        filename = self._json + today + '.json'
        # writing JSON data on the file
        with open(filename, 'w') as oF:
             oF.write(json.dumps(self.l))
