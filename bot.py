import discord
import os
import responses
import random
import random
from pathlib import Path
from dotenv import load_dotenv
from webserver import keep_alive


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
    os.chdir(os.path.dirname(os.path.abspath(file))) # bug in python, think it was fixed but this just makes sure

    load_dotenv(dotenv_path=str(Path(os.path.realpath(__file__)).parent.parent)+"\\Token.env") # i use this personally as i find it the easiest to use, you might want to change it 
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
                     "<:brucelove:997414533356331068>", 
                     "<:bruceowo:997117891071725719>", 
                     "<:bruceevilera:997117911040807013>",
                     "<:bite_onion:1003670600067334145>", 
                     "<:bite_tl:1003671564644007936>",
                     "<:blush:940232012336349194>",
                     "<:hamsterluv:939494342798766150>", 
                     "<:omg_cat:943033137829662721>",
                     "<:elmorise:939452816810979370>", 
                     "<:feetcacao_revanna:969985639858733116>",
                     "<:feetdevil:957833444648439869>", 
                     "<:feetfig:942463290766934026>",
                     "<:feetgnome:957832987272159263>", 
                     "<:feetherb:957833315891707954>",
                     "<:feetpome:957833343192404058>", 
                     "<:feetsonic:957833282635046923>",
                     "<:feetsorbet:957833413979684874>", 
                     "<:feetsquid:942598509302022154>",
                     "<:feetwalla:957983015936622622>", 
                     "<:feetwhroom:957833378101604422>"
                     "<:gnome:963213787681406979>", 
                     "<:pepelove:942461588068253706>", 
                     "<:pepecookie:957852663821766746>",
                     "<:stolenkapebeansies_uwu:1054064888009461880>",
                     "<:stolenkapekermit_wow:1054065957548609566>",
                     "<:stolenkapekermit_raise:1054066401515683890>",
                     "<:stolenkapekermit_heart:1054066347237199983>",
                     "<:stolenkapekermit_shy:1054066475423518730>",
                     "<:stolenkapebeansies_banana:1056159295659585657>",
                     "<:stolenkapebeansies_cat1:1054064729225695292>",
                     "<:stolenkapebeansies_egg:1054557639083835422>",
                     "<:stolenkapebeansies_owo:1054065406320574586>",
                     "<:beestealthishapibee:1102056952038690877>",
                     "<:stolenkapekermit_uvu:1054066083801337908>"]
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
        choices = [f"Welcome {member.mention} to the **{member.guild.name}** server! Please check out out <#{rules_channel_id}> to pick up some roles and familiarize yourself with us!",
                  f"Greetings, {member.mention}, and welcome to the **{member.guild.name}** server! Be sure to explore <#{rules_channel_id}> to select some roles and get acquainted with our community!",
                  f"Hey there, {member.mention}! A warm welcome to the **{member.guild.name}** server! Don't forget to swing by <#{rules_channel_id}> to grab some roles and get to know us better!",
                  f"Hello, {member.mention}, and a big welcome to the **{member.guild.name}** server! Make sure to drop by <#{rules_channel_id}> to choose your roles and get comfortable with our community!",
                  f"Hi, {member.mention}! We're thrilled to have you in **{member.guild.name}**! Take a moment to visit <#{rules_channel_id}> to pick up some roles and get acclimated with our community!",
                  f"Salutations, {member.mention}! Joining **{member.guild.name}** was a fantastic choice 😎. Head over to <#{rules_channel_id}> to select roles and acquaint yourself with us!"] # if im honest i just used chatgpt to write varients of this 💀
        await welcome_channel.send(random.choice(choices))

    keep_alive()
    client.run(os.getenv('TOKEN'))
