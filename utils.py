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