import discord
import logging
import json
import urllib, time

logging.basicConfig(level=logging.INFO)

token = json.load(open('auth.json'))['token']

client = discord.Client()

OPTIONS = {
    'help': 'btthelp',
    'bttpm': 'bttpm',
    'bttm': 'bttm'
}


def pokemon_text(txt: str):
    alt = 0
    new_txt = ""
    for i in range(txt.__len__()):
        if alt == 0:
            new_txt += txt[i].upper()
            alt = 1
        else:
            new_txt += txt[i].lower()
            alt = 0
    return new_txt


@client.event
async def on_ready():
    print("Bot's up. Everything went fine.")
    await client.change_presence(activity=discord.Game(name='!btthelp for list of commands'))


@client.event
async def on_message(message):
    if message.content[0] == '!':
        args = message.content[1:].split(' ')
        cmd = args[0]

        if cmd == OPTIONS['help']:
            await message.author.send(
                f"Here are the commands available to you:\n!{OPTIONS['help']} - display bot usage"
                f"\n!{OPTIONS['bttpm']} [message] - change given message to pokemon text"
                f"\n!{OPTIONS['bttm']} - mock person above")
        elif cmd == OPTIONS['bttpm']:
            await message.channel.send(pokemon_text(' '.join(str(arg) for arg in args[1:])))
            await message.delete()
        elif cmd == OPTIONS['bttm']:
            to_mock = await message.channel.history(limit=2).flatten()
            if to_mock[1]:
                await message.channel.send(pokemon_text(to_mock[1].content))
            await message.delete()
        # Just add any case commands if you want to..


loop_value = True
iteration = 0
while loop_value:
    try:
        urllib.request.urlopen("https://google.com")
        loop_value = False
    except urllib.error.URLError as e:
        print('Network is currently down')
        iteration += 1
        if iteration > 100:
            break
        time.sleep(5)
client.run(token)
