from robodm.loader.hdf5 import HDF5Loader
import robodm

import os
os.system("rm -rf /tmp/robodm/*")

loader = HDF5Loader("/home/kych/datasets/2024-07-03-red-on-cyan/**/trajectory_im128.h5")

index = 0

for data_traj in loader:

    robodm.Trajectory.from_dict_of_lists(
        data_traj, path=f"/tmp/robodm/output_{index}.vla"
    )
    index += 1
    

# read the data back
for i in range(index):
    print(robodm.Trajectory(f"/tmp/robodm/output_{i}.vla")["action"].keys())