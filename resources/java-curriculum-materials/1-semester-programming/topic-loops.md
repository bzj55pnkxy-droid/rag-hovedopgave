# Loops - Week 3

*Prerequisites: Week 2 - Conditions and Logic*
*Phase: Phase 1: Foundation Building*

---

## What You'll Learn

By the end of this week, you will be able to:

- Use **while loops** to repeat code as long as a condition is true
- Apply **do-while loops** when you need the code to run at least once before checking
- Write **for loops** for counting and known iterations
- Control loop flow with **break** (exit early) and **continue** (skip to next iteration)
- Validate user input using loops and Scanner methods
- Choose the **right loop type** for each situation
- Debug **infinite loops** and **off-by-one errors** confidently
- Use **nested loops** for multi-dimensional problems

This week transforms your programs from making single decisions into performing repetitive tasks automatically. You are about to give your programs the ability to work tirelessly!

---

## Why This Matters

Last week, your programs could make decisions - "if this, do that." But imagine you needed to check something 100 times, or keep asking for input until the user gets it right. Without loops, you would need to copy and paste the same code over and over.

Consider these everyday scenarios:

- A **password system** keeps asking until you enter the correct password (or run out of attempts)
- A **game** runs the same game logic every frame until the player quits
- A **fitness app** counts down from 10 to 1 during an exercise
- A **calculator** asks "Do you want to calculate again?" after each result
- A **search function** checks every item in a list until it finds what you are looking for

Every useful program contains repetition. Without loops, your programs would be tedious to write and impossible to scale. Loops are what make computers powerful - they can repeat tasks millions of times without getting tired or making mistakes.

---

## Building Your Intuition

### The Big Picture

Think of loops like repetitive tasks in your daily life:

**Brushing teeth analogy:**
You do not brush each tooth once and declare yourself done. You brush back and forth for about 2 minutes. In programming terms:

```
while (timer has not reached 2 minutes) {
    brush back and forth
}
```

**Checking your phone analogy:**
You might check your phone every hour to see if you have new messages:

```
repeat every hour {
    if (new message) {
        read message
    }
}
```

**Counting down for a race:**
"3... 2... 1... GO!" - this is a loop that counts from 3 down to 1:

```
for (number from 3 down to 1) {
    announce number
    wait 1 second
}
say "GO!"
```

### Connecting to What You Already Know

Remember from Week 2:
- You know how to write **conditions** (like `count < 10` or `isValid == false`)
- You know how **boolean expressions** work (true/false)
- You know how to make **decisions** with if statements

Loops use the exact same conditions! The only difference is:
- An **if statement** checks the condition once and runs the code once
- A **loop** checks the condition repeatedly and runs the code multiple times

This is why understanding conditions from Week 2 was essential. The condition in a loop works exactly like the condition in an if statement - it evaluates to true or false.

### The Three Fundamental Loop Questions

Whenever you write a loop, ask yourself:

1. **What is the starting state?** (initialization)
   - Where does my counter start? What is my initial condition?

2. **When should the loop stop?** (termination condition)
   - This is the most critical question. A loop without a proper exit condition runs forever!

3. **What changes each time?** (progression)
   - Something must change to eventually make the condition false, or the loop will never end

These three questions apply to ALL types of loops. Keep them in mind as we explore each loop type.

---

## Understanding While Loops

### What Is a While Loop?

A **while loop** repeats a block of code as long as a condition is true. It checks the condition BEFORE each iteration, which is why it is called a "pre-test loop."

### Why Do We Need While Loops?

Use while loops when:
- You do not know in advance how many times you need to repeat
- The repetition depends on user input or some other condition
- You might not need to execute the loop body at all

Real examples:
- Keep asking for a password until it is correct
- Read lines from a file until you reach the end
- Process transactions while there are more to process

### How While Loops Work

The structure is:

```
while (condition) {
    // code to repeat
    // something here should eventually make condition false
}
```

**The flow:**
1. Check the condition
2. If true, execute the code inside the braces
3. Go back to step 1
4. If false, skip the code and continue after the loop

**Critical insight:** If the condition is false from the start, the code inside never runs at all. The condition is checked BEFORE the first iteration.

### Seeing While Loops in Action

```java
// Simple countdown
int countdown = 5;

while (countdown > 0) {
    System.out.println(countdown);
    countdown = countdown - 1;  // CRITICAL: This makes the loop eventually stop
}

System.out.println("Blastoff!");

// Output:
// 5
// 4
// 3
// 2
// 1
// Blastoff!
```

**Walk through this step by step:**

| Step | countdown | Is countdown > 0? | Action |
|------|-----------|-------------------|--------|
| 1 | 5 | true | Print 5, decrement to 4 |
| 2 | 4 | true | Print 4, decrement to 3 |
| 3 | 3 | true | Print 3, decrement to 2 |
| 4 | 2 | true | Print 2, decrement to 1 |
| 5 | 1 | true | Print 1, decrement to 0 |
| 6 | 0 | false | Exit loop, print "Blastoff!" |

