import sys
from os.path import abspath
from os.path import join

from pandas import DataFrame

import utils
from database import Database
from heatmap import HeatMap
from vector_set import VectorSet


def parse_inputs(arguments):
    if len(arguments) != 4:
        raise Exception("Run the program as: python3 task3.py dir=<wrd-files-dir> f=1.csv type=tf")
    wrd_files_directory = abspath(arguments[1][4:])
    gesture_name = arguments[2][2:].split('.')[0]
    value_type = arguments[3][5:]
    return (wrd_files_directory, gesture_name, value_type)


if __name__ == "__main__":
    WRD_FILES_DIRECTORY, GESTURE_NAME, TYPE = parse_inputs(sys.argv)

    db = Database.from_wrd_files(WRD_FILES_DIRECTORY)
    vector_set = VectorSet.get_vector_set_representation_of_gesture(db, GESTURE_NAME, method=TYPE)
    words_list = utils.words_in_database(db)
    df = DataFrame(
        data=vector_set.get_array(words_list),
        columns=words_list
    )
    hm = HeatMap(df, words_list)
    output_file_path = join(WRD_FILES_DIRECTORY, GESTURE_NAME + "-" + TYPE + ".png")
    hm.plot(
        output_file_path,
        title="Heatmap for " + GESTURE_NAME + ".csv using " + TYPE.upper() + " values"
    )
    print("Heatmap generated at", output_file_path)
