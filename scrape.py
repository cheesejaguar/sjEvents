import httplib
import re
from bs4 import BeautifulSoup

import twitter

my_consumer_key = ''
my_consumer_secret = ''
my_access_token = ''
my_access_token_secret = ''

'''
api = twitter.Api(consumer_key=my_consumer_key,
                  consumer_secret=my_consumer_secret,
                  access_token_key=my_access_token,
                  access_token_secret=my_access_token_secret)
'''
user_token = ''

def crawl():
    url = '/liveandlocal/'
    connection = httplib.HTTPConnection('sjdowntown.com')
    connection.request('GET', url)
    response = connection.getresponse()
    result_str = response.read()
    connection.close()
    if result_str == "":
        print "Error."
        return
    else:
        return result_str

class venue:
    def __init__(self,input):
        self.name = input.contents[1].text
        self.address = input.contents[2].text
        self.website = input.contents[1].a["href"]

def main():
    soup = BeautifulSoup(crawl())
    raw = []
    venues = []
    for each in soup.tbody.children:
        raw.append(each)
    raw = raw[1::2]
    raw[0].contents.insert(0,0) #Stupid web designers have unique first row...
    for each in raw:
        venues.append(venue(each))
        
 
    
