import numpy as np
import timeit
import statistics


def benchmark(n):
    data = list(range(n))
    arr = np.array(data, dtype=np.int64)

    def python_loop():
        result = []
        for x in data:
            result.append(x * 2)
        return result

    def numpy_operation():
        return arr * 2

    assert python_loop() == numpy_operation().tolist()

    py_time = statistics.median(
        timeit.repeat(python_loop, repeat=7, number=10)
    ) / 10

    np_time = statistics.median(
        timeit.repeat(numpy_operation, repeat=7, number=10)
    ) / 10

    print(f"Array size: {n}")
    print(f"Python: {py_time * 1000:.6f} ms")
    print(f"NumPy: {np_time * 1000:.6f} ms")
    print(f"Speedup: {py_time / np_time:.2f}x")
    print()


if __name__ == "__main__":
    for n in [1000, 100000, 1000000]:
        benchmark(n)