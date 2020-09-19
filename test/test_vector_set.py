import utils
import constants
from database import Database
from vector_set import VectorSet
from pprint import pprint
from word import Word

def print_a_vector_set():
    database = Database(constants.RESULTS_DIRECTORY_PATH, filenames_ending_with="_wordified.csv")
    database.applymap(Word.parse)
    print(database.get_gesture_count())
    gesture = database.get_gesture("1_wordified")
    print(gesture)
    vector_set = VectorSet.get_vector_set_representation_of_gesture(database, "1_wordified", method="tf")
    pprint(vector_set)

def print_ndarray_representation_of_a_vector_set():
    db = Database.from_wrd_files("D:\\Google Drive\\ASU\\CSE 515 Multimedia and Web Databases\\Project\\database")
    vector_set_1 = VectorSet.get_vector_set_representation_of_gesture(db, '1', method="tf")
    arr = vector_set_1.get_array(possible_words_list=utils.words_in_database(db))
    print(arr)

def write_vectors_txt():
    db = Database.from_wrd_files("D:\\Google Drive\\ASU\\CSE 515 Multimedia and Web Databases\\Project\\database")
    VectorSet.write_to_file(
        [VectorSet.get_vector_set_representation_of_gesture(db, gesture_name, method="tf") for gesture_name in
         sorted(db.gestures.keys())],
        utils.words_in_database(db),
        "D:\\Google Drive\\ASU\\CSE 515 Multimedia and Web Databases\\Project\\database\\vectors.txt"
    )

if __name__ == "__main__":
    # TODO: There is something wrong with my tf values. 0.26 everywhere when it should be 0.25.
    # print_a_vector_set()
    # print_ndarray_representation_of_a_vector_set()
    write_vectors_txt()