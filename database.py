import pandas as pd
import constants

from os import listdir
from os.path import join, basename, splitext, abspath
from typing import Dict, List
from gesture import Gesture
from pprint import pformat

import math

class Database:

    gestures: Dict[str, Gesture]

    def __init__(self, directory_name:str, filenames_ending_with=".csv"):
        self.gestures = self._generate_gestures(directory_name, filenames_ending_with)

    def get_gesture(self, gesture_file_name):
        return self.gestures[gesture_file_name]

    def get_gesture_count(self):
        return len(self.gestures)

    def applymap(self, f):  # This one is in-place
        for gesture_name,gesture in self.gestures.items():
            self.gestures[gesture_name] = gesture.applymap(f)

    # All private,utility methods go below

    @classmethod
    def _get_filename_without_extension(cls, filename:str) -> str:
        return splitext(basename(filename))[0]

    def _get_all_csv_file_paths(self, directory_name:str, endswith:str) -> List[str]:
        """Given a directory, return all the csv files in that directory, returned in a numeric sorted order. This
        assumes that all the csv files have names like '<number>.csv', or else an error will be thrown."""
        L = [abspath(join(directory_name, f)) for f in listdir(directory_name) if f.endswith(endswith)]
        # L.sort(key=lambda x: int(Database._get_filename_without_extension(x)))
        return L

    def _generate_gestures(self, directory_name:str, endswith) -> Dict[str,Gesture]:
        """Given a directory, returns a dict of gestures with the key as the filename (without extension) and the
        value is a Gesture."""
        gesture_files = self._get_all_csv_file_paths(directory_name, endswith)
        dfs = {}
        for f in gesture_files:
            gesture_name = Database._get_filename_without_extension(f)
            dfs[gesture_name] = Gesture(pd.read_csv(f, header=None), gesture_name)
        return dfs

    # The functions used for display and hashing

    def __str__(self) -> str:
        return pformat(self.gestures)

    def __repr__(self) -> str:
        return pformat(self.gestures)

    def __iter__(self):
        for x in self.gestures.values():
            yield x

# All testing code goes here

def test_printing():
    database = Database(constants.GESTURES_DIRECTORY_PATH)
    gesture = database.get_gesture("1")
    print("Database:", database)
    # pprint(gesture)
    print("Gestures in database:", database.get_gesture_count())
    print("SensorSeries:\n", gesture.get_sensor_series(1), sep='')
    print("\n")

def test_sensor_series_iterator():
    database = Database(constants.GESTURES_DIRECTORY_PATH)
    gesture1 = database.get_gesture("1")
    sensor_series0 = gesture1.get_sensor_series(1)
    # print(sensor_series0)
    print("max:", max(sensor_series0))
    print("Now iterating over the entires sensor series:")
    L = list(sensor_series0)
    print(L)
    print("length:", len(L))

def test_sensor_division():
    database = Database(constants.GESTURES_DIRECTORY_PATH)
    gesture1 = database.get_gesture("1")
    sensor_series1 = gesture1.get_sensor_series(1)
    divided_series = sensor_series1 / 2
    assert math.isclose(divided_series[0], -0.0070495), "Actual value is " + str(divided_series[0])

def test_sensor_series_contains():
    wordified_gesture = Gesture.get_gesture_from_wordified_file(constants.WORDIFIED_FILE_PATH, "1")
    wordified_gesture.get_sensor_series(1)

if __name__ == "__main__":
    # test_printing()
    # test_sensor_series_iterator()
    test_sensor_division()

