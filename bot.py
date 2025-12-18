from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8554387315:AAE9UqWhvPrwvxrGwhDinGW5_gxMMW63Z-k"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am Manish Sharma ")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "hello" in text:
        reply = "Hi! How can I help you?"
    else:
        reply = "I am still learning"

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("Bot running...")
app.run_polling()
