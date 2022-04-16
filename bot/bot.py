import telebot
import requests




token = "5183640507:AAGg_pSs91nJMFpG3ccRKpVB3m9Y_7NaLHI"

bot = telebot.TeleBot(token)

url_create = 'http://127.0.0.1:8000/api/v1/bot/user/'

def create_user(id):
    response = requests.post(url_create,data={'telegram_id':id})
    


@bot.message_handler(commands=["start"])
def send_mess(message):
    user_ID = message.from_user.id
    username = message.from_user.username
    data = {
    "telegram_id": user_ID,
}

    tests = requests.get(url="http://127.0.0.1:8000/api/v1/bot/test/").json()
    
    markup_inline = telebot.types.InlineKeyboardMarkup()
    keyboards = [telebot.types.InlineKeyboardButton(x.get("title"),callback_data=x.get("id")) for x in tests]
    markup_inline.add(*keyboards)
    bot.send_message(
        message.chat.id, "Тесты",
        reply_markup=markup_inline,
    )
        

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    print(call.data)
    print("http://127.0.0.1:8000/api/v1/bot/test/"+str(call.data))
    questions = requests.get(url="http://127.0.0.1:8000/api/v1/bot/test/"+str(call.data)).json()
    print(call.message.chat.id)
    print(questions)
    bot.send_message(call.message.chat.id,'cе тут')
    # print(questions)
if __name__ == "__main__":
    bot.polling(none_stop=True)
