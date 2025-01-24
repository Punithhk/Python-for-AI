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

# import image
# sample = image.open("./check.jpg")
# pixels = list(sample.getdata())

n_states = env.observation_space
n_actions = env.action_space

print(n_states,n_actions)
#env.s = 254
print(env.render())

#possible actions/steps is 0 down, 1up, 2right, 3left, 4pickup, 5dropoff
#env.step(3)
print(env.render())
#state = env.action_space()
#print(state)

#without Q learning 
state = env.reset()
counter = 0
g = 0
reward = None

#env.render()
#random state 

#if reach target, reward is 20, picked and dropped custmer
while reward!=20:
    state, reward, done, info = env.step(env.action_space.sample()) #random action chosen
    counter +=1 
    g += reward

print("Solved in {} steps and {} total reward".format(counter,g))

