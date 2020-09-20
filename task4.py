import sys
from os.path import abspath

import numpy as np

import utils
from database import Database


def parse_inputs(arguments):
    if len(arguments) != 4:
        raise Exception("Run the program as: python3 task4.py dir=<wrd-files-dir> f=1.csv type=tf")
    wrd_files_directory = abspath(arguments[1][4:])
    gesture_name = arguments[2][2:].split('.')[0]
    type = arguments[3][5:]
    return (wrd_files_directory, gesture_name, type)


if __name__ == "__main__":
    WRD_FILES_DIRECTORY, GESTURE_NAME, TYPE = parse_inputs(sys.argv)

    # Initialize all the gesture vectors
    db = Database.from_wrd_files(WRD_FILES_DIRECTORY)
    db.compute_ndarrays_for_gestures(method=TYPE, possible_words_list=utils.words_in_database(db))

    # Compare the queried gesture with all other gestures in the database
    query_gesture = db.get_gesture(GESTURE_NAME)
    distances = []
    for gesture in db:
        distances.append((abs(np.linalg.norm(query_gesture.ndarray - gesture.ndarray)), gesture.gesture_name))
    distances.sort()
    print("The 10 most similar gestures to", GESTURE_NAME+".csv using", TYPE.upper(), "values are:")
    i = 1
    for distance, gesture_name in distances:
        if i > 11: break
        print(gesture_name + ".csv with distance", round(distance, 4))
        i += 1
