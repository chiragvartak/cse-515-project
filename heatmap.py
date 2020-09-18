import utils
from sensor_series import SensorSeries
from vector_set import VectorSet
import numpy as np
from typing import Tuple, List
from word import Word
import seaborn as sns
import matplotlib.pyplot as plt

class Heatmap:
    ndarray: np.ndarray
    _number_of_sensors: int
    _number_of_words: int
    _shape: Tuple[int,int]

    def __init__(self, vector_set:VectorSet, possible_words_list:List[Word]):
        self._number_of_sensors = len(vector_set)
        self._number_of_words = len(possible_words_list)
        self._shape = (self._number_of_sensors, self._number_of_words)
        M = []
        for sensor_id in sorted(vector_set.vector_set.keys()):
            sensor_vector = vector_set[sensor_id]
            L = []
            for word in possible_words_list:
                L.append(sensor_vector[word] if (word in sensor_vector) else 0.0)
            M.append(tuple(L))
        self.ndarray = np.array(M)

    def plot_heatmap(self):
        sns.heatmap(self.ndarray, square=True)
        plt.savefig("heatmap.png")
        plt.show()

    def plot_gray_heatmap(self):
        cmap = sns.cubehelix_palette(50, hue=0.05, rot=0, light=0.9, dark=0, as_cmap=True)
        sns.heatmap(self.ndarray, cmap=cmap, square=True, cbar=False)
        plt.savefig("heatmap.png")
        plt.show()

    def __str__(self):
        return str(self.ndarray)

    def __repr__(self):
        return str(self.ndarray)