import logging
import gym
from time import sleep

import doom_py

logger = logging.getLogger(__name__)

class DoomEnv(gym.Env):
    metadata = {'render.modes': ['human', 'rgb_array']}

    def _step(self, action):
        # action is a np array but DoomGame.make_action expects a list of ints
        list_action = [int(x) for x in action]
        try:
            state = self.game.get_state()
            reward = self.game.make_action(list_action)
            if self.game.is_episode_finished():
                is_finished = True
            else:
                is_finished = False
            return state.image_buffer.copy(), reward, is_finished, dict(game_variables=state.game_variables)

        except doom_py.vizdoom.doom_is_not_running_exception:
            return [], 0, True, {}

    def _reset(self):
        self.game.new_episode()
        return self.game.get_state().image_buffer.copy()

    def _render(self, mode='human', close=False):
        if close:
            if self.viewer is not None:
                self.viewer.close()
            return
        try:
            state = self.game.get_state()
            img = state.image_buffer
            if mode == 'rgb_array':
                return img
            elif mode is 'human':
                from gym.envs.classic_control import rendering
                if self.viewer is None:
                    self.viewer = rendering.SimpleImageViewer()
                self.viewer.imshow(img)
                sleep(0.02857)  # 35 fps = 0.02857 sleep between frames
        except doom_py.vizdoom.doom_is_not_running_exception:
            pass # Doom has been closed
