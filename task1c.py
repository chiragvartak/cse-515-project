import pandas as pd

from pprint import pprint
from word import Word

# def generate_word_string(number_list):
#     return "[" + ":".join(map(str,number_list)) + "]"

def extract_words_from_series(series, window_length, shift_length):
    w = window_length
    s = shift_length
    current_time = 0
    word_list = []
    while(current_time+w-1 <= len(series)-1):
        word_mini_series = series[current_time:current_time+w].tolist()
        word_list.append(Word(word_mini_series))
        current_time += s
    return pd.Series(word_list)

def wordify_gesture(df, window_length, shift_length):
    return df.apply(lambda series: extract_words_from_series(series, window_length, shift_length), axis=1)

def save_wordified_df(df, the_file_this_df_is_of, output_file_path):
    with open(output_file_path, 'w') as word_file:
        for series_index, series in df.iterrows():
            for time, word in series.items():
                word_file.write(the_file_this_df_is_of + "," + str(series_index) + "," + str(time) + "," + str(word) + "\n")

if __name__ == "__main__":
    FILE_NAME = "D:\\Google Drive\\ASU\\CSE 515 Multimedia and Web Databases\\Project\\results\\1_quantized.csv"
    OUTPUT_FILE_NAME = "D:\\Google Drive\\ASU\\CSE 515 Multimedia and Web Databases\\Project\\results\\1_wordified.csv"
    df = pd.read_csv(FILE_NAME, header=None)

    # word_series = extract_words_from_series(df.loc[1], 3, 1)
    # pprint(word_series)

    wordified_gesture = wordify_gesture(df, 3, 1)
    pprint(wordified_gesture)

    wordified_gesture.to_csv(OUTPUT_FILE_NAME, header=False, index=False)

    save_wordified_df(wordified_gesture, "1",
                      "D:\\Google Drive\\ASU\\CSE 515 Multimedia and Web Databases\\Project\\results\\1_word.csv")