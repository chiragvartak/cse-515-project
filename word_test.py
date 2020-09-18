from database import Database
import utils
import constants
from word import Word
from pprint import pprint

def test_possible_words_list():
    possible_words_list = Word.all_possible_words_list(resolution=3, window_length=3)
    pprint(possible_words_list)
    print("Total words:", len(possible_words_list))

def test_in_database():
    database = Database(constants.RESULTS_DIRECTORY_PATH, filenames_ending_with="_wordified.csv")
    database.applymap(Word.parse)
    words_in_database = utils.words_in_database(database)
    pprint(words_in_database)
    print("Total words:", len(words_in_database))

if __name__ == "__main__":
    # test_possible_words_list()
    test_in_database()