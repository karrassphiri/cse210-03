"""
    This class is responsible to display the game response
 
    Author: Karrass
"""


class terminal_service:

    def __init__(self):
        self.guessed_word = ["_"] * 5
        self.previous_guesses = []

    # this ask the player for a letter
    def ask_players_input(self):
        """
        Validate that it is lowercase and no numbers and get input. Add guess to previous input list
        """
        user_input = input("Guess a letter [a-z]: ")
        self._input_letter = user_input
        self.previous_guesses.append(user_input)
        return self._input_letter

    def display_word(self):
        """display blanks/letter guessed correctly"""
        print(f"Previous Guesses: {self.previous_guesses}")
        print("".join(self.guessed_word))

    def get_word(self):
        """returns the word as a string rather than a list"""
        return "".join(self.guessed_word)

    def update_word(self, positions, guess):
        """update the word every time the guess is correct"""
        for position in positions:
            self.guessed_word[position] = guess
