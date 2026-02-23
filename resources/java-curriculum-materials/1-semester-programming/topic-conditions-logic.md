# Conditions and Logic - Week 2

*Prerequisites: Week 1 - Input, Output, Data Types, and Calculations*
*Phase: Phase 1: Foundation Building*

---

## What You'll Learn

By the end of this week, you will be able to:

- Make your programs **decide** what to do based on conditions
- Compare values using **relational operators** (greater than, less than, equal to, etc.)
- Combine multiple conditions using **logical operators** (AND, OR, NOT)
- Write **if-else statements** for two-way decisions
- Chain conditions together for multiple choices using **else-if**
- Use **switch statements** for clean multi-way branching
- Store and work with **boolean values** (true/false)

This week transforms your programs from simple calculators into intelligent decision-makers. You are about to give your programs the ability to think!

---

## Why This Matters

Last week, your programs were like a straight road - they executed every line from top to bottom, always doing the same thing. But real programs need to adapt. Consider these everyday scenarios:

- A **login system** must check if the password is correct
- A **game** decides what happens based on the player's health
- A **weather app** shows different advice depending on the temperature
- A **store checkout** applies discounts only if you have a coupon

Every useful program makes decisions. Without conditions, your calculator could not even tell the user they divided by zero - it would just crash! Conditional logic is what makes programs respond intelligently to different situations.

---

## Building Your Intuition

### The Big Picture

Think of conditional logic like the decisions you make every day:

**Morning routine analogy:**
- **If** it is raining, **then** take an umbrella, **else** leave it at home
- **If** the alarm did not ring AND you are late, **then** skip breakfast
- **If** it is Monday OR Friday, **then** wear the special shirt

Your programs make decisions in exactly the same way. They evaluate a condition (is it raining?), and based on whether that condition is true or false, they take different actions.

**Traffic light analogy:**
Think of a traffic light controller:
- **If** the light is green, cars go
- **If** the light is yellow, cars slow down
- **If** the light is red, cars stop

This is exactly how if-else-if chains work in programming. The program checks each condition in order and executes the matching action.

### Connecting to What You Already Know

Remember from Week 1:
- You know how to store values in **variables**
- You know how to get **input** from users
- You know how to perform **calculations**

Now you will learn how to make your program *react* to those values. Instead of just calculating someone's age, you can now determine if they are old enough to vote. Instead of just storing a password, you can check if it matches!

### Common Questions Beginners Ask

**"What is the difference between = and ==?"**
This is the #1 source of bugs for beginners! They look similar but do completely different things:
- `=` is **assignment** - it puts a value into a variable: `age = 25`
- `==` is **comparison** - it checks if two values are equal: `age == 25`

Think of it this way: "age = 25" means "store 25 in age." "age == 25" means "is age equal to 25?"

**"Why does my if statement always run (or never run)?"**
You might have used `=` when you meant `==`. This is such a common mistake that we will cover it multiple times.

**"When should I use if-else versus switch?"**
Use `if-else` when comparing ranges or complex conditions. Use `switch` when checking one variable against many specific values. We will explore this in detail.

**"What does short-circuit evaluation mean?"**
When Java evaluates `&&` (AND) and `||` (OR), it stops as soon as it knows the answer. If the first part of an AND is false, why bother checking the second part? The whole thing is already false! This is called "short-circuit" evaluation.

---

## Understanding Boolean Values

### What Is a Boolean?

A **boolean** is a data type that can only hold one of two values: `true` or `false`. Nothing else - no "maybe," no "sometimes," just true or false.

You encountered booleans briefly in Week 1, but now they become central to everything we do.

### Why Do We Need Booleans?

Booleans are the foundation of all decision-making in programming. Every condition you write evaluates to a boolean:

- "Is the user logged in?" - true or false
- "Is the temperature below freezing?" - true or false
- "Did the player win?" - true or false

Think of booleans as the answers to yes/no questions. Your program asks questions, gets boolean answers, and decides what to do based on those answers.

### How Booleans Work

You can create boolean variables directly, or they can be the result of comparisons:

```java
// Creating boolean variables directly
boolean isGameOver = false;       // We are stating this is false
boolean hasPermission = true;     // We are stating this is true

// Booleans from comparisons (these are evaluated automatically)
int age = 20;
boolean isAdult = age >= 18;      // 20 >= 18 is true, so isAdult becomes true
boolean isTeenager = age < 20;    // 20 < 20 is false, so isTeenager becomes false

// Using boolean variables
System.out.println("Is adult: " + isAdult);       // Displays: Is adult: true
System.out.println("Is teenager: " + isTeenager); // Displays: Is teenager: false
```

