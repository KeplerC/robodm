import os

__root_dir__ = os.path.dirname(os.path.abspath(__file__))


# from robodm import dataset, episode, feature
# from robodm.dataset import Dataset
# from robodm import trajectory

from robodm.feature import FeatureType
from robodm.trajectory import Trajectory

all = ["trajectory"]

import logging

_FORMAT = "%(levelname).1s %(asctime)s %(filename)s:%(lineno)d] %(message)s"
logging.basicConfig(format=_FORMAT)
logging.root.setLevel(logging.INFO)
