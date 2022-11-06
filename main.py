import os, nextcord, random as randomMdl, asyncio, json
from nextcord.ext import commands
from nextcord.ui import Button, View
from nextcord import Interaction, SlashOption
from threading import Thread
from typing import Optional

TOKEN = "MTAzODgzNjE3Njg0NjU5ODI0NQ.G2JgJS.8G5DPvFKV04cyisakebxyG0ge0o-ywtMJzZ7yk"

client = commands.Bot(command_prefix='-', intents=nextcord.Intents.all())



@client.event
async def on_ready():
    activity = nextcord.Game(name=f"Sunrise Highway", type=3)
	await client.change_presence(status=nextcord.Status.online,
                                 activity=activity)
	print('Ready')
	
def check(interaction, cmd):
    user = interaction.user
    guild = interaction.guild
    #if user.id == owner_id:
        #return True

    if data['maintenance']==True:
        return "Bot is under maintenance. Try again later."
    
    if cmd in data['disabled_cmds']:
        return "This command is currenty disabled. Try again later."
    
    if str(user.id) in data['bled_users']:
        if int(datetime.timestamp(datetime.now())) < data[bled_users][str(user.id)]:
            return f"You are blacklisted until <t:{data[bled_users][str(user.id)]}:F>. You can't run (almost) any cmds until then."
        
    if str(guild.id) in data['bled_servers']:
        if int(datetime.timestamp(datetime.now())) < data[bled_servers][str(servers.id)]:
            return f"This server is blacklisted until <t:{data[bled_users][str(user.id)]}:F>. You can't run (almost) any cmds here until then."
    
@client.slash_command(description="Event manager")
async def event(interaction: Interaction):
    if check(interaction, "invite"):
        await interaction.response.send_message(
            f'Hey, you can invite me to your server by clicking this {INVITE_LINK}'
        )
    else:
        await interaction.response.send_message(check(interaction,
                                                      'invite'),
                                                ephemeral=True)
