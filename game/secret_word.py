import random
"""
This class is risponsible for choosing randomly a secret word

"""
class Secret_word:
    """This class is risponsible OF choosing a random secret word for the game

    Attributes:
    
    random_words (word): This will store the random words created by the random_word library
    word (word): This is going to have the secret selected random word

    """
  

    def __init__(self):
        self._word = ""
        self._word_list = []
        self.word_characters_list = []
        self._empty_word = []

    #this generates a random word from the list
    def secret_word(self):  

        #return a single random word in CAPS

        self._word_list = ["apple", "ability", "agency", "argue", "attack", "biscuit", "baby", "behavior", "blue", "budget",
         "camel", "campaign", "choice", "cup", "crime", "dinosaur", "design", "draw", "difference", "despite", "elegance",
         "education", "exactly", "executive", "evidence", "family", "fear", "follow", "forward", "future", "galaxy", "government"]
        
        self._word = random.choice(self._word_list)
        self._hidden_word()

    #this generates a list of "_"
    def _hidden_word(self):

        self.word_characters_list = list(self._word)
        for each_character in range(len(self.word_characters_list)):
            each_character = "_" * len(self.word_characters_list) 
            self._empty_word = list(each_character) 
        
        return self._empty_word
        

            
        