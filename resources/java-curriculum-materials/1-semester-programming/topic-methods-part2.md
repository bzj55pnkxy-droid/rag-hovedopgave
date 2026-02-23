# Methods Part 2 - Week 5

*Prerequisites: Week 4 - Methods Part 1*
*Phase: Phase 2: Decomposition and Abstraction*

---

## What You'll Learn

By the end of this week, you will be able to:

- **Use method overloading** to create multiple versions of a method with different parameters
- **Decompose complex problems** into smaller, manageable helper methods
- **Chain and nest method calls** for cleaner, more expressive code
- **Plan before coding** using activity diagrams and pseudocode
- **Debug systematically** when methods do not work as expected
- **Decide when to create a method** versus writing inline code
- **Organize code** for readability and maintainability

Last week you learned the fundamentals of methods - how to create them, call them, pass parameters, and return values. This week, you will level up those skills. You will learn how professional programmers design method-based solutions for complex problems, not just write individual methods, but orchestrate them together into elegant, maintainable code.

---

## Why This Matters

In Week 4, you learned to write individual methods. But real programs are not just collections of isolated methods - they are carefully designed systems where methods work together. This week is about learning to **think in methods** and **design before you code**.

Consider these real-world scenarios:

- A **calculator app** needs an "add" function that works with 2 numbers, 3 numbers, or even a list of numbers. Do you write three methods with different names (`add2`, `add3`, `addMany`)? There is a better way: **method overloading**.

- A **game engine** needs to check collisions, update positions, render graphics, and handle input - all working together every frame. This requires **method composition** where one method orchestrates many others.

- A **banking system** where a simple "transfer money" operation actually involves checking balances, validating accounts, logging transactions, and sending notifications. This is **problem decomposition** - breaking one big task into many small ones.

- A **restaurant ordering system** that crashes mysteriously. Without systematic debugging skills, finding the bug could take days instead of minutes.

The skills you learn this week bridge the gap between "I can write methods" and "I can design solutions." This is the difference between writing code and engineering software.

---

## Building Your Intuition

### The Big Picture: From Single Methods to Method Systems

Last week, you learned to write individual methods - like learning individual words in a new language. This week, you learn to write sentences and paragraphs - combining methods together to express complex ideas.

Think of it this way:

- **Week 4**: You learned to build LEGO bricks (individual methods)
- **Week 5**: You learn to build LEGO structures (methods working together)

The individual brick is important, but the real magic happens when you combine bricks into something meaningful.

### The Restaurant Kitchen Analogy

Imagine a restaurant kitchen. The head chef does not cook every dish alone from start to finish. Instead:

1. **The head chef** plans the menu and coordinates (your `main` or `run` method)
2. **The sous chef** handles complex preparation (helper methods)
3. **Station cooks** specialize in specific tasks - one for sauces, one for grilling, one for desserts (specialized methods)

When an order comes in for "Grilled Salmon with Vegetables":

```
headChef.prepareOrder("Grilled Salmon with Vegetables")
    -> calls grillStation.cookSalmon()
    -> calls sauceStation.prepareBeurBlanc()
    -> calls vegStation.roastVegetables()
    -> calls plateStation.arrangePlate()
```

Each station (method) has one job. The head chef coordinates. This is **problem decomposition** - breaking a big task into specialized smaller tasks.

### The Toolbox Analogy for Overloading

Think about a screwdriver. You do not have just ONE screwdriver - you have:
- A flathead screwdriver
- A Phillips screwdriver
- Different sizes of each

They are all "screwdrivers" - they all turn screws. But each is designed for a specific type of screw.

**Method overloading** is the same idea. You can have multiple methods with the same name, each designed to handle different types of inputs:

```
screwdriver(flatheadScrew)     -> uses flathead technique
screwdriver(phillipsScrew)     -> uses Phillips technique
screwdriver(tinyScrew)         -> uses precision technique
```

Same name, same purpose, different implementations for different situations.

### The GPS Navigation Analogy for Planning

When you use GPS navigation, you do not just start driving and hope for the best. The GPS:

1. **Analyzes the destination** (understands the problem)
2. **Plans the route** (designs the solution)
3. **Breaks it into steps** (turn-by-turn directions)
4. **Executes step by step** (drives the route)
5. **Recalculates when needed** (debugs and adjusts)

Professional programmers work the same way. They do not just start typing code. They:

1. Understand the problem
2. Plan the solution (activity diagrams, pseudocode)
3. Break it into methods
4. Implement step by step
5. Debug and refine

This week, you will learn these planning techniques.

---

## Understanding Method Overloading

### What Is Method Overloading?

**Method overloading** means having multiple methods with the **same name** but **different parameter lists**. Java knows which version to call based on the arguments you provide.

This is one of Java's most useful features for creating clean, intuitive code.

### Why Do We Need Method Overloading?

Consider this problem: You want to create a method that prints a greeting. But sometimes you want to greet someone by name, sometimes you want to specify how many times to greet, and sometimes you just want a generic greeting.

**Without overloading (messy approach):**

```java
public static void printGreeting() { ... }
public static void printGreetingWithName(String name) { ... }
public static void printGreetingWithNameAndTimes(String name, int times) { ... }
```

