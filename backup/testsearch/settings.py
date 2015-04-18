# -*- coding: utf-8 -*-

# Scrapy settings for testsearch project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'testsearch'

SPIDER_MODULES = ['testsearch.spiders']
NEWSPIDER_MODULE = 'testsearch.spiders'
ITEM_PIPELINES ={
    'testsearch.pipelines.TestsearchPipeline',}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "5sites"
MONGODB_COLLECTION = "dhondhu"
DEPTH_LIMIT = 3
CONCURRENT_REQUESTS = 150
DOWNLOAD_TIMEOUT = 100
