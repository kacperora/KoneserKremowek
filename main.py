
import os

import discord
import pytz
import schedule

import asyncio

from datetime import timedelta, time, datetime
from discord.ext.commands import bot

from keep_alive import keep_alive
from discord.ext import tasks

from dotenv import load_dotenv
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    runner.start()


@tasks.loop(hours=24)
async def kremowka():
    print("kremowka")
    guild = client.guilds[0]
    channel = guild.system_channel
    with open('kremowka.jpeg', 'rb') as f:
       picture = discord.File(f)
       await channel.send(file=picture)


@tasks.loop(seconds=10)
async def runner():
    when = time(21, 37, 0)
    now = datetime.now().astimezone(pytz.timezone('Europe/Warsaw')).replace(tzinfo=None)
    if now.time() > when:
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
        await asyncio.sleep(seconds)
    while True:
        now = datetime.now().astimezone(pytz.timezone('Europe/Warsaw')).replace(tzinfo=None)
        target_time = datetime.combine(now.date(), when)
        seconds_until_target = (target_time - now).total_seconds()
        await asyncio.sleep(seconds_until_target)  # Sleep until we hit the target time
        await kremowka()  # Call the helper function that sends the message
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        seconds = (tomorrow - now).total_seconds()
        await asyncio.sleep(seconds)

keep_alive()
try:
    client.run("MTAwNDgzNTkzNTYzODI1NzY4NA.GmQJDe.rOEGYjhDo-HS6z2NPwoZyFXVHKcpySKUns2gqo")
except:
    os.system("kill 1")
