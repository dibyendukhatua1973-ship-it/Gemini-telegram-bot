import logging
from google import genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# লগিং সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# আপনার প্রদান করা টেলিগ্রাম বট টোকেন ও জেমিনি এপিআই কী
BOT_TOKEN = "8974579957:AAGoqSEd-miv5Vi5NGE6kdENya6v3QE214k"
GEMINI_API_KEY = "AQ.Ab8RN6LJsYPtGEZbLf2RFe04dj9CcQXQFuiUNba7LRtNXJ51QhQ"

# Google GenAI Client তৈরি
client = genai.Client(api_key=GEMINI_API_KEY)
MODEL_NAME = 'gemini-2.5-pro'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am a bot. created by X")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    
    # টাইপিং ইন্ডিকেটর পাঠানো
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    try:
        # Gemini 2.5 Pro মডেল দিয়ে উত্তর প্রস্তুত করা
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=user_text
        )
        
        if response.text:
            await update.message.reply_text(response.text)
        else:
            await update.message.reply_text("দুঃখিত, কোনো উত্তর প্রস্তুত করা সম্ভব হয়নি।")
            
    except Exception as e:
        logging.error(f"Error details: {e}")
        await update.message.reply_text("Sorry")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("Bot is running...")
    app.run_polling()