This is called a **trace table** - a powerful tool for understanding exactly what happens in a loop.

### Real-World Example: Input Validation

This is one of the most common uses of while loops - keep asking until you get valid input:

```java
import java.util.Scanner;

public class AgeValidator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int age = -1;  // Start with an invalid value

        // Keep asking while the age is invalid
        while (age < 0 || age > 150) {
            System.out.print("Enter your age (0-150): ");
            age = scanner.nextInt();

            if (age < 0 || age > 150) {
                System.out.println("Invalid age. Please try again.");
            }
        }

        System.out.println("Your age is: " + age);
    }
}
```

**Why this works:**
- We start with `age = -1`, which is invalid (makes the condition true)
- The loop asks for input and checks if it is valid
- Only when the user enters a valid age does the condition become false
- Then the loop exits and we have a guaranteed valid age

### Common Mistakes with While Loops

**Mistake 1: Forgetting to update the loop variable (Infinite Loop!)**

```java
int count = 0;
while (count < 5) {
    System.out.println("Hello!");
    // OOPS! We never change count, so count < 5 is ALWAYS true
}
// This prints "Hello!" forever until you force-quit the program
```

**Fix:**
```java
int count = 0;
while (count < 5) {
    System.out.println("Hello!");
    count = count + 1;  // Now count increases, eventually reaching 5
}
```

**Mistake 2: Wrong condition direction**

```java
int count = 10;
while (count > 0) {
    System.out.println(count);
    count = count + 1;  // WRONG! We are increasing when we should decrease
}
// count goes 10, 11, 12, 13... forever
```

**Fix:**
```java
int count = 10;
while (count > 0) {
    System.out.println(count);
    count = count - 1;  // Now count decreases toward 0
}
```

**Mistake 3: Off-by-one error**

```java
int count = 1;
while (count < 5) {  // Will print 1, 2, 3, 4 - NOT 5!
    System.out.println(count);
    count = count + 1;
}
```

If you wanted to include 5, use `count <= 5` instead of `count < 5`.

---

## Understanding Do-While Loops

### What Is a Do-While Loop?

A **do-while loop** is similar to a while loop, but it checks the condition AFTER each iteration. This guarantees the code runs at least once before checking, which is why it is called a "post-test loop."

### Why Do We Need Do-While Loops?

Use do-while when:
- You need the code to run at least once, no matter what
- The condition depends on something that happens inside the loop
- You want to "do something, then ask if we should do it again"

Real examples:
- Display a menu, then ask if the user wants to continue
- Roll a die, then check if we should roll again
- Process one input, then ask "Process another?"

### How Do-While Loops Work

The structure is:

```
do {
    // code to repeat (runs at least once!)
} while (condition);  // Note the semicolon!
```

**The flow:**
1. Execute the code inside the braces (no condition check yet!)
2. Check the condition
3. If true, go back to step 1
4. If false, exit the loop

**Key difference from while:** The code ALWAYS runs at least once, even if the condition is false.

### Seeing Do-While in Action

```java
import java.util.Scanner;

public class MenuExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String choice;

        do {
            // This menu displays at least once, guaranteed
            System.out.println("\n=== Menu ===");
            System.out.println("1. Play Game");
            System.out.println("2. View Score");
            System.out.println("3. Exit");
            System.out.print("Enter choice: ");

            choice = scanner.nextLine();

            switch (choice) {
                case "1" -> System.out.println("Starting game...");
                case "2" -> System.out.println("Your score: 100");
                case "3" -> System.out.println("Goodbye!");
                default -> System.out.println("Invalid choice!");
            }

        } while (!choice.equals("3"));  // Keep going until user chooses exit
    }
}
```

**Why do-while is perfect here:**
- We MUST show the menu at least once - there is no point in checking before
- The condition (`!choice.equals("3")`) depends on what the user entered
- We check AFTER the user makes a choice

### Comparing While vs Do-While

```java
// These behave DIFFERENTLY when the condition starts false

int x = 10;

// While loop - checks FIRST
while (x < 5) {
    System.out.println("While: " + x);
    x++;
}
// Nothing prints! 10 < 5 is false from the start

// Do-While loop - executes FIRST
x = 10;  // Reset x
do {
    System.out.println("Do-While: " + x);
    x++;
} while (x < 5);
// Prints "Do-While: 10" once, then checks 11 < 5 (false), exits
```

**Output:**
```
Do-While: 10
```

The while loop printed nothing because it checked first. The do-while printed once because it executed first.

### When to Choose Do-While Over While

**Use do-while when you can say:** "Do this at least once, then repeat while condition is true."

**Use while when you can say:** "While condition is true, keep doing this (but maybe not at all)."

Common do-while scenarios:
- Menu systems (show menu at least once)
- "Do you want to play again?" games
- Rolling dice (must roll at least once to have a result to check)
- Input that should be processed at least once before validation

### Common Mistakes with Do-While

