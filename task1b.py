from math import sqrt
from os.path import join

from scipy.special import erf

from constants import QUANTIZED_GESTURE_FILE_SUFFIX
from database import Database


# The sc.special.erf (error function) needs a minor modification to be converted to the Gaussian integral
# Source: https://stackoverflow.com/questions/509994/best-way-to-write-a-python-function-that-integrates-a-gaussian
def gaussian_integral(x, mu, sigma):
    return 0.5 * (1 + erf((x - mu) / (sigma * sqrt(2))))


def limited_gaussian_integral(x1, x2, mu, sigma):
    return gaussian_integral(x2, mu, sigma) - gaussian_integral(x1, mu, sigma)


def compute_gaussian_band_lengths(resolution, mu, sigma):
    r = resolution
    D = {}
    for i in range(1, resolution + 1):
        lengthi = 2 * limited_gaussian_integral((i - r - 1) / r, (i - r) / r, mu, sigma) / \
                  limited_gaussian_integral(-1, 1, mu, sigma)
        D[i] = lengthi
    return D


def compute_gaussian_offsets(gaussian_band_lengths):
    D = {}
    total_length_till_now = 0.0
    for length_index, length in gaussian_band_lengths.items():
        total_length_till_now = total_length_till_now + length
        D[length_index] = total_length_till_now
    return D


def quantify_number(number, gaussian_offsets):
    if number < 0:
        for integer, offset in gaussian_offsets.items():
            if abs(number) <= offset:
                return -integer
    elif number >= 0:
        for integer, offset in gaussian_offsets.items():
            if number <= offset:
                return integer
    else:
        raise Exception("This statement should not be reachable")


def quantize_df(df, gaussian_offsets):
    return df.applymap(lambda x: quantify_number(x, gaussian_offsets))


def quantize_all_gestures(normalized_gesture_database: Database, res, mu, sigma, extra_directory):
    gaussian_offsets = compute_gaussian_offsets(compute_gaussian_band_lengths(res, mu, sigma))
    for normalized_gesture in normalized_gesture_database:
        quantized_df = quantize_df(normalized_gesture._dataframe, gaussian_offsets)
        quantized_df.to_csv(
            join(extra_directory, normalized_gesture.gesture_name + QUANTIZED_GESTURE_FILE_SUFFIX),
            header=False, index=False
        )
