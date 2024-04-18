from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=['GET' , 'POST'])
def index () :
    # print(request.methods, request.args)
    t1 = request.args.to_dict()
    t2 = dict(request.args)
    return json.dumps([t1['idade'], t2['nome']])

app.run(debug=True, port='3000')


