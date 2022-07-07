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
        legmem[msg.from_user.id]=[r1,1]
        bot.reply_to(msg,msg.from_user.first_name +' ከ 1 አስከ 1000 ቁጥር ይዣለው 10 ጊዘ ገምታቹ ካገኛቹ ኣሸነፋቹ ማለት ነው አስኪ ጀምሩ')
    except:
        legmem[msg.from_user.id]=[r1,1]
        bot.reply_to(msg,msg.from_user.first_name + ' ከ 1 አስከ 1000 ቁጥር ይዣለው 10 ጊዘ ገምታቹ ካገኛቹ ኣሸነፋቹ ማለት ነው አስኪ ጀምሩ')


#bot.send_photo(chat_id= -1001575818933,photo=open('joly.jpg', 'rb'))

@bot.message_handler(is_digit=True)
def echo(msg):
    print(msg)
    try:
        b=legmem[msg.from_user.id]
    except:
        bot.reply_to(msg,"please tap the /start button")
        return 0
    if legmem[msg.from_user.id][1]>=10:
        bot.reply_to(msg,msg.from_user.first_name + " teshenfehal yeyazkut "+str(legmem[msg.from_user.id][0])+ " new")
        legmem.pop(msg.from_user.id, None)
    elif int(msg.text)>legmem[msg.from_user.id][0]:
        bot.reply_to(msg,str(legmem[msg.from_user.id][1]) + " ዝቅ")
        legmem[msg.from_user.id][1]=legmem[msg.from_user.id][1]+1
    elif int(msg.text)<legmem[msg.from_user.id][0]:
        bot.reply_to(msg,str(legmem[msg.from_user.id][1]) + " ከፍ")
        legmem[msg.from_user.id][1]=legmem[msg.from_user.id][1]+1
    else:
        bot.reply_to(msg,"👍")
        legmem.pop(msg.from_user.id, None)


bot.add_custom_filter(custom_filters.IsDigitFilter())

bot.infinity_polling()
