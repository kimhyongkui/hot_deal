import discord
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
channel_id = int(os.getenv("APP_ID"))
token = os.getenv("BOT_TOKEN")


async def send_discord_notification(message):
    channel = client.get_channel(channel_id)
    await channel.send(message)


@client.event
async def on_ready():
    await client.close()


client.run(token)
