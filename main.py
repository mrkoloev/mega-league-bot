import discord
import telegram_bot
from config import DISCORD_TOKEN, TG_TOKEN, TG_CHAT_ID
import parser

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message, game_url=None):
    # if message.author == client.user:
    #     return

    # send game recap
    if 'gamerecap' in message.content:
        msg = message.content
        game_url=msg[msg.find('http'):]
        parser.download_recap_img(game_url)
        img_path = game_url[game_url.find("gamerecap"):] + '.png'
        await telegram_bot.send_img(img_path=img_path, chat_id=TG_CHAT_ID, token=TG_TOKEN, url=game_url)

    if 'league' in message.content:
        # print(type(message.content))
        await telegram_bot.send_msg(msg=message.content, chat_id=TG_CHAT_ID, token=TG_TOKEN)
        # await message.channel.send("JJJ")

client.run(token=DISCORD_TOKEN)
