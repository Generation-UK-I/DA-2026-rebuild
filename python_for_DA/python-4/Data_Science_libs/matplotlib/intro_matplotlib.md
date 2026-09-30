# Introduction to Matplotlib

Matplotlib is the fundamental plotting library in Python for creating static, animated, and interactive visualizations. It's the foundation upon which many other Python visualization libraries (like Seaborn, Pandas plotting, and Plotly) are built.

It is used for:

- Analysing trends
- Comparing values
- Monitoring systems
- Presenting findings
- Debugging performance issues

## Installing Matplotlib

>If you have deployed the `Anaconda/Jupyter` environment in `Docker` you may skip this step, numpy, pandas, and matplotlib are installed automatically via the requirements.txt file.

Matplotlib is not included in the Standard Python Library, but it can be installed using `pip`.

>**Optional**: Create a virtual environment with `python -m venv ./venv` then activate it with `.venv\Scripts\activate.ps1`

Install Matplotlib by running `pip install Matplotlib` in your terminal, then import it into your workspace just like any other module, however by convention we alias it as `pd`:

```python
import Matplotlib.pyplot as plt
```

## Why Matplotlib?

- Versatility: Create almost any type of plot imaginable
- Fine-grained control: Customize every aspect of your plots
- Integration: Works seamlessly with NumPy, Pandas, and SciPy
- Cross-platform: Works on Windows, macOS, Linux, and in web backends
- Publication-quality: Produce high-resolution figures for papers and presentations

### Architecture

Matplotlib has a three-layer architecture:

- Backend Layer: Handles rendering to various outputs (screen, files, etc.)
- Artist Layer: Everything you see (lines, text, ticks, etc.) is an Artist object
- Scripting Layer (pyplot): The interface most users interact with

### Anatomy of a Matplotlib Figure

Matplotlib graphs your data on Figures which are made of several parts:

- Figure: Think of the Figure as a blank canvas or a piece of paper. It's the top-level container that holds everything.
- Axes: Where the actual plotting happens. A Figure can contain multiple Axes objects.
- Axis: Handles the x-axis and y-axis, including limits, ticks, and labels.
- Ticks: the marks on the axes
- Labels: axis labels
- Title: the plot title
- Legend: labels for multiple lines or categories

Think of the Figure as a blank canvas or a piece of paper. It's the top-level container that holds everything.

## Creating Plots

### Line Plots

Line plots show trends over time.

```py
import matplotlib.pyplot as plt

cpu_usage = [40, 55, 70, 65, 80]

plt.plot(cpu_usage)
plt.show()
```

- `plot()`: draws the graph
- `show()`: renders it
- The default x-axis is the `index` position

#### Adding Labels and Title

A chart without labels is almost useless.

```py
plt.plot(cpu_usage)
plt.title("CPU Usage Over Time")
plt.xlabel("Time")
plt.ylabel("CPU %")
plt.show()
```

#### Customising Style

Basic styling makes plots readable, markers show data points, and line styles improve clarity. Common customisations include `marker`, `linestyle`, `linewidth`, and `color`.

```py
plt.plot(cpu_usage, marker="o", linestyle="--", linewidth=2)
```

#### Multiple Lines on One Plot

You can define multiple plots as part of the same figure; ensure you include a Legend to identify datasets.

```py
cpu = [40, 55, 70, 65]
memory = [60, 65, 75, 85]

plt.plot(cpu, label="CPU")
plt.plot(memory, label="Memory")

plt.legend()
plt.show()
```

### Bar Charts

Bar charts compare categories.

```py
servers = ["A", "B", "C"]
cpu = [65, 80, 55]

plt.bar(servers, cpu)
plt.show()
```

### Histograms

Histogram shows frequency distribution

```py
response_times = [0.5, 0.7, 0.6, 1.2, 1.5, 0.9]

plt.hist(response_times)
plt.show()
```

### Scatter Plots

Shows correlation between variables.

```py
cpu = [40, 50, 60, 70]
response = [0.5, 0.6, 0.9, 1.4]

plt.scatter(cpu, response)
plt.show()
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

## Saving Plots

Simple, but important

```py
plt.savefig("cpu_plot.png")
```

## Matplotlib Exercises

Practice your knowledge by trying the tasks linked below.

- [Matplotlib Exercises](./matplotlib_exercises.md)
- [Matplotlib Solutions](./matplotlib_solutions.md)
- [Matplotlib Quick Tips](./matplotlib_quick_tips.md)
