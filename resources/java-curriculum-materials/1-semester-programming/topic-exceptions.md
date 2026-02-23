# Exception Handling - Week 12

*Prerequisites: Week 11 (File Handling), Weeks 7-10 (Complete OOP Foundation including Inheritance)*
*Phase: Phase 4: Practical Software Development (Second Week)*

---

## What You'll Learn

By the end of this week, you will be able to:

- **Understand what exceptions really are** and why they exist
- **Distinguish errors from exceptions** - not all problems are the same!
- **Differentiate checked vs. unchecked exceptions** - the key distinction in Java
- **Use try-catch blocks** to handle exceptions gracefully
- **Work with multiple catch blocks** for different exception types
- **Understand the finally block** for guaranteed cleanup
- **Master try-with-resources** at a deeper level than Week 11
- **Use throw to create exceptions** in your own code
- **Declare exceptions with throws** in method signatures
- **Create custom exception classes** - combining OOP with error handling!
- **Read and understand stack traces** for debugging
- **Apply exception handling best practices** in real applications

**CONNECTION TO WEEK 11**: Last week you saw `FileNotFoundException` and used `try-catch`. This week we go DEEP. You will understand WHY those constructs exist, HOW exceptions work internally, and when to create your OWN exception types!

---

## Why This Matters

### The Problem: Things Go Wrong

Programs fail. It is not a matter of IF, but WHEN. Consider these scenarios:

```
User enters "abc" when asked for a number      --> NumberFormatException
Program tries to read a missing file           --> FileNotFoundException
Array index goes beyond the array size         --> ArrayIndexOutOfBoundsException
Network connection drops mid-request           --> IOException
User provides null where object expected       --> NullPointerException
```

Without exception handling, your program crashes. With exception handling, your program can:
- Recover gracefully
- Inform the user what went wrong
- Log the error for debugging
- Try an alternative approach
- Save important data before exiting

### Real-World Everywhere

Think about apps you use daily:

| Situation | Without Exception Handling | With Exception Handling |
|-----------|---------------------------|------------------------|
| No internet | App crashes | "Please check your connection" |
| File corrupted | Data lost | "File damaged, using backup" |
| Invalid input | Program freezes | "Please enter a valid number" |
| Server down | Mysterious error | "Service temporarily unavailable" |

**Professional software NEVER crashes silently.** It handles problems gracefully.

### This Builds on Week 11

Remember this pattern from last week?

```java
try {
    Scanner scanner = new Scanner(new File("data.txt"));
    // ... work with file
} catch (FileNotFoundException e) {
    System.out.println("File not found!");
}
```

Week 11 taught you the WHAT. Week 12 teaches you the WHY and MUCH MORE:
- What IS `FileNotFoundException`? (It is an object - a class instance!)
- Why does `FileNotFoundException` require try-catch but `ArrayIndexOutOfBoundsException` does not?
- How do exceptions propagate through your program?
- When should YOU throw exceptions vs. handle them?

### This Is Exam-Critical (20-25%)

Exception handling accounts for 20-25% of your exam. You WILL be asked to:
- Handle specific exception types appropriately
- Create custom exception classes
- Choose between catching and throwing
- Demonstrate proper resource management

---

## Building Your Intuition

### Analogy 1: Exceptions as Emergency Alerts

Imagine you are a pilot flying an airplane. The cockpit has warning systems:

**Normal operation:** Everything runs smoothly. No alerts.

**Warning (Exception):** "Low fuel" alert appears. You can HANDLE this - divert to a closer airport, adjust speed, or radio for priority landing. The flight continues.

**Critical failure (Error):** Engine on fire, structural damage. No recovery possible. Emergency procedures only.

In Java:
- **Normal code execution** = smooth flight
- **Exceptions** = warnings you can handle and recover from
- **Errors** = critical failures (out of memory, stack overflow) that you typically cannot recover from

**The key insight:** Exceptions are not failures - they are SIGNALS that something unexpected happened, giving you a chance to respond appropriately.

### Analogy 2: The Safety Net

Think of a trapeze artist in a circus:

```
HIGH WIRE (risky operation)
    |
    v
+-------------------+
|   TRY BLOCK       |  "I'll attempt this risky move..."
|  (the performance)|
+-------------------+
    |
    | if fall
    v
+-------------------+
|   CATCH BLOCK     |  "...but if I fall, the net catches me"
|  (the safety net) |
+-------------------+
    |
    v
+-------------------+
|   FINALLY BLOCK   |  "Either way, I'll take a bow at the end"
| (always happens)  |
+-------------------+
```

**The performer (try)** attempts the risky move.
**The safety net (catch)** catches them if they fall.
**The bow (finally)** happens whether they succeeded or fell!

### Analogy 3: Exception Propagation as Passing the Buck

Imagine a company with multiple levels:

```
CEO              (main method)
  |
VP               (method A)
  |
Manager          (method B)
  |
Employee         (method C - where problem occurs)
```

An employee encounters a problem they cannot solve. What happens?

1. **Handle it locally**: Employee fixes it themselves (catch the exception)
2. **Escalate to manager**: Employee reports it, manager decides (throw to caller)
3. **Escalate to VP**: Manager cannot solve it, passes it up
4. **Escalate to CEO**: If CEO cannot handle it, the company (program) fails

In Java, exceptions "propagate up the call stack" - passing from method to method until someone handles them or the program crashes.

### Analogy 4: Checked vs. Unchecked - Required vs. Optional Insurance

**Checked exceptions** are like mandatory car insurance:
- The law (Java compiler) REQUIRES you to have it
- You cannot drive (compile) without proving you have coverage
- Examples: FileNotFoundException, IOException
- These represent situations you should EXPECT and PLAN for

**Unchecked exceptions** are like accidental damage:
- No insurance required by law
- But accidents can still happen at runtime
- Examples: NullPointerException, ArrayIndexOutOfBoundsException
- These usually represent BUGS in your code

