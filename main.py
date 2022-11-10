import random
import sys

import disnake
from disnake.ext import commands

# required setup
intents = disnake.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                      intents=intents)
global rcount


@client.event
async def on_ready():
    print("logged on as", client.user)
    async for guild in client.fetch_guilds(limit=150):
        print(guild.name)


@client.event
async def on_message(message):

    if message.author == client.user:  # don't respond to ourselves
        return

    print(
        f"Message from {message.author}: {message.content}")  # simple logging

    if message.content == "ping":
        await message.channel.send("Pong")

    if message.content == "whoareyou":
        await message.channel.send("I am " + str(client.user))

    if message.content == "whoami":
        await message.channel.send("You are " + str(message.author))

    if message.content == "SCREAMS":
        await message.channel.send(
            "L, Loser. Imagine not being able to fix this")

    if message.content == "POGGERS":
        name = str(message.author)
        name = "".join(
            name.split())[:-5]  # remove the last 5 characters from name
        await message.channel.send("I fucking knew it " + name +
                                   ", you fucking did it you madman")

    if (message.content == "restart"
        ):  # TODO try to create another process that starts this process again
        if str(message.author) == "supermikea#5051":
            await message.channel.send("This still needs to be finished")

    if message.content == "rps":
        comp_choice = random.randint(0, 3)
        gamemessage = await message.channel.send("What will you choose?")
        await gamemessage.add_reaction("🪨")
        await gamemessage.add_reaction("✂️")
        await gamemessage.add_reaction("🧻")

    if str(message.author) == "disborbrob#0650":  # react to this bot
        if rcount / 5 == 0:
            rcount = 0
            name = str(message.author)
            name = "".join(name.split())[:-5]
            await message.reply("Is this " + name + "?", mention_author=True)
        else:
            rcount = rcount + 1

    if message.content.startswith("repeat "):
        messagetosend = message.content[7:]
        await message.channel.send(messagetosend)


@client.command()
async def send_button(ctx: commands.Context):
    await ctx.send(
        "Here's a button!",
        components=disnake.ui.Button(label="Click me!",
                                     custom_id="cool_button"),
    )

    # async def on_reaction_add(reaction, user):
    #    if str(user) == str(self.user):
    #        return 0
    #    print(user)
    #    print(reaction)


def write_read_tk(
    option,
    token,
):  # write or read token from token file
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


if __name__ == "__main__":  # run the bot
    try:
        client.run(str(write_read_tk(False, 0)))
    except:
        client.run(str(write_read_tk(True, str(input("token: ")))))
