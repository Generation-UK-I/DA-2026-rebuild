# Pandas Exercises - Instructor Solutions (Pyplot Interface)

These solutions use the simple pyplot interface with pandas plotting functionality, which is beginner-friendly.

## Exercise 1: Daily Temperatures

**Objective**: Create a line plot showing temperature changes across the week.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Data
df1 = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "temperature": [12, 14, 15, 13, 16, 18, 17]
})

# Create line plot
df1.plot(x='day', y='temperature', kind='line', marker='o', color='red', legend=False)

# Labels and title
plt.xlabel('Day of Week')
plt.ylabel('Temperature (°C)')
plt.title('Daily Temperatures Throughout the Week')

# Display
plt.show()
```

## Exercise 2: Fruit Sales

**Objective**: Create a bar chart to identify which fruit sold the most.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Data
df = pd.DataFrame({
    "fruit": ["Apples", "Bananas", "Cherries", "Dates"],
    "sales": [50, 75, 40, 20]
})

# Create bar chart
df.plot(x='fruit', y='sales', kind='bar', color=['red', 'yellow', 'purple', 'brown'], legend=False)

# Labels and title
plt.xlabel('Fruit')
plt.ylabel('Sales (units)')
plt.title('Fruit Sales - Banana is the Best Seller!')

# Display
plt.show()
```

## Exercise 3: Student Study Hours vs Test Score

**Objective**: Create a scatter plot to explore correlation between study hours and test scores.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Data
df = pd.DataFrame({
    "hours_studied": [1, 2, 3, 4, 5, 6],
    "test_score": [50, 55, 65, 70, 80, 85]
})

# Create scatter plot
df.plot(x='hours_studied', y='test_score', kind='scatter', color='blue')

# Labels and title
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Relationship Between Study Hours and Test Scores')

# Display
plt.show()
```


## Exercise 4: Distribution of Exam Scores

**Objective**: Create a histogram to understand score distribution.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Data
df = pd.DataFrame({
    "score": [55, 60, 62, 65, 70, 72, 75, 80, 85, 90, 92, 95]
})

# Create histogram
df['score'].plot(kind='hist', bins=5, color='lightgreen', edgecolor='black', alpha=0.7)

# Labels and title
plt.xlabel('Exam Score')
plt.ylabel('Frequency')
plt.title('Distribution of Exam Scores')
plt.legend()
plt.grid(axis='y', alpha=0.3)

# Display
plt.show()
```

## Exercise 5: Monthly Revenue for Two Products

**Objective**: Create a line plot comparing revenue trends for two products.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Data
df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "product_A": [1000, 1200, 1300, 1250, 1400],
    "product_B": [900, 950, 1100, 1150, 1200]
})

# Create line plots
df.plot(x='month', y=['product_A', 'product_B'], kind='line', marker='o', linewidth=2)

# Labels and title
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.title('Monthly Revenue Comparison: Product A vs Product B')

# Display
plt.show()
```

**Alternative using pandas plot:**
```python
df5.plot(x='month', y=['product_A', 'product_B'], kind='line', marker='o', linewidth=2)
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.title('Monthly Revenue Comparison: Product A vs Product B')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## Exercise 6: Budget Breakdown

**Objective**: Create a pie chart showing how budget is allocated.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Data
df6 = pd.DataFrame({
    "category": ["Rent", "Food", "Transport", "Entertainment", "Savings"],
    "amount": [800, 300, 120, 150, 200]
})

# Create pie chart
plt.pie(df6["amount"], 
        labels=df6["category"], 
        autopct='%1.1f%%',  # Show percentages
        startangle=90,       # Rotate for better appearance
        colors=['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightgray'])

plt.title('Monthly Budget Breakdown')
plt.show()
```

**Alternative using pandas plot:**
```python
df6.set_index('category')['amount'].plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Monthly Budget Breakdown')
plt.ylabel('')  # Remove default ylabel
plt.show()
```

---

## Exercise 7: Class Scores by Group

**Objective**: Create side-by-side box plots to compare score distributions.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Data
df7 = pd.DataFrame({
    "class": ["A", "A", "A", "B", "B", "B"],
    "score": [70, 75, 80, 65, 68, 72]
})

# Prepare data for box plot
class_a_scores = df7[df7["class"] == "A"]["score"]
class_b_scores = df7[df7["class"] == "B"]["score"]

# Create box plot
plt.boxplot([class_a_scores, class_b_scores], 
            labels=['Class A', 'Class B'],
            patch_artist=True,
            boxprops=dict(facecolor='lightblue'))

# Labels and title
plt.xlabel('Class')
plt.ylabel('Score')
plt.title('Score Distribution Comparison: Class A vs Class B')
plt.grid(axis='y', alpha=0.3)

plt.show()
```