**Key insight:** When you write `age >= 18`, Java evaluates this and produces a boolean result. That result can be stored in a boolean variable or used directly in an if statement.

---

## Understanding Relational Operators

### What Are Relational Operators?

**Relational operators** (also called comparison operators) compare two values and produce a boolean result. They answer questions like "is this greater than that?" or "are these equal?"

### Why Do We Need Them?

Without comparison, your program cannot make decisions. You need to compare:
- A user's input to the correct password
- A player's score to the high score
- Today's date to a deadline
- An item's price to your budget

### The Six Relational Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `true` |
| `!=` | Not equal to | `5 != 3` | `true` |
| `>` | Greater than | `10 > 5` | `true` |
| `<` | Less than | `3 < 7` | `true` |
| `>=` | Greater than or equal to | `5 >= 5` | `true` |
| `<=` | Less than or equal to | `4 <= 3` | `false` |

### Seeing Relational Operators in Action

```java
int score = 85;
int passingScore = 70;
int perfectScore = 100;

// Comparing values produces boolean results
boolean passed = score >= passingScore;     // 85 >= 70 is true
boolean perfect = score == perfectScore;   // 85 == 100 is false
boolean needsImprovement = score < 70;     // 85 < 70 is false

System.out.println("Passed: " + passed);              // Passed: true
System.out.println("Perfect score: " + perfect);      // Perfect score: false
System.out.println("Needs improvement: " + needsImprovement); // Needs improvement: false

// You can also compare directly in output
System.out.println("Score above 80? " + (score > 80)); // Score above 80? true
```

**Notice the parentheses** around `(score > 80)`. When combining comparisons with string concatenation, parentheses ensure the comparison happens first.

### Common Mistakes with Relational Operators

**Mistake 1: Using = instead of == (THE MOST COMMON BUG)**
```java
int x = 5;
if (x = 10) {    // WRONG! This tries to assign 10 to x, not compare!
    // This causes a compiler error in Java (thankfully!)
}
```

**Fix:**
```java
int x = 5;
if (x == 10) {   // CORRECT! This compares x to 10
    // This works properly
}
```

**Mistake 2: Confusing > and >= (or < and <=)**
```java
int age = 18;
// Is this person old enough to vote (must be 18 or older)?

boolean canVote = age > 18;   // WRONG! This excludes exactly 18
// age is 18, and 18 > 18 is false

boolean canVoteCorrect = age >= 18;  // CORRECT! Includes 18 and above
// age is 18, and 18 >= 18 is true
```

**Mistake 3: Comparing strings with ==**
```java
String name = "Alice";
if (name == "Alice") {  // This MIGHT work, but is unreliable for strings!
    // ...
}
```

**Fix:** Use `.equals()` for comparing strings (we will cover this more in later weeks):
```java
if (name.equals("Alice")) {  // CORRECT way to compare strings
    // ...
}
```

---

## Understanding If Statements

### What Is an If Statement?

An **if statement** tells Java: "Only run this code IF this condition is true." It is the most basic form of decision-making in programming.

### Why Do We Need If Statements?

If statements allow your program to respond to different situations:
- Only show an error message if the user entered invalid data
- Only apply a discount if the customer has a coupon
- Only end the game if the player's health reaches zero

### How If Statements Work

The structure is:
```
if (condition) {
    // code to run if condition is true
}
```

If the condition is true, the code inside the curly braces runs. If the condition is false, the code is skipped entirely.

### Seeing If Statements in Action

```java
int temperature = 35;  // Temperature in Celsius

// Simple if statement
if (temperature > 30) {
    System.out.println("It's a hot day!");
    System.out.println("Remember to stay hydrated.");
}

System.out.println("Have a good day!");  // This ALWAYS runs

// Output:
// It's a hot day!
// Remember to stay hydrated.
// Have a good day!
```

**What happens if temperature is 25?**
```java
int temperature = 25;

if (temperature > 30) {
    System.out.println("It's a hot day!");        // Skipped!
    System.out.println("Remember to stay hydrated.");  // Skipped!
}

System.out.println("Have a good day!");  // This still runs

// Output:
// Have a good day!
```

The code inside the if block is simply skipped when the condition is false. The program continues with whatever comes after.

### Real-World Example: Age Verification

```java
import java.util.Scanner;

public class AgeCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        if (age >= 18) {
            System.out.println("You are eligible to vote.");
            System.out.println("Please proceed to registration.");
        }

        System.out.println("Thank you for using our system.");
    }
}
```

