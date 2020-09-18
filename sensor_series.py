from pandas import Series

class SensorSeries:
    _series: Series  # Raw data stored for doing hacky things - try your best not to use this
    gesture_name: str
    sensor_index: int

    def __init__(self, series:Series, gesture_name:str, sensor_index:int):
        self._series = series
        self.gesture_name = gesture_name
        self.sensor_index = sensor_index

    def __contains__(self, item):
        return item in self._series

    def __getitem__(self, key:int):
        return self._series[key]

    def __iter__(self):
        for x in self._series:
            yield x

    def __truediv__(self, other):
        return SensorSeries(self._series / other, self.gesture_name, self.sensor_index)

    def __str__(self) -> str:
        return str(self._series)

    def __repr__(self) -> str:
        return repr(self._series)

    def __len__(self):
        return len(self._series)