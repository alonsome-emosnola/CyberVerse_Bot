import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

pwd = os.environ["MONGODB_PWD"]
uri = f"mongodb+srv://cyberversecbv:{pwd}@cyberverse.8labz2y.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
def post_wallet(query):
    try:
        db = client.CyberVerse
        db.wallets.insert_one(query)
    except:
        raise Exception("Error during insertion, please check")

def read_wallet(query1, query2):
    try:
        db = client.CyberVerse
        wallet = db.wallets.find_one(query1, query2)
    except:
        raise Exception("Error reading value from database, please review")
    else:
        return wallet["wallet"]

def post_link(query):
    try:
        db = client.CyberVerse
        db.links.insert_one(query)
    except:
        raise Exception("Error during insertion, please check")

def read_link(query1, query2):
    try:
        db = client.CyberVerse
        link = db.links.find_one(query1, query2)
    except:
        raise Exception("Error reading value from database, please review")
    else:
        return link["referral_link"]