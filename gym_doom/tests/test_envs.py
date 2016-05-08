import numpy as np
from nose2 import tools
import os

import gym_doom
from gym import envs

# This is copied from core gym

# This runs a smoketest on each official registered doom env. We may
# want to try also running environments which are not officially
# registered envs.
specs = [spec for spec in envs.registry.all() if spec._entry_point and spec._entry_point.startswith('gym_doom:')]
@tools.params(*specs)
def test_env(spec):
    env = spec.make()
    ob_space = env.observation_space
    act_space = env.action_space
    ob = env.reset()
    assert ob_space.contains(ob), 'Reset observation: {!r} not in space'.format(ob)
    a = act_space.sample()
    observation, reward, done, _info = env.step(a)
    assert ob_space.contains(observation), 'Step observation: {!r} not in space'.format(observation)
    assert np.isscalar(reward), "{} is not a scalar for {}".format(reward, env)
    assert isinstance(done, bool), "Expected {} to be a boolean".format(done)

    for mode in env.metadata.get('render.modes'):
        env.render(mode=mode)
    env.render(close=True)
