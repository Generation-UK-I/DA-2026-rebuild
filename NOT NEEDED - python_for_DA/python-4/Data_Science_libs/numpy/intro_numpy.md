# Introduction to NumPy

NumPy is the foundation of **data-science** in Python.

Whereas Python works with `lists`, NumPy introduces the `ndarray` (N-dimensional array), which are faster and more efficient for large datasets. Unlike Python lists, in an array each item must be of the same type (homogenous), such as integers or floats.

Some operations are handled differently or automatically by Numpy, for example you can add two arrays as if they were single values (a + b), and NumPy will automatically apply the operation to every element simultaneously; to do this in standard Python you might need to implement a loop. This is known as `vectorised` operation.

## Installing NumPy

>If you have deployed the `Anaconda/Jupyter` environment in `Docker` you may skip this step, numpy, pandas, and matplotlib are installed automatically via the requirements.txt file.

Numpy is not included in the Standard Python Library, but it can be installed using `pip`.

>**Optional**: Create a virtual environment with `python -m venv ./venv` then activate it with `.venv\Scripts\activate.ps1`

Install numpy by running `pip install numpy` in your terminal, then import it into your workspace just like any other module, however by convention we alias it as `np`:

```python
import numpy as np
```

## Homogenous Multi-dimensional Arrays

Luckily we don't use that long term often, we simply say `array`, or `ndarray`; however, these are the fundamental objects of Numpy.

>NOTE: The Standard Python Library also has `array` functionality, but these are different to `numpy` arrays. Compared to Python lists, Python arrays are homogenous, use less memory, and are faster for calculations; however, unlike `numpy arrays`, they can only contain a single dimension, and have less functionality.

### One Dimensional Arrays

Arrays are a little tricky at first, but once it clicks they're easy.

Here is a simply array: `[2, 1, 3]`, the values could be responses to a survey, or the number of pizzas 3 people ate last month. If these values were in a spreadsheet then they would be like the columns, and therefore the series of values represents a row.

This array is a single `axis`, and dimensions refers to the number of axis, so this is a one-dimensional (1-D) array, of length 3.

Below we create two 1-D arrays `a` & `b`, and print the sum of adding each pair of values together.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)
```

---
**SIDE NOTE**: We mentioned `vectorised` operation... to complete the above task using the Standard Python Libraries we would likely need to use some type of `for` loop:

```python
list_a = [1, 2, 3]
list_b = [10, 20, 30]
sum_list = []

for x in list_a:
    new_val = x + list_b[list_a.index(x)]
    sum_list.append(new_val)
    
print(sum_list)
```

You can see the benefit and efficiency of using Numpy.

>*There are more efficient ways to write the loop with the Standard Library, e.g. `result = [a[i] + b[i] for i in range(len(a))]`, other functions are also available which could achieve the same thing, but the point remains, that Numpy arrays are faster, easier, and provide greater functionality.*

---

### Two Dimensional Arrays

It gets a little trickier now - let's add a second dataset: `[4, 7, 5]`.

Our array now contains two rows, and for readability it is typically written like this:

```Python
my_array = [[2, 1, 3],
            [4, 4, 5]]
```

We still have the axis we already identified, which represents the length of a single row, and this is `axis-1`; however, we now have a second axis, `axis-0`, which is the number of rows, in this case there are 2. Looking at the example above, imagine axis-0 is a vertical scale, with two notches, our two rows, and a horizontal scale with three notches, our three columns.

[add image]

When we create an array it has a number of attributes, one example is `dtype` which, similar to Python objects, describes the data type of the elements in the array; we also have `ndim` (number of dimensions), `size`, a another called `shape`.

#### Shape

`Shape` describes the array's dimensions, our first one-dimensional array was: `[2, 1, 3]`; the shape attribute is stored as a tuple in the format (rows, columns) or (r, c), so for our first array it has 1 row and 3 columns, so a shape of `(1, 3)`.

What is the shape of our 2-D example: `[[2, 1, 3, 2],[6, 4, 4, 5]]`?

Answer: (2, 4) - Axis-0 has 2 rows, Axis-1 has 4 columns.

The shape can be displayed with the shape method`.

```py
my_array = [[2, 1, 3],
            [4, 4, 5]]

print(my_array.shape)
```

### Three Dimensional Arrays (To Infinity...) and Beyond...

We can continue to add dimensions to our arrays, but this is where getting your head around it can be difficult.

Here's an example of a 3D-array, but we'll come back to it later to make sense of all the brackets:

```py
my_array = np.array([[[12, 18, 25, 20],
                 [15, 22, 30, 28]],
                 [[10, 14, 19, 16],
                 [11, 21, 13, 14]]])

print(my_array[1,1,3])
```

A common analogy to understand multi-dimensions is to imagine storing papers in filing cabinets...

- 1D: A stack (column) of papers
  - Dimensions: (columns)
- 2D: A drawer with divided into sections (rows) to organise the papers
  - Dimensions: (columns, rows)
- 3D: Multiple drawers in a filing cabinet
  - Dimensions: (columns, rows, drawers)
