# Input, Output, Data Types, and Calculations - Week 1

*Prerequisites: None (this is your starting point!)*
*Phase: Phase 1: Foundation Building*

---

## What You'll Learn

By the end of this week, you will be able to:

- Store information in your programs using **variables**
- Work with different types of data (numbers, text, true/false values)
- Get input from users and display output to them
- Perform calculations using Java's arithmetic operators
- Format your output so it looks professional

This is your first step into programming. Take your time, experiment, and remember: every expert was once a beginner.

---

## Why This Matters

Imagine you are building a simple calculator app. You need to:
1. **Ask** the user for two numbers (input)
2. **Store** those numbers somewhere (variables and data types)
3. **Calculate** the result (arithmetic operations)
4. **Show** the answer to the user (output)

Every useful program does some version of these four things. This week, you learn the foundations that make all of it possible. Whether you are building a game, a business application, or a website, these concepts appear everywhere.

---

## Building Your Intuition

### The Big Picture

Think of a computer program like a recipe in a kitchen:

- **Variables** are like labeled containers (jars, bowls) that hold ingredients
- **Data types** tell you what kind of container you need (a jar for flour, a measuring cup for liquid)
- **Input** is like receiving ingredients from a supplier
- **Output** is like serving the finished dish to customers
- **Calculations** are the actual cooking - combining and transforming ingredients

Just as a chef needs containers to hold ingredients while cooking, a program needs variables to hold data while running.

### Common Questions Beginners Ask

**"Why can't the computer just remember everything automatically?"**
Computers are extremely fast but not intelligent. They only do exactly what you tell them. Variables are your way of telling the computer "remember this piece of information, I will need it later."

**"Why are there so many data types? Why not just one?"**
Different types of data need different amounts of memory and behave differently. Storing the number 42 is very different from storing the text "forty-two." By choosing the right data type, you make your program more efficient and prevent errors.

**"What is the difference between print and println?"**
`print` displays text and stays on the same line. `println` displays text and then moves to the next line. Think of `println` as pressing Enter after typing.

**"Why do I get errors when I try to use a variable I just created?"**
You might be confusing *declaring* a variable (creating the container) with *initializing* it (putting something in the container). A variable must have a value before you can use it.

---

## Understanding Variables

### What Is a Variable?

A **variable** is a named storage location in your program's memory. It holds a piece of data that can change while your program runs.

Think of it like a labeled box:
- The **name** is the label on the box (so you can find it later)
- The **value** is what is inside the box
- The **type** describes what kind of things the box can hold

### Why Do We Need Variables?

Without variables, programs could not remember anything. Consider this scenario:

> You ask a user for their age, perform a calculation, and then want to display a message including their age. Without a variable, the age is lost the moment the calculation finishes.

Variables allow your program to:
1. Store data for later use
2. Modify data as the program runs
3. Pass data between different parts of your program

### How Variables Work

Creating a variable happens in two steps:

1. **Declaration**: Tell Java you want a container of a certain type with a certain name
2. **Initialization**: Put a value into that container

You can do both in one line (recommended for beginners) or separately.

### Seeing Variables in Action

```java
// Declaration AND initialization in one step (recommended)
int age = 25;              // A whole number container named "age" holding 25
String name = "Maria";     // A text container named "name" holding "Maria"
double price = 19.99;      // A decimal number container named "price" holding 19.99

// Using the variables
System.out.println(name);          // Displays: Maria
System.out.println(age);           // Displays: 25
System.out.println(price);         // Displays: 19.99

// Variables can change (that's why they're called "variables"!)
age = 26;                          // Birthday! Update the value
System.out.println(age);           // Now displays: 26
```

**Line-by-line explanation:**
- Lines 2-4: We create three variables, each with a different type, name, and value
- Lines 7-9: We display what is stored in each variable
- Line 12: We change what is stored in `age` (the old value 25 is replaced with 26)
- Line 13: When we display `age` now, we see the new value

