# Methods Part 1 - Week 4

*Prerequisites: Week 3 - Loops*
*Phase: Phase 2: Decomposition and Abstraction*

---

## What You'll Learn

By the end of this week, you will be able to:

- **Decompose problems** into smaller, reusable pieces using methods
- **Create methods** with proper syntax (return type, name, parameters, body)
- **Call methods** from other parts of your code
- Understand the difference between **parameters** and **arguments**
- Create methods that **return values** and methods that return **void**
- Understand **variable scope** (where variables can be accessed)
- Follow **method naming conventions** (verb-based, descriptive names)
- Trace the **flow of control** when methods are called and return

This week marks a pivotal shift in how you think about programming. Instead of writing one long sequence of instructions, you will learn to organize your code into named, reusable building blocks. This is the foundation of professional software development!

---

## Why This Matters

In the first three weeks, you wrote programs where all the code lived in the `main` method. While this works for simple programs, imagine you needed to calculate a BMI for 100 different people, or validate 50 different inputs. Without methods, you would copy and paste the same code over and over again.

Consider these real-world scenarios:

- A **fitness app** needs to calculate BMI in multiple places (user profile, progress tracker, goal setting)
- A **banking system** validates account numbers hundreds of times throughout the code
- A **game** checks collision detection for every object, every frame
- A **recipe website** converts measurements (cups to milliliters) throughout every recipe

Methods solve these problems by letting you:

1. **Write code once, use it many times** - No more copy-pasting
2. **Give meaningful names to complex operations** - `calculateBMI()` is clearer than 5 lines of math
3. **Hide complexity** - Other parts of your code do not need to know HOW something works, just WHAT it does
4. **Find and fix bugs in one place** - If your BMI calculation is wrong, fix it once, and everywhere is fixed
5. **Collaborate with others** - Different team members can work on different methods

Methods are like the paragraphs of programming. Just as good writing is organized into paragraphs that each make one point, good code is organized into methods that each do one thing.

---

## Building Your Intuition

### The Big Picture: What Is a Method?

A **method** is a named block of code that performs a specific task. You give it a name, and whenever you want to perform that task, you call it by name.

Think about this: In daily life, you do not explain every detail every time you describe an activity. You say "I brushed my teeth" - not "I picked up the toothbrush, applied toothpaste, moved the brush back and forth across each tooth for 30 seconds, rinsed..." The phrase "brush teeth" is like a method name - it represents a whole sequence of steps.

### The Recipe Analogy

Imagine you are writing a cookbook. Each recipe is like a method:

```
Recipe: makeScrambledEggs
Ingredients needed: 2 eggs, butter, salt
Steps:
  1. Crack eggs into bowl
  2. Beat eggs with fork
  3. Melt butter in pan
  4. Pour eggs into pan
  5. Stir until cooked
  6. Add salt
Result: Returns a plate of scrambled eggs
```

This recipe has:
- A **name**: `makeScrambledEggs`
- **Ingredients** (inputs): eggs, butter, salt - these are like **parameters**
- **Steps**: The code inside the method
- A **result**: The eggs - this is like a **return value**

When you want scrambled eggs, you do not re-explain the recipe every time. You just say "make scrambled eggs with 2 eggs" and follow the named recipe.

### The TV Remote Analogy

Think of a TV remote control. Each button is like a method:

- Press `volumeUp()` - the TV knows how to increase volume
- Press `changeChannel(7)` - you provide which channel (a parameter), and the TV does the rest
- Press `mute()` - no input needed, it just performs the action

You do not know exactly what happens inside the TV when you press a button - and you do not need to know. You just trust that `volumeUp()` will make things louder. This is called **abstraction** - hiding the complex details behind a simple interface.

### The Factory Worker Analogy

Imagine a factory worker whose job is to paint cars. You can think of this worker as a method:

```
Worker: paintCar
Input needed: A car, a color
Process: Apply primer, apply paint coats, let dry, apply clear coat
Output: Returns the painted car
```

When you need a car painted:
1. You **call** the worker (invoke the method)
2. You **give them what they need** (pass arguments: the car and color)
3. They **do their job** (execute the method body)
4. They **give you back the result** (return the painted car)

The manager does not need to know HOW to paint cars. They just need to know that this worker CAN paint cars if given the right inputs.

### Connecting to What You Already Know

Over the past three weeks, you have built up essential skills:

**From Week 1 (Input/Output/Types):**
- You know about data types (`int`, `double`, `String`, `boolean`)
- You know how to declare variables
- These become the building blocks for method parameters and return types

**From Week 2 (Conditions):**
- You can write decision-making code with if/else
- Methods often contain conditionals to handle different situations

**From Week 3 (Loops):**
- You can repeat actions with for/while loops
- Methods often encapsulate loop logic (like "sum all numbers from 1 to N")

Now, methods let you **organize** all this knowledge into reusable pieces. A method might contain variables, conditionals, AND loops - all wrapped up with a meaningful name.

---

## Understanding Methods: The Foundation

### What Is a Method Declaration?

A **method declaration** (also called a method definition) is where you write the code that defines what a method does. It is like writing a recipe before you can follow it.

### Why Do We Declare Methods?

