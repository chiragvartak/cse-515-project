import pandas as pd

from math import sqrt
from scipy.special import erf
from pprint import pprint
from os.path import join

# The sc.special.erf (error function) needs a minor modification to be converted to the Gaussian integral
# Source: https://stackoverflow.com/questions/509994/best-way-to-write-a-python-function-that-integrates-a-gaussian
def gaussian_integral(x, mu, sigma):
    return 0.5 * (1+ erf((x - mu) / (sigma * sqrt(2))))

def limited_gaussian_integral(x1, x2, mu, sigma):
    return gaussian_integral(x2, mu, sigma) - gaussian_integral(x1, mu, sigma)

def compute_gaussian_band_lengths(resolution, mu, sigma):
    r = resolution
    D = {}
    for i in range(1, resolution+1):
        lengthi = 2 * limited_gaussian_integral((i-r-1)/r, (i-r)/r, mu, sigma) / limited_gaussian_integral(-1, 1, mu, sigma)
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
        for integer,offset in gaussian_offsets.items():
            if abs(number) <= offset:
                return -integer
    elif number >= 0:
        for integer,offset in gaussian_offsets.items():
            if number <= offset:
                return integer
    else:
        raise Exception("This statement should not be reachable")

def quantify_df(df, gaussian_offsets):
    return df.applymap(lambda x: quantify_number(x,gaussian_offsets))

if __name__ == "__main__":
    band_lengths = compute_gaussian_band_lengths(3, 0.0, 0.25)
    pprint(band_lengths)
    print(sum(band_lengths.values()))
    gaussian_offsets = compute_gaussian_offsets(band_lengths)
    pprint(gaussian_offsets)
    print(quantify_number(0.999819598, gaussian_offsets))

    DIRECTORY_NAME = "D:\Google Drive\ASU\CSE 515 Multimedia and Web Databases\Project"
    TEST_FILE_NAME = "1"
    df = pd.read_csv("D:\\Google Drive\\ASU\\CSE 515 Multimedia and Web Databases\\Project\\results\\1_normalized.csv", header=None)
    gaussian_offsets = compute_gaussian_offsets(compute_gaussian_band_lengths(3, 0.0, 0.25))
    pprint(gaussian_offsets)
    quantized_df = quantify_df(df, gaussian_offsets)
    pprint(quantized_df)
    quantized_df.to_csv(join(DIRECTORY_NAME, 'results', TEST_FILE_NAME + '_quantized.csv'), header=False, index=False)