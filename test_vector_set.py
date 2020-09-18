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

if __name__ == "__main__":
    # TODO: There is something wrong with my tf values. 0.26 everywhere when it should be 0.25.
    print_a_vector_set()