Before you can use a method, Java needs to know:
1. What is the method's name?
2. What inputs does it need (if any)?
3. What type of result does it return (if any)?
4. What steps should it perform?

### How Methods Are Structured

Every method has these parts:

```
[access modifier] [static] returnType methodName(parameterList) {
    // method body - the code that runs when method is called
    return value; // if not void
}
```

Let us break this down:

| Part | Purpose | Example |
|------|---------|---------|
| Access modifier | Who can use this method | `public`, `private` |
| static | Whether the method belongs to the class or objects | `static` (for now, always use this) |
| Return type | What type of value comes back | `int`, `double`, `String`, `void` |
| Method name | What you call to use this method | `calculateSum`, `printGreeting` |
| Parameter list | What inputs the method needs | `(int x, int y)` or `()` for none |
| Method body | The code that runs | `{ ... }` |
| Return statement | What value to send back | `return result;` |

### Seeing a Method Declaration

```java
//        return type
//        |     method name
//        |     |          parameters
//        |     |          |
public static int addNumbers(int a, int b) {
    int sum = a + b;    // method body
    return sum;         // return statement
}
```

This method:
- Returns an `int`
- Is named `addNumbers`
- Takes two `int` parameters named `a` and `b`
- Adds them together and returns the result

### Common Mistakes with Method Declarations

**Mistake 1: Forgetting the return statement**

```java
public static int multiply(int x, int y) {
    int result = x * y;
    // COMPILER ERROR! Method says it returns int, but no return statement!
}
```

**Fix:**
```java
public static int multiply(int x, int y) {
    int result = x * y;
    return result;  // Now the method properly returns the result
}
```

**Mistake 2: Wrong return type**

```java
public static int divide(int x, int y) {
    return x / (double)y;  // ERROR! Returns double, but declared as int
}
```

**Fix:**
```java
public static double divide(int x, int y) {  // Changed return type to double
    return x / (double)y;
}
```

**Mistake 3: Trying to return from a void method**

```java
public static void printMessage(String msg) {
    System.out.println(msg);
    return msg;  // ERROR! void methods cannot return a value
}
```

**Fix:**
```java
public static void printMessage(String msg) {
    System.out.println(msg);
    // No return statement needed (or use just: return;)
}
```

---

## Understanding Calling Methods

### What Does "Calling a Method" Mean?

**Calling a method** (also called **invoking** a method) means asking the method to execute its code. When you call a method, the program:
1. Pauses what it was doing
2. Jumps to the method's code
3. Executes all the steps in the method
4. Returns back to where it left off

### Why Do We Call Methods?

You call a method when you want to use the functionality it provides. Writing a method is like writing a recipe; calling a method is like following that recipe.

### How to Call a Method

The syntax is:

```java
// For methods that return a value:
variableType result = methodName(arguments);

// For void methods (no return value):
methodName(arguments);
```

### Seeing Method Calls in Action

```java
public class Calculator {
    public static void main(String[] args) {
        // CALLING the addNumbers method
        int total = addNumbers(5, 3);  // total becomes 8
        System.out.println("Sum: " + total);

        // Calling again with different arguments
        int anotherTotal = addNumbers(10, 20);  // anotherTotal becomes 30
        System.out.println("Sum: " + anotherTotal);

        // You can also use the result directly
        System.out.println("Sum: " + addNumbers(100, 200));  // Prints 300
    }

    public static int addNumbers(int a, int b) {
        int sum = a + b;
        return sum;
    }
}
```

**What happens when `addNumbers(5, 3)` is called:**

1. Java sees `addNumbers(5, 3)`
2. It finds the method `addNumbers`
3. It assigns: `a = 5` and `b = 3` (parameters get argument values)
4. It executes: `int sum = a + b;` (sum becomes 8)
5. It executes: `return sum;` (sends 8 back)
6. Back in main, `total` receives the value 8

### Tracing Method Calls

Here is a visual trace of what happens:

```
main() starts
  |
  v
int total = addNumbers(5, 3);  <-- Call method
  |
  +---> Enter addNumbers(a=5, b=3)
        |
        int sum = 5 + 3 = 8
        |
        return 8  <-- Send value back
        |
  <----+
  |
total = 8  <-- Receive returned value
  |
  v
System.out.println("Sum: " + total);  <-- Prints "Sum: 8"
```

### Common Mistakes When Calling Methods

**Mistake 1: Forgetting parentheses**

```java
int result = addNumbers;  // ERROR! Missing parentheses
```

**Fix:**
```java
int result = addNumbers(5, 3);  // Correct: parentheses with arguments
```

**Mistake 2: Wrong number of arguments**

```java
int result = addNumbers(5);  // ERROR! Method expects 2 arguments, got 1
```

**Fix:**
```java
int result = addNumbers(5, 3);  // Correct: provide all required arguments
```

**Mistake 3: Ignoring the return value when you need it**

```java
addNumbers(5, 3);  // The result (8) is calculated but thrown away!
System.out.println(/* What goes here? We lost the result! */);
```

**Fix:**
```java
int result = addNumbers(5, 3);  // Store the result
System.out.println(result);     // Now we can use it
```

---

