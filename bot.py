#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import telegram

import bot


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')
    
def fuck(update, context):
    """Send a message when the command /fuck is issued."""
    update.message.reply_text('come lets do sex!')

def hai(update, context):
    """Send a message when the command /hai is issued."""
    update.message.reply_text('hello how are you')


def echo(update, context):
    """Echo the user message."""
    mes = update.message.text
    sender = update.message.chat.first_name or update.message.chat.title
    
    if update.message.text.lower() == 'hai' or update.message.text.lower() == 'hi' :
       update.message.reply_text("hai how are you") 
       update.message.reply_text("❤️") 
       update.message.reply_text(sender)
       pic='t_logo.png'
       
       context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(pic,'rb'))
       
    
    update.message.reply_text(update.message.text)
    

    print(update.message.text)

def photo_handler(update, context):
    
    fileid = file_id = update.message.photo[-1].file_id
    img = 'AgACAgUAAxkBAAPhYY_0PJPm26fFXI1CY16m3lzbxFEAAqytMRuuy3lUA0If8V2l7rYBAAMCAAN5AAMiBA'
    pic='t_logo.png'
    
    
    update.message.reply_text(update.message.photo.file_name)
    
    print (fileid)
    
def file_handler(update, context):
    update.message.reply_text("I Recognied This as a document ")
    print (update.message.document.file_name)
    
    fileid = file_id = update.message.document[-1].file_id
    img = 'AgACAgUAAxkBAAPhYY_0PJPm26fFXI1CY16m3lzbxFEAAqytMRuuy3lUA0If8V2l7rYBAAMCAAN5AAMiBA'
    pic='t_logo.png'
    
    
    
    
    print (fileid)
    newFile = bot.get_file(file_id)
    filename = update.message.document[-1].file_name
    newFile.download("userfiles/"+filename)
    update.message.reply_text("userfiles/"+filename)
    
    
    
def admin_handler(update, context):
    update.message.reply_text("Yes I am Online")
    if update.message.chat.username == 'g4_media' :
       update.message.reply_text('Greetings Master')
       file = update.message.document[-1]
       update.message.replyDocument(update.message.document.thumb[-1])
       context.bot.sendDocument(chat_id=update.effective_chat.id, document=open(file, 'rb'), filename="sample.pdf")    
    
    
    
    



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1433983998:AAHoiInziufUT9MOF51LFzRKnJR1xZcJquI", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("fuck", fuck))
    dp.add_handler(CommandHandler("hai", hai))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.photo, photo_handler))
    dp.add_handler(MessageHandler(Filters.document, file_handler))
    dp.add_handler(MessageHandler(Filters.all, admin_handler))
    

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
