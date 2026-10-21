# Introduction to Pandas

Pandas is one of the most popular data science libraries for Python, it is particularly powerful for data analysis. It is built upon Numpy, but introduces two new powerful data structures we can work with:

- Series: A column of data
- DataFrame: A table of data (columns and rows)

Pandas is for working with fast numerical arrays; Pandas is for working with labelled data tables, a Pandas DataFrame is similar to an Excel spreadsheet.

In addition to tabular data, Pandas is commonly used for:

- real-world data
- CSV files
- Logs/Metrics
- Importing spreadsheets
- Filtering and aggregation
- Time series data

## Installing Pandas

>If you have deployed the `Anaconda/Jupyter` environment in `Docker` you may skip this step, numpy, pandas, and matplotlib are installed automatically via the requirements.txt file.

Pandas is not included in the Standard Python Library, but it can be installed using `pip`.

>**Optional**: Create a virtual environment with `python -m venv ./venv` then activate it with `.venv\Scripts\activate.ps1`

Install numpy by running `pip install pandas` in your terminal, then import it into your workspace just like any other module, however by convention we alias it as `pd`:

```python
import pandas as pd
```

## Pandas Series

### Creating a Series

A series is a column of data with a labelled index, it's similar to a 1D-array.

```py
import pandas as pd

sales = pd.Series([120, 135, 150, 160])

print(sales)
```

We said there is a **labelled index**, we can provide our own labels for the values using the `index` argument, if we do not do so, then the items are labelled with their index number, and can be accessed similarly to elements in a list or an array.

>Not providing labels for the `index` is the same as defining it as `index=index`

```py
sales = pd.Series([120, 135, 150, 160])

print(sales[1])
```

If we do provide an alternative label we can access elements using that:

```py
sales = pd.Series([120, 135, 150, 160], index = ["w", "x", "y", "z"])

print(sales["x"])
```

A series can also be created from a dictionary:

```py
sales = {
    "Monday": 389,
    "Tuesday": 298,
    "Wednesday": 187,
    "Thursday": 612,
    "Friday": 412
    }

my_series = pd.Series(sales)

print(my_series)
```

### Working with Pandas Series

Similar to Numpy arrays, we can access attributes of the series

```py
s = pd.Series([10, 20, 30, 40, 50])

print(s.head(3))      # First 3 elements
print(s.tail(2))      # Last 2 elements
print(s.describe())   # Statistical summary
print(s.shape)        # (5,)
print(s.size)         # 5
```

We can also perform mathematical operations directly against the series

```py
print(s + 5)    # Add 5 to each: [15, 25, 35, 45, 55]
print(s * 2)    # Multiply by 2: [20, 40, 60, 80, 100]
print(s ** 2)   # Square each: [100, 400, 900, 1600, 2500]
print(s / 10)   # Divide by 10: [1, 2, 3, 4, 5]
```

Remember, Pandas is for data science, so we can also perform easy statistical analysis

```py
print(s.mean())      # 30.0
print(s.median())    # 30.0
print(s.sum())       # 150
print(s.min())       # 10
print(s.max())       # 50
print(s.std())       # Standard deviation: 15.81
print(s.var())       # Variance: 250.0
```

We can also do sorting, filtering, cleaning, string operations, and more. However, Pandas is a lot more powerful when we work with DataFrames.

## Pandas DataFrames

### Creating a DataFrame

Where as a Series is a single column of data, a DataFrame comprises both columns and rows, i.e. a table. In other words, a DataFrame has 2 dimensions.

```py
data = {
    "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "sales": [389, 298, 187, 612, 412],
}

df = pd.DataFrame(data)

print(df)
```

We can add additional columns to our DataFrame by adding additional Series

```py
data = {
    "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "sales": [389, 298, 187, 612, 412],
    "customers": [30, 26, 22, 57, 39]
}

df = pd.DataFrame(data)

print(df)
```

### Working With DataFrames

This is where we start to see the power and efficiency of Pandas, we can start by using many of the same methods against the DataFrame.

```py
df.head(n)
df.tail(n)
df.info()
df.describe()
df.shape
df.columns
```

#### Selecting data

One powerful feature is being able to easily select data, and select data according to conditions

```py
data = {
    "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "sales": [389, 298, 187, 612, 412],
    "customers": [30, 26, 22, 57, 39]
}

df = pd.DataFrame(data)

df["day"]                       # Select column
df[["sales", "customers"]]      # Select multiple columns
df.iloc[0]                      # Select row (iloc integer location, basically the row's index
df[df["sales"] > 300]           # Select only rows where sales are >300
```

