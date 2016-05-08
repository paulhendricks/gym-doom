from gym.envs import register

from gym_doom.doom_env import DoomEnv
from gym_doom.doom_basic import DoomBasicEnv
from gym_doom.doom_corridor import DoomCorridorEnv
from gym_doom.doom_defend_center import DoomDefendCenterEnv
from gym_doom.doom_defend_line import DoomDefendLineEnv
from gym_doom.doom_health_gathering import DoomHealthGatheringEnv
from gym_doom.doom_my_way_home import DoomMyWayHomeEnv
from gym_doom.doom_predict_position import DoomPredictPositionEnv
from gym_doom.doom_take_cover import DoomTakeCoverEnv
from gym_doom.doom_deathmatch import DoomDeathmatchEnv

# Doom
# ----------------------------------------

register(
    id='DoomBasic-v0',
    entry_point='gym_doom:DoomBasicEnv',
)

register(
    id='DoomCorridor-v0',
    entry_point='gym_doom:DoomCorridorEnv',
)

register(
    id='DoomDefendCenter-v0',
    entry_point='gym_doom:DoomDefendCenterEnv',
)

register(
    id='DoomDefendLine-v0',
    entry_point='gym_doom:DoomDefendLineEnv',
)

register(
    id='DoomHealthGathering-v0',
    entry_point='gym_doom:DoomHealthGatheringEnv',
)

register(
    id='DoomMyWayHome-v0',
    entry_point='gym_doom:DoomMyWayHomeEnv',
)

register(
    id='DoomPredictPosition-v0',
    entry_point='gym_doom:DoomPredictPositionEnv',
)

register(
    id='DoomTakeCover-v0',
    entry_point='gym_doom:DoomTakeCoverEnv',
)

register(
    id='DoomDeathmatch-v0',
    entry_point='gym_doom:DoomDeathmatchEnv',
)