### Common Mistakes with Variables

**Mistake 1: Using a variable before giving it a value**
```java
int score;                    // Declared but not initialized
System.out.println(score);    // ERROR! Java doesn't know what value to display
```

**Fix:** Always initialize your variables when you declare them:
```java
int score = 0;                // Now it has a value
System.out.println(score);    // Works! Displays: 0
```

**Mistake 2: Trying to change a variable's type**
```java
int count = 10;
count = "ten";    // ERROR! count was declared as int, can't hold text
```

**Fix:** Once you choose a type, stick with it. Create a new variable if you need a different type.

---

## Understanding Data Types

### What Is a Data Type?

A **data type** defines what kind of data a variable can hold and how much memory it needs. Java is a "strongly typed" language, meaning every variable must have a declared type.

Think of data types like different sizes and shapes of containers:
- A shoebox for shoes (not for liquids!)
- A bottle for liquids (not for shoes!)
- A filing cabinet for documents

### Why Do We Need Different Types?

1. **Memory efficiency**: Storing a small number uses less memory than storing a large number
2. **Preventing errors**: Java stops you from accidentally putting text where a number should go
3. **Enabling operations**: You can add numbers together, but "adding" text works differently (it concatenates)

### The Primitive Data Types

Java has 8 **primitive** (basic, built-in) data types. Here are the most commonly used:

| Type | What It Stores | Example Values | When to Use |
|------|---------------|----------------|-------------|
| `int` | Whole numbers | -5, 0, 42, 1000 | Counting, ages, quantities |
| `double` | Decimal numbers | 3.14, -0.5, 99.99 | Prices, measurements, calculations |
| `boolean` | True or false | true, false | Yes/no decisions, on/off states |
| `char` | Single character | 'A', '7', '@' | Single letters, symbols |

**Less common but good to know:**
- `byte`, `short`, `long`: Different sizes of whole numbers
- `float`: Decimal numbers (less precise than double)

### Seeing Data Types in Action

```java
// Whole numbers - use int for most cases
int studentsInClass = 28;
int temperature = -5;          // Can be negative
int yearBorn = 1995;

// Decimal numbers - use double for precision
double pi = 3.14159;
double bankBalance = 1523.47;
double weight = 72.5;

// True/false values - use boolean
boolean isLoggedIn = true;
boolean hasPermission = false;
boolean isAdult = true;

// Single characters - use char (note: single quotes!)
char firstInitial = 'J';
char grade = 'A';
char symbol = '@';

// Text - use String (note: capital S and double quotes!)
String firstName = "Emma";
String message = "Hello, World!";
String empty = "";             // An empty string is valid
```

**Important distinctions:**
- `char` uses single quotes: `'A'`
- `String` uses double quotes: `"A"` or `"Hello"`
- `String` is capitalized because it is a reference type (more on this later in the course)

### Common Mistakes with Data Types

**Mistake 1: Using the wrong quotes**
```java
char letter = "A";     // ERROR! Double quotes create a String, not a char
String word = 'Hi';    // ERROR! Single quotes are only for single characters
```

**Fix:**
```java
char letter = 'A';     // Single character = single quotes
String word = "Hi";    // Text = double quotes
```

**Mistake 2: Forgetting that int cannot store decimals**
```java
int price = 19.99;     // ERROR! int cannot hold decimal values
```

**Fix:**
```java
double price = 19.99;  // Use double for decimal numbers
```

---

## Understanding Output (Displaying Information)

### What Is Output?

**Output** is how your program communicates with the user. In console programs (programs that run in a text window), output means displaying text on the screen.

### Why Do We Need Output?

Without output, your program works silently. You would have no way to:
- Show results of calculations
- Display instructions or menus
- Confirm that actions completed successfully
- Debug (find problems in) your code

### How Output Works in Java

Java provides several ways to display output. The most common is `System.out`:

