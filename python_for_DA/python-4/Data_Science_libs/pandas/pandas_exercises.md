# Pandas Exercises

These exercises are designed to help you understand the key functionality of Pandas.

## Working with Series

The following tasks require you to work with a single series.

### **1. Basic Arithmetic on a Series**

```py
import pandas as pd

s = pd.Series([10, 20, 30, 40, 50])
```

Tasks:

- Increase every value in the Series by 5.
- Then calculate the Series multiplied by 2.

### **2. Summary Statistics**

```py
s = pd.Series([3, 7, 2, 9, 4, 6, 8, 10, 9, 11, 4, 6, 10])
```

Tasks:

- Find the:
  - mean
  - median
  - minimum
  - maximum

### **3. Boolean Filtering**

```py
s = pd.Series([12, 5, 18, 7, 20, 3, 15, 9, 11, 13, 8, 2, 10])
```

Task:

- Create a new Series containing only the values greater than 10.
- Create a second Series containing only the values lower than 10.

### **4. Value Counts (Categorical Data)**

```py
s = pd.Series(["red", "Yellow", "blue", "red", "pink", "green", "blue", "red", "Yellow", "red", "pink", "green"])
```

Task:

- Count how many times each colour appears.

### **5. Applying a Function**

```py
s = pd.Series([1, 4, 9, 16, 25])
```

Task:

- Create a new Series containing the square roots of each value.

## Working with DataFrames

The following tasks require you to work with a DataFrame.

### **1. Column Arithmetic**

```py
df = pd.DataFrame({
    "price": [5, 10, 15, 20],
    "quantity": [1, 2, 3, 4]
})
```

Task:

- Create a new column called `total_cost` equal to `price` x `quantity`.

### **2. Row Filtering**

```py
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40]
})
```

Task:

- Select only the rows where age is greater than 30.

### **3. Basic Statistics on a DataFrame**

```py
df = pd.DataFrame({
    "math": [70, 80, 90, 85],
    "english": [65, 75, 70, 80]
})
```

Task:

- Calculate the mean score for each subject.
- Calculate the average score per student.

### **4. Normalising a Column**

```py
df = pd.DataFrame({
    "math": [70, 80, 90, 85],
    "english": [65, 75, 70, 80]
})
```

Task:

- Create a new column `value_normalised` where each value is divided by the maximum value in the column.

### **5. Grouping and Aggregation**

```py
df = pd.DataFrame({
    "math": [70, 80, 90, 85],
    "english": [65, 75, 70, 80]
})
```

Task:

- Calculate the total points scored by each team.

### **6. Sorting Data**

```py
df = pd.DataFrame({
    "product": ["A", "B", "C", "D"],
    "sales": [200, 150, 300, 100]
})
```

Task:

- Sort the DataFrame by sales in descending order.

## Choosing the Right Visualisation

Each exercise includes a small DataFrame and a question that can be answered by the data. Your objective is to choose an appropriate visualisation to answer the question, based on the structure and meaning of the data.

### **1. Daily Temperatures**

How does temperature change across the week?

```python
import pandas as pd

df1 = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "temperature": [12, 14, 15, 13, 16, 18, 17]
})
```

<details><summary>Hint:</summary>Trend Over Time</details>

### **2. Fruit Sales**

Which fruit sold the most?

```python
df2 = pd.DataFrame({
    "fruit": ["Apples", "Bananas", "Cherries", "Dates"],
    "sales": [50, 75, 40, 20]
})
```

<details><summary>Hint:</summary>Categorical Comparison</details>

### **3. Student Study Hours vs Test Score**

Is there a correlation between hours studied and test score?

```python
df3 = pd.DataFrame({
    "hours_studied": [1, 2, 3, 4, 5, 6],
    "test_score": [50, 55, 65, 70, 80, 85]
})
```

<details><summary>Hint:</summary>Relationship</details>

### **4. Distribution of Exam Scores**

How are exam scores distributed?  

```python
df4 = pd.DataFrame({
    "score": [55, 60, 62, 65, 70, 72, 75, 80, 85, 90, 92, 95]
})
```

<details><summary>Hint:</summary>Spread</details>

### **5. Monthly Revenue for Two Products**

How do revenue trends for two products compare over time?

```python
df5 = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "product_A": [1000, 1200, 1300, 1250, 1400],
    "product_B": [900, 950, 1100, 1150, 1200]
})
```

<details><summary>Hint:</summary>Multiple Trends</details>

### **6. Budget Breakdown**

How is the monthly budget divided across categories?

```python
df6 = pd.DataFrame({
    "category": ["Rent", "Food", "Transport", "Entertainment", "Savings"],
    "amount": [800, 300, 120, 150, 200]
})
```

<details><summary>Hint:</summary>Proportions</details>

### **7. Class Scores by Group**

How do the score distributions compare between Class A and Class B?

```python
df7 = pd.DataFrame({
    "class": ["A", "A", "A", "B", "B", "B"],
    "score": [70, 75, 80, 65, 68, 72]
})
```

<details><summary>Hint:</summary>Distribution comparison, including medians and outliers</details>

### **8. Website Traffic Sources**

Which traffic sources contribute most to total visits?

```python
df8 = pd.DataFrame({
    "source": ["Search", "Direct", "Social", "Referral"],
    "visits": [500, 300, 150, 50]
})
```

<details><summary>Hint:</summary>Categorical Proportions</details>

### **9. Sales by Quarter and Product**

How do product sales compare across quarters?

```python
df9 = pd.DataFrame({
    "quarter": ["Q1", "Q1", "Q2", "Q2", "Q3", "Q3"],
    "product": ["A", "B", "A", "B", "A", "B"],
    "sales": [100, 80, 120, 90, 140, 110]
})
```

<details><summary>Hint:</summary>Grouped Categories</details>

### **10. Height vs Weight**

Is there a relationship between height and weight?

```python
df10 = pd.DataFrame({
    "height_cm": [150, 155, 160, 165, 170, 175, 180],
    "weight_kg": [50, 55, 60, 65, 70, 75, 80]
})
```

<details><summary>Hint:</summary>Scatter With Trend</details>
