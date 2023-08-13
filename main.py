# search images in gif format via GIPHY API
# (requires API key from https://developers.giphy.com/dashboard/)
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot (step by step tutorial)

import requests
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)


def get_gifs(search):
    load_dotenv()
    api_key = os.getenv("MY_GIPHY_API_KEY")

    GIPHY_URL = "https://api.giphy.com/v1/gifs/search"

    resp = requests.get(GIPHY_URL, params={"api_key": api_key, "q": search})
    content = resp.json()

    links = [gif["images"]["fixed_height"]["url"] for gif in content["data"]]

    return links


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi, I'm a Bot that will find GIFs for you! \
        Please enter a word you want to look for GIFs of.",
    )


async def show_gifs(update, context):
    search = update.message.text
    links = get_gifs(search)

    for link in links:
        await context.bot.send_animation(
            chat_id=update.effective_chat.id, animation=link
        )


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

application = ApplicationBuilder().token(TOKEN).build()
start_handler = CommandHandler("start", start)
application.add_handler(start_handler)
gifs_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), show_gifs)
application.add_handler(gifs_handler)
application.run_polling()
