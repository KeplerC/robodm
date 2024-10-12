from robodm.loader import VLALoader
import robodm
import os


loader = VLALoader("/tmp/robodm/vla/berkeley_autolab_ur5/*.vla")
for index, data_traj in enumerate(loader):

    print(data_traj.load())
    index += 1