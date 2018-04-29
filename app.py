from flask import Flask
from flask import render_template
app = Flask(__name__)


##
# Index/Home Route
##################
@app.route('/giflooper', methods=['GET'])
@app.route('/')
def index():
    return render_template('home.html')

##
# Results Route
###############
@app.route('/resultloop', methods=['POST'])
def resultloop():
    # return 'Resultloop'
    # searchterms = request.form['searchterms']
    return render_template('resultloop.html')



# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
