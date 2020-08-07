import discord
from mcrcon import MCRcon
from secret.bot_token import token
from secret.mc_server_login import ip, port, password

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.contains(' server ') and message.content.contains(' lag '):
        with MCRcon(ip, password=password, port=port) as mcr:
            resp = mcr.command("tps")
            await message.channel.send(f'It appears you may be complaining about server lag! {resp}')

client.run(token)
