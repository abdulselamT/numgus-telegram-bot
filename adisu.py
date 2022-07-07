import telebot
from telebot import types
from telebot import custom_filters
from telegram import ReplyMarkup
from adiscon import API_KEY
import random
legmem={}
bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])
def start_message(msg):
    print(msg)
    try:
        r1 = random.randint(1, 1000)
        legmem[msg.chat.id]=[r1,1]
        bot.reply_to(msg,'ከ 1 አስከ 1000 ቁጥር ይዣለው 10 ጊዘ ገምታቹ ካገኛቹ ኣሸነፋቹ ማለት ነው አስኪ ጀምሩ')
    except:
        legmem[msg.chat.id]=[r1,1]
        bot.reply_to(msg,'ከ 1 አስከ 1000 ቁጥር ይዣለው 10 ጊዘ ገምታቹ ካገኛቹ ኣሸነፋቹ ማለት ነው አስኪ ጀምሩ')


#bot.send_photo(chat_id= -1001575818933,photo=open('joly.jpg', 'rb'))

@bot.message_handler(is_digit=True)
def echo(msg):
    try:
        b=legmem[msg.chat.id]
    except:
        bot.reply_to(msg,"please tap the /start button")
        return 0
    if legmem[msg.chat.id][1]>=10:
        bot.reply_to(msg,"teshenfehal yeyazkut "+str(legmem[msg.chat.id][0])+ " new")
        legmem.pop(msg.chat.id, None)
    elif int(msg.text)>legmem[msg.chat.id][0]:
        bot.reply_to(msg,"ዝቅ")
        legmem[msg.chat.id][1]=legmem[msg.chat.id][1]+1
    elif int(msg.text)<legmem[msg.chat.id][0]:
        bot.reply_to(msg,"ከፍ")
        legmem[msg.chat.id][1]=legmem[msg.chat.id][1]+1
    else:
        bot.reply_to(msg,"👍",ReplyMarkup=markup)
        legmem.pop(msg.chat.id, None)
        
@bot.message_handler(func= lambda m:True)
def msf(msg):
    bot.reply_to(msg,"good to see you")

bot.add_custom_filter(custom_filters.IsDigitFilter())

bot.infinity_polling()
