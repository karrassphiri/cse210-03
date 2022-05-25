
class Jumper:
    """A person closer to ground when guessed wrong.
    
    Attributes:
        is_alive (boolean): Whether or not the jumper is alive
        
    """
    
    def __init__(self):
        """Constructs a Jumper.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self._is_alive = True
        self._level = 0
            
    def draw_jumper(self):
        #Parachute
       
    
    #getter and setter for is_alive
    def get_alive(self):
        return self._is_alive

    def set_alive(self, is_alive):
        self._is_alive = is_alive

    #getter and setter for level
    def get_level(self):
        return self._level
    
    def set_level(self, level):
        self._level = level
