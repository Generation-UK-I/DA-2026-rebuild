# Programming Foundations - Solutions to Exercises

</details>

## Lesson 1: Variables

### Exercise 1

<details><summary>Answer:</summary>

```py
val_1 = 10
val_2 = 15

myVar = val_1 + val_2
print(myVar)
```

</details>

### Exercise 2

<details><summary>Answer:</summary>

```py
number = 15

total = number**2
print(total)
```

</details>

### Exercise 3

<details><summary>Answer:</summary>

```py
num_1 = 15
num_1 += 100

print(num_1)
```

</details>

### Exercise 4

<details><summary>Answer:</summary>

```py
val_1 = 75
val_2 = 87

compare = val_1 > val_2
print(compare)
```

</details>

## Lesson 2: Strings

### Exercise 1

<details><summary>Answer:</summary>

```py
myVar = 'hello world'
print(myVar)
```

</details>

### Exercise 2

<details><summary>Answer:</summary>

```py
line1 = 'Jurrasic'
line2 = ' Park'
film = line1 + line2
```

</details>

### Exercise 3

<details><summary>Answer:</summary>

```py
name = 'charles babbage'

formatted = name.title()

print(formatted)
```

</details>

### Exercise 4

<details><summary>Answer:</summary>

```py
val_1 = 'gathering'
val_2 = 'cleaning'
val_3 = 'visualisations'

sentence = f"Data Analysis includes {val_1} data, {val_2} data, and creating {val_3}"

print(sentence)
```

</details>

## Lesson 3: Lists

### Exercise 1

<details><summary>Answer:</summary>

```py
NamesList = ["Bob", "Sally", "Mohammed", "Maddie"]

print(NamesList)
```

</details>

### Exercise 2

<details><summary>Answer:</summary>

```py
BandList = ["Queen", "Led Zeppelin", "Black Sabbath", "Iron Maiden"]

FirstBand = BandList[0]
SecondBand = BandList[3]
```

</details>

### Exercise 3

<details><summary>Answer:</summary>

```py
New_Car = "Porsche"

Car_List = ["Ferrari", "Aston Martin", "Lamborghini"]

Car_List.append(New_Car)
```

</details>

### Exercise 4

<details><summary>Answer:</summary>

```py
Mixed_List = ["Ferrari", 4, 2.4, True]

print(Mixed_List)
```

</details>

## Lesson 3: Loops

### Exercise 1

<details><summary>Answer:</summary>

```py
colours_list = ['red', 'yellow', 'blue']

colours = []

for item in colours_list:
    colours.append(item)

print(colours)
```

</details>

### Exercise 2

<details><summary>Answer:</summary>

```py
numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total += num

print(total)
```

</details>

### Exercise 3

<details><summary>Answer:</summary>

```py
numbers = []

for num in range(1,11):
    numbers.append(num)
    
print(numbers)
```

</details>

### Exercise 4

<details><summary>Answer:</summary>

```py
numbers = []

total_sales = [3500, 4200, 2900, 3200, 4500, 3000]

six_month_total = 0
sales_per_employee = 0
annual_estimate = 0

for num in total_sales:
    six_month_total += num

sales_per_employee = six_month_total/10
annual_estimate = six_month_total*2
```

</details>

## Lesson 3: List Comprehension

### Exercise 1

<details><summary>Answer:</summary>

```py
cars = ["ford", "toyota", "mercedes"]

uppercase_cars = [car.upper() for car in cars]

print(uppercase_cars)
```

</details>

### Exercise 2

<details><summary>Answer:</summary>

```py
numbers = [2, 3, 4, 5, 6]

cubes = [num**3 for num in numbers]

print(cubes)
```

</details>

### Exercise 3

<details><summary>Answer:</summary>

```py
wholesale_prices = [30, 21.2, 15.6, 78, 5.78, 45.90]

retail_prices = [round(x*1.2, 2) for x in wholesale_prices]

print(retail_prices)
```

</details>

### Exercise 4

<details><summary>Answer:</summary>

```py
retail_prices = [44.99, 30, 5.50, 199.99, 1, 939]

wholesale_prices = [round(x*0.8, 2) for x in retail_prices]

print(wholesale_prices)
```

</details>

## Lesson 5: Dictionaries

### Exercise 1

<details><summary>Answer:</summary>

```py
band = {
    "name": "Queen",
    "genre": "Rock",
    "lead_singer": "Freddie Mercury"
}

singer = band['lead_singer']
```

