# Arrays - Week 6

*Prerequisites: Week 3 - Loops, Week 4 - Methods Part 1, Week 5 - Methods Part 2*
*Phase: Phase 2: Decomposition and Abstraction*

---

## What You'll Learn

By the end of this week, you will be able to:

- **Understand what an array is** and why we need collections of data
- **Create and initialize arrays** using different approaches
- **Access and modify elements** using index-based notation
- **Traverse arrays with loops** using both traditional for loops and for-each loops
- **Implement common array operations** such as sum, average, min/max, and counting
- **Search for elements** by value or condition
- **Understand array references** versus copying values
- **Use arrays with methods** - passing arrays to methods and returning arrays
- **Handle ArrayIndexOutOfBoundsException** and prevent it proactively
- **Use the Random class** to generate pseudo-random numbers for array population

This week introduces your first **complex data structure** - the array. Up until now, every piece of data you have worked with has been stored in a single variable: one `int` for a number, one `String` for text, one `boolean` for a true/false value. But what if you need to store 100 student grades? 1,000 temperatures? 10,000 product prices? Creating 100 separate variables would be impractical and impossible to manage. Arrays solve this problem elegantly.

---

## Why This Matters

Every real-world application deals with collections of data. Consider these everyday scenarios:

- **A gradebook app** stores grades for 30 students. Without arrays, you would need `grade1`, `grade2`, `grade3`... up to `grade30`. With arrays, you use `grades[0]` through `grades[29]`.

- **A music player** manages a playlist of songs. Each song is an item in an array. You can shuffle, sort, add, or remove songs by working with array operations.

- **A weather app** tracks temperatures for each day of the week. Seven values stored in one structure: `temperatures[0]` for Sunday through `temperatures[6]` for Saturday.

- **A shopping cart** holds the items a customer wants to purchase. Adding to cart? Add to the array. Removing an item? Remove from the array.

- **A game leaderboard** stores the top 10 high scores. Arrays make it easy to sort, display, and update the rankings.

Arrays are fundamental to programming because data naturally comes in groups. Learning to work with arrays unlocks your ability to handle realistic amounts of data. The skills you develop this week - traversing, searching, calculating aggregates - are patterns you will use throughout your programming career.

Furthermore, arrays are the foundation for understanding more complex data structures you will encounter later, including `ArrayList` (Week 8), object collections, and eventually databases and files.

---

## Building Your Intuition

### The Big Picture: From Single Values to Collections

Until now, you have worked with individual variables - like having individual sticky notes, each holding one piece of information. An array is like a **notebook** - multiple pages bound together, where each page holds one piece of information but they all belong together as a unit.

| Week 1-5 Approach | Week 6 Approach (Arrays) |
|-------------------|-------------------------|
| `int score1 = 85;` | `int[] scores = new int[30];` |
| `int score2 = 92;` | `scores[0] = 85;` |
| `int score3 = 78;` | `scores[1] = 92;` |
| ... 27 more variables ... | `scores[2] = 78;` |
| Unmanageable! | Clean and organized |

### The Row of Mailboxes Analogy

Imagine a row of mailboxes at an apartment building:

```
+-----+-----+-----+-----+-----+-----+-----+-----+
|  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |
+-----+-----+-----+-----+-----+-----+-----+-----+
| 85  | 92  | 78  | 95  | 88  | 73  | 91  | 84  |
+-----+-----+-----+-----+-----+-----+-----+-----+
```

Key observations:

1. **Each mailbox has a number** (the index). Mailbox numbers start at **0**, not 1. This is critical!
2. **Each mailbox holds one piece of mail** (the value stored at that index)
3. **All mailboxes are the same size** (all elements have the same type)
4. **The total number of mailboxes is fixed** when the row is built (array length is fixed)
5. **You access a specific mailbox by its number**: "Give me what is in mailbox 3"

This is exactly how arrays work in Java!

### The Train Analogy

Think of an array as a train:

- The **train** is the array itself - one unified structure
- Each **train car** is a slot in the array
- Each car has a **car number** starting from 0 (the index)
- Each car **carries one passenger or cargo item** (the value)
- The **number of cars is decided when the train is built** (fixed length)
- You can visit any car by its number: "Take me to car 5"

### The Egg Carton Analogy

A dozen eggs in a carton:

- The carton holds exactly 12 eggs (fixed size)
- Each position is numbered 0-11 (not 1-12!)
- You can put an egg in position 3, check position 7, or take the egg from position 0
- All positions hold the same thing: eggs (same type)

These physical analogies help you visualize what Java does with arrays in memory.

---

## Understanding What Is an Array

### What Is It?

An **array** is a fixed-size, ordered collection of elements that are all the same type. Once created, an array's size cannot change.

Think of it as: **"A numbered list where every item is the same type of thing, and the list size never changes."**

### Why Do We Need Arrays?

Consider tracking grades for a class of 30 students:

**Without arrays (nightmare):**

```java
int grade1 = 85;
int grade2 = 92;
int grade3 = 78;
// ... 27 more lines ...
int grade30 = 81;

// To calculate average, you need:
int sum = grade1 + grade2 + grade3 + ... + grade30;  // Impossible to maintain!
```

**With arrays (elegant):**

```java
int[] grades = new int[30];

// To calculate average, use a loop:
int sum = 0;
for (int i = 0; i < grades.length; i++) {
    sum += grades[i];
}
double average = (double) sum / grades.length;
```

Arrays enable:

1. **Scalability** - Easily handle 10, 100, or 10,000 elements
2. **Loop processing** - Process all elements with a simple loop
3. **Organization** - Related data stays together
4. **Algorithms** - Enable searching, sorting, and other operations

