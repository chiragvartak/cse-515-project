import numpy as np
from database import Database
from utils import words_in_database
from heatmap import Heatmap
from sensor_vector import SensorVector
from vector_set import VectorSet

def euclidean_distance_between_vector_sets(database:Database, vs1:VectorSet, vs2:VectorSet) -> float:
    occurring_words_in_database = words_in_database(database)
    heatmap1 = Heatmap(vs1, occurring_words_in_database)
    heatmap2 = Heatmap(vs2, occurring_words_in_database)
    return np.linalg.norm(heatmap1.ndarray - heatmap2.ndarray)

if __name__ == "__main__":
    raise NotImplementedError