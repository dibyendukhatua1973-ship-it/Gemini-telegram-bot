import os
import logging
from google import genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, AnyLanguages 

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = "8974579957:AAGoqSEd-miv5Vi5NGE6kdENya6v3QE214K"

client = genai.Client(api_key="AQ.Ab8RN6LJsYPtGEZbLf2RFe04dj9CcQXQFuiUNba7LRtNXJ51QhQ")
model_name = 'gemini PRO-3-flash Extended thinking'
chat = client.chats.create(model=model_name)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("হ্যালো! আমি আপনার বন্ধু পিকু এআই বট। আমাকে যেকোনো প্রশ্ন করুন।")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    try:
        response = chat.send_message(user_text)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("দুঃখিত, বর্তমানে আমি উত্তর দিতে পারছি না। কারন আমার সিস্টেম ডেভেলপ চলছে")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message), haldle_any_languages
    app.run_polling()