- `System.out.println()` - prints text and moves to the next line
- `System.out.print()` - prints text and stays on the same line
- `System.out.printf()` - prints formatted text (more control over appearance)

### Seeing Output in Action

```java
// println - each print on its own line
System.out.println("Hello");
System.out.println("World");
// Output:
// Hello
// World

// print - stays on the same line
System.out.print("Hello ");
System.out.print("World");
System.out.println();    // Move to next line (empty println)
// Output:
// Hello World

// Combining text and variables
String name = "Alex";
int age = 22;
System.out.println("Name: " + name);           // String concatenation with +
System.out.println("Age: " + age);
// Output:
// Name: Alex
// Age: 22

// printf - formatted output (great for aligning columns, controlling decimals)
double price = 49.5;
System.out.printf("Price: $%.2f%n", price);    // %.2f means 2 decimal places
// Output:
// Price: $49.50
```

**printf format codes you will use often:**
- `%d` - for whole numbers (int)
- `%f` - for decimal numbers (double), `%.2f` for 2 decimal places
- `%s` - for text (String)
- `%n` - new line (works on all operating systems)

### Common Mistakes with Output

**Mistake 1: Forgetting to use + when combining text and variables**
```java
String name = "Sam";
System.out.println("Hello " name);    // ERROR! Missing +
```

**Fix:**
```java
System.out.println("Hello " + name);  // Correct
```

**Mistake 2: Using println when you want to stay on the same line**
```java
System.out.println("Loading");
System.out.println("...");
// Output (on two lines - probably not what you wanted):
// Loading
// ...
```

**Fix:**
```java
System.out.print("Loading");
System.out.println("...");
// Output (on one line):
// Loading...
```

---

## Understanding Input (Getting Information from Users)

### What Is Input?

**Input** is how your program receives information from the outside world. In console programs, this typically means reading what the user types on the keyboard.

### Why Do We Need Input?

Without input, your program does the exact same thing every time it runs. Input makes programs interactive and useful:
- A calculator needs to know which numbers to calculate
- A game needs to know the player's choices
- A registration form needs the user's information

### How Input Works in Java: The Scanner Class

Java uses a tool called `Scanner` to read input. Think of Scanner as a helper that watches the keyboard and captures what the user types.

**Three steps to use Scanner:**
1. Import it (tell Java you want to use it)
2. Create a Scanner object
3. Use Scanner methods to read different types of data

### Seeing Input in Action

```java
import java.util.Scanner;    // Step 1: Import Scanner (at top of file)

public class InputExample {
    public static void main(String[] args) {
        // Step 2: Create a Scanner connected to keyboard input
        Scanner scanner = new Scanner(System.in);

        // Step 3: Use Scanner to read data
        System.out.print("Enter your name: ");      // Prompt (tell user what to type)
        String name = scanner.nextLine();           // Read a full line of text

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();                // Read a whole number

        System.out.print("Enter your height in meters: ");
        double height = scanner.nextDouble();       // Read a decimal number

        // Display what we collected
        System.out.println();
        System.out.println("Summary:");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Height: " + height + "m");
    }
}
```

**Scanner methods for different data types:**
- `nextLine()` - reads a full line of text (until user presses Enter)
- `next()` - reads a single word (until space or Enter)
- `nextInt()` - reads a whole number
- `nextDouble()` - reads a decimal number
- `nextBoolean()` - reads true or false

### Common Mistakes with Scanner

**Mistake 1: The "nextLine() after nextInt()" problem (VERY COMMON!)**

This is the most confusing Scanner issue for beginners:

```java
System.out.print("Enter your age: ");
int age = scanner.nextInt();

System.out.print("Enter your name: ");
String name = scanner.nextLine();    // PROBLEM: Seems to skip this!

System.out.println("Age: " + age + ", Name: " + name);
// Output shows empty name!
```

**Why this happens:** When you type `25` and press Enter, `nextInt()` reads `25` but leaves the Enter key press in the input buffer. Then `nextLine()` immediately reads that leftover Enter and thinks you entered nothing.

