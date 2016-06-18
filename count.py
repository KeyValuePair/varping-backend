#-*- coding: utf-8 -*-
import urllib2
from urllib import urlencode, quote
import json

params = """{
        "ids": ["1", "2"],
        "parameters": {
            "fields": [
                "text"
                ],
            "term_statistics": true
            }
        }"""

url = "http://localhost:9200/original_code/javascript/_mtermvectors"        


print(url)
request = urllib2.Request(url, data=params)
response = urllib2.urlopen(request)

res = json.load(response)
term = res['docs'][0]['term_vectors']['text']['terms']
print(term_vectors)