### Key Characteristics of Arrays

| Characteristic | Meaning |
|----------------|---------|
| Fixed size | Once created, length cannot change |
| Same type | All elements must be the same data type |
| Zero-indexed | First element is at index 0, not 1 |
| Ordered | Elements maintain their position |
| Direct access | Any element can be accessed instantly by index |

---

## Understanding Array Declaration and Initialization

### What Does This Mean?

**Declaration** tells Java that a variable will hold an array of a certain type.
**Initialization** actually creates the array with a specific size.

### The Three Ways to Create Arrays

**Way 1: Declare and initialize separately**

```java
// Step 1: Declare (variable exists but points to nothing yet)
int[] numbers;

// Step 2: Initialize (create the actual array)
numbers = new int[5];  // Creates array with 5 slots, all containing 0
```

**Way 2: Declare and initialize together**

```java
int[] numbers = new int[5];  // Creates array with 5 slots, all containing 0
```

**Way 3: Declare and initialize with values**

```java
int[] numbers = {85, 92, 78, 95, 88};  // Creates array with these 5 values
```

### Understanding Default Values

When you create an array with `new`, Java fills it with default values:

| Array Type | Default Value |
|-----------|---------------|
| `int[]` | 0 |
| `double[]` | 0.0 |
| `boolean[]` | false |
| `String[]` | null |
| Any object type | null |

```java
int[] numbers = new int[5];
// numbers now contains: [0, 0, 0, 0, 0]

double[] prices = new double[3];
// prices now contains: [0.0, 0.0, 0.0]

boolean[] flags = new boolean[4];
// flags now contains: [false, false, false, false]

String[] names = new String[3];
// names now contains: [null, null, null]
```

### Seeing Array Creation in Action

```java
// Creating an array of test scores
int[] scores = new int[5];          // [0, 0, 0, 0, 0]

// Creating an array with initial values
int[] scores2 = {85, 92, 78, 95, 88};  // [85, 92, 78, 95, 88]

// Creating an array of names
String[] students = new String[3];     // [null, null, null]

// Creating with initial values
String[] students2 = {"Alice", "Bob", "Carol"};
```

### Common Mistakes with Array Creation

**Mistake 1: Forgetting to initialize**

```java
int[] numbers;              // Declared but not initialized
numbers[0] = 5;             // ERROR! NullPointerException - array does not exist yet

// Fix:
int[] numbers = new int[10];  // Now it exists
numbers[0] = 5;               // Works!
```

**Mistake 2: Mixing declaration styles**

```java
// WRONG: Cannot use {} initialization after separate declaration
int[] numbers;
numbers = {1, 2, 3};         // ERROR!

// Fix: Use new with {}
int[] numbers;
numbers = new int[]{1, 2, 3};  // Works!

// Or declare and initialize together:
int[] numbers = {1, 2, 3};     // Best approach
```

---

## Understanding Zero-Based Indexing

### What Is Zero-Based Indexing?

In Java (and most programming languages), array indices start at **0**, not 1.

- The **first** element is at index **0**
- The **second** element is at index **1**
- The **third** element is at index **2**
- And so on...

### Why Does This Confuse Beginners?

In everyday life, we count starting from 1:

- "The first day of the month is the 1st"
- "The first place winner"
- "Page 1 of the book"

But in programming, we count from 0:

- "The first element is at index 0"
- "The first character of a String is at position 0"

This is called **zero-based indexing** or **zero-indexing**.

### Why Zero-Based? (Brief History)

Zero-based indexing exists for efficiency in how computers access memory. The index represents an **offset** from the starting address. The first element has an offset of 0 (it IS at the starting address). While you do not need to understand memory addressing, understanding that "0 means no offset from the start" helps the concept make sense.

### Visualizing Zero-Based Indexing

```
Array: int[] scores = {85, 92, 78, 95, 88};

Index:    0     1     2     3     4
        +-----+-----+-----+-----+-----+
Values: |  85 |  92 |  78 |  95 |  88 |
        +-----+-----+-----+-----+-----+

scores[0] = 85  (FIRST element)
scores[1] = 92  (SECOND element)
scores[2] = 78  (THIRD element)
scores[3] = 95  (FOURTH element)
scores[4] = 88  (FIFTH element, also the LAST element)

Length: 5 elements
Valid indices: 0, 1, 2, 3, 4
Highest valid index: length - 1 = 4
```

### The Critical Formula

**Last valid index = length - 1**

This is the most important formula to remember! If an array has 5 elements:

- Valid indices: 0, 1, 2, 3, 4
- Invalid indices: 5 (and higher)

If an array has 100 elements:

- Valid indices: 0 to 99
- Invalid index: 100 (and higher)

### Common Mistakes with Zero-Based Indexing

**Mistake 1: Accessing index equal to length**

```java
int[] numbers = {10, 20, 30, 40, 50};  // Length is 5
System.out.println(numbers[5]);         // ERROR! Index 5 does not exist!
// Valid indices are 0, 1, 2, 3, 4

// Fix: Remember last valid index is length - 1
System.out.println(numbers[4]);         // Prints 50 (the last element)
```

**Mistake 2: Thinking index 1 is the first element**

```java
String[] names = {"Alice", "Bob", "Carol"};
System.out.println("First student: " + names[1]);  // WRONG! Prints "Bob"

// Fix: Index 0 is the first element
System.out.println("First student: " + names[0]);  // Correct! Prints "Alice"
```

**Mistake 3: Off-by-one in loops (covered in detail later)**