## Understanding Parameters vs Arguments

This distinction confuses almost everyone at first. Let us make it crystal clear.

### What Are Parameters?

**Parameters** are the **variables declared in the method definition**. They are placeholders that say "I will need values of these types."

Think of parameters as empty labeled boxes waiting to receive items.

### What Are Arguments?

**Arguments** are the **actual values you provide when calling the method**. They are the real data that fills those placeholder boxes.

### The Key Difference

```java
// Parameters: Declared in method header - these are NAMES (placeholders)
public static void greet(String name, int times) {  // name and times are PARAMETERS
    for (int i = 0; i < times; i++) {
        System.out.println("Hello, " + name + "!");
    }
}

// Arguments: Provided when calling - these are VALUES
public static void main(String[] args) {
    greet("Alice", 3);   // "Alice" and 3 are ARGUMENTS
    greet("Bob", 2);     // "Bob" and 2 are ARGUMENTS
}
```

### The Envelope Analogy

Think of mailing a letter:

- **Parameters** are like the blank lines on an envelope template: "TO: _______, ADDRESS: _______"
- **Arguments** are what you actually write on those lines: "TO: John Smith, ADDRESS: 123 Main St"

The template (method definition) has placeholders (parameters). Each time you send a letter (call the method), you fill in those placeholders with actual information (arguments).

### The Restaurant Order Analogy

At a restaurant:

- The **menu** lists dishes with customizable options: "Burger (size: ___, toppings: ___)"
- These blanks are like **parameters** - they define what choices exist
- When you order, you say "Burger, large, with cheese and bacon"
- These specific choices are like **arguments** - the actual values you provide

### Matching Arguments to Parameters

Arguments are matched to parameters **by position**, not by name:

```java
public static void describePerson(String name, int age, double height) {
    System.out.println(name + " is " + age + " years old and " + height + " cm tall.");
}

// When calling:
describePerson("Maria", 25, 165.5);
// "Maria" goes to name (1st parameter)
// 25 goes to age (2nd parameter)
// 165.5 goes to height (3rd parameter)
```

### Common Mistakes with Parameters and Arguments

**Mistake 1: Arguments in wrong order**

```java
describePerson(25, "Maria", 165.5);  // ERROR! 25 is not a String, "Maria" is not an int
```

**Fix:**
```java
describePerson("Maria", 25, 165.5);  // Types match: String, int, double
```

**Mistake 2: Confusing parameter names with argument values**

```java
int age = 30;
describePerson("John", age, 180.0);  // This works! 'age' is a variable with value 30
// The parameter is also named 'age', but they are different variables!
```

This is not an error, but it can be confusing. The variable `age` in main and the parameter `age` in the method are DIFFERENT variables that happen to have the same name.

---

## Understanding Return Values

### What Is a Return Value?

A **return value** is the result that a method sends back to whoever called it. It is like the answer to a question.

### Why Do Methods Return Values?

Methods return values when they compute something that the caller needs to use. For example:
- A `calculateArea()` method returns the area so you can display it or use it in further calculations
- A `findMaximum()` method returns which number is largest
- A `isValidEmail()` method returns true or false

### How Return Values Work

```java
public static double calculateCircleArea(double radius) {
    double area = 3.14159 * radius * radius;
    return area;  // Send this value back to whoever called
}

public static void main(String[] args) {
    // The returned value (28.27...) becomes the value of circleArea
    double circleArea = calculateCircleArea(3.0);
    System.out.println("Area: " + circleArea);
}
```

### The Vending Machine Analogy

A vending machine is a method that returns a value:

1. You **call** the machine (select a product)
2. You **provide arguments** (insert money, press button B4)
3. The machine **processes** your request (internal machinery)
4. The machine **returns** a snack (the return value)

The returned snack is now yours to use however you want - eat it, give it away, or store it for later. Similarly, a returned value is yours to store in a variable, print, or use in calculations.

### Using Return Values Directly

You do not always need to store a return value in a variable:

```java
// Store in variable, then use
double area = calculateCircleArea(5.0);
System.out.println("Area: " + area);

// Use directly without storing
System.out.println("Area: " + calculateCircleArea(5.0));

// Use in calculations
double totalArea = calculateCircleArea(3.0) + calculateCircleArea(4.0);
```

### The Return Statement Immediately Exits

When Java hits a `return` statement, the method ends immediately:

```java
public static int getFirst(int a, int b) {
    return a;                    // Method ends here!
    System.out.println("This never runs");  // Unreachable code!
}
```

This can be useful for early exits:

```java
public static String getLetterGrade(int score) {
    if (score < 0 || score > 100) {
        return "Invalid";  // Exit early for bad input
    }

    if (score >= 90) return "A";
    if (score >= 80) return "B";
    if (score >= 70) return "C";
    if (score >= 60) return "D";
    return "F";
}
```

---

## Understanding Void Methods

### What Is a Void Method?

A **void method** is a method that performs an action but does not return a value. The keyword `void` means "nothing" - the method returns nothing.

### Why Use Void Methods?

Some methods exist purely for their side effects - things they DO rather than values they PRODUCE:
- Print something to the screen
- Modify a display
- Play a sound
- Save data to a file

