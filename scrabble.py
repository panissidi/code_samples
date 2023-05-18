#Created a scrabble program that lets players play words, and calculates the scores of words and players.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Added lowercase letters to the letters list so that the program can also recognize letters formatted in lowercase.
letters += [
    letter.lower()
    for letter
    in letters
]

#Duplicated the points list to match the length of the letters list, which is twice as long after the addition of the lowercase letters.
points *= 2

#Combined the letters and points lists into a dictionary so that each letter corresponds to a point value.
letters_to_points = {
    key:value 
    for key, value 
    in zip(letters, points)
}

#Added a key:value pair to the dictionary that assigns empty spaces to a 0 point value.
letters_to_points[""] = 0

def score_word(word):
    """
    Score a word.

    Parameters
  
    ----------
    
    word: string
          The word to score. Acceptable formats include uppercase, lowercase, or a mix of both.

    Returns

    -------

    point_total: int
                 The word's total point value based on its letters' combined point values.

    """
    point_total = 0
    for letter in word:
      point_total += letters_to_points.get(letter, 0)
    return point_total

#Created a dictionary so that up to four people can play. If necessary, change the keys to the desired names of the players; for example, change "player1" to "Anthony". Also, if necessary, add more players; for example, players_to_words["player5] = [].
players_to_words = {
    "player1": [], 
    "player2": [], 
    "player3": [],
    "player4": []
  }

def play_word(player, word):
    """
    Play a word for a specified player.

    Parameters
  
    ----------

    player: string
            The name of the player.

    word: string
          The word to play. Acceptable formats include uppercase, lowercase, or a mix of both.

    Returns

    -------

    players_to_words: dict
                      The players and their words.

    """
    players_to_words[player].append(word)
    return players_to_words

#Created an empty dictionary to hold players and their scores.
players_to_points = {}

def caclulate_player_points():
    """
    Calculate all players' points.

    """
    for player, words in players_to_words.items():
      player_points = 0
      for word in words:
        player_points += score_word(word)
        players_to_points[player] = player_points

#Calculated and printed player points to test the code.
caclulate_player_points()
print(caclulate_player_points())
