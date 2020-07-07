from gym.envs.registration import register



register(
    id = 'OctaKing-v0',
    entry_point = 'gym_OctaKing.envs:OctaKingEnv'
)
