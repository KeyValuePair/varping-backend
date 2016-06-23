import re
from elasticsearch import Elasticsearch


def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string)
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string)
    return string

def getElasticSearch():
    return Elasticsearch([
        {'host': 'localhost'}
    ])

def deleteIndex(index_name):
    es = getElasticSearch()
    es.indices.delete(index=index_name, ignore=[400, 404])
