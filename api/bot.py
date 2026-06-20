from http.server import BaseHTTPRequestHandler
import json
import os
import asyncio
from telegram import Bot

TOKEN = os.environ.get("8988150913:AAEah2JWOvVFiE2dHzOcZPLzFaF5lSAF3O8")

if not TOKEN:
    raise Exception("BOT_TOKEN is missing")

bot = Bot(token=TOKEN)


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Telegram bot is running")

    def do_POST(self):
        try:
            length = int(self.headers.get("content-length", 0))
            body = self.rfile.read(length)

            update = json.loads(body.decode("utf-8"))

            asyncio.run(handle_update(update))

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())


async def handle_update(update):

    if "message" not in update:
        return

    message = update["message"]

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    if text == "/start":
        await bot.send_message(
            chat_id=chat_id,
            text="اهلا بك في البوت 🤖"
        )

    elif text == "/ping":
        await bot.send_message(
            chat_id=chat_id,
            text="Pong!"
        )

    else:
        await bot.send_message(
            chat_id=chat_id,
            text=f"قلت: {text}"
          )
