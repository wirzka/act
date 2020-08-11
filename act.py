from rss import RSS
import os

url = "https://csirt.gov.it/data/indexer/rss"
xml = "csirtita.xml"

u = RSS(url, xml)

def main():

	# retrieve the rss feed and bring it on local as xml file
	u.RSS2XML()

	# take the title from the item inside the XML file
	u.XMLParser()

	# save the output to a json file named: csirtita_<TodayDate>.json
	u.Cont2File()

	# cleaning
	os.remove(xml)

if __name__ == "__main__":
	main()
