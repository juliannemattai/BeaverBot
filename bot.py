from dotenv import load_dotenv
load_dotenv()

import discord
import os

from funfact import *

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    


@client.event
async def on_message(message):
    if message.author == client.user:
        return


###FUNFACT BOT###
channel_facts = "beaver-bot"
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.name != channel_facts:
        print("wrong channel")
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello! My name is Standford the Beaver. Ask me about Skule History by using the command $funfact followed by a topic you want to know more about")
    
    elif message.content.startswith("$funfact"):
        subject = message.content.replace('$funfact','').strip()
        fact = get_fun_fact(subject)
        await message.channel.send(fact)


###REACTION FOR ROLES###
##PARAMETERS + CUSTOMIZATION##
message_react_id = 861300988936716328
blue_heart_role = 'research team'
green_heart_role = 'mom'
pink_heart_role = 'events volunteer'
purple_heart_role = 'inventory volunteer'

def choose_role(guild, payload):
    if payload.emoji.name == '💙':
        #print("blue")
        #print(guild.roles)
        role = discord.utils.get(guild.roles, name = blue_heart_role)
            
    elif payload.emoji.name == '💚':
        #print("green")
        role = discord.utils.get(guild.roles, name = green_heart_role)

    elif payload.emoji.name =="💗":
        #print("pink")
        role = discord.utils.get(guild.roles, name = pink_heart_role)

    elif payload.emoji.name =="💜":
        #print("purple")
        role = discord.utils.get(guild.roles,name = purple_heart_role)
    
    return role

##REACTION CODE##
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if (message_id==message_react_id):
        print("this is the right message")
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id==guild_id, client.guilds)

        #print(payload.emoji.name)
        role = choose_role(guild, payload)
        
        if role is not None:
            #print(payload.user_id)
            #print(guild.members)
            member = discord.utils.find(lambda m : m.id ==payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("member not found")
        else:
            print("role not found")


    #print("Hello world")

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if (message_id==message_react_id):
        #print("goodbye message")
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id==guild_id, client.guilds)

        #print(payload.emoji.name)
        role = choose_role(guild, payload)

        
        if role is not None:
            #print(payload.user_id)
            #print(guild.members)
            member = discord.utils.find(lambda m : m.id ==payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("done")
            else:
                print("member not found")
        else:
            print("role not found")


    #print("Goodbye world")



client.run(os.getenv('BOT_TOKEN'))