If the user enters 20:
```
Enter your age: 20
You are eligible to vote.
Please proceed to registration.
Thank you for using our system.
```

If the user enters 15:
```
Enter your age: 15
Thank you for using our system.
```

Notice how the voting messages are skipped when age is below 18, but the thank you message always appears.

---

## Understanding If-Else Statements

### What Is If-Else?

An **if-else statement** handles two possibilities: what to do if the condition is true, AND what to do if it is false. It creates two distinct paths through your program.

### Why Do We Need Else?

Sometimes you need to do one thing OR another, never both:
- Display "Correct!" OR "Try again"
- Grant access OR show "Access denied"
- Apply a discount OR charge full price

### How If-Else Works

```
if (condition) {
    // code to run if condition is TRUE
} else {
    // code to run if condition is FALSE
}
```

**Exactly one block will run** - never both, never neither.

### Seeing If-Else in Action

```java
int score = 65;
int passingScore = 70;

if (score >= passingScore) {
    System.out.println("Congratulations! You passed!");
} else {
    System.out.println("Sorry, you did not pass.");
    System.out.println("Please study and try again.");
}
```

With score = 65:
```
Sorry, you did not pass.
Please study and try again.
```

With score = 75:
```
Congratulations! You passed!
```

### Real-World Example: Login Check

```java
import java.util.Scanner;

public class SimpleLogin {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String correctPassword = "secret123";

        System.out.print("Enter password: ");
        String enteredPassword = scanner.nextLine();

        if (enteredPassword.equals(correctPassword)) {
            System.out.println("Welcome! Login successful.");
            System.out.println("Loading your dashboard...");
        } else {
            System.out.println("Incorrect password.");
            System.out.println("Please try again.");
        }
    }
}
```

**Note:** We use `.equals()` to compare strings, not `==`. This is a Java-specific detail that will be explained more in later weeks.

### Common Mistakes with If-Else

**Mistake 1: Forgetting the curly braces**
```java
if (score >= 70)
    System.out.println("You passed!");
    System.out.println("Great job!");   // WARNING: This ALWAYS runs!
```

Without braces, only the first line is part of the if statement. The second line is NOT part of the if - it runs no matter what!

**Fix:** Always use curly braces, even for single lines:
```java
if (score >= 70) {
    System.out.println("You passed!");
    System.out.println("Great job!");
}
```

**Mistake 2: Adding a semicolon after if**
```java
if (score >= 70); {    // WRONG! That semicolon ends the if statement
    System.out.println("You passed!");  // This ALWAYS runs
}
```

The semicolon makes Java think the if statement is complete (with an empty body). The block that follows is not connected to the if.

**Fix:** No semicolon after the condition:
```java
if (score >= 70) {
    System.out.println("You passed!");
}
```

---

## Understanding Else-If Chains

### What Are Else-If Chains?

**Else-if chains** let you check multiple conditions in sequence, where only the first matching condition runs. Think of it as "if this, else if that, else if that other thing, else do this default action."

### Why Do We Need Else-If?

Real decisions often have more than two outcomes:
- A grade could be A, B, C, D, or F
- Weather could be hot, warm, cool, or cold
- A number could be positive, negative, or zero

### How Else-If Chains Work

```
if (condition1) {
    // runs if condition1 is true
} else if (condition2) {
    // runs if condition1 is false AND condition2 is true
} else if (condition3) {
    // runs if condition1 and condition2 are false AND condition3 is true
} else {
    // runs if ALL conditions above are false
}
```

**Key insight:** Java checks conditions from top to bottom. The FIRST true condition wins, and the rest are skipped.

### Seeing Else-If in Action: Grade Calculator

```java
int score = 82;
String grade;

if (score >= 90) {
    grade = "A";
} else if (score >= 80) {
    grade = "B";
} else if (score >= 70) {
    grade = "C";
} else if (score >= 60) {
    grade = "D";
} else {
    grade = "F";
}

System.out.println("Your grade is: " + grade);  // Your grade is: B
```

**Walk through the logic:**
1. Is 82 >= 90? No, skip to else-if
2. Is 82 >= 80? **Yes!** Assign "B" and skip all remaining conditions
3. The checks for 70 and 60 never happen - we already found our answer

**Why the order matters:**
```java
// WRONG ORDER - this gives wrong results!
if (score >= 60) {
    grade = "D";       // A score of 95 would get "D" because 95 >= 60 is true!
} else if (score >= 70) {
    grade = "C";
} else if (score >= 80) {
    grade = "B";
} else if (score >= 90) {
    grade = "A";
}
```

When checking ranges, always start with the most restrictive condition (highest threshold) and work down.

