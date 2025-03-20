from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import API_TOKEN
import mysql.connector
import logging
import stripe

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

bot = TeleBot(API_TOKEN)

# Stripe API Key (Replace with your actual secret key)
STRIPE_API_KEY = "sk_test_XXXXXXXXXXXXXXXXXXXXXXXX"
stripe.api_key = STRIPE_API_KEY

# Database Connection (Replace with real credentials)
def get_db_connection():
    return mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_database"
    )

# Function to fetch user balance from DB
def get_user_balance(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else 0.00

# Function to create a Stripe checkout session
def create_stripe_checkout(user_id, amount):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': 'Wallet Top-Up'},
                    'unit_amount': amount * 100,
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='https://yourdomain.com/success',
        cancel_url='https://yourdomain.com/cancel',
    )
    return session.url

# Profile Menu
profile_menu = InlineKeyboardMarkup(row_width=1)
profile_buttons = [
    InlineKeyboardButton(text="💰 Account Balance", callback_data="account_balance"),
    InlineKeyboardButton(text="➕ Add Funds", callback_data="add_funds"),
    InlineKeyboardButton(text="📄 FAQ", callback_data="profile_faq"),
    InlineKeyboardButton(text="👤 Personal Data", callback_data="personal_data"),
    InlineKeyboardButton(text="⬅ Back to Main Menu", callback_data="back_main")
]
profile_menu.add(*profile_buttons)

# /my_profile command handler
@bot.message_handler(commands=['my_profile'])
def my_profile(message):
    bot.send_message(message.chat.id, "📋 Your Profile Menu:", reply_markup=profile_menu)

# Handling profile menu selections
@bot.callback_query_handler(func=lambda call: call.data == "account_balance")
def account_balance(call):
    user_id = call.from_user.id
    balance = get_user_balance(user_id)
    bot.send_message(call.message.chat.id, f"💰 Your current balance is: ${balance:.2f}")

@bot.callback_query_handler(func=lambda call: call.data == "add_funds")
def add_funds(call):
    payment_menu = InlineKeyboardMarkup(row_width=1)
    amounts = [10, 50, 100]
    for amt in amounts:
        payment_menu.add(InlineKeyboardButton(text=f"💳 Pay ${amt}", callback_data=f"pay_{amt}"))
    payment_menu.add(InlineKeyboardButton(text="⬅ Back to Profile", callback_data="my_profile"))
    bot.send_message(call.message.chat.id, "Choose the amount to add:", reply_markup=payment_menu)

# Handling Stripe payments
@bot.callback_query_handler(func=lambda call: call.data.startswith("pay_"))
def process_payment(call):
    amount = int(call.data.split("_")[1])
    payment_url = create_stripe_checkout(call.from_user.id, amount)
    bot.send_message(call.message.chat.id, f"🔗 Click to complete your payment: {payment_url}")

@bot.callback_query_handler(func=lambda call: call.data == "personal_data")
def personal_data(call):
    bot.send_message(call.message.chat.id, "📜 Your registered data:\nName: John Doe\nEmail: johndoe@example.com")

@bot.callback_query_handler(func=lambda call: call.data == "profile_faq")
def profile_faq(call):
    bot.send_message(call.message.chat.id, "Profile FAQ:\n1. How to add funds?\n2. How to check balance?\n3. How to contact support?")

# Back to main menu
@bot.callback_query_handler(func=lambda call: call.data == "back_main")
def back_to_main_menu(call):
    bot.send_message(call.message.chat.id, "Bine ați revenit la meniul principal!", reply_markup=profile_menu)

bot.polling()
