import os
from typing import Any, Dict, List, Optional, Text
from robodm.loader.vla import VLALoader, NonShuffleVLALoader
from robodm.utils import data_to_tf_schema
import numpy as np

class VLADataset:
    """
    1. figure out the path to the dataset
    2. shuffling / training management 
    """
    def __init__(self, 
                 path: Text,
                 split: Text, 
                 shuffle: bool = True,
                 format: Optional[Text] = None):
        """
        init method for Dataset class
        Args:
            paths Text: path-like to the dataset
                it can be a glob pattern or a directory
                if it starts with gs:// it will be treated as a google cloud storage path with rlds format 
                if it ends with .h5 it will be treated as a hdf5 file
                if it ends with .tfrecord it will be treated as a rlds file
                if it ends with .vla it will be treated as a vla file
            split (Text): split of the dataset
            format (Optional[Text]): format of the dataset. Auto-detected if None. Defaults to None.
                we assume that the format is the same for all files in the dataset
        """    
        self.path = path
        self.split = split
        self.format = format
        self.shuffle = shuffle
        if shuffle:
            self.loader = VLALoader(path, batch_size=1, return_type="tensor", split=split)
        else:
            self.loader = NonShuffleVLALoader(path, batch_size=1, return_type="tensor")
    
    def __iter__(self):
        return self

    def __next__(self):
        return self.loader.get_batch()[0]

    def __len__(self):
        raise NotImplementedError

    def __getitem__(self, index):
        raise NotImplementedError

    def get_tf_schema(self):
        data = self.loader.peek()
        return data_to_tf_schema(data)

    def get_loader(self):
        return self.loader
    
    def get_next_trajectory(self):
        if self.shuffle:
            return self.loader.peak(np.random.randint(0, len(self.loader))).load()
        else:
            return next(self.loader).load()