# 🦊 Robo-DM 

🦊 Robo-DM : An Efficient and Scalable Data Collection and Management Framework For Robotics Learning. Support [Open-X-Embodiment](https://robotics-transformer-x.github.io/) ([Dataset Visualization](https://keplerc.github.io/openxvisualizer/)).

🦊 Robo-DM (Former Name: fog_x)  considers both speed 🚀 and storage efficiency.

## Install 

```bash
git clone https://github.com/KeplerC/robodm.git
cd robodm
pip install -e .
```

## Usage

```py
import robodm
import numpy as np

path = "/tmp/output.vla"

# create a new trajectory
traj = robodm.Trajectory(
    path = path, mode="w"
)

traj.add(feature = "arm_view", data = np.ones((4, 4)))

# Saves and compresses the trajectory
traj.close()

# load it 
print(robodm.Trajectory(
    path = path
).load())
# outputs 
# {'arm_view': array([[[1., 1., 1., 1.],
#       [1., 1., 1., 1.],
#       [1., 1., 1., 1.],
#       [1., 1., 1., 1.]]])}
```

## Examples

* [Data Collection and Loading](./examples/hello_world/data_collection_and_load.pydata_collection_and_load.py)
* Conversions From [Open_X](./examples/converters/openx_to_vla.py), [HDF5](./examples/converters/h5_loader.py)
* [Running Benchmarks](./examples/benchmarks/openx.py)

## Development
We are actively developing the framework, which may introduce breaking changes. Our active 
branches are in a separate [repo](https://github.com/BerkeleyAutomation/fog_x/pulls). 
Read the [CONTRIBUTING.md](CONTRIBUTING.md) file. 
