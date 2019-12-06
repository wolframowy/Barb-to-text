const Discord = require('discord.js');
var logger = require('winston');
var auth = require('./auth.json');

// Configure logger settings
logger.remove(logger.transports.Console);
logger.add(logger.transports.Console, {
    colorize: true
});
logger.level = 'debug';
// //Initialize Discord Bot
const bot = new Discord.Client();

bot.on('ready', () => {
    logger.info('Connected');
});

bot.on('message', message => {
	// Bot needs to know if it will execute a command
	// It will listen for messages that will start with `!`
	if (message.content.substring(0, 1) == '!') {
		var args = message.content.substring(1).split(' ');
		var cmd = args[0];

	   
		switch(cmd) {
			case 'help' :
				message.author.send(
					"Here are the commands available to you:\n!help \n!bttpm [message] \n!bttm"
				).catch(console.error);
			break;
			case 'bttpm':
				args.shift();
				var txt = args.join(' ');
				message.channel.send(pokemonText(txt)).catch(console.error);
				message.delete().catch(console.error);
			break;
			case 'bttm' :
				message.channel.fetchMessages({limit: 2})
								.then(messages => {
									if(messages.array()[1].content) {
										messages.array()[1].channel
											.send(pokemonText(messages.array()[1].content)).catch(console.error)};
									messages.array()[0].delete().catch(console.error);
									}
								).catch(console.error);
			break;
			// Just add any case commands if you want to..
		 }
	 }
});

bot.login(auth.token);

function pokemonText(txt) {
	var alt = 0;
	var newTxt = [];
	for (var i = 0, len = txt.length; i < len; i++) {
		if (alt === 0) {
			newTxt[i] = txt[i].toUpperCase();
			alt = 1;
		}
		else {
			newTxt[i] = txt[i].toLowerCase();
			alt = 0;
		}
	}
	return newTxt.join('');
}

