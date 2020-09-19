from sys import argv
import os
from os.path import abspath, join, exists
from typing import List, Tuple
from database import Database
from task1a import normalize_all_gestures
from task1b import quantize_all_gestures
from task1c import wordify_all_gestures
from constants import *

def parse_inputs(arguments:List) -> Tuple[str, int, int, int]:
    if len(arguments) != 5:
        raise Exception("Run the program as: python3 task1.py dir=<db-dir> w=3 s=2 r=3")
    database_directory = abspath(arguments[1][4:])
    window_length = int(arguments[2][2:])
    shift_length = int(arguments[3][2:])
    resolution = int(arguments[4][2:])
    return (database_directory, window_length, shift_length, resolution)

if __name__ == "__main__":
    DATABASE_DIRECTORY, WINDOW_LENGTH, SHIFT_LENGTH, RESOLUTION = parse_inputs(argv)
    EXTRA_DIRECTORY = join(DATABASE_DIRECTORY, "extra")
    if not exists(EXTRA_DIRECTORY):
        os.mkdir(EXTRA_DIRECTORY)

    # Task 1a
    raw_gesture_database = Database(DATABASE_DIRECTORY, filenames_ending_with=".csv")
    normalize_all_gestures(raw_gesture_database, extra_directory=EXTRA_DIRECTORY)

    # Task 1b
    normalized_gesture_database = Database(EXTRA_DIRECTORY, filenames_ending_with=NORMALIZED_GESTURE_FILE_SUFFIX)
    quantize_all_gestures(normalized_gesture_database, res=RESOLUTION, mu=MU, sigma=SIGMA,
                          extra_directory=EXTRA_DIRECTORY)

    # Task 1c
    quantized_gesture_database = Database(EXTRA_DIRECTORY, filenames_ending_with=QUANTIZED_GESTURE_FILE_SUFFIX)
    wordify_all_gestures(quantized_gesture_database, window_length=WINDOW_LENGTH, shift_length=SHIFT_LENGTH,
                         output_directory=DATABASE_DIRECTORY, extra_directory=EXTRA_DIRECTORY)