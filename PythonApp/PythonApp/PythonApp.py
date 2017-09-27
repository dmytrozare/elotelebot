import telebot
import re

bot = telebot.TeleBot("363495179:AAGv53SUW8K5c9_aQpyUvzdWxSTpoqbk5BE") #already created bot, let's join to group https://t.me/joinchat/EpNnZkAjUWYrvMWH4Xqwnw 
@bot.message_handler(commands=['start','kikdenis'])
def kik_member(message):
    if(message.text == "/kikdenis"):
	    bot.kick_chat_member(message.chat.id,144452506,1506175439) #method for kiking member from group
	    bot.reply_to(message, "kik, Denis!") #just sending messag to group

@bot.message_handler(content_types=["new_chat_members"])
def echo_all(message):
	bot.send_message(message.chat.id, "Hello, @%s"%(message.new_chat_member.username)) #bot will be react if someone joined to group

@bot.message_handler(content_types=["text"])
def delete_spam(message):
    url = []
    isUrl = False
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text) #find url in messages
    ethereum = re.search(r'(0x)?[0-9a-f]{40}$',message.text,re.I) #simple antifrod 
    if ethereum is not None : ethereum = ethereum.group()
    if not (message.entities is None): 
        if(message.entities[0].type=="url"): #another method from Telegram api, for detecting url in messages
            isUrl=True
    if(len(url)>0 or isUrl or (ethereum is not None)):
        administrators = bot.get_chat_administrators(message.chat.id) 
        is_admin = False
        for i in administrators:
            if(i.user.id==message.from_user.id):
                is_admin = True
        if not is_admin:
            bot.delete_message(message.chat.id, message.message_id)
            


# Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
# - none_stop: True/False (default False) - Don't stop polling when receiving an error from the Telegram servers
# - interval: True/False (default False) - The interval between polling requests
#           Note: Editing this parameter harms the bot's response time
# - timeout: integer (default 20) - Timeout in seconds for long polling.
bot.polling(none_stop=False, interval=0, timeout=20)