</details>

### Exercise 2

<details><summary>Answer:</summary>

```py
band = {
    "name": "Queen",
    "genre": "Rock",
    "lead_singer": "Freddie Mercury"
}

band["guitarist"] = "Brian May"
```

</details>

### Exercise 3

<details><summary>Answer:</summary>

```py
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 91},
    {"name": "Maria", "score": 82},
    {"name": "Sumar", "score": 78},    
]

for student in students:
    sentence = f'{student['name']} has passed the test'
    print(sentence)
```

</details>

### Exercise 4

<details><summary>Answer:</summary>

```py
basket = {
    "rice" : 2.50,
    "eggs" : 1.99,
    "sausages" : 3.30,
    "shampoo" : 4.25,
    "butter" : 2.35,
    "mince" : 3.99
    }

total = 0

for x in basket.values():
    total += x
    
print(total)
```

</details>

### Stretch and Challenge

<details><summary>Answer:</summary>

```py
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 91},
    {"name": "Maria", "score": 82},
    {"name": "Sumar", "score": 78},    
]

scores = [student['score'] for student in students] # Extract scores into list - Hint: use list comprehension

average = sum(scores)/len(scores)

print(scores)
print(average)
```

</details>

## Lesson 4: If Statements

### Exercise 1

<details><summary>Answer:</summary>

```py
current_temp = 20
baseline = 15

message = ''

if current_temp > baseline:
    message = "It's warm"
else:
    message = "It's cold"

print(message)
```

</details>

### Exercise 2

<details><summary>Answer:</summary>

```py
child_age = 13
message = ''

if child_age > 9 and child_age < 15:
    message = "You may attend"
else:
    message = "You are outside of the age range!"
    
print(message)
```

</details>

### Exercise 3

<details><summary>Answer:</summary>

```py
child_age = 9
message = ''

if child_age < 10:
    message = "Too young"
elif child_age > 14:
    message = "Too old"
else:
    message = "You may attend"

print(message)
```

</details>

### Exercise 4

<details><summary>Answer:</summary>

```py
courses = ["Linux", "Python", "Networking", "SQL"]
course_available = False

if "Python" in courses:
    course_available = True
    
print(course_available)
```

</details>

### Stretch and Challenge

<details><summary>Answer:</summary>

```py
students = [
    {"name": "Ahmed", "faults": 8},
    {"name": "Sarah", "faults": 7},
    {"name": "Paul", "faults": 11},
    {"name": "Sidra", "faults": 6},
    {"name": "Peter", "faults": 17},    
]

passed = [student["name"] for student in students if student["faults"] < 10]
        
print(passed)
```

</details>

## Lesson 5: Functions

### Exercise 1

<details><summary>Answer:</summary>

```py
def greeting():
    return 'Good morning Jamal'

message = greeting()

print(message)
```

</details>

### Exercise 2

<details><summary>Answer:</summary>

```py
def greeting(name):
    return f'Good morning {name}'

message = greeting('Susan')

print(message)
```

</details>

### Exercise 3

<details><summary>Answer:</summary>

```py
def greeting(name):
    return f'Good morning {name}'

user_input = input('enter your name')

message = greeting(user_input)

print(message)
```

</details>

### Exercise 4

<details><summary>Answer:</summary>

```py
basket = {
    "A4 printer paper" : 4.50,
    "20x ballpoint - black" : 6.00,
    "5x Post-its" : 3.00,
    "10x A4 notepads" : 8.99,
    "3x A4 ringbinders" : 5.99
}

def calc_total(prices):
    # add code to add up product_prices
    total = 0
    for x in prices:
        total += x
    return total

def calc_vat(wholesale):
    # add code to add VAT
    retail = wholesale * 1.2
    return retail

product_prices = [x for x in basket.values()] # use list comprehension to make list of product prices

wholesale_price = calc_total(product_prices) # Pass the correct argument

retail_price = calc_vat(wholesale_price) # Pass the correct argument

print(round(retail_price,2))
```

</details>

### Stretch and Challenge

<details><summary>Answer:</summary>

```py
daily_sales = []

for x in range(1,6):
    value = input('Enter the daily sales total:')
    daily_sales.append(value)

def calc_avg(sales):
    total = 0
    for x in sales:
        total += int(x)
    average = total/len(daily_sales)
    return average

daily_average = calc_avg(daily_sales)

print(daily_average)
```

</details>
