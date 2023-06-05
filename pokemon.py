class PokemonCards:
    def __init__(self, name, type, level, current_health, max_health):
      self.name = name
      self.type = type
      self.level = level
      self.current_health = current_health
      self.max_health = max_health

Blastoise = PokemonCards("Blastoise", "Water", 3, 100, 100)
print(Blastoise)