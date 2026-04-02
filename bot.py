from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "APNA_BOT_TOKEN_DAL"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bot chal raha hai 🔥")

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
