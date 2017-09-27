import telebot
import re

bot = telebot.TeleBot("363495179:AAGv53SUW8K5c9_aQpyUvzdWxSTpoqbk5BE")
@bot.message_handler(commands=['start','kikdenis'])
def kik_member(message):
    if(message.text == "/kikdenis"):
	    bot.kick_chat_member(message.chat.id,144452506,1506175439)
	    bot.reply_to(message, "kik, Denis!")

@bot.message_handler(content_types=["new_chat_members"])
def echo_all(message):
	bot.send_message(message.chat.id, "Hello, @%s"%(message.new_chat_member.username))

@bot.message_handler(content_types=["text"])
def delete_spam(message):
    url = []
    isUrl = False
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text)
    ethereum = re.search(r'(0x)?[0-9a-f]{40}$',message.text,re.I)
    if ethereum is not None : ethereum = ethereum.group()
    if not (message.entities is None):
        if(message.entities[0].type=="url"):
            isUrl=True
    if(len(url)>0 or isUrl or (ethereum is not None)):
        administrators = bot.get_chat_administrators(message.chat.id)
        is_admin = False
        for i in administrators:
            if(i.user.id==message.from_user.id):
                is_admin = True
        if not is_admin:
            bot.delete_message(message.chat.id, message.message_id)
            



bot.polling(none_stop=False, interval=0, timeout=20)
