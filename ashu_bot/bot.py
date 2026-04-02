import telebot

BOT_TOKEN = "8088297539:AAFH0ogYeEeehahggqoZH9OZLdQHHJnsPKk"
GROUP_ID = -1003677941183

bot = telebot.TeleBot(BOT_TOKEN)

def is_user_joined(user_id):
    try:
        member = bot.get_chat_member(GROUP_ID, user_id)
        return member.status in ["member", "creator", "administrator"]
    except:
        return False

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    if not is_user_joined(user_id):
        markup = telebot.types.InlineKeyboardMarkup()

        join_btn = telebot.types.InlineKeyboardButton(
            "👥 Join Group",
            url="https://t.me/refervsreferbot"
        )

        check_btn = telebot.types.InlineKeyboardButton(
            "✅ Joined",
            callback_data="check_join"
        )

        markup.add(join_btn)
        markup.add(check_btn)

        bot.send_message(
            message.chat.id,
            "⚠️ Pehle group join karo phir 'Joined' dabao!"
        , reply_markup=markup)
    else:
        bot.send_message(
            message.chat.id,
            "✅ Welcome bro! Ab tum bot use kar sakte ho 🚀"
        )

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def check_join(call):
    user_id = call.from_user.id

    if is_user_joined(user_id):
        bot.answer_callback_query(call.id, "✅ Verified!")
        bot.send_message(call.message.chat.id, "🎉 Access Granted!")
    else:
        bot.answer_callback_query(call.id, "❌ Abhi join nahi kiya!")

bot.infinity_polling()
