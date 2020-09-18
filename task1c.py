from os.path import join

import pandas as pd

from constants import WINDOW_LENGTH, SHIFT_LENGTH, WORDIFIED_GESTURE_FILE_SUFFIX, \
    EXTRA_DIRECTORY, OUTPUT_DIRECTORY, WRD_FILE_SUFFIX
from database import Database
from word import Word


def extract_words_from_series(series, window_length, shift_length):
    w = window_length
    s = shift_length
    current_time = 0
    word_list = []
    while (current_time + w - 1 <= len(series) - 1):
        word_mini_series = series[current_time:current_time + w].tolist()
        word_list.append(Word(word_mini_series))
        current_time += s
    return pd.Series(word_list)


def wordify_gesture(df, window_length, shift_length):
    return df.apply(lambda series: extract_words_from_series(series, window_length, shift_length), axis=1)


def save_wordified_df(df, the_file_this_df_is_of, output_file_path):
    with open(output_file_path, 'w') as word_file:
        for series_index, series in df.iterrows():
            for time, word in series.items():
                word_file.write(
                    the_file_this_df_is_of + "," + str(series_index) + "," + str(time) + "," + str(word) + "\n")


def wordify_all_gestures(quantized_gesture_database: Database):
    for quantized_gesture in quantized_gesture_database:
        wordified_df = wordify_gesture(quantized_gesture._dataframe, WINDOW_LENGTH, SHIFT_LENGTH)
        wordified_df.to_csv(
            join(EXTRA_DIRECTORY, quantized_gesture.gesture_name + WORDIFIED_GESTURE_FILE_SUFFIX),
            header=False, index=False
        )
        the_file_this_df_is_of = quantized_gesture.gesture_name.split("_")[0]
        save_wordified_df(wordified_df, the_file_this_df_is_of,
                          join(OUTPUT_DIRECTORY, the_file_this_df_is_of + WRD_FILE_SUFFIX))
