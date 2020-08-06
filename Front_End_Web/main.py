from flask import Flask
from flask import jsonify
from flask import request
import os
import csv
from flask import render_template
from flask_bootstrap import Bootstrap


# declair some image for 'Government_Measures' page
data = {}
data["Germany"] = "/static/Germany.png"
data["USA"] = "/static/USA.png"
data["Italy"] = "/static/Italy.png"
data["China"] = "/static/China.png"
data["Spain"] = "/static/Spain.png"
data["UnitedKingdom"] = "/static/UnitedKingdom.png"
data["italyGoverment"] = "/static/italyGoverment.png"
data["ChinaGoverment"] = "/static/ChinaGoverment.png"
data["Canada"] = "/static/Canada.png"

app = Flask(__name__)
bootstrap = Bootstrap(app)

# set main page
@app.route('/')
def index():
    return render_template('index.html')

# set 'EDA' page
@app.route('/EDA')
def EDA():
    return render_template('EDA.html',name="neow")

# set click response on 'Government_Measures' page image
@app.route('/Government_Measures')
def Government_Measures():
    return render_template('Impact.html',name="neow")

# set click response on 'Government_Measures' page image
@app.route('/Impact/<name>/',methods=['GET'])
def ss(name):
    print(name)
    return render_template('Detal.html',name=name,url=data[name])




if __name__ == '__main__':
    
    # init()
    app.debug = False
    # any port can visit this website
    app.run(host='0.0.0.0', port=8888, debug=True)