### Real-World Example: Temperature Advice

```java
import java.util.Scanner;

public class WeatherAdvice {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("What is the temperature in Celsius? ");
        int temp = scanner.nextInt();

        System.out.print("Clothing recommendation: ");

        if (temp >= 30) {
            System.out.println("Light clothes, stay cool!");
        } else if (temp >= 20) {
            System.out.println("T-shirt weather, enjoy!");
        } else if (temp >= 10) {
            System.out.println("Bring a jacket.");
        } else if (temp >= 0) {
            System.out.println("Wear a warm coat.");
        } else {
            System.out.println("Bundle up! It's freezing!");
        }
    }
}
```

---

## Understanding Logical Operators

### What Are Logical Operators?

**Logical operators** combine multiple boolean values or conditions into a single boolean result. They answer questions like "is this AND that true?" or "is this OR that true?"

### Why Do We Need Logical Operators?

Real-world decisions often depend on multiple conditions:
- Grant access if username is correct AND password is correct
- Apply senior discount if age is 65 OR older
- Enable the button if form is complete AND NOT already submitted

### The Three Logical Operators

| Operator | Name | Meaning | Example |
|----------|------|---------|---------|
| `&&` | AND | Both must be true | `age >= 18 && hasLicense` |
| `\|\|` | OR | At least one must be true | `isStudent \|\| isSenior` |
| `!` | NOT | Reverses true/false | `!isGameOver` |

### Understanding AND (&&)

`&&` returns true only if BOTH sides are true:

| Left | Right | Result |
|------|-------|--------|
| true | true | **true** |
| true | false | false |
| false | true | false |
| false | false | false |

**Real-world analogy:** "I will go to the beach if it is sunny AND I have free time." Both conditions must be true for you to go.

```java
int age = 20;
boolean hasTicket = true;

// Can attend the concert if adult AND has ticket
if (age >= 18 && hasTicket) {
    System.out.println("Welcome to the concert!");
}

// Both conditions are true (20 >= 18 is true, hasTicket is true)
// So the message displays
```

### Understanding OR (||)

`||` returns true if AT LEAST ONE side is true:

| Left | Right | Result |
|------|-------|--------|
| true | true | **true** |
| true | false | **true** |
| false | true | **true** |
| false | false | false |

**Real-world analogy:** "I will be happy if I get a raise OR if I get a promotion." Either one (or both) makes you happy.

```java
boolean isStudent = true;
boolean isSenior = false;

// Discount applies if student OR senior
if (isStudent || isSenior) {
    System.out.println("You qualify for a discount!");
}

// isStudent is true, so the whole condition is true
// Even though isSenior is false, one true is enough for OR
```

### Understanding NOT (!)

`!` reverses a boolean value:

| Original | After NOT |
|----------|-----------|
| true | false |
| false | true |

**Real-world analogy:** "If the door is NOT locked, you can enter."

```java
boolean isGameOver = false;

// Keep playing while game is NOT over
if (!isGameOver) {
    System.out.println("Game continues...");
}

// !false becomes true, so the message displays
```

### Short-Circuit Evaluation

This is a crucial concept that helps you write efficient and safe code.

**Short-circuit AND (&&):**
If the left side is false, Java does not even check the right side. Why? Because false AND anything is always false.

```java
int x = 0;

// Java checks left side first: x != 0 is false
// Since false && anything is false, Java skips checking (10 / x > 2)
// This is good because 10 / 0 would cause an error!
if (x != 0 && 10 / x > 2) {
    System.out.println("Result is greater than 2");
}
```

**Short-circuit OR (||):**
If the left side is true, Java does not check the right side. Why? Because true OR anything is always true.

```java
boolean hasVIPPass = true;

// Java checks left side first: hasVIPPass is true
// Since true || anything is true, Java skips checking isPremiumMember
if (hasVIPPass || isPremiumMember()) {
    System.out.println("Welcome to the VIP area!");
}
```

### Combining Multiple Conditions

You can combine multiple logical operators, but be careful with precedence:
- `!` (NOT) has highest precedence
- `&&` (AND) comes next
- `||` (OR) has lowest precedence

Use parentheses to make your intentions clear:

```java
int age = 25;
boolean isStudent = true;
boolean isEmployee = false;

// Discount for: young people (under 25) OR students OR employees
if (age < 25 || isStudent || isEmployee) {
    System.out.println("Discount applies!");  // true - isStudent is true
}

// VIP access for: adults who are students AND employees
if (age >= 18 && isStudent && isEmployee) {
    System.out.println("VIP access granted!");  // false - isEmployee is false
}

// Complex condition with parentheses for clarity
// Weekend discount: (young OR senior) AND (member)
boolean isSenior = false;
boolean isMember = true;

if ((age < 25 || isSenior) && isMember) {
    System.out.println("Weekend discount!");  // true!
}
// (true || false) && true  ->  true && true  ->  true
```

