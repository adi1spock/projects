import scrapy
import re
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)


ner=["member","members","minister","ministers","ministries","directory","directories","council","a-z","government a-z",
             "parliament","federal government","cabinet members","cabinet","board member","board members","contact directory",
             "government leader","government leaders","senator","senators","representative","representatives","legislator",
             "legislators","governor","mayor","state authorities","adminstrator","adminstrative","senators'","department",
             "chancellery","ministry","member's","mla","mlas","mlcs","mla","mlc","lt. governor","governors","lt. governors"]

name_finder=["hon","honourable","mr","mrs","ms","shri","sri","smt.","dr","dr.","msc","mba","mag."
             "sushri","his highness","his excellency","lieutenant","her excellency","lord","sh."]

role_=["mp","mla","prime minister","minister of","commisioner","chairperson","president","vice","hon'ble"]

ministry=["ministry of","department of"]
#creating different list of variables
name=[]
role=[]
position=[]



#making functions for extracting data, lowering string, and checking its presence in the text enclosed in a tag.
def country(x):
    if(x=="https://www.india.gov.in/my-government"):
        country="india"
    elif(x=="https://uaecabinet.ae/en"):
        country="uae"
    elif(x=="https://www.gov.za/"):
        country="south-africa"
    elif(x=="https://www.usa.gov/"):
        country="usa"
    elif(x=="https://www.australia.gov.au/"):
        country="australia"
    elif(x=="https://www.gov.uk/"):
        country="uk"
    elif(x=="https://www.gov.si/"):
        country="slovenia"
    elif(x=="https://www.canada.ca/en.html"):
        country="canada"
    elif(x=="https://www.government.se/"):
        country="sweden"
    elif(x=="https://www.bundeskanzleramt.gv.at/en.html"):
        country="austria"
    elif(x=="https://www.gov.si/en/"):
        country="singapore"
    elif(x=="https://www.govt.nz/"):
        country="new zeland"
    elif(x=="https://denmark.dk/"):
        country="denmark"
    elif(x=="https://www.admin.ch/gov/en/start.html"):
        country="switzerland"
    elif(x=="https://www.regjeringen.no/en/id4/"):
        country="norway"
def extractor(x):
    x=x.lower()
    for i in name_finder:
        if(bool(re.search(i,x))==True):
            name.append(x)
    for i in ministry:
        if(bool(re.search(i,x))==True):
            role.append(x)
    for i in role_:
        if(bool(re.search(i,x))==True):
            position.append(x)
def lowering_f(x):
    x=x.lower()
    return x
def checker(x):
    for i in ner:
        if(bool(re.search(i,lowering_f(x)))):
            return True
def name_checker(x):
    for i in name_finder:
        if(bool(re.search(i,lowering_f(x)))):
            return True









class IndiaSpider(scrapy.Spider):
    name = 'india'
    allowed_domains = ['india.gov.in/my-government']
    start_urls = ['http://india.gov.in/my-government/']

    def parse(self,response):
        links=response.xpath("//a/@href").extract()
        links_text=response.xpath("//a/text()").extract()
        for i in links:
            if(i[:1]=="/"):
                i='http://india.gov.in/my-government'+i
                j="india.gov.in/my-government"+i
                yield{"links":i}
                yield scrapy.Request(i)
                print("---------------")

print(links)
