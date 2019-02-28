import requests
from bs4 import BeautifulSoup

def getTitle(url):
    print(url)
    try:

        res = requests.get(url)

    except:

        return None

    try:

        bsObj = BeautifulSoup(res.text,'html.parser')
        t= bsObj.select('title')
        print(t[0].getText())
        
    

    except:

        print('BS Raised an exception')

        
title = getTitle("http://nostarch.com")
