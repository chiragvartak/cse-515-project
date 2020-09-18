from heatmap import Heatmap
import constants
from database import Database
from vector_set import VectorSet
from pprint import pprint
from word import Word
import seaborn as sns
import matplotlib.pyplot as plt
import utils

def print_heatmap():
    database = Database(constants.RESULTS_DIRECTORY_PATH, filenames_ending_with="_wordified.csv")
    database.applymap(Word.parse)
    vector_set = VectorSet.get_vector_set_representation_of_gesture(database, "1_wordified", method="tf")
    pprint(vector_set)
    heatmap = Heatmap(vector_set, Word.all_possible_words_list(resolution=3, window_length=3))
    print(heatmap)

def test_plot_heatmap():
    database = Database(constants.RESULTS_DIRECTORY_PATH, filenames_ending_with="_wordified.csv")
    database.applymap(Word.parse)
    vector_set = VectorSet.get_vector_set_representation_of_gesture(database, "1_wordified", method="tf")
    # heatmap = Heatmap(vector_set, Word.all_possible_words_list(resolution=3, window_length=3))
    heatmap = Heatmap(vector_set, utils.words_in_database(database))
    heatmap.plot_heatmap()

def test_plot_gray_heatmap():
    database = Database(constants.RESULTS_DIRECTORY_PATH, filenames_ending_with="_wordified.csv")
    database.applymap(Word.parse)
    vector_set = VectorSet.get_vector_set_representation_of_gesture(database, "1_wordified", method="tf")
    # heatmap = Heatmap(vector_set, Word.all_possible_words_list(resolution=3, window_length=3))
    heatmap = Heatmap(vector_set, utils.words_in_database(database))
    heatmap.plot_gray_heatmap()

if __name__ == "__main__":
    # print_heatmap()
    # test_plot_heatmap()
    test_plot_gray_heatmap()