**Fix:** Add an extra `nextLine()` to consume the leftover Enter:
```java
System.out.print("Enter your age: ");
int age = scanner.nextInt();
scanner.nextLine();    // Consume the leftover Enter

System.out.print("Enter your name: ");
String name = scanner.nextLine();    // Now this works correctly!
```

**Mistake 2: Forgetting the import statement**
```java
public class Example {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);  // ERROR! Scanner not found
    }
}
```

**Fix:** Add `import java.util.Scanner;` at the very top of your file.

---

## Understanding Calculations and Operators

### What Are Operators?

**Operators** are symbols that tell Java to perform specific operations on values. The most common are arithmetic operators for mathematical calculations.

### Why Do We Need Operators?

Programs frequently need to:
- Calculate totals, averages, percentages
- Compare values
- Combine conditions

Operators are how you express these operations in code.

### Arithmetic Operators

| Operator | Operation | Example | Result |
|----------|-----------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `7 * 6` | `42` |
| `/` | Division | `15 / 3` | `5` |
| `%` | Modulo (remainder) | `17 % 5` | `2` |

**The modulo operator (%)** deserves special attention. It gives you the remainder after division:
- `17 % 5 = 2` (17 divided by 5 is 3 with remainder 2)
- `10 % 2 = 0` (10 divides evenly by 2, no remainder)
- Use it to check if numbers are even/odd, or to cycle through values

### Order of Operations (Operator Precedence)

Java follows mathematical order of operations (PEMDAS/BODMAS):

1. **P**arentheses first `()`
2. Then **M**ultiplication, **D**ivision, **M**odulo (left to right)
3. Then **A**ddition, **S**ubtraction (left to right)

```java
int result1 = 2 + 3 * 4;       // = 2 + 12 = 14 (multiplication first)
int result2 = (2 + 3) * 4;     // = 5 * 4 = 20 (parentheses first)
int result3 = 10 - 4 + 2;      // = 6 + 2 = 8 (left to right)
```

### Seeing Calculations in Action

```java
// Basic arithmetic
int a = 10;
int b = 3;

System.out.println("a + b = " + (a + b));    // 13
System.out.println("a - b = " + (a - b));    // 7
System.out.println("a * b = " + (a * b));    // 30
System.out.println("a / b = " + (a / b));    // 3 (integer division!)
System.out.println("a % b = " + (a % b));    // 1 (remainder)

// IMPORTANT: Integer division truncates (throws away) the decimal part
int wholeResult = 10 / 3;       // = 3, not 3.333...

// If you need the decimal, at least one operand must be a double
double decimalResult = 10.0 / 3;    // = 3.333...
double alsoWorks = (double) 10 / 3; // = 3.333... (casting 10 to double)

// Using the Math class for advanced operations
double squareRoot = Math.sqrt(25);        // = 5.0
double power = Math.pow(2, 8);            // = 256.0 (2 to the power of 8)
double rounded = Math.round(3.7);         // = 4.0
int maximum = Math.max(10, 25);           // = 25
```

### Common Mistakes with Calculations

**Mistake 1: Integer division surprise**
```java
int average = (90 + 85 + 78) / 3;    // = 84, not 84.33!
System.out.println(average);
```

When dividing two integers, Java performs **integer division** - it throws away the decimal part.

**Fix:** Use double if you need decimal precision:
```java
double average = (90 + 85 + 78) / 3.0;    // = 84.33...
```

**Mistake 2: Forgetting parentheses in output**
```java
int x = 5;
int y = 10;
System.out.println("Sum: " + x + y);    // Prints "Sum: 510" (oops!)
```

The `+` is treated as string concatenation from left to right.

**Fix:** Use parentheses to force arithmetic first:
```java
System.out.println("Sum: " + (x + y));  // Prints "Sum: 15"
```

---