**Why the difference?**
- Checked: "This operation commonly fails. You MUST have a plan."
- Unchecked: "This probably means your code has a bug. Fix the code!"

### Analogy 5: Custom Exceptions as Specialized Alarm Systems

A hospital has different alarms:
- Fire alarm: everyone evacuates
- Code blue: cardiac emergency, specific team responds
- Code orange: hazardous material, different response

Generic alarms are not enough. Specific alarms enable specific responses.

In Java:
- Generic `Exception` = "Something went wrong"
- Custom `InvalidUserException` = "User data is invalid, show registration form again"
- Custom `InsufficientFundsException` = "Not enough money, offer payment options"

Custom exceptions let your code respond SPECIFICALLY to SPECIFIC problems.

---

## Understanding Exceptions: The Foundation

### What Is an Exception?

An **exception** is an object that represents something abnormal that happened during program execution.

Yes, an OBJECT! Exceptions are instances of classes, just like your Student or Car objects. This connects directly to your OOP knowledge from Weeks 7-10!

```java
// When you write:
throw new FileNotFoundException("data.txt not found");

// You are CREATING an object:
// - Class: FileNotFoundException
// - Constructor called: FileNotFoundException(String message)
// - Object created on heap, just like any other object!
```

### Why Exceptions Are Objects

Because exceptions are objects:
- They have **state** (error message, cause, stack trace)
- They have **behavior** (getMessage(), printStackTrace())
- They participate in **inheritance** (FileNotFoundException IS-A IOException IS-A Exception)
- You can **create your own types** (custom exception classes)

### How It Works

When something goes wrong:

1. Java creates an exception object
2. Java "throws" this object - stops normal execution
3. Java looks for a "catch" block that can handle this exception type
4. If found, execution continues in the catch block
5. If not found, the exception propagates to the calling method
6. If no method handles it, the program crashes with a stack trace

```java
public class ExceptionDemo {
    public static void main(String[] args) {
        try {
            int result = divide(10, 0);  // This will cause an exception!
            System.out.println("Result: " + result);  // Never reached
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero!");
        }
        System.out.println("Program continues...");  // This DOES run!
    }

    public static int divide(int a, int b) {
        return a / b;  // ArithmeticException thrown here if b is 0
    }
}
```

---

## Understanding: Errors vs. Exceptions

### What Is the Difference?

Both `Error` and `Exception` extend `Throwable`, but they represent very different situations:

**Exceptions**: Problems your code CAN and SHOULD handle
- File not found
- Invalid user input
- Network timeout
- Database connection failed

**Errors**: Catastrophic problems your code usually CANNOT handle
- Out of memory (OutOfMemoryError)
- Stack overflow (StackOverflowError)
- JVM internal error
- Hardware failure

### Why This Distinction Matters

```java
// This makes sense - handle recoverable situation
try {
    readFile("data.txt");
} catch (FileNotFoundException e) {
    createDefaultFile();  // Recover by creating the file
}

// This is usually pointless - cannot recover from this
try {
    infiniteRecursion();  // Will overflow the stack
} catch (StackOverflowError e) {
    // What can you even do here? The stack is gone!
}
```

### Visual Hierarchy

```
        java.lang.Throwable
              /    \
             /      \
    java.lang.Error  java.lang.Exception
         |                    |
    (Don't catch)      (DO catch when appropriate)
         |                    |
  StackOverflowError    IOException
  OutOfMemoryError      SQLException
                        RuntimeException
                              |
                        NullPointerException
                        ArrayIndexOutOfBoundsException
```

### The Rule of Thumb

- **Catch exceptions** - they are meant to be handled
- **Don't catch errors** - they indicate serious problems that usually cannot be fixed at runtime
- **Fix the cause** of errors (memory leaks, infinite recursion) rather than trying to catch them

---

## Understanding: The Exception Hierarchy

### Why Hierarchy Matters

Exception classes form an inheritance tree. This is OOP in action!

```
Throwable
    |
    +-- Error (don't catch these)
    |      |
    |      +-- OutOfMemoryError
    |      +-- StackOverflowError
    |
    +-- Exception (catch these!)
           |
           +-- IOException (checked)
           |      |
           |      +-- FileNotFoundException
           |
           +-- SQLException (checked)
           |
           +-- RuntimeException (unchecked)
                  |
                  +-- NullPointerException
                  +-- ArrayIndexOutOfBoundsException
                  +-- NumberFormatException
                  +-- IllegalArgumentException
```

### Inheritance Applies!

Because of inheritance, catching a parent class catches ALL its children:

```java
try {
    // Some risky code
} catch (Exception e) {
    // This catches FileNotFoundException, IOException,
    // NullPointerException, AND ANY other exception!
}
```

This is powerful but dangerous. Usually you want to catch SPECIFIC exceptions:

```java
try {
    // Some risky code
} catch (FileNotFoundException e) {
    System.out.println("File missing: " + e.getMessage());
} catch (IOException e) {
    System.out.println("I/O error: " + e.getMessage());
}
```

### Polymorphism in Exceptions

Remember polymorphism from Week 9? It applies here too!

```java
// FileNotFoundException IS-A IOException
// So this works:
IOException ex = new FileNotFoundException("data.txt");

// And in catch blocks, order matters!
try {
    // code
} catch (FileNotFoundException e) {  // More specific FIRST
    // Handle specifically
} catch (IOException e) {  // More general SECOND
    // Handle generally
}
// If you reversed the order, FileNotFoundException would never be caught
// by its own block - IOException would catch it first!
```

---

## Understanding: Checked vs. Unchecked Exceptions

### The Most Important Distinction

This is where many beginners struggle. Let us make it crystal clear.

**Checked exceptions:**
- MUST be handled (try-catch) OR declared (throws)
- Compiler enforces this - code will not compile otherwise!
- Extend Exception but NOT RuntimeException
- Represent expected, recoverable conditions
- Examples: IOException, FileNotFoundException, SQLException

