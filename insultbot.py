import discord
import random
import time
import os


def wait(time_amount):
  time.sleep(time_amount)

client = discord.Client()

insults = ['Fuck you', 'Get a life']


@client.event

async def on_ready():
   #this is were the bot logs on

  await client.change_presence(activity=discord.Game(name='On v1.04 !help'))
  print(f'Logged in')
  


@client.event

async def on_message(message):
  #this is were a mesage is sent

  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)

  #now we have all the commands
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


  if user_message.lower() == '!dicklength':

    dicklength = random.randint(1,10)
    await message.channel.send(f'{username}s dick length is...{dicklength} inches')
    print(f'!dicklength command used by {username}')


  if user_message.lower() == '!randomnumber':
    number = random.randint(1,100)
    await message.channel.send(f'Your random number is {number}')
    print(f'!randomnumber command used by {username}')


  if user_message.lower() == '!help':
    await message.channel.send('!hello !insultme !pog !dicklength !randomnumber !ball')
    print(f'!help command used by {username}')


  if '!ball' in user_message:
    yn = random.randint(1,2)
    if yn == 1:
      await message.channel.send('Yes')
    else:
      await message.channel.send('No')
    print(f'!ball command used by {username}')


  if user_message.lower() == '!pope':
    await message.channel.send(file=discord.File('spinning-priest-priest.gif'))
    print(f'!pope command used by {username}')

  

#all repl.its are public so i needed to hide the token
my_secret = os.environ['token']
client.run(my_secret)

#gtg cya tmmr

