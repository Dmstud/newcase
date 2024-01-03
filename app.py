import telebot
from config import TOKEN,keys
from extensions import CryptoConverter,APIException
bot=telebot.TeleBot(TOKEN)




@ bot.message_handler(commands=['start','help'])
def help(message:telebot.types.Message):
    text='Чтобы начать работу введите запрос в следующем формате: \n <имя валюты>\
    <в какую валюту перевести>\
    <количество валюты>\nУвидеть список валют:/values'
    bot.reply_to(message,text)


@ bot.message_handler(commands=['values'])
def values(message:telebot.types.Message):
    text= 'Доступные валюты'
    for key in keys:
        text='\n'.join((text,key))
    bot.reply_to(message,text)

@ bot.message_handler(content_types=['text'])
def convert(message:telebot.types.Message):
    values=message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Необходимо ровно три параметра ввода')
        base, quote, amount = values

        total_base = CryptoConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message,f'Ошибка пользователя.\n {e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду \n {e}')
    else:

        total_base=total_base*float(amount)
        text = f'Цена {amount} {base} в {quote} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()