**Unchecked exceptions (Runtime exceptions):**
- Do NOT require handling or declaration
- Compiler does not enforce anything
- Extend RuntimeException
- Usually represent programming bugs
- Examples: NullPointerException, ArrayIndexOutOfBoundsException

### Why This Design?

Java designers reasoned:

**Checked exceptions** = "External problems you should expect"
- Files might not exist
- Network might be down
- Database might be unavailable
- **You SHOULD have a plan for these!**

**Unchecked exceptions** = "Bugs in your code"
- Null pointer = you forgot to check for null
- Array out of bounds = your loop logic is wrong
- Number format = you did not validate input
- **Fix your code instead of catching these!**

### How to Tell the Difference

```java
// If your code doesn't compile with this message:
// "Unhandled exception type FileNotFoundException"
// --> It's a CHECKED exception. You MUST handle it.

// If your code compiles but crashes at runtime with:
// "Exception in thread "main" java.lang.NullPointerException"
// --> It's an UNCHECKED exception. You SHOULD fix the code.
```

### Code Examples

**Checked exception - compiler forces handling:**

```java
// This does NOT compile!
public void readFile() {
    Scanner s = new Scanner(new File("data.txt"));  // Compiler error!
}

// This DOES compile - we handle the exception
public void readFile() {
    try {
        Scanner s = new Scanner(new File("data.txt"));
    } catch (FileNotFoundException e) {
        System.out.println("File not found!");
    }
}

// This ALSO compiles - we declare we might throw it
public void readFile() throws FileNotFoundException {
    Scanner s = new Scanner(new File("data.txt"));
}
```

**Unchecked exception - compiles fine, fails at runtime:**

```java
// This compiles perfectly!
public void accessArray() {
    int[] arr = new int[5];
    System.out.println(arr[10]);  // ArrayIndexOutOfBoundsException at RUNTIME
}

// Better: prevent the error through good code
public void accessArray() {
    int[] arr = new int[5];
    int index = 10;
    if (index >= 0 && index < arr.length) {
        System.out.println(arr[index]);
    } else {
        System.out.println("Index out of range!");
    }
}
```

---

## Understanding: try-catch Blocks

### What Is a try-catch Block?

A try-catch block lets you attempt risky code and handle any exceptions that occur.

### Why It Exists

Without try-catch, exceptions crash your program. With try-catch, you maintain control.

### How It Works

```java
try {
    // Code that MIGHT throw an exception
    // If an exception occurs, remaining try-block code is SKIPPED
} catch (ExceptionType e) {
    // Code that runs IF the exception occurs
    // 'e' is the exception object - use it to get details
}
// Code here runs AFTER try-catch, regardless of whether exception occurred
// (as long as the catch block didn't throw or return)
```

### Basic Example

```java
import java.util.Scanner;

public class TryCatchDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        String input = scanner.nextLine();

        try {
            int number = Integer.parseInt(input);  // Might throw!
            System.out.println("You entered: " + number);
            System.out.println("Doubled: " + (number * 2));
        } catch (NumberFormatException e) {
            System.out.println("That's not a valid number!");
            System.out.println("You entered: " + input);
        }

        System.out.println("Program continues normally...");
    }
}
```

### The Exception Object

The `e` in `catch (Exception e)` is a variable holding the exception object. It has useful methods:

```java
try {
    // risky code
} catch (FileNotFoundException e) {
    // Get the error message
    String message = e.getMessage();  // "data.txt (No such file or directory)"

    // Print the full stack trace (very useful for debugging!)
    e.printStackTrace();

    // Get the exception's class name
    String type = e.getClass().getName();  // "java.io.FileNotFoundException"
}
```

### Common Mistake: Empty Catch Block

**NEVER do this:**

```java
try {
    // risky code
} catch (Exception e) {
    // Empty! Silent failure!
}
```

This "swallows" the exception. Your program continues but something is wrong, and you have no idea what! At minimum, log or print the error:

```java
try {
    // risky code
} catch (Exception e) {
    System.err.println("Error occurred: " + e.getMessage());
    // Or: e.printStackTrace();
}
```

---

## Understanding: Multiple Catch Blocks

### What Are Multiple Catch Blocks?

Different exceptions may need different handling. Multiple catch blocks let you respond specifically to each type.

### Why Use Them

```java
// One response for all errors - not ideal
try {
    readFile();
    parseData();
    saveResults();
} catch (Exception e) {
    System.out.println("Something went wrong");  // Not helpful!
}

// Specific responses - much better!
try {
    readFile();
    parseData();
    saveResults();
} catch (FileNotFoundException e) {
    System.out.println("File not found. Check the filename.");
} catch (NumberFormatException e) {
    System.out.println("Invalid number in data. Check file format.");
} catch (IOException e) {
    System.out.println("Error saving results. Check disk space.");
}
```

### How It Works

Java checks catch blocks IN ORDER. The first matching block handles the exception.

```java
try {
    Scanner s = new Scanner(new File("data.txt"));
    String line = s.nextLine();
    int value = Integer.parseInt(line);
} catch (FileNotFoundException e) {
    System.out.println("File not found!");
} catch (NumberFormatException e) {
    System.out.println("First line is not a number!");
} catch (Exception e) {
    System.out.println("Some other error: " + e.getMessage());
}
```

### Order Matters!

More specific exceptions must come BEFORE more general ones:

```java
// WRONG - won't compile!
try {
    // code
} catch (Exception e) {        // Catches EVERYTHING
    // handle
} catch (IOException e) {      // Never reached - already caught above!
    // handle
}

// CORRECT - specific before general
try {
    // code
} catch (IOException e) {      // Specific first
    // handle
} catch (Exception e) {        // General last (catches anything else)
    // handle
}
```

### Multi-Catch Syntax (Java 7+)

Handle multiple exception types the same way:

