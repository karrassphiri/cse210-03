"""
    This class is responsible to display the game response
 
    Author: Karrass
"""

class terminal_service:

    def __init__(self):
        self._input_letter = ""

    # this ask the player for a letter
    def ask_players_input(self):
            user_input = input("Guess a letter [a-z]: ")
            self._input_letter = user_input
            return self._input_letter
            
    
   
                

    # # this displays the parachute graphic
    # # def display_parachute_graphic(self, parachute):

    # #     for i in parachute:
    # #         print(i)

    # # this displays the "_" and letters
    # # def display_empty_word(self, hiddenWord):
    # #     display = ""
    # #     for i in hiddenWord:
    # #         display += f" {i}"
    # #     display += "\n"
    # #     print(display)

    # # this displays the game over message
    # def display_game_over(self):
    #     print("Game over!!")

    # # this displays the win message
    # def display_win_message(self):
    #     print("You win!!")
