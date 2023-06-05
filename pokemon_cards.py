# Created a program that lets users enter different types of Pokemon cards.

class Rare_Holofoil_Pokemon_Cards:
      """
      Represents a rare holofoil Pokemon card.

      Attributes
      ----------
      name: string
            The name of the Pokemon on the card, such as Charizard.
              
      level: integer
             The level of the Pokemon on the card, such as 1, 2, or 3.
               
      type: string
            The type of Pokemon on the card, such as water, fire, or grass.

      Methods
      -------
      __init__(self, name, level, type): 
                                        Initializes a Pokemon card object with the given name, level, and type.
        
      __repr__(self): 
                     Returns a string representation of the Pokemon card.
      """
        
    def __init__(self, name, level, type):
      """
      Initilaizes an instance of a Rare_Holofoil_Pokemon_Card object.
      
      Parameters
      ----------
      name: string
            The name of the Pokemon on the card, such as Blastoise.
              
      level: integer
             The level of the Pokemon on the card, such as 1, 2, or 3.
               
      type: string
            The type of Pokemon on the card, such as water, fire, or grass
      """
      self.name = name
      self.level = level
      self.type = type
    
    def __repr__(self):
      """
      Creates a string representation of a Rare_Holofoil_Pokemon_Card object.
      
      Returns
      -------
      A string representation of a Rare_Holofoil_Pokemon_Card object.
      """
      return "{name} is a level {level} {type} Pokemon.".format(name = self.name, level = self.level, type = self.type)

Blastoise = Rare_Holofoil_Pokemon_Cards("Blastoise", 3, "water")
print(Blastoise)

class Uncommon_NonHolofoil_Pokemon_Cards:
      """
      Represents an uncommon nonholofoil Pokemon card.

      Attributes
      ----------
      name: string
            The name of the Pokemon on the card, such as Wartortle.
              
      level: integer
             The level of the Pokemon on the card, such as 1, 2, or 3.
               
      type: string
            The type of Pokemon on the card, such as water, fire, or grass.

      Methods
      -------
      __init__(self, name, level, type): 
                                        Initializes a Pokemon card object with the given name, level, and type.
        
      __repr__(self): 
                     Returns a string representation of the Pokemon card.
      """
        
    def __init__(self, name, level, type):
       """
      Initilaizes an instance of an Uncommon_Nonholofoil_Pokemon_Card object.
      
      Parameters
      ----------
      name: string
            The name of the Pokemon on the card, such as Blastoise.
              
      level: integer
             The level of the Pokemon on the card, such as 1, 2, or 3.
               
      type: string
            The type of Pokemon on the card, such as water, fire, or grass
      """
      self.name = name
      self.level = level
      self.type = type
    
    def __repr__(self):
      """
      Creates a string representation of an Uncommon_Nonholofoil_Pokemon_Card object.
      
      Returns
      -------
      A string representation of an Uncommon_Nonholofoil_Pokemon_Card object.
      """
      return "{name} is a level {level} {type} Pokemon.".format(name = self.name, level = self.level, type = self.type)

Wartortle = Uncommon_NonHolofoil_Pokemon_Cards("Wartortle", 2, "water")
print(Wartortle)

class Common_NonHolofoil_Pokemon_Cards:
     """
      Represents a common nonholofoil Pokemon card.

      Attributes
      ----------
      name: string
            The name of the Pokemon on the card, such as Squirtle.
              
      level: integer
             The level of the Pokemon on the card, such as 1, 2, or 3.
               
      type: string
            The type of Pokemon on the card, such as water, fire, or grass.

      Methods
      -------
      __init__(self, name, level, type): 
                                        Initializes a Pokemon card object with the given name, level, and type.
        
      __repr__(self): 
                     Returns a string representation of the Pokemon card.
      """
        
    def __init__(self, name, level, type):
      """
      Initilaizes an instance of a Common_Nonholofoil_Pokemon_Card object.
      
      Parameters
      ----------
      name: string
            The name of the Pokemon on the card, such as Squirtle.
              
      level: integer
             The level of the Pokemon on the card, such as 1, 2, or 3.
               
      type: string
            The type of Pokemon on the card, such as water, fire, or grass
      """
      self.name = name
      self.level = level
      self.type = type
    
    def __repr__(self):
      """
      Creates a string representation of a Common_Nonholofoil_Pokemon_Card object.
      
      Returns
      -------
      A string representation of an Common_Nonholofoil_Pokemon_Card object.
      """
      return "{name} is a level {level} {type} Pokemon.".format(name = self.name, level = self.level, type = self.type)

Squirtle = Common_NonHolofoil_Pokemon_Cards("Squirtle", 1, "water")
print(Squirtle)