**Mistake 1: Forgetting the semicolon after the condition**

```java
do {
    System.out.println("Hello");
} while (count < 5)  // COMPILER ERROR! Missing semicolon!
```

**Fix:**
```java
do {
    System.out.println("Hello");
} while (count < 5);  // Semicolon required!
```

**Mistake 2: Using do-while when while would be clearer**

```java
// Awkward - do-while is not the right choice here
int count = 0;
do {
    System.out.println(count);
    count++;
} while (count < 5);

// Clearer - this is a counting problem, while (or for) is more natural
int count = 0;
while (count < 5) {
    System.out.println(count);
    count++;
}
```

---

## Understanding For Loops

### What Is a For Loop?

A **for loop** is a compact loop structure that puts initialization, condition, and update all in one line. It is called a "counter-controlled loop" because it is ideal for counting a specific number of times.

### Why Do We Need For Loops?

Use for loops when:
- You know exactly how many times to repeat
- You are counting up or down
- You need a counter variable for indexing

Real examples:
- Print numbers 1 through 10
- Repeat an action exactly 5 times
- Count down from 10 to 1
- Iterate through elements by index (when you learn arrays)

### How For Loops Work

The structure is:

```
for (initialization; condition; update) {
    // code to repeat
}
```

The three parts:
1. **Initialization:** Runs once before the loop starts (e.g., `int i = 0`)
2. **Condition:** Checked before each iteration (e.g., `i < 10`)
3. **Update:** Runs after each iteration (e.g., `i++`)

**The flow:**
1. Execute initialization (once only)
2. Check condition
3. If true, execute the loop body
4. Execute update
5. Go back to step 2
6. If condition is false, exit loop

### Seeing For Loops in Action

```java
// Count from 1 to 5
for (int i = 1; i <= 5; i++) {
    System.out.println("Count: " + i);
}

// Output:
// Count: 1
// Count: 2
// Count: 3
// Count: 4
// Count: 5
```

**Trace table for this loop:**

| Step | i value | Is i <= 5? | Action |
|------|---------|------------|--------|
| Start | 1 | - | Initialization |
| 1 | 1 | true | Print "Count: 1", then i++ makes i = 2 |
| 2 | 2 | true | Print "Count: 2", then i++ makes i = 3 |
| 3 | 3 | true | Print "Count: 3", then i++ makes i = 4 |
| 4 | 4 | true | Print "Count: 4", then i++ makes i = 5 |
| 5 | 5 | true | Print "Count: 5", then i++ makes i = 6 |
| 6 | 6 | false | Exit loop |

### A For Loop Is Just a Compact While Loop

These two loops do exactly the same thing:

```java
// Using for
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

// Equivalent while loop
int i = 0;              // Initialization
while (i < 5) {         // Condition
    System.out.println(i);
    i++;                // Update
}
```

The for loop puts all three parts (initialization, condition, update) in one place, making it harder to forget any of them.

### Counting Variations

```java
// Counting UP from 0 to 4 (5 iterations)
for (int i = 0; i < 5; i++) {
    System.out.println(i);  // 0, 1, 2, 3, 4
}

// Counting UP from 1 to 5 (5 iterations)
for (int i = 1; i <= 5; i++) {
    System.out.println(i);  // 1, 2, 3, 4, 5
}

// Counting DOWN from 5 to 1
for (int i = 5; i >= 1; i--) {
    System.out.println(i);  // 5, 4, 3, 2, 1
}

// Counting by 2s (even numbers from 0 to 10)
for (int i = 0; i <= 10; i += 2) {
    System.out.println(i);  // 0, 2, 4, 6, 8, 10
}

// Counting by 3s backwards from 12 to 3
for (int i = 12; i >= 3; i -= 3) {
    System.out.println(i);  // 12, 9, 6, 3
}
```

### The Common "0 to n-1" Pattern

In programming, we often count from 0 to n-1 instead of 1 to n. This will become especially important when you learn arrays next week. Get comfortable with this pattern:

```java
int numberOfStudents = 5;

// This loops 5 times with i = 0, 1, 2, 3, 4
for (int i = 0; i < numberOfStudents; i++) {
    System.out.println("Processing student #" + (i + 1));
}
```

**Why start at 0?** Arrays (which you will learn next) are zero-indexed. The first element is at position 0, not position 1. Starting loops at 0 prepares you for this.

### Common Mistakes with For Loops

**Mistake 1: Off-by-one errors**

```java
// Prints 0 to 9 (10 numbers), not 1 to 10!
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}

// To print 1 to 10:
for (int i = 1; i <= 10; i++) {  // Start at 1, use <=
    System.out.println(i);
}

// Or keep 0-based and add 1 when displaying:
for (int i = 0; i < 10; i++) {
    System.out.println(i + 1);  // Prints 1 to 10
}
```

**Mistake 2: Modifying the loop variable inside the loop**

