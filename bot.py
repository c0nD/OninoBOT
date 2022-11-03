import discord
from discord import File
import os
import responses
import random


# Replies to the onion (setup method)
async def send_message(message, user_message):
    try:
        response = responses.get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)


# Runs the bot and sends messages
def run_bot():
    # Boring annoying shit
    tkn = os.environ['token']
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.guilds = True
    intents.presences = False
    client = discord.Client(intents=intents)

    # Connected to Discord API woooo
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    # Reply to messages
    @client.event
    async def on_message(message):
        if message.author == client.user:
          return
        user_message = str(message.content)
        await send_message(message, user_message)

    # Welcome members
    @client.event 
    async def on_member_join(member):
        #channel = member.guild.system_channel
        welcome_test_id = 1036888997114429450
        rules_channel_id = 1037605079076831253
        welcome_channel = client.get_channel(welcome_test_id)
        rules_channel = client.get_channel(rules_channel_id)
      
        await welcome_channel.send(f"Welcome {member.mention} to **{member.guild.name}**! Please check out out <#{rules_channel_id}>")
  
    client.run(tkn)