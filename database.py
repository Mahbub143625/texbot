from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def log_user_message(user_id, user_message, bot_response):
    """Logs user messages and bot responses to MongoDB."""
    db.conversations.insert_one({
        "user_id": user_id,
        "user_message": user_message,
        "bot_response": bot_response
    })

def log_user_profile(user_profile):
    """Logs user profile information."""
    db.users.update_one(
        {"user_id": user_profile['user_id']},
        {"$set": user_profile},
        upsert=True
    )

def get_all_users():
    """Retrieves all users from the database."""
    return db.users.find()
