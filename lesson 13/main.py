import telebot, wikipedia, re

bot = telebot.TeleBot('6295463767:AAFkQ93dR-aKFEMtkgLmW80Hn9759nfFvv8')

wikipedia.set_lang('ru')

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        witext = ny.content[:1000]
        wimas = witext.split('.')
        wimas = wimas[:-1]
        witext2 = ''
        for i in wimas:
            if not('==' in i):
                if (len((i.strip()))>3):
                    witext2 = witext2 + i + "."
            else: 
                break
        return witext2
    except Exception as е:
        return 'Такой информации нет'

@bot.message_handler(commands = ['start'])
def start(m, res = False):
    bot.send_message(m.chat.id, 'Скажи мне, я скажу тебе ')

@bot.message_handler(content_types = ['text'])
def handler_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(non_stop = True, interval = 0)
