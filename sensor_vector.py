from word import Word
from sensor_series import SensorSeries
from database import Database
from typing import Dict
import math

class SensorVector:
    vector: Dict[Word, float]
    gesture_name:str
    sensor_index:int

    def __init__(self, word_value_map:Dict[Word,float], gesture_name:str, sensor_index:int):
        self.vector = word_value_map
        self.gesture_name = gesture_name
        self.sensor_index = sensor_index

    @classmethod
    def get_sensor_vector_by_tf(cls, wordified_series: SensorSeries, gesture_name:str, sensor_index:int):
        word_count = {}
        K = len(wordified_series)
        for word in wordified_series:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        word_value_map = {key: (value / K) for key, value in word_count.items()}
        return SensorVector(word_value_map, gesture_name, sensor_index)

    @classmethod
    def _tf(cls, word:Word, sensor_series:SensorSeries):
        word_count = 0
        for sensor_word in sensor_series:
            if word == sensor_word:
                word_count += 1
        return (word_count / len(sensor_series))

    @classmethod
    def _idf(cls, word:Word, sensor_index:int, database:Database):
        m = 0
        for gesture in database:
            if word in gesture.get_sensor_series(sensor_index):
                m += 1
        N = len(database.get_gesture_count())
        return math.log(N / m)

    @classmethod
    def _combine_tf_idf(cls, tf, idf):
        # TODO: Make this formula better
        return tf * idf

    @classmethod
    def get_sensor_vector_by_tfidf(cls, gesture_name:str, sensor_index:int, database:Database):
        sensor_series = database.get_gesture(gesture_name).get_sensor_series(sensor_index)
        word_value_map = {}
        for word in sensor_series:
            tfidf = SensorVector._combine_tf_idf(
                SensorVector._tf(word, sensor_series),
                SensorVector._idf(word, sensor_index, database)
            )
            word_value_map[word] = tfidf
        return SensorVector(word_value_map, gesture_name, sensor_index)

    def __str__(self) -> str:
        return str({k:round(v,3) for k,v in self.vector.items()})

    def __repr__(self) -> str:
        return repr({k:round(v,3) for k,v in self.vector.items()})

    def __getitem__(self, word:Word):
        return self.vector[word]

    def __contains__(self, word:Word):
        return word in self.vector