```java
for (int i = 0; i < 10; i++) {
    System.out.println(i);
    i = i + 1;  // DANGEROUS! Now i increases by 2 each iteration
}
// Prints 0, 2, 4, 6, 8 - only 5 numbers!
```

Let the update part of the for loop handle the counter changes.

**Mistake 3: Using wrong comparison operator**

```java
// This runs 11 times (0 through 10), not 10!
for (int i = 0; i <= 10; i++) {
    System.out.println(i);
}

// For exactly 10 iterations starting at 0, use i < 10
for (int i = 0; i < 10; i++) {
    System.out.println(i);  // 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
}
```

**Tip:** If you want exactly N iterations starting from 0, use `i < N`, not `i <= N`.

---

## Understanding Break and Continue

### What Are Break and Continue?

**break** and **continue** are statements that alter the normal flow of a loop:
- **break**: Immediately exits the loop entirely
- **continue**: Skips the rest of the current iteration and jumps to the next one

### A Word of Caution

These statements can make code harder to understand if overused. They are tools for specific situations, not replacements for good loop design.

**Good uses of break:**
- Exit a search loop when you find what you are looking for
- Exit when an error condition is detected
- Exit a menu loop when user chooses "quit"

**Good uses of continue:**
- Skip invalid data in a processing loop
- Skip certain iterations based on a condition

### How Break Works

```java
// Searching for a specific number
for (int i = 1; i <= 100; i++) {
    if (i == 42) {
        System.out.println("Found it at position " + i);
        break;  // No need to continue searching
    }
}
System.out.println("Search complete");

// Output:
// Found it at position 42
// Search complete
```

Without break, the loop would continue checking all 100 numbers even though we already found what we wanted.

### How Continue Works

```java
// Print only odd numbers from 1 to 10
for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0) {
        continue;  // Skip even numbers
    }
    System.out.println(i);  // Only reached for odd numbers
}

// Output:
// 1
// 3
// 5
// 7
// 9
```

When continue executes, it skips the rest of the current iteration (the println) and goes directly to the next iteration.

### Real-World Example: Input Validation with Break

```java
import java.util.Scanner;

public class PasswordAttempts {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String correctPassword = "secret123";
        int maxAttempts = 3;

        for (int attempt = 1; attempt <= maxAttempts; attempt++) {
            System.out.print("Attempt " + attempt + " - Enter password: ");
            String input = scanner.nextLine();

            if (input.equals(correctPassword)) {
                System.out.println("Access granted!");
                break;  // Exit the loop early - no more attempts needed
            }

            if (attempt < maxAttempts) {
                System.out.println("Wrong password. Try again.");
            } else {
                System.out.println("Too many failed attempts. Account locked.");
            }
        }
    }
}
```

### Common Mistakes with Break and Continue

**Mistake 1: Overusing break instead of fixing the loop condition**

```java
// Bad - using break as a crutch
int i = 0;
while (true) {  // Infinite loop!
    if (i >= 10) {
        break;  // Relying on break to exit
    }
    System.out.println(i);
    i++;
}

// Better - proper loop condition
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}
```

**Mistake 2: Continue that makes the code harder to read**

```java
// Confusing - multiple continues
for (int i = 0; i < 100; i++) {
    if (condition1) continue;
    if (condition2) continue;
    if (condition3) continue;
    // What conditions lead to this code?
    doSomething();
}

// Clearer - use positive logic
for (int i = 0; i < 100; i++) {
    if (!condition1 && !condition2 && !condition3) {
        doSomething();
    }
}
```

---

## Understanding Nested Loops

### What Are Nested Loops?

**Nested loops** are loops inside other loops. The inner loop completes all its iterations for each single iteration of the outer loop.

### Why Do We Need Nested Loops?

Use nested loops for:
- Working with grids or tables (rows and columns)
- Generating combinations or pairs
- Pattern printing
- Comparing all pairs of items

### How Nested Loops Work

Think of it like a clock: the minute hand (inner loop) goes around 60 times for each movement of the hour hand (outer loop).

```java
// Printing a multiplication table (rows 1-3, columns 1-4)
for (int row = 1; row <= 3; row++) {
    for (int col = 1; col <= 4; col++) {
        System.out.print(row * col + "\t");  // \t is a tab character
    }
    System.out.println();  // New line after each row
}

// Output:
// 1    2    3    4
// 2    4    6    8
// 3    6    9    12
```

**Trace through this:**

| Outer (row) | Inner (col) | Print |
|-------------|-------------|-------|
| 1 | 1 | 1 |
| 1 | 2 | 2 |
| 1 | 3 | 3 |
| 1 | 4 | 4 |
| 1 | - | newline |
| 2 | 1 | 2 |
| 2 | 2 | 4 |
| 2 | 3 | 6 |
| 2 | 4 | 8 |
| 2 | - | newline |
| 3 | 1 | 3 |
| 3 | 2 | 6 |
| 3 | 3 | 9 |
| 3 | 4 | 12 |
| 3 | - | newline |

### Pattern Example: Printing a Triangle

