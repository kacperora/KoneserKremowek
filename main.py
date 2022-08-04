import os

import discord
import schedule
import time
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    #await kremowka()

async def kremowka():
    guild = client.guilds[0]
    channel = guild.system_channel
    with open('kremowka.jpeg', 'rb') as f:
        picture = discord.File(f)
        await channel.send(file=picture)


client.run(TOKEN)
schedule.every().day.at("21:37").do(kremowka)