You end up with confusing, hard-to-remember method names. The user of your code has to remember three different names for essentially the same operation.

**With overloading (clean approach):**

```java
public static void greet() { ... }
public static void greet(String name) { ... }
public static void greet(String name, int times) { ... }
```

All three methods are called `greet`. Java figures out which one you want based on what arguments you provide. This is cleaner and more intuitive.

### How Method Overloading Works

Java distinguishes overloaded methods by their **method signature** - the combination of:

1. The method name
2. The number of parameters
3. The types of parameters
4. The order of parameter types

**Important:** The return type is NOT part of the signature. You cannot overload by only changing the return type.

### Seeing Method Overloading in Action

```java
public class Greeter {

    // Version 1: No parameters - generic greeting
    public static void greet() {
        System.out.println("Hello!");
    }

    // Version 2: One String parameter - personalized greeting
    public static void greet(String name) {
        System.out.println("Hello, " + name + "!");
    }

    // Version 3: String and int - repeated personalized greeting
    public static void greet(String name, int times) {
        for (int i = 0; i < times; i++) {
            System.out.println("Hello, " + name + "!");
        }
    }

    public static void main(String[] args) {
        greet();              // Calls version 1: prints "Hello!"
        greet("Alice");       // Calls version 2: prints "Hello, Alice!"
        greet("Bob", 3);      // Calls version 3: prints "Hello, Bob!" three times
    }
}
```

**How Java decides which method to call:**

| Call | Arguments | Matches | Method Called |
|------|-----------|---------|---------------|
| `greet()` | none | `greet()` | Version 1 |
| `greet("Alice")` | 1 String | `greet(String)` | Version 2 |
| `greet("Bob", 3)` | 1 String, 1 int | `greet(String, int)` | Version 3 |

### The sumUp Example: Classic Overloading

Here is a practical example showing three versions of a sum method:

```java
public class Calculator {

    // Sum two integers
    public static int sumUp(int a, int b) {
        return a + b;
    }

    // Sum three integers
    public static int sumUp(int a, int b, int c) {
        return a + b + c;
    }

    // Sum two doubles (different types!)
    public static double sumUp(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {
        System.out.println(sumUp(5, 3));           // 8 (calls int, int version)
        System.out.println(sumUp(5, 3, 2));        // 10 (calls int, int, int version)
        System.out.println(sumUp(5.5, 3.3));       // 8.8 (calls double, double version)
    }
}
```

Notice how the same name `sumUp` handles different situations naturally. The caller does not need to remember `sumUpTwoInts`, `sumUpThreeInts`, `sumUpTwoDoubles` - just `sumUp`.

### Valid vs Invalid Overloading

**Valid overloading - these CAN coexist:**

```java
public static void print(int x) { }           // Different number of parameters
public static void print(int x, int y) { }

public static void print(int x) { }           // Different parameter types
public static void print(String x) { }

public static void print(int x, String y) { } // Different parameter order
public static void print(String x, int y) { }
```

**Invalid overloading - these CANNOT coexist:**

```java
// WRONG: Only return type is different - NOT valid overloading
public static int calculate(int x) { return x; }
public static double calculate(int x) { return x; }  // ERROR!

// WRONG: Only parameter names are different - NOT valid overloading
public static void greet(String firstName) { }
public static void greet(String lastName) { }  // ERROR! Same as (String)
```

### Common Mistakes with Method Overloading

**Mistake 1: Thinking parameter names matter**

```java
// These are THE SAME method to Java - ERROR!
public static void display(String title) { }
public static void display(String message) { }  // Compiler error: duplicate method
```

**Fix:** Parameter names do not affect the signature. Only types matter.

**Mistake 2: Thinking return type makes methods different**

```java
// These are THE SAME method to Java - ERROR!
public static int getValue() { return 42; }
public static String getValue() { return "42"; }  // Compiler error
```

**Fix:** You cannot overload by return type alone. Change the parameters.

**Mistake 3: Ambiguous calls**

```java
public static void process(int x, double y) { }
public static void process(double x, int y) { }

// This is ambiguous - Java cannot decide!
process(5, 5);  // ERROR: both methods match equally well
```

**Fix:** Be explicit: `process(5, 5.0)` or `process(5.0, 5)`

### When to Use Method Overloading

Use overloading when:

1. **Same logical operation, different inputs**: Like `sumUp` with 2 or 3 numbers
2. **Optional parameters**: Like `greet()` vs `greet(String name)`
3. **Different data types**: Like `print(int)` vs `print(String)`

Do NOT use overloading when:

1. The methods do completely different things
2. It makes the code confusing
3. You are just trying to avoid thinking of a good name

---

## Understanding Problem Decomposition

### What Is Problem Decomposition?

**Problem decomposition** is the practice of breaking a large, complex problem into smaller, manageable pieces. Each piece becomes its own method. This is also called **top-down design** or **divide and conquer**.

### Why Is Decomposition Important?

Large problems are overwhelming. Small problems are solvable. Decomposition transforms the overwhelming into the solvable.

Consider writing an essay:

| Without Decomposition | With Decomposition |
|-----------------------|-------------------|
| "Write a 10-page essay" | "Write an introduction" |
| Overwhelming! | "Write body paragraph 1" |
| Where do I even start? | "Write body paragraph 2" |
| | "Write conclusion" |
| | Each part is manageable! |

Programming works the same way. A complex program is just many simple methods working together.

### The Top-Down Design Process

**Step 1: Understand the whole problem**
- What is the goal?
- What are the inputs and outputs?
- What are the main steps?

**Step 2: Identify major subtasks**
- Break the problem into 3-7 main parts
- Each part should have a single, clear purpose

**Step 3: Break down each subtask**
- If a subtask is still complex, break it down further
- Continue until each piece is simple enough to code directly

**Step 4: Implement from simple to complex**
- Start with the simplest methods
- Build up to the more complex ones
- Test each piece as you go

### Seeing Decomposition in Action: A Report Generator

**Problem:** Create a program that generates a student report card.

**Without decomposition (nightmare):**

```java
public static void generateReport(String name, int[] scores) {
    // 100+ lines of code doing everything:
    // - validating inputs
    // - calculating average
    // - determining grade
    // - formatting output
    // - printing headers
    // - printing scores
    // - printing summary
    // Impossible to understand, test, or maintain!
}
```

**With decomposition (manageable):**

```java
public static void main(String[] args) {
    String name = "Alice";
    int[] scores = {85, 92, 78, 95, 88};
    generateReport(name, scores);
}

// Level 1: The main orchestrator
public static void generateReport(String name, int[] scores) {
    printHeader(name);
    printScores(scores);
    printSummary(scores);
}

// Level 2: Major components
public static void printHeader(String name) {
    printDivider();
    System.out.println("Report Card for: " + name);
    printDivider();
}

public static void printScores(int[] scores) {
    System.out.println("\nIndividual Scores:");
    for (int i = 0; i < scores.length; i++) {
        System.out.println("  Assignment " + (i + 1) + ": " + scores[i]);
    }
}

public static void printSummary(int[] scores) {
    double average = calculateAverage(scores);
    String grade = determineGrade(average);

    System.out.println("\nSummary:");
    System.out.println("  Average: " + average);
    System.out.println("  Grade: " + grade);
}

// Level 3: Helper methods
public static void printDivider() {
    System.out.println("================================");
}

public static double calculateAverage(int[] scores) {
    int sum = 0;
    for (int score : scores) {
        sum += score;
    }
    return (double) sum / scores.length;
}

public static String determineGrade(double average) {
    if (average >= 90) return "A";
    if (average >= 80) return "B";
    if (average >= 70) return "C";
    if (average >= 60) return "D";
    return "F";
}
```

**Notice the hierarchy:**

```
generateReport()
    -> printHeader()
        -> printDivider()
    -> printScores()
    -> printSummary()
        -> calculateAverage()
        -> determineGrade()
```

Each method has ONE job. The high-level methods coordinate; the low-level methods do the work.

### The Single Responsibility Principle

A method should do ONE thing and do it well. This is called the **Single Responsibility Principle**.

**Bad: Method does too much**

```java
public static void processOrder(String customer, String item, int quantity, double price) {
    // Validates customer
    // Checks inventory
    // Calculates total
    // Applies discounts
    // Processes payment
    // Updates inventory
    // Sends confirmation email
    // Updates customer history
    // ... 200 lines later ...
}
```

**Good: Each method has one responsibility**

```java
public static void processOrder(String customer, String item, int quantity, double price) {
    validateCustomer(customer);
    checkInventory(item, quantity);
    double total = calculateTotal(quantity, price);
    total = applyDiscounts(total, customer);
    processPayment(customer, total);
    updateInventory(item, quantity);
    sendConfirmation(customer, item, quantity, total);
}
```

Now if the discount calculation is wrong, you know exactly where to look: `applyDiscounts()`. If the email is not sending, check `sendConfirmation()`. Each method is focused and testable.

### How to Decide What Becomes a Method

Ask yourself these questions:

| Question | If YES, make it a method |
|----------|-------------------------|
| Will this code be used more than once? | Definitely |
| Is this a distinct, nameable task? | Yes |
| Is this block more than 10-15 lines? | Probably |
| Would extracting this make the code clearer? | Yes |
| Could someone else need this functionality? | Yes |
| Does it have a single, clear purpose? | Yes |

---

## Understanding Helper Methods

### What Is a Helper Method?

A **helper method** is a method that assists other methods by handling a specific subtask. Helper methods are usually:

- Called by other methods, not directly from `main`
- Private or package-private (not part of the public interface)
- Focused on a single, specific task

### Why Use Helper Methods?

Helper methods:

1. **Reduce complexity** - Break big methods into smaller pieces
2. **Eliminate repetition** - Code used multiple times lives in one place
3. **Improve readability** - Give meaningful names to complex operations
4. **Enable testing** - Small methods are easier to test
5. **Support maintenance** - Changes are isolated to specific methods

### The Assistant Analogy

Think of helper methods as assistants to the main methods:

- **The CEO (main method)**: Makes high-level decisions
- **The manager (public methods)**: Coordinates tasks
- **The assistants (helper methods)**: Do specific work

The CEO does not stuff envelopes. The CEO tells the manager to handle mailings, and the manager delegates to assistants who stuff envelopes, apply postage, and deliver to the mailroom.

### Seeing Helper Methods in Action

**Problem:** Create a password strength checker.

```java
public class PasswordChecker {

    // Main public method - the "manager"
    public static String checkPasswordStrength(String password) {
        if (!isLongEnough(password)) {
            return "Weak: Password must be at least 8 characters";
        }

        int score = 0;
        if (hasUpperCase(password)) score++;
        if (hasLowerCase(password)) score++;
        if (hasDigit(password)) score++;
        if (hasSpecialChar(password)) score++;

        return getStrengthMessage(score);
    }

    // Helper methods - the "assistants"

    private static boolean isLongEnough(String password) {
        return password.length() >= 8;
    }

    private static boolean hasUpperCase(String password) {
        for (char c : password.toCharArray()) {
            if (Character.isUpperCase(c)) {
                return true;
            }
        }
        return false;
    }

    private static boolean hasLowerCase(String password) {
        for (char c : password.toCharArray()) {
            if (Character.isLowerCase(c)) {
                return true;
            }
        }
        return false;
    }

    private static boolean hasDigit(String password) {
        for (char c : password.toCharArray()) {
            if (Character.isDigit(c)) {
                return true;
            }
        }
        return false;
    }

    private static boolean hasSpecialChar(String password) {
        String special = "!@#$%^&*()_+-=[]{}|;:,.<>?";
        for (char c : password.toCharArray()) {
            if (special.indexOf(c) >= 0) {
                return true;
            }
        }
        return false;
    }

    private static String getStrengthMessage(int score) {
        if (score <= 1) return "Weak: Add more character types";
        if (score == 2) return "Fair: Consider adding more variety";
        if (score == 3) return "Good: Solid password";
        return "Excellent: Very strong password";
    }
}
```

**Notice:**

- `checkPasswordStrength()` is the main method - it coordinates
- Each helper does ONE specific check
- The main method is readable like a checklist
- Each helper can be tested independently
- If requirements change (e.g., minimum length becomes 10), change ONE method

---

## Understanding Methods Calling Methods

### What Is Method Chaining and Nesting?

**Method nesting** is when one method calls another method. This is fundamental to decomposition.

**Method chaining** is when the result of one method call is immediately used in another.

### Why Methods Call Other Methods

Think about how you follow a recipe:

1. "Make the sauce" - This itself involves multiple steps
2. You look up the sauce recipe, follow it, then continue with the main recipe

The main recipe "calls" the sauce recipe. Programming works the same way.

### Seeing Methods Calling Methods

**Simple nesting:**

```java
public static void main(String[] args) {
    displayResults();
}

public static void displayResults() {
    int result = calculateResult();    // Calls another method
    System.out.println("Result: " + result);
}

public static int calculateResult() {
    int a = getValue();    // Calls another method
    int b = getValue();
    return a + b;
}

public static int getValue() {
    return 42;
}
```

**Execution flow:**

```
main()
  -> displayResults()
       -> calculateResult()
            -> getValue()  // returns 42
            -> getValue()  // returns 42
            // returns 84
       // prints "Result: 84"
```

### Method Chaining Examples

**Using a returned value directly:**

```java
// Without chaining (verbose)
double bmi = calculateBMI(weight, height);
String category = getCategory(bmi);
System.out.println(category);

// With chaining (concise)
System.out.println(getCategory(calculateBMI(weight, height)));
```

**Building up results:**

```java
// Calculate a complex value step by step
public static double calculateFinalPrice(double basePrice, double taxRate, double discountPercent) {
    double afterTax = addTax(basePrice, taxRate);
    double afterDiscount = applyDiscount(afterTax, discountPercent);
    return roundToTwoDecimals(afterDiscount);
}

// Each step uses the result of the previous step
```

### The Call Stack Revisited

Remember the call stack from Week 4? When methods call other methods, the stack grows:

```java
public static void methodA() {
    System.out.println("A start");
    methodB();
    System.out.println("A end");
}

public static void methodB() {
    System.out.println("B start");
    methodC();
    System.out.println("B end");
}

public static void methodC() {
    System.out.println("C start");
    System.out.println("C end");
}
```

**Output:**
```
A start
B start
C start
C end
B end
A end
```

**Stack visualization:**

```
Step 1: [methodA]
Step 2: [methodA, methodB]
Step 3: [methodA, methodB, methodC]
Step 4: [methodA, methodB]  // methodC finished
Step 5: [methodA]           // methodB finished
Step 6: []                  // methodA finished
```

Each method completes in reverse order of when it was called. Last in, first out.

---

## Understanding Activity Diagrams and Pseudocode

### What Are These Planning Tools?

**Pseudocode** is informal, human-readable description of what your code should do. It is not real code, but it captures the logic.

**Activity diagrams** are visual flowcharts showing the flow of actions in a process.

### Why Plan Before Coding?

Planning before coding is like:

- Architects drawing blueprints before construction
- Chefs writing recipes before cooking
- Directors storyboarding before filming

It helps you:

1. **Think through the problem** before getting lost in syntax
2. **Spot issues early** when they are cheap to fix
3. **Communicate ideas** with others (or your future self)
4. **Break down complexity** into manageable steps

### Writing Pseudocode

Pseudocode uses natural language with programming concepts:

**Example: Password checker pseudocode**

```
FUNCTION checkPasswordStrength(password)
    IF password length < 8 THEN
        RETURN "Too short"
    END IF

    SET score = 0

    IF password has uppercase THEN
        INCREMENT score
    END IF

    IF password has lowercase THEN
        INCREMENT score
    END IF

    IF password has digit THEN
        INCREMENT score
    END IF

    IF password has special character THEN
        INCREMENT score
    END IF

    IF score <= 1 THEN RETURN "Weak"
    IF score = 2 THEN RETURN "Fair"
    IF score = 3 THEN RETURN "Good"
    RETURN "Excellent"
END FUNCTION
```

**Key pseudocode conventions:**

- Use CAPITALS for keywords (IF, THEN, RETURN, FOR, WHILE)
- Use indentation to show nesting
- Focus on WHAT, not HOW (ignore syntax details)
- Be specific enough to translate to code

### Drawing Activity Diagrams

Activity diagrams use these symbols:

| Symbol | Meaning |
|--------|---------|
| Filled circle | Start |
| Circle with ring | End |
| Rectangle (rounded) | Action/Activity |
| Diamond | Decision (yes/no) |
| Arrow | Flow direction |
| Horizontal bar | Fork (parallel) / Join |

**Example: Simple login process**

```
    [Start]
       |
       v
  +----------------+
  | Display login  |
  | form           |
  +----------------+
       |
       v
  +----------------+
  | Get username   |
  | and password   |
  +----------------+
       |
       v
      / \
     /   \
    /Valid?\
    \     /
     \   /
      \ /
    /     \
   Yes     No
    |       |
    v       v
+-------+ +----------------+
| Grant | | Display error  |
|access | | message        |
+-------+ +----------------+
    |       |
    v       |
 [End] <----+
```

### From Pseudocode to Code

**Step 1: Write pseudocode first**

```
FUNCTION calculateTotal(prices, taxRate)
    SET subtotal = 0
    FOR EACH price IN prices
        ADD price TO subtotal
    END FOR
    SET tax = subtotal * taxRate
    SET total = subtotal + tax
    RETURN total
END FUNCTION
```

**Step 2: Translate to Java**

```java
public static double calculateTotal(double[] prices, double taxRate) {
    double subtotal = 0;
    for (double price : prices) {
        subtotal += price;
    }
    double tax = subtotal * taxRate;
    double total = subtotal + tax;
    return total;
}
```

The pseudocode becomes your roadmap. Translation is mechanical once the logic is clear.

---

## Understanding Debugging Techniques

### What Is Debugging?

**Debugging** is the process of finding and fixing errors (bugs) in your code. The name comes from an actual moth found in an early computer!

### Why Systematic Debugging Matters

Debugging is NOT:
- Randomly changing code and hoping it works
- Staring at the screen waiting for insight
- Rewriting everything from scratch

Debugging IS:
- A systematic process
- Following clues like a detective
- Understanding WHAT happened vs WHAT should happen

### The Scientific Method for Debugging

1. **Observe**: What is the actual behavior?
2. **Hypothesize**: What might cause this?
3. **Test**: Check your hypothesis
4. **Conclude**: Was your hypothesis correct?
5. **Repeat**: If not, form a new hypothesis

### Common Debugging Techniques

**Technique 1: Print Statement Debugging**

Add print statements to see what is happening:

```java
public static int calculateTotal(int[] values) {
    System.out.println("DEBUG: Starting calculateTotal");
    System.out.println("DEBUG: values.length = " + values.length);

    int sum = 0;
    for (int i = 0; i < values.length; i++) {
        System.out.println("DEBUG: i=" + i + ", values[i]=" + values[i] + ", sum so far=" + sum);
        sum += values[i];
    }

    System.out.println("DEBUG: Final sum = " + sum);
    return sum;
}
```

This shows you exactly what happens at each step.

**Technique 2: Check Inputs and Outputs**

Verify that methods receive what they expect and return what they should:

```java
public static double divide(double a, double b) {
    System.out.println("divide() called with a=" + a + ", b=" + b);  // Check inputs

    if (b == 0) {
        System.out.println("ERROR: Division by zero!");
        return 0;
    }

    double result = a / b;
    System.out.println("divide() returning " + result);  // Check output
    return result;
}
```

**Technique 3: Isolate the Problem**

If a program has 10 methods and something is wrong:

1. Comment out code until the bug disappears
2. The last thing you commented out contains the bug
3. Or add code back gradually until the bug appears

**Technique 4: Test Methods Individually**

Create a simple test in `main` to verify one method works:

