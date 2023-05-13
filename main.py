import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from DemoUIs.demoView import DemoView

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Initialize bot
client = commands.Bot(
    command_prefix="!", intents=discord.Intents.all(), case_insensitive=True
)


# Bot Functions
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.command()
async def demo(ctx):
    await ctx.send("Hi! Click the items below to test out the different UIs that are offered.", view=DemoView())


client.run(DISCORD_TOKEN)
