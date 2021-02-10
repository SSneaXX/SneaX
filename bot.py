# Import Discord Package
import discord

# Client (Bot)
client = discord.Client()

@client.event
async def on_ready():
    # DO STUFF....

    bot_channel = client.get_channel(809070846290952233)
    await bot_channel.send('')

@client.event
async def on_disconnect():
    bot_channel = client.get_channel(809070846290952233)
    await bot_channel.send('')

@client.event  
async def on_message(message):
    
    if message.content == 'What is the version of the bot?':
        chat_channel = client.get_channel(808744280264802306)

        myEmbed = discord.Embed(titel="Current Version", description="Current Version", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Data Released:", value="10th Feburary, 2021", inline=True)

        await chat_channel.send(embed=myEmbed)

@client.event
async def on_ready():

    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Rainbow Six Siege'))

# Run the client on the server
client.run('ODA5MDUzOTYwNzI2OTA0ODgz.YCPgNw.GLQuwGdF3oLqJe1SDgm66745MM8')
