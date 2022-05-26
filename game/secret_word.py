import random
"""
This class is risponsible for choosing randomly a secret word

"""
class secret_word:
    """This class is risponsible OF choosing a random secret word for the game

    Attributes:
    
    random_words (word): This will store the random words created by the random_word library
    word (word): This is going to have the secret selected random word

    """
  

    def __init__(self):
        self._word_list = ["apple", "agent"]
        self._word = random.choice(self._word_list)

    #this generates a random word from the list
    # def secret_word(self):  

    #     #return a single random word in CAPS

        
    #     #["attic", "blood", "books", "budget",
    #     # "camel", "cargo", "crime", "dried", "facts", "forest"]
        
    #     #print(self._word)
    #     #self._hidden_word()
    #     return self._word
        

    # #this generates a list of "_"
    # def _hidden_word(self):

    #     self.word_characters_list = list(self._word)
    #     for each_character in range(len(self.word_characters_list)):
    #         each_character = "_" * len(self.word_characters_list) 
    #         self._empty_word = list(each_character) 
        
    #     return self._empty_word
        

            
        