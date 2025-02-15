## Mujoco库安装（[链接](https://zhuanlan.zhihu.com/p/502112539)）

- 解决部分报错：https://blog.csdn.net/li1873997/article/details/130811131?ops_request_misc=%257B%2522request%255Fid%2522%253A%25223d7d8ffacd747991f6e0d41d71799e4a%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=3d7d8ffacd747991f6e0d41d71799e4a&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-130811131-null-null.142^v100^pc_search_result_base6&utm_term=ImportError%3A%20DLL%20load%20failed%20while%20importing%20cymj%3A%20%E6%89%BE%E4%B8%8D%E5%88%B0%E6%8C%87%E5%AE%9A%E7%9A%84%E6%A8%A1%E5%9D%97%E3%80%82&spm=1018.2226.3001.4187

- 以下为测试代码：*（mujoco和mujoco_py路径需要更换成自己的！）*

```python
'''conda activate gym'''

import os
os.add_dll_directory(r"C:\Users\Administrator\.mujoco\mjpro150\bin")
os.add_dll_directory(r"E:\anaconda_cdh\envs\gym\Lib\site-packages\mujoco_py")
 
import mujoco_py
import os
mj_path,_= mujoco_py.utils.discover_mujoco()

print(mj_path)

xml_path = os.path.join(mj_path, 'model', 'humanoid.xml')
model = mujoco_py.load_model_from_path(xml_path)
sim = mujoco_py.MjSim(model)
print(sim.data.qpos)
sim.step()
print(sim.data.qpos)
```

- 安装成功则如下图所示：

![测试成功图](https://github.com/cdh66666/Deep_RL_Control/blob/main/img_for_readme/mujoco%26mujoco_py%E5%AE%89%E8%A3%85%E6%88%90%E5%8A%9F%E6%B5%8B%E8%AF%95%E5%9B%BE.png)

- 测试gym环境：

```python
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
```

![蚂蚁环境](https://github.com/cdh66666/Deep_RL_Control/blob/main/img_for_readme/mujoco-%E8%9A%82%E8%9A%81%E7%8E%AF%E5%A2%83.gif)

