from os import listdir
from os.path import join, basename, splitext, abspath
from pprint import pformat
from typing import Dict, List

import numpy as np
import pandas as pd

from gesture import Gesture
from word import Word


class Database:
    gestures: Dict[str, Gesture]

    def __init__(self, directory_name: str, filenames_ending_with=".csv", name_gesture_dict=None):
        if name_gesture_dict is None:  # Initiazing the database using a dir name and filename ending
            self.gestures = self._generate_gestures(directory_name, filenames_ending_with)
        else:  # Initializing the database directly with the name vs gesture dict provided
            self.gestures = name_gesture_dict

    def get_gesture(self, gesture_file_name):
        return self.gestures[gesture_file_name]

    def get_gesture_count(self):
        return len(self.gestures)

    def applymap(self, f):  # This one is in-place
        for gesture_name, gesture in self.gestures.items():
            self.gestures[gesture_name] = gesture.applymap(f)

    @classmethod
    def from_wrd_files(cls, wrd_files_directory):
        wrd_file_paths = [abspath(join(wrd_files_directory, f))
                          for f in listdir(wrd_files_directory)
                          if f.endswith(".wrd")]
        name_gesture_dict = {}
        for wrd_file_path in wrd_file_paths:
            wrd_file_df = pd.read_csv(wrd_file_path, header=None)
            nsensors = len(wrd_file_df[1].unique())
            dimensions = (nsensors, len(wrd_file_df[1]) // nsensors)
            wordified_df = pd.DataFrame(np.array(wrd_file_df[3]).reshape(dimensions))
            wordified_df = wordified_df.applymap(Word.parse)
            filename_without_extension = splitext(basename(wrd_file_path))[0]
            name_gesture_dict[filename_without_extension] = Gesture(wordified_df, filename_without_extension)
        return Database("Dummy", name_gesture_dict=name_gesture_dict)

    # All private,utility methods go below

    @classmethod
    def _get_filename_without_extension(cls, filename: str) -> str:
        return splitext(basename(filename))[0]

    def _get_all_csv_file_paths(self, directory_name: str, endswith: str) -> List[str]:
        """Given a directory, return all the csv files in that directory, returned in a numeric sorted order. This
        assumes that all the csv files have names like '<number>.csv', or else an error will be thrown."""
        L = [abspath(join(directory_name, f)) for f in listdir(directory_name) if f.endswith(endswith)]
        # L.sort(key=lambda x: int(Database._get_filename_without_extension(x)))
        return L

    def _generate_gestures(self, directory_name: str, endswith) -> Dict[str, Gesture]:
        """Given a directory, returns a dict of gestures with the key as the filename (without extension) and the
        value is a Gesture."""
        gesture_files = self._get_all_csv_file_paths(directory_name, endswith)
        dfs = {}
        for f in gesture_files:
            gesture_name = Database._get_filename_without_extension(f)
            dfs[gesture_name] = Gesture(pd.read_csv(f, header=None), gesture_name)
        return dfs

    # The functions used for display and hashing

    def __str__(self) -> str:
        return pformat(self.gestures)

    def __repr__(self) -> str:
        return pformat(self.gestures)

    def __iter__(self):
        for x in self.gestures.values():
            yield x
