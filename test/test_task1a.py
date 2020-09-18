import constants
from database import Database
from task1a import normalize_series, normalize_gesture, absolute_max, write_to_file
from os.path import join
from pprint import pprint
import math

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