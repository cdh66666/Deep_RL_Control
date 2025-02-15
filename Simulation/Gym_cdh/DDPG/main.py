import gymnasium as gym
from DDPG import DDPGAgent
import numpy as np
import torch
import matplotlib.pyplot as plt

# 初始化环境
env = gym.make('Pendulum-v1',render_mode="human")
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.shape[0]

# 创建DDPG智能体
agent = DDPGAgent(state_dim, action_dim,hidden_dim=200)

# 训练智能体
max_episodes = 500
max_steps = 200
rewards = []

for episode in range(max_episodes):
    state, _ = env.reset(seed=episode)
    episone_reward = 0

    for step in range(max_steps):
        action = agent.select_action(state)
        next_state, reward, terminated, truncated, _ = env.step(action)
        agent.replay_buffer.push(state, action, reward, next_state, terminated)
        
        if len(agent.replay_buffer) > 128:
            agent.update()

        state = next_state
        episone_reward += reward

        if terminated or truncated:
            break

    rewards.append(episone_reward)

    # 实时显示每轮训练得到的奖励值
    print(f"Episode {episode + 1}, Total Reward: {episone_reward}")

    # 每1轮更新一次图像
    if (episode + 1) % 1 == 0:
        plt.plot(rewards)
        plt.xlabel('Episode')
        plt.ylabel('Total Reward')
        plt.title('Reward per Episode')
        plt.pause(0.01)  # 暂停一段时间，以便更新图像

    # 每隔20轮保存一次模型
    if (episode + 1) % 20 == 0:
        torch.save(agent.actor.state_dict(), f'DDPG/pendulum_actor.pth')
        torch.save(agent.critic.state_dict(), f'DDPG/pendulum_critic.pth')

# 计算平均奖励
avg_reward = np.mean(rewards)

# 显示最终的奖励曲线
plt.show()