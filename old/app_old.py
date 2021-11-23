from flask import Flask,jsonify,Response 
from bson import json_util
from pymongo import MongoClient
from pprint import pprint


def get_database(CONNECTION_STRING):
    client = MongoClient(CONNECTION_STRING, connect=False)
    return client['Bestiario']

app = Flask(__name__)
app.config.from_pyfile('config.py')

pprint(app.config.get("ENVIRONMENT"))
db = get_database(app.config.get("DATABASE_URI"))

@app.route("/")
def hello_world():
    return "<p>Hello </p>" + __name__ + "  " + app.config.get("ENVIRONMENT")


@app.route("/isAliveDB")
def isAliveDB():
    serverStatusResult=db.command("serverStatus")
    pprint(serverStatusResult)
    return "AA"


@app.route("/get/<id>")
def get(id):
    ASingleReview = db.Mucca.find_one({'_id': id})
    return convertiInJson(ASingleReview)


@app.route("/getByName/<nome>")
def getByName(nome):
    mucca = db.Mucca.find_one({'nome': nome})
    return convertiInJson(mucca)


@app.route("/getMucche")
def getMucche():
    mucche = db.Mucca.find()
    return convertiInJson(mucche)



def convertiInJson(elemento):
    list_cur = list(elemento)
    json_data = json_util.dumps(list_cur, indent = 2)
    pprint(json_data)
    return json_data
