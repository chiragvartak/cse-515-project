from word import Word
from sensor_series import SensorSeries
from database import Database
from typing import Dict
from tfidf import tf, idf, idf2, combine_tf_idf
from gesture import Gesture

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
        return SensorVector(
            {word:tf(word,wordified_series) for word in wordified_series},
            gesture_name,
            sensor_index
        )

    @classmethod
    def get_sensor_vector_by_tfidf(cls, gesture_name:str, sensor_index:int, database:Database):
        sensor_series = database.get_gesture(gesture_name).get_sensor_series(sensor_index)
        word_value_map = {}
        for word in sensor_series:
            tfidf = combine_tf_idf(tf(word, sensor_series), idf(word, sensor_index, database))
            word_value_map[word] = tfidf
        return SensorVector(word_value_map, gesture_name, sensor_index)

    @classmethod
    def get_sensor_vector_by_tfidf2(cls, gesture: Gesture, sensor_index: int):
        sensor_series = gesture.get_sensor_series(sensor_index)
        word_value_map = {}
        for word in sensor_series:
            tfidf2 = combine_tf_idf(tf(word, sensor_series), idf2(word, gesture))
            word_value_map[word] = tfidf2
        return SensorVector(word_value_map, gesture.gesture_name, sensor_index)

    def __str__(self) -> str:
        return str({k:round(v,3) for k,v in self.vector.items()})

    def __repr__(self) -> str:
        return repr({k:round(v,3) for k,v in self.vector.items()})

    def __getitem__(self, word:Word):
        return self.vector[word]

    def __contains__(self, word:Word):
        return word in self.vector