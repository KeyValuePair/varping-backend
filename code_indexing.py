#-*- coding: utf8 -*-
import os, sys
from util import removeComments, getElasticSearch, deleteIndex

def getFiles(path, extension="js"):
    files = os.listdir(path)
    files_to_index = []
    for file in files:
        if file.endswith("." + extension):
            files_to_index.append(file)
    return files_to_index

def indexCodes(path, files, doc):
    es = getElasticSearch()
    count = 1
    for file in files:
        with open(path+file, "r") as file:
            content = removeComments(file.read())
            doc['text'] = content
            es.index(index="original_code", doc_type=doc['language'], id=count,
                body=doc)
            count += 1



doc = {
        'language': 'javascript',
        'text': '',
}

path = "../src/"
deleteIndex('original_code')
indexCodes(path, getFiles(path, "js"), doc)
