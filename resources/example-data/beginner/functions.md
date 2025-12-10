---
title: "Functions: Reusable Blocks of Code"
description: "Master functions, parameters, return values, scope, and how to write reusable code"
category: "Programming Fundamentals"
tags: ["functions", "programming", "code-reusability", "fundamentals"]
difficulty: "beginner"
---

# Functions: Reusable Blocks of Code

## What is a Function?

A function is a reusable block of code that performs a specific task. Think of it as a recipe that you can follow whenever you need to make that dish.

**Real-world analogy**: A blender
- **Input**: Fruits, ice, milk (parameters)
- **Process**: Blend everything together (function body)
- **Output**: Smoothie (return value)

You can use the same blender (function) with different ingredients (parameters) to make different smoothies!

## Why Use Functions?

### Problem: Repetitive Code
```python
# Without functions - lots of repetition!
print("Hello, Alice!")
print("Welcome to our app!")
print("---")

print("Hello, Bob!")
print("Welcome to our app!")
print("---")

print("Hello, Charlie!")
print("Welcome to our app!")
print("---")
```

### Solution: Functions!
```python
def greet(name):
    print(f"Hello, {name}!")
    print("Welcome to our app!")
    print("---")

greet("Alice")
greet("Bob")
greet("Charlie")
```

**Benefits:**
- Write code once, use it many times
- Easier to read and understand
- Easier to fix bugs (fix in one place)
- Organize code into logical chunks

## Creating Functions

### Python:
```python
def function_name(parameters):
    # code here
    return result
```

### JavaScript:
```javascript
function functionName(parameters) {
    // code here
    return result;
}
```

### Java:
```java
public returnType functionName(parameters) {
    // code here
    return result;
}
```

## Basic Function Example

```python
def add(a, b):
    result = a + b
    return result

# Using the function
sum = add(5, 3)  # sum = 8
total = add(10, 20)  # total = 30
```

**Parts of a function:**
1. **Name**: `add`
2. **Parameters**: `a, b` (inputs)
3. **Body**: The code inside
4. **Return value**: What the function gives back

## Parameters vs Arguments

### Parameters (The Recipe Variables)
The placeholders in the function definition:
```python
def greet(name, age):  # name and age are parameters
    print(f"{name} is {age} years old")
```

### Arguments (The Actual Ingredients)
The actual values you pass:
```python
greet("Alice", 25)  # "Alice" and 25 are arguments
```

**Analogy**:
- **Parameters**: "Add 2 eggs" (recipe instruction)
- **Arguments**: The actual eggs you grab from the fridge

## Types of Parameters

### 1. Required Parameters
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Works
greet()  # Error! Missing required parameter
```

### 2. Default Parameters
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")  # "Hello, Alice!"
greet("Bob", "Hi")  # "Hi, Bob!"
```

### 3. Keyword Arguments
```python
def create_user(name, age, city):
    print(f"{name}, {age}, from {city}")

# Clear and order doesn't matter
create_user(age=25, name="Alice", city="NYC")
```

### 4. Variable Number of Arguments
```python
def sum_all(*numbers):  # * means "any number of arguments"
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
```

## Return Values

### Single Return Value:
```python
def square(x):
    return x * x

result = square(5)  # 25
```

### Multiple Return Values:
```python
def get_user():
    name = "Alice"
    age = 25
    city = "NYC"
    return name, age, city

name, age, city = get_user()
print(name)  # "Alice"
```

### No Return Value:
```python
def say_hello():
    print("Hello!")
    # No return statement

result = say_hello()  # Prints "Hello!"
print(result)  # None
```

## Function Scope

Variables inside functions are **local** - they don't exist outside:

```python
def calculate():
    x = 10  # Local variable
    return x * 2

result = calculate()  # 20
print(x)  # Error! x doesn't exist here
```

**Accessing global variables:**
```python
username = "Alice"  # Global

def greet():
    print(f"Hello, {username}")  # Can read global

def change_name():
    global username  # Need this to modify global
    username = "Bob"

greet()  # "Hello, Alice"
change_name()
greet()  # "Hello, Bob"
```

## Nested Functions

Functions inside functions!

```python
def outer():
    message = "Hello"

    def inner():
        print(message)  # Can access outer function's variables

    inner()  # Call the inner function

outer()  # "Hello"
```

