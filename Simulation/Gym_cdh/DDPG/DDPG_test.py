import gymnasium as gym
import numpy as np
import torch
from DDPG import Actor 
  


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device("cpu")

# 初始化环境
env = gym.make('Pendulum-v1', render_mode="human")
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.shape[0]


#测试DDPG训练效果并可视化
#加载模型
actor = Actor(state_dim, action_dim).to(device)
actor.load_state_dict(torch.load('DDPG\\pendulum_actor.pth', weights_only=True))
actor.eval()

 
episons = 10
max_steps = 200

for episode in range(episons):
    state, _ = env.reset()
    episone_reward = 0

    for step in range(max_steps):
        #选择动作
        action = actor(torch.FloatTensor(state).to(device)).cpu().data.numpy()
        #执行动作
        next_state, reward, terminated, truncated, _ = env.step(action)

        #更新状态
        state = next_state
        episone_reward += reward

        #渲染环境
        env.render()
        if terminated or truncated:
            break

    print(f"Episode {episode + 1}, Total Reward: {episone_reward}")

#关闭环境
env.close()
 