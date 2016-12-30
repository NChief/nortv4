from blinker import signal
from asyncirc import irc

def hpmsg(message, user, target, text):
  print("LOLSAAaaBBBccc:D")
  print(irc.plugins)
  
signal("public-message").connect(hpmsg)
signal("plugin-registered").send("plugins.test")