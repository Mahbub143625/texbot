import telebot
from telebot import types
from math_solver import solve_textile_math
from textile_search import find_textile_info
from dialoGPT_chat import get_chat_response
from database import log_user_message, log_user_profile, get_all_users
from question_answer_storage import find_or_store_answer, update_answer_from_json
from config import PDF_FOLDER, TEXT_FOLDER, JSON_FILE

# Initialize Telegram Bot with your API token
bot = telebot.TeleBot("7318496042:AAFSw093UXniC742R4PFODCzGTx_is9rUEU")

# Create custom keyboard with reset and notification options
def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    reset_btn = types.KeyboardButton('Reset Conversation')
    notify_btn = types.KeyboardButton('Notify All Users')
    markup.add(reset_btn, notify_btn)
    return markup

# Handle /start command and show the menu
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_profile = {
        "user_id": message.from_user.id,
        "username": message.from_user.username,
        "first_name": message.from_user.first_name
    }
    log_user_profile(user_profile)
    bot.send_message(message.chat.id, "Welcome to the bot!", reply_markup=main_menu())

# Handle math queries
@bot.message_handler(func=lambda message: "math" in message.text.lower())
def handle_math(message):
    result = solve_textile_math(message.text)
    bot.reply_to(message, result)
    log_user_message(message.from_user.id, message.text, result)

# Handle textile queries
@bot.message_handler(func=lambda message: "textile" in message.text.lower())
def handle_textile(message):
    answer = find_textile_info(message.text)
    if not answer:
        # Check if we can find or store the question in storage
        answer = find_or_store_answer(message.text)
    bot.reply_to(message, answer)
    log_user_message(message.from_user.id, message.text, answer)

# Handle casual conversations using DialoGPT
@bot.message_handler(func=lambda message: True)
def handle_chat(message):
    response = get_chat_response(message.text)
    bot.reply_to(message, response)
    log_user_message(message.from_user.id, message.text, response)

# Handle reset conversation
@bot.message_handler(func=lambda message: message.text == 'Reset Conversation')
def handle_reset(message):
    bot.reply_to(message, "Conversation has been reset.", reply_markup=main_menu())

# Handle notifications to all users
@bot.message_handler(func=lambda message: message.text == 'Notify All Users')
def notify_all_users(message):
    users = get_all_users()
    notification = "This is a global notification!"
    for user in users:
        try:
            bot.send_message(user['user_id'], notification)
        except:
            continue
    bot.reply_to(message, "Notification sent to all users!")

# Start polling for messages
bot.polling()