```java
// WRONG: Goes one index too far
for (int i = 0; i <= numbers.length; i++) {  // <= instead of <
    System.out.println(numbers[i]);           // Crashes on last iteration!
}

// CORRECT: Stop BEFORE length
for (int i = 0; i < numbers.length; i++) {   // < not <=
    System.out.println(numbers[i]);
}
```

---

## Understanding Accessing and Modifying Elements

### What Does Access Mean?

**Accessing** (or reading) an element means getting the value stored at a specific index.
**Modifying** (or writing) an element means changing the value stored at a specific index.

Both use the **square bracket notation**: `arrayName[index]`

### How to Access Elements

```java
int[] scores = {85, 92, 78, 95, 88};

// Reading/accessing elements
int firstScore = scores[0];    // firstScore = 85
int thirdScore = scores[2];    // thirdScore = 78
int lastScore = scores[4];     // lastScore = 88

// Using in expressions
int total = scores[0] + scores[1];  // total = 177
double oneScore = scores[2] * 1.1;  // oneScore = 85.8

// Printing directly
System.out.println(scores[0]);      // Prints 85
System.out.println("Third score: " + scores[2]);  // Prints "Third score: 78"
```

### How to Modify Elements

```java
int[] scores = {85, 92, 78, 95, 88};

// Before: [85, 92, 78, 95, 88]

scores[0] = 90;          // Change first element
scores[2] = 82;          // Change third element
scores[4] = scores[4] + 5;  // Increase last element by 5

// After: [90, 92, 82, 95, 93]
```

### Dynamic Index Access

The index can be a variable or expression, not just a literal number:

```java
int[] scores = {85, 92, 78, 95, 88};

int i = 2;
System.out.println(scores[i]);       // Prints 78 (value at index 2)

// Index can be calculated
System.out.println(scores[i + 1]);   // Prints 95 (value at index 3)

// Index can come from user input
Scanner scanner = new Scanner(System.in);
System.out.print("Which score to view (0-4)? ");
int choice = scanner.nextInt();
System.out.println("Score: " + scores[choice]);
```

### Common Mistakes with Element Access

**Mistake 1: Negative index**

```java
int[] numbers = {10, 20, 30};
System.out.println(numbers[-1]);  // ERROR! Negative indices are invalid
```

**Mistake 2: Confusing value and index**

```java
int[] values = {100, 200, 300};

// values[1] is 200 (the value at index 1)
// This is NOT "the position where 100 is stored"

// To find WHERE 100 is stored, you need to search (covered later)
```

---

## Understanding the Length Property

### What Is the Length Property?

Every array has a **length** property that tells you how many elements it contains. Access it using `arrayName.length` (no parentheses - it is a property, not a method).

### Why Is Length Important?

Length is critical for:

1. **Loop boundaries** - knowing when to stop
2. **Validating indices** - checking if an index is valid
3. **Calculations** - computing averages, finding last element

### Using the Length Property

```java
int[] scores = {85, 92, 78, 95, 88};

System.out.println(scores.length);  // Prints 5

// Calculate average
double average = (double) sum / scores.length;

// Access last element
int lastScore = scores[scores.length - 1];  // Index 4, value 88

// Check if index is valid
int requestedIndex = 7;
if (requestedIndex >= 0 && requestedIndex < scores.length) {
    System.out.println(scores[requestedIndex]);
} else {
    System.out.println("Invalid index!");
}
```

### Length vs Last Valid Index

This is critical to understand:

| Concept | Array with 5 elements |
|---------|----------------------|
| `length` | 5 |
| First valid index | 0 |
| Last valid index | 4 (which is `length - 1`) |
| Invalid index (out of bounds) | 5 or higher |

```java
int[] numbers = {10, 20, 30, 40, 50};

// length is 5
// BUT the indices are 0, 1, 2, 3, 4
// There is NO index 5!

numbers[numbers.length];      // ERROR! Index 5 does not exist
numbers[numbers.length - 1];  // CORRECT! Accesses index 4
```

### Common Mistake: length() vs length

```java
String text = "Hello";
int stringLength = text.length();   // Strings use length() METHOD with ()

int[] numbers = {1, 2, 3};
int arrayLength = numbers.length;   // Arrays use length PROPERTY without ()

// Mixing them up causes errors:
// numbers.length()  <- ERROR! Arrays do not have length() method
// text.length       <- ERROR! Strings do not have length property
```

---

## Understanding ArrayIndexOutOfBoundsException

### What Is This Exception?

`ArrayIndexOutOfBoundsException` is a runtime error that occurs when you try to access an array index that does not exist.

### Why Does This Happen?

Common causes:

1. **Using index equal to length** (most common)
2. **Using negative index**
3. **Loop going one step too far**
4. **Incorrect calculation of index**

### Seeing the Exception

```java
int[] numbers = {10, 20, 30};  // Valid indices: 0, 1, 2

// These cause ArrayIndexOutOfBoundsException:
System.out.println(numbers[3]);   // Index 3 out of bounds for length 3
System.out.println(numbers[-1]);  // Index -1 out of bounds for length 3
System.out.println(numbers[100]); // Index 100 out of bounds for length 3
```

The error message tells you exactly what went wrong:

```
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 5
    at MyProgram.main(MyProgram.java:7)
```

Translation: "You tried to access index 5, but valid indices are only 0-4 (length is 5)"

### How to Prevent This Exception

**Prevention 1: Always use < length in loops (never <=)**

```java
// WRONG (will crash on last iteration)
for (int i = 0; i <= numbers.length; i++) { ... }

// CORRECT
for (int i = 0; i < numbers.length; i++) { ... }
```

