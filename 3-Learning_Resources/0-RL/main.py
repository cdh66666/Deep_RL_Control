import os
os.add_dll_directory(r"C:\Users\Administrator\.mujoco\mjpro150\bin")
os.add_dll_directory(r"E:\anaconda_cdh\envs\gym\Lib\site-packages\mujoco_py")


import gym
# import mujoco
env = gym.make('InvertedPendulum-v2', render_mode='human')
env = env.unwrapped
for episode in range(20):
    observation = env.reset() #环境重置
    print(episode)
    # for timestep in range(100):
    while True:
        # print(timestep)
        env.render() #可视化
        action = env.action_space.sample() #动作采样
        observation_, reward, done, info = env.step(action)[:4]
        # if done:
        #     # print(observation)
        #     print('Episode {}'.format(episode))
        #     break
        observation=observation_
env.close()