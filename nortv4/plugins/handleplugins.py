# YES I HANDLE PLUGINS IN A PLUGIN
from blinker import signal
from asyncirc import irc
import importlib
import sys

def load_plugin(p):
  try:
    importlib.import_module(p)
    return True
  except SyntaxError:
    print('SYNTAX ERROR')
    return False
  except:
    print('ERROR')
    return False

def reload_plugin(p):
  try:
    irc.plugins.remove(p) # Remove from list
    importlib.reload(sys.modules[p])
    return True
  except SyntaxError:
    print('SYNTAX ERROR')
    return False
  except:
    print('ERROR')
    return False
  

def unload_plugin(p):
  #http://stackoverflow.com/questions/1668223/how-to-de-import-a-python-module
  # HUSK COMMAND SHIT
  return False
 
def usage(message, target, type):
  message.client.say(target, "USAGE: {} <plugin_name>".format(type))
  
 
def pubmsg(message, user, target, text):
  s = text.split()
  
  # TODO: NEED TO CHECK IF ADMIN xD
  
  if s[0] == '!load':
    if len(s) != 2: usage(message, target, s[0])
    elif load_plugin(s[1]):
      message.client.say(target, "Plugin ({}) loaded.".format(s[1]))
    else:
      message.client.say(target, "Error loading plugin ({}).".format(s[1]))
  elif s[0] == '!reload':
    if len(s) != 2: usage(message, target, s[0])
    elif reload_plugin(s[1]):
      message.client.say(target, "Plugin ({}) reloaded.".format(s[1]))
    else:
      message.client.say(target, "Error reloading plugin ({}).".format(s[1]))
  elif s[0] == '!unload':
    message.client.say(target, "Ikke implementert.")

signal("public-message").connect(pubmsg)
signal("command-added").send("plugins.handle.plugins", cmd='!load', info='Load plugin')
signal("command-added").send("plugins.handle.plugins", cmd='!reload', info='Reload plugin')
signal("command-added").send("plugins.handle.plugins", cmd='!unload', info='Unload plugin')
signal("plugin-registered").send("plugins.handleplugins")