```java
public static void main(String[] args) {
    // Test calculateAverage in isolation
    int[] test1 = {10, 20, 30};
    double result1 = calculateAverage(test1);
    System.out.println("Test 1: Expected 20.0, Got " + result1);

    int[] test2 = {5};
    double result2 = calculateAverage(test2);
    System.out.println("Test 2: Expected 5.0, Got " + result2);

    int[] test3 = {};  // Edge case!
    double result3 = calculateAverage(test3);
    System.out.println("Test 3: Expected 0.0 (or error?), Got " + result3);
}
```

**Technique 5: Read the Error Message**

Error messages tell you:

- **What** went wrong (`NullPointerException`, `ArrayIndexOutOfBoundsException`)
- **Where** it happened (file name, line number)
- **How** you got there (stack trace)

```
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 5
    at Calculator.sumArray(Calculator.java:15)    <- The problem is here
    at Calculator.main(Calculator.java:5)          <- Called from here
```

This tells you: Line 15 of Calculator.java tried to access index 5 of an array with only 5 elements (indices 0-4).

### Common Bugs and Their Fixes

| Bug | Symptom | Likely Cause | Fix |
|-----|---------|--------------|-----|
| Off-by-one error | Loop runs one too many/few times | Using `<=` vs `<` or wrong starting value | Check loop bounds carefully |
| Null reference | `NullPointerException` | Variable was never initialized | Initialize before use |
| Logic error | Wrong result, no error | Incorrect condition or formula | Add print statements, trace manually |
| Scope error | "Cannot find symbol" | Variable not visible in this scope | Check where variable is declared |
| Type mismatch | "Incompatible types" | Wrong type assigned/returned | Check method return types |

---

## Connecting to What You Already Know

### Building on Week 4's Foundation

Everything from Week 4 still applies - this week adds new capabilities on top:

| Week 4 Concept | Week 5 Extension |
|----------------|------------------|
| One method with one signature | Multiple methods with same name (overloading) |
| Simple method calls | Methods calling other methods (composition) |
| Writing code directly | Planning with pseudocode first |
| Finding bugs by luck | Systematic debugging techniques |
| Methods as individual tools | Methods as orchestrated systems |

### Connecting to What Comes Next

**Week 6 (Arrays)**: You will write methods that process arrays:

```java
public static int findMax(int[] numbers) { ... }
public static double calculateAverage(int[] scores) { ... }
public static void sortArray(int[] values) { ... }
```

Decomposition becomes essential when working with complex data.

**Week 7+ (OOP)**: Objects have methods too! Method overloading becomes crucial:

```java
public class Rectangle {
    // Overloaded constructors
    public Rectangle() { ... }
    public Rectangle(int width, int height) { ... }

    // Overloaded methods
    public void scale(int factor) { ... }
    public void scale(double factor) { ... }
}
```

**Week 11 (File Handling)**: File operations are naturally method-based:

```java
public static void readFile(String filename) { ... }
public static void writeFile(String filename, String data) { ... }
```

The decomposition skills you learn this week directly apply.

---

## Common Struggles and How to Overcome Them

### Struggle 1: Deciding Method Granularity

**The confusion:** "How big should a method be? When is it too small or too big?"

**The solution:** Use these guidelines:

**Too small** (probably do not need a separate method):
```java
public static int addOne(int x) {
    return x + 1;  // Just use x + 1 directly
}
```

**Too big** (definitely should be split):
```java
public static void doEverything() {
    // 200 lines handling multiple responsibilities
}
```

**Just right** (one clear purpose):
```java
public static double calculateAverage(int[] scores) {
    // 5-20 lines focused on averaging
}
```

**Rule of thumb:** If you cannot describe what a method does in one sentence without using "and," it might be too big.

### Struggle 2: Understanding Overloading Resolution

**The confusion:** "Which version of my overloaded method will Java call?"

**The solution:** Java matches by finding the most specific match:

1. Exact match wins first
2. Then widening conversions (int -> long -> double)
3. Then boxing (int -> Integer)
4. Then varargs

```java
public static void print(int x) { System.out.println("int"); }
public static void print(double x) { System.out.println("double"); }
public static void print(String x) { System.out.println("String"); }

print(5);       // "int" - exact match
print(5.0);     // "double" - exact match
print("hi");    // "String" - exact match
print(5L);      // "double" - long widens to double (no long version)
```

### Struggle 3: Planning Before Coding

**The confusion:** "I want to just start coding. Why write pseudocode?"

**The solution:** Compare these two approaches:

**Without planning:**
1. Start coding
2. Get stuck
3. Delete code, try again
4. Get lost in details
5. End up with messy, buggy code
6. Spend hours debugging

**With planning:**
1. Write pseudocode (10 minutes)
2. Identify methods needed
3. Code each method systematically
4. Fewer bugs, clearer code
5. Finish faster overall

Planning feels slower but IS faster. Professional developers always plan complex features first.

### Struggle 4: Systematic Debugging Approach

**The confusion:** "My code does not work and I do not know why!"

**The solution:** Follow this debugging checklist:

1. **What is the error?** (Read the message carefully)
2. **Where is the error?** (Check the line number)
3. **What are the inputs?** (Print them out)
4. **What should happen?** (Trace manually)
5. **What actually happens?** (Print intermediate values)
6. **Where do they diverge?** (That is the bug location)

