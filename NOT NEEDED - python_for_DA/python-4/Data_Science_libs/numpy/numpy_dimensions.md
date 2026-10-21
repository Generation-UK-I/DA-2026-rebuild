# NumPy Dimensions

## Why is the following only two dimensions?

```python
np.array([[0,1,2,3,4], [5,6,7,8,9], [10,11,12,13,14],[15,16,17,18,19]])
```

Notice there are 5x lists; the three lists of integers (call these B1-4), which are in a list of lists, defined by the outremost square brackets (call this A).

Imagine we wanted this data in a table: List A containes four elements: B1, B2, B3, B4, these are the rows of data. Each of the B lists contains 5 elements, these are the columns of our table.

|   |   |   |   |   |
|---|---|---|---|---|
|0|1|2|3|4|
|5|6|7|8|9|
|10|11|12|13|14|
|15|16|17|18|19|

It can help to think of dimensions like axis, one axis is the number of lists (rows), the other axis is the number of items in each row.

We can use numpy's `shape` method to view the number of rows and columns in our array.

```python
print(twoDArray.shape)

(3, 5)
```

## Three Dimensions

Adding another dimension can, again, break you brain a little:

```python
np.array([[[0,1,2,3,4],[5,6,7,8,9]], [[10,11,12,13,14],[15,16,17,18,19]]])
```

Here we have 2x individual two dimensional arrays, the first one includes the lists `[0,1,2,3,4]` and `[5,6,7,8,9]`, we know it's two dimensions because there are 2 rows, with 5 columns each. The second array includes `[10,11,12,13,14]` and `[15,16,17,18,19]`, again 2 rows and 5 columns.

The third dimension is the one which contains both of these 2d arrays.

    A simple analogy is to think about egg cartons, each carton contains 2x6 eggs (2d), then imagine having multiple egg cartons and stacking them up. The third dimension is the height of the stack.

The following image illustrates the concept further.