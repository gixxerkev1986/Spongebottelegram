from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Vul hier je token in of gebruik Render's environment variable
TOKEN = os.getenv("TELEGRAM_TOKEN") or "VUL_HIER_JE_TOKEN_IN"

async def analyse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Gebruik: /analyse <coin>")
        return
    coin = context.args[0]
    msg = (
        f"Analyse voor {coin}:\n"
        "- RSI: 53\n"
        "- Trend: Neutraal\n"
        "- Sentiment: Positief"
    )
    await update.message.reply_text(msg)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welkom bij Spongebot! Gebruik /analyse, /ping of /hulp.")

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pong!")

async def hulp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Beschikbare commando's:\n"
        "/analyse <coin> - Simpele analyse van een coin\n"
        "/ping - Check of de bot leeft\n"
        "/start - Startbericht\n"
        "/hulp - Dit hulpbericht"
    )
    await update.message.reply_text(help_text)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("analyse", analyse))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("hulp", hulp))
    print("[INFO] Spongebot Telegram gestart...")
    app.run_polling()
