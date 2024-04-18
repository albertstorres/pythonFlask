from flask import Flask

app = Flask(__name__)

def hello (nome = "oMenu") :
    return "<h1>Hello {} </h1>".format(nome)

def blog (postID = -1) :
    if postID >= 0 :
        return "Blog info {}".format(postID)
    else :
        return "Blog <h1>SEM</h1> info"

app.add_url_rule("/hello/", "hello", hello)
app.add_url_rule("/hello/<nome>", "hello", hello)
app.add_url_rule("/blog/", "blog", blog)
app.add_url_rule("/blog/<int:postID>", "blog", blog)

app.run(debug=True, port="3000")