These methods perform actions; they do not calculate answers.

### How Void Methods Work

```java
public static void printGreeting(String name) {
    System.out.println("Hello, " + name + "!");
    System.out.println("Welcome to our program.");
    // No return statement needed (or you can use: return;)
}

public static void main(String[] args) {
    printGreeting("Alice");  // Just call it - no value comes back
    printGreeting("Bob");

    // This would be an ERROR:
    // String result = printGreeting("Charlie");  // void methods return nothing!
}
```

### Void vs Return: The Printer vs Calculator Analogy

Think of two machines:

**A Calculator (method with return value):**
- You input numbers
- It computes internally
- It GIVES YOU BACK a result that you can use

**A Printer (void method):**
- You input a document
- It performs an action (prints)
- It does NOT give you anything back - the action IS the purpose

```java
// Calculator: gives back a value
public static int add(int a, int b) {
    return a + b;  // You get this back
}

// Printer: performs action, gives nothing back
public static void printSum(int a, int b) {
    System.out.println(a + b);  // Action happens, nothing returned
}
```

### Common Mistake: Confusing Print and Return

This is the #1 confusion for beginners:

```java
// WRONG understanding: "I printed it, so it returned"
public static void calculateArea(double radius) {  // void - returns nothing
    double area = 3.14159 * radius * radius;
    System.out.println(area);  // This PRINTS, it does NOT return
}

// Trying to use the "result":
double myArea = calculateArea(5.0);  // ERROR! void methods return nothing

// CORRECT: return the value if you need to use it
public static double calculateArea(double radius) {  // double - returns a value
    double area = 3.14159 * radius * radius;
    return area;  // This RETURNS the value
}

// Now you can use it:
double myArea = calculateArea(5.0);  // Works! myArea is 78.54...
```

**Remember:**
- `System.out.println()` displays on screen - for humans to see
- `return` sends a value back to the code - for the program to use

You might want BOTH:
```java
public static double calculateArea(double radius) {
    double area = 3.14159 * radius * radius;
    System.out.println("Calculated area: " + area);  // Show the user
    return area;  // Also return for the program to use
}
```

---

## Understanding Variable Scope

### What Is Scope?

**Scope** refers to where in your code a variable can be accessed. A variable's scope is the region of code where that variable exists and can be used.

This is one of the most confusing topics for beginners, so let us break it down carefully.

### Why Does Scope Exist?

Scope exists to:
1. **Prevent naming conflicts** - Different methods can use variables named `i` or `count` without interfering
2. **Manage memory** - Variables are created when needed and destroyed when no longer needed
3. **Protect data** - Variables inside a method cannot be accidentally changed by other methods

### Local Variables: The Most Common Type

A **local variable** is declared inside a method and only exists within that method. It is "local" to that method - other methods cannot see it.

```java
public static void methodOne() {
    int x = 10;  // x is LOCAL to methodOne
    System.out.println(x);  // Works fine
}

public static void methodTwo() {
    System.out.println(x);  // ERROR! x does not exist here
}
```

### The Hotel Room Analogy

Think of methods as hotel rooms and variables as items in those rooms:

- Each room (method) has its own items (variables)
- Items in Room 101 (methodOne) cannot be seen from Room 102 (methodTwo)
- When you leave a room (method ends), the items in that room are gone
- Two rooms can have items with the same name (both rooms might have a lamp) without confusion

```java
public static void room101() {
    int lamp = 1;      // This lamp exists only in room 101
}

public static void room102() {
    int lamp = 2;      // This is a DIFFERENT lamp, only in room 102
    // They do not interfere with each other
}
```

### Parameters Are Also Local

Parameters are local variables too - they only exist inside their method:

```java
public static void greet(String name) {  // 'name' is local to greet
    System.out.println("Hello, " + name);
}

public static void main(String[] args) {
    greet("Alice");
    System.out.println(name);  // ERROR! 'name' does not exist in main
}
```

### Block Scope: Even More Local

Variables declared inside blocks (like if statements or loops) only exist in that block:

```java
public static void example() {
    int x = 10;  // x exists in the whole method

    if (x > 5) {
        int y = 20;  // y only exists inside this if block
        System.out.println(x + y);  // Works: both x and y are visible
    }

    System.out.println(x);  // Works: x is still in scope
    System.out.println(y);  // ERROR! y no longer exists
}
```

### Visualizing Scope

```java
public static void main(String[] args) {
    //
    // main's scope starts here
    //
    int a = 1;

    for (int i = 0; i < 5; i++) {
        //
        // loop's scope starts here (i exists)
        //
        int b = 2;  // b exists only in loop
        System.out.println(a + b + i);  // Can see a, b, and i
        //
        // loop's scope ends here (i and b are gone after last iteration)
        //
    }

    System.out.println(a);  // Works
    // System.out.println(b);  // ERROR - b is gone
    // System.out.println(i);  // ERROR - i is gone
    //
    // main's scope ends here
    //
}
```

### Why Variables Do Not Pass Between Methods

Each method call creates a fresh set of local variables. When the method ends, those variables are destroyed.