#### Sorting data

We can sort data easily

```py
print(df.sort_values("sales"))
print(df.sort_values("customers", ascending=False))
print(df.sort_index())
```

#### Creating New Columns

Data Analysis is involves answering questions using your data, for example: "*What is the average spend per customer?*"

We can answer the question using Pandas to create a new column containing newly calculated values, in this case the average spend per customer, by dividing `/` the `sales` by `customers` on each day (row)

```py
df["avg_per_cust"] = df["sales"] / df["customers"]
```

#### Removing columns

Delete columns with the `drop` function

```py
df.drop(columns=["sales"])
```

#### Mathematical and Statistical Functions

Just like Series, we can perform fast calculations against our DataFrame, although the syntax has an extra component to identify the column on which to perform the calculation

```py
print(df["sales"].mean())
print(df["sales"].sum())
print(df["sales"].max())
print(df["sales"].std())
```

---

There are also functions for reshaping DFs, joining them like SQL tables, cleaning data, creating subsets, querying the DF, and more. However, one of Pandas' most powerful features is it's ability to create visualisations through integration with Matplotlib.

## Pandas Visualisation

Pandas can generate a wide variety of visualisations, however bare in mind that different chart types may depend upon different types of DataFrames.

The structure of the `plot` function is as follows:

`df_line.plot(x="[series_1]", y="[series_2]", kind="[Chart_type]")`

---

### Line Plot

To show how something changes over time.

```py
df_line = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "temperature": [12, 14, 15, 13, 16]
})

df_line.plot(x="day", y="temperature", kind="line")
```

---

### Multiple Line Plot

To compare trends across multiple groups.

```py
df_multi_line = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr"],
    "product_A": [30, 35, 40, 38],
    "product_B": [20, 22, 25, 30]
})

df_multi_line.plot(x="month", y=["product_A", "product_B"], kind="line")
```

---

### Bar Chart

To compare quantities across categories.

```py
df_hbar = pd.DataFrame({
    "country": ["United Kingdom", "United States", "Germany", "France"],
    "population_millions": [67, 331, 83, 65]
})

df_hbar.plot(x="country", y="population_millions", kind="barh")
```

---

### Horizontal Bar Chart

When category labels are long or numerous

```py
df_hbar = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "temperature": [12, 14, 15, 13, 16]
})

df_hbar.plot(x="day", y="temperature", kind="barh")
```

---

### Grouped Bar Plot

To compare categories and subcategories.

```py
df_grouped = pd.DataFrame({
    "quarter": ["Q1", "Q1", "Q2", "Q2"],
    "product": ["A", "B", "A", "B"],
    "sales": [100, 80, 120, 90]
})

df_grouped.pivot(index="quarter", columns="product", values="sales").plot(kind="bar")
```

---

### Scatter Plot

To show correlation or patterns between two variables.

```py
df_scatter = pd.DataFrame({
    "hours_studied": [1, 2, 3, 4, 5],
    "test_score": [50, 55, 65, 70, 80]
})

df_scatter.plot(x="hours_studied", y="test_score", kind="scatter")
```

---

### Histogram

To show how values are distributed

```py
df_hist = pd.DataFrame({
    "scores": [55, 60, 62, 65, 70, 72, 75, 80, 85, 90]
})

df_hist["scores"].plot(kind="hist", bins=5)
```

---

### Box Plot

To compare distributions across categories.

```py
df_box = pd.DataFrame({
    "class": ["A", "A", "A", "B", "B", "B"],
    "score": [70, 75, 80, 65, 68, 72]
})

df_box.boxplot(by="class", column="score")
```

---

### Pie Chart

To show parts of a whole

```py
df_pie = pd.DataFrame({
    "category": ["Rent", "Food", "Transport", "Entertainment"],
    "amount": [800, 300, 120, 150]
})

df_pie.set_index("category")["amount"].plot(kind="pie")
```

## Plot Types Summary

|Goal|Best Plot|
|---|---|
|Show a trend|Line plot|
|Compare categories|Bar chart|
|Show distribution|Histogram|
|Show relationship|Scatter plot|
|Compare multiple trends|Multi‑line plot|
|Compare distributions|Box plot|

---

>TODO: CSV section

## Pandas Exercises

Practice your knowledge by trying the tasks linked below.

- [Pandas Exercises](pandas_exercises.md)
- [Pandas Solutions](./pandas_solutions.md.md)
- [Pandas Quick Tips](./pandas_quick_tips.md)
