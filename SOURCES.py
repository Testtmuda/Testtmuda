import telebot 
from telebot import types
import requests



bot = telebot.TeleBot("2138298056:AAHYMpVCCBpXxWrTDZ9NUXiiOJCCi8XNsw4")
r=requests.session() 
mud8 = types.InlineKeyboardButton(text="DEV ",url="https://t.me/m9yum")
mud2 = types.InlineKeyboardButton(text="DEV",url="https://t.me/m9yum")

@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(mud8)
    bjj = message.chat.id
    messagee = bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{fr}</code>, 
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
WELCOME TO THE BOT TO BRING TEH CHANNELS OF THE SOURCES 
[SHOW THE SOURCES SEND] /SOURCES
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
DEV @M9YUM
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)

	
@bot.message_handler(commands=['SOURCES'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(mud2)
    bjj = message.chat.id
    messagee = bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{fr}</code>, 
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
[/aria]
/
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
DEV @M9YUM
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)

	
@bot.message_handler(commands=['aria'])
def start(message):
	bot.send_message(message.chat.id,f"git clone https://github.com/Sources2022/ARIA && cd ARIA && chmod +x ARIAfast.sh &&chmod +x ARIA.sh && ./ARIAfast.sh")
	
bot.polling(True)
	