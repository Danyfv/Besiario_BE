from flask import Flask,jsonify,Response 
from pprint import pprint
from bson import json_util
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_pyfile('config.py')
pprint(app.config.get("ENVIRONMENT"))



@app.route("/")
def hello_world():
    return "<p>Hello </p>" + __name__ + "  " + app.config.get("ENVIRONMENT")


@app.route("/isAliveDB")
def isAliveDB():
    return "AA"


@app.route("/get/<id>")
def get(id):
    return "" + id


@app.route("/getByName/<nome>")
def getByName(nome):
    db = getDb();
    mucca = db.execute("select * from mucca where nome = \'" + nome + "\'").fetchall() 
    db.close()
    return jsonify(mucca)


@app.route("/getMucche")
def getMucche():
    db = getDb();
    mucche = db.execute('select * from mucca').fetchall() 
    db.close()
    return jsonify(mucche)



def convertiInJson(elemento):
    json_data = json_util.dumps(elemento, indent = 2)
    pprint(json_data)
    return json_data

def getDb():
    return sqlite3.connect(app.config.get("DATABASE_URI"))