```java
// Old way - repetitive
try {
    // code
} catch (FileNotFoundException e) {
    System.out.println("Error: " + e.getMessage());
} catch (NumberFormatException e) {
    System.out.println("Error: " + e.getMessage());
}

// New way - combine with |
try {
    // code
} catch (FileNotFoundException | NumberFormatException e) {
    System.out.println("Error: " + e.getMessage());
}
```

---

## Understanding: The finally Block

### What Is finally?

A `finally` block contains code that ALWAYS runs, whether an exception occurred or not.

### Why It Exists

Some cleanup MUST happen regardless of success or failure:
- Close files
- Release connections
- Free resources
- Log completion

### How It Works

```java
try {
    // Risky code
} catch (Exception e) {
    // Handle exception
} finally {
    // This ALWAYS runs
    // Even if try succeeds
    // Even if catch runs
    // Even if there's a return statement!
}
```

### Example: Resource Cleanup (Before try-with-resources)

```java
Scanner scanner = null;
try {
    scanner = new Scanner(new File("data.txt"));
    // Process file...
    String data = scanner.nextLine();
    System.out.println(data);
} catch (FileNotFoundException e) {
    System.out.println("File not found!");
} finally {
    // Close scanner no matter what happened
    if (scanner != null) {
        scanner.close();
        System.out.println("Scanner closed.");
    }
}
```

### finally Runs Even with return!

```java
public static String test() {
    try {
        return "from try";
    } finally {
        System.out.println("finally runs!");  // This STILL executes!
    }
}

// Output:
// finally runs!
// (returns "from try")
```

### When finally Does NOT Run

Only in extreme cases:
- System.exit() is called
- JVM crashes
- Infinite loop in try or catch
- Thread is killed

For normal operation, finally ALWAYS runs.

---

## Understanding: try-with-resources (Deeper)

### Week 11 Refresher

You learned this pattern for safe file handling:

```java
try (Scanner scanner = new Scanner(new File("data.txt"))) {
    // Use scanner
}  // Automatically closed!
```

### Why It Is Better Than finally

```java
// OLD WAY with finally - verbose and error-prone
Scanner scanner = null;
try {
    scanner = new Scanner(new File("data.txt"));
    // use scanner
} catch (FileNotFoundException e) {
    // handle
} finally {
    if (scanner != null) {
        scanner.close();
    }
}

// NEW WAY with try-with-resources - clean and safe
try (Scanner scanner = new Scanner(new File("data.txt"))) {
    // use scanner
} catch (FileNotFoundException e) {
    // handle
}
// Automatically closed, even if exception occurs!
```

### The AutoCloseable Interface

Try-with-resources works with any class implementing `AutoCloseable`:

```java
public interface AutoCloseable {
    void close() throws Exception;
}
```

Classes that implement this:
- Scanner
- PrintWriter
- BufferedReader
- BufferedWriter
- Connection (database)
- Many more!

### Multiple Resources

You can declare multiple resources:

```java
try (Scanner input = new Scanner(new File("input.txt"));
     PrintWriter output = new PrintWriter("output.txt")) {

    while (input.hasNextLine()) {
        String line = input.nextLine();
        output.println(line.toUpperCase());
    }
}
// BOTH input AND output are automatically closed!
```

### Order of Closing

Resources close in REVERSE order of declaration:

```java
try (Resource1 r1 = new Resource1();
     Resource2 r2 = new Resource2();
     Resource3 r3 = new Resource3()) {
    // use resources
}
// Closed in order: r3, r2, r1 (reverse!)
```

---

## Understanding: throw Keyword

### What Is throw?

The `throw` keyword creates and throws an exception. YOU decide when something is an error condition.

### Why Use throw

Sometimes YOUR code detects an error condition:
- Invalid parameter passed to your method
- Business rule violated
- State inconsistency detected

Instead of returning a magic value or printing an error, you THROW an exception.

### How It Works

```java
// Syntax:
throw new ExceptionType("Error message");
```

### Example: Validating Parameters

```java
public class BankAccount {
    private double balance;

    public void withdraw(double amount) {
        // Check for invalid input
        if (amount < 0) {
            throw new IllegalArgumentException("Amount cannot be negative!");
        }

        // Check for business rule violation
        if (amount > balance) {
            throw new IllegalArgumentException("Insufficient funds!");
        }

        balance -= amount;
    }
}
```

### Example: Age Validation

```java
public class Student {
    private String name;
    private int age;

    public void setAge(int age) {
        if (age < 0 || age > 150) {
            throw new IllegalArgumentException("Age must be between 0 and 150");
        }
        this.age = age;
    }
}

// Usage:
Student s = new Student();
s.setAge(-5);  // Throws IllegalArgumentException!
```

### throw vs. throws

These are DIFFERENT things!

- `throw` = actively throw an exception (creates and sends)
- `throws` = declare that a method MIGHT throw an exception (documentation)

```java
// throw - the action of throwing
throw new IOException("Cannot read file");

// throws - declaring what exceptions a method might throw
public void readFile() throws IOException {
    // ...
}
```

---

## Understanding: throws Declaration

### What Is throws?

The `throws` keyword in a method signature declares that this method might throw certain exceptions.

### Why Use throws

For CHECKED exceptions, you have two choices:
1. Handle it with try-catch (handle locally)
2. Declare it with throws (pass responsibility to caller)

### How It Works

```java
// This method declares it might throw FileNotFoundException
public void readFile(String filename) throws FileNotFoundException {
    Scanner scanner = new Scanner(new File(filename));
    // ... use scanner
}
```

### When to throws vs. try-catch

**Use try-catch when:**
- You CAN handle the problem here
- You have a recovery strategy
- The caller should not worry about this error

**Use throws when:**
- You CANNOT handle the problem here
- The caller should decide how to handle it
- Multiple callers might want different handling

### Example: Letting the Caller Decide

