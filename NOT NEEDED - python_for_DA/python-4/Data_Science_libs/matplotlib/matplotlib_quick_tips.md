# MatPlotLib Quick Tips

| Plot Type | Function | Common Parameters |
|-----------|----------|-------------------|
| Line plot | `plt.plot(x, y)` | `color`, `linestyle`, `marker`, `linewidth` |
| Scatter plot | `plt.scatter(x, y)` | `color`, `s` (size), `alpha` |
| Bar chart | `plt.bar(x, y)` | `color`, `edgecolor` |
| Horizontal bar | `plt.barh(x, y)` | `color`, `edgecolor` |
| Histogram | `plt.hist(data)` | `bins`, `color`, `edgecolor` |

| Useful Functions ||
|-|-|
| `plt.xlabel()` | Label x-axis |
| `plt.ylabel()` | Label y-axis |
| `plt.title()` | Add title |
| `plt.legend()` | Show legend |
| `plt.grid()` | Add grid |
| `plt.xticks(rotation=45)` | Rotate labels |
| `plt.tight_layout()` | Fix spacing |

---

## Common Mistakes to Watch For

1. **Forgetting `plt.show()`** - Plot won't appear without it
2. **Missing labels** - Always label axes for clarity
3. **Not importing matplotlib** - `import matplotlib.pyplot as plt` is required
4. **Rotated labels getting cut off** - Use `plt.tight_layout()`
5. **Colors not displaying** - Check color names or use hex codes