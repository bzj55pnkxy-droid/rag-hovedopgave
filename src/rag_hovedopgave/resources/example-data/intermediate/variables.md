---
title: "Variables: Boxes for Storing Information"
description: "Learn about variables, data types, scope, naming conventions, and variable best practices"
category: "Programming Fundamentals"
tags: ["variables", "data-types", "programming", "fundamentals", "basics"]
difficulty: "intermediate"
---

# Variables: Boxes for Storing Information

## What is a Variable?

A variable is like a labeled box where you can store information and give it a name.

Imagine you have a box:
- You write "AGE" on it
- You put the number "25" inside
- Now whenever you need to know the age, you look in the AGE box!

That's exactly what variables do in programming.

## Creating Variables

### Python:
```python
name = "Alice"
age = 25
is_student = True
```

### JavaScript:
```javascript
let name = "Alice";
let age = 25;
let isStudent = true;
```

### Java:
```java
String name = "Alice";
int age = 25;
boolean isStudent = true;
```

## Why Use Variables?

### Without Variables (Bad):
```python
print("Hello, Alice!")
print("Alice is 25 years old")
print("Alice lives in New York")

# If name changes, update 3 places!
```

### With Variables (Good):
```python
name = "Alice"
age = 25
city = "New York"

print(f"Hello, {name}!")
print(f"{name} is {age} years old")
print(f"{name} lives in {city}")

# Change name once, updates everywhere!
```

## Variable Names (Identifiers)

### Good Names (Descriptive):
```python
user_age = 25
total_price = 99.99
is_logged_in = True
```

### Bad Names (Confusing):
```python
a = 25
x = 99.99
flag = True
```

### Naming Rules:

**Can use:**
- Letters (a-z, A-Z)
- Numbers (but not at the start)
- Underscores (_)

