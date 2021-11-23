from flask import Flask,jsonify,Response 
from bson import json_util
from pymongo import MongoClient
from pprint import pprint

app = Flask(__name__)

# connessioneDB = "mongodb://Bestie:BelleVacche01@bestiario.bku3d.mongodb.net"
#"mongodb://Bestie:BelleVacche01@bestiario.bku3d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
#if __name__ == "app_prod":
    # connessioneDB = "mongodb://localhost:27017"

#client = MongoClient(connessioneDB)
#db=client.Bestiario


def get_database():
    CONNECTION_STRING = "mongodb://Bestie:BelleVacche01@bestiario-shard-00-00.bku3d.mongodb.net:27017,bestiario-shard-00-01.bku3d.mongodb.net:27017,bestiario-shard-00-02.bku3d.mongodb.net:27017/Bestiario?ssl=true&replicaSet=atlas-rph8gy-shard-0&authSource=admin&retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING, connect=False)
    return client['Bestiario']

def get_local_database():
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    return client['Bestiario']

print("avvio:" + __name__)
if __name__ == "app_prod":
    db = get_database()
else:
    db = get_local_database()






@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>" + __name__


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

