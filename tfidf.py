import math
from database import Database
from word import Word
from sensor_series import SensorSeries

def tf(word: Word, sensor_series: SensorSeries):
    if not isinstance(sensor_series[0], Word):
        raise Exception("For finding the tf values, you should provide a SensorSeries of Word elements")
    word_count = 0
    for sensor_word in sensor_series:
        if word == sensor_word:
            word_count += 1
    return (word_count / len(sensor_series))

def idf(word:Word, sensor_index:int, database:Database):
    m = 0
    for gesture in database:
        if word in gesture.get_sensor_series(sensor_index):
            m += 1
    if m == 0:
        m = 1
    N = len(database.get_gesture_count())
    return math.log(N / m)

def combine_tf_idf(tf, idf):
    return tf * idf