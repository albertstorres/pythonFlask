from flask import Flask 

app = Flask(__name__)

def index () :
    return "Index"

def testando () :
    res = "<h1>Testando</h1>"
    return res

app.add_url_rule("/", "Index", index)
app.add_url_rule("/teste", "teste", testando)

app.run(debug=True, port="3000")