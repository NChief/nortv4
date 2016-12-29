from asyncirc import irc
import configparser
from configtools import Configtools

config = configparser.ConfigParser()
config.read('config.ini')

ct = Configtools(config)

channels = ct.GetChannels();

#bot = irc.connect()