from instabot import Bot
import os
import datetime

bot = Bot()
bot.login(username=os.getenv("IG_USERNAME"), password=os.getenv("IG_PASSWORD"))

today = datetime.date.today()
base = datetime.date(2025, 4, 20)
count = (today - base).days + 1

message = f"{count}. Good Morning"
receiver = os.getenv("IG_RECEIVER")

bot.send_message(message, [receiver])
