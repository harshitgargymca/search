import scrapy
import json
import ast
import HTMLParser
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

h =  HTMLParser.HTMLParser()
from testsearch.items import searchItem
class testspider(CrawlSpider):
    name = "alpha"
    allowed_domains = [#'thehindu.com','stackoverflow.com','google.co.in','wikipedia.org','amazon.in','quora.com',
                        'w3schools.com',
                        'flipkart.com']
    start_urls = [#"http://www.thehindu.com/",
                  #"http://stackoverflow.com/","https://www.google.co.in",
                  #"https://en.wikipedia.org/wiki/Main_Page","http://www.amazon.in",
                  #"https://www.quora.com/","http://www.w3schools.com/",
                  #"http://en.wikipedia.org/wiki/List_of_most_popular_websites"
                  "http://www.flipkart.com"
                 ]
    rules = [Rule(SgmlLinkExtractor(),callback ='parse_item', follow =False)]
    
    
    def parse_item(self,response):
        for sel in response.xpath('//a/*'):
            item = searchItem()
            
          

            item['title'] =str(ast.literal_eval(json.dumps(h.unescape(sel.xpath('//title/text()').extract())))).replace("\\n","").replace("\'","").replace("[","").replace("]","")
            item['link'] = urljoin_rfc(get_base_url(response),'')
           # item['desc'] = str(ast.literal_eval(json.dumps(h.unescape(sel.xpath('//body//text()').extract())))).replace("\\n","").replace("\\r","").replace("\\t","").replace("\\\\","").replace("'\'","").replace("\'","")
            
            return item
            
            
        
        
    
   # def parse(self,response):
   #     filename = response.url.split("/")[-2]
    #    with open(filename,'wb') as f:
     #       f.write(response.body)
            
