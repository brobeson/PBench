# Rayne

A micro benchmarking utility for Python

## A Simple Example

First, implement a benchmark for the function you want to measure.
For this example, we'll measure how long it takes to run a recursive implementation of the [Fibonacci sequence](): $F_n = F_{n-1} + F_{n-2}$

```python
# fibonacci_benchmark.py

from rayne import Benchmark

# This is the function we want to measure.
def fibonacci(n):
  if n < 2:
    return n
  return fibonacci(n-1) + fibonacci(n-2)


# Construct a Benchmark object, then benchmark a call to
# fibonacci(5).
benchmark = Benchmark()
benchmark(fibonacci, 5)
```

Run the benchmark with your Python interpreter.

```bash
python3 -m fibonacci_benchmark
```
