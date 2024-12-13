#! /user/bin/env python
import gym
env = gym.make("Ant-v2", render_mode="human") #create a mountaincar environment
env.reset()
for _ in range(2000):   # run for 2000 steps
    env.render()
    env.step(env.action_space.sample())  #send a random action 

