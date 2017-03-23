import telebot
import logging
from const import token, text, text2

logging.basicConfig(filename='telebot.log', level=logging.INFO, format='%(asctime)s %(message)s')
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['new_chat_member'])
def new_chat_member(message):
    """Main decorator, check and send message in case if new member in chat."""
    user_id = message.new_chat_member.id
    responce = bot.send_message(user_id, text)
    logging.warning("New chat member({}) received the message, /n {}".format(user_id, responce))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    responce = bot.reply_to(message, text2)
    logging.warning('{}, added bot to contacts/n{}'.format(message.from_user, responce))

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
