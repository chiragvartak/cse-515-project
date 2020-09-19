import utils
import math

import constants
from database import Database
from gesture import Gesture


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

def test_from_wrd_files():
    wrd_files_db = Database.from_wrd_files("D:\\Google Drive\\ASU\\CSE 515 Multimedia and Web Databases\\Project\\database")
    print(wrd_files_db)

def test_compute_ndarrays_for_gestures():
    wrd_files_db = Database.from_wrd_files(
        "D:\\Google Drive\\ASU\\CSE 515 Multimedia and Web Databases\\Project\\database")
    wrd_files_db.compute_ndarrays_for_gestures("tf", utils.words_in_database(wrd_files_db))

if __name__ == "__main__":
    # test_printing()
    # test_sensor_series_iterator()
    # test_sensor_division()
    # test_from_wrd_files()
    test_compute_ndarrays_for_gestures()
