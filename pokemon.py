class Rare_Holofoil_Pokemon_Cards:
    def __init__(self, name, level, type):
      self.name = name
      self.level = level
      self.type = type
    
    def __repr__(self):
      return "{name} is a level {level} {type} Pokemon.".format(name = self.name, level = self.level, type = self.type)

Blastoise = Rare_Holofoil_Pokemon_Cards("Blastoise", 3, "water")
print(Blastoise)

class Uncommon_NonHolofoil_Pokemon_Cards:
    def __init__(self, name, level, type):
      self.name = name
      self.level = level
      self.type = type
    
    def __repr__(self):
      return "{name} is a level {level} {type} Pokemon.".format(name = self.name, level = self.level, type = self.type)

Wartortle = Uncommon_NonHolofoil_Pokemon_Cards("Wartortle", 2, "water")
print(Wartortle)

class Common_NonHolofoil_Pokemon_Cards:
    def __init__(self, name, level, type):
      self.name = name
      self.level = level
      self.type = type
    
    def __repr__(self):
      return "{name} is a level {level} {type} Pokemon.".format(name = self.name, level = self.level, type = self.type)

Squirtle = Common_NonHolofoil_Pokemon_Cards("Squirtle", 1, "water")
print(Squirtle)
