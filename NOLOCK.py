import discord
import json
import colorama
import random
import asyncio
import datetime
import time
import os


from colorama import Fore
from colorama import Fore as C
from discord.ext import commands

os.system("title NO LOCK MADE BY TOUSKI")

client = discord.Client()
prefix = "."
client = commands.Bot(
    command_prefix=prefix,
    self_bot=True
)
client.remove_command('help') 

print(f'''{Fore.GREEN}
 ███▄    █  ▒█████       ██▓    ▒█████   ▄████▄  ▀██ ▄█▀
 ██ ▀█   █ ▒██▒  ██▒    ▓██▒   ▒██▒  ██▒▒██▀ ▀█   ██▄█▒ 
▓██  ▀█ ██▒▒██░  ██▒    ▒██░   ▒██░  ██▒▒▓█    ▄ ▓███▄░ 
▓██▒  ▐▌██▒▒██   ██░    ▒██░   ▒██   ██░▒▓▓▄ ▄██ ▓██ █▄ 
▒██░   ▓██░░ ████▓▒░    ░██████░ ████▓▒░▒ ▓███▀  ▒██▒ █▄
░ ▒░   ▒ ▒ ░ ▒░▒░▒░     ░ ▒░▓  ░ ▒░▒░▒░ ░ ░▒ ▒   ▒ ▒▒ ▓▒
░ ░░   ░ ▒░  ░ ▒ ▒░     ░ ░ ▒    ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░
   ░   ░ ░ ░ ░ ░ ▒        ░ ░  ░ ░ ░ ▒  ░        ░ ░░ ░ 
         ░     ░ ░          ░      ░ ░  ░ ░      ░  ░    
                 MADE BY Touski
              Github : TheyLoveTouski
  btw just put ur own custom emojis in the random.choice such as :dog:
''')

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
      time.sleep(1)
      await message.add_reaction(random.choice(["😊","👍","😡","🆒","😎" ]))
        
with open('./config.json')as f:
  config = json.load(f)

token = config.get('token')
client.run(token, bot=False)
