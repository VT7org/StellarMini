import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = MongoClient(MONGO_URI)
db = client.tg_music

def init_mongo():
    print("MongoDB initialized.")

async def is_admin(user_id):
    return db.admins.find_one({"user_id": user_id}) is not None

async def get_all_users():
    return list(db.users.find({}))