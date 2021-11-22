from flask import Flask,jsonify,Response 
from bson import json_util
from pymongo import MongoClient
from pprint import pprint

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db=client.Bestiario


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/isAliveDB")
def isAliveDB():
    serverStatusResult=db.command("serverStatus")
    pprint(serverStatusResult)
    return "AA"


@app.route("/get/<id>")
def get(id):
    print('A sample document:')
    ASingleReview = db.Mucca.find_one({'_id': id})
    print('A sample document:')
    pprint(ASingleReview)
    return  pprint(ASingleReview)


@app.route("/getByName/<nome>")
def getByName(nome):
    print('getByName ' + nome)
    mucca = db.Mucca.find_one({'nome': nome})
    pprint(mucca)
    return  Response(mucca,mimetype='application/json')


@app.route("/getMucche")
def getMucche():
    print('getMucche ')
    mucche = db.Mucca.find()
    list_cur = list(mucche)
    # Converting to the JSON
    json_data = json_util.dumps(list_cur, indent = 2)
    pprint(json_data)
    return json_data

