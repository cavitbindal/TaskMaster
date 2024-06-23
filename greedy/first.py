from flask import Flask

app = Flask("Greedy")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"