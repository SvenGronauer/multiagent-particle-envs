import os
import warnings

from gym.envs.registration import register

# Multiagent envs
# ----------------------------------------

register(
    id='MultiagentSimple-v0',
    entry_point='multiagent.envs:SimpleEnv',
    # FIXME(cathywu) currently has to be exactly max_path_length parameters in
    # rllab run script
    max_episode_steps=100,
)

register(
    id='MultiagentSimpleSpeakerListener-v0',
    entry_point='multiagent.envs:SimpleSpeakerListenerEnv',
    max_episode_steps=100,
)


register(
    id='Simple-v0',
    entry_point='multiagent.envs.simple:SimpleEnv',
    max_episode_steps=100,
)

register(
    id='Simplespread-v2',
    entry_point='multiagent.envs.simple_spread:SimpleSpreadEnv',
    max_episode_steps=100,
)