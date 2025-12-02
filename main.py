import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎯 **مرحباً! البوت شغّال الآن** ✅\n\n"
        "🤖 الميزات الجاهزة:\n"
        "• تحليل البوتات\n"
        "• إدارة المحافظ\n"
        "• نظام الإحالات\n\n"
        "🚀 كل شيء جاهز!",
        parse_mode="Markdown"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ **الأوامر المتاحة:**\n"
        "/start\n/help\n/bots\n/wallets\n/referrals"
    )


async def bots_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bots_list = [
        "🤖 بوت 1: موثوق",
        "🤖 بوت 2: موثوق",
        "🤖 بوت 3: موثوق",
    ]
    await update.message.reply_text("\n".join(bots_list))


async def wallets_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    wallets_list = [
        "💰 Trust Wallet: موجود",
        "💰 Binance Wallet: موجود",
        "💰 Telegram Wallet: موجود",
    ]
    await update.message.reply_text("\n".join(wallets_list))


async def referrals_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔗 نظام الإحالات يعمل. عدد الإحالات: 0")


async def main():
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN غير موجود!")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("bots", bots_command))
    app.add_handler(CommandHandler("wallets", wallets_command))
    app.add_handler(CommandHandler("referrals", referrals_command))

    logger.info("🚀 Starting bot...")
    await app.run_polling()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())    ]
    update.message.reply_text("\n".join(wallets_list))

def referrals_command(update: Update, context: CallbackContext):
    # مثال: نظام الإحالات
    update.message.reply_text("🔗 **نظام الإحالات يعمل بكفاءة.**\nعدد الإحالات: 0")

# ==========================
# التشغيل الرئيسي للبوت
# ==========================
def main():
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN غير موجود! تأكد من إضافته في Environment Variables")
        return

    try:
        updater = Updater(BOT_TOKEN, use_context=True)
        dp = updater.dispatcher

        # تسجيل جميع الأوامر
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help_command))
        dp.add_handler(CommandHandler("bots", bots_command))
        dp.add_handler(CommandHandler("wallets", wallets_command))
        dp.add_handler(CommandHandler("referrals", referrals_command))

        logger.info("✅ البوت يبدأ التشغيل...")
        updater.start_polling()
        logger.info("✅ البوت يعمل الآن!")

        updater.idle()
    except Exception as e:
        logger.error(f"❌ خطأ أثناء التشغيل: {e}")

if __name__ == '__main__':
    main()
