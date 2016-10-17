import telebot
from const import token, text


bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['new_chat_member'])
def send_welcome(message):
    """Main Decorator, check and send message in case if new member in chat."""
    user_id = message.new_chat_member.id
    bot.send_message(user_id, text)
    print("New chat member received the message")

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