```java
// Print a right triangle of stars
int rows = 5;

for (int i = 1; i <= rows; i++) {
    for (int j = 1; j <= i; j++) {
        System.out.print("*");
    }
    System.out.println();  // Move to next line
}

// Output:
// *
// **
// ***
// ****
// *****
```

Notice how the inner loop's limit (`j <= i`) depends on the outer loop's variable. This creates the growing pattern.

### Counting Total Iterations

If the outer loop runs M times and the inner loop runs N times, the inner code executes M x N times total.

```java
// Outer: 5 iterations, Inner: 3 iterations
// Total: 5 x 3 = 15 executions of the print statement
for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 3; j++) {
        System.out.println("i=" + i + ", j=" + j);
    }
}
```

### Common Mistakes with Nested Loops

**Mistake 1: Using the same variable name for both loops**

```java
// ERROR! Cannot have two variables named 'i' in the same scope
for (int i = 0; i < 5; i++) {
    for (int i = 0; i < 3; i++) {  // COMPILER ERROR!
        System.out.println(i);
    }
}

// Fix: Use different names (i, j, k or row, col or outer, inner)
for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 3; j++) {
        System.out.println("i=" + i + ", j=" + j);
    }
}
```

**Mistake 2: Confusing which variable to use**

When accessing the outer loop's variable from inside the inner loop, make sure you use the right one!

```java
for (int row = 1; row <= 3; row++) {
    for (int col = 1; col <= 4; col++) {
        // Make sure you use 'row' and 'col' correctly
        System.out.print(row + "," + col + "  ");
    }
    System.out.println();
}
```

---

## Understanding Infinite Loops (And How to Avoid Them)

### What Is an Infinite Loop?

An **infinite loop** is a loop that never terminates because its condition never becomes false. The program gets stuck running forever (or until you force-quit it).

### Common Causes of Infinite Loops

**Cause 1: Forgetting to update the loop variable**

```java
int i = 0;
while (i < 10) {
    System.out.println(i);
    // i never changes! Always 0, always < 10, loops forever
}
```

**Cause 2: Updating in the wrong direction**

```java
int i = 0;
while (i < 10) {
    System.out.println(i);
    i--;  // Going DOWN when we need to go UP toward 10
}
```

**Cause 3: Condition can never be false**

```java
int x = 5;
while (x != 10) {
    x = x + 3;  // x becomes 5, 8, 11, 14... it will NEVER equal exactly 10!
}
```

**Cause 4: Semicolon after while condition**

```java
int i = 0;
while (i < 5);  // This semicolon makes an empty loop body!
{
    System.out.println(i);  // This is NOT part of the loop
    i++;
}
// The while loop just checks (0 < 5) over and over, doing nothing
```

### How to Stop an Infinite Loop

When your program seems frozen:
- In IntelliJ/Eclipse: Click the red stop button
- In terminal: Press Ctrl+C (or Cmd+C on Mac)

### Prevention Strategies

1. **Always identify what will make the condition false** before writing the loop
2. **Trace through your loop** with a trace table for the first few iterations
3. **Add debug output** temporarily: `System.out.println("Loop iteration: " + i);`
4. **Check your condition logic** - will it ever become false?
5. **Verify the update goes in the right direction** toward making the condition false

### Intentional Infinite Loops

Sometimes infinite loops are intentional, with break statements to exit:

```java
// Game loop - runs until player quits
while (true) {
    displayGame();
    String input = getPlayerInput();

    if (input.equals("quit")) {
        break;  // Exit the infinite loop
    }

    processInput(input);
    updateGame();
}
```

This pattern is common in games and servers. The loop runs "forever" until a specific exit condition is met.

---

## Choosing the Right Loop Type

### Decision Guide

Ask yourself these questions:

**Question 1: Do you know how many times to repeat?**
- YES, exactly N times -> **Use for loop**
- NO, it depends on a condition -> Continue to question 2

**Question 2: Must the code run at least once?**
- YES, always at least once -> **Use do-while**
- NO, might not run at all -> **Use while**

### Summary Table

| Situation | Best Loop | Why |
|-----------|-----------|-----|
| Print numbers 1 to 100 | for | Known count |
| Ask for input until valid | while | May already be valid |
| Show menu, repeat until quit | do-while | Must show menu once |
| Process file until end | while | File might be empty |
| Repeat action exactly 5 times | for | Known count |
| Game runs until player dies | while | Might die immediately |
| Dice game: roll until you roll 6 | do-while | Must roll at least once |

### Conversion Examples

Any loop type can be converted to another (though one may be cleaner):

```java
// FOR LOOP: Print 1 to 5
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}

// WHILE equivalent:
int i = 1;
while (i <= 5) {
    System.out.println(i);
    i++;
}

// DO-WHILE equivalent (less natural for counting):
int i = 1;
do {
    System.out.println(i);
    i++;
} while (i <= 5);
```

Choose the loop that makes your intent clearest to someone reading the code.

---

## Common Loop Patterns