## Type Conversion (Casting)

### What Is Type Conversion?

Sometimes you need to convert a value from one type to another. This is called **type conversion** or **casting**.

### Two Types of Conversion

**Implicit conversion (automatic):** Java automatically converts "smaller" types to "larger" types:
```java
int wholeNumber = 42;
double decimalNumber = wholeNumber;    // Automatic: int to double is safe
// decimalNumber now contains 42.0
```

**Explicit conversion (manual casting):** You must tell Java when converting to a "smaller" type:
```java
double decimalNumber = 42.7;
int wholeNumber = (int) decimalNumber; // Manual: might lose data!
// wholeNumber now contains 42 (the .7 is lost!)
```

### Seeing Type Conversion in Action

```java
// Implicit (automatic) - safe, no data loss
int age = 25;
double ageAsDouble = age;              // 25 becomes 25.0
System.out.println(ageAsDouble);       // 25.0

// Explicit (manual) - potentially loses data
double price = 19.99;
int priceRounded = (int) price;        // WARNING: truncates, doesn't round!
System.out.println(priceRounded);      // 19 (not 20!)

// If you want proper rounding:
int priceProperlyRounded = (int) Math.round(price);    // 20
```

---

## Common Struggles and How to Overcome Them

### Struggle 1: Variable Declaration vs Initialization

**The confusion:** "I declared a variable, why can't I use it?"

**The solution:** Declaration creates the container; initialization fills it. Java requires a value before use.

```java
// Declaration only (container exists but is empty)
int score;

// Initialization (putting a value in)
score = 100;

// Or do both at once (recommended for beginners):
int score = 100;
```

### Struggle 2: Type Conversion Confusion (When to Cast)

**The confusion:** "When do I need to write (int) or (double)?"

**The solution:**
- Going to a "larger" type (int to double): automatic, no cast needed
- Going to a "smaller" type (double to int): requires explicit cast, warns about data loss

Think of it like containers: you can always pour a small cup into a big bucket, but pouring a bucket into a cup requires you to acknowledge that overflow (data loss) will happen.

### Struggle 3: Scanner.nextLine() After nextInt() Issues

**The confusion:** "My program skips my input!"

**The solution:** After reading a number with `nextInt()` or `nextDouble()`, add `scanner.nextLine()` before trying to read text.

```java
int age = scanner.nextInt();
scanner.nextLine();              // Consume the leftover Enter
String name = scanner.nextLine(); // Now this works
```

### Struggle 4: print vs println Difference

**The confusion:** "Why is my output all on one line / on separate lines?"

**The solution:**
- `println` = "print line" - prints then moves to next line
- `print` = prints and stays where it is

```java
// Multiple items on ONE line:
System.out.print("One ");
System.out.print("Two ");
System.out.println("Three");    // Move to next line after this

// Each item on its OWN line:
System.out.println("Apple");
System.out.println("Banana");
System.out.println("Cherry");
```

---

## Practice Exercises

### Exercise 1: Personal Information Display (mycket hjalp - Maximum Guidance)

**Goal:** Practice variables, data types, and output.

**Step-by-step instructions:**

1. Create a new Java file called `PersonalInfo.java`
2. Declare variables for:
   - Your name (String)
   - Your age (int)
   - Your height in meters (double)
   - Whether you are a student (boolean)
3. Initialize each variable with appropriate values
4. Print each piece of information on its own line with a label

**Expected output format:**
```
Name: [your name]
Age: [your age]
Height: [your height]m
Student: [true/false]
```

**Hint:** Use `System.out.println()` with string concatenation (`+`) to combine labels and values.

### Exercise 2: Simple Calculator (nogen hjalp - Moderate Guidance)

**Goal:** Practice input with Scanner and calculations.

**Instructions:**

1. Create a program that asks the user for two numbers
2. Calculate and display:
   - The sum
   - The difference
   - The product
   - The quotient (use double for this one!)
   - The remainder

