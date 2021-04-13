import requests
import discord
import json
import random
import os

from discord import Embed
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands.cooldowns import BucketType
from colorama import Fore, Back, Style

#Edits config.json token value
if json.load(open("config/config.json"))["token"] == "":
    os.system("cls")
    print("")
    print("Please input the discord bot token below.".center(os.get_terminal_size().columns))
    print("")
    token = input()

    config = json.load(open("config/config.json"))
    config["token"] = (token)
    json.dump(config, open('config/config.json', 'w'), sort_keys=False, indent=4)

#Edits config.json prefix value
if json.load(open("config/config.json"))["prefix"] == "":
    os.system("cls")
    print("")
    print("Please input the prefix you would like to use to run commands below.".center(os.get_terminal_size().columns))
    print("")
    prefix = input()

    config = json.load(open("config/config.json"))
    config["prefix"] = (prefix)
    json.dump(config, open('config/config.json', 'w'), sort_keys=False, indent=4)

#Edits config.json apikey value
if json.load(open("config/config.json"))["apikey"] == "":
    os.system("cls")
    print("")
    print("Please input the api key of your thealtening account:".center(os.get_terminal_size().columns))
    print("")
    apiKey = input()

    config = json.load(open("config/config.json"))
    config["apikey"] = (apiKey)
    json.dump(config, open('config/config.json', 'w'), sort_keys=False, indent=4)

TOKEN = json.load(open("config/config.json"))["token"]
PREFIX = json.load(open("config/config.json"))["prefix"]
APIKEY = json.load(open("config/config.json"))["apikey"]

bot = Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
	os.system("cls")
	print("     _    _ _             _             ".center(os.get_terminal_size().columns))
	print("    / \  | | |_ ___ _ __ (_)_ __   __ _ ".center(os.get_terminal_size().columns))
	print("   / _ \ | | __/ _ \ '_ \| | '_ \ / _` |".center(os.get_terminal_size().columns))
	print("  / ___ \| | |_  __/ | | | | | | | (_| |".center(os.get_terminal_size().columns))
	print(" /_/   \_\_|\__\___|_| |_|_|_| |_|\__, |".center(os.get_terminal_size().columns))
	print("                                  |___/ ".center(os.get_terminal_size().columns))
	print("")
	print(f"Thealtening discord bot".center(os.get_terminal_size().columns))
	print(f"Code by Thereallo".center(os.get_terminal_size().columns))
	print(f"Logged into bot {bot.user.name}".center(os.get_terminal_size().columns))
	print("")
	print(f"{Fore.RED}SPAMMING THE COMMAND MAY RESULT A RATE LIMIT!{Style.RESET_ALL}".center(os.get_terminal_size().columns))
	print(f"{Fore.RED}USE THIS AS YOUR OWN RISK!{Style.RESET_ALL}".center(os.get_terminal_size().columns))
	print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	print("Logs:")

@bot.command()
async def gen(ctx):
	bad = ["401", "402", "403", "404", "500"]
	web = requests.get(f"http://api.thealtening.com/v2/generate?key={APIKEY}&info=true")
 
	helpembed = discord.Embed(title="Thealtening generator", description="", colour=discord.Color.blurple(), url="")

	helpembed.set_footer(text=f"Bot code by Thereallo")
	helpembed.set_image(url="")
	helpembed.set_thumbnail(url="")

	helpembed.add_field(name="Account sent!", value="Please check your dms!", inline=False)
 
	if web.status_code in bad:
		raise ValueError(f'Not Given, {web.status_code}')
		return
	else:
		acc = web.json()
		print(f"Raw account data: \n{acc}")
		print("")

		embed = Embed(title="Your Thealtening account.", colour=discord.Color.green())
		try:
			token = acc["token"]
			embed.add_field(name="Account Email", value=token, inline=True)
			print(f"[Token] {token}")
		except:
			embed.add_field(name="Account Email", value="Not Given", inline=True)
		try:
			password = acc["password"]
			embed.add_field(name="Account Password", value=password, inline=True)
			print(f"[Password] {password}")
		except:
			embed.add_field(name="Account Password", value="Not Given", inline=True)
		try:
			limit = acc["limit"]
			embed.add_field(name="Account Limited", value=limit, inline=True)
		except:
			embed.add_field(name="Account Limited", value="Not Given", inline=True)
		try:
			skin = acc["skin"]
			embed.add_field(name="Account Skin", value=skin, inline=True)
		except:
			embed.add_field(name="Account Skin", value="Not Given", inline=True)
		try:
			name = acc["username"]
			embed.add_field(name="Account Name", value=name, inline=True)
			print(f"[Username] {name}")
		except:
			embed.add_field(name="Account Name", value="Not Given", inline=True)
		try:
			hypixelLevel = acc["info"]["hypixel.level"]
			embed.add_field(name="Info\n\nHypixel Level", value="\n\n" + str(hypixelLevel), inline=True)
		except:
			embed.add_field(name="Hypixel level", value="Not Given", inline=True)
		try:
			hypixelRank = acc["info"]["hypixel.rank"]
			embed.add_field(name="Hypixel Rank", value=hypixelRank, inline=True)
		except:
			embed.add_field(name="Hypixel Rank", value="Not Given", inline=True)
		try:
			mineplexLevel = acc["info"]["mineplex.level"]
			embed.add_field(name="Mineplex Level", value=mineplexLevel, inline=True)
		except:
			embed.add_field(name="Mineplex Level", value="Not Given", inline=True)
		try:
			mineplexRank = acc["info"]["mineplex.rank"]
			embed.add_field(name="Mineplex Rank", value=mineplexRank, inline=True)
		except:
			embed.add_field(name="Mineplex Rank", value="Not Given", inline=True)
		try:
			labymodCape = acc["info"]["labymod.cape"]
			embed.add_field(name="Labymod Cape", value=labymodCape, inline=True)
		except:
			embed.add_field(name="Labymod Cape", value="Not Given", inline=True)
		try:
			zigcape = acc["info"]["5zig.cape"]
			embed.add_field(name="5Zig Cape", value=zigcape, inline=True)
		except:
			embed.add_field(name="5Zig Cape", value="Not Given", inline=True)

		await ctx.author.send(embed=embed)
		await ctx.send(embed=helpembed)

bot.run(TOKEN)
