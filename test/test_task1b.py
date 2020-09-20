from task1b import *

res = 3
mu = 0.0
sigma = 0.25

if __name__ == "__main__":
    gbl = compute_gaussian_band_lengths(res, mu, sigma)
    print(gbl)
    print(sum([y for x,y in gbl]))
    print(compute_gaussian_offsets(gbl))