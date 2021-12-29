from os import link, replace
import discord
from discord.audit_logs import _transform_verification_level
from discord.embeds import Embed
from requests.models import codes
from getDateAndTime import getDT
import random
import requests

hacker_cats = ("https://c.tenor.com/SoBzDkrJuNUAAAAC/cat-hack.gif", "https://i.pinimg.com/originals/56/69/42/566942b729a1e9158c41d7b0c1df689c.jpg", "https://cdn.shopify.com/s/files/1/1915/5397/products/HackerCat_530x@2x.jpg?v=1598995616", "https://images.squarespace-cdn.com/content/v1/59551c6ed482e9b2f9cfd19e/1623407137645-LUTYG3GZ4D8SP1MFNH2Y/Hacker+cat.jpg?format=750w", "https://memegenerator.net/img/instances/75928946.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeM8pjsE8kc1J6L4BoFFZ6-eSp9K8tyRESCA&usqp=CAU")

#put this in another py file later
def getTK():
    token_file = open("token.txt", "r")
    x = token_file.read()
    token_file.close()
    return str(x)

client = discord.Client()

@client.event
async def on_ready():
    print(f"Started MatrixCat")

@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.author == client.user:
        return

    if message.content.startswith("-help"):
        help_embed = discord.Embed(title="Help", description="**MatrixCat info**\nCreated 11/3/2021\nCreated And Coded By github.com/FatyCaty\nThank you for helping me a lot Λcє#8759\n**Commands:**\n-help - MatrixCat bot help and info\n-cat - sends a random cat cute cat image (FatyCatys Favorite command ever)\n-hack [mention the person you want to hack] - Hacks someones\n-suggestion [suggestion] - Notifys the Owners About your a suggestion\n-say [message] - says something you want it to say\n-pooppost - shet post\n-codematrixinvite - sends a Code Matrix Invite", color=0x56e670)
        await message.channel.send(embed=help_embed)


    if message.content.startswith("-hack"):
        message.content = message.content.replace("-hack ", "")
        hack_embed = discord.Embed(title="POV")
        hack_embed.set_image(url=random.choice(hacker_cats))
        await message.channel.send(f"{message.author.mention} **Hacked** {message.content}", embed=hack_embed)
    
    if message.content.startswith("-cat"):
        catimg = requests.get("https://some-random-api.ml/img/cat").json()["link"]
        catimg_embed = discord.Embed(title="Cute Cat :heart:", color=0x56e670)
        catimg_embed.set_image(url=catimg)
        await message.channel.send(embed=catimg_embed)
    
    if message.content.startswith("-suggestion"):
        message.content = message.content.replace("-suggestion ", "")
        
        s_file = open("sugestions.txt", "a")
        s_file.write(f"User:{message.author} UserID:{message.author.id} at [{getDT()}] Suggested: {message.content}\n")
        suggestion_embed = discord.Embed(title = "Suggestion added", description = f"Suggestion by {message.author} was added", color=0x56e670)
        await message.channel.send(embed=suggestion_embed)
        

    if message.content.startswith("-say"):
        message.content = message.content.replace("-say ", "")
        say_embed = discord.Embed(title = message.content, description = f"Command Called by: {message.author}", color=0x56e670)
        await message.channel.send(embed=say_embed)
        #logs message (for security)
        say_log_file = open("say_log.txt", "a")
        say_log_file.write(f"{message.author}")
        say_log_file.close()

    if message.content.startswith("-pooppost") or message.content.startswith("-shetpost"):
        pooppost_embed = discord.Embed(title="Poop posted", color=0x56e670)
        await message.channel.send(embed=pooppost_embed)
        await message.channel.send("https://i.pinimg.com/originals/83/32/49/83324980390cd588a99d7c74cf54bc82.png")

    if message.content.startswith("-meme"):
        #discusting api - change ASAP!!!
        memeimg = requests.get("https://meme-api.herokuapp.com/gimme").json()["url"]
        memeimg_embed = discord.Embed(title="Funny meme :D", color=0x56e670)
        memeimg_embed.set_image(url=memeimg)
        await message.channel.send(embed = memeimg_embed)
    
    if message.content.startswith("-codematrixinvite"):
        await message.channel.send("**Code Matrix Invite:**\nhttps://discord.gg/HeKwRWt8sc")
    





        














































































client.run("OTA1NDUzNzYzNzk0NDY0ODE5.YYKThw.RdV7PLnrnqEj3MNROU4tCeDLtCI")