**What you will need:**
- Import Scanner
- Create a Scanner object
- Use appropriate Scanner methods for reading doubles
- Perform arithmetic operations
- Display results with clear labels

**Sample interaction:**
```
Enter first number: 15
Enter second number: 4
Sum: 19.0
Difference: 11.0
Product: 60.0
Quotient: 3.75
Remainder: 3.0
```

### Exercise 3: Temperature Converter (ingen hjalp - Minimal Guidance)

**Goal:** Apply all concepts from this week.

**Requirements:**
- Ask the user for a temperature in Celsius
- Convert it to Fahrenheit using the formula: F = C * 9/5 + 32
- Display the result formatted to one decimal place
- Make the program work correctly with decimal inputs

**Hint for formatting:** Look up `printf` with `%.1f`

---

## Looking Ahead

This week you have built the foundation for everything that follows:

- **Week 2 (Conditions and Logic):** You will use the variables and comparisons you learned here to make programs that make decisions. "If the age is over 18, display this message."

- **Week 3 (Loops):** You will combine input, output, and calculations with repetition. "Keep asking for numbers until the user enters -1."

- **Week 4 (Methods):** You will organize your code into reusable pieces, passing variables as parameters and returning calculated results.

Every concept you learn builds on what you learned this week. Take time to practice until variables, data types, input, and output feel natural.

---

## Key Takeaways

- **Variables** are named containers that store data; they must have a type and should be initialized when declared
- **Data types** define what kind of data a variable holds (int for whole numbers, double for decimals, String for text, boolean for true/false)
- **Output** uses `System.out.println()` to display information to users; use `+` to combine text with variables
- **Input** uses the Scanner class to read user input; remember to handle the nextLine() issue after reading numbers
- **Operators** perform calculations; watch out for integer division losing decimal precision
- **Type conversion** happens automatically when going to larger types, but requires explicit casting when going to smaller types

---

## For the Next Topic Agent

### Terminology Established This Week

- **variable**: A named storage location in memory that holds a value which can change during program execution
- **data type**: A classification that specifies what kind of data a variable can hold and how much memory it uses
- **primitive type**: One of Java's 8 built-in basic data types (int, double, boolean, char, byte, short, long, float)
- **String**: A reference type that holds text (sequences of characters); note the capital S
- **declaration**: The act of creating a variable by specifying its type and name
- **initialization**: The act of giving a variable its first value
- **Scanner**: A Java utility class used to read input from various sources, commonly keyboard input
- **operator**: A symbol that tells Java to perform a specific operation (like +, -, *, /)
- **concatenation**: Joining strings together using the + operator
- **casting**: Explicitly converting a value from one type to another using (type) syntax
- **integer division**: Division between two integers that discards any decimal remainder

### Example Classes/Concepts Created

- Basic variable declaration and initialization patterns
- Scanner input patterns (with the nextLine() after nextInt() fix)
- System.out.println() and printf() output patterns
- Arithmetic calculation patterns
- Type conversion examples

### Student Capabilities After This Week

Students can now:
- Declare and initialize variables of all primitive types and String
- Choose appropriate data types for different kinds of information
- Use Scanner to read user input (int, double, String)
- Display output using println, print, and printf
- Perform arithmetic calculations with correct operator precedence
- Convert between data types (both implicit and explicit casting)
- Concatenate strings with variables for meaningful output

### Pedagogical Patterns Used

- **Analogy-first approach**: Every concept introduced with a real-world analogy before technical details
- **Common mistakes sections**: Proactively showing what NOT to do builds debugging skills
- **Progressive exercise difficulty**: meget hjalp -> nogen hjalp -> ingen hjalp structure
- **Encouraging tone**: Normalizing confusion and struggle as part of learning
- **Why before how**: Each concept starts with motivation before mechanics
- **Heavily annotated code**: Comments explain not just what, but why
- **Small code examples**: No example exceeds 20 lines; most are under 10
