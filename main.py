import os
import logging
from Google import genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# এখানে আপনার টোকেন ও এপিআই কি বসান
BOT_TOKEN = "8974579957:AAGoqSEd-miv5Vi5NGE6kdENya6v3QE214k"
genai.configure(api_key="AQ.Ab8RN6LJsYpTgEZbLf2RFeO4dj9CqXQFuiUNba7LRtNxJ51QhQ")

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[]) # এখানে বটের স্মৃতি বা হিস্ট্রি জমা থাকবে

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("হ্যালো! আমি আপনার জেমিনিpiku এআই বট। আমাকে যেকোনো প্রশ্ন করুন।")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    
    try:
        response = chat.send_message(user_text)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("দুঃখিত, বর্তমানে আমি উত্তর দিতে পারছি না।")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
