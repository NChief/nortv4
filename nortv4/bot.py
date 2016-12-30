from asyncirc import irc
import configparser
from configtools import Configtools
import importlib
import sys
import plugins.commands
import plugins.handleplugins

config = configparser.ConfigParser()
config.read('config.ini')

ct = Configtools(config)

channels = ct.GetChannels()

bot = irc.connect(config['bot'].get('server'), config['bot'].getint('port'), use_ssl=config['bot'].getboolean('ssl')) \
         .register(config['bot'].get('nick'), config['bot'].get('user'), config['bot'].get('name')) \
         .join(list(channels.keys()))

#@bot.on("public-message")
#def on_public_message(message, user, target, text):
#  if text == "load":
#    importlib.import_module('plugins.test')
#    print("OK")
#    print(irc.plugins)
#  if text == "reload":
#    importlib.reload(sys.modules['plugins.test'])
         
import asyncio
asyncio.get_event_loop().run_forever()