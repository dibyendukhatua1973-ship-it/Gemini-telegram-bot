import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 
BOT_TOKEN = "8841244048:AAHA5PHAGi-K5g97bkv4aQ5RDv52QTGfbI4"

bot = telebot.TeleBot(BOT_TOKEN)
#
GEMINI_API KEY = "AQ.Ab8RN6LJsYpTgEZbLf2RFeO4dj9CqXQFuiUNba7LRtNxJ51QhQ"
# /start কমান্ড হ্যান্ডলার
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_first_name = message.from_user.first_name
    
    # 
    welcome_text = (হ্যালো! আমি আপনার বন্ধু পিকু AI bot. Created by [AM]Anamitra Khatua. আপনি আমাকে যেকোনো প্রশ্ন করতে পারেন)
        f"হ্যালো {user_first_name}! 🤖\n\n"
        f"আমি **PM_Piku AI** - আপনার অল-ইন-ওয়ান এআই অ্যাসিস্ট্যান্ট।\n"
        f"Created by: **(AM) Anamitra Khatua"
        f"নিচের মেনু থেকে আপনার পছন্দের AI ইঞ্জিন সিলেক্ট করুন:"
    )
    
    # ইনলাইন বাটন বা মেনু তৈরি
    markup = InlineKeyboardMarkup()
    
    # এআই ইঞ্জিন বাটন
    btn_chatgpt = InlineKeyboardButton("🟢 ChatGPT 4", callback_data="ai_chatgpt")
    btn_claude = InlineKeyboardButton("🟣 Claude 3", callback_data="ai_claude")
    btn_gemini = InlineKeyboardButton("🔵 Gemini Pro", callback_data="ai_gemini")
    btn_grok = InlineKeyboardButton("⚫️ Grok (X)", callback_data="ai_grok")
    btn_perplexity = InlineKeyboardButton("🌐 Perplexity", callback_data="ai_perplexity")
    
    # প্রো-টিপ বাটন (@Anamitra492)
    btn_dev = InlineKeyboardButton("💬 ডেভেলপারের সাথে চ্যাট", url="https://t.me/@Anamitra492")
    btn_channel = InlineKeyboardButton("📢 অফিশিয়াল চ্যানেল", url="https://t.me/আপনার_চ্যানেল")
    
    # বাটনগুলো সাজানো (প্রতি লাইনে কয়টি থাকবে)
    markup.row(btn_chatgpt, btn_claude)
    markup.row(btn_gemini, btn_grok)
    markup.row(btn_perplexity)
    markup.row(btn_channel)
    markup.row(btn_dev)
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

# বাটন ক্লিকের রেসপন্স হ্যান্ডলার (আপাতত শুধু মেসেজ দেবে, পরে জেমিনি যুক্ত হবে)
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    ai_names = {
        "ai_chatgpt": "ChatGPT 4",
        "ai_claude": "Claude 3",
        "ai_gemini": "Gemini Pro",
        "ai_grok": "Grok",
        "ai_perplexity": "Perplexity"
    }
    
    if call.data in ai_names:Anamitra Khatua 
        selected_ai = ai_names[call.data]
        bot.answer_callback_query(call.id, f"{selected_ai} সিলেক্ট করা হয়েছে!")
        bot.send_message(call.message.chat.id, f"✅ আপনি **{selected_ai}** মোডে আছেন। এবার আপনার প্রশ্নটি লিখুন:", parse_mode="Markdown")

# বট রান করার লুপ
print("PM_Piku AI বট চালু হয়েছে...!")
bot.infinity_polling()