**Prevention 2: Validate indices before use**

```java
public static int getElement(int[] array, int index) {
    // Validate first
    if (index < 0 || index >= array.length) {
        System.out.println("Invalid index: " + index);
        return -1;  // or throw exception, or handle differently
    }
    return array[index];
}
```

**Prevention 3: Use for-each loops when you do not need the index**

```java
// Traditional loop - risk of index errors
for (int i = 0; i < numbers.length; i++) {
    System.out.println(numbers[i]);
}

// For-each loop - no index to mess up
for (int number : numbers) {
    System.out.println(number);
}
```

**Prevention 4: Be careful with calculated indices**

```java
int[] numbers = {10, 20, 30, 40, 50};
int middle = numbers.length / 2;  // 2 (correct middle index)
int last = numbers.length - 1;    // 4 (correct last index)

// Dangerous: user-provided index
int userIndex = scanner.nextInt();
if (userIndex >= 0 && userIndex < numbers.length) {
    System.out.println(numbers[userIndex]);
} else {
    System.out.println("Please enter a valid index (0 to " + (numbers.length - 1) + ")");
}
```

---

## Understanding Array Traversal with Loops

### What Is Array Traversal?

**Traversal** means visiting every element in an array, usually to perform some operation on each element. This is where your loop skills from Week 3 become essential!

### Why Traversal Matters

Almost every array operation requires traversal:

- Printing all elements
- Calculating sum or average
- Finding maximum or minimum
- Searching for a value
- Counting occurrences
- Transforming values

### The Traditional For Loop Approach

Use a traditional `for` loop when you **need the index**:

```java
int[] scores = {85, 92, 78, 95, 88};

// Print all elements with their indices
for (int i = 0; i < scores.length; i++) {
    System.out.println("Index " + i + ": " + scores[i]);
}

// Output:
// Index 0: 85
// Index 1: 92
// Index 2: 78
// Index 3: 95
// Index 4: 88
```

**When to use traditional for loop:**

- You need to know the current index
- You need to modify elements
- You need to traverse in reverse
- You need to skip elements
- You need to access multiple arrays at once

### The For-Each Loop Approach

The **for-each loop** (also called enhanced for loop) is simpler when you just need the values:

```java
int[] scores = {85, 92, 78, 95, 88};

// Print all elements (no index needed)
for (int score : scores) {
    System.out.println(score);
}

// Output:
// 85
// 92
// 78
// 95
// 88
```

**Read it as:** "For each score in scores, do..."

**When to use for-each loop:**

- You only need the values, not the indices
- You do not need to modify the array
- You want simpler, cleaner code

### Comparing the Two Approaches

```java
int[] numbers = {10, 20, 30, 40, 50};

// Traditional for loop
System.out.println("Using traditional for loop:");
for (int i = 0; i < numbers.length; i++) {
    System.out.println("numbers[" + i + "] = " + numbers[i]);
}

// For-each loop
System.out.println("\nUsing for-each loop:");
for (int num : numbers) {
    System.out.println(num);
}
```

### Common Traversal Patterns

**Pattern 1: Calculate sum**

```java
int[] values = {10, 20, 30, 40, 50};

// Using for-each (cleaner when you don't need index)
int sum = 0;
for (int value : values) {
    sum += value;
}
System.out.println("Sum: " + sum);  // Sum: 150
```

**Pattern 2: Calculate average**

```java
int[] scores = {85, 92, 78, 95, 88};

int sum = 0;
for (int score : scores) {
    sum += score;
}
double average = (double) sum / scores.length;
System.out.println("Average: " + average);  // Average: 87.6
```

**Pattern 3: Find maximum**

```java
int[] numbers = {45, 23, 78, 12, 96, 34};

int max = numbers[0];  // Start by assuming first element is max
for (int i = 1; i < numbers.length; i++) {  // Start at 1, already have 0
    if (numbers[i] > max) {
        max = numbers[i];
    }
}
System.out.println("Maximum: " + max);  // Maximum: 96
```

**Pattern 4: Find minimum**

```java
int[] numbers = {45, 23, 78, 12, 96, 34};

int min = numbers[0];
for (int num : numbers) {
    if (num < min) {
        min = num;
    }
}
System.out.println("Minimum: " + min);  // Minimum: 12
```

**Pattern 5: Count occurrences**

```java
int[] numbers = {1, 5, 3, 5, 7, 5, 2};
int target = 5;

int count = 0;
for (int num : numbers) {
    if (num == target) {
        count++;
    }
}
System.out.println("Number of 5s: " + count);  // Number of 5s: 3
```

### When You Cannot Use For-Each

**Modifying array elements:**

```java
int[] numbers = {1, 2, 3, 4, 5};

// This does NOT modify the array!
for (int num : numbers) {
    num = num * 2;  // Only modifies the local variable, not the array
}
// numbers is still: [1, 2, 3, 4, 5]

// To modify, use traditional for loop:
for (int i = 0; i < numbers.length; i++) {
    numbers[i] = numbers[i] * 2;  // Actually modifies the array
}
// numbers is now: [2, 4, 6, 8, 10]
```

**Traversing in reverse:**

```java
int[] numbers = {1, 2, 3, 4, 5};

// Print in reverse order
for (int i = numbers.length - 1; i >= 0; i--) {
    System.out.println(numbers[i]);
}
// Output: 5, 4, 3, 2, 1
```

---

## Understanding Common Array Operations

### Searching for an Element

**Linear search** checks each element until finding a match:

