import discord
import os
import responses
import random


# Replies to the onion (setup method)
async def send_message(message, user_message):
    try:
        response = responses.get_response(user_message)
        if response != "nil":
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
  
    welcome_test_id = 1036888997114429450
    rules_channel_id = 1037605079076831253

    # Connected to Discord API woooo
    @client.event
    async def on_ready():
        print(f'\n\n\t\t{client.user} is now running!')

    # Reply to messages
    @client.event
    async def on_message(message):
      # Send funny msg
        user_message = str(message.content)
        await send_message(message, user_message)
      # React to join message
        emoji_list = ["\U0001F5A4", "<:manlet:1037374977680351233>", "\U0001F63C", "\U0001F497",
                     "\U0001F919", "\U0001F9C5", "\U0001F920", "\U0001F49E"]
        react_list = random.sample(emoji_list, 4)
      
        if message.author == client.user:
          if message.channel.id == welcome_test_id:
            for react in react_list:
              await message.add_reaction(react)
      

    # Welcome members
    @client.event 
    async def on_member_join(member):
        #channel = member.guild.system_channel
        welcome_channel = client.get_channel(welcome_test_id)
      
        await welcome_channel.send(f"Welcome {member.mention} to the **{member.guild.name}!** Please check out out <#{rules_channel_id}> to pick up some roles and familiarize yourself with us!")
  
    client.run(tkn)