import discord
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()


def send_discord_notification(messages):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    channel_id = int(os.getenv("APP_ID"))
    token = os.getenv("BOT_TOKEN")

    @client.event
    async def on_ready():
        channel = client.get_channel(channel_id)
        for message in messages:
            await channel.send(message)
        await client.close()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.start(token))
