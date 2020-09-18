import os
from os.path import exists

from constants import GESTURES_DIRECTORY_PATH, OUTPUT_DIRECTORY, EXTRA_DIRECTORY, NORMALIZED_GESTURE_FILE_SUFFIX, \
    QUANTIZED_GESTURE_FILE_SUFFIX
from database import Database
from task1a import normalize_all_gestures
from task1b import quantize_all_gestures
from task1c import wordify_all_gestures

# Create all the necessary directories if they don't exist
for directory in (OUTPUT_DIRECTORY, EXTRA_DIRECTORY):
    if not exists(directory):
        os.mkdir(directory)

# Task 1a
raw_gesture_database = Database(GESTURES_DIRECTORY_PATH, filenames_ending_with=".csv")
normalize_all_gestures(raw_gesture_database)

# Task 1b
normalized_gesture_database = Database(EXTRA_DIRECTORY, filenames_ending_with=NORMALIZED_GESTURE_FILE_SUFFIX)
quantize_all_gestures(normalized_gesture_database)

# Task 1c
quantized_gesture_database = Database(EXTRA_DIRECTORY, filenames_ending_with=QUANTIZED_GESTURE_FILE_SUFFIX)
wordify_all_gestures(quantized_gesture_database)