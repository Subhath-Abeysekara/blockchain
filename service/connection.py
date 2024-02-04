from pymongo import MongoClient
import os

def connect_mongo_complain():
    CONNECTION_STRING = "mongodb+srv://icodeinnovahostingservice:pi1p1MQQcIRWOEHp@fitsixes.1begbkj.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db_Name = client['crime_project']
    collection_name = db_Name["complain"]
    return collection_name

