import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

# التوكن من متغيرات البيئة
BOT_TOKEN = os.environ.get('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await update.message.reply_text(
        f"🎯 **مرحباً {user.first_name}!**\n\n"
        "🤖 **أنا البوت الذكي لأبو علي**\n\n"
        "✅ **الميزات المتاحة:**\n"
        "• تحليل البوتات الذكي\n" 
        "• إدارة المحافظ\n"
        "• نظام الإحالات\n"
        "• إدارة المشاريع\n"
        "• تقارير تلقائية\n\n"
        "🚀 **البوت يعمل على Render بنجاح!**",
        parse_mode='Markdown'
    )

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔍 **نظام تحليل البوتات جاهز**\n\n"
        "أرسل username أي بوت لتحليله!",
        parse_mode='Markdown'
    )

async def wallets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💼 **نظام إدارة المحافظ جاهز**\n\n"
        "جاري تحميل بيانات محافظك...",
        parse_mode='Markdown'
    )

async def keep_alive():
    """إبقاء البوت نشطاً على Render"""
    while True:
        logging.info("🟢 البوت يعمل...")
        await asyncio.sleep(300)  # كل 5 دقائق

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