### Pattern 1: Counting/Accumulating

Add up all numbers, keep a running total:

```java
// Sum of numbers 1 to 100
int sum = 0;
for (int i = 1; i <= 100; i++) {
    sum = sum + i;  // Or: sum += i;
}
System.out.println("Sum: " + sum);  // Sum: 5050
```

### Pattern 2: Finding Maximum/Minimum

Track the largest or smallest value seen:

```java
import java.util.Scanner;

// Find the largest of 5 numbers entered by user
Scanner scanner = new Scanner(System.in);
int max = Integer.MIN_VALUE;  // Start with smallest possible int

for (int i = 1; i <= 5; i++) {
    System.out.print("Enter number " + i + ": ");
    int num = scanner.nextInt();

    if (num > max) {
        max = num;  // Found a new maximum
    }
}
System.out.println("Largest number: " + max);
```

### Pattern 3: Counting Occurrences

Count how many times something happens:

```java
// Count how many numbers between 1-100 are divisible by 7
int count = 0;
for (int i = 1; i <= 100; i++) {
    if (i % 7 == 0) {
        count++;
    }
}
System.out.println("Count of multiples of 7: " + count);  // 14
```

### Pattern 4: Searching

Look for a specific value:

```java
// Check if user entered a specific number in 5 guesses
Scanner scanner = new Scanner(System.in);
int target = 42;
boolean found = false;

for (int attempt = 1; attempt <= 5; attempt++) {
    System.out.print("Guess #" + attempt + ": ");
    int guess = scanner.nextInt();

    if (guess == target) {
        System.out.println("Correct!");
        found = true;
        break;  // Exit early - no need to continue
    }
}

if (!found) {
    System.out.println("Sorry, you did not guess it. The answer was " + target);
}
```

### Pattern 5: Input Validation

Keep asking until valid input is received:

```java
Scanner scanner = new Scanner(System.in);
int choice;

do {
    System.out.print("Enter a number between 1 and 10: ");

    // Check if input is actually an integer
    while (!scanner.hasNextInt()) {
        System.out.println("That is not a valid number. Try again.");
        scanner.next();  // Discard the invalid input
        System.out.print("Enter a number between 1 and 10: ");
    }

    choice = scanner.nextInt();

    if (choice < 1 || choice > 10) {
        System.out.println("Number must be between 1 and 10.");
    }

} while (choice < 1 || choice > 10);

System.out.println("You entered: " + choice);
```

---

## Connecting to What You Already Know

### Loops Use Conditions From Week 2

The condition in every loop is exactly like the condition in an if statement:

```java
// Week 2: If statement - checks condition ONCE
if (temperature > 30) {
    System.out.println("It is hot!");
}

// Week 3: While loop - checks condition REPEATEDLY
while (temperature > 30) {
    System.out.println("Still hot... opening windows");
    temperature = temperature - 2;  // Room cools down
}
```

All the relational operators (`<`, `>`, `<=`, `>=`, `==`, `!=`) and logical operators (`&&`, `||`, `!`) you learned work exactly the same way in loop conditions.

### Boolean Variables Control Loops

Just like with if statements, boolean variables can control loops:

```java
// Using a boolean to control the loop
boolean gameOver = false;

while (!gameOver) {
    // Game logic here
    int playerHealth = getPlayerHealth();

    if (playerHealth <= 0) {
        gameOver = true;  // This will end the loop
    }
}
```

### Short-Circuit Evaluation Still Applies

Remember from Week 2 that `&&` stops if the first condition is false, and `||` stops if the first condition is true:

```java
// This is safe! If str is null, the second part is not evaluated
while (str != null && str.length() > 0) {
    // Process string
}
```

---

## Common Struggles and How to Overcome Them

### Struggle 1: Choosing Between while, do-while, and for

**The confusion:** "I never know which loop to use!"

**The solution:** Ask two questions:
1. Do I know exactly how many times? -> **for**
2. Must it run at least once? -> **do-while**
3. Otherwise -> **while**

**Memory trick:**
- **for** = **for** a known number of times
- **while** = **while** something is true (might be never)
- **do-while** = **do** at least once, **while** still true

### Struggle 2: Off-By-One Errors

**The confusion:** "My loop runs one too many or one too few times!"

**The solution:** Be explicit about what you want:

```java
// Want iterations: 0, 1, 2, 3, 4 (5 total)
// Use: i < 5 (less than count)
for (int i = 0; i < 5; i++) { }

// Want iterations: 1, 2, 3, 4, 5 (5 total)
// Use: i <= 5 (less than or equal to last value)
for (int i = 1; i <= 5; i++) { }
```

**Test strategy:** Always test with small numbers. If your loop should run 100 times, first test with 3 or 5 times and manually verify.

### Struggle 3: Infinite Loops

**The confusion:** "My program freezes and I do not know why!"

**The solution:** Before writing the loop, answer these questions:
1. What is my starting value?
2. What condition makes the loop stop?
3. What changes to eventually make that condition false?

