from rss import RSS

u = RSS('https://csirt.gov.it/data/indexer/rss')

def main():
	u.RSS2XML()
	u.XMLParser()
	u.Cont2File()

if __name__ == "__main__":
	main()
