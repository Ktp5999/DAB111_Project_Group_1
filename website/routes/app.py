from flask import Flask
from home import home
from about import about
from data import data

app = Flask(__name__)

app.add_url_rule('/', 'home', home)
app.add_url_rule('/about', 'about', about)
app.add_url_rule('/data', 'data', data)

run_simple('localhost',8080,app,use_reloader=False, use_debugger=False)
