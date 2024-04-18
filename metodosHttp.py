from flask import Flask, request
from json import dumps

app = Flask (__name__, static_folder="./public")

@app.route("/add", methods=["GET","POST"])
def add () :
    if request.method == "POST" :
        return dumps(request.form)
    return "OKK GET"


app.run(debug=True, port="3000")