import pandas as pd

from os.path import join

from database import Database
from gesture import Gesture
from sensor_series import SensorSeries

from pandas import DataFrame

from typing import List
import constants

import math
from pprint import pprint

from utils import floating_point_equals

### Task 1(a): Normalization ###
# Tested
def absolute_max(sensor_series_list:List[SensorSeries]) -> float:
    absolute_max = -1.0
    for sensor_series in sensor_series_list:
        absolute_max_in_series = abs(max(sensor_series, key=abs))
        if absolute_max_in_series > absolute_max:
            absolute_max = absolute_max_in_series
    return absolute_max

### Task 1(a): Normalization ###
# Eh, too damn simple, but I'm gonna let the function be and use it
# Tested
def normalize_series(database:Database, gesture_name:str, sensor_index:int) -> SensorSeries:
    gesture = database.get_gesture(gesture_name)
    abs_max = absolute_max([gesture.get_sensor_series(sensor_index) for gesture in database])
    print("Absolute max for sensor series", sensor_index, "is", abs_max)
    return gesture.get_sensor_series(sensor_index) / abs_max

def normalize_gesture(database:Database, gesture_name:str) -> Gesture:
    gesture = database.get_gesture(gesture_name)
    r, _ = gesture.get_shape()
    result_sensor_series_list = [normalize_series(database, gesture_name, sensor_index) for sensor_index in range(r)]
    return Gesture(DataFrame(result_sensor_series_list), gesture_name)

def write_to_file(gesture:Gesture, output_file_path:str):
    gesture._dataframe.to_csv(output_file_path, header=False, index=False)

# All the testing code goes below

def test():
    database = Database(constants.GESTURES_DIRECTORY_PATH)
    normalized_gesture = normalize_gesture(database, "1")
    print(normalized_gesture)
    write_to_file(normalized_gesture, join(constants.RESULTS_DIRECTORY_PATH, '1_normalized.csv'))

def test_absolute_max():
    SENSOR = 1
    database = Database(constants.GESTURES_DIRECTORY_PATH)
    abs_max = absolute_max(
        [database.get_gesture("1").get_sensor_series(SENSOR),
         database.get_gesture("2").get_sensor_series(SENSOR),
         database.get_gesture("3").get_sensor_series(SENSOR)
         ])
    print("abs_max:", abs_max)
    assert math.isclose(abs_max, 0.024239), "Actual value is " + str(abs_max)

def test_normalize_series():
    GESTURE_NAME = "1"
    SENSOR = 1
    database = Database(constants.GESTURES_DIRECTORY_PATH)
    normalized_series = normalize_series(database, GESTURE_NAME, SENSOR)
    pprint(normalized_series)
    assert math.isclose(normalized_series[0], -0.5816659103098313), "Actual value is " + str(normalized_series[0])

if __name__ == "__main__":
    test()
    # test_absolute_max()
    # test_normalize_series()