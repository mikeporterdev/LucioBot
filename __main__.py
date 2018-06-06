import os

from discord import ChannelType
from discord.ext.commands import Bot

from YouTubeService import YouTubeService

BOT_PREFIX = ("Lucio ", "l")

client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command()
async def play(url):
    voice_channel_list = []
    for server in client.servers:
        for channel in server.channels:
            if channel.type is ChannelType.voice:
                voice_channel_list.append(channel)

    channel = voice_channel_list[0]
    service = YouTubeService()
    service.download(url)

    # channel_join = await client.join_voice_channel(channel)
    # player = await channel_join.create_ytdl_player(YT_LINK)
    # player.volume = 0.05
    # player.start()

@client.command(pass_context=True)
async def join(context, *args):
	channel = context.message.author.voice_channel
	await client.join_voice_channel(channel)

client.run(os.environ.get('DISCORD_KEY'))