Add debug output if stuck:
```java
while (condition) {
    System.out.println("DEBUG: i = " + i);  // See what is happening
    // ... rest of loop
}
```

### Struggle 4: Understanding When Loops Terminate

**The confusion:** "I cannot predict when my loop will end!"

**The solution:** Use trace tables! Write down:
- The value of each variable at the start of each iteration
- Whether the condition is true or false
- What changes after each iteration

Even just 3-4 rows of a trace table often reveals the pattern.

### Struggle 5: Nested Loop Logic Complexity

**The confusion:** "Nested loops make my head spin!"

**The solution:** Think in layers:
1. Pretend the inner loop is just one action called "doInnerThing()"
2. Understand the outer loop first
3. Then zoom in to understand what "doInnerThing()" really does

Also, use meaningful variable names:
```java
// Confusing
for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 3; j++) { }
}

// Clearer
for (int row = 0; row < 5; row++) {
    for (int col = 0; col < 3; col++) { }
}
```

---

## Practice Exercises

### Exercise 1: Countdown Timer (meget hjalp - Maximum Guidance)

**Goal:** Practice basic while loops and loop termination.

**Step-by-step instructions:**

1. Create a new Java file called `CountdownTimer.java`
2. Create an `int` variable called `seconds` and set it to 10
3. Write a while loop that continues while `seconds` is greater than 0
4. Inside the loop:
   - Print the current value of `seconds`
   - Decrease `seconds` by 1
5. After the loop ends, print "Liftoff!"

**Expected output:**
```
10
9
8
7
6
5
4
3
2
1
Liftoff!
```

**Hints:**
- Start with `int seconds = 10;`
- The condition is `seconds > 0`
- Use `seconds = seconds - 1;` or `seconds--;` to decrease

**Challenge extension:** Add a one-second pause between each number using `Thread.sleep(1000);` (you will need to add `throws InterruptedException` to your main method).

### Exercise 2: Sum Calculator (meget hjalp - Maximum Guidance)

**Goal:** Practice the accumulator pattern with a for loop.

**Step-by-step instructions:**

1. Create a program that calculates the sum of numbers from 1 to N
2. Ask the user to enter a positive integer N using Scanner
3. Use a for loop to add up all numbers from 1 to N
4. Display the result

**Expected output:**
```
Enter a positive integer: 5
The sum of numbers from 1 to 5 is: 15
```

**Hints:**
- Create `int sum = 0;` before the loop
- Inside the loop: `sum = sum + i;`
- The sum of 1+2+3+4+5 = 15

### Exercise 3: Number Guessing Game (nogen hjalp - Moderate Guidance)

**Goal:** Practice do-while loops and input validation.

**Instructions:**

1. Create a number guessing game where:
   - The computer picks a random number between 1 and 100
   - The player guesses until they get it right
   - After each guess, tell them if they need to go higher or lower
   - Count the number of attempts

2. Use a do-while loop (the player must guess at least once)

3. To generate a random number: `int target = (int)(Math.random() * 100) + 1;`

**What you will need:**
- Scanner for input
- do-while loop (player guesses at least once)
- if-else for "higher" or "lower" feedback
- A counter variable for attempts

**Expected behavior:**
```
I am thinking of a number between 1 and 100.
Your guess: 50
Too low! Try again.
Your guess: 75
Too high! Try again.
Your guess: 62
Correct! You got it in 3 attempts!
```

### Exercise 4: Multiplication Table (nogen hjalp - Moderate Guidance)

**Goal:** Practice nested loops.

**Instructions:**

1. Create a program that prints a multiplication table
2. Ask the user for the table size (e.g., 5 for a 5x5 table)
3. Use nested for loops to generate the table
4. Format the output nicely using tabs (`\t`)

**Expected output for size 5:**
```
1	2	3	4	5
2	4	6	8	10
3	6	9	12	15
4	8	12	16	20
5	10	15	20	25
```

**Hints:**
- Outer loop controls rows
- Inner loop controls columns
- Print value with `System.out.print(row * col + "\t");`
- After each row, use `System.out.println();` for a new line

### Exercise 5: Finding Min and Max (ingen hjalp - Minimal Guidance)

**Goal:** Apply loop patterns to find minimum and maximum values.

**Requirements:**
- Ask the user how many numbers they want to enter
- Read that many numbers from the user
- Keep track of the smallest and largest numbers entered
- At the end, display both the minimum and maximum

**Sample run:**
```
How many numbers? 5
Enter number 1: 42
Enter number 2: 17
Enter number 3: 89
Enter number 4: 3
Enter number 5: 56
Minimum: 3
Maximum: 89
```

**Note:** Think about what initial values to use for min and max. You might start with the first number entered, or use `Integer.MAX_VALUE` and `Integer.MIN_VALUE`.

### Exercise 6: Input Validation Loop (ingen hjalp - Minimal Guidance)

**Goal:** Create a robust input validation system.

