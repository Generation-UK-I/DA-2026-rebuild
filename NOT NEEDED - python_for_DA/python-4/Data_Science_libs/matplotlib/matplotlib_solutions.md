# Matplotlib Exercises - Instructor Solutions

## Exercise 1: Line Plot

**Objective**: Create a styled line plot with markers and custom formatting.

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 6, 5]

# Create the plot
plt.plot(x, y, '--o', color='green', linewidth=2, markersize=8)

# Add labels and title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Line Plot of X vs Y')

# Display
plt.show()
```

## Exercise 2: Scatter Plot

**Objective**: Create a scatter plot to visualize the relationship between two variables.

```python
import matplotlib.pyplot as plt

# Data
height = [150, 155, 160, 165, 170, 175]
weight = [50, 55, 60, 65, 70, 75]

# Create scatter plot
plt.scatter(height, weight, color='blue')

# Labels and title
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Relationship Between Height and Weight')

# Display
plt.show()
```

## Exercise 3: Bar Chart

**Objective**: Create a vertical bar chart with rotated labels.

```python
import matplotlib.pyplot as plt

# Data
fruits = ["Apples", "Bananas", "Cherries", "Dates"]
sales = [50, 75, 40, 20]

# Create bar chart
plt.bar(fruits, sales, color=['red', 'yellow', 'purple', 'brown'], edgecolor='black')

# Labels and title
plt.xlabel('Fruit')
plt.ylabel('Sales (units)')
plt.title('Fruit Sales Report')

# Rotate x-axis labels
plt.xticks(rotation=45)

# Display
plt.show()
```

## Exercise 4: Horizontal Bar Chart

**Objective**: Create a horizontal bar chart.

```python
import matplotlib.pyplot as plt

# Data
countries = ["UK", "USA", "Germany", "France"]
population = [67, 331, 83, 65]

# Create horizontal bar chart
plt.barh(countries, population, color='steelblue', edgecolor='black')

# Labels and title
plt.xlabel('Population (millions)')
plt.ylabel('Country')
plt.title('Population by Country')

# Display
plt.show()
```

## Exercise 5: Histogram

**Objective**: Create a histogram to visualize the distribution of scores.

```python
import matplotlib.pyplot as plt

# Data
scores = [55, 60, 62, 65, 70, 72, 75, 80, 85, 90]

# Create histogram with 5 bins
plt.hist(scores, bins=5, color='lightgreen', edgecolor='black')

# Labels and title
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.title('Distribution of Student Scores')

# Display
plt.show()
```

## Exercise 6: Multiple Lines on One Plot

**Objective**: Create a multi-line plot with legend to compare two products.

```python
import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr"]
product_A = [30, 35, 40, 38]
product_B = [20, 22, 25, 30]

# Plot both lines
plt.plot(months, product_A, marker='o', linewidth=2, label='Product A')
plt.plot(months, product_B, marker='s', linewidth=2, label='Product B')

# Labels and title
plt.xlabel('Month')
plt.ylabel('Sales (units)')
plt.title('Product Sales Comparison')

# Add legend
plt.legend()

# Display
plt.show()
```
