# parabar

Progress bars from `tqdm` for multiprocessing with `pathos` in Python.

This is similar in spirit to `tqdm_pathos` but more simplified.

## Installation

`pip install parabar`

## Usage

There is a single function `parabar.map`.

The two required arguments are the function you want to map and the iterable(s) you want to map over: `parabar.map(func, iterable)`.

If you want to iterate over multiple arguments, you should zip them: `parabar.map(func, zip(iterable1, iterable2))`.

It has two optional arguments:
- `ncpus = 1`: the number of processes for the pool
- `tqdm_kwargs = {}`: dictionary of extra arguments to pass to `tqdm`.

If the length of your iterable is `total`, you can tell `tqdm` by using `tqdm_kargs = {'total': total}`. Otherwise, `parabar.map` will convert your iterables to a list and use `len`.

You can provide other fixed positional and keywords arguments to your function that you do not want to iterate over as the reminaing position and keyword arguments: `parabar.map(func, iterable, arg1, arg2, kwarg1=None, ncpus=1)`.

## Examples

### Function of a single iterable:

```
f = lambda x: x**2
iterable = [1, 2, 3]

# Serial
y = [f(x) for x in iterable]
print(y)

# Parallel
y = parabar.map(f, iterable)
print(y)
```

### Function of a single iterable, with non-iterable args and kwargs:

```
f = lambda x, a, b = 0: x**2 * a + b
iterable = [1, 2, 3]
a = 1
b = 0

# Serial
y = [f(x, a, b = b) for x in iterable]
print(y)

# Parallel
y = parabar.map(f, iterable, a, b = b)
print(y)
```

### Function of multiple iterables:

```
f = lambda x, y: x * y
iterable1 = [1, 2, 3]
iterable2 = [4, 5, 6]

# Serial
z = [f(x, y) for x, y in zip(iterable1, iterable2)]
print(z)

# Parallel
z = parabar.map(f, zip(iterable1, iterable2))
print(z)
```

### Function of multiple iterables, with non-iterable args and kwargs

```
f = lambda x, y, a, b = 0: x * y * a + b
iterable1 = [1, 2, 3]
iterable2 = [4, 5, 6]
a = 1
b = 0

# Serial
z = [f(x, y, a, b = b) for x, y in zip(iterable1, iterable2)]
print(z)

# Parallel
z = parabar.map(f, zip(iterable1, iterable2), a, b = b)
print(z)
```

### Specify number of processes and keyword arguments for progress bar

```
from tqdm.auto import tqdm

f = lambda x: x
iterable = [1, 2, 3]
tqdm_kwargs = dict(total = 3, desc = 'iterating')

# Serial
y = [f(x) for x in tqdm(iterable, **tqdm_kwargs)]
print(y)

# Parallel
y = parabar.map(f, iterable, ncpus=2, tqdm_kwargs=tqdm_kwargs)
print(y)
```
