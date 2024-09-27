import os
import json
from pymongo import MongoClient
from config import JSON_FILE, MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def find_or_store_answer(question):
    """Finds or stores questions that don't have predefined answers."""
    stored_answer = db.qa_storage.find_one({"question": question})
    if stored_answer:
        return stored_answer['answer']

    db.qa_storage.insert_one({"question": question, "answer": "pending"})
    log_question_to_json(question)
    return "Your question has been recorded. We'll get back to you soon!"

def update_answer_from_json():
    """Updates answers from the JSON file."""
    with open(JSON_FILE, 'r', encoding='utf-8') as file:
        qa_data = json.load(file)
        for entry in qa_data:
            db.qa_storage.update_one(
                {"question": entry["question"]},
                {"$set": {"answer": entry["answer"]}},
                upsert=True
            )

def log_question_to_json(question):
    """Logs unanswered questions to JSON file."""
    new_entry = {"question": question, "answer": "pending"}
    
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data.append(new_entry)
            file.seek(0)
            json.dump(data, file, indent=4)
    else:
        with open(JSON_FILE, 'w', encoding='utf-8') as file:
            json.dump([new_entry], file, indent=4)
