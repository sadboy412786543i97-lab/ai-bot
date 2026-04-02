import requests
PROMPT_API = "https://img-2-txt-eta.vercel.app/img2txt"
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes
)

BOT_TOKEN = "8088297539:AAFmLwMkICiJBjwNNPe5KLnbvdRbeNl6Cro"

HF_API = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

CINEMATIC_STYLE = "masterpiece, best quality, ultra realistic, 8k, cinematic lighting, dramatic shadows, volumetric light, depth of field, sharp focus, professional photography, highly detailed, HDR, film grain, epic composition, realistic skin texture, global illumination"

negative_prompt = "blurry, low quality, distorted, bad anatomy, extra limbs, ugly"

user_mode = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📸 Image → Prompt", callback_data="i2p")],
        [InlineKeyboardButton("🎨 Prompt → Image", callback_data="p2i")]
    ]
    await update.message.reply_text("Mode choose kar:", reply_markup=InlineKeyboardMarkup(keyboard))


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "p2i":
        user_mode[query.from_user.id] = "prompt2img"
        await query.message.reply_text("✍️ Prompt bhej bro")

    elif query.data == "i2p":
        user_mode[query.from_user.id] = "img2prompt"
        await query.message.reply_text("📸 Photo bhej bro")


async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if user_mode.get(update.message.from_user.id) != "img2prompt":
        return

    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    file_url = file.file_path

    await update.message.reply_text("⏳ Prompt bana raha hu...")

    try:
        res = requests.get(f"{PROMPT_API}?url={file_url}")
        data = res.json()

        prompt_text = data.get("prompt")

        if data.get("success") and prompt_text:
            await update.message.reply_text(f"🧠 Prompt:\n{prompt_text}")
        else:
            await update.message.reply_text("❌ Error: " + str(data))

    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {str(e)}")

        await update.message.reply_text(f"⚠️ Error: {str(e)}")

        await update.message.reply_text(f"⚠️ Error: {str(e)}")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if user_mode.get(update.message.from_user.id) != "prompt2img":
        return

    user_prompt = update.message.text
    final_prompt = f"{CINEMATIC_STYLE}, {user_prompt}"

    await update.message.reply_text("🎨 Image bana raha hu...")

    try:
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}
        response = requests.post(
            HF_API,
            headers=headers,
            json={
                "inputs": final_prompt,
                "parameters": {
                    "negative_prompt": negative_prompt,
                    "guidance_scale": 7.5,
                    "num_inference_steps": 30
                },
                "options": {"wait_for_model": True}
            }
        )

        if response.status_code == 200:
            if "image" in response.headers.get("content-type", ""):
                await update.message.reply_photo(photo=response.content)
            else:
                await update.message.reply_text(f"❌ Error: {response.text}")
        else:
            await update.message.reply_text(f"❌ API Error: {response.status_code}")

    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {str(e)}")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
app.add_handler(MessageHandler(filters.PHOTO, handle_image))

print("🤖 Cinematic Bot chal raha hai...")

app.run_polling()
