import json
from flask import Flask
from flask import render_template, request
from flask import request


HOME_DIR = ''
static_folder = HOME_DIR + '/static'
template_folder = HOME_DIR + '/templates'
app = Flask(__name__)


@app.route("/")
def index(name=None):
   return render_template('index.html', name=name)


@app.route("/other_page")
@app.route("/other_page/<data>")
def other(data=1):
   return json.dumps({'building_name': 'Tower 49'})


app.config.from_object('config')
app.run()