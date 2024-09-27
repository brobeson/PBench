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
def fibonacci(n: int) -> int:
    # Calculate Fibonacci of 5.

with Benchmark() as benchmark:
    benchmark.set_user_code(fibonacci, n=5)
```

By default, PBench runs the subject 1000 times.
You can change this with the `runs` argument to `Benchmark()`:

```python
def fibonacci():
    # Calculate Fibonacci of 5.

with Benchmark(runs=2000) as benchmark:
    benchmark.set_user_code(fibonacci, n=5)
```

## Reference

### `Benchmark.__init__()`

Initialize a `Benchmark` context manager.

#### Arguments

- `runs`  
  **Type:** `int`  
  **Default:** 1000  
  **Description:** Run the user code this many times.
  Multiple runs creates a statistical distribution of run times to account for variables outside the user's control.
- `name`  
  **Type:** `str`  
  **Default:** `None`  
  **Description:** A name for the benchmark.
  If this is `None` or an empty string, the benchmark takes the name from the user function.

### `Benchmark.set_user_code(function: Callable, **kwargs)`

Set the user code to benchmark.

#### Arguments

- **function**  
  **type:** Any callable object  
  **description:** The benchmark context manager measures the run time of this function.
- **kwargs**  
  **type:** Keyword arguments  
  **description:** The benchmark passes these arguments to `function`.