```java
public class FileProcessor {

    // This method DECLARES it might throw, but doesn't handle it
    public String readFirstLine(String filename) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(filename));
        return scanner.nextLine();
    }
}

// Caller 1: Handle by showing error
public class Application1 {
    public void process() {
        FileProcessor fp = new FileProcessor();
        try {
            String line = fp.readFirstLine("data.txt");
            System.out.println(line);
        } catch (FileNotFoundException e) {
            System.out.println("Error: File not found!");
        }
    }
}

// Caller 2: Handle by using default
public class Application2 {
    public void process() {
        FileProcessor fp = new FileProcessor();
        try {
            String line = fp.readFirstLine("data.txt");
            System.out.println(line);
        } catch (FileNotFoundException e) {
            System.out.println("Using default data...");
            processDefault();
        }
    }
}
```

### Multiple throws

A method can declare multiple exception types:

```java
public void processFile(String filename)
        throws FileNotFoundException, IOException, NumberFormatException {
    // Method implementation
}
```

### Propagation Through Call Stack

```java
public class PropagationDemo {

    // Level 3: Throws, doesn't handle
    public void level3() throws IOException {
        throw new IOException("Problem at level 3!");
    }

    // Level 2: Also throws, doesn't handle
    public void level2() throws IOException {
        level3();  // Exception propagates up
    }

    // Level 1: Also throws, doesn't handle
    public void level1() throws IOException {
        level2();  // Exception propagates up
    }

    // main: Finally handles it!
    public static void main(String[] args) {
        PropagationDemo demo = new PropagationDemo();
        try {
            demo.level1();
        } catch (IOException e) {
            System.out.println("Caught: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```

---

## Understanding: Creating Custom Exception Classes

### What Is a Custom Exception?

A custom exception is YOUR OWN exception class that extends Exception or RuntimeException.

### Why Create Custom Exceptions

Generic exceptions like `Exception` or `IllegalArgumentException` do not tell you WHAT went wrong in YOUR domain:

```java
// Generic - what does this mean?
throw new Exception("Error");

// Custom - specific and meaningful!
throw new InvalidUserException("Username already exists");
throw new InsufficientFundsException("Balance: $50, Requested: $100");
throw new InvalidAgeException("Age 250 is not valid for a human");
```

### How to Create: Checked Exception

Extend `Exception` for a checked exception:

```java
// Custom CHECKED exception
public class InvalidUserException extends Exception {

    // Constructor with message
    public InvalidUserException(String message) {
        super(message);  // Pass message to parent Exception
    }

    // Optional: constructor with message and cause
    public InvalidUserException(String message, Throwable cause) {
        super(message, cause);
    }
}
```

### How to Create: Unchecked Exception

Extend `RuntimeException` for an unchecked exception:

```java
// Custom UNCHECKED exception
public class InvalidAgeException extends RuntimeException {

    private int invalidAge;  // Extra data about the error!

    public InvalidAgeException(String message, int invalidAge) {
        super(message);
        this.invalidAge = invalidAge;
    }

    public int getInvalidAge() {
        return invalidAge;
    }
}
```

### Using Custom Exceptions

```java
public class UserManager {
    private ArrayList<String> usernames = new ArrayList<>();

    // Throws checked exception - callers MUST handle
    public void registerUser(String username) throws InvalidUserException {
        if (username == null || username.isEmpty()) {
            throw new InvalidUserException("Username cannot be empty");
        }
        if (usernames.contains(username)) {
            throw new InvalidUserException("Username '" + username + "' already exists");
        }
        usernames.add(username);
    }
}

// Usage:
UserManager manager = new UserManager();
try {
    manager.registerUser("alice");
    manager.registerUser("alice");  // Throws!
} catch (InvalidUserException e) {
    System.out.println("Registration failed: " + e.getMessage());
}
```

### This Is OOP!

Notice how creating custom exceptions uses OOP concepts from Weeks 7-10:

- **Classes**: Exceptions are classes
- **Inheritance**: Custom exceptions extend Exception or RuntimeException
- **Constructors**: Custom constructors with parameters
- **Instance variables**: Store additional error information
- **Encapsulation**: Getters for error details

---

## Understanding: Stack Traces

### What Is a Stack Trace?

A stack trace shows the sequence of method calls that led to an exception. It is your debugging roadmap!

### Reading a Stack Trace

```
Exception in thread "main" java.lang.NullPointerException: Cannot invoke method on null
    at com.example.DataProcessor.processLine(DataProcessor.java:25)
    at com.example.DataProcessor.processFile(DataProcessor.java:18)
    at com.example.Application.main(Application.java:10)
```

Read from TOP to BOTTOM:
1. **Exception type**: `NullPointerException`
2. **Message**: "Cannot invoke method on null"
3. **Where it happened**: `DataProcessor.java`, line 25, in method `processLine`
4. **Called from**: `DataProcessor.java`, line 18, in method `processFile`
5. **Called from**: `Application.java`, line 10, in method `main`

### The Pattern

```
Exception type: error description
    at ClassName.methodName(FileName.java:lineNumber)  <-- Error occurred HERE
    at ClassName.methodName(FileName.java:lineNumber)  <-- Called from here
    at ClassName.methodName(FileName.java:lineNumber)  <-- Called from here
    ...
```

### Printing Stack Traces

```java
try {
    // risky code
} catch (Exception e) {
    // Print stack trace to System.err (standard error)
    e.printStackTrace();

    // Or get it as a string
    StringWriter sw = new StringWriter();
    e.printStackTrace(new PrintWriter(sw));
    String stackTrace = sw.toString();
}
```

### Using Stack Traces for Debugging

When you see a stack trace:
1. Find the FIRST line with YOUR code (not library code)
2. Go to that file and line number
3. Understand what that line is doing
4. Figure out why it failed

---

## Understanding: Best Practices

### 1. Be Specific in What You Catch

```java
// BAD - catches everything, including bugs
try {
    processData();
} catch (Exception e) {
    // handle
}

// GOOD - catches only expected exceptions
try {
    processData();
} catch (FileNotFoundException e) {
    // handle missing file specifically
} catch (NumberFormatException e) {
    // handle bad number format specifically
}
```

