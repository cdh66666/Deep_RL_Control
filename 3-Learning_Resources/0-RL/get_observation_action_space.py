#!/usr/bin/env python
import gym
from gym.spaces import *
import sys


def print_space(space):
    print(space)
    if isinstance(space,Box):
        print("\n space.low", space.low)
        print("\n space.high", space.high)


if __name__ == '__main__':
    env = gym.make(sys.argv[1])
    print("Observation Space:")
    print_space(env.observation_space)
    print("\n Action Space:")
    print_space(env.action_space)
    try:
        print("Action description/meaning:",env.unwrapped.get_action_meanings())
    except AttributeError:
        pass
 