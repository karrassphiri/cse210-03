from game.secret_word import secret_word
from game.terminal_service import terminal_service
from game.jumper import jumper


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        secret (SecretWord): Guessing secret word.
        is_playing (boolean): Whether or not to keep playing.
        Jumper (jumper): To jump further.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._secret = secret_word()
        self._jumper = jumper()
        self._terminal_service = terminal_service()

    def _start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            # self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_guess(self):
        """Gets the guesser classes inputs

        Args:
            self (Director): an instance of Director.
        """
        return self._terminal_service._get_inputs()

    def _get_inputs(self):
        """Jump further.

        Args:
            self (Director): An instance of Director.
        """
        return self._terminal_service.ask_players_input()

    def _do_updates(self):
        """Keeps guessing secret word to jump.

        Args:
            self (Director): An instance of Director.
        """
       # self._word.watch_parachute(self._word)
        level = self._jumper.get_level()

        guess = self._get_inputs()
        positions = self._secret.make_guess(guess)
        if positions:  # guess a letter correctly
            self._terminal_service.update_word(positions, guess)
        else:
            self._jumper.set_level(level + 1)

        if self._jumper.get_level() >= 4:
            self._jumper.set_alive(False)

        if not self._jumper.get_alive():
            self._win = False
            self._is_playing = False
        if self._secret.get_word() == self._terminal_service.get_word():
            self._win = True
            self._is_playing = False

    def _do_outputs(self):
        """Provides a hint for the player to use.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.display_word()
        self._jumper.draw_jumper()
        if not self._is_playing:
            if self._win:
                print("You Won!")
            else:
                print(f"You Lost, the word was: {self._secret.get_word()}")
