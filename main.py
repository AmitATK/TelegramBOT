from telegram.ext import *
import tokenn
from datetime import date  
print("Booting the bot..")

def start_command(update, context):
    update.message.reply_text("Hello there!What\'s up?")

def help_command(update, context):
    update.message.reply_text("Please Type to get answer")


def custom_command(update, context):
    update.message.reply_text("This is the custom command, you can add your desire text.")

def handle_response(text) -> str:
    #custom command
    if "Hello" in text:
        return "Hey Buddy!"

    if "How are you" in text:
        return "I\'m good!"
    if "Today date" in text:
        td = date.today()
        return "Today date is", td
         
    return "I don\'t understand"


def handle_message(update, context):
    # Get basic info of the incoming message
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if '@bot19292bot' in text:
            new_text = text.replace('@bot19292bot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    # Reply normal if the message is in private
    update.message.reply_text(response)


# Log errors
def error(update, context):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    updater = Updater(tokenn.token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
