from flask import Flask

app = Flask (__name__,static_folder="public")



app.run(debug=True, port="3000")