#-*- coding: utf8 -*-
import re
from elasticsearch import Elasticsearch
import os, sys


def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string)
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string)
    return string

es = Elasticsearch([
    {'host': 'localhost'}
])

doc = {
        'language': 'javascript',
        'text': '',
}

path = "../src/"
dirs = os.listdir(path)
js_files = []
count = 1
for file in dirs:
    if file.endswith(".js"):
        js_files.append(file)
        #print(file)
        with open('../src/'+file, "r") as js_file:
            content = removeComments(js_file.read())
            print(content)

            doc['text'] = content
            res = es.index(index="original_code", doc_type="javascript", id=count, 
                    body=doc)
            count += 1



