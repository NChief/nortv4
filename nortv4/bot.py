from asyncirc import irc
import configparser
from configtools import Configtools

config = configparser.ConfigParser()
config.read('config.ini')

ct = Configtools(config)

channels = ct.GetChannels()

bot = irc.connect(config['bot'].get('server'), config['bot'].getint('port'), use_ssl=config['bot'].getboolean('ssl'))
bot.register(config['bot'].get('nick'), config['bot'].get('user'), config['bot'].get('name'))
bot.join(list(channels.keys()))

import asyncio
asyncio.get_event_loop().run_forever()