```java
public static void setNumber() {
    int number = 42;  // Created when setNumber() starts
    // number is destroyed when setNumber() ends
}

public static void useNumber() {
    System.out.println(number);  // ERROR! number does not exist here
}
```

**To share data between methods, use parameters and return values:**

```java
public static int createNumber() {
    int number = 42;
    return number;  // Send the value out before method ends
}

public static void main(String[] args) {
    int myNumber = createNumber();  // Receive the value
    System.out.println(myNumber);   // Works! myNumber is 42
}
```

### Common Mistake: Shadowing Variables

If you declare a variable with the same name as one in an outer scope, you "shadow" the outer one:

```java
public static void example() {
    int x = 10;

    if (true) {
        int x = 20;  // This SHADOWS the outer x - usually a bad idea
        System.out.println(x);  // Prints 20 (inner x)
    }

    System.out.println(x);  // Prints 10 (outer x)
}
```

This is confusing and usually a mistake. Use different names to be clear.

---

## Understanding the Call Stack (Conceptual)

### What Is the Call Stack?

The **call stack** is how Java keeps track of which method is currently running and where to return when it finishes. Think of it as a stack of plates - you add plates on top, and remove them from the top.

### Why Does the Call Stack Matter?

Understanding the call stack helps you:
- Trace how your program executes
- Read error messages (stack traces)
- Debug when things go wrong

### The Stack of Books Analogy

Imagine you are reading a textbook and encounter a reference: "See Chapter 3 for details on X."

1. You put a bookmark in your current page (remember where you were)
2. You flip to Chapter 3 and read it
3. Chapter 3 says "See Appendix A for the formula"
4. You bookmark Chapter 3 and flip to Appendix A
5. You finish Appendix A and return to your bookmark in Chapter 3
6. You finish Chapter 3 and return to your original bookmark

This is exactly how method calls work! Each "bookmark" is an entry on the call stack.

### Visualizing the Call Stack

```java
public static void main(String[] args) {
    System.out.println("Starting main");
    methodA();
    System.out.println("Back in main");
}

public static void methodA() {
    System.out.println("In methodA");
    methodB();
    System.out.println("Back in methodA");
}

public static void methodB() {
    System.out.println("In methodB");
}
```

**Output:**
```
Starting main
In methodA
In methodB
Back in methodA
Back in main
```

**Call stack visualization:**

```
Step 1: main() is called
Stack: [main]

Step 2: methodA() is called from main
Stack: [main, methodA]

Step 3: methodB() is called from methodA
Stack: [main, methodA, methodB]

Step 4: methodB() finishes, returns to methodA
Stack: [main, methodA]

Step 5: methodA() finishes, returns to main
Stack: [main]

Step 6: main() finishes
Stack: []
```

### Stack Traces in Error Messages

When your program crashes, Java shows you the call stack. This is incredibly helpful for debugging:

```
Exception in thread "main" java.lang.ArithmeticException: / by zero
    at Calculator.divide(Calculator.java:15)
    at Calculator.calculate(Calculator.java:10)
    at Calculator.main(Calculator.java:5)
```

Read this from bottom to top:
1. `main` called `calculate` (line 5)
2. `calculate` called `divide` (line 10)
3. `divide` crashed with division by zero (line 15)

This tells you exactly where the problem is and how you got there!

---

## Understanding Static Methods

### What Does Static Mean?

For now, think of `static` as meaning "this method belongs to the class itself, not to an object." Since we have not learned about objects yet (that is Week 7!), ALL your methods should be `static`.

### Why Do We Need Static Right Now?

The `main` method is static. To call other methods directly from `main`, those methods must also be static. Otherwise, Java does not know how to find them.

```java
public class Example {
    public static void main(String[] args) {
        helper();  // Works because helper is static
        // Without static on helper, this would be an error
    }

    public static void helper() {  // Must be static to be called from static main
        System.out.println("I am helping!");
    }
}
```

### The Simple Rule for Now

**Until you learn about objects in Week 7, always make your methods `public static`.**

```java
public static returnType methodName(parameters) {
    // method body
}
```

### What Happens Without Static

If you forget `static`, you will see an error like:

```
Error: non-static method helper() cannot be referenced from a static context
```

This means you tried to call a non-static method from a static method (like `main`). Just add `static` to fix it for now. We will explain the deeper reason in Week 7.

---

## Understanding the run() Method Pattern

### What Is the run() Method Pattern?

Instead of putting all your code in `main`, a common pattern is to have `main` simply create an instance and call a `run()` method. However, since we are not using objects yet, we can adapt this pattern:

```java
public class MyProgram {
    public static void main(String[] args) {
        run();  // main just calls run
    }

    public static void run() {
        // All the main program logic goes here
        greetUser();
        doCalculations();
        showResults();
    }

    public static void greetUser() {
        System.out.println("Welcome!");
    }

    public static void doCalculations() {
        // ...
    }

    public static void showResults() {
        // ...
    }
}
```

### Why Use This Pattern?

1. **Cleaner organization** - `main` is just a starting point
2. **Easier testing** - You can test `run()` independently
3. **Prepares you for OOP** - This pattern becomes important with objects
4. **Separation of concerns** - `main` handles startup, `run` handles logic

---

## Method Naming Conventions

