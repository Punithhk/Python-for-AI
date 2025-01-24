
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


Q = np.zeros((env.observation_space.n,env.action_space.n))
#number of states, actions, intiliaze with 0 

total_episodes = 10000
G = 0
alpha = 0.81 
gamma = 0.96
#alpha = 0.618
max_steps = 200 

for episode in range(1,total_episodes+1):
    done = False
    G, reward = 0,0
    state = env.reset()
    firstState = state
    #print("intial state is {}".format(state))
    while done != True:
        action = np.argmax(Q[state])
        state2, reward, done, info = env.step(action)
        Q[state, action] = Q[state,action]+alpha*(reward+gamma*np.max(Q[state2]-Q[state,action]))
        G += reward
        state = state2
        noSteps = noSteps+1

print(Q) #Q table 

state = env.reset() #check how Q table updated
done = None

counter = 0
while done!=True:
    #take action with highest Q value
    action = np.argmax(Q[state])
    state,reward,done,info = env.step(action)
    env.render()
    counter = counter+1

    #once car picks passenger the car color changes to green 

print(counter)