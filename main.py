import random

def generate_letter_scores() -> dict:
    return {
  "E": 1, "A": 1, "I": 1, "O": 1,
  "N": 1, "R": 1, "T": 1, "L": 1,
  "S": 1, "U": 1, "D": 2, "G": 2,
  "B": 3, "C": 3, "M": 3, "P": 3,
  "F": 4, "H": 4, "V": 4, "W": 4,
  "Y": 4, "K": 5, "J": 8, "X": 8,
  "Q": 10, "Z": 10
}


def score_word(word: str) -> int:
    if not isinstance(word, str):
        raise TypeError("Not a valid word.")

    if word == "":
        raise ValueError("No letters found in word.")
        
    sum = 0
    scores = generate_letter_scores()
    word = word.upper()

    for i in word:
        if i in scores:
            sum += scores[i]
    
    return sum

def generate_player_hand() -> list:
    rack = []
    bag = "AAAAAAAAABBCCDDDDDEEEEEEEEEEEEFFGGGHHIIIIIIIIIJKLLLLMMNNNNNNOOOOOOOOPPQRRRRRRSSSSTTTTTTUUUUVVWWXYYZ"
    for i in range(7):
       random_tile = random.choice(bag)
       rack.append(random_tile)
       bag.replace(random_tile, "", 1)
    
    return rack