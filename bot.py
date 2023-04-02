import discord
from discord import app_commands
intents = discord.Intents.default()
intents.members = True
class discordClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
client = discordClient(intents = intents)
@client.event
async def on_ready():
    print("Logged in, ready.")
    print(f'Bot now active under user {client.user} with the ID of {client.user.id}')

@client.event
async def on_member_join(member):
    embed = discord.Embed(title="Banned lmao",color=0x613583)
    await member.send(embed=embed)
    await member.guild.ban(user=member,reason="Instaban")
client.run("token here")
