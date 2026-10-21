## Instructor Guide (With Solutions)

## Task 1 — Create and Explore Arrays

Expected Solution:

```py
import numpy as np

sales = np.array([34, 28, 45, 51, 39, 48, 52])

print("Total:", sales.sum())
print("Average:", sales.mean())
print("Max:", sales.max())
print("Min:", sales.min())
```

Expected Output (Approx):

```sh
Total: 297
Average: 42.42857142857143
Max: 52
Min: 28
```

## Task 2 — Temperature Adjustment

Expected Solution:

```python
temps = np.array([18.5, 19.0, 20.2, 21.1, 19.8])

corrected = temps + 2

print(corrected)
```

Expected Output:

```sh
[20.5 21.  22.2 23.1 21.8]
```

## Task 3 — Sales Increase Simulation

Expected Solution:

```py
revenue = np.array([120, 135, 150, 160, 145])

new_revenue = np.round(revenue * 1.10, 2)

print("Old:", revenue)
print("New:", new_revenue)
```

Expected Output:

```sh
Old: [120 135 150 160 145]
New: [132.0  148.5 165.  176.  159.5]
```

## Task 4 — Find Busy Days

Expected Solution:

```py
customers = np.array([120, 85, 90, 140, 110, 75, 160])

busy_days = customers[customers > 100]

print(busy_days)
```

Expected Output

```sh
[120 140 110 160]
```

## Task 5 — Reshape Data

Expected Solution:

```py
data = np.array([12, 18, 25, 20, 15, 22, 30, 28, 10, 14, 19, 16])

matrix = data.reshape(3, 4)

daily_totals = matrix.sum(axis=1)

print(matrix)
print(daily_totals)
```

Expected Output
```sh
[[12 18 25 20]
 [15 22 30 28]
 [10 14 19 16]]
[75 95 59]
```

## Task 6 — Performance Comparison

Expected Solution:

```py
import time

numbers_list = list(range(1_000_000))
numbers_array = np.array(numbers_list)

start = time.time()
result = [x * 2 for x in numbers_list]
print("List time:", time.time() - start)

start = time.time()
result = numbers_array * 2
print("NumPy time:", time.time() - start)
```

Expected Output (approx):

```sh
List time: 0.04480695724487305
NumPy time: 0.014488697052001953
```

## Task 7 — Mini Data Analysis Challenge

Expected Solution:

```py
scores = np.array([55, 62, 48, 71, 69, 80, 77, 52, 60, 90])

mean = scores.mean()
median = np.median(scores)
std = scores.std()

above_mean = scores[scores > mean]

scores[scores < 50] = 50

print("Mean:", mean)
print("Median:", median)
print("Std:", std)
print("Above mean:", len(above_mean))
print("Adjusted scores:", scores)
```

Expected Output (Approx):

```sh
Mean: 66.4
Median: 65.5
Std: ~12.5
Above mean: 5
Adjusted scores: [55 62 50 71 69 80 77 52 60 90]
```