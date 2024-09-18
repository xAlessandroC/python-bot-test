import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CommandHandler

load_dotenv()

# Function that responds with "Hello World" to any message
async def respond_hello_world(update: Update, context):
    await update.message.reply_text("Hello World")

def main():
    # Insert your API token here
    TOKEN = os.getenv("BOT_TOKEN")

    # Create the application
    application = Application.builder().token(TOKEN).build()

    # Add a handler to respond to text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond_hello_world))

    # Start the bot
    application.run_polling()
    

if __name__ == '__main__':
    main()
