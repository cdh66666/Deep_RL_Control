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