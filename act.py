__author__ = "Andrea Grigoletto https://github.com/wirzka"
__version__ = "0.1"
__maintainer__ = "Andrea Grigoletto https://github.com/wirzka"
"""
act.py is a script to grab the Italian CSIRT's RSS feeds, then print them on the screen
and finally save them on a file.
"""
from rss import RSS
import os
import time

try:
	from art import *
	flag=True
except ImportError:
	flag=False

# url from where to grab the feeds
url = "https://csirt.gov.it/data/indexer/rss"
# xml filename
xml = "csirtita.xml"
# first part of JSON filename
json = "csirtita_"

# class useful to manage output color
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

u = RSS(url, xml, json)

def greetings(flag):
	os.system('cls' if os.name == 'nt' else 'clear')
	if flag:
		tprint("ACT",font="starwars",chr_ignore=True)
		print(color.GREEN + "Automatic " + color.END + "CSIRT " + color.RED + "Teller\n" + color.END)
	else:
		print(color.GREEN + "Automatic " + color.END + "CSIRT " + color.RED + "Teller\n" + color.END)

def main():
	# welcome
	greetings(flag)
	time.sleep(1)

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
	input("\nPress ENTER to exit.")
