MU = 0.0
SIGMA = 0.25

def task1(directory_path, window_length, shift_length, resolution):
    band_lengths = compute_band_lengths(resolution, MU, SIGMA)
    for file in directory_path:
        normalized_data = normalize_data(f)
        quantized_data = quantize_data(normalized_data, band_lengths)
        pattern_vector_data = compute_pattern_vectors(quantized_data, window_length, shift_length)
        store_pattern_vectors(file_identifier, output_file_path)

