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
async def post_to_db(**kwargs):
    try:
        db = client.CyberVerse
        post = await db.wallets.insert_one(kwargs).acknowledged
    except Exception as e:
        raise e("Error during insertion, please check", e)
    else:
        return post

async def read_from_db(**kwargs):
    try:
        db = client.CyberVerse
        read = db.wallets.find_one(kwargs).acknowledged
    except Exception as e:
        raise e("Error reading value from database, please review", e)
    else:
        return read