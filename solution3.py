import math


def create_indices_generator(index_size, batches, split_ratio):
    test_size = (index_size - 1) / (batches + (1 / split_ratio))
    start_data, start_test_data, end_test_data = 0, 0, 0

    for index_batch in range(batches):
        start_test_data = start_data + test_size * (1 / split_ratio)
        end_test_data = start_test_data + test_size
        yield list(map(math.floor, [start_data, start_test_data, end_test_data]))
        start_data += test_size


test_gen = create_indices_generator(100, 5, 0.25)

for indices in test_gen:
    print(indices)