from FM.DBClient import DBClient
from FM.DBDatabase import DBDatabase

_client_object = DBClient()
CLIENT = lambda ip, port: _client_object.connect(ip, port)
def get_mongo_client(ip="192.168.1.180", port=27017):
    DBClient().connect(ip, port)
def get_brain_db(client:DBClient):
    return DBDatabase(dbclient=client).database("brain")
def get_research_db(client:DBClient):
    return DBDatabase(dbclient=client).database("research")