### The Golden Rules

1. **Use verbs** - Methods DO things, so their names should describe actions
2. **Be descriptive** - A reader should understand what the method does from its name
3. **Use camelCase** - Start lowercase, capitalize each new word
4. **Avoid abbreviations** - `calculateTotal` not `calcTot`

### Good Method Names

| Method Name | Why It's Good |
|-------------|---------------|
| `calculateArea()` | Verb + what it calculates |
| `printReceipt()` | Verb + what it prints |
| `isValidEmail()` | Predicate (returns boolean) starts with is/has/can |
| `getUserInput()` | Verb + what it gets |
| `convertToMetric()` | Verb + what it converts to |
| `findMaxValue()` | Verb + what it finds |

### Bad Method Names

| Bad Name | Why It's Bad | Better Name |
|----------|--------------|-------------|
| `area()` | Not a verb | `calculateArea()` |
| `doIt()` | Too vague | `processOrder()` |
| `x()` | Meaningless | `validateInput()` |
| `CalculateSum()` | Starts with capital | `calculateSum()` |
| `calc_sum()` | Uses underscores | `calculateSum()` |
| `getAge()` | (for a void method) | `printAge()` |

### Boolean Methods: Special Naming

Methods that return `boolean` typically start with:
- `is` - `isValid()`, `isEmpty()`, `isOver18()`
- `has` - `hasPermission()`, `hasItems()`
- `can` - `canProceed()`, `canEdit()`

```java
public static boolean isValidAge(int age) {
    return age >= 0 && age <= 150;
}

public static boolean hasEnoughBalance(double balance, double amount) {
    return balance >= amount;
}
```

---

## Connecting to What You Already Know

### Methods Can Contain Loops

All those loop patterns from Week 3 can now be wrapped in methods:

```java
// Week 3: Loop to sum numbers
int sum = 0;
for (int i = 1; i <= 100; i++) {
    sum += i;
}

// Week 4: Same logic, but in a reusable method!
public static int sumUpTo(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

// Now use it anywhere:
int total1 = sumUpTo(100);   // 5050
int total2 = sumUpTo(1000);  // 500500
```

### Methods Can Contain Conditionals

Decision logic from Week 2 can also be encapsulated:

```java
// Week 2: If-else chain for grades
if (score >= 90) {
    grade = "A";
} else if (score >= 80) {
    // ...
}

// Week 4: As a reusable method
public static String getLetterGrade(int score) {
    if (score >= 90) return "A";
    if (score >= 80) return "B";
    if (score >= 70) return "C";
    if (score >= 60) return "D";
    return "F";
}

// Use it for any student:
String aliceGrade = getLetterGrade(95);  // "A"
String bobGrade = getLetterGrade(73);    // "C"
```

### Methods Can Call Other Methods

You can build complex behavior from simple pieces:

```java
public static void main(String[] args) {
    printStudentReport("Alice", 92);
}

public static void printStudentReport(String name, int score) {
    String grade = getLetterGrade(score);  // Call another method
    boolean passing = isPassing(score);     // Call another method

    System.out.println("Student: " + name);
    System.out.println("Score: " + score);
    System.out.println("Grade: " + grade);
    System.out.println("Passing: " + passing);
}

public static String getLetterGrade(int score) {
    if (score >= 90) return "A";
    if (score >= 80) return "B";
    if (score >= 70) return "C";
    if (score >= 60) return "D";
    return "F";
}

public static boolean isPassing(int score) {
    return score >= 60;
}
```

---

## Common Struggles and How to Overcome Them

### Struggle 1: Understanding When to Create a Method

**The confusion:** "How do I know when to make something a method?"

**The solution:** Create a method when you see:
1. **Repetition** - You wrote the same (or similar) code twice
2. **Complexity** - A block of code is more than 10-15 lines
3. **A clear purpose** - You can describe what the code does in one sentence
4. **Reusability** - The code might be useful elsewhere

**Memory trick:** If you can name it, you can method it. If you catch yourself saying "this part calculates the total" or "this part validates the input," those are candidates for methods.

### Struggle 2: Confusion About Return vs Print

**The confusion:** "I printed the answer, why can I not use it?"

**The solution:** Remember the key difference:
- `System.out.println()` - Shows on screen for HUMANS to see
- `return` - Sends back to CODE for the PROGRAM to use

```java
// WRONG: Printing is not returning
public static void calculateArea(double radius) {
    double area = 3.14 * radius * radius;
    System.out.println(area);  // Human sees it, program cannot use it
}

// RIGHT: Return the value
public static double calculateArea(double radius) {
    double area = 3.14 * radius * radius;
    return area;  // Program can use this value
}
```

### Struggle 3: Variable Scope Confusion

**The confusion:** "Why can my variable not be seen in this other method?"

**The solution:** Remember the hotel room analogy - each method is a private room. To share data:
1. **Pass data IN** using parameters
2. **Get data OUT** using return values