**Alternative using pandas plot:**
```python
# Pivot the data for box plot
df7.boxplot(column='score', by='class')
plt.title('Score Distribution Comparison')
plt.suptitle('')  # Remove default title
plt.xlabel('Class')
plt.ylabel('Score')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

---

## Exercise 8: Website Traffic Sources

**Objective**: Create a bar chart showing traffic source contributions.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Data
df8 = pd.DataFrame({
    "source": ["Search", "Direct", "Social", "Referral"],
    "visits": [500, 300, 150, 50]
})

# Create bar chart
plt.bar(df8["source"], df8["visits"], color='skyblue', edgecolor='black')

# Add value labels on top of bars
for i, visits in enumerate(df8["visits"]):
    plt.text(i, visits + 10, str(visits), ha='center', fontweight='bold')

# Labels and title
plt.xlabel('Traffic Source')
plt.ylabel('Number of Visits')
plt.title('Website Traffic by Source - Search Dominates')

# Add total visits annotation
total = df8["visits"].sum()
plt.text(0.5, 520, f'Total: {total} visits', fontsize=10, style='italic')

plt.tight_layout()
plt.show()
```

**Alternative using pandas plot:**
```python
df8.plot(x='source', y='visits', kind='bar', color='skyblue', legend=False)
plt.xlabel('Traffic Source')
plt.ylabel('Number of Visits')
plt.title('Website Traffic by Source - Search Dominates')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

## Exercise 9: Sales by Quarter and Product

**Objective**: Create grouped bar charts to compare product sales across quarters.

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
df9 = pd.DataFrame({
    "quarter": ["Q1", "Q1", "Q2", "Q2", "Q3", "Q3"],
    "product": ["A", "B", "A", "B", "A", "B"],
    "sales": [100, 80, 120, 90, 140, 110]
})

# Pivot the data for easier plotting
pivot_df = df9.pivot(index='quarter', columns='product', values='sales')
print(pivot_df)  # Shows the reshaped data

# Create grouped bar chart
pivot_df.plot(kind='bar', color=['steelblue', 'lightcoral'], edgecolor='black')

# Labels and title
plt.xlabel('Quarter')
plt.ylabel('Sales')
plt.title('Product Sales Comparison by Quarter')
plt.legend(title='Product')
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for container in plt.gca().containers:
    plt.bar_label(container, label_type='edge')

plt.tight_layout()
plt.show()
```

**Alternative without pivot (more manual):**
```python
quarters = ['Q1', 'Q2', 'Q3']
product_a_sales = [100, 120, 140]
product_b_sales = [80, 90, 110]

x = np.arange(len(quarters))
width = 0.35

plt.bar(x - width/2, product_a_sales, width, label='Product A', color='steelblue')
plt.bar(x + width/2, product_b_sales, width, label='Product B', color='lightcoral')

plt.xlabel('Quarter')
plt.ylabel('Sales')
plt.title('Product Sales Comparison by Quarter')
plt.xticks(x, quarters)
plt.legend()
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## Exercise 10: Height vs Weight

**Objective**: Create a scatter plot to explore the relationship between height and weight.

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
df10 = pd.DataFrame({
    "height_cm": [150, 155, 160, 165, 170, 175, 180],
    "weight_kg": [50, 55, 60, 65, 70, 75, 80]
})

# Create scatter plot
plt.scatter(df10["height_cm"], df10["weight_kg"], color='green', s=100, alpha=0.7)

# Add trend line
z = np.polyfit(df10["height_cm"], df10["weight_kg"], 1)
p = np.poly1d(z)
plt.plot(df10["height_cm"], p(df10["height_cm"]), "r--", linewidth=2, label='Trend Line')

# Labels and title
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Height vs Weight Relationship')

# Add correlation coefficient
correlation = df10["height_cm"].corr(df10["weight_kg"])
plt.text(152, 78, f'Correlation: {correlation:.2f}', fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

**Alternative using pandas plot:**
```python
df10.plot(x='height_cm', y='weight_kg', kind='scatter', color='green', s=100)
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Height vs Weight Relationship')
plt.grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(df10["height_cm"], df10["weight_kg"], 1)
p = np.poly1d(z)
plt.plot(df10["height_cm"], p(df10["height_cm"]), "r--", linewidth=2, label='Trend')
plt.legend()

plt.show()
```

---

