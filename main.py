import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackContext
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN




logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Define a function to handle the /start command
def start(update: Update, context: CallbackContext):
    user_name = update.message.from_user.first_name
    update.message.reply_text(f"Hola, {user_name}! Welcome to the Stock Tracker Bot.")



async def show_menu(update, context):
    # Create keyboard buttons
    keyboard = [
        [KeyboardButton("Button 1")],
        [KeyboardButton("Button 2")]
    ]

    # Create a reply keyboard markup
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Send a message with the keyboard
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Choose an option:",
        reply_markup=reply_markup
    )


async def start(update, context):
    # Create inline keyboard buttons
    keyboard = [
        [InlineKeyboardButton("Button 1", callback_data='button1')],
        [InlineKeyboardButton("Button 2", callback_data='button2')]
    ]

    # Create an inline keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the inline keyboard
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Choose an option:",
        reply_markup=reply_markup
    )


async def info(update: Update, context: CallbackContext):
    bot_info = await context.bot.get_me()
    text = f"Bot Name: {bot_info.first_name}\nUsername: @{bot_info.username}\nID: {bot_info.id}"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


async def reply_to_message(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I received your message!")



if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', show_menu)
    info_handler = CommandHandler('info', info)
    
    application.add_handlers([start_handler, info_handler])

    application.run_polling()
