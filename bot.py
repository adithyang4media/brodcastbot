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
import os
import sys




import bot
from telegram.ext import ConversationHandler


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

GENDER, NAMER, VOICE, BIO = range(4)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
    update.message.reply_text('This Bot Was Made By @g4_media')
    update.message.reply_text('Please Consider Subscribing our Youtube Channel https://www.youtube.com/channel/UCad4U0t57KqjvHxqqdmZW_w')


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
       update.message.reply_text('This Bot Was Made By @g4_media')
       update.message.reply_text('Please Consider Subscribing our Youtube Channel https://www.youtube.com/channel/UCad4U0t57KqjvHxqqdmZW_w')


       
       context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(pic,'rb'))
    
    elif "http" in mes: 
         def is_downloadable(url):
             """
             Does the url contain a downloadable resource
             """
             h = requests.head(url, allow_redirects=True)
             header = h.headers
             content_type = header.get('content-type')
             if 'text' in content_type.lower():
                 return False
             if 'html' in content_type.lower():
                 return False
             return True
         if str(is_downloadable(mes)):
            update.message.reply_text("Hey it is an Downloadable Link")
            if mes.find('/'):
               filesname=mes.rsplit('/', 1)[1]
               url = mes
               r = requests.get(url, allow_redirects=True)

               open(filesname, 'wb').write(r.content)
               context.bot.sendDocument(chat_id=update.effective_chat.id, document=open(filesname, 'rb'), filename=filesname)
               os.remove(filesname)
               
         else : update.message.reply_text("Hey it is not an Downloadable Link")
    
    update.message.reply_text(update.message.text)
    

    print(update.message.text)

def photo_handler(update, context):
    
    fileid = file_id = update.message.photo[-1].file_id
    img = 'AgACAgUAAxkBAAPhYY_0PJPm26fFXI1CY16m3lzbxFEAAqytMRuuy3lUA0If8V2l7rYBAAMCAAN5AAMiBA'
    pic='t_logo.png'
    
    
    update.message.reply_photo(update.message.photo[-1])
    
    print (fileid)
    
def file_handler(update, context):
    update.message.reply_text(update.message.document.mime_type)
    update.message.reply_text(update.message.document.file_name)
    update.message.reply_text(update.message.document.file_id)
    update.message.reply_text("I Recognied This as a document ")
    print (update.message.document.file_name)
    
    
    global filesname
    fileid = update.message.document.file_id
    filesname = update.message.document.file_name
    file = context.bot.getFile(fileid)
    file.download(filesname)
    update.message.reply_text(update.message.document.file_name)
    
    context.bot.sendDocument(chat_id=update.effective_chat.id, document=open(filesname, 'rb'), filename=filesname)
    
    update.message.reply_text("Enter File Name With Extention")
    
    return NAMER
    
    
    
    
    
def rename(update, context):
    update.message.reply_text("OK")
    fln=update.message.text
    if fln == "/cancel" :
       python = sys.executable
       os.execl(python, python, * sys.argv)
    context.bot.sendDocument(chat_id=update.effective_chat.id, document=open(filesname, 'rb'), filename=fln)
    os.remove(filesname)
    update.message.reply_text("Thank You Have A Nice Day")
    update.message.reply_text('This Bot Was Made By @g4_media')
    update.message.reply_text('Please Consider Subscribing our Youtube Channel https://www.youtube.com/channel/UCad4U0t57KqjvHxqqdmZW_w')


    
    
def admin_handler(update, context):
    update.message.reply_text("Yes I am Online")
    if update.message.chat.username == 'g4_media' :
       update.message.reply_text('Greetings Master')
       file = update.message.document[-1]
       update.message.replyDocument(update.message.document.thumb[-1])
       context.bot.sendDocument(chat_id=update.effective_chat.id, document=open(file, 'rb'), filename="sample.pdf")    
      
       
    
    

    
    
def audio_handler(update, context):
    update.message.reply_text(update.message.audio.mime_type)
    update.message.reply_text(update.message.audio.file_name)
    update.message.reply_text(update.message.audio.file_id)
    update.message.reply_text("I Recognied This as a Audio File ")
    print (update.message.audio.file_name)
    
    
    global filesname
    fileid = update.message.audio.file_id
    filesname = update.message.audio.file_name
    voicename = filesname + ".ogg"
    file = context.bot.getFile(fileid)
    file.download(filesname)
    update.message.reply_text(update.message.audio.file_name)
    
    context.bot.sendDocument(chat_id=update.effective_chat.id, document=open(filesname, 'rb'), filename=filesname)
    context.bot.sendDocument(chat_id=update.effective_chat.id, document=open(filesname, 'rb'), filename=voicename)
    os.remove(filesname)
    update.message.reply_text('This Bot Was Made By @g4_media')
    update.message.reply_text('Please Consider Subscribing our Youtube Channel https://www.youtube.com/channel/UCad4U0t57KqjvHxqqdmZW_w')


    
    
def voice_handler(update, context):
    update.message.reply_text(update.message.voice.mime_type)
    
    update.message.reply_text(update.message.voice.file_id)
    update.message.reply_text("I Recognied This as a Voice Message ")
    global fileid
    fileid = update.message.voice.file_id
    
    update.message.reply_text("Please Enter Name For Audio File with Desired Extention ")
    
    return VOICE
    
    

    
def voup(update, context):
    update.message.reply_text("OK")
    fln=update.message.text
    
    if fln == "/cancel" :
       python = sys.executable
       os.execl(python, python, * sys.argv)
      
    global file
    
    
    file = context.bot.getFile(fileid)
    file.download(fln)
    update.message.reply_text(fln)
    
    
    context.bot.sendDocument(chat_id=update.effective_chat.id, document=open(fln, 'rb'), filename=fln)
    context.bot.sendAudio(chat_id=update.effective_chat.id, audio=open(fln, 'rb'), filename=fln)
    os.remove(fln)
    update.message.reply_text("Thank You Have A Nice Day")
    update.message.reply_text('This Bot Was Made By @g4_media')
    update.message.reply_text('Please Consider Subscribing our Youtube Channel https://www.youtube.com/channel/UCad4U0t57KqjvHxqqdmZW_w')




def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    update.message.reply_text("Sorry Error Occured   " + str(context.error))
    
def cancel(update, context):
    update.message.reply_text("Current Operation Canceled")
    os.remove(filesname)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(os.environ['bottoken'], use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("fuck", fuck))
    dp.add_handler(CommandHandler("hai", hai))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.photo, photo_handler))
    # dp.add_handler(MessageHandler(Filters.document, file_handler))
    # dp.add_handler(MessageHandler(Filters.all, admin_handler))
    
    
    
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.document, file_handler)],
        states={
            
            NAMER: [MessageHandler(Filters.text, rename)]
            
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
 
    dp.add_handler(conv_handler)
  
    con_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.voice, voice_handler)],
        states={
            
            VOICE: [MessageHandler(Filters.text, voup)]
            
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
 
    dp.add_handler(con_handler)
  
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.audio, audio_handler))
    dp.add_handler(MessageHandler(Filters.voice, voice_handler))

    

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
