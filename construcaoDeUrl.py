from flask import Flask, redirect, url_for

app = Flask (__name__)

def admin () :
    return "Admin"

def convidado (nome) :
    return "Olá %s" %nome

def user (nome) :
    if nome == "admin" :
        return redirect(url_for('admin'))
    else :
        return redirect(url_for('convidado', nome = nome))

app.add_url_rule("/admin", "admin", admin)
app.add_url_rule("/convidado/<nome>", "convidado", convidado)
app.add_url_rule("/user/<nome>", "user", user)

app.run(debug=True, port="3000")