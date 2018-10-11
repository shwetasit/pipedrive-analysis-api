# pip3 install pipedrive-python-lib
from pipedrive.client import Client
import json
from pandas.io.json import json_normalize
from itertools import islice
import pandas as pd
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


class Analysis:
    def callingDeals(deals):
        return (deals)
    def topTenDeals(deals):
        dat=take(2, deals['data'] )
        return (list(dat))
    def openDeal(deals):
        dat=deals['data']
        dat2=[]
        for d in dat:
            if d.get('status') == 'open':
                dat2.append(d)
        return dat2
    
    def closeDeal(deals):
        dat=deals['data']
        dat2=[]
        for d in dat:
            if d.get('status') == 'close':
                dat2.append(d)
        return dat2


    def wonDeal(deals):
        dat=deals['data']
        dat2=[]
        for d in dat:
            if d.get('status') == 'won':
                dat2.append(d)
        return dat2

    def pandasdemo(deals):
        print(deals)
        #deal=json.dumps(deals)
        #df=json.loads(deal)
         

       


       

            

