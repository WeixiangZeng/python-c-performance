# Python Libraries Implemented in C

## Introduction

This project explores how Python calls C functions and why
NumPy is faster than regular Python loops.

## Experiments

### Experiment 1: Calling C from Python

I wrote a simple addition function in C, compiled it into
a shared library, and called it from Python using ctypes.

### Experiment 2: Python vs. NumPy

I compared the time needed to multiply every element
by 2 using a Python loop and NumPy.

## Results

- 1,000 elements: Python 0.016889 ms, NumPy 0.000742 ms (22.76x).
- 100,000 elements: Python 2.332336 ms, NumPy 0.028871 ms (80.79x).
- 1,000,000 elements: Python 27.513321 ms, NumPy 0.414122 ms (66.44x).

NumPy was faster in all three tests.

## Key Discoveries

- Python can call compiled C functions using ctypes.
- NumPy reduces interpreter overhead by using compiled code.
- NumPy was faster in all three tests.
- A larger array does not always result in a higher speedup.

## How to Run

Experiment 1:

```bash
gcc -shared -fPIC add.c -o libadd.so
python3 call_c.py
```

Experiment 2:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy
python benchmark.py
```

## Presentation

[Presentation Slides](presentation.pdf)

## References

- [Python ctypes](https://docs.python.org/3/library/ctypes.html)
- [NumPy](https://numpy.org/doc/stable/)
