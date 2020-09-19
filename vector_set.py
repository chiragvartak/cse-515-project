from typing import List
import numpy as np
from database import Database
from typing import Dict, Tuple
from sensor_vector import SensorVector
from gesture import Gesture
from pprint import pformat
from word import Word

class VectorSet:
    vector_set: Dict[int, SensorVector]
    gesture_name: str
    shape: Tuple[int,int]

    def __init__(self, sindex_svector_mapping:Dict[int, SensorVector], gesture_name:str):
        self.vector_set = sindex_svector_mapping
        self.gesture_name = gesture_name

    def get_array(self, possible_words_list: List[Word]):
        number_of_sensors = len(self)
        number_of_words = len(possible_words_list)
        self.shape = (number_of_sensors, number_of_words)
        M = []
        for sensor_id in sorted(self.vector_set.keys()):
            sensor_vector = self[sensor_id]
            L = []
            for word in possible_words_list:
                L.append(sensor_vector[word] if (word in sensor_vector) else 0.0)
            M.append(tuple(L))
        return np.array(M)

    @classmethod
    def get_vector_set_representation_of_gesture(cls, database:Database, gesture_name:str, method="tf"):
        if method not in ("tf", "tfidf", "tfidf2"):
            raise Exception("Invalid method: " + method)
        gesture:Gesture = database.get_gesture(gesture_name)
        if method == "tf":
            H = {}
            for i in range(gesture.get_rows()):
                sensor_index = i
                sensor_series = gesture.get_sensor_series(i)
                sensor_vector = SensorVector.get_sensor_vector_by_tf(sensor_series, gesture_name, sensor_index)
                H[sensor_index] = sensor_vector
            return VectorSet(H, gesture_name)
        elif method == "tfidf":
            raise NotImplementedError
        elif method == "tfidf2":
            raise NotImplementedError
        else:
            raise Exception("Unreachable statement")

    @classmethod
    def write_to_file(cls, vector_sets:List, possible_words_list:List[Word], output_file_path:str, file_mode='w'):
        np.set_printoptions(threshold=np.inf, linewidth=np.inf)
        with open(output_file_path, file_mode) as output_file:
            for vector_set in vector_sets:
                ndarray = vector_set.get_array(possible_words_list)
                ndarray = np.vectorize(lambda x: round(x,4))(ndarray)
                output_file.write(str(vector_set.gesture_name) + ":\n")
                output_file.write(str(ndarray) + "\n\n")

    def __str__(self):
        return "VectorSet" + pformat(self.vector_set)

    def __repr__(self):
        return "VectorSet" + pformat(self.vector_set)

    def __len__(self):
        return len(self.vector_set)

    def __getitem__(self, sensor_id:int):
        return self.vector_set[sensor_id]