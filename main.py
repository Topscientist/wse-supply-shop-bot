##This code is copyrighted under the UK Intellectaul property house, Attempting to re-distribute or use the code for your own purposes without permisiion from the original owner is subject to law enforcement.

##Copyright (c) Artymartin3459#9245 2021

import discord
import os
from discord_components import *
from replit import db

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(
        name=f"WSE Supply Co. Shop Bot! | Never Gonna Let you Down | wse help")
                                 )
    DiscordComponents(client)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('wse help'):
        embed = discord.Embed(title="WSE Shop Bot Command List:", colour=discord.Colour(0x7289da))

        embed.add_field(name=f"💁 General:", value="—————————", inline=False)
        embed.add_field(name=f"ℹ️ Help Command", value="wse help", inline=True)
        embed.add_field(name=f"🛠 Staff List", value="wse staff list", inline=True)
        embed.add_field(name=f"** **", value="** **", inline=False)
        embed.add_field(name=f"🏬 Shopping:", value="—————————", inline=False)
        embed.add_field(name=f"🛒 The Shop!", value="wse shop", inline=True)
        embed.add_field(name=f"🧺 Your Basket", value="wse basket", inline=True)
        embed.add_field(name=f"** **", value="** **", inline=False)

        await message.channel.send(embed=embed)
    
    if msg.startswith('wse staff list'):
      embed = discord.Embed(title="WSE Supply Co. Staff List:", colour=discord.Colour(0xf1c40f))

      embed.add_field(name=f"_CEO:_:", value="+SixpennyFlame66", inline=False)
      embed.add_field(name=f"_Managers:_", value="MistahQuack", inline=False)
      embed.add_field(name=f"_Affiliates:_", value="MistahQuack and Q u e e n", inline=False)
      embed.add_field(name=f"_Security:_", value="MistahQuack, +footdabmommy, Mask3D_WOLF", inline=False)
      embed.add_field(name=f"_Staff:_", value="+footdabmommy, Mask3D_WOLF, Liamcraycray", inline=False)

      await message.channel.send(embed=embed)

    if msg.startswith('wse basket'):
      name = message.author.id
      if str(name) in db:
        await message.channel.send('Hi!')
      else:
        await message.channel.send("**💥 Error 404:** It looks like you don't have a basket! Start shopping using `wse shop` to create one!")

    if msg.startswith('wse shop'):
        mention = message.author.mention
        await message.channel.send(
            "**Welcome To Our Shop!** - Pick A Catagory To Begin.",
            components=[
                Select(placeholder="Select One Of The Values",
                       options=[
                           SelectOption(label="Food + Seeds", value="Food + Seeds"),
                           SelectOption(label="Wood And Planks", value="Wood And Planks"),
                           SelectOption(label="Cave Stuff And Ores", value="Cave Stuff And Ores"),
                           SelectOption(label="Mob Droppings", value="Mob Droppings"),
                           SelectOption(label="Melee", value="Melee"),
                           SelectOption(label="Nether Items", value="Nether Items"),
                           SelectOption(label="Materials", value="Materials")
                       ])
            ])

        interaction = await client.wait_for(
            "select_option", check=lambda i: i.component[0].value)

        await interaction.respond(
          content=f"**Please Wait...** Loading The {interaction.component[0].label} Catagory...")
        
        if interaction.component[0].label != "Food + Seeds":
          embed = discord.Embed(
            title='💥 Error 404 - This Catagory Has No Data Yet',
            description=
            "The only catagory with data is `Food + Seeds`.",
            color=discord.Colour.red())
          await message.channel.send(embed=embed)
        
        if interaction.component[0].label == "Food + Seeds":
          embed = discord.Embed(title="WSE Supply Co. Shop:", colour=discord.Colour(0x1abc9c))

          embed.add_field(name=f"🥖 Food + Seeds Catagory:", value="—————————", inline=False)
          embed.add_field(name=f"Food:", value="Bread [3x for 1x Sand]", inline=False)
          embed.add_field(name=f"Seeds:", value="Wheat Seeds [9x for 3x Coal]", inline=False)
          embed.add_field(name=f"** **", value="%s" %mention, inline=False)

          await message.channel.send(embed=embed)

          await message.channel.send("_ _", 
            components=[
                Select(placeholder="Please Select A Product",
                       options=[
                           SelectOption(label="Bread", value="Bread"),
                           SelectOption(label="Wheat Seeds", value="Wheat Seeds"),
                       ])
            ])
          
          interaction = await client.wait_for(
            "select_option", check=lambda i: i.component[0].value)

          await interaction.respond(
            content=f"How Much/Many {interaction.component[0].label} Would You Like?", 
            components=[
                Select(placeholder="Please Select An Amount",
                       options=[
                           SelectOption(label="9", value="9"),
                           SelectOption(label="18", value="18"),
                           SelectOption(label="27", value="27"),
                           SelectOption(label="36", value="36"),
                           SelectOption(label="45", value="45"),
                           SelectOption(label="54", value="54"),
                           SelectOption(label="64", value="64"),
                       ])
            ])

          interaction = await client.wait_for(
          "select_option", check=lambda i: i.component[0].value)

          await interaction.respond(
            content=f"☑️ Order Added To Basket")


client.run(os.getenv('TOKEN'))
