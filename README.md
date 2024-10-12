# 🦊 Robo-DM 

🦊 Robo-DM : An Efficient and Scalable Data Collection and Management Framework For Robotics Learning. Support [Open-X-Embodiment](https://robotics-transformer-x.github.io/) ([Dataset Visualization](https://keplerc.github.io/openxvisualizer/)).

🦊 Robo-DM (Former Name: fog_x)  considers both speed 🚀 and storage efficiency.

## Install 

```bash
git clone https://github.com/KeplerC/robodm.git
cd fog_x
pip install -e .
```

## Usage

```py
import fog_x

path = "/tmp/output.vla"

# 🦊 Data collection: 
# create a new trajectory
traj = fog_x.Trajectory(
    path = path
)

traj.add(feature = "arm_view", value = "image1.jpg")

# Saves and compresses the trajectory
traj.close()

# load it 
fog_x.Trajectory(
    path = path
)
```

## Examples

* [Data Collection and Loading](./examples/data_collection_and_load.py)
* [Convert From Open_X](./examples/openx_loader.py)
* [Convert From H5](./examples/h5_loader.py)
* [Running Benchmarks](./benchmarks/openx.py)

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file. 
