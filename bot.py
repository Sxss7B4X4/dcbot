import discord
import time
from discord.ext import commands

# Moduller Eklendi
print('Starting.....')
Bot = commands.Bot('! ')

@Bot.event
async def on_ready():
    print('''     _____             _     ____        _    __      ____ 
    |  __ \           | |   |  _ \      | |   \ \    / /_ |
    | |__) |___   ___ | |_  | |_) | ___ | |_   \ \  / / | |
    |  _  // _ \ / _ \| __| |  _ < / _ \| __|   \ \/ /  | |
    | | \ \ (_) | (_) | |_  | |_) | (_) | |_     \  /   | |
    |_|  \_\___/ \___/ \__| |____/ \___/ \__|     \/    |_|
                                                        
                                                       Started... ''')
    print('''            ============================
                Commands  (prefix is !)
                    1 = sayilar
                    2 = kick
             ============================''')

# Bot Calistirilacak
@Bot.command()
async def sayilar(msg):
    await msg.send('1')
    time.sleep(1)
    await msg.send('2')
    time.sleep(1)
    await msg.send('3')
    time.sleep(1)
    await msg.send('4')
    time.sleep(1)
    await msg.send('6')
    time.sleep(1)
    await msg.send('7')
    time.sleep(1)
    await msg.send('8')
    time.sleep(1)
    await msg.send('9')
    time.sleep(1)
    await msg.send('10')

@Bot.command()
async def kick(ctx, member:discord.Member, *args, reason="Yok",):
        await member.kick(reason=reason)
Bot.run('OTY5MzM1ODQ2OTU0MjA5Mjkw.Ymr6Ww.kCs3-Ez7BHhTZ6Ptv2ufJrZKtPA')

