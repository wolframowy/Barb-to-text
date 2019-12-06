# Barb-to-text discord bot readme

This is a code for Discord bot that allows "To WrItE lIkE tHaT" or to mock other people.
As for now there are available 3 commands:
`!btthelp` - whispers all available commands
`!bttpm [message]` - converts the message to cancer giving format
`!bttm` - mocks the person above by converting what they said to cancer giving format

Source files do not include bot token without which it's impossible to run the bot. If you want to add the token, follow the discord tutorial https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token and add the file auth.json in format 

```
{
   "token": "YOUR_TOKEN_HERE" 
}
```

**To run this bot you need to have Python installed on your machine.**

**The only dependency is `discord.py`.**

**To run the bot run `python bot.js`**
