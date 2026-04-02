import requests
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    filters,
    ContextTypes
)

BOT_TOKEN = "8088297539:AAFmLwMkICiJBjwNNPe5KLnbvdRbeNl6Cro"
API_URL = "https://img-2-txt-eta.vercel.app/img2txt"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Bhai welcome!\n\n📸 Ek photo bhej aur main uska AI prompt banaunga 😎"
    )

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    file_url = file.file_path

    await update.message.reply_text("⏳ Processing image...")

    try:
        res = requests.get(f"{API_URL}?url={file_url}")
        data = res.json()

        prompt = data.get("prompt")

        if data.get("success") and prompt:
            await update.message.reply_text(f"🧠 Prompt:\n{prompt}")
        else:
            await update.message.reply_text("❌ Prompt generate nahi hua, dusri image try kar 😅")

    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {str(e)}")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, handle_image))

print("🤖 Bot chal raha hai...")

app.run_polling()
