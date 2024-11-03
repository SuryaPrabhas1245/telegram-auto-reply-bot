from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Function to handle incoming messages
def auto_reply(update: Update, context: CallbackContext) -> None:
    # Reply with a custom message
    update.message.reply_text("Hey there! I'm currently offline, but I'll get back to you soon.")

# Main function to set up the bot
def main():
    # Set up the Updater with your bot token
    updater = Updater("8177260502:AAGbD5iUoWLJtTJ0givGe9QE89dLIuUqxRc")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add a message handler to respond to all text messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, auto_reply))

    # Start polling for updates
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
