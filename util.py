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

def getIDListString(index_name, doc_type):
    es = getElasticSearch()
    res = es.count(index=index_name, doc_type=doc_type)
    id_string = "["
    for i in range(1, res[u'count']+1):
        id_string += '"' + str(i) + '",'
    id_string = id_string[:-1]
    id_string += "]"
    return id_string
