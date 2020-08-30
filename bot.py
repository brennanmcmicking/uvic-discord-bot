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

    if 'server' in message.content and ' lag' in message.content:
        with MCRcon(ip(), password=password(), port=port()) as mcr:
            resp = mcr.command('tps')
            msg = resp.replace('§6', '')
            msg = msg.replace('§a', '')
            print(msg)
            await message.channel.send(f'It appears you may be complaining about server lag! `{msg}`')

client.run(token())