### Common Mistakes with Logical Operators

**Mistake 1: Using & instead of && (or | instead of ||)**
```java
// Single & and | are bitwise operators - different behavior!
if (x > 0 & y > 0) {   // This works but always evaluates BOTH sides
    // ...
}
```

**Fix:** Use `&&` and `||` for logical operations - they short-circuit:
```java
if (x > 0 && y > 0) {  // Correct - stops early if x > 0 is false
    // ...
}
```

**Mistake 2: Confusing precedence**
```java
// Without parentheses, this might not do what you expect
if (a || b && c) {
    // This is evaluated as: a || (b && c)
    // Because && has higher precedence than ||
}
```

**Fix:** Use parentheses to show exactly what you mean:
```java
if ((a || b) && c) {   // Now it is clear: must have (a OR b) AND c
    // ...
}
```

---

## Understanding Switch Statements

### What Is a Switch Statement?

A **switch statement** provides a clean way to execute different code based on the value of a single variable. It is an alternative to long else-if chains when you are comparing one value against multiple specific options.

### Why Do We Need Switch?

Compare these two approaches:

```java
// Using if-else-if (works but verbose)
if (day == 1) {
    dayName = "Monday";
} else if (day == 2) {
    dayName = "Tuesday";
} else if (day == 3) {
    dayName = "Wednesday";
} // ... and so on
```

```java
// Using switch (cleaner!)
switch (day) {
    case 1: dayName = "Monday"; break;
    case 2: dayName = "Tuesday"; break;
    case 3: dayName = "Wednesday"; break;
    // ... and so on
}
```

Switch is often cleaner when comparing one variable against many specific values.

### How Switch Works (Traditional Syntax)

```java
switch (variable) {
    case value1:
        // code for value1
        break;
    case value2:
        // code for value2
        break;
    default:
        // code if no case matches
        break;
}
```

**Important:** The `break` statement exits the switch. Without it, execution "falls through" to the next case!

### Seeing Switch in Action

```java
int dayNumber = 3;
String dayName;

switch (dayNumber) {
    case 1:
        dayName = "Monday";
        break;
    case 2:
        dayName = "Tuesday";
        break;
    case 3:
        dayName = "Wednesday";
        break;
    case 4:
        dayName = "Thursday";
        break;
    case 5:
        dayName = "Friday";
        break;
    case 6:
        dayName = "Saturday";
        break;
    case 7:
        dayName = "Sunday";
        break;
    default:
        dayName = "Invalid day";
        break;
}

System.out.println("Day: " + dayName);  // Day: Wednesday
```

### Modern Switch Syntax (Java 14+)

Java has a newer, cleaner switch syntax using arrows:

```java
int dayNumber = 3;

String dayName = switch (dayNumber) {
    case 1 -> "Monday";
    case 2 -> "Tuesday";
    case 3 -> "Wednesday";
    case 4 -> "Thursday";
    case 5 -> "Friday";
    case 6 -> "Saturday";
    case 7 -> "Sunday";
    default -> "Invalid day";
};

System.out.println("Day: " + dayName);  // Day: Wednesday
```

**Advantages of new syntax:**
- No need for `break` statements
- Can directly return values
- Cleaner and less error-prone

### Grouping Cases

Sometimes multiple values should produce the same result:

```java
// Traditional syntax - grouping cases
switch (day) {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        System.out.println("Weekday");
        break;
    case 6:
    case 7:
        System.out.println("Weekend");
        break;
}

// Modern syntax - grouping is cleaner
String dayType = switch (day) {
    case 1, 2, 3, 4, 5 -> "Weekday";
    case 6, 7 -> "Weekend";
    default -> "Invalid";
};
```

### When to Use Switch vs If-Else

**Use switch when:**
- Comparing ONE variable against SPECIFIC values
- You have many distinct cases to handle
- The values are discrete (integers, strings, enum values)

**Use if-else when:**
- Checking ranges (score >= 90)
- Comparing multiple different variables
- Using complex boolean expressions
- Conditions involve AND/OR logic

```java
// Good for switch - one variable, specific values
switch (menuChoice) {
    case 1 -> startNewGame();
    case 2 -> loadGame();
    case 3 -> showSettings();
    case 4 -> exitGame();
}

// Better as if-else - checking ranges
if (score >= 90) {
    grade = "A";
} else if (score >= 80) {
    grade = "B";
}

// Better as if-else - multiple variables and conditions
if (age >= 18 && hasLicense && !isIntoxicated) {
    allowDriving = true;
}
```

