import os, nextcord, random as randomMdl, asyncio, json
from nextcord.ext import commands
from nextcord.ui import Button, View
from nextcord import Interaction, SlashOption
from threading import Thread
from typing import Optional

TOKEN = os.environ['TOKEN']
client = commands.Bot(command_prefix='-', intents=nextcord.Intents.all())



@client.event
async def on_ready():
    activity = nextcord.Game(name=f"Sunrise Highway", type=3)
	await client.change_presence(status=nextcord.Status.online,
                                 activity=activity)
	print('Ready')
	
	
def loadCmd(cmd):
	with open(f"cmds/{cmd}.json") as f:
		f = json.load(f)
		"""
		try:
			ctn = f['content']
		except:
			ctn = None
		try:
			title = f['embed']['title']
		except:
			title = None
			
		try:
			description = f['embed']['description']
		except:
			description = None
		emb = nextcord.Embed(title=title, description=description)
		"""
		
		emb = nextcord.Embed().from_dict(f['embed'])
		try:
			ctn = f['content']
		except:
			ctn = None
		return [ctn, emb]

def is_owner():
    def predicate(interaction: Interaction):
        return interaction.user.id in [753222096141680651, 867700344250040350] 
        
    return application_checks.check(predicate)

@application_checks.check_any(applications_checks.has_role(1017787962001457262), is_owner())
@client.slash_command(description="Event manager")
async def event(interaction: Interaction):
	cmd = loadCmd('event')
    	await interaction.response.send_message(content=cmd[0], embed=cmd[1])
    
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
client.run(TOKEN)
