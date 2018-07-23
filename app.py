from flask import Flask, request
from flask import render_template
from giffer import Giffer


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
    searchterms = request.form['searchterms']
    a = Giffer(searchterms)
    a.makeRequest()
    a.jsonifyResult()
    a.getGifList(50)
    a.shuffleGifs()
    resultloop = a.gifs_list

    return render_template('resultloop.html', resultloop=resultloop, searchterms=searchterms)
