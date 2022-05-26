import random
"""
Imports 'random' a built in function of python.

"""


class secret_word:
    """This class is responsible of choosing a random secret word for the game

    Attributes:
    _word_list (words): This will store the random words created by the random_word library
    _word (word): This is going to have the secret selected random word

    """

    def __init__(self):
        self._word_list = ["apple", "agent", "attic", "blood", "books", "budget",
                           "camel", "cargo", "crime", "dried", "facts", "forest"]
        self._word = random.choice(self._word_list)

    def make_guess(self, guess):
        """Find the positions of the guess in the Secret Word"""
        positions = []
        for i, letter in enumerate(self._word):
            if guess == letter:
                positions.append(i)
        return positions

    def get_word(self):
        """Getter for the Secret Word"""
        return self._word
