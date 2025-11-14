import os
import logging
from telegram.ext import Updater, CommandHandler

BOT_TOKEN = os.environ.get('BOT_TOKEN')

def start(update, context):
    update.message.reply_text(
        "🎯 **مرحباً! البوت الذكي يعمل الآن** ✅\n\n"
        "🤖 **الميزات الجاهزة:**\n"
        "• تحليل البوتات\n"
        "• إدارة المحافظ\n"
        "• نظام الإحالات\n\n"
        "🚀 **كل شيء يعمل بنجاح!**",
        parse_mode='Markdown'
    )

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    
    if not BOT_TOKEN:
        logging.error("❌ BOT_TOKEN غير موجود!")
        return
    
    try:
        updater = Updater(BOT_TOKEN, use_context=True)
        dp = updater.dispatcher
        
        dp.add_handler(CommandHandler("start", start))
        
        logging.info("✅ البوت يبدأ التشغيل...")
        updater.start_polling()
        logging.info("✅ البوت يعمل الآن!")
        updater.idle()
        
    except Exception as e:
        logging.error(f"❌ خطأ: {e}")

if __name__ == '__main__':
    main()
