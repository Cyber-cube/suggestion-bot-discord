import discord
import os
from discord.ext import commands
from discord.ui import Button, View
from keep_alive import keep_alive

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Logged in as {0.user}".format(bot))

@bot.command()
async def ping(ctx):
  latency = round(bot.latency * 1000)
  await ctx.send(f"Pong! {latency}ms")

@bot.event
async def on_message(message):
  if message.author.bot:
    return 

  elif str(message.channel.id) == '1025472080919150693':
    await message.delete()
    embed = discord.Embed(title='New suggestion', description=str(message.content), color=None)
    embed.set_footer(text=f'Suggested by {message.author.name}', icon_url=message.author.avatar)
    
    button1 = Button(label='Accept', style=discord.ButtonStyle.green)
    button2 = Button(label='Decline', style=discord.ButtonStyle.danger)

    view = View()
    view.add_item(button1)
    view.add_item(button2)
    await message.channel.send(embed=embed, view=view)
    async def button1_callback(interaction):
      if str(interaction.user.id) != '702569410598141982':
        await interaction.response.send_messeage('You are not eligible to accept/decline suggestion', ephemeral=True)
      else:
        embed = discord.Embed(title='Suggestion accepted', description=str(message.content), color=discord.Color.green()) 
        embed.set_footer(text=f'Suggested by {message.author.name}', icon_url=message.author.avatar)
        view.clear_items()
        await interaction.message.edit(embed=embed, view=view)
        await interaction.message.add_reaction('⬆️')
        await interaction.message.add_reaction('⬇️')

    async def button2_callback(interaction):
      if str(interaction.user.id) != '702569410598141982':
        await interaction.response.send_messeage('You are not eligible to accept/decline suggestion', ephemeral=True)
      else:
        view.clear_items()
        
        embed = discord.Embed(title='Suggestion declined', description=str(message.content), color=discord.Color.red()) 
        embed.set_footer(text=f'Suggested by {message.author.name}', icon_url=message.author.avatar)
        await interaction.message.edit(embed=embed, view=view)
    button1.callback = button1_callback
    button2.callback = button2_callback

@bot.command()
async def test(ctx):
  button1 = Button(label="Test", style=discord.ButtonStyle.green)
  button2 = Button(label="Test2", style=discord.ButtonStyle.green)

  view = View()
  view.add_item(button1)
  view.add_item(button2)

  await ctx.send("Test", view=view)
  async def button1_callback(interaction):
    await interaction.response.send_message("hi", ephemeral=True)
  async def button2_callback(interaction):
    await interaction.response.send_message("Yo", ephemeral=True)

  button1.callback = button1_callback
  button2.callback = button2_callback

keep_alive()
bot.run(os.getenv("TOKEN"))