```java
public static int findIndex(int[] array, int target) {
    for (int i = 0; i < array.length; i++) {
        if (array[i] == target) {
            return i;  // Found it! Return the index
        }
    }
    return -1;  // Not found (convention: -1 means "not present")
}

// Usage:
int[] numbers = {45, 23, 78, 12, 96, 34};
int index = findIndex(numbers, 78);
if (index != -1) {
    System.out.println("Found 78 at index " + index);  // Found 78 at index 2
} else {
    System.out.println("78 not found");
}
```

### Finding First and Last Elements

```java
int[] scores = {85, 92, 78, 95, 88};

int first = scores[0];                    // First element: 85
int last = scores[scores.length - 1];     // Last element: 88

System.out.println("First: " + first);    // First: 85
System.out.println("Last: " + last);      // Last: 88
```

### Checking if Element Exists

```java
public static boolean contains(int[] array, int target) {
    for (int value : array) {
        if (value == target) {
            return true;
        }
    }
    return false;
}

// Usage:
int[] numbers = {10, 20, 30, 40, 50};
boolean hasThirty = contains(numbers, 30);     // true
boolean hasSixty = contains(numbers, 60);      // false
```

### Printing Array Contents

Java arrays do not have a nice built-in print format. If you print directly:

```java
int[] numbers = {1, 2, 3, 4, 5};
System.out.println(numbers);  // Prints something like: [I@15db9742 (not useful!)
```

**Better ways to print:**

```java
// Using a loop
for (int num : numbers) {
    System.out.print(num + " ");
}
System.out.println();  // Output: 1 2 3 4 5

// Using Arrays.toString (requires import java.util.Arrays)
import java.util.Arrays;
System.out.println(Arrays.toString(numbers));  // Output: [1, 2, 3, 4, 5]
```

---

## Understanding Arrays and Methods

### Passing Arrays to Methods

Arrays can be passed to methods just like other values. When you pass an array, you pass a **reference** to the array (more on this later).

```java
public class ArrayMethods {

    public static void main(String[] args) {
        int[] scores = {85, 92, 78, 95, 88};

        printArray(scores);                        // Pass array to method
        System.out.println("Sum: " + sum(scores)); // Pass and get result
        System.out.println("Average: " + average(scores));
    }

    // Method that receives an array
    public static void printArray(int[] array) {
        System.out.print("Array: ");
        for (int value : array) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    // Method that returns a value calculated from array
    public static int sum(int[] array) {
        int total = 0;
        for (int value : array) {
            total += value;
        }
        return total;
    }

    // Another calculation method
    public static double average(int[] array) {
        return (double) sum(array) / array.length;
    }
}
```

### Returning Arrays from Methods

Methods can also **return** arrays:

```java
// Method that creates and returns an array
public static int[] createSequence(int length) {
    int[] result = new int[length];
    for (int i = 0; i < length; i++) {
        result[i] = i + 1;  // 1, 2, 3, ...
    }
    return result;
}

// Usage:
int[] sequence = createSequence(5);  // [1, 2, 3, 4, 5]
```

### Methods Modifying Arrays

When a method receives an array, it can modify the original array (because it receives a reference):

```java
public static void doubleAll(int[] array) {
    for (int i = 0; i < array.length; i++) {
        array[i] = array[i] * 2;  // Modifies the original array!
    }
}

// Usage:
int[] numbers = {1, 2, 3, 4, 5};
System.out.println("Before: " + Arrays.toString(numbers));  // [1, 2, 3, 4, 5]

doubleAll(numbers);

System.out.println("After: " + Arrays.toString(numbers));   // [2, 4, 6, 8, 10]
```

This is different from primitive types! When you pass an `int` to a method, the method gets a copy. When you pass an `int[]`, the method gets access to the same array.

---

## Understanding Array References and Copying

### What Is a Reference?

When you create an array, Java stores the array data somewhere in memory. The variable holds a **reference** (like an address) to that data, not the data itself.

Think of it like a house address:

- The house is the actual array data
- The address (stored in the variable) tells you where to find the house
- You can have multiple addresses (variables) pointing to the same house

### Assignment Does Not Copy Arrays

```java
int[] original = {1, 2, 3, 4, 5};
int[] copy = original;  // This does NOT copy the array!

// Both variables point to the SAME array
copy[0] = 999;

System.out.println(original[0]);  // Prints 999! original was changed too!
```

Visualized:

```
BEFORE: copy = original;

original  -----> [1, 2, 3, 4, 5]


AFTER: copy = original;

original  -----+
               |---> [1, 2, 3, 4, 5]   (SAME array!)
copy      -----+


AFTER: copy[0] = 999;

original  -----+
               |---> [999, 2, 3, 4, 5]   (Both see the change!)
copy      -----+
```

### How to Actually Copy an Array

**Method 1: Manual copy with loop**

```java
int[] original = {1, 2, 3, 4, 5};
int[] copy = new int[original.length];

for (int i = 0; i < original.length; i++) {
    copy[i] = original[i];
}

// Now they are independent
copy[0] = 999;
System.out.println(original[0]);  // Still 1! original unchanged
```

**Method 2: Using Arrays.copyOf (recommended)**

```java
import java.util.Arrays;

int[] original = {1, 2, 3, 4, 5};
int[] copy = Arrays.copyOf(original, original.length);

copy[0] = 999;
System.out.println(original[0]);  // Still 1!
```

**Method 3: Using clone()**

```java
int[] original = {1, 2, 3, 4, 5};
int[] copy = original.clone();

copy[0] = 999;
System.out.println(original[0]);  // Still 1!
```

### Why This Matters

Understanding references is crucial because:

1. **Method calls** - Arrays passed to methods can be modified by the method
2. **Assignment** - Simple assignment creates aliases, not copies
3. **Comparisons** - `==` compares references, not contents

```java
int[] a = {1, 2, 3};
int[] b = {1, 2, 3};
int[] c = a;

System.out.println(a == b);  // false! Different arrays (same contents, different references)
System.out.println(a == c);  // true! Same array (c points to a's array)

// To compare contents:
System.out.println(Arrays.equals(a, b));  // true! Same contents
```

---

## Understanding the Random Class

### What Is the Random Class?

The `Random` class generates **pseudo-random numbers** - numbers that appear random but are actually generated by a mathematical formula. This is useful for:

- Simulating dice rolls
- Creating random test data
- Populating arrays with random values
- Game development

### How to Use Random

```java
import java.util.Random;

public class RandomDemo {
    public static void main(String[] args) {
        Random random = new Random();  // Create a Random object

        // Generate random integers
        int num1 = random.nextInt();        // Any integer (can be negative)
        int num2 = random.nextInt(100);     // 0 to 99 (exclusive upper bound)
        int num3 = random.nextInt(10) + 1;  // 1 to 10 (for dice roll, etc.)

        // Generate random doubles
        double d1 = random.nextDouble();    // 0.0 to 0.999... (less than 1.0)

        // Generate random booleans
        boolean b1 = random.nextBoolean();  // true or false
    }
}
```

### Generating Random Numbers in a Range

```java
Random random = new Random();

// Random number from min to max (inclusive)
int min = 5;
int max = 15;
int randomInRange = random.nextInt(max - min + 1) + min;  // 5 to 15

// Dice roll (1 to 6)
int diceRoll = random.nextInt(6) + 1;
```

### Populating Arrays with Random Values

```java
import java.util.Random;
import java.util.Arrays;

public class RandomArrayDemo {
    public static void main(String[] args) {
        Random random = new Random();

        // Create array of 10 random scores (0-100)
        int[] scores = new int[10];
        for (int i = 0; i < scores.length; i++) {
            scores[i] = random.nextInt(101);  // 0 to 100
        }

        System.out.println(Arrays.toString(scores));
        // Example output: [67, 23, 89, 45, 12, 78, 56, 91, 34, 72]
    }
}
```

---

## Connecting to What You Already Know

### From Week 3: Loops

Arrays and loops are inseparable partners:

| Loop Type | Array Use |
|-----------|-----------|
| `for` loop with counter | When you need the index |
| `for-each` loop | When you only need values |
| `while` loop | When searching with early exit |

All your loop skills directly apply to array processing!

### From Week 4-5: Methods

Array processing naturally fits into methods:

```java
// Method signatures you will commonly write:
public static int sum(int[] array) { ... }
public static double average(int[] array) { ... }
public static int findMax(int[] array) { ... }
public static int findMin(int[] array) { ... }
public static int count(int[] array, int target) { ... }
public static boolean contains(int[] array, int target) { ... }
public static int findIndex(int[] array, int target) { ... }
public static void printArray(int[] array) { ... }
```

Method overloading from Week 5 applies:

```java
// Overloaded print methods
public static void print(int[] array) { ... }
public static void print(double[] array) { ... }
public static void print(String[] array) { ... }

// Overloaded search methods
public static int find(int[] array, int target) { ... }
public static int find(String[] array, String target) { ... }
```

### Preparing for Week 7+: OOP

Arrays are foundational for object-oriented programming:

- Classes often contain arrays as instance variables (attributes)
- Methods operate on these internal arrays
- ArrayList (Week 8) is a more flexible alternative to arrays

```java
// Preview of what is coming in OOP:
public class Gradebook {
    private int[] grades;  // Array as an attribute

    public double getAverage() {
        // Method using the array
    }
}
```

---

## Common Struggles and How to Overcome Them

### Struggle 1: Zero-Based Indexing Confusion

**The confusion:** "Why is the first element at index 0? That makes no sense!"

**The solution:** Practice this mantra: **"Index = Position - 1"**

| Position (human counting) | Index (Java counting) |
|--------------------------|----------------------|
| 1st element | index 0 |
| 2nd element | index 1 |
| 3rd element | index 2 |
| Nth element | index N-1 |

Also remember: **Last index = length - 1**

Draw arrays with index numbers above them until it becomes automatic.

### Struggle 2: ArrayIndexOutOfBoundsException

**The confusion:** "My program crashes and I do not understand the error!"

**The solution:** Check these things:

1. **Are you using `<=` instead of `<` in your loop?**
   ```java
   // WRONG
   for (int i = 0; i <= array.length; i++)

   // CORRECT
   for (int i = 0; i < array.length; i++)
   ```

2. **Are you accessing index equal to length?**
   ```java
   // WRONG
   array[array.length]  // This index does not exist!

   // CORRECT
   array[array.length - 1]  // Last valid index
   ```

3. **Is your calculated index valid?**
   ```java
   // Always validate
   if (index >= 0 && index < array.length) {
       // Safe to access
   }
   ```

### Struggle 3: Understanding References vs Values

**The confusion:** "I copied my array but changes affect both!"

**The solution:** Remember:

- `int[] copy = original;` creates an **alias** (same array, two names)
- To get a real copy, use `Arrays.copyOf()`, `clone()`, or a manual loop

Test your understanding:

```java
int[] a = {1, 2, 3};
int[] b = a;          // Alias - same array
int[] c = a.clone();  // Copy - different array

a[0] = 99;

// What is b[0]?  Answer: 99 (same array as a)
// What is c[0]?  Answer: 1 (independent copy)
```

