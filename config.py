import os

# Directory paths
PDF_FOLDER = os.path.join("data", "pdf_files")
TEXT_FOLDER = os.path.join("data", "text_files")
JSON_FILE = os.path.join("data", "qa_storage.json")

# MongoDB connection details (assuming localhost for now)
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "telegram_bot_db"
