import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from database import Database
import constants
from word import Word
from pprint import pprint
from vector_set import VectorSet

if __name__ == "__main__":
    database = Database(constants.RESULTS_DIRECTORY_PATH, filenames_ending_with="_wordified.csv")
    database.applymap(Word.parse)
    gesture = database.get_gesture("1_wordified")
    vector_set = VectorSet.get_vector_set_representation_of_gesture(database, "1_wordified", method="tf")
    pprint(vector_set)