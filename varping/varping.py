#!../venv/bin/python
from flask import Flask, request
import count, code_indexing
import requests
import json
import os.path
app = Flask(__name__)

@app.route("/")
def search():
    param = request.args.get('pattern')
    url = "http://localhost:9200/refined_words/javascript/_search?q=term:*" \
            + param + "*"
    response = requests.get(url).content
    print param
    return response

@app.route("/test/")
def test():
    param = request.args.get('pattern')
    default_dictionary_list = ['component']
    for word in default_dictionary_list:
        # TODO: handle cases that param matches  multiple words
        if param in word:
            param = word
            break
    url = "http://localhost:9200/refined_words/javascript/_search?q=term:*" \
            + param + "*"
    response = requests.get(url).content
    print param
    return response

@app.route("/ddtest/")
def dd_test():
    param = request.args.get('pattern')

    default_dictionary_list = ['component']
    for word in default_dictionary_list:
        # TODO: handle cases that param matches  multiple words
        if param in word:
            param = word
            break

    response = ""
    if os.path.isfile(param+'.txt'):
        with open(param+".txt", "rb") as f:
            response = f.read()
    else:
        url = "https://twinword-word-associations-v1.p.mashape.com/associations/?entry=" + param
        headers = {'X-Mashape-Key': 'Av29bZ5lvHmshx0LGxGFjUIQpT59p1LbTQ4jsnGRCqwzG95ZeT'}
        response = requests.get(url, headers=headers).content
        with open(param+".txt", "wb") as f:
            f.write(response)

    associations_array = json.loads(response)['associations_array']

    merged_response = ""

    url = "http://localhost:9200/refined_words/javascript/_search?q=term:*" \
            + param + "*"
    response = requests.get(url).content
    merged_response += response
    for word in associations_array:
        url = "http://localhost:9200/refined_words/javascript/_search?q=term:*" \
                + word + "*"
        response = requests.get(url).content
        merged_response += response
    return merged_response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
