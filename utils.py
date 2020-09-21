from typing import List
from database import Database

def floating_point_equals(f1, f2):
    abs_max = max(abs(f1), abs(f2))
    abs_min = min(abs(f1), abs(f2))
    allowed_error = abs_max * 0.01
    return f1 * f2 >= 0.0 and abs_min >= (abs_max-allowed_error) and abs_min <= (abs_max+allowed_error)

def words_in_database(database:Database):
    occuring_words = set()
    for gesture in database:
        for sensor_series in gesture:
            for word in sensor_series:
                occuring_words.add(word)
    return sorted(list(occuring_words))

def sort_vector_sets_list(vs_list: List):
    Z = zip([vs.gesture_name for vs in vs_list], vs_list)
    numbers_list = []
    non_numbers_list = []
    for s in Z:
        if s[0].isdigit():
            numbers_list.append((int(s[0]),s[1]))
        else:
            non_numbers_list.append(s)
    return [vs for _,vs in sorted(numbers_list)] + [vs for _,vs in sorted(non_numbers_list)]