class Configtools:
  def __init__(self, config):
    self.config = config
  
  def GetGroup(self, find):
    group = {}
    for section in self.config.sections():
      gs = section.split()
      if gs[0] == find:
        #group.append(section)
        group[gs[1]] = self.config[section]
    return group
  
  def GetChannels(self):
    return self.GetGroup('channel')
    
  def GetPlugins(self):
    return self.GetGroup('plugin')