### Struggle 4: When Arrays Are Copied vs Referenced

**The confusion:** "Sometimes my array changes, sometimes it does not!"

**The solution:** Two rules:

1. **Passing to methods**: The method can modify the original array
   ```java
   void doubleValues(int[] arr) {
       for (int i = 0; i < arr.length; i++) {
           arr[i] *= 2;  // Modifies original!
       }
   }
   ```

2. **Assignment**: Creates alias, not copy
   ```java
   int[] copy = original;  // Alias!
   int[] realCopy = original.clone();  // Actual copy
   ```

---

## Practice Exercises

### Exercise 1: Array Basics (meget hjalp - Maximum Guidance)

**Goal:** Practice creating arrays and accessing elements.

**Step-by-step instructions:**

1. Create a new Java file called `ArrayBasics.java`
2. Create an array of 5 integer scores: 85, 92, 78, 95, 88
3. Print each score with its index
4. Print the first and last scores
5. Calculate and print the sum and average

**Starter code:**

```java
public class ArrayBasics {
    public static void main(String[] args) {
        // Step 1: Create the array
        int[] scores = {85, 92, 78, 95, 88};

        // Step 2: Print each score with index
        System.out.println("All scores:");
        for (int i = 0; i < scores.length; i++) {
            System.out.println("Index " + i + ": " + scores[i]);
        }

        // Step 3: Print first and last
        System.out.println("\nFirst score: " + scores[0]);
        System.out.println("Last score: " + scores[scores.length - 1]);

        // Step 4: Calculate sum
        int sum = 0;
        // TODO: Add loop to calculate sum

        // Step 5: Calculate average
        double average = 0;  // TODO: Calculate properly

        System.out.println("\nSum: " + sum);
        System.out.println("Average: " + average);
    }
}
```

**Expected output:**

```
All scores:
Index 0: 85
Index 1: 92
Index 2: 78
Index 3: 95
Index 4: 88

First score: 85
Last score: 88

Sum: 438
Average: 87.6
```

### Exercise 2: Array Methods (meget hjalp - Maximum Guidance)

**Goal:** Practice writing methods that work with arrays.

**Step-by-step instructions:**

1. Create these methods:
   - `sum(int[] array)` - returns the sum of all elements
   - `average(int[] array)` - returns the average
   - `max(int[] array)` - returns the largest value
   - `min(int[] array)` - returns the smallest value
2. Test each method in main

**Starter code:**

```java
public class ArrayMethods {

    public static void main(String[] args) {
        int[] numbers = {45, 23, 78, 12, 96, 34, 67};

        System.out.println("Array: ");
        printArray(numbers);

        System.out.println("Sum: " + sum(numbers));
        System.out.println("Average: " + average(numbers));
        System.out.println("Max: " + max(numbers));
        System.out.println("Min: " + min(numbers));
    }

    public static void printArray(int[] array) {
        System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i]);
            if (i < array.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }

    // TODO: Implement sum
    public static int sum(int[] array) {
        // Your code here
        return 0;
    }

    // TODO: Implement average
    public static double average(int[] array) {
        // Hint: Use the sum method you just wrote!
        return 0;
    }

    // TODO: Implement max
    public static int max(int[] array) {
        // Hint: Start by assuming first element is max
        return 0;
    }

    // TODO: Implement min
    public static int min(int[] array) {
        // Similar to max, but compare for smaller
        return 0;
    }
}
```

**Expected output:**

```
Array:
[45, 23, 78, 12, 96, 34, 67]
Sum: 355
Average: 50.714285714285715
Max: 96
Min: 12
```

### Exercise 3: Search and Count (nogen hjalp - Moderate Guidance)

**Goal:** Practice searching arrays and counting occurrences.

**Instructions:**

Create a program that:

1. Creates an array of 20 random numbers between 1 and 10
2. Prints the array
3. Asks the user for a number to search for
4. Reports:
   - Whether the number exists in the array
   - The first index where it appears (or -1 if not found)
   - How many times it appears

**Hints:**

- Use `Random` to generate numbers
- Create methods: `contains()`, `findFirst()`, `countOccurrences()`
- Use Scanner for user input

**Sample output:**

```
Generated array: [5, 3, 7, 5, 2, 8, 5, 1, 9, 3, 5, 7, 2, 4, 6, 5, 8, 3, 1, 7]

Enter a number to search for (1-10): 5
Found: true
First index: 0
Occurrences: 6
```

### Exercise 4: Array Statistics (nogen hjalp - Moderate Guidance)

**Goal:** Practice comprehensive array analysis.

**Instructions:**

Create a `StatisticsCalculator` class that analyzes an array of grades and reports:

1. Number of grades
2. Sum and average
3. Highest and lowest grades
4. Range (highest - lowest)
5. Count of passing grades (60 or above)
6. Count of A grades (90+), B grades (80-89), C grades (70-79), D grades (60-69), F grades (below 60)

**Structure suggestion:**

```java
public class StatisticsCalculator {
    public static void main(String[] args) {
        int[] grades = {85, 92, 78, 65, 95, 88, 72, 58, 91, 79, 84, 67};

        printStatistics(grades);
    }

    public static void printStatistics(int[] grades) {
        System.out.println("=== Grade Statistics ===");
        System.out.println("Number of grades: " + grades.length);
        System.out.println("Sum: " + sum(grades));
        System.out.println("Average: " + average(grades));
        // ... more statistics ...
    }

    // Helper methods: sum, average, max, min, countPassing, countGrade, etc.
}
```

### Exercise 5: Receipt Printer (ingen hjalp - Minimal Guidance)

