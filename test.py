import discord

client = discord.Client()
prefix = "&"


@client.event
async def on_ready():
    print("Trimmau is ready for your orders.")
    await client.change_presence(activity=discord.Game("Working for El-Melloi"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('&hello'):
        await message.channel.send('Hello. How may I serve you?')

    if message.content.startswith('&sub') or message.content.startswith('&drop'):
        await message.channel.send('https://docs.google.com/spreadsheets/d/1TgpuozjukEdkOJdGGn-cWD3sIzMWCqnzeaycJsvmjTk/edit#gid=495949767')
        
    if message.content.startswith('&raid') or message.content.startswith('&graph'):
        await message.channel.send('https://www.dropbox.com/sh/nplk7n833zpht59/AACSJGEen0ccpkVaZ-jTJIo2a/FGO_Rashomon_Tracker?dl=0&lst=&subfolder_nav_tracking=1')


client.run('NTgxMzY2Mjc0NDc1NTU2ODc0.XOi7vg.SNwHGRSzeCsYroLKS8IkpBX6Gv4')
