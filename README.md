# Rayne

A micro benchmarking utility for Python

[![Static Analysis](https://github.com/brobeson/Rayne/actions/workflows/code_quality.yaml/badge.svg)](https://github.com/brobeson/Rayne/actions/workflows/code_quality.yaml)
[![Coverage Status](https://coveralls.io/repos/github/brobeson/Rayne/badge.svg?branch=main)](https://coveralls.io/github/brobeson/Rayne?branch=main)

## Using PBench

First, import `pbench`

```python
from pbench import Benchmark
```

PBench uses a context manager to run a micro benchmark.
In the context manager, set the benchmark `subject` to the function you want to benchmark.
When the context manager exits, it runs the benchmarks.

```python
>>> def fibonacci():
...     # Calculate Fibonacci of 5.
...
>>> with Benchmark() as benchmark:
...    benchmark.subject = fibonacci
...
>>> benchmark.mean
0.00345245963
>>> benchmark.standard_deviation
0.00050298475
```

By default, PBench runs the subject 1000 times.
You can change this with the `runs` argument to `Benchmark()`:

```python
>>> def fibonacci():
...     # Calculate Fibonacci of 5.
...
>>> with Benchmark(runs=2000) as benchmark:
...     benchmark.subject = fibonacci
...
>>> benchmark.mean
0.00345245963
>>> benchmark.standard_deviation
0.00050298475
```
