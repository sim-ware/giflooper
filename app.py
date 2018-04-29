from flask import Flask
app = Flask(__name__)


##
# Index/Home Route
##################
@app.route('/index')
@app.route('/')
def index():
    return 'Search Page'

##
# Results Route
###############
@app.route('/resultloop')
def hello():
    return 'Resultloop'
