from game.terminal_service import Terminal_service
from game.secret_word import Secret_word
from game.jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        secret (SecretWord): Guessing secret word.
        is_playing (boolean): Whether or not to keep playing.
        parachute (PlayerParachute): To jump further.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._secret = Secret_word()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = Terminal_service()
        
    def _start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Jump further.

        Args:
            self (Director): An instance of Director.
        """
        new_location = self._terminal_service.read_word("\nGuess a letter [a-z]: ")
        self._player.move_location(new_location)
        
    def _do_updates(self):
        """Keeps guessing secret word to jump.

        Args:
            self (Director): An instance of Director.
        """
        self._word.watch_parachute(self._word)
        
    def _do_outputs(self):
        """Provides a hint for the player to use.

        Args:
            self (Director): An instance of Director.
        """
        hint = self._word.get_hint()
        self._terminal_service.write_text(hint)
        if self._word.is_found():
            self._is_playing = False