### 2. Never Swallow Exceptions

```java
// TERRIBLE - exception disappears silently
try {
    riskyOperation();
} catch (Exception e) {
    // Empty! Bugs will be invisible!
}

// MINIMUM - at least log it
try {
    riskyOperation();
} catch (Exception e) {
    System.err.println("Error: " + e.getMessage());
    e.printStackTrace();
}
```

### 3. Throw Early, Catch Late

```java
// THROW EARLY - validate inputs immediately
public void processFile(String filename) {
    if (filename == null) {
        throw new IllegalArgumentException("Filename cannot be null");
    }
    // ... process file
}

// CATCH LATE - handle at the appropriate level
public static void main(String[] args) {
    try {
        processFile(null);
    } catch (IllegalArgumentException e) {
        System.out.println("Invalid input: " + e.getMessage());
    }
}
```

### 4. Provide Meaningful Messages

```java
// BAD - useless message
throw new InvalidUserException("Error");

// GOOD - helpful message
throw new InvalidUserException(
    "Cannot register user 'alice': username already exists in system"
);
```

### 5. Clean Up Resources

```java
// BEST - try-with-resources
try (Scanner s = new Scanner(new File("data.txt"))) {
    // use scanner
}

// If you can't use try-with-resources, use finally
Scanner s = null;
try {
    s = new Scanner(new File("data.txt"));
    // use scanner
} finally {
    if (s != null) s.close();
}
```

### 6. Do Not Use Exceptions for Flow Control

```java
// BAD - using exceptions as if/else
try {
    int value = array[index];
} catch (ArrayIndexOutOfBoundsException e) {
    // handle missing element
}

// GOOD - check first
if (index >= 0 && index < array.length) {
    int value = array[index];
} else {
    // handle missing element
}
```

### 7. Document Exceptions

```java
/**
 * Withdraws money from the account.
 *
 * @param amount the amount to withdraw
 * @throws IllegalArgumentException if amount is negative
 * @throws InsufficientFundsException if balance is too low
 */
public void withdraw(double amount)
        throws IllegalArgumentException, InsufficientFundsException {
    // implementation
}
```

---

## Connecting to What You Already Know

### Week 11: File Handling

You have been using exception handling already!

```java
// Week 11 pattern - now you understand WHY!
try (Scanner scanner = new Scanner(new File("data.txt"))) {
    while (scanner.hasNextLine()) {
        String line = scanner.nextLine();
        // process line
    }
} catch (FileNotFoundException e) {
    // FileNotFoundException is a CHECKED exception
    // That's why you HAD to use try-catch!
    System.out.println("File not found: " + e.getMessage());
}
```

### Weeks 7-10: OOP Connection

Custom exceptions USE everything from OOP:

| OOP Concept | Exception Application |
|-------------|----------------------|
| Classes | Exception is a class |
| Objects | throw new Exception() creates an object |
| Inheritance | YourException extends Exception |
| Constructors | Custom constructors with messages |
| Instance variables | Store error details (invalid value, etc.) |
| Polymorphism | Catching parent catches children |

### Week 6: Arrays

ArrayIndexOutOfBoundsException is an UNCHECKED exception:

```java
int[] arr = new int[5];
// Week 6 arrays + Week 12 exceptions
try {
    int value = arr[10];  // ArrayIndexOutOfBoundsException!
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("Index out of bounds: " + e.getMessage());
}

// Better: prevent it with validation (Week 2 conditionals!)
int index = 10;
if (index >= 0 && index < arr.length) {
    int value = arr[index];
}
```

### Week 2: Conditions

Exception handling works WITH conditionals, not instead of them:

```java
// Prevent exceptions when possible
if (divisor != 0) {
    result = dividend / divisor;
} else {
    System.out.println("Cannot divide by zero");
}

// Handle exceptions when you cannot prevent them
try {
    int value = Integer.parseInt(userInput);
} catch (NumberFormatException e) {
    System.out.println("Invalid number");
}
```

---

## Common Struggles and How to Overcome Them

### Struggle 1: Checked vs. Unchecked Confusion

**The problem:** "Why does FileNotFoundException require try-catch but NullPointerException doesn't?"

**Why it happens:** The distinction feels arbitrary at first.

**Remember:**
- **Checked** = external problems you should EXPECT (files, network, database)
- **Unchecked** = bugs in YOUR code (null pointers, bad indexes, type errors)

**Visual memory aid:**
```
CHECKED (requires handling):       UNCHECKED (fix your code):
- FileNotFoundException            - NullPointerException
- IOException                      - ArrayIndexOutOfBoundsException
- SQLException                     - NumberFormatException

Checked = "check your plan"        Unchecked = "check your code"
```

### Struggle 2: When to Catch vs. When to Throw

**The problem:** "Should I handle this exception here or let it propagate?"

**Guidelines:**

**Catch when:**
- You CAN recover from the error
- You have a sensible default or alternative
- The caller should not need to know about this error
- This is the right place to log or display the error

**Throw when:**
- You CANNOT meaningfully handle the error here
- Different callers might want different handling
- The error needs to propagate to a higher-level handler
- You are writing a library/utility method

### Struggle 3: Creating Meaningful Custom Exceptions

**The problem:** "My custom exceptions are too generic."

**Solution:** Include specific, actionable information:

```java
// TOO GENERIC
throw new ValidationException("Invalid data");

// BETTER - specific and actionable
throw new InvalidEmailException(
    "Invalid email format: '" + email + "'. Expected format: user@domain.com"
);
```

### Struggle 4: Understanding Exception Propagation

**The problem:** "I don't understand how exceptions 'bubble up'."

**Visualization:**

```
main() calls processOrder()
    processOrder() calls validatePayment()
        validatePayment() calls checkBalance()
            checkBalance() throws InsufficientFundsException

If checkBalance() doesn't catch it:
    --> Goes to validatePayment()
If validatePayment() doesn't catch it:
    --> Goes to processOrder()
If processOrder() doesn't catch it:
    --> Goes to main()
If main() doesn't catch it:
    --> Program crashes with stack trace
```