## Lambda Functions (Anonymous Functions)

Short, one-line functions without a name:

```python
# Regular function
def square(x):
    return x * x

# Lambda function
square = lambda x: x * x

# Common use: with map, filter, sort
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x * x, numbers)
# [1, 4, 9, 16, 25]
```

## Recursion (Functions Calling Themselves)

A function that calls itself:

```python
def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)  # Calls itself!

countdown(3)
# Output:
# 3
# 2
# 1
# Blastoff!
```

**Classic example - Factorial:**
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 5 * 4 * 3 * 2 * 1 = 120
```

**Warning**: Recursion can cause stack overflow if not careful!

## Higher-Order Functions

Functions that take other functions as parameters:

```python
def apply_operation(x, y, operation):
    return operation(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = apply_operation(5, 3, add)  # 8
result2 = apply_operation(5, 3, multiply)  # 15
```

## Real-World Examples

### Example 1: Password Validator
```python
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    return True

print(is_valid_password("abc123"))  # False (too short)
print(is_valid_password("abcdefgh"))  # False (no number)
print(is_valid_password("abcdefg1"))  # False (no uppercase)
print(is_valid_password("Abcdefg1"))  # True
```

### Example 2: Temperature Converter
```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(celsius_to_fahrenheit(0))  # 32.0
print(celsius_to_fahrenheit(100))  # 212.0
print(fahrenheit_to_celsius(32))  # 0.0
```

### Example 3: Shopping Cart
```python
def calculate_total(items, tax_rate=0.08):
    subtotal = sum(items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return {
        'subtotal': subtotal,
        'tax': tax,
        'total': total
    }

prices = [29.99, 15.50, 8.99]
result = calculate_total(prices)
print(f"Total: ${result['total']:.2f}")
```

## Function Documentation

Good functions have documentation:

```python
def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Parameters:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters

    Returns:
        float: The calculated BMI

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    return weight_kg / (height_m ** 2)
```

## Function Best Practices

### 1. Do One Thing Well
```python
# Bad - does too much
def process_user(name, email):
    validate_email(email)
    save_to_database(name, email)
    send_welcome_email(email)
    update_statistics()

# Good - separate functions
def validate_email(email):
    # validation logic

def save_user(name, email):
    # save logic

def send_welcome_email(email):
    # email logic
```

### 2. Use Descriptive Names
```python
# Bad
def calc(x, y):
    return x + y

# Good
def calculate_total_price(item_price, quantity):
    return item_price * quantity
```

### 3. Keep Functions Short
If a function is more than 20-30 lines, consider breaking it up.

### 4. Avoid Side Effects
```python
# Bad - modifies global state
total = 0

def add_to_total(x):
    global total
    total += x

# Good - pure function
def add(a, b):
    return a + b

total = add(total, 5)
```

### 5. Use Default Parameters Wisely
```python
# Good use of defaults
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Bad - mutable default (common pitfall!)
def add_item(item, items=[]):  # Don't do this!
    items.append(item)
    return items

# Better
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## Common Function Patterns

### 1. Guard Clauses (Early Returns)
```python
def process_user(user):
    if not user:
        return None
    if not user.is_active:
        return None
    if not user.email:
        return None

    # Main logic here
    return process_active_user(user)
```

### 2. Function Factories
```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

times_two = make_multiplier(2)
times_three = make_multiplier(3)

print(times_two(5))  # 10
print(times_three(5))  # 15
```

### 3. Decorators (Python)
```python
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello"

print(greet())  # "HELLO"
```

## Testing Functions

Functions are easy to test:

```python
def add(a, b):
    return a + b

# Test cases
assert add(2, 3) == 5
assert add(0, 0) == 0
assert add(-1, 1) == 0
assert add(100, 200) == 300

print("All tests passed!")
```

## The Bottom Line

Functions are the building blocks of organized code. They:

- **Reuse code**: Write once, use many times
- **Organize**: Break complex problems into simple pieces
- **Abstract**: Hide complexity behind a simple interface
- **Test**: Easy to test individual pieces
- **Maintain**: Fix bugs in one place

Think of functions as:
- **Recipes** in a cookbook
- **Tools** in a toolbox
- **Verbs** in a sentence

Master functions, and you'll write cleaner, more maintainable code!
