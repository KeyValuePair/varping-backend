#!../venv/bin/python
#-*- coding: utf-8 -*-
import urllib2
from urllib import urlencode, quote
import json
from util import getElasticSearch, deleteIndex, getIDListString

def getSortedMTermVectors(language):
    params = """{
            "ids": """ + getIDListString('original_code', language) + \
            """
            , "parameters": {
                "fields": [
                    "text"
                    ],
                "term_statistics": true
                }
            }"""

    url = "http://localhost:9200/original_code/"+ language +"/_mtermvectors"
    request = urllib2.Request(url, data=params)
    response = urllib2.urlopen(request)

    res = json.load(response)

    term = res['docs'][0]['term_vectors']['text']['terms']
    terms = []
    for key, value in term.iteritems():
        if len(key) >= 2 and value[u'ttf'] >= 0 :
            temp_obj = {}
            temp_obj['term'] = str(key)
            temp_obj['ttf'] = value[u'ttf']
            terms.append(temp_obj)
    terms = sorted(terms, key=lambda x: x[u'ttf'], reverse=True)
    return terms

def indexRefinedWords(language, terms):
    es = getElasticSearch()
    count = 1
    for term in terms:
        doc = {
            'deleted' : 0,
            'displayed': 0,
            'term': term['term'],
            'ttf': term['ttf']
            }
        es.index(index="refined_words", doc_type="javascript",
                id=count, body=doc)
        count += 1


if __name__ == "__main__":
    deleteIndex('refined_words')
    terms = getSortedMTermVectors('javascript')
    indexRefinedWords('javascript', terms)