```java
// WRONG: Trying to access another method's variable
public static void calculateTotal() {
    int sum = 100;
}

public static void printTotal() {
    System.out.println(sum);  // ERROR! sum does not exist here
}

// RIGHT: Use parameters and returns to share data
public static int calculateTotal() {
    int sum = 100;
    return sum;  // Send it out
}

public static void printTotal(int total) {  // Receive it as parameter
    System.out.println(total);
}

public static void main(String[] args) {
    int result = calculateTotal();  // Get the value
    printTotal(result);             // Pass it to the other method
}
```

### Struggle 4: Understanding Pass by Value

**The confusion:** "I changed the variable inside the method, why did it not change outside?"

**The solution:** Java passes copies of values, not the actual variables. When you pass an argument, the method gets a COPY.

```java
public static void tryToChange(int number) {
    number = 999;  // Only changes the LOCAL copy
}

public static void main(String[] args) {
    int myNumber = 5;
    tryToChange(myNumber);
    System.out.println(myNumber);  // Still 5! The original was not changed
}
```

Think of it like giving someone a photocopy of a document. They can write all over their copy, but your original is unchanged.

### Struggle 5: Method Naming (Using Verbs)

**The confusion:** "What should I name this method?"

**The solution:** Follow this formula:
1. What DOES the method do? (action verb)
2. What does it do it TO? (noun)

| What it does | What it does it to | Method name |
|--------------|-------------------|-------------|
| calculate | area | `calculateArea()` |
| print | receipt | `printReceipt()` |
| find | maximum | `findMaximum()` |
| validate | email | `validateEmail()` |
| convert | temperature | `convertTemperature()` |

---

## Practice Exercises

### Exercise 1: HelloRunner (meget hjalp - Maximum Guidance)

**Goal:** Practice basic method creation with the run() pattern.

**Step-by-step instructions:**

1. Create a new Java file called `HelloRunner.java`
2. Create a class named `HelloRunner`
3. Create a `main` method that only calls `run()`
4. Create a `run()` method that:
   - Calls a method named `printWelcome()`
   - Calls a method named `printGoodbye()`
5. Create `printWelcome()` that prints "Welcome to Java methods!"
6. Create `printGoodbye()` that prints "Thanks for using this program!"

**Expected output:**
```
Welcome to Java methods!
Thanks for using this program!
```

**Starter code:**
```java
public class HelloRunner {
    public static void main(String[] args) {
        run();  // Call run() from main
    }

    public static void run() {
        // TODO: Call printWelcome() and printGoodbye()
    }

    public static void printWelcome() {
        // TODO: Print welcome message
    }

    public static void printGoodbye() {
        // TODO: Print goodbye message
    }
}
```

### Exercise 2: Print Methods (meget hjalp - Maximum Guidance)

**Goal:** Practice void methods with parameters.

**Step-by-step instructions:**

1. Create a method `printLine(char symbol, int length)` that prints a line of symbols
   - Example: `printLine('*', 5)` prints `*****`
2. Create a method `printBox(char symbol, int width, int height)` that prints a rectangle
   - It should call `printLine` for each row
3. Test by printing a box of `#` symbols, 10 wide and 4 tall

**Expected output for `printBox('#', 10, 4)`:**
```
##########
##########
##########
##########
```

**Hints:**
- Use `System.out.print(symbol)` to print without a newline
- Use `System.out.println()` after each line
- `printBox` should use a loop that calls `printLine` multiple times

### Exercise 3: TV Channels (nogen hjalp - Moderate Guidance)

**Goal:** Practice methods with return values.

**Instructions:**

Create a TV channel helper program with these methods:

1. `getChannelName(int channelNumber)` - Returns the name of a channel
   - Channel 1: "DR1"
   - Channel 2: "TV2"
   - Channel 3: "TV2 Charlie"
   - Other: "Unknown Channel"

2. `isKidsChannel(int channelNumber)` - Returns true if it is a children's channel
   - Channel 3 (TV2 Charlie) is a kids channel

3. Create a `run()` method that:
   - Asks user for a channel number
   - Prints the channel name
   - Tells if it is a kids channel

**Sample run:**
```
Enter channel number: 3
Channel: TV2 Charlie
Kids channel: Yes
```

### Exercise 4: BMI Calculator (nogen hjalp - Moderate Guidance)

**Goal:** Practice methods with multiple parameters and return values.

**Instructions:**

1. Create `calculateBMI(double weightKg, double heightM)` that returns the BMI
   - Formula: BMI = weight / (height * height)

2. Create `getBMICategory(double bmi)` that returns a String category:
   - Below 18.5: "Underweight"
   - 18.5 to 24.9: "Normal"
   - 25 to 29.9: "Overweight"
   - 30 or above: "Obese"

3. Create a `run()` method that:
   - Asks for weight in kg
   - Asks for height in meters
   - Displays the BMI (rounded to 1 decimal)
   - Displays the category

**Sample run:**
```
Enter weight (kg): 70
Enter height (m): 1.75
Your BMI: 22.9
Category: Normal
```

### Exercise 5: Fitness Subscription (ingen hjalp - Minimal Guidance)

**Goal:** Apply method design to a real-world business problem.

**Requirements:**

Create a fitness subscription calculator with these business rules:
- Base price: 199 kr/month
- Under 18 (junior): 25% discount
- Over 65 (senior): 15% discount
- Annual payment: Additional 10% off
- Student discount: 20% off (cannot combine with age discount)

