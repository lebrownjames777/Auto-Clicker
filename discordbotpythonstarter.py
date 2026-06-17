import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(
  command_prefix="/",
  intents=intents
)

# ---------------- PUT COMMANDS HERE ---------------- #

# Here's an example:

@bot.tree.command(
  name="hello",
  description="The bot says hello back"
)
async def hello(itcn: discord.Interaction):
  await itcn.response.send_message(f"Hello, {itcn.user.mention}!")

# ---------------- SYNC SLASH COMMANDS ON START ---------------- #

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")


# ---------------- RUN ---------------- #

bot.run("YOUR_TOKEN_HERE")
