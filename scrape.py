import httplib
import re
from bs4 import BeautifulSoup

#import twitter

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
        self.name = input.contents[2].text
        self.address = input.contents[4].text
        self.website = input.contents[2].a["href"]

class event: 
    def __init__(self,input,column):
        self.text = input
        self.column = column
        self.day = days[column-4]
        temp = input.split()
        index = temp.index("p.m.")
        self.time = temp[index-1] + ' ' + temp[index]

def main():
    soup = BeautifulSoup(crawl())
    raw = []
    venues = []
    events = []
    days = []
    week = soup.thead.contents[1]
    for each in range(4,len(week)-1):
        days.append(week.contents[each].text)
    for each in soup.tbody.children:
        raw.append(each)
    raw = raw[1::2]
    raw[0].contents.insert(0,0) #Stupid web designers have unique first row...
    for each in raw:
        print(venue(each))
        venues.append(venue(each))
    for each in raw:
        for all in range(4,len(raw[0])-1):
            if each.contents[all].text != '':
                events.append(event(each.contents[all].text,all))
    for each in events:
        print events[each]
    
