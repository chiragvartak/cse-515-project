import os
from os.path import exists
from constants import GESTURES_DIRECTORY_PATH, OUTPUT_DIRECTORY, EXTRA_DIRECTORY
from database import Database
from task1a import normalize_all_gestures

# Create all the necessary directories if they don't exist
for directory in (OUTPUT_DIRECTORY, EXTRA_DIRECTORY):
    if not exists(directory):
        os.mkdir(directory)

raw_gesture_database = Database(GESTURES_DIRECTORY_PATH, filenames_ending_with=".csv")
normalize_all_gestures(raw_gesture_database)