import discord
from dotenv import load_dotenv
import os

load_dotenv()

message = "안녕"


def send_discord_notification(message):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    channel_id = int(os.getenv("APP_ID"))
    token = os.getenv("BOT_TOKEN")

    @client.event
    async def on_ready():
        channel = client.get_channel(channel_id)
        await channel.send(message)
        client.close()

    client.run(token)


send_discord_notification("안녕")
