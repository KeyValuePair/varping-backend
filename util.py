#-*- coding: utf-8 -*-
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


# document 의 id의 list를 string 으로 변환
def getIDListString(index_name, doc_type):
    es = getElasticSearch()

    # index, doc_type에 해당하는 document 개수를 json형태로 가져온다
    res = es.count(index=index_name, doc_type=doc_type)

    # 1부터 count값까지 ["1", "2"] 형태로 string 조합
    id_string = "["
    for i in range(1, res[u'count']+1):
        id_string += '"' + str(i) + '",'
    id_string = id_string[:-1]
    id_string += "]"
    return id_string