**The exception "bubbles up" until someone catches it!**

### Struggle 5: Resource Management in finally

**The problem:** Forgetting to close resources, or closing incorrectly.

**Solution:** Always use try-with-resources when possible!

```java
// OLD WAY - error-prone
Scanner s = null;
try {
    s = new Scanner(new File("data.txt"));
    // use s
} catch (FileNotFoundException e) {
    // handle
} finally {
    if (s != null) {
        s.close();  // What if close() throws?
    }
}

// MODERN WAY - safe and clean
try (Scanner s = new Scanner(new File("data.txt"))) {
    // use s
} catch (FileNotFoundException e) {
    // handle
}
// s is guaranteed closed, even if exception occurs
```

---

## Practice Exercises

### Exercise 1: Fun with Exceptions (meget hjaelp - Maximum Guidance)

**Goal:** Practice basic exception handling with ArrayIndexOutOfBoundsException.

**Part A: Catch the exception**

```java
public class FunWithExceptions {
    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40, 50};

        // TODO: Try to access index 10
        // This will throw ArrayIndexOutOfBoundsException!

        // TODO: Wrap in try-catch and print a friendly message
        // Expected output if index is invalid:
        // "Error: Index 10 is out of bounds for array of length 5"

        // TODO: Also print the value if access succeeds
        // Expected output if index is valid:
        // "Value at index 2: 30"
    }

    // TODO: Create a method that safely gets a value from an array
    // If index is invalid, return -1 instead of throwing
    public static int safeGet(int[] array, int index) {
        // Implement this!
    }
}
```

**Part B: Multiple exception types**

Create a program that:
1. Asks user for an array index
2. Catches `ArrayIndexOutOfBoundsException` if index is invalid
3. Catches `NumberFormatException` if user enters non-numeric input
4. Uses different error messages for each case

### Exercise 2: Throw My Exception (nogen hjaelp - Moderate Guidance)

**Goal:** Create and use a custom exception class.

**Part A: Create InvalidAgeException**

```java
// Create this class in its own file: InvalidAgeException.java
public class InvalidAgeException extends Exception {
    // TODO: Add an instance variable to store the invalid age value

    // TODO: Create constructor that takes message and invalid age

    // TODO: Create getter for the invalid age

    // TODO: Override getMessage() to include the invalid age
}
```

**Part B: Use your exception**

```java
public class Person {
    private String name;
    private int age;

    // TODO: Create setAge method that throws InvalidAgeException
    // if age is < 0 or > 150

    // TODO: Create setName method that throws IllegalArgumentException
    // if name is null or empty
}

public class ThrowMyException {
    public static void main(String[] args) {
        Person p = new Person();

        // TODO: Try setting invalid age, catch your custom exception
        // Print: "Cannot set age: [getMessage result]"

        // TODO: Try setting invalid name, catch IllegalArgumentException
        // Print: "Cannot set name: [getMessage result]"
    }
}
```

### Exercise 3: User Admin (ingen hjaelp - Minimal Guidance)

**Goal:** Build a complete user management system with comprehensive exception handling.

Create a user administration system with:

**Custom Exceptions:**
- `UserNotFoundException` - when user does not exist
- `DuplicateUserException` - when username already exists
- `InvalidPasswordException` - when password does not meet requirements

**User class:**
- username (String)
- password (String, at least 8 characters)
- email (String)
- active (boolean)

**UserManager class:**
- `addUser(User user) throws DuplicateUserException`
- `removeUser(String username) throws UserNotFoundException`
- `findUser(String username) throws UserNotFoundException`
- `updatePassword(String username, String newPassword) throws UserNotFoundException, InvalidPasswordException`
- `loadFromFile(String filename)` - load users from file
- `saveToFile(String filename)` - save users to file

**Main program with menu:**
```
=== User Admin System ===
1. Add user
2. Remove user
3. Find user
4. Update password
5. List all users
6. Save and exit
Choose:
```

**Requirements:**
- All operations handle appropriate exceptions
- File operations use try-with-resources
- Meaningful error messages shown to user
- Users persist between runs

### Exercise 4: Logging Those Actions (ingen hjaelp - Minimal Guidance)

**Goal:** Create an action logger with exception handling and file persistence.

Build a logging system that:

1. **Logs actions to a file** with timestamp
2. **Uses append mode** so history is preserved
3. **Creates custom exceptions** for log errors
4. **Handles all file I/O exceptions** gracefully

**Logger class requirements:**
- Constructor takes filename
- `log(String action)` - logs action with timestamp
- `logError(String error)` - logs with "ERROR:" prefix
- `logWarning(String warning)` - logs with "WARNING:" prefix
- `readAll()` - returns all log entries as ArrayList<String>
- `clearOlderThan(int days)` - removes old entries

**Log file format:**
```
2024-10-11 14:30:25 | INFO | User logged in
2024-10-11 14:30:45 | WARNING | Invalid password attempt
2024-10-11 14:31:02 | ERROR | Database connection failed
```

**Custom exception:**
- `LogWriteException` - when logging fails

**Integration with User Admin:**
Add logging to the User Admin system from Exercise 3:
- Log each successful user operation
- Log errors when operations fail
- Log system startup and shutdown

---

## Looking Ahead

### Week 13: Unit Testing

Exception handling is ESSENTIAL for testing:

```java
// Testing that exceptions ARE thrown when expected
@Test
void testInvalidAge() {
    Person p = new Person();
    assertThrows(InvalidAgeException.class, () -> {
        p.setAge(-5);
    });
}

// Testing that code handles exceptions correctly
@Test
void testMissingFile() {
    UserManager manager = new UserManager();
    // Should handle gracefully, not crash
    assertDoesNotThrow(() -> {
        manager.loadFromFile("nonexistent.txt");
    });
}
```