**Cannot use:**
- Spaces
- Special characters (@, #, $, etc.)
- Reserved words (if, for, while, etc.)

```python
# Valid names
user_name = "Bob"
user1 = "Alice"
_private = 42

# Invalid names
user-name = "Bob"    # No hyphens!
2nd_place = "Alice"  # Can't start with number!
for = 42             # "for" is a keyword!
```

### Naming Conventions:

**snake_case (Python):**
```python
user_name = "Alice"
total_price = 100
```

**camelCase (JavaScript):**
```javascript
let userName = "Alice";
let totalPrice = 100;
```

**PascalCase (Classes):**
```python
class UserAccount:
    pass
```

**SCREAMING_SNAKE_CASE (Constants):**
```python
MAX_USERS = 100
API_KEY = "abc123"
```

## Data Types

Variables can store different types of information:

### 1. Numbers

**Integers (whole numbers):**
```python
age = 25
score = 100
temperature = -5
```

**Floats (decimals):**
```python
price = 19.99
temperature = 98.6
pi = 3.14159
```

### 2. Strings (Text)

```python
name = "Alice"
greeting = "Hello, World!"
address = "123 Main St"
```

**String operations:**
```python
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name  # "Alice Smith"

message = "Hello"
repeated = message * 3  # "HelloHelloHello"

text = "Python Programming"
length = len(text)  # 18
```

### 3. Booleans (True/False)

```python
is_sunny = True
has_license = False
is_adult = age >= 18  # True if age is 18 or more
```

### 4. None/Null (Nothing)

```python
middle_name = None  # No value
result = None       # Not calculated yet
```

## Variable Assignment

### Simple Assignment:
```python
x = 5
```

### Multiple Assignment:
```python
x, y, z = 1, 2, 3
# x=1, y=2, z=3
```

### Same Value:
```python
a = b = c = 0
# All equal to 0
```

### Swapping:
```python
a = 5
b = 10
a, b = b, a  # Swap!
# Now a=10, b=5
```

## Variable Scope

Scope determines where a variable can be used.

### Global Scope (Everywhere):
```python
username = "Alice"  # Global

def greet():
    print(username)  # Can access global

def update():
    global username
    username = "Bob"  # Can modify global

greet()  # "Alice"
update()
greet()  # "Bob"
```

### Local Scope (Inside Function):
```python
def calculate():
    result = 10 + 5  # Local to this function
    return result

print(result)  # Error! result doesn't exist here
```

### Block Scope (Inside Blocks):
```javascript
if (true) {
    let x = 5;  // Only exists in this block
}
console.log(x);  // Error! x doesn't exist here
```

**Real-world analogy:**
- **Global**: Announcement on school PA system (everyone hears it)
- **Local**: Conversation in a classroom (only that class hears it)
- **Block**: Whispering in a group (only the group hears it)

## Mutable vs Immutable

### Immutable (Can't Change):
```python
name = "Alice"
# Strings are immutable - this creates a NEW string
name = "Bob"
```

### Mutable (Can Change):
```python
scores = [85, 90, 95]
# Lists are mutable - this changes the SAME list
scores[0] = 100  # [100, 90, 95]
scores.append(88)  # [100, 90, 95, 88]
```

## Constants

Variables that shouldn't change:

```python
# Python (convention only, not enforced)
PI = 3.14159
MAX_USERS = 100

# JavaScript (enforced)
const PI = 3.14159;
// PI = 3; // Error! Can't change const
```

## Variable Operations

### Arithmetic:
```python
x = 10
y = 3

sum = x + y        # 13
difference = x - y # 7
product = x * y    # 30
quotient = x / y   # 3.333...
remainder = x % y  # 1
power = x ** y     # 1000
```

### Compound Assignment:
```python
x = 10
x = x + 5  # Old way
x += 5     # New way (same thing)

# Works with all operators
x -= 3  # x = x - 3
x *= 2  # x = x * 2
x /= 4  # x = x / 4
```

### Increment/Decrement:
```python
count = 0
count += 1  # Increment
count -= 1  # Decrement
```

## Type Conversion

### Explicit Conversion:
```python
# String to integer
age_string = "25"
age_number = int(age_string)  # 25

# Integer to string
score = 100
score_string = str(score)  # "100"

# String to float
price = float("19.99")  # 19.99
```

### Implicit Conversion (Automatic):
```python
x = 5      # int
y = 2.0    # float
z = x + y  # 7.0 (float) - int converted to float
```

## Variable Best Practices

### 1. Use Descriptive Names
```python
# Bad
x = 25
y = "New York"

# Good
user_age = 25
user_city = "New York"
```

### 2. Initialize Variables
```python
# Bad
if condition:
    result = calculate()
print(result)  # Might not exist!

# Good
result = None
if condition:
    result = calculate()
if result:
    print(result)
```

### 3. Don't Reuse Variables for Different Purposes
```python
# Bad
temp = calculate_total()
print(temp)
temp = get_user_name()  # Confusing!
print(temp)

# Good
total = calculate_total()
print(total)
username = get_user_name()
print(username)
```

### 4. Use Constants for Fixed Values
```python
# Bad
if age >= 18:  # Magic number!
    allow_entry()

# Good
LEGAL_AGE = 18
if age >= LEGAL_AGE:
    allow_entry()
```

## Common Mistakes

### Mistake 1: Undefined Variable
```python
print(username)  # Error! username not defined yet
username = "Alice"
```

### Mistake 2: Typos
```python
user_name = "Alice"
print(user_nane)  # Error! Typo in variable name
```

### Mistake 3: Reserved Keywords
```python
class = "Math"  # Error! "class" is a keyword
```

### Mistake 4: Type Errors
```python
age = "25"  # String, not number
next_year = age + 1  # Error! Can't add string and number
```

## Variables in Different Languages

### Python (Dynamic Typing):
```python
x = 5        # x is an integer
x = "hello"  # Now x is a string - totally fine!
```

### Java (Static Typing):
```java
int x = 5;
x = "hello";  // Error! x is an integer, can't hold string
```

### TypeScript (Optional Typing):
```typescript
let x: number = 5;
x = "hello";  // Error! Type checking catches this

let y = 5;   // Type inferred as number
y = "hello";  // Error! Can't change type
```

## Real-World Example

```python
# Shopping cart calculator
item_price = 29.99
quantity = 3
tax_rate = 0.08

# Calculate subtotal
subtotal = item_price * quantity  # 89.97

# Calculate tax
tax = subtotal * tax_rate  # 7.20

# Calculate total
total = subtotal + tax  # 97.17

# Apply discount if over $50
discount = 0
if subtotal > 50:
    discount = subtotal * 0.10  # 10% off
    total = total - discount

# Display results
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Total: ${total:.2f}")
```

## The Bottom Line

Variables are the fundamental building blocks of programming. They:

- Store information with meaningful names
- Can be updated as your program runs
- Come in different types (numbers, text, booleans)
- Have scope (where they can be used)
- Make code readable and maintainable

Think of variables as labeled boxes:
- The label is the variable name
- The contents are the value
- The type of box determines what you can store
- The box's location determines who can access it

Master variables, and you've taken your first big step in programming!
