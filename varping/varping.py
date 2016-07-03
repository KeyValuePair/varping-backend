from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/script1")
def script1():
    return "script`"


if __name__ == "__main__":
    app.run()
