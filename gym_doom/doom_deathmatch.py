import logging
import os
from gym import error, spaces
import numpy as np
from gym_doom import doom_env, spaces as doom_spaces

from doom_py import DoomGame, Mode, Button, GameVariable, ScreenFormat, ScreenResolution, Loader

logger = logging.getLogger(__name__)

class DoomDeathmatchEnv(doom_env.DoomEnv):
    """
    ------------ Final Mission - Deathmatch ------------
    Kill as many monsters as possible without being killed.

    Allowed actions:
        ALL
    Note: see controls.md for details

    Rewards:
        +1      - Killing a monster

    Goal: 25 points
        Kill 25 monsters without being killed

    Ends when:
        - Player is dead
        - Timeout (3 minutes - 6,300 frames)
    -----------------------------------------------------
    """
    def __init__(self):
        package_directory = os.path.dirname(os.path.abspath(__file__))
        self.loader = Loader()
        self.game = DoomGame()
        self.game.load_config(os.path.join(package_directory, 'assets/deathmatch.cfg'))
        self.game.set_vizdoom_path(self.loader.get_vizdoom_path())
        self.game.set_doom_game_path(self.loader.get_freedoom_path())
        self.game.set_doom_scenario_path(self.loader.get_scenario_path('deathmatch.wad'))
        self.screen_height = 480                    # Must match .cfg file
        self.screen_width = 640                     # Must match .cfg file
        # 41 allowed actions (must match .cfg file)
        self.action_space = doom_spaces.HighLow(np.matrix([[0, 1, 0]] * 36 + [[0, 10, 0]] * 5))
        self.observation_space = spaces.Box(low=0, high=255, shape=(self.screen_height, self.screen_width, 3))
        self.game.set_window_visible(False)
        self.viewer = None
        self.game.init()
        self.game.new_episode()