**Requirements:**
- Create a program that asks for a test score (0-100)
- If the input is not a valid integer, display an error and ask again
- If the input is out of range (less than 0 or greater than 100), display an error and ask again
- Only accept the input when it is both a valid integer and in the correct range
- Display the letter grade based on the validated score

**Challenge:** Use `scanner.hasNextInt()` to check if the next input is an integer before reading it with `scanner.nextInt()`.

---

## Looking Ahead

This week you learned how to make your programs repeat tasks automatically. These skills are essential for everything that follows:

- **Week 4 (Methods):** Methods often contain loops. You will create methods like `printStars(int count)` that use loops internally. You will also learn to use loops to call methods repeatedly.

- **Week 5 (Methods Part 2):** More complex methods will combine loops with the decision-making skills from Week 2.

- **Week 6 (Arrays):** This is where loops become truly powerful. Arrays store multiple values, and loops let you process every element. Without loops, arrays would be nearly useless!

- **Week 7+ (OOP):** You will loop through collections of objects, processing each Student in a class list or each Item in an inventory.

- **Week 11 (File Handling):** Reading files is fundamentally a loop: "while there are more lines to read, process the next line."

Every program that works with collections, files, or user interaction uses loops. The patterns you learned this week - counting, accumulating, searching, validating - will appear in every project you build.

---

## Key Takeaways

- **while loops** check the condition BEFORE each iteration - they might run zero times
- **do-while loops** check the condition AFTER each iteration - they always run at least once
- **for loops** are ideal for counting - they put initialization, condition, and update in one place
- **break** exits a loop immediately; **continue** skips to the next iteration
- **Nested loops** are loops inside loops - the inner loop completes fully for each outer iteration
- **Infinite loops** happen when the condition never becomes false - always plan your exit condition
- **Off-by-one errors** are extremely common - carefully consider `<` vs `<=` and your starting value
- **Trace tables** help you understand exactly what happens in each iteration
- Loop conditions use the same operators you learned in Week 2 (`<`, `>`, `==`, `&&`, `||`, etc.)
- Common patterns: counting, accumulating, finding min/max, searching, validating input

---

## For the Next Topic Agent

### Terminology Established This Week

- **loop**: A control structure that repeats code multiple times
- **iteration**: One execution of the loop body; "the loop ran for 5 iterations"
- **while loop**: A pre-test loop that checks the condition before each iteration
- **do-while loop**: A post-test loop that executes once before checking the condition
- **for loop**: A counter-controlled loop with initialization, condition, and update in one line
- **loop body**: The code inside the loop that gets repeated
- **loop variable / counter**: A variable that tracks progress through the loop (often `i`, `j`, or `count`)
- **infinite loop**: A loop that never terminates because the condition is always true
- **off-by-one error**: A common bug where a loop runs one too many or one too few times
- **break**: A statement that immediately exits the enclosing loop
- **continue**: A statement that skips the rest of the current iteration
- **nested loops**: Loops placed inside other loops
- **trace table**: A debugging tool that tracks variable values through each iteration
- **accumulator pattern**: Keeping a running total by adding to a variable each iteration
- **sentinel value**: A special value that signals when to stop a loop
- **input validation**: Using loops to ensure user input meets requirements
- **pre-test vs post-test**: Whether the condition is checked before or after the loop body

### Example Classes/Concepts Created

- Countdown timer with while loop
- Number guessing game with do-while
- Multiplication table with nested for loops
- Sum calculator with accumulator pattern
- Min/max finder with comparison in loop
- Input validation with hasNextInt()
- Password attempt limiter with break
- Pattern printing with nested loops

### Student Capabilities After This Week

Students can now:
- Write while loops for condition-controlled repetition
- Write do-while loops when code must execute at least once
- Write for loops for counting and known iterations
- Use break to exit loops early and continue to skip iterations
- Create nested loops for grid/table problems
- Debug infinite loops and off-by-one errors using trace tables
- Validate user input using loops
- Apply common patterns: counting, accumulating, searching, min/max
- Choose the appropriate loop type for each situation
- Convert between loop types when needed

### Pedagogical Patterns Continued

- **Analogy-first approach**: Brushing teeth, checking phone, countdown for race
- **Trace tables**: Step-by-step execution tables for understanding loops
- **Common mistakes sections**: Infinite loops, off-by-one errors, wrong condition
- **Progressive exercise difficulty**: meget hjalp -> nogen hjalp -> ingen hjalp structure
- **Connecting to prior week**: Explicit links to Week 2 conditions in loop conditions
- **Why before how**: Each loop type motivated before syntax
- **Decision guide**: Clear questions to help choose between loop types
- **Small code examples**: Most under 15 lines, heavily annotated
- **Real-world examples**: Password validation, menu systems, games

### Critical Connections for Week 4 (Methods)

- Loops are commonly placed inside methods
- Methods can be called from within loops
- The counting pattern prepares for array iteration
- Input validation patterns will be encapsulated in methods
- The accumulator pattern becomes `sum(int n)` type methods