Never change code randomly. Always have a hypothesis about what is wrong before changing anything.

---

## Practice Exercises

### Exercise 1: Overloading sumUp (meget hjalp - Maximum Guidance)

**Goal:** Practice method overloading with the classic sumUp example.

**Step-by-step instructions:**

1. Create a new Java file called `SumCalculator.java`
2. Create three overloaded methods called `sumUp`:
   - Version 1: Takes two `int` parameters, returns their sum
   - Version 2: Takes three `int` parameters, returns their sum
   - Version 3: Takes two `double` parameters, returns their sum
3. In main, test all three versions:
   - `sumUp(5, 3)` should return 8
   - `sumUp(5, 3, 2)` should return 10
   - `sumUp(5.5, 3.3)` should return 8.8

**Starter code:**

```java
public class SumCalculator {

    public static void main(String[] args) {
        // Test all three versions
        System.out.println("sumUp(5, 3) = " + sumUp(5, 3));
        System.out.println("sumUp(5, 3, 2) = " + sumUp(5, 3, 2));
        System.out.println("sumUp(5.5, 3.3) = " + sumUp(5.5, 3.3));
    }

    // TODO: Create sumUp(int, int)

    // TODO: Create sumUp(int, int, int)

    // TODO: Create sumUp(double, double)
}
```

**Expected output:**

```
sumUp(5, 3) = 8
sumUp(5, 3, 2) = 10
sumUp(5.5, 3.3) = 8.8
```

### Exercise 2: Helper Method Practice (meget hjalp - Maximum Guidance)

**Goal:** Practice creating helper methods through problem decomposition.

**Step-by-step instructions:**

Create a program that prints a decorative message box. The output should look like:

```
********************
*                  *
*  Hello, World!   *
*                  *
********************
```

Use these methods:

1. `printBox(String message)` - The main method that coordinates
2. `printTopBottom(int width)` - Prints a line of asterisks
3. `printEmptyLine(int width)` - Prints asterisks on sides with spaces between
4. `printMessageLine(String message, int width)` - Prints the message centered

**Starter code:**

```java
public class MessageBox {

    public static void main(String[] args) {
        printBox("Hello, World!");
        System.out.println();
        printBox("Java is fun");
    }

    public static void printBox(String message) {
        int width = message.length() + 6;  // padding on each side

        printTopBottom(width);
        printEmptyLine(width);
        printMessageLine(message, width);
        printEmptyLine(width);
        printTopBottom(width);
    }

    // TODO: Implement printTopBottom
    // Should print 'width' asterisks

    // TODO: Implement printEmptyLine
    // Should print * then (width-2) spaces then *

    // TODO: Implement printMessageLine
    // Should print * then centered message then *
}
```

### Exercise 3: Temperature Converter (nogen hjalp - Moderate Guidance)

**Goal:** Practice overloading and helper methods together.

**Instructions:**

Create a temperature converter with these requirements:

1. Create overloaded `convert` methods:
   - `convert(double celsius)` - Converts Celsius to Fahrenheit
   - `convert(double value, String from, String to)` - Converts between any units

2. Create helper methods:
   - `celsiusToFahrenheit(double c)`
   - `fahrenheitToCelsius(double f)`
   - `celsiusToKelvin(double c)`
   - `kelvinToCelsius(double k)`

3. Test these conversions:
   - 0 C to F (should be 32)
   - 100 C to F (should be 212)
   - 98.6 F to C (should be 37)
   - 0 C to K (should be 273.15)

**Hint for the flexible convert method:**

```java
public static double convert(double value, String from, String to) {
    // First convert to Celsius (common base)
    double celsius;
    if (from.equals("C")) celsius = value;
    else if (from.equals("F")) celsius = fahrenheitToCelsius(value);
    else if (from.equals("K")) celsius = kelvinToCelsius(value);
    else return value;  // Unknown unit

    // Then convert from Celsius to target
    // ... your code here ...
}
```

### Exercise 4: Menu System with Pseudocode (nogen hjalp - Moderate Guidance)

**Goal:** Practice planning with pseudocode before coding.

**Instructions:**

**First, write pseudocode for a simple menu system:**

```
PROGRAM Menu System

REPEAT
    Display menu options:
        1. Say Hello
        2. Calculate Sum
        3. Exit

    Get user choice

    IF choice is 1 THEN
        Ask for name
        Display greeting
    ELSE IF choice is 2 THEN
        Ask for two numbers
        Display their sum
    ELSE IF choice is 3 THEN
        Display goodbye
        Exit program
    ELSE
        Display "Invalid choice"
    END IF

UNTIL user chooses exit
```

**Then, implement using these methods:**

- `run()` - Main loop
- `displayMenu()` - Shows options
- `getUserChoice()` - Returns the choice as int
- `handleHello()` - Handles option 1
- `handleSum()` - Handles option 2

### Exercise 5: Simple Black Jack (ingen hjalp - Minimal Guidance)

**Goal:** Apply all Week 5 concepts to a mini-project.

**Requirements:**

Create a simplified Black Jack game with these rules:

1. The player starts with 2 cards (random values 1-11)
2. The player can "hit" (get another card) or "stand" (keep current hand)
3. If the total exceeds 21, the player "busts" and loses
4. If the player stands, compare to a dealer total (random 17-21)
5. Higher total wins (without busting)

**Methods you should create:**

Planning methods:
- Write pseudocode first
- Identify 5-7 methods you will need

Core methods:
- `dealCard()` - Returns a random card value (1-11)
- `calculateTotal(int[] cards)` - Sums the cards
- `displayHand(int[] cards)` - Shows the cards
- `isOverloaded versions of display methods` - Practice overloading

Game flow methods:
- `playRound()` - Handles one round
- `playerTurn()` - Manages hit/stand decisions
- `determineWinner(int playerTotal, int dealerTotal)`

**Sample output:**

```
=== SIMPLE BLACK JACK ===

Your cards: [7, 5]
Your total: 12

Hit or Stand? (h/s): h
You drew: 6
Your total: 18

Hit or Stand? (h/s): s

Dealer total: 19
Dealer wins!

Play again? (y/n):
```

---

## Looking Ahead

This week you learned to design with methods - overloading, decomposition, helper methods, planning, and debugging. These skills become increasingly important as programs grow more complex.

- **Week 6 (Arrays):** Arrays are collections of data, and processing them efficiently requires well-designed methods. You will write methods like `findMax(int[] numbers)` that combine loops with method design.

- **Week 7+ (OOP):** Object-oriented programming uses method overloading extensively, especially in constructors. You will see classes like:
  ```java
  public class Student {
      public Student() { }  // Default constructor
      public Student(String name) { }  // Overloaded
      public Student(String name, int age) { }  // Overloaded again
  }
  ```

- **Week 11 (File Handling):** File operations are naturally organized into methods. Decomposition helps manage the complexity of reading, processing, and writing data.

- **Week 13 (Unit Testing):** Testing verifies that individual methods work correctly. The decomposed, focused methods you learn to write this week are perfect for testing.

The planning and debugging skills you develop now will serve you throughout your programming career. Professional software development is largely about managing complexity, and methods are your primary tool for that.

---

## Key Takeaways

- **Method overloading** lets you create multiple methods with the same name but different parameter lists
- Java distinguishes overloaded methods by **number, types, and order** of parameters (not return type or parameter names)
- **Problem decomposition** breaks complex problems into smaller, manageable methods
- The **Single Responsibility Principle** says each method should do one thing well
- **Helper methods** handle specific subtasks for other methods
- Methods calling other methods creates a **hierarchy** of responsibility
- **Pseudocode** helps you plan logic before writing Java syntax
- **Activity diagrams** visualize the flow of your program
- **Systematic debugging** uses a scientific approach: observe, hypothesize, test, conclude
- Print statements are your friend when debugging - show what is actually happening
- Plan before coding - it feels slower but results in faster completion
- Good decomposition makes code readable, testable, and maintainable

---

## For the Next Topic Agent

### Terminology Established This Week

- **method overloading**: Having multiple methods with the same name but different parameter lists
- **method signature**: The combination of method name, parameter types, and parameter order (NOT return type)
- **problem decomposition**: Breaking a large problem into smaller, manageable pieces
- **top-down design**: Starting with the big picture and breaking down into details
- **helper method**: A method that assists other methods with specific subtasks
- **method composition**: Building complex behavior by having methods call other methods
- **method chaining**: Using the result of one method call directly in another
- **pseudocode**: Informal, human-readable description of program logic
- **activity diagram**: Visual flowchart showing the flow of actions in a process
- **debugging**: The process of finding and fixing errors in code
- **Single Responsibility Principle**: A method should do one thing and do it well

### Example Classes/Concepts Created

- Greeter with overloaded greet() methods
- SumCalculator with three sumUp() versions
- PasswordChecker with helper methods for each check
- Temperature converter with overloaded convert() methods
- MessageBox with decomposed printing methods
- Simple Black Jack game with full decomposition

### Student Capabilities After This Week

Students can now:
- Create overloaded methods with different parameter lists
- Understand how Java resolves which overloaded method to call
- Break complex problems into smaller methods (decomposition)
- Create helper methods for specific subtasks
- Write pseudocode to plan before coding
- Draw simple activity diagrams
- Debug systematically using print statements
- Test methods individually
- Read and interpret error messages and stack traces
- Decide when to create a method vs inline code

### Pedagogical Patterns Continued

- **Restaurant kitchen analogy**: Problem decomposition as chef delegation
- **Toolbox analogy**: Method overloading as having the right tool for each job
- **GPS navigation analogy**: Planning before execution
- **Scientific method**: Systematic debugging approach
- **Building blocks analogy**: Week 4 = bricks, Week 5 = structures
- **Progressive complexity**: From simple overloading to mini-project

### Critical Connections for Week 6 (Arrays)

- Arrays require methods for processing (findMax, calculateAverage, sort)
- Loops from Week 3 + methods from Weeks 4-5 = array processing power
- Helper methods become essential for array algorithms
- Decomposition is crucial when working with collections of data
- Debugging array-related bugs (off-by-one errors, bounds checking)
