import datetime
from flask import Flask, render_template

app = Flask(__name__,template_folder='template')

@app.route('/')
def puchu():
    return render_template("puchu.html")

@app.route('/bapan')
def puchi():
    return render_template("bapan.html")