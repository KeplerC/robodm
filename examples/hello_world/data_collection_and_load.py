import robodm
import numpy as np
import time 

path = "/tmp/output3.vla"

# remove the existing file
import os
os.system(f"rm -rf {path}")
os.system(f"rm -rf /tmp/*.cache")

# 🦊 Data collection: 
# create a new trajectory
traj = robodm.Trajectory(
    path = path, mode = "w"
)

# collect step data for the episode
for i in range(10):
    time.sleep(0.001)
    traj.add(feature = "arm_view", data = np.ones((640, 480, 3), dtype=np.uint8))
    traj.add(feature = "gripper_pose", data = np.ones((4, 4), dtype=np.float32))
    traj.add(feature = "view", data = np.ones((640, 480, 3), dtype=np.uint8))
    traj.add(feature = "wrist_view", data = np.ones((640, 480, 3), dtype=np.uint8))
    traj.add(feature = "joint_angles", data = np.ones((7,), dtype=np.float32))
    traj.add(feature = "joint_velocities", data = np.ones((7,), dtype=np.float32))
    traj.add(feature = "joint_torques", data = np.ones((7,), dtype=np.float32))
    traj.add(feature = "ee_force", data = np.ones((6,), dtype=np.float32))
    traj.add(feature = "ee_velocity", data = np.ones((6,), dtype=np.float32))
    traj.add(feature = "ee_pose", data = np.ones((4, 4), dtype=np.float32))
    print(f"added step {i}")

traj.close()

traj = robodm.Trajectory(
    path = path
)
print(traj.load())