Your custom exceptions from this week will be tested in Week 13!

### Weeks 14-15: Sorting and Interfaces

Comparators can throw exceptions:

```java
public int compare(Student s1, Student s2) {
    if (s1 == null || s2 == null) {
        throw new NullPointerException("Cannot compare null students");
    }
    return s1.getName().compareTo(s2.getName());
}
```

### Real-World Applications

Exception handling is used everywhere in professional development:
- Web applications handle HTTP errors
- Database applications handle connection failures
- APIs return appropriate error codes
- Logging systems capture exceptions for debugging

---

## Key Takeaways

1. **Exceptions are objects** - they are instances of classes, just like your Student or Car

2. **Errors vs. Exceptions** - Errors are fatal (don't catch), Exceptions are recoverable (do handle)

3. **Checked vs. Unchecked** - Checked must be handled (external problems), Unchecked are typically bugs

4. **try-catch-finally** - try the risky code, catch exceptions, finally always runs for cleanup

5. **try-with-resources** - automatic resource cleanup: `try (Resource r = ...) { }`

6. **throw** creates exceptions - `throw new ExceptionType("message")`

7. **throws** declares exceptions - `public void method() throws ExceptionType`

8. **Custom exceptions use OOP** - extend Exception (checked) or RuntimeException (unchecked)

9. **Exception hierarchy uses inheritance** - catching parent catches all children

10. **Stack traces are your friend** - read them to find where and why errors occur

11. **Be specific** - catch specific exceptions, throw meaningful exceptions

12. **Never swallow exceptions** - at minimum, log them!

13. **Throw early, catch late** - validate inputs immediately, handle at appropriate level

14. **Clean up resources** - use try-with-resources or finally

---

## For the Next Topic Agent

### Terminology Established This Week

- **exception**: An object representing an abnormal condition during program execution
- **error**: A serious problem that typically cannot be recovered from (OutOfMemoryError, StackOverflowError)
- **throwable**: The parent class of both Error and Exception
- **checked exception**: Exception that MUST be handled or declared; extends Exception but not RuntimeException
- **unchecked exception**: Exception that does NOT require handling; extends RuntimeException
- **try block**: Code that might throw an exception
- **catch block**: Code that handles a specific exception type
- **finally block**: Code that ALWAYS runs, regardless of exceptions
- **try-with-resources**: Automatic resource management syntax; resources auto-close
- **throw**: Keyword to create and throw an exception
- **throws**: Keyword in method signature declaring possible exceptions
- **stack trace**: Debug information showing method call sequence leading to exception
- **exception propagation**: Exception "bubbling up" through call stack until caught
- **custom exception**: User-defined exception class extending Exception or RuntimeException
- **exception hierarchy**: Inheritance tree of exception classes
- **swallowing exceptions**: Catching without handling (bad practice!)

### Concepts From Prior Weeks Applied

| Prior Week | Concept | Week 12 Application |
|------------|---------|---------------------|
| Week 11 | FileNotFoundException | Now understood as checked exception |
| Week 11 | try-with-resources | Deeper understanding of why it works |
| Week 9 | Inheritance | Custom exceptions extend Exception |
| Week 9 | Polymorphism | Catching parent catches children |
| Week 8 | Constructors | Custom exception constructors |
| Week 8 | Encapsulation | Exception instance variables and getters |
| Week 7 | Classes/Objects | Exceptions ARE objects |
| Week 6 | Arrays | ArrayIndexOutOfBoundsException |
| Week 2 | Conditionals | Validation before throwing |

### Student Capabilities After This Week

Students can now:
- Explain the difference between errors and exceptions
- Distinguish checked from unchecked exceptions
- Write try-catch blocks for exception handling
- Use multiple catch blocks for different exception types
- Implement finally blocks for guaranteed cleanup
- Use try-with-resources for resource management
- Throw exceptions using the throw keyword
- Declare exceptions using the throws keyword
- Create custom checked and unchecked exception classes
- Read and interpret stack traces for debugging
- Apply exception handling best practices

### Critical Concepts for Week 13 (Unit Testing)

Week 13 should build on these Week 12 foundations:
- **Testing exception throwing**: assertThrows() to verify exceptions occur
- **Testing exception handling**: Verify code handles errors gracefully
- **Custom exceptions in tests**: Test that custom exceptions have correct messages
- **Edge case testing**: Invalid inputs that trigger exceptions

Exception patterns students have created:

```java
public class InvalidUserException extends Exception {
    public InvalidUserException(String message) {
        super(message);
    }
}

public void registerUser(String username) throws InvalidUserException {
    if (userExists(username)) {
        throw new InvalidUserException("User already exists: " + username);
    }
}
```

Week 13 will teach:
- Testing that exceptions ARE thrown: `assertThrows(InvalidUserException.class, () -> {...})`
- Testing exception messages: `assertEquals("expected message", exception.getMessage())`
- Testing that code handles exceptions correctly
- Test coverage including exception paths

### Common Misconceptions to Address Later

1. "Exceptions are always bad" - No, they are signals that enable graceful handling
2. "Catch everything with Exception" - No, be specific for better error handling
3. "Unchecked exceptions don't matter" - They indicate bugs that need fixing
4. "Custom exceptions are overkill" - They enable domain-specific error handling
5. "Stack traces are scary" - They are debugging roadmaps!

### Assessment Preparation Notes

Exception handling comprises 20-25% of exam. Key patterns:
1. Write try-catch for specific exception types
2. Implement finally or try-with-resources for cleanup
3. Create custom exception classes with appropriate inheritance
4. Use throw to signal error conditions
5. Use throws to declare exceptions in method signatures
6. Read stack traces to identify error sources
7. Choose appropriate handling strategy (catch vs. throw)

Typical exam question pattern:
- Given: A scenario with potential errors (file I/O, validation)
- Task: Implement exception handling with custom exceptions
- Requirements: Proper use of checked/unchecked, meaningful messages, resource cleanup
