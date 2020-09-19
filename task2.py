import sys
from os.path import abspath, join

import utils
from database import Database
from vector_set import VectorSet


def parse_inputs(arguments):
    if len(arguments) != 2:
        raise Exception("Run the program as: python3 task2.py dir=<wrd-files-dir>")
    wrd_files_directory = abspath(arguments[1][4:])
    return wrd_files_directory


if __name__ == "__main__":
    # Parse the command line arguments
    WRD_FILES_DIRECTORY = parse_inputs(sys.argv)

    # Parse the .wrd files from the given directory, and load the data in the memory
    wrd_files_db = Database.from_wrd_files(WRD_FILES_DIRECTORY)

    # Generate the gesture vectors
    gesture_vectors_by_tf = []
    gesture_vectors_by_tfidf = []
    gesture_vectors_by_tfidf2 = []
    represent_gesture = VectorSet.get_vector_set_representation_of_gesture
    for gesture_name in sorted(wrd_files_db.gestures.keys()):
        wordified_gesture = wrd_files_db.get_gesture(gesture_name)
        gesture_vectors_by_tf.append(represent_gesture(wrd_files_db, gesture_name, method="tf"))
        # TODO: Make this TFIDF
        gesture_vectors_by_tfidf.append(represent_gesture(wrd_files_db, gesture_name, method="tf"))
        # TODO: Make this TFIDF2
        gesture_vectors_by_tfidf2.append(represent_gesture(wrd_files_db, gesture_name, method="tf"))

    # Print the vector representation of vectors to vectors.txt
    possible_words_list = utils.words_in_database(wrd_files_db)
    output_file_path = join(WRD_FILES_DIRECTORY, "vectors.txt")
    VectorSet.write_to_file(gesture_vectors_by_tf, possible_words_list, output_file_path, file_mode='w')
    VectorSet.write_to_file(gesture_vectors_by_tfidf, possible_words_list, output_file_path, file_mode='a+')
    VectorSet.write_to_file(gesture_vectors_by_tfidf2, possible_words_list, output_file_path, file_mode='a+')
