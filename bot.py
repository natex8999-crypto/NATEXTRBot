from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 NATEX KRALLIĞI'NA HOŞ GELDİNİZ\n\n"
        "Komutlar:\n"
        "/discord\n"
        "/basvuru\n"
        "/oneri\n"
        "/sikayet"
    )

async def discord(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💬 Discord: https://discord.gg/Q9Tfn6nA")

async def basvuru(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Yetkili Başvurusu:\nhttps://forms.gle/EsbsbqhLstj4qWq59"
    )

async def oneri(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💡 Öneri Formu:\nhttps://forms.gle/aKapGbVvr1nTnXsu5"
    )

async def sikayet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚠️ Şikayet Formu:\nhttps://forms.gle/GcoaGAT6ZN7MhLqDA"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("discord", discord))
app.add_handler(CommandHandler("basvuru", basvuru))
app.add_handler(CommandHandler("oneri", oneri))
app.add_handler(CommandHandler("sikayet", sikayet))

app.run_polling()
