import os
import logging
from telegram.ext import Updater, CommandHandler

BOT_TOKEN = os.environ.get('BOT_TOKEN')

def start(update, context):
    update.message.reply_text("🎯 **مرحباً! البوت يعمل الآن بنجاح** ✅", parse_mode='Markdown')

def main():
    logging.basicConfig(level=logging.INFO)
    
    if not BOT_TOKEN:
        logging.error("❌ BOT_TOKEN غير موجود!")
        return
    
    try:
        updater = Updater(BOT_TOKEN, use_context=True)
        dp = updater.dispatcher
        
        dp.add_handler(CommandHandler("start", start))
        
        updater.start_polling()
        logging.info("✅ البوت يعمل على Render!")
        updater.idle()
        
    except Exception as e:
        logging.error(f"❌ خطأ: {e}")

if __name__ == '__main__':
    main()        await asyncio.sleep(300)  # كل 5 دقائق

def main():
    # إعداد التسجيل
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    
    if not BOT_TOKEN:
        logging.error("❌ BOT_TOKEN غير موجود!")
        return
    
    try:
        application = Application.builder().token(BOT_TOKEN).build()
        
        # إضافة الأوامر
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("analyze", analyze))
        application.add_handler(CommandHandler("wallets", wallets))
        application.add_handler(CommandHandler("report", analyze))
        
        # بدء البوت
        logging.info("✅ البوت يعمل على Render!")
        
        # تشغيل نظام الإبقاء نشطاً
        application.run_polling()
        
    except Exception as e:
        logging.error(f"❌ خطأ: {e}")

if __name__ == '__main__':
    main()
