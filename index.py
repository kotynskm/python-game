""" Arcade Platformer """

import arcade
import pathlib

# Game Constants
# Window Dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Adventure Time"

# Assets path using pathlib to ensure path works correctly on Windows, Mac, or Linux
ASSETS_PATH = pathlib.Path(__file__).resolve().parent.parent / "assets"

class Platformer(arcade.Window):
    def __init__(self) -> None:
        """ Code here that handles actions that should be taken when game first starts. init function only runs when the game first starts. """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Sprite list - all sprites defined here only, will be fully implemented in setup
        self.coins = None
        self.background = None
        self.walls = None
        self.ladders = None
        self.goals = None
        self.enemies = None
        # Player Sprite
        self.player = None

        # Physics engine
        self.physics_engine = None

        # Score
        self.score = 0

        # Level
        self.level = 1

        # Load sounds
        # self.coin_sound = arcade.load_sound(
        #     str(ASSETS_PATH / "sounds" / "coin.wav")
        # )
        # self.jump_sound = arcade.load_sound(
        #     str(ASSETS_PATH / "sounds" / "jump.wav")
        # )
        # self.victory_sound = arcade.load_sound(
        #     str(ASSETS_PATH / "sounds" / "victory.wav")
        # )

        

    def setup(self):
        """Sets up the game for the current level. Place to add code that may be repeated throughout the game, such as initialize new level
         on success, or reset the current level on failure. """
        pass

    def on_key_press(self, key: int, modifiers: int):
        """Processes key presses

        Arguments:
            key {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were down at the time
        """

    def on_key_release(self, key: int, modifiers: int):
        """Processes key releases

        Arguments:
            key {int} -- Which key was released
            modifiers {int} -- Which modifiers were down at the time
        """

    def on_update(self, delta_time: float):
        """Updates the position of all game objects (this is where everything happens) - update scores, handle object collisions, play sound effects, animate sprites.

        Arguments:
            delta_time {float} -- How much time since the last call
        """
        pass

    def on_draw(self):
        """Where everything displayed in the game is drawn (only a few lines of code here typically). """
        pass

""" Create the game object window, setup the game, and run the game. """
if __name__ == "__main__":
    window = Platformer()
    window.setup()
    arcade.run()