### Common Mistakes with Switch

**Mistake 1: Forgetting break (traditional syntax)**
```java
int x = 1;
switch (x) {
    case 1:
        System.out.println("One");
        // Missing break! Falls through to case 2
    case 2:
        System.out.println("Two");
        break;
}
// Output:
// One
// Two   <- Unintended!
```

**Fix:** Always include break (or use modern arrow syntax):
```java
switch (x) {
    case 1:
        System.out.println("One");
        break;  // Now it stops here
    case 2:
        System.out.println("Two");
        break;
}
```

**Mistake 2: Forgetting the default case**
```java
switch (userInput) {
    case 1 -> doOptionOne();
    case 2 -> doOptionTwo();
    // What if user enters 3? Nothing happens - might be confusing!
}
```

**Fix:** Include a default case for unexpected values:
```java
switch (userInput) {
    case 1 -> doOptionOne();
    case 2 -> doOptionTwo();
    default -> System.out.println("Invalid option. Please try again.");
}
```

---

## Understanding the Ternary Operator

### What Is the Ternary Operator?

The **ternary operator** (also called the conditional operator) is a shorthand for simple if-else statements that assign a value. It is called "ternary" because it takes three parts.

### Syntax

```
result = condition ? valueIfTrue : valueIfFalse;
```

### When to Use It

Use the ternary operator for simple assignments where you choose between two values:

```java
// Using if-else (verbose for simple assignment)
String status;
if (age >= 18) {
    status = "Adult";
} else {
    status = "Minor";
}

// Using ternary (concise)
String status = age >= 18 ? "Adult" : "Minor";
```

Both do exactly the same thing. The ternary version is more compact for simple cases.

### Examples

```java
int score = 75;
String result = score >= 70 ? "Pass" : "Fail";
System.out.println(result);  // Pass

int number = -5;
String sign = number >= 0 ? "Positive or zero" : "Negative";
System.out.println(sign);  // Negative

// Finding the larger of two numbers
int a = 10, b = 15;
int max = a > b ? a : b;
System.out.println("Larger: " + max);  // Larger: 15

// Can be used directly in output
System.out.println("Status: " + (score >= 70 ? "PASS" : "FAIL"));
```

### When NOT to Use Ternary

Avoid ternary for complex conditions or multiple statements:

```java
// DON'T do this - hard to read!
String result = score >= 90 ? "A" : score >= 80 ? "B" : score >= 70 ? "C" : "F";

// Use if-else-if instead for clarity
String result;
if (score >= 90) {
    result = "A";
} else if (score >= 80) {
    result = "B";
} else if (score >= 70) {
    result = "C";
} else {
    result = "F";
}
```

---

## Nested If Statements

### What Are Nested If Statements?

**Nested if statements** are if statements inside other if statements. They let you make secondary decisions after a primary decision.

### Why Nesting?

Sometimes you need to check one condition first, then check additional conditions only if the first is true:
- First check if the user is logged in
- If logged in, then check if they have admin privileges

### Seeing Nested Ifs in Action

```java
boolean isLoggedIn = true;
boolean isAdmin = true;

if (isLoggedIn) {
    System.out.println("Welcome back!");

    if (isAdmin) {
        System.out.println("You have admin access.");
        System.out.println("Admin panel is available.");
    } else {
        System.out.println("You have regular user access.");
    }
} else {
    System.out.println("Please log in first.");
}
```

### Keep Nesting Shallow

Deeply nested code is hard to read and maintain. If you find yourself nesting more than 2-3 levels deep, consider restructuring:

```java
// Hard to read - too much nesting
if (condition1) {
    if (condition2) {
        if (condition3) {
            if (condition4) {
                // What are we even checking anymore?
            }
        }
    }
}

// Better - use logical operators or early returns
if (condition1 && condition2 && condition3 && condition4) {
    // Much clearer!
}
```

---

## Real-World Application: Traffic Light Exercise

This exercise ties together many concepts from this week. A traffic light system uses conditions to control what happens based on the light's color:

```java
import java.util.Scanner;

public class TrafficLight {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Traffic Light Controller");
        System.out.println("Enter light color (red, yellow, green): ");
        String light = scanner.nextLine().toLowerCase();

        switch (light) {
            case "red":
                System.out.println("STOP - Do not proceed");
                System.out.println("Wait for green light");
                break;
            case "yellow":
                System.out.println("CAUTION - Slow down");
                System.out.println("Prepare to stop");
                break;
            case "green":
                System.out.println("GO - Proceed with caution");
                System.out.println("Watch for pedestrians");
                break;
            default:
                System.out.println("Invalid color!");
                System.out.println("Traffic lights are red, yellow, or green");
                break;
        }
    }
}
```

---

## Common Struggles and How to Overcome Them

### Struggle 1: Confusing = and == (Assignment vs Comparison)

**The confusion:** "My if statement seems to always run" or "My condition is not working"

**The solution:** Remember this rule:
- Single `=` puts a value INTO a variable (assignment)
- Double `==` asks "are these equal?" (comparison)

```java
int x = 5;          // Assignment: x now holds 5
if (x == 10) {      // Comparison: is x equal to 10?
    // This will NOT run because 5 is not equal to 10
}
```

**Memory trick:** "Double equals for double-checking"

### Struggle 2: Complex Boolean Logic

**The confusion:** "I cannot figure out what my condition evaluates to"

**The solution:** Break it down step by step:

```java
// Complex condition
if (age >= 18 && (isStudent || isEmployee) && !isBlocked)

// Break it down:
// Step 1: age >= 18         -> Let's say true
// Step 2: isStudent         -> Let's say true
// Step 3: isEmployee        -> Let's say false
// Step 4: isStudent || isEmployee -> true || false = true
// Step 5: !isBlocked        -> Let's say isBlocked is false, so !false = true
// Step 6: true && true && true = true
```

Also, use intermediate boolean variables to clarify:

```java
boolean isAdult = age >= 18;
boolean hasAffiliation = isStudent || isEmployee;
boolean canAccess = !isBlocked;

if (isAdult && hasAffiliation && canAccess) {
    // Much easier to understand!
}
```

### Struggle 3: When to Use If-Else vs Switch

**The confusion:** "Which control structure should I use?"

**The solution:** Ask yourself these questions:
1. Am I comparing ONE variable to SPECIFIC values? -> Consider switch
2. Am I checking ranges (greater than, less than)? -> Use if-else
3. Am I combining multiple conditions with AND/OR? -> Use if-else
4. Do I have more than 4-5 specific values to check? -> Switch is cleaner

### Struggle 4: Operator Precedence with && and ||

**The confusion:** "My compound conditions give unexpected results"

**The solution:** When in doubt, use parentheses! They make your intentions clear and prevent precedence surprises:

```java
// Ambiguous - what runs first?
if (a || b && c)

// Clear - parentheses show exactly what you mean
if ((a || b) && c)   // a OR b, then AND with c
if (a || (b && c))   // a OR (b AND c)
```

**Remember:** `&&` has higher precedence than `||`, so `a || b && c` is evaluated as `a || (b && c)`.

---

## Practice Exercises

### Exercise 1: Number Classifier (meget hjalp - Maximum Guidance)

**Goal:** Practice basic if-else statements and comparison operators.

**Step-by-step instructions:**

1. Create a new Java file called `NumberClassifier.java`
2. Use Scanner to ask the user for an integer
3. Using if-else statements, determine and print:
   - If the number is positive, negative, or zero
   - If the number is even or odd (hint: use the modulo operator %)
4. Display both results to the user

**Expected output examples:**
```
Enter a number: 7
The number is positive.
The number is odd.

Enter a number: -4
The number is negative.
The number is even.

Enter a number: 0
The number is zero.
The number is even.
```

**Hints:**
- A number is positive if it is > 0
- A number is negative if it is < 0
- A number is even if number % 2 == 0
- A number is odd if number % 2 != 0

### Exercise 2: Grade Calculator (nogen hjalp - Moderate Guidance)

**Goal:** Practice else-if chains and logical operators.

**Instructions:**

1. Create a program that asks for a test score (0-100)
2. Assign a letter grade based on:
   - 90-100: A
   - 80-89: B
   - 70-79: C
   - 60-69: D
   - Below 60: F
3. Add validation: if the score is below 0 or above 100, print "Invalid score"
4. Display both the numeric score and letter grade

**What you will need:**
- Scanner for input
- else-if chain for grade assignment
- Logical operator (||) for validation check

**Challenge extension:** Add a special message if the score is exactly 100.

### Exercise 3: Movie Ticket Pricing (nogen hjalp - Moderate Guidance)

**Goal:** Practice combining multiple conditions with logical operators.

**Instructions:**

Create a program that calculates movie ticket prices:
- Base price: 120 kr
- Children (under 12): 50% discount
- Seniors (65 and over): 30% discount
- Students (any age, but must indicate student status): 20% discount
- Tuesday special: Additional 15% off the already discounted price

