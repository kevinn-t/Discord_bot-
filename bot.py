# import discord
# from discord.ext import commands

# client = commands.Bot(command_prefix =  ';')
# # bot = discord.Client()

# @client.event
# async def on_ready():
#     print("Bot is ready.")

# client.run('Nzc4MDY1OTY4MzkxOTEzNDky.X7MkZg.9bhEvfqmNsp5OzdZixKzXmwtJLo')
import discord
import random
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
#guessing game
        if message.content.startswith(';guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))
# rock paper scissors
        if message.content.startswith(';rps'):
            await message.channel.send('Rock, Paper, or Scissors?')

            def win(m):
                return m.author == message.author and m.contnt.isdigit()

            cpu = random.randint(1,3)

            try:
                player = await self.wait_for('message', check=win, timeout=5.0)            
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long')
            #cpu plays rock
            if cpu == 1 and player.content == 'Rock':
                await message.channel.send('CPU played **Rock** and you played **Rock. TIE**')
            elif cpu == 1 and player.content == 'Paper':
                await message.channel.send('CPU played **Rock** and you played **Paper. PLAYER WINS**')
            elif cpu == 1 and player.content == 'Scissors':
                await message.channel.send('CPU played **Rock** and you played **Scissors. CPU WINS**')
            #cpu plays paper
            if cpu == 2 and player.content == 'Rock':
                await message.channel.send('CPU played **Paper** and you played **Rock. CPU WINS**')
            elif cpu == 2 and player.content == 'Paper':
                await message.channel.send('CPU played **Paper** and you played **Paper. TIE**')
            elif cpu == 2 and player.content == 'Scissors':
                await message.channel.send('CPU played **Paper** and you played **Scissors. PLAYER WINS**')
            #cpu plays scissors
            if cpu == 3 and player.content == 'Rock':
                await message.channel.send('CPU played **Scissors** and you played **Rock. PLAYER WINS**')
            elif cpu == 3 and player.content == 'Paper':
                await message.channel.send('CPU played **Scissors** and you played **Paper. CPU WINS**')
            elif cpu == 3 and player.content == 'Scissors':
                await message.channel.send('CPU played **Scissors** and you played **Scissors. TIE**')


client = MyClient()
client.run('Nzc4MDY1OTY4MzkxOTEzNDky.X7MkZg.9bhEvfqmNsp5OzdZixKzXmwtJLo')





