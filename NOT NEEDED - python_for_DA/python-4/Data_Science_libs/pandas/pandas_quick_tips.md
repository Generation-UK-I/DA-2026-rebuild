# Pandas Quick Tips

## Common Plot Types with Pandas

| Plot Type | pandas Method | Equivalent plt Function |
|-----------|---------------|------------------------|
| Line plot | `df.plot(kind='line')` | `plt.plot()` |
| Bar chart | `df.plot(kind='bar')` | `plt.bar()` |
| Horizontal bar | `df.plot(kind='barh')` | `plt.barh()` |
| Scatter plot | `df.plot(kind='scatter')` | `plt.scatter()` |
| Histogram | `df.plot(kind='hist')` | `plt.hist()` |
| Box plot | `df.plot(kind='box')` | `plt.boxplot()` |
| Pie chart | `df.plot(kind='pie')` | `plt.pie()` |

## Key pandas Plotting Functions

```python
# Simple line plot
df.plot(x='column1', y='column2')

# Multiple columns
df.plot(x='column1', y=['col2', 'col3'])

# Bar chart with custom colors
df.plot(kind='bar', color=['red', 'blue'])

# Scatter plot (needs x and y)
df.plot(kind='scatter', x='col1', y='col2')

# Histogram of a single column
df['column'].plot(kind='hist', bins=10)
```

## Common plt Functions Used

| Function | Purpose |
|----------|---------|
| `plt.xlabel()` | Label x-axis |
| `plt.ylabel()` | Label y-axis |
| `plt.title()` | Add title |
| `plt.legend()` | Show legend |
| `plt.grid()` | Add grid |
| `plt.text()` | Add text annotation |
| `plt.tight_layout()` | Fix spacing |

## Tips for Beginners

1. **Always import both libraries**: `import pandas as pd` and `import matplotlib.pyplot as plt`
2. **Remember `plt.show()`** at the end
3. **Use `plt.tight_layout()`** to prevent labels from being cut off
4. **Add labels and titles** to make plots understandable
5. **Experiment with colors** to make plots visually appealing

## Common Mistakes to Avoid

- Forgetting to call `plt.show()` - nothing appears!
- Missing axis labels - plots become meaningless
- Using `df.plot()` without `plt.show()`
- Not handling rotated x-labels with `plt.tight_layout()`
- Using pie charts with too many categories (keep it simple)