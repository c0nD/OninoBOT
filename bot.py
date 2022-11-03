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
  
    welcome_test_id = 939241047379308554
    rules_channel_id = 939240668369387590

    # Connected to Discord API woooo
    @client.event
    async def on_ready():
        print(f'\n\n\t\t\t\t{client.user} is now running!')

    # Reply to messages
    @client.event
    async def on_message(message):
      # Send funny msg
        user_message = str(message.content)
        await send_message(message, user_message)
      # React to join message
        emoji_list = ["\U0001F49B", "\U0001F497", "\U0001F49C", "\U0001F9E1", "\U0001F499", "\U0001F49A",
                     "\U0001F49D", "\U0001F496", "\U0001F31F", "\U0001F9C5", "\U0001F9C4",
                     "<:brucelove:997414533356331068>", "<:brucecute:994569978080657468>",
                     "<:bruceowo:997117891071725719>", "<:bruceevilera:997117911040807013>",
                     "<:bite_onion:1003670600067334145>", "<:bite_tl:1003671564644007936>",
                     "<:uwu:942591940430540871>", "<:blush:940232012336349194>",
                     "<:hamsterluv:939494342798766150>", "<:omg_cat:943033137829662721>",
                     "<:elmorise:939452816810979370>", "<:feetcacao_revanna:969985639858733116>",
                     "<:feetdevil:957833444648439869>", "<:feetfig:942463290766934026>",
                     "<:feetgnome:957832987272159263>", "<:feetherb:957833315891707954>",
                     "<:feetpome:957833343192404058>", "<:feetsonic:957833282635046923>",
                     "<:feetsorbet:957833413979684874>", "<:feetsquid:942598509302022154>",
                     "<:feetwalla:957983015936622622>", "<:feetwhroom:957833378101604422>"
                     "<:gnome:963213787681406979>", "<:kermit_cowboy:1019075257480511538>",
                     "<:kermit_gasp:1019075299817816094>", "<:kermit_hand:1019075234617376768>",
                     "<:kermit_luv:1019075279240568913>", "<:kermit_shy:1019075213427740712>",
                     "<:pepelove:942461588068253706>", "<:pepecookie:957852663821766746>",
                     "<:qt_bananya:1019077326983663707>", "<:qt_duck:1015560434553733140>",
                     "<:qt_flowercat:1015562180650860565>", "<:qt_oo:1015562456728358912>",
                     "<:qt_peek:1015561776554835988>", "<:qt_yougotgames:1015562517013090385>"]
        react_list = random.sample(emoji_list, random.randint(7,9))
      
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