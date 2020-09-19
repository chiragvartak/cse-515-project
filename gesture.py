import numpy as np
import pandas as pd

from pandas import DataFrame
from typing import List
from sensor_series import SensorSeries
from word import Word

class Gesture:
    _dataframe: pd.DataFrame  # Raw data stored for doing hacky things - try your best not to use this
    sensor_series_list: List[SensorSeries]
    gesture_name: str
    ndarray: np.ndarray  # Will not be computed when the object is initialized

    def __init__(self, dataframe:DataFrame, gesture_name:str):
        self._dataframe = dataframe
        self.sensor_series_list = [SensorSeries(series,gesture_name,sensor_index) for
                                   (sensor_index,series) in dataframe.iterrows()]
        self.gesture_name = gesture_name

    def get_sensor_series(self, sensor_index:int) -> SensorSeries:
        return self.sensor_series_list[sensor_index]

    def get_shape(self):
        return self._dataframe.shape

    def get_rows(self):
        return self.get_shape()[0]

    def applymap(self, f):
        return Gesture(self._dataframe.applymap(f), self.gesture_name)

    # Utility functions go below

    @classmethod
    def get_gesture_from_wordified_file(cls, wordified_file_path:str, gesture_name:str):
        raw_df = pd.read_csv(wordified_file_path)
        wordified_df = raw_df.applymap(Word.parse)
        return Gesture(wordified_df, gesture_name)

    # The functions used for display and hashing

    def __repr__(self):
        return repr(self._dataframe)

    def __str__(self):
        return str(self._dataframe)

    def __iter__(self):
        for x in self.sensor_series_list:
            yield x