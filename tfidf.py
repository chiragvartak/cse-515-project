import math
from database import Database
from word import Word
from sensor_series import SensorSeries
from gesture import Gesture

TF_CACHE = {}
IDF_CACHE = {}
IDF2_CACHE = {}

def tf(word: Word, sensor_series: SensorSeries):
    if not isinstance(sensor_series[0], Word):
        raise Exception("For finding the tf values, you should provide a SensorSeries of Word elements")
    if (word.word, sensor_series.gesture_name, sensor_series.sensor_index) in TF_CACHE:
        return TF_CACHE[(word.word, sensor_series.gesture_name, sensor_series.sensor_index)]
    word_count = 0
    for sensor_word in sensor_series:
        if word == sensor_word:
            word_count += 1
    tf_value = (word_count / len(sensor_series))
    TF_CACHE[(word.word, sensor_series.gesture_name, sensor_series.sensor_index)] = tf_value
    return tf_value

def idf(word:Word, sensor_index:int, database:Database):
    if (word.word, sensor_index) in IDF_CACHE:
        return IDF_CACHE[(word.word, sensor_index)]
    m = 0
    for gesture in database:
        if word in gesture.get_sensor_series(sensor_index):
            m += 1
    if m == 0:
        m = 1
    N = database.get_gesture_count()
    idf_value = math.log(N / m)
    IDF_CACHE[(word.word, sensor_index)] = idf_value
    return idf_value

def idf2(word:Word, gesture:Gesture):
    if (word.word, gesture.gesture_name) in IDF2_CACHE:
        return IDF2_CACHE[(word.word, gesture.gesture_name)]
    m = 0
    for sensor_series in gesture:
        if word in sensor_series:
            m += 1
    if m == 0:
        m = 1
    N = gesture.get_rows()
    idf2_value = math.log(N / m)
    IDF2_CACHE[(word.word, gesture.gesture_name)] = idf2_value
    return idf2_value

def combine_tf_idf(tf, idf):
    return tf * idf