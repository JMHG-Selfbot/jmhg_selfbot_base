###
# Developed Solely By JMHG, AKA epicgamerjay#4862 on discord(quick promo there)
# This Can be Used AntyWay That You want But Im Not In Any Way Responsible For Any Bans That Happen During The Use Of JMHG Self Bot
#commercial use of te code(used to make a selfbot which you can sell) is prohibited, dont know why youd use my code anyway cus you should be good at coding if your gonna sell a selfbot but ok
###

import discord, json, pyfiglet, os, ctypes, time
from colorama import Fore, init
from discord.ext import commands

clear = lambda: os.system('cls')
bot = commands.Bot(description="Youtube Selfbot Test", command_prefix="!", self_bot=True)

bot.remove_command('help')
print("""
     _ __  __ _   _  ____     ____       _  __ ____        _   
    | |  \/  | | | |/ ___|   / ___|  ___| |/ _| __ )  ___ | |_ 
 _  | | |\/| | |_| | |  _    \___ \ / _ \ | |_|  _ \ / _ \| __|
| |_| | |  | |  _  | |_| |    ___) |  __/ |  _| |_) | (_) | |_ 
 \___/|_|  |_|_| |_|\____|   |____/ \___|_|_| |____/ \___/ \__|
 """)

print(f"""
__     __            _                _        ___         ___  
\ \   / /__ _ __ ___(_) ___  _ __    / |      / _ \       / _ \ 
 \ \ / / _ \ '__/ __| |/ _ \| '_ \   | |     | | | |     | | | |
  \ V /  __/ |  \__ \ | (_) | | | |  | |  _  | |_| |  _  | |_| |
   \_/ \___|_|  |___/_|\___/|_| |_|  |_| (_)  \___/  (_)  \___/ 

                        Created By JMHG
================================================================
""")
time.sleep(2)
print("[-] Initialising Bot") # just thought it looked cool, does absolutely fuck all
time.sleep(2)
print("[-] Logging Into Discord")
time.sleep(2)
text = "================================================================" #64 

@bot.event  # code that runs when the bot is ready to be used
async def on_ready():
    clear()
    print("""
     _ __  __ _   _  ____     ____       _  __ ____        _   
    | |  \/  | | | |/ ___|   / ___|  ___| |/ _| __ )  ___ | |_ 
 _  | | |\/| | |_| | |  _    \___ \ / _ \ | |_|  _ \ / _ \| __|
| |_| | |  | |  _  | |_| |    ___) |  __/ |  _| |_) | (_) | |_ 
 \___/|_|  |_|_| |_|\____|   |____/ \___|_|_| |____/ \___/ \__|
    """) # you can actually get an ascii title by running the bot and typeing !ascii {whatever you want your logo to be} and pressing enter
    print("""
__     __            _                _        ___         ___  
\ \   / /__ _ __ ___(_) ___  _ __    / |      / _ \       / _ \ 
 \ \ / / _ \ '__/ __| |/ _ \| '_ \   | |     | | | |     | | | |
  \ V /  __/ |  \__ \ | (_) | | | |  | |  _  | |_| |  _  | |_| |
   \_/ \___|_|  |___/_|\___/|_| |_|  |_| (_)  \___/  (_)  \___/ 

                        Created By JMHG
================================================================
    """)
    numberofservers = len(bot.guilds)
    usertext = f"Currently Logged In As {bot.user} : Currently In {numberofservers} Servers "
    usetextlen = len(usertext) - 1
    print(usertext)
    print("=" * usetextlen)

@bot.command()
async def ascii(ctx, *, args): #turns your desired message into ascii
    await ctx.message.delete()
    text = pyfiglet.figlet_format(args)
    await ctx.send(f"```{text}```")
    print(f"[-] !ascii [{args}]")

@bot.command()
async def yolo(ctx, *, args): # testing out embeds, do whatever you want with this
    await ctx.message.delete()
    embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    embedVar.add_field(name="whatever", value=args, inline=False)
    embedVar.add_field(name="Whatever", value=args, inline=False)
    await ctx.send(embed=embedVar)
    print(f"[-] !yolo [{args}]")

@bot.command()
async def Myping(ctx): # prints your current ping in ms
    await ctx.message.delete()
    await ctx.send(f"```Ping: {round(bot.latency * 1000)}ms```")
    print("[-] !ping")

@bot.command()
async def hello(ctx, *, args): # replies with hello + your argument so !hello jmhg would return Hello jmhg
    await ctx.message.delete()
    await ctx.send(f"```Hello {args}```")
    print(f"[EVENT] !hello [{args}]")

with open('./config.json') as f:
    config = json.load(f) # loads the config.json file

token = config.get('token') # gets the token from the config.json file
bot.run(token, bot=False)
