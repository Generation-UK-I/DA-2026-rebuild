# NumPy Practical Tasks

## Task 1 — Create and Explore Arrays (Very Easy)

Create a NumPy array representing the number of coffees sold each day:

>[34, 28, 45, 51, 39, 48, 52]

Objectives:

- Convert the list into a NumPy array
- Print:
  - total sales
  - average sales
  - highest sales day
  - lowest sales day

## Task 2 — Temperature Adjustment (Easy)

A sensor is mis-calibrated and every temperature reading is 2 degrees too low.

>[18.5, 19.0, 20.2, 21.1, 19.8]

Objectives:

- Store the values in a NumPy array
- Correct the readings using vectorised addition
- Print the corrected temperatures

## Task 3 — Sales Increase Simulation (Easy → Medium)

A coffee shop increases prices, resulting in a 10% increase in daily revenue. Daily revenue:

>[120, 135, 150, 160, 145]

Objectives:

- Calculate new revenue values
- Round values to 2 decimal places
- Print both old and new arrays

## Task 4 — Find Busy Days (Medium)

Using this customer count data:

>[120, 85, 90, 140, 110, 75, 160]

Objectives:

- Find all days where customer count was greater than 100
- Print only those values

## Task 5 — Reshape Data (Medium)

A café tracks sales for 3 days, with 4 time blocks per day:

>[12, 18, 25, 20, 15, 22, 30, 28, 10, 14, 19, 16]

Objectives:

- Convert into a 3 × 4 matrix
- Print total sales per day

## Stretch & Challenge

### Task 6 — Performance Comparison (Medium → Hard)

Create:

- a Python list with 1 million numbers
- a NumPy array with the same numbers

Objectives:

- Time how long it takes to multiply all values by 2
- Compare list comprehension vs NumPy vectorisation

### Task 7 — Mini Data Analysis Challenge (Hard)

You are given exam scores:

>[55, 62, 48, 71, 69, 80, 77, 52, 60, 90]

Objectives:

- Calculate:
  - mean
  - median
  - standard deviation
- Count how many students scored above the mean
- Convert failing scores (<50) to 50