The program should ask for:
1. Age
2. Whether the person is a student (yes/no)
3. What day it is (or just whether it is Tuesday)

Then calculate and display the final price.

### Exercise 4: Traffic Light Controller (ingen hjalp - Minimal Guidance)

**Goal:** Apply switch statements and create a simple state-based program.

**Requirements:**
- Create a program that simulates a traffic light
- Accept input for the current light color (red, yellow, green)
- Display appropriate instructions for each color
- Handle invalid input gracefully
- Use switch statement (either traditional or modern syntax)
- Bonus: Add a pedestrian signal that should be "Walk" only when the traffic light is red

---

## Looking Ahead

This week you learned how to make your programs think and decide. These skills are essential for everything that follows:

- **Week 3 (Loops):** You will use conditions to control when loops start and stop. "Keep asking for input while the answer is invalid." "Repeat until the player says quit."

- **Week 4 (Methods):** Methods often use conditions for guard clauses. "If the input is invalid, return early." You will also use boolean return values: "Does this string contain the letter 'a'?"

- **Week 6 (Arrays):** You will search arrays using conditions. "Is this value in the array?" "Find all scores above 90."

- **Weeks 7-10 (OOP):** Encapsulation uses conditions for validation. "Only set the age if it is positive." Polymorphism relies on type checking.

Every interactive program uses conditional logic. The patterns you learned this week - comparing values, combining conditions, branching based on state - appear everywhere in programming.

---

## Key Takeaways

- **Boolean values** (`true`/`false`) are the foundation of all decision-making in programs
- **Relational operators** (==, !=, <, >, <=, >=) compare values and produce booleans
- **Logical operators** combine conditions: && (AND), || (OR), ! (NOT)
- **Short-circuit evaluation** means && stops if the left side is false; || stops if the left side is true
- **If statements** run code only when a condition is true
- **If-else statements** provide two paths - exactly one will run
- **Else-if chains** check multiple conditions in order - the first true condition wins
- **Switch statements** cleanly handle one variable with many specific values
- The **ternary operator** (`?:`) is shorthand for simple if-else value assignments
- **CRITICAL:** `=` is assignment, `==` is comparison - mixing them up is the most common bug!

---

## For the Next Topic Agent

### Terminology Established This Week

- **boolean**: A data type that holds only `true` or `false`
- **condition**: An expression that evaluates to true or false, used to control program flow
- **relational operators**: Operators that compare values (==, !=, <, >, <=, >=)
- **logical operators**: Operators that combine boolean values (&&, ||, !)
- **short-circuit evaluation**: The behavior where && stops on first false and || stops on first true
- **if statement**: A control structure that executes code only when a condition is true
- **else clause**: The alternative code path when an if condition is false
- **else-if chain**: Multiple conditions checked in sequence until one is true
- **switch statement**: A control structure for choosing among many specific values
- **case**: A single option in a switch statement
- **break**: A statement that exits from a switch (or loop - covered next week)
- **default**: The fallback case in a switch when no other case matches
- **ternary operator**: The `?:` operator for compact conditional value assignment
- **nested**: Placing one control structure inside another
- **control flow**: The order in which statements are executed in a program

### Example Classes/Concepts Created

- Grade calculator with else-if chains
- Login validation with string comparison
- Traffic light controller with switch statement
- Weather advice program with temperature ranges
- Number classifier (positive/negative, even/odd)

### Student Capabilities After This Week

Students can now:
- Create and use boolean variables
- Compare values using all six relational operators
- Combine conditions using && (AND), || (OR), and ! (NOT)
- Understand and leverage short-circuit evaluation
- Write if, if-else, and else-if-else statements
- Use switch statements for multi-way branching
- Apply the ternary operator for simple conditional assignments
- Nest if statements appropriately
- Avoid the = vs == confusion
- Choose between if-else and switch based on the situation

### Pedagogical Patterns Continued

- **Analogy-first approach**: Traffic lights, morning routines, daily decisions
- **Common mistakes sections**: Extensive coverage of = vs == and other pitfalls
- **Progressive exercise difficulty**: meget hjalp -> nogen hjalp -> ingen hjalp structure
- **Encouraging tone**: Normalizing the difficulty of boolean logic
- **Why before how**: Each concept motivated before syntax introduced
- **Heavily annotated code**: Comments explain the logic, not just the syntax
- **Small code examples**: Most under 15 lines, never overwhelming
- **Building on Week 1**: Explicitly connected to variables, input, output from previous week
