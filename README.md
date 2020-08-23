# SheypoorScraper
Sheypoor.com phone number scraper using TOR proxy

## Requirements
Python Packages : requests , torrequest , unidecode , beautifulsoup4
`pip install requests torrequest unidecode beautifulsoup4`

## Tor installation
### Linux
`sudo apt install tor`
and then you should change `RUN_DAEMON` to `no` using :
`sudo gedit /etc/default/tor`
and stop the daemon using :
`sudo /etc/init.d/tor stop`
> using Ubuntu 20.04

### Windows
- Download and install [Tor Browser](https://www.torproject.org/download/)
- add `tor.exe` to your environment variables

