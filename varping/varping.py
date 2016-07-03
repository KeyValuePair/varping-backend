#!../venv/bin/python
from flask import Flask, request
import count, code_indexing
import requests
app = Flask(__name__)

@app.route("/")
def search():
    param = request.args.get('pattern')
    url = "http://localhost:9200/refined_words/javascript/_search?q=term:*" \
            + param + "*"
    response = requests.get(url).content
    print param
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
