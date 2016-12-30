from blinker import signal

commands = []

def addcom(sender, cmd, info):
  commands.append({'cmd': cmd, 'info': info})
  
def pubmsg(message, user, target, text):
  if text == '!commands':
    s = []
    for v in commands:
      s.append("{} ({})".format(v['cmd'], v['info']))
    message.client.say(target,  "Commands: " + ", ".join(s))

signal("command-added").connect(addcom)
signal("public-message").connect(pubmsg)
signal("plugin-registered").send("plugins.commands")