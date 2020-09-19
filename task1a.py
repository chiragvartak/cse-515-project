from os.path import join
from constants import NORMALIZED_GESTURE_FILE_SUFFIX
from typing import List

from pandas import DataFrame

from database import Database
from gesture import Gesture
from sensor_series import SensorSeries


def absolute_max(sensor_series_list: List[SensorSeries]) -> float:
    abs_max = -1.0
    for sensor_series in sensor_series_list:
        absolute_max_in_series = abs(max(sensor_series, key=abs))
        if absolute_max_in_series > abs_max:
            abs_max = absolute_max_in_series
    return abs_max


def normalize_series(database: Database, gesture_name: str, sensor_index: int) -> SensorSeries:
    gesture = database.get_gesture(gesture_name)
    abs_max = absolute_max([gesture.get_sensor_series(sensor_index) for gesture in database])
    return gesture.get_sensor_series(sensor_index) / abs_max


def normalize_gesture(database: Database, gesture_name: str) -> Gesture:
    gesture = database.get_gesture(gesture_name)
    r, _ = gesture.get_shape()
    result_sensor_series_list = [normalize_series(database, gesture_name, sensor_index) for sensor_index in range(r)]
    return Gesture(DataFrame(result_sensor_series_list), gesture_name)


def write_to_file(gesture: Gesture, output_file_path: str):
    gesture._dataframe.to_csv(output_file_path, header=False, index=False)


def normalize_all_gestures(database:Database, extra_directory):
    for gesture in database:
        normalized_gesture = normalize_gesture(database, gesture.gesture_name)
        output_file_path = join(extra_directory, normalized_gesture.gesture_name + NORMALIZED_GESTURE_FILE_SUFFIX)
        write_to_file(normalized_gesture, output_file_path)