**Goal:** Apply all array concepts to a practical problem.

**Requirements:**

Create a receipt printer program that:

1. Stores item names in a `String[]` array
2. Stores prices in a `double[]` array
3. Stores quantities in an `int[]` array
4. Prints a formatted receipt with:
   - Store name and date
   - Each item with quantity, unit price, and line total
   - Subtotal
   - Tax (8%)
   - Total

**Sample output:**

```
================================
       JAVA GROCERY STORE
         January 5, 2026
================================

Item           Qty   Price    Total
--------------------------------
Apples           3   $1.50    $4.50
Bread            2   $2.99    $5.98
Milk             1   $3.49    $3.49
Cheese           2   $4.99    $9.98
Eggs             1   $2.79    $2.79

--------------------------------
Subtotal:                   $26.74
Tax (8%):                    $2.14
================================
TOTAL:                      $28.88
================================

      Thank you for shopping!
```

**Challenge extensions:**

- Allow user input for items
- Apply discounts to certain items
- Handle buy-one-get-one deals
- Sort items alphabetically before printing

---

## Looking Ahead

This week you learned arrays - your first complex data structure. Arrays are fundamental building blocks that enable working with collections of data.

- **Week 7 (OOP - Classes and Objects):** You will create classes that contain arrays as attributes. A `Student` class might have an array of grades. A `Playlist` class might have an array of songs.

- **Week 8 (OOP - Encapsulation and ArrayList):** You will learn `ArrayList`, which is like an array that can grow and shrink. Many of the operations you learned this week (traversal, searching, etc.) apply directly to ArrayList.

- **Week 11 (File Handling):** When reading data from files, arrays (or ArrayLists) are the natural place to store that data.

- **Week 14 (Sorting):** You will learn algorithms to put arrays in order - alphabetically, numerically, or by custom criteria. Sorting builds directly on the array manipulation skills from this week.

The traversal patterns, search algorithms, and aggregate calculations you practiced this week are patterns you will use throughout your programming career. Arrays are everywhere in programming!

---

## Key Takeaways

- An **array** is a fixed-size, ordered collection of elements of the same type
- Arrays use **zero-based indexing** - the first element is at index 0
- The **last valid index** is always `length - 1`
- Create arrays with `new int[size]` or initialize with `{value1, value2, ...}`
- Access elements with `arrayName[index]`
- **ArrayIndexOutOfBoundsException** occurs when accessing an invalid index
- Use `for` loops when you need the index; use `for-each` when you only need values
- Arrays are **passed by reference** to methods - methods can modify the original
- **Assignment** creates an alias; use `clone()` or `Arrays.copyOf()` for true copies
- The `Random` class generates pseudo-random numbers for array population
- Common operations: sum, average, min, max, search, count, first, last
- Arrays combine powerfully with loops (Week 3) and methods (Weeks 4-5)

---

## For the Next Topic Agent

### Terminology Established This Week

- **array**: A fixed-size, ordered collection of elements of the same type
- **index**: The position of an element in an array (starting from 0)
- **zero-based indexing**: The convention where the first element is at index 0
- **element**: A single value stored in an array
- **length property**: `array.length` returns the number of elements
- **traversal**: Visiting every element in an array
- **for-each loop** (enhanced for loop): Simpler loop syntax when you only need values
- **ArrayIndexOutOfBoundsException**: Runtime error when accessing an invalid index
- **reference**: A variable holding an address to array data, not the data itself
- **alias**: Two variables pointing to the same array
- **linear search**: Checking each element sequentially to find a target
- **pseudo-random numbers**: Numbers that appear random, generated by `Random` class

### Example Classes/Concepts Created

- ArrayBasics demonstrating creation and access
- ArrayMethods with sum, average, max, min
- Search methods: contains, findFirst, countOccurrences
- StatisticsCalculator analyzing grades
- Receipt Printer using parallel arrays

### Student Capabilities After This Week

Students can now:

- Create and initialize arrays with both new and literal syntax
- Access and modify array elements using index notation
- Understand why indices start at 0 and that last index = length - 1
- Traverse arrays using both for loops and for-each loops
- Choose the appropriate loop type for the task
- Implement common operations: sum, average, min, max, count, search
- Write methods that accept arrays as parameters
- Write methods that return arrays
- Understand that arrays are passed by reference to methods
- Correctly copy arrays using clone() or Arrays.copyOf()
- Prevent and debug ArrayIndexOutOfBoundsException
- Use the Random class to generate random values
- Apply Week 3 loop skills to array processing
- Apply Week 4-5 method skills to array operations

### Pedagogical Patterns Continued

- **Row of mailboxes analogy**: Visualizing array indices as mailbox numbers
- **Train cars analogy**: Fixed sequence of numbered compartments
- **Egg carton analogy**: Fixed size, same type, numbered positions
- **House address analogy**: References as addresses pointing to data
- **Physical analogies**: Making abstract concepts concrete
- **Progressive exercises**: Basic access to comprehensive Receipt Printer

### Critical Connections for Week 7 (OOP - Classes and Objects)

- Arrays as attributes (instance variables) in classes
- Methods operating on internal arrays
- Understanding references prepares for object references
- Array traversal patterns apply to collections of objects
- The shift from "data + methods" to "objects containing both"
- Objects stored in arrays (arrays of objects)
- Constructor overloading (from Week 5) used extensively in OOP

### Student Misconceptions to Address in Week 7

- Arrays vs ArrayList (ArrayList is introduced with OOP)
- Object references work similarly to array references
- Methods in classes vs static methods (transition from static to instance)
- The concept of "state" - objects can have arrays as part of their state