- 4D: Multiple cabinets in a room
  - Dimensions: (columns, rows, drawers, cabinets)
- 5D: Multiple rooms in a building
  - Dimensions: (columns, rows, drawers, cabinets, rooms)
- 6D: Multiple buildings on a campus...
- 7D: Multiple campuses in a city...
- 8D: Multiple cities in a country...

It's important to remember that our data points are modelling something in the real-world, so what can we model with different dimensions?

|Number of Dimensions|Real-world analog|
|---|---|
|1|Streamed data points / Peak temperature each day / Ages of people|
|2|Location coordinates / Time-series data / Tabular data|
|3|Coordinates in 3D space (height, width, depth) / RGB values|
|4|Weather modelling (latitude, longitude, altitude, time) / Video Processing (height, width, colour, time)|
|5|Medical Imaging (height, weight, age, sex, BMI)|
|6|5D, 6D, and beyond are used in cutting edge science, and large complex data, such as particle physics and climate modelling|

## Working with Numpy Arrays

### Creating an Array

We've seen a few examples already, but just to take a step back, we can create arrays by using Numpy's `array()` function:

```python
import numpy as np

my_array = np.array([5, 2, 3, 6, 4])

print(my_array)
```

In this case we've created `my_array` by providing it with a Python list: `[5, 2, 3, 6, 4]`. We can also create an array from a Tuple: `my_array = np.array((5, 2, 3, 6, 4))`.

### Accessing the Array

As you can see above with the print statement, we can work with Numpy arrays similarly to how we work with Python lists, for arrays are also indexed:

```py
my_array = np.array([5, 2, 3, 6, 4])

print(my_array[2])
```

#### Accessing Multi-Dimensional Arrays

Accessing elements in multi-dimensional arrays is very similar, we simply provide the index number for each of the axes.

**Two Dimensions**:

```py
my_array = np.array([[5,2,3,6,4], [4,7,2,5,3]])

print('2nd element on 1st row: ', my_array[0, 1])
```

**Three Dimensions**:

As we start to add more dimensions the basic logic is the same, but the syntax gets hard to read as there can be an overwhelming number of brackets.

Review this example of a simple 3D array which we saw earlier:

```py
my_array = np.array([[[12, 18, 25, 20],
                 [15, 22, 30, 28]],
                 [[10, 14, 19, 16],
                 [11, 21, 13, 14]]])

print(my_array[1,1,3])
```

>Notice we need to provide 3x axis values to retrieve a single element

To understand the 3D-array above:

- First we have the standard parenthisis `()` for the `np.array` function, like we find with all Python functions that we call
- Next, think back of a simple 1D-array: `[2,1,3,4]`. When we create a 2D array it is simply 2x 1D arrays separated by a comma, and they're both contained within a new layer of square brackets, for example: `[[2,1,3,4],[3,2,5,2]]`
- When we move to 3D it's basically the same thing; we have two individual 2D arrays, separated by a comma, and then both are enclosed in a new layer of square brackets: `[[[2,1,3,4],[3,2,5,2]],[[3,4,1,2],[2,6,3,5]]]`.

Perhaps clearer with this diagram:

```sh
|-------------------------------------------|    <--- 3D array
 |------------------|   |------------------|     <--- 2D arrays
  |-------| |-------|   |-------| |-------|      <--- 1D arrays
[[[2,1,3,4],[3,2,5,2]],[[3,4,1,2],[2,6,3,5]]]
```

### Slicing an Array

Again, similar to Python, we can access a `slice` of an array:

```py
array_b = np.array([5,2,3,6,4])

print(array_b[1:4])
```

### Some Other Numpy Functions

#### Accessing Attributes

```py
len(my_array) # Length of array
my_array.ndim # Number of array dimensions
my_array.size # Number of array elements
my_array.dtype # Data type of array elements
my_array.shape # Array dimensions
```

#### Mathematical Operations

We can easily apply a wide range of mathematical operations on our arrays, a small sample of which can be seen below.

|Function|Description|
|---|---|
|`np.add(a,b)`|Add the elements of array a & b together - The arrays should be the same shape|
|`np.subtract(a,b)`|Subtract a from b for each pair of elements|
|`np.divide(a,b)`|Divide a by b for each pair of elements|
|`np.multiply(a,b)`|Multiply a by b for each pair of elements|
|`np.sqrt(a)`|Calculates the square root of each element|
|`np.median(a)`|Calculate the median value of the array|
|`np.std(a)`|Calculate the standard deviation of each element|
|`a.sum(a)`|Calculate the sum of elements in an array|
|`a.mean(a)`|Calculate the sum of elements in an array|
|`a.min(a)`|Identify the smallest value in an array|
|`a.max(a)`|Identify the highest value in an array|

Code example:

```py
array_a = np.array([4,7,2,5,3])
array_b = np.array([5,2,3,6,4])

print(np.add(array_a,array_b))
```

## Numpy Exercises

Apply your learning by trying some Numpy exercises

- [Numpy Exercises](./numpy_exercises.md)
- [Numpy Solutions](./numpy_solutions.md)
