
class jumper:
    """A person closer to ground when guessed wrong.
    
    Attributes:
        is_alive (boolean): Whether or not the jumper is alive
        _level: indicates the jumpers paraschute strength
    """
    
    def __init__(self):
        """Constructs a Jumper.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self._is_alive = True
        self._level = 0
            
    def draw_jumper(self):
        """
        Draws a jumper with three parts Parachute,Jumper Alive,Jumper Dead.
        """
        #Parachute
        if self._level < 1:
            print(" ___")
        if self._level < 2:
            print("/___\\")
        if self._level < 3:
            print("\   /")
        if self._level < 4:
            print(" \ /")

        #Jumper head alive
        if self._is_alive:
            print("  o")
            print(" /|\\")
            print(" / \\")

        #Jumper head dead
        if not self._is_alive:
            print("  x")
            print(" /|\\")
            print(" / \\")
            print("~~~~~~")
    
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
