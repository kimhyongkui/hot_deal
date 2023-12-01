import discord

async def send_discord_notification(token, channel_id, message):
    client = discord.Client()

    @client.event
    async def on_ready():
        channel = client.get_channel(channel_id)
        await channel.send(message)
        await client.close()

    client.run(token)
