import disnake
import random
import sys
from disnake.ext import commands

# legacy code I guess????

class discorBot2(disnake.Client):
    async def on_ready(self):
        print('logged on as', self.user)
        async for guild in client.fetch_guilds(limit=150):
                print(guild.name)
    
    async def on_message(self, message):

        if message.author == self.user: # don't respond to ourselves
            return
        
        print(f'Message from {message.author}: {message.content}') # simple logging

        if message.content == 'ping':
            await message.channel.send('Pong')
        
        if message.content == 'whoareyou':
            await message.channel.send('I am ' + str(self.user))
        
        if message.content == 'whoami':
            await message.channel.send('You are ' + str(message.author))
        
        if message.content == 'SCREAMS':
            await message.channel.send('L, Loser. Imagine not being able to fix this')

        if message.content == 'POGGERS':
            name = str(message.author)
            name = ''.join(name.split())[:-5] # remove the last 5 characters from name
            await message.channel.send('I fucking knew it ' + name + ', you fucking did it you madman')
        
        if message.content == 'restart': # TODO try to create another process that starts this process again
            if str(message.author) == "supermikea#5051":
                await message.channel.send('This still needs to be finished')
        
        if message.content == 'rps':
            comp_choice = random.randint(0, 3)
            gamemessage = await message.channel.send('What will you choose?')
            await gamemessage.add_reaction("🪨")
            await gamemessage.add_reaction("✂️")
            await gamemessage.add_reaction("🧻")

# required setup

intents = disnake.Intents.default()
intents.message_content = True
client = discorBot2(intents=intents)

def write_read_tk(option, token,): # write or read token from token file
    if option:
        file = open(sys.path[0] + "/token", "w")
        file.write(token)
        file.close()
        return 0
    else:
        file = open(sys.path[0] + "/token", "r")
        token = file.read()
        file.close()
        return token

if __name__ == "__main__": # run the bot
    try:
        client.run(str(write_read_tk(False,0)))
    except:
        client.run(str(write_read_tk(True, str(input("token: ")))))
