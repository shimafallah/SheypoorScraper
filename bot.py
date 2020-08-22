import requests
import json
import re
import random
import stem
import time
from torrequest import TorRequest
from bs4 import BeautifulSoup
from unidecode import unidecode

Headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36" }

with TorRequest() as TorR:
    def sheypoor(ProductId):
        URL = f"https://www.sheypoor.com/api/web/listings/{ProductId}/description"
        SheypoorResponse = TorR.get(URL,headers=Headers).text
        time.sleep(3)
        Data = json.loads(SheypoorResponse)
        try:
            PhoneData = Data["data"]["description"]
            SheypoorNumber = re.search(r"<strong>شماره تماس:(.*)<\/strong>", PhoneData)[1]
        except:
            print("Ip Banned , Changing ip ...")
            TorR.close()
            try:
                NewPort = random.randrange(8000,9100)
                TorR.__init__(proxy_port=NewPort,ctrl_port=NewPort + 1)
                return sheypoor(ProductId)
            except stem.SocketError:
                return sheypoor(ProductId)


        SheypoorNumber = unidecode(SheypoorNumber)
        return SheypoorNumber



    URL = "https://www.sheypoor.com/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86?"

    def GetList(page):
        RequestUrl = f"{URL}p={page}"
        HtmlContent = requests.post(RequestUrl,headers=Headers).text
        Soup = BeautifulSoup(HtmlContent, "html.parser")
        # print(Soup.prettify())
        
        for link in Soup.select('.icon-star-empty'):
            GetId = link['data-save-item']
            print(sheypoor(GetId))


    while True:
        for page in range(1, 21):
           GetList(page)
   
   


   
