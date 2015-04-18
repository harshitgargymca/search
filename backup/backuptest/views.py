from django.shortcuts import render, RequestContext, render_to_response
from backuptest.models import post
import sys
from os import path
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log
from testsearch.spiders.test_spider import testspider
#sys.path.insert(0,'D:\django\django\scripts\testsearch\testsearch\spiders')
#sys.path.insert(0,'D:\django\django\scripts\dhondhu\search')
#import flipkart


import pymongo
from pymongo import MongoClient
client = MongoClient('localhost',27017)
def form(request):
    x= ["http://www.thehindu.com/",
        "http://stackoverflow.com/","https://www.google.co.in",
        "https://en.wikipedia.org/wiki/Main_Page","http://www.amazon.in","https://www.quora.com/",
        "http://www.w3schools.com/","http://en.wikipedia.org/wiki/List_of_most_popular_websites"
                 ]
      
    return render(request,'search_form.html',{'sites':x})



def search(request):
    if 'q' in request.GET:
        q= request.GET['q']

        db = client['5sites']
        
        collection = db['dhondhu']
        cursor = collection.find({'$text':{'$search': q}}).sort('created_at').limit(15)
        
        
        return render(request,'search_results.html',{'items':cursor,'query':q})

def sitecrawl(request):
    if 'q' in request.GET:
        q = request.GET['q']
        
        spider = testspider(domain='q')
        crawler = Crawler(Settings())
        crawler.configure()
        crawler.crawl(spider)
        crawler.start()
        log.start()
        reactor.run()
        return render(request,'sitescrawl.html')
    else:
        return render(request,'sitescrawl.html')
            
    
def showdata(request):
    db = client['5sites']
    collection = db['dhondhu']
    post.objects.all().delete()
    cursor = collection.find()
    for item in cursor:
        data = post.objects.create(title=item.get('title'),link =item.get('link'),popularity = 1)
        
    
    return render(request,'displayupdate.html')    
    



# Create your views here.

# Create your views here.
