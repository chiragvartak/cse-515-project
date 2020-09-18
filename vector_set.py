from database import Database
from typing import Dict
from sensor_vector import SensorVector
from gesture import Gesture
from pprint import pformat

class VectorSet:
    vector_set: Dict[int, SensorVector]
    gesture_name: str

    def __init__(self, sindex_svector_mapping:Dict[int, SensorVector], gesture_name:str):
        self.vector_set = sindex_svector_mapping
        self.gesture_name = gesture_name

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

    def __str__(self):
        return "VectorSet" + pformat(self.vector_set)

    def __repr__(self):
        return "VectorSet" + pformat(self.vector_set)

    def __len__(self):
        return len(self.vector_set)

    def __getitem__(self, sensor_id:int):
        return self.vector_set[sensor_id]