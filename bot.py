import os
from queue import Queue
from telegram import Update
from telegram.ext import Updater, dispatcher, CommandHandler, MessageHandler, filters, CallbackContext

# Function to handle incoming messages
def auto_reply(update: Update, context: CallbackContext) -> None:
    # Reply with a custom message
    update.message.reply_text("Hey there! I'm currently offline, but I'll get back to you soon.")

# Main function to set up the bot
def main():
    # Create an update queue
    update_queue = Queue()

    # Set up the Updater with the environment variable TELEGRAM_BOT_TOKEN
    updater = Updater(os.environ['TELEGRAM_BOT_TOKEN'], update_queue=update_queue)

    # Get the dispatcher (directly imported)
    dispatcher = updater.dispatcher

    # Add a message handler to respond to all text messages
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, auto_reply))

    # Start polling for updates
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()