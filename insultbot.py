import discord
import random

TOKEN = [HIDDEN]

client = discord.Client()

insults = ['Fuck you', 'Get a life']


@client.event

async def on_ready():

  print(f'Logged in')











@client.event

async def on_message(message):

  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)



    

  if user_message.lower() == '!hello':
    await message.channel.send(f'Hello!')
    print(f'!hello command used by {username}')


  
  if user_message.lower() == '!insultme':
    choice = random.randint(1,2)
    if choice == 1:
      await message.channel.send(f'Fuck you {username}')
    elif choice == 2:
      await message.channel.send(f'Get a life {username}')
    print(f'!insultme command used by {username}')



  if user_message.lower() == '!flipacoin':
    coin_choice = random.randint(1,2)
    if coin_choice == 1:
       await message.channel.send(f'Heads')
    else:
      await message.channel.send(f'Tails')
    print(f'!flipacoin command used by {username}')


  if user_message.lower() == '!pog':
    await message.channel.send(file=discord.File('pog.jpg'))
    print(f'!pog command used by {username}')
    

  

client.run(TOKEN)