Methods you might need:
- `calculateMonthlyPrice(int age, boolean isStudent)` - Base price with age/student discount
- `calculateAnnualPrice(int age, boolean isStudent)` - Full year with additional discount
- `printSubscriptionDetails(...)` - Display formatted summary

The program should:
1. Ask for age
2. Ask if student (yes/no)
3. Ask if paying annually (yes/no)
4. Display monthly equivalent price and total if annual

**Sample run:**
```
Enter your age: 20
Are you a student? (yes/no): yes
Pay annually? (yes/no): yes

Subscription Summary:
--------------------
Base price: 199.00 kr/month
Student discount: -39.80 kr (20%)
Monthly rate: 159.20 kr
Annual total: 1718.56 kr (10% annual discount)
```

---

## Looking Ahead

This week you learned how to organize code into methods - the building blocks of larger programs. This is foundational for everything that follows:

- **Week 5 (Methods Part 2):** You will learn method overloading (same name, different parameters), method composition (methods calling methods), and activity diagrams for planning. You will also explore debugging techniques for method-based code.

- **Week 6 (Arrays):** Arrays store multiple values, and methods that process arrays are extremely common. You will write methods like `findMaximum(int[] numbers)` and `calculateAverage(int[] scores)`.

- **Week 7+ (OOP):** Object-oriented programming is ALL about methods! Objects have behaviors defined by methods. Everything you learned this week - parameters, return values, scope - applies directly to object methods.

- **Week 11 (File Handling):** File operations are typically wrapped in methods: `readFile(String filename)`, `saveData(String filename, String data)`.

- **Week 13 (Unit Testing):** Testing is done METHOD BY METHOD. Each test verifies that one method works correctly. Good method design makes testing possible!

The decomposition skills you are developing now - breaking problems into smaller pieces - will serve you throughout your programming career.

---

## Key Takeaways

- A **method** is a named, reusable block of code that performs a specific task
- **Parameters** are variables declared in the method definition; **arguments** are values passed when calling
- **Return values** send results back to the caller; **void** methods perform actions without returning
- **Local variables** only exist within their method - use parameters and returns to share data
- The **call stack** tracks which method is running and where to return
- Use `public static` for all methods until you learn about objects
- **Naming conventions**: Use verbs, be descriptive, use camelCase
- **Print vs Return**: Printing is for humans to see; returning is for code to use
- Methods can contain loops, conditionals, and calls to other methods
- Create methods when you see repetition, complexity, or a clear single purpose
- **Pass by value**: Methods receive copies of primitive values, not the originals

---

## For the Next Topic Agent

### Terminology Established This Week

- **method**: A named block of code that performs a specific task
- **method declaration/definition**: Where you write the code that defines a method
- **method call/invocation**: Using the method by name to execute its code
- **parameter**: A variable declared in the method header (placeholder)
- **argument**: The actual value provided when calling a method
- **return value**: The result sent back from a method to its caller
- **return type**: The data type of the value a method returns (or void)
- **void**: A return type indicating the method returns nothing
- **local variable**: A variable that exists only within its method or block
- **scope**: The region of code where a variable can be accessed
- **call stack**: The mechanism tracking which methods are executing
- **static**: A modifier meaning the method belongs to the class (required for now)
- **pass by value**: Java passes copies of primitive values to methods
- **method signature**: The combination of method name and parameter types
- **method body**: The code inside the method that executes
- **return statement**: The statement that sends a value back and exits the method

### Example Classes/Concepts Created

- HelloRunner with run() pattern
- Print methods (printLine, printBox)
- TV channel lookup with getChannelName and isKidsChannel
- BMI calculator with calculateBMI and getBMICategory
- Fitness subscription calculator with discount logic
- Trace tables for method calls

### Student Capabilities After This Week

Students can now:
- Decompose problems into smaller, reusable methods
- Write methods with proper syntax (return type, name, parameters, body)
- Call methods with appropriate arguments
- Distinguish between parameters (placeholders) and arguments (actual values)
- Create methods that return values and void methods
- Understand and work within variable scope rules
- Trace method calls and returns through the call stack
- Follow naming conventions (verb-based, camelCase)
- Recognize when to use return vs print
- Apply the run() method pattern for program organization

### Pedagogical Patterns Continued

- **Recipe analogy**: Methods as recipes with ingredients (parameters) and results (return)
- **Hotel room analogy**: Variable scope as private spaces
- **Vending machine analogy**: Methods that return values
- **Printer vs calculator analogy**: Void vs returning methods
- **Trace tables**: Step-by-step execution for method calls
- **Common mistakes sections**: Missing returns, wrong types, scope errors
- **Progressive exercise difficulty**: meget hjalp -> nogen hjalp -> ingen hjalp
- **Why before how**: Each concept motivated before syntax
- **Connecting to prior weeks**: Methods contain loops and conditionals

### Critical Connections for Week 5 (Methods Part 2)

- Method overloading builds on understanding method signatures
- Method composition extends the concept of methods calling methods
- Activity diagrams help plan complex method interactions
- Debugging techniques build on understanding the call stack
- Variable scope becomes more complex with instance variables (preview for OOP)
