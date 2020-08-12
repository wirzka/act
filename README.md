```
     ___        ______ .___________.
    /   \      /      ||           |
   /  ^  \    |  ,----'`---|  |----`
  /  /_\  \   |  |         |  |
 /  _____  \  |  `----.    |  |
/__/     \__\  \______|    |__|

      Automatic CSIRT Teller
```
# Automatic CSIRT Teller

Python command line tool to check RSS feeds from the Italian [CSIRT](https://csirt.gov.it/home).

### How it works
This is how the script runs:
1. Retrieves the RSS feed
2. Saves it to file (*default filename: csirtita.xml*)
3. Grabs the alerts' title
4. Prints on screen the titles
5. Saves the titles to file (*default filename: csirtita_YYYY-MM-DD.json*)
4. Deletes the *csirtita.xml* file

### Prerequisites & dependecies

* Python version: `3.7`
* [Art](https://github.com/sepandhaghighi/art) for the ASCII art 
##### Art is not mandatory, but it will add some fancy ASCII art

### How to use it
```console
> python act.py
     ___        ______ .___________.
    /   \      /      ||           |
   /  ^  \    |  ,----'`---|  |----`
  /  /_\  \   |  |         |  |
 /  _____  \  |  `----.    |  |
/__/     \__\  \______|    |__|



Automatic CSIRT Teller

 - (AL01/200811/CSIRT-ITA) Aggiornamento di sicurezza di Teamviewer
 - (BL01/200811/CSIRT-ITA) Campagna crime che fa uso di allegati RTF
 - (AL01/200810/CSIRT-ITA) Individuate 295 estensioni malevole nel web store di Chrome
 - (AL01/200808/CSIRT-ITA) Ursa Loader contro utenti italiani
 - (AL03/200807/CSIRT-ITA) Nuovi riscontri relativi al malware Emotet
```

### Default files

| File | Description|
| -------------|------------- |
| csirtita.xml  | where the RSS feed is saved |
| csirtita-YYMMDD.json | the output file with the alerts' title |


## Purpose of this tool
Automate the checking process of the Italian CSIRT alerting service.

Bear in mind that I am not a professional dev, so feel free to show me better ways to do it.

## Authors

* **Andrea Grigoletto** - [Wirzka](https://github.com/wirzka)

## Acknowledgments

* Thanks to the [CSIRT](https://csirt.gov.it/home) for the service
