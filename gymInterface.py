# #Reinforcement Learning using Open AI gym package 
# import gym 
# env = gym.make("Taxi-v3")
# env.render(mode="Human")

# #env.reset, step(action) action can be observation, reward, done, info

import gym, pickle, os
import numpy as np 

env = gym.make("Taxi-v3",render_mode="rgb_array")
state = env.reset()
print(state)
print(env.render())

