# Unit Testing and Code Coverage - Week 13

*Prerequisites: Week 12 (Exception Handling), Weeks 4-5 (Methods), Weeks 7-10 (Complete OOP Foundation)*
*Phase: Phase 4: Practical Software Development (Final Week)*

---

## What You'll Learn

By the end of this week, you will be able to:

- **Understand what unit testing is** and why professional developers rely on it
- **Write basic unit tests** using the JUnit 5 framework
- **Use the @Test annotation** to mark methods as tests
- **Apply assertion methods** (assertEquals, assertTrue, assertFalse, assertNull, assertNotNull, assertThrows)
- **Follow test naming conventions** that make tests self-documenting
- **Test exception handling** - verify that your code throws the right exceptions
- **Use @BeforeEach and @AfterEach** for test setup and cleanup
- **Understand code coverage** - what percentage of your code is actually tested?
- **Grasp Test-Driven Development (TDD)** principles at a conceptual level
- **Recognize what makes a good test** vs. a test that provides false confidence

**IMPORTANT NOTE**: Unit testing and JUnit are NOT part of your final exam. However, this is one of the most valuable professional skills you will learn this semester. Every professional Java developer writes tests!

**CONNECTION TO WEEKS 4-5**: Remember when you learned about methods? A "unit" in unit testing IS a method! Testing is about verifying that individual methods work correctly.

**CONNECTION TO WEEK 12**: Last week you created custom exceptions. This week you will learn how to TEST that your code throws exceptions when it should!

---

## Why This Matters

### The Professional Reality

Walk into any professional software company, and you will find developers writing tests. Not because they are told to, but because tests make their lives EASIER.

Consider this scenario:

```
Monday: You write code for a shopping cart
Tuesday: You add a discount feature
Wednesday: Discount feature accidentally breaks the shopping cart
Thursday: Customer reports bug
Friday: You spend the entire day hunting for what went wrong
```

Now with tests:

```
Monday: You write code for a shopping cart (and tests)
Tuesday: You add a discount feature
Tuesday (5 minutes later): Tests fail, showing exactly what you broke
Tuesday (10 minutes later): Bug fixed, tests pass
```

**Tests do not slow you down. Tests make you FASTER.**

### The Confidence Factor

Without tests, making changes to code feels scary:

- "What if I break something?"
- "Does this still work?"
- "I better not touch that old code..."

With tests, you have confidence:

- "If my tests pass, my code works"
- "I can refactor fearlessly"
- "The tests will tell me if I break something"

### The Cost of Change

Software engineering pioneer Kent Beck described the "cost of change curve":

```
                           |
Cost to fix                |                    *
a bug                      |                 *
                           |              *
                           |           *
                           |        *
                           |     *
                           |  *
                           |*
                           +-------------------------
                            Development  Testing  Production
                            (cheap)      (medium) (EXPENSIVE!)
```

Bugs found during development (when you write the code) cost almost nothing to fix.
Bugs found during testing cost more.
Bugs found in production (by customers) are EXTREMELY expensive.

**Unit tests catch bugs during development - the cheapest time to fix them!**

### Real-World Impact

| Without Tests | With Tests |
|---------------|------------|
| Fear of changing code | Confidence to refactor |
| Bugs found by customers | Bugs found immediately |
| "It works on my machine" | Automated verification |
| Manual testing every time | Automated testing in seconds |
| No documentation of behavior | Tests document expected behavior |

### This Is Industry Standard

Every major company practices testing:
- Google requires tests for all code changes
- Amazon runs millions of automated tests daily
- Netflix tests constantly to maintain reliability
- Your future employer will expect you to write tests!

---

## Building Your Intuition

### Analogy 1: Testing as a Safety Net

Remember the trapeze artist from Week 12? The safety net catches them if they fall.

**Unit tests are your safety net for code changes.**

```
Making code changes without tests:
    Walking a tightrope without a net.
    One wrong step = disaster.

Making code changes with tests:
    Walking with a safety net.
    If something goes wrong, the net catches you.
    You can try bold moves with confidence!
```

### Analogy 2: Testing as Recipe Verification

Imagine you are a chef developing a new recipe:

**Without testing:**
- Make the dish
- Serve it to customers
- Hope it tastes good
- Find out when customers complain

**With testing:**
- Make the dish
- Taste it yourself (unit test!)
- Verify each ingredient is correct
- Only serve when you are confident it is right

Each unit test is like tasting a specific component:
- Is the sauce sweet enough? (Does `calculateDiscount()` return the right value?)
- Is the meat cooked through? (Does `validateEmail()` reject invalid emails?)
- Is the presentation correct? (Does `formatDate()` produce the expected string?)

### Analogy 3: Units as Building Blocks

Think of LEGO:

```
A LEGO set = Your complete program
Each LEGO brick = A method (unit)

Before building:
- Test each brick: Does it click properly?
- Test small assemblies: Do these three bricks fit together?
- Only then build the complete model

Unit testing = Testing each brick individually
```

If a brick is defective, you want to know BEFORE you build the castle, not after!

### Analogy 4: Testing as Spell-Check

When you write a document:
- Spell-check catches typos WHILE you type
- You do not wait until the document is printed to check spelling!

Unit tests are spell-check for your code:
- They catch errors WHILE you develop
- You do not wait until users find bugs!

### Analogy 5: The Pilot's Checklist

Before every flight, pilots run through a checklist:
- Fuel? Check
- Flaps? Check
- Instruments? Check
- Communication? Check

They do not skip this because "I've flown 1000 times before."

Unit tests are your code's preflight checklist:
- After every code change, run the tests
- All tests pass? Clear for takeoff!
- Tests fail? Fix before continuing!

---

## Understanding Unit Testing: The Foundation

### What Is a Unit?

A **unit** is the smallest testable piece of code. In Java, this typically means a **method**.

Remember from Weeks 4-5 when you learned about methods? Each method has:
- A clear purpose (what it does)
- Inputs (parameters)
- Outputs (return value or side effects)

This makes methods perfect for testing!

```java
// This method IS a unit
public int add(int a, int b) {
    return a + b;
}

// Testing this unit:
// Input: a=2, b=3
// Expected output: 5
// We test: Does add(2, 3) actually return 5?
```

### What Is Unit Testing?

**Unit testing** is the practice of testing individual units (methods) in isolation to verify they work correctly.

Key characteristics:
- **Isolated**: Test one method at a time
- **Automated**: Tests run automatically, not manually
- **Repeatable**: Same test, same result, every time
- **Fast**: Unit tests run in milliseconds

### Why Not Just Run the Program?

You might think: "Why write tests? I can just run my program and check if it works!"

Consider this program:

```java
public class Calculator {
    public int add(int a, int b) { return a + b; }
    public int subtract(int a, int b) { return a - b; }
    public int multiply(int a, int b) { return a * b; }
    public int divide(int a, int b) { return a / b; }
    public double power(double base, int exp) { /* ... */ }
    public double squareRoot(double n) { /* ... */ }
    // ... 20 more methods
}
```

To "test" this by running:
- You would have to manually try each method
- With multiple inputs each
- And check every output
- Every time you change anything!

With unit tests:
- Write each test once
- Run all tests with one command
- In seconds, know if everything works
- Every change automatically verified!

### The Structure of a Unit Test

Every unit test follows this pattern:

```
1. ARRANGE - Set up what you need
2. ACT     - Call the method you're testing
3. ASSERT  - Verify the result is correct
```

This is often called the **AAA pattern**:

```java
@Test
void testAddition() {
    // ARRANGE - set up test data
    Calculator calc = new Calculator();
    int a = 2;
    int b = 3;

    // ACT - call the method being tested
    int result = calc.add(a, b);

    // ASSERT - verify the result
    assertEquals(5, result);
}
```

---

## Understanding JUnit 5: The Testing Framework

### What Is JUnit?

**JUnit** is the most popular testing framework for Java. It provides:
- Annotations to mark test methods
- Assertion methods to verify results
- Test runners to execute tests
- Reports showing which tests passed or failed

JUnit 5 is the current version (also called "JUnit Jupiter").

### Why Use a Framework?

You could write your own testing code:

```java
// Testing without a framework (messy!)
public class ManualTest {
    public static void main(String[] args) {
        Calculator calc = new Calculator();

        // Test 1
        int result1 = calc.add(2, 3);
        if (result1 == 5) {
            System.out.println("Test 1 passed");
        } else {
            System.out.println("Test 1 FAILED: expected 5, got " + result1);
        }

        // Test 2
        int result2 = calc.subtract(10, 4);
        if (result2 == 6) {
            System.out.println("Test 2 passed");
        } else {
            System.out.println("Test 2 FAILED: expected 6, got " + result2);
        }

        // ... hundreds more tests?
    }
}
```

With JUnit, it becomes elegant:

```java
class CalculatorTest {

    @Test
    void additionReturnsCorrectSum() {
        Calculator calc = new Calculator();
        assertEquals(5, calc.add(2, 3));
    }

    @Test
    void subtractionReturnsCorrectDifference() {
        Calculator calc = new Calculator();
        assertEquals(6, calc.subtract(10, 4));
    }
}
```

JUnit handles:
- Running tests automatically
- Reporting results clearly
- Providing helpful failure messages
- Organizing and managing tests

### Setting Up JUnit 5

In most IDEs (IntelliJ IDEA, Eclipse), JUnit 5 is easy to add:
1. Right-click your project
2. Add JUnit 5 as a dependency
3. Start writing tests!

Your test files typically go in a `test` folder parallel to your `src` folder:

```
project/
    src/
        Calculator.java
        Student.java
    test/
        CalculatorTest.java
        StudentTest.java
```

---

## Understanding the @Test Annotation

### What Is @Test?

The `@Test` annotation marks a method as a test method. When you run your tests, JUnit finds all methods with `@Test` and executes them.

```java
import org.junit.jupiter.api.Test;

class MyTests {

    @Test  // This annotation tells JUnit "this is a test!"
    void myFirstTest() {
        // test code here
    }
}
```

### Why Annotations?

Annotations are a Java feature that adds metadata to code. Instead of implementing a special interface or extending a class, you simply annotate your methods.

```java
// WITHOUT annotations (old style) - more complex
class MyTest extends TestCase {
    public void testSomething() {
        // ...
    }
}

// WITH annotations (modern JUnit 5) - clean and simple
class MyTest {
    @Test
    void testSomething() {
        // ...
    }
}
```

### Test Method Requirements

Test methods must:
- Be annotated with `@Test`
- Have `void` return type
- Take no parameters
- Not be private (package-private, protected, or public)

```java
@Test
void validTest() {
    // This is a valid test method
}

@Test
private void invalidTest() {
    // WRONG! Cannot be private
}

@Test
int alsoInvalid() {
    // WRONG! Must return void
    return 5;
}
```

### Multiple Tests in One Class

You can (and should) have many tests in one class:

```java
class CalculatorTest {

    @Test
    void testAddPositiveNumbers() {
        Calculator calc = new Calculator();
        assertEquals(5, calc.add(2, 3));
    }

    @Test
    void testAddNegativeNumbers() {
        Calculator calc = new Calculator();
        assertEquals(-5, calc.add(-2, -3));
    }

    @Test
    void testAddZero() {
        Calculator calc = new Calculator();
        assertEquals(7, calc.add(7, 0));
    }

    @Test
    void testSubtract() {
        Calculator calc = new Calculator();
        assertEquals(4, calc.subtract(10, 6));
    }
}
```

---

## Understanding Assertions

### What Are Assertions?

**Assertions** are statements that verify expected results. If an assertion fails, the test fails.

Think of assertions as questions:
- "Is this value what I expected?" (assertEquals)
- "Is this condition true?" (assertTrue)
- "Is this condition false?" (assertFalse)
- "Is this value null?" (assertNull)
- "Is this value NOT null?" (assertNotNull)

### The Core Assertions

**assertEquals** - Are two values equal?

```java
@Test
void testEquality() {
    int result = calculator.add(2, 3);
    assertEquals(5, result);  // Expected 5, is result 5?

    // With descriptive message (shown if test fails)
    assertEquals(5, result, "2 + 3 should equal 5");
}
```

**assertTrue** - Is the condition true?

```java
@Test
void testConditionTrue() {
    int result = calculator.add(2, 3);
    assertTrue(result > 0);  // Is result positive?
    assertTrue(result == 5, "Sum should be 5");
}
```

**assertFalse** - Is the condition false?

```java
@Test
void testConditionFalse() {
    List<String> names = new ArrayList<>();
    assertFalse(names.contains("Alice"));  // Alice should NOT be in empty list
}
```

**assertNull** - Is the value null?

```java
@Test
void testNullValue() {
    User user = userManager.findUser("nonexistent");
    assertNull(user);  // User should be null if not found
}
```

**assertNotNull** - Is the value NOT null?

```java
@Test
void testNotNull() {
    User user = userManager.findUser("alice");
    assertNotNull(user);  // User should exist
    assertNotNull(user.getName(), "User name should not be null");
}
```

### Assertion Parameter Order

**Important convention**: In JUnit, the expected value comes FIRST:

```java
assertEquals(expected, actual);
//           ^^^^^^^   ^^^^^^
//           What you  What your
//           expect    code returns

// Example:
assertEquals(5, calculator.add(2, 3));
//           ^  ^^^^^^^^^^^^^^^^^^^^^
//           expected    actual
```

If you get these backwards, your error messages will be confusing!

### When Assertions Fail

When an assertion fails, JUnit reports exactly what went wrong:

```
org.opentest4j.AssertionFailedError:
Expected: 5
Actual:   6
    at CalculatorTest.testAddition(CalculatorTest.java:15)
```

This tells you:
- What was expected (5)
- What you actually got (6)
- Where the failure occurred (line 15)

---

## Understanding Test Naming Conventions

### Why Names Matter

Test names are documentation. A good test name tells you:
- What is being tested
- Under what conditions
- What the expected outcome is

### The methodName_condition_expectedResult Pattern

A popular convention:

```java
@Test
void add_twoPositiveNumbers_returnsSum() {
    assertEquals(5, calculator.add(2, 3));
}

@Test
void add_negativeAndPositive_returnsCorrectSum() {
    assertEquals(2, calculator.add(-3, 5));
}

@Test
void divide_byZero_throwsException() {
    assertThrows(ArithmeticException.class, () -> calculator.divide(10, 0));
}
```

Breaking down: `add_twoPositiveNumbers_returnsSum`
- `add` - the method being tested
- `twoPositiveNumbers` - the test condition
- `returnsSum` - the expected result

### Alternative: Should Pattern

```java
@Test
void shouldReturnSumWhenAddingTwoPositiveNumbers() {
    assertEquals(5, calculator.add(2, 3));
}

@Test
void shouldThrowExceptionWhenDividingByZero() {
    assertThrows(ArithmeticException.class, () -> calculator.divide(10, 0));
}
```

### What Makes a Good Test Name

**Good test names:**
- Describe behavior, not implementation
- Are readable as sentences
- Tell you what failed without reading the code
- Make test reports useful documentation

```java
// BAD - tells you nothing
@Test
void test1() { }

// BAD - too vague
@Test
void testAdd() { }

// GOOD - descriptive and specific
@Test
void add_twoPositiveNumbers_returnsPositiveSum() { }

// GOOD - describes scenario
@Test
void calculateDiscount_forPremiumMember_applies20Percent() { }
```

---

## Understanding Exception Testing

### Why Test Exceptions?

Remember from Week 12? Your code throws exceptions to signal errors. You need to test that:
1. Exceptions ARE thrown when they should be
2. The RIGHT exception type is thrown
3. Exception messages are correct

### Testing with assertThrows

**assertThrows** verifies that code throws a specific exception:

```java
import static org.junit.jupiter.api.Assertions.assertThrows;

@Test
void divide_byZero_throwsArithmeticException() {
    Calculator calc = new Calculator();

    assertThrows(ArithmeticException.class, () -> {
        calc.divide(10, 0);
    });
}
```

The `() -> { }` syntax is a **lambda expression** - think of it as "code to run". We are telling JUnit: "Run this code and expect this exception."

### Connecting to Week 12

Remember the custom exceptions you created in Week 12? Now you can test them!

```java
// From Week 12: InvalidAgeException
public class Person {
    public void setAge(int age) throws InvalidAgeException {
        if (age < 0 || age > 150) {
            throw new InvalidAgeException("Age must be between 0 and 150");
        }
        this.age = age;
    }
}

// Testing that the exception IS thrown
@Test
void setAge_negativeValue_throwsInvalidAgeException() {
    Person person = new Person();

    assertThrows(InvalidAgeException.class, () -> {
        person.setAge(-5);
    });
}

@Test
void setAge_over150_throwsInvalidAgeException() {
    Person person = new Person();

    assertThrows(InvalidAgeException.class, () -> {
        person.setAge(200);
    });
}
```

### Verifying Exception Messages

You can also check the exception message:

```java
@Test
void setAge_negativeValue_throwsExceptionWithCorrectMessage() {
    Person person = new Person();

    InvalidAgeException exception = assertThrows(
        InvalidAgeException.class,
        () -> person.setAge(-5)
    );

    assertTrue(exception.getMessage().contains("between 0 and 150"));
}
```

### Testing That Exceptions Are NOT Thrown

Sometimes you want to verify code does NOT throw:

```java
@Test
void setAge_validValue_doesNotThrow() {
    Person person = new Person();

    // This should NOT throw any exception
    assertDoesNotThrow(() -> {
        person.setAge(25);
    });
}
```

---

## Understanding @BeforeEach and @AfterEach

### The Problem: Repeated Setup

Many tests need the same setup:

```java
@Test
void testAdd() {
    Calculator calc = new Calculator();  // Same setup
    assertEquals(5, calc.add(2, 3));
}

@Test
void testSubtract() {
    Calculator calc = new Calculator();  // Same setup!
    assertEquals(4, calc.subtract(10, 6));
}

@Test
void testMultiply() {
    Calculator calc = new Calculator();  // Same setup again!
    assertEquals(12, calc.multiply(3, 4));
}
```

This is repetitive. What if Calculator needs complex initialization?

### The Solution: @BeforeEach

Code in a `@BeforeEach` method runs before EACH test:

```java
class CalculatorTest {
    private Calculator calc;  // Instance variable shared by tests

    @BeforeEach
    void setUp() {
        // This runs BEFORE each test method
        calc = new Calculator();
        System.out.println("Setting up new calculator");
    }

    @Test
    void testAdd() {
        assertEquals(5, calc.add(2, 3));
    }

    @Test
    void testSubtract() {
        assertEquals(4, calc.subtract(10, 6));
    }

    @Test
    void testMultiply() {
        assertEquals(12, calc.multiply(3, 4));
    }
}
```

### Why Fresh Setup Matters

Each test should be **independent**. They should not affect each other.

```java
class UserManagerTest {
    private UserManager manager;

    @BeforeEach
    void setUp() {
        // FRESH manager for each test
        manager = new UserManager();
    }

    @Test
    void testAddUser() {
        manager.addUser("alice");
        assertEquals(1, manager.getUserCount());
    }

    @Test
    void testAddMultipleUsers() {
        // This test gets a FRESH manager
        // It does not have "alice" from the previous test!
        manager.addUser("bob");
        manager.addUser("charlie");
        assertEquals(2, manager.getUserCount());
    }
}
```

### @AfterEach for Cleanup

Code in `@AfterEach` runs after each test - useful for cleanup:

```java
class FileProcessorTest {
    private File tempFile;

    @BeforeEach
    void setUp() throws IOException {
        tempFile = File.createTempFile("test", ".txt");
    }

    @AfterEach
    void tearDown() {
        // Clean up the temp file after each test
        if (tempFile.exists()) {
            tempFile.delete();
        }
    }

    @Test
    void testWriteToFile() {
        // Test uses tempFile
    }

    @Test
    void testReadFromFile() {
        // Test uses fresh tempFile
    }
}
```

### @BeforeAll and @AfterAll

For expensive setup that should happen once for the entire test class:

```java
class DatabaseTest {

    @BeforeAll
    static void setUpDatabase() {
        // Runs ONCE before any tests
        // Note: must be static!
        connectToDatabase();
    }

    @AfterAll
    static void tearDownDatabase() {
        // Runs ONCE after all tests
        disconnectFromDatabase();
    }

    @BeforeEach
    void resetData() {
        // Runs before EACH test
        clearTestData();
    }
}
```

### Execution Order

```
@BeforeAll (once)
    |
    +-- @BeforeEach
    |       @Test method1
    |   @AfterEach
    |
    +-- @BeforeEach
    |       @Test method2
    |   @AfterEach
    |
    +-- @BeforeEach
            @Test method3
        @AfterEach
    |
@AfterAll (once)
```

---

## Understanding Code Coverage

### What Is Code Coverage?

**Code coverage** measures what percentage of your code is executed by your tests.

```java
public int getGrade(int score) {
    if (score >= 90) {
        return 1;  // A grade
    } else if (score >= 80) {
        return 2;  // B grade
    } else if (score >= 70) {
        return 3;  // C grade
    } else {
        return 4;  // F grade
    }
}
```

If your only test is:

```java
@Test
void testHighScore() {
    assertEquals(1, grader.getGrade(95));  // Only tests first branch!
}
```

Your coverage would be around 25% - you only test the `score >= 90` branch!

To achieve higher coverage:

```java
@Test
void testGradeA() {
    assertEquals(1, grader.getGrade(95));
}

@Test
void testGradeB() {
    assertEquals(2, grader.getGrade(85));
}

@Test
void testGradeC() {
    assertEquals(3, grader.getGrade(75));
}

@Test
void testGradeF() {
    assertEquals(4, grader.getGrade(50));
}
```

Now all branches are covered!

### Types of Coverage

**Line coverage**: What percentage of lines were executed?
**Branch coverage**: What percentage of if/else branches were taken?
**Method coverage**: What percentage of methods were called?

Most tools report all three.

### What Is "Good" Coverage?

A common target is **80% coverage**, but remember:
- 100% coverage does not mean no bugs
- Coverage measures quantity, not quality
- Some code is hard to test (UI, external services)

**High coverage + good tests = confidence**
**High coverage + bad tests = false confidence**

### Coverage Tools

Most IDEs have built-in coverage tools:
- IntelliJ IDEA: Run with Coverage
- Eclipse: EclEmma plugin
- Maven: JaCoCo plugin

These tools highlight which lines are covered (green) and which are not (red).

---

## Understanding Test-Driven Development (TDD)

### What Is TDD?

**Test-Driven Development** is a practice where you write tests BEFORE writing the code.

The cycle:
1. **RED**: Write a failing test
2. **GREEN**: Write minimal code to make the test pass
3. **REFACTOR**: Improve the code while keeping tests passing
4. Repeat!

### Why Write Tests First?

It sounds backwards, but it has benefits:
- Forces you to think about what the code should DO
- Results in more testable code
- Guarantees test coverage
- Creates a tight feedback loop

### TDD Example

Let us build an `add` method using TDD:

**Step 1: Write a failing test (RED)**

```java
@Test
void add_twoPositiveNumbers_returnsSum() {
    Calculator calc = new Calculator();
    assertEquals(5, calc.add(2, 3));  // Calculator doesn't exist yet!
}
```

Test fails! Calculator class does not exist.

**Step 2: Write minimal code to pass (GREEN)**

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
}
```

Test passes!

**Step 3: Refactor if needed**

Code is simple, no refactoring needed.

**Step 4: Write next failing test**

```java
@Test
void add_negativeNumbers_returnsNegativeSum() {
    Calculator calc = new Calculator();
    assertEquals(-5, calc.add(-2, -3));
}
```

Test passes (our implementation already handles this).

**Step 5: Continue with more tests...**

### TDD Is Not Always Required

TDD is a valuable skill to understand, but it is not always the best approach:
- Learning phase: Sometimes you need to explore before you can test
- Prototype code: Quick experiments might not need tests
- UI code: Visual elements are harder to test-first

The key insight: **Think about how you will test your code as you write it.**

---

## What Makes a Good Test?

### Characteristics of Good Tests

**1. Independent** - Tests should not depend on each other

```java
// BAD - test2 depends on test1 running first
@Test
void test1() {
    sharedList.add("item");
}

@Test
void test2() {
    assertEquals(1, sharedList.size());  // Fails if test1 hasn't run!
}

// GOOD - each test is self-contained
@Test
void test1() {
    List<String> list = new ArrayList<>();
    list.add("item");
    assertEquals(1, list.size());
}

@Test
void test2() {
    List<String> list = new ArrayList<>();
    list.add("item");
    list.add("another");
    assertEquals(2, list.size());
}
```

**2. Repeatable** - Same result every time

```java
// BAD - depends on current time, might fail
@Test
void testCurrentHour() {
    assertEquals(14, Clock.getCurrentHour());  // Only passes at 2 PM!
}

// GOOD - consistent input, consistent output
@Test
void testHourCalculation() {
    assertEquals(14, Clock.getHourFromTimestamp(1699538400000L));
}
```

**3. Fast** - Tests should run quickly

```java
// BAD - takes forever
@Test
void testSlowOperation() {
    Thread.sleep(5000);  // Tests should not wait!
    // ...
}

// GOOD - runs instantly
@Test
void testFastOperation() {
    assertEquals(5, calc.add(2, 3));
}
```

**4. Clear** - Easy to understand what is being tested

```java
// BAD - what is this testing?
@Test
void test42() {
    var x = new A();
    x.b(1, 2);
    assertTrue(x.c());
}

// GOOD - clear purpose
@Test
void addItem_whenCartEmpty_itemIsAddedSuccessfully() {
    ShoppingCart cart = new ShoppingCart();
    cart.addItem(new Product("Book", 29.99));
    assertTrue(cart.contains("Book"));
}
```

### The FIRST Principles

Good tests are:
- **F**ast - Run quickly (milliseconds)
- **I**ndependent - Don't depend on other tests
- **R**epeatable - Same result every run
- **S**elf-validating - Pass or fail clearly (no manual checking)
- **T**imely - Written close to when the code is written

### Common Testing Mistakes

**Testing too much in one test:**

```java
// BAD - tests multiple things
@Test
void testEverything() {
    Calculator calc = new Calculator();
    assertEquals(5, calc.add(2, 3));
    assertEquals(2, calc.subtract(5, 3));
    assertEquals(12, calc.multiply(3, 4));
    assertEquals(2, calc.divide(10, 5));
}

// GOOD - one test per behavior
@Test
void add_returnsSum() { /* ... */ }

@Test
void subtract_returnsDifference() { /* ... */ }

@Test
void multiply_returnsProduct() { /* ... */ }

@Test
void divide_returnsQuotient() { /* ... */ }
```

**Testing implementation instead of behavior:**

```java
// BAD - tests HOW it works (implementation)
@Test
void testInternalDataStructure() {
    UserList users = new UserList();
    assertEquals(ArrayList.class, users.getInternalList().getClass());
}

// GOOD - tests WHAT it does (behavior)
@Test
void addUser_userCanBeRetrieved() {
    UserList users = new UserList();
    users.add("alice");
    assertTrue(users.contains("alice"));
}
```

---

## Connecting to What You Already Know

### Weeks 4-5: Methods

**A unit IS a method!**

Everything you learned about methods applies to testing:

| Method Concept | Testing Application |
|----------------|---------------------|
| Parameters (input) | Test with different inputs |
| Return value (output) | Assert expected return values |
| Method signature | Defines what to test |
| Single responsibility | One unit = one test focus |

```java
// Method from Week 4:
public int calculateArea(int width, int height) {
    return width * height;
}

// Testing this unit:
@Test
void calculateArea_positiveValues_returnsProduct() {
    assertEquals(50, calculator.calculateArea(5, 10));
}
```

### Week 12: Exception Handling

**Testing exceptions verifies your error handling works!**

```java
// Custom exception from Week 12:
public class InvalidUserException extends Exception {
    public InvalidUserException(String message) {
        super(message);
    }
}

// Method that throws:
public void registerUser(String username) throws InvalidUserException {
    if (username == null || username.isEmpty()) {
        throw new InvalidUserException("Username cannot be empty");
    }
    // ...
}

// Testing the exception:
@Test
void registerUser_emptyUsername_throwsInvalidUserException() {
    UserManager manager = new UserManager();

    assertThrows(InvalidUserException.class, () -> {
        manager.registerUser("");
    });
}

// Testing valid case:
@Test
void registerUser_validUsername_doesNotThrow() {
    UserManager manager = new UserManager();

    assertDoesNotThrow(() -> {
        manager.registerUser("alice");
    });
}
```

### Weeks 7-10: OOP

**Test objects you create!**

```java
// Class from OOP weeks:
public class BankAccount {
    private double balance;

    public BankAccount(double initialBalance) {
        this.balance = initialBalance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public double getBalance() {
        return balance;
    }
}

// Testing the class:
class BankAccountTest {

    @Test
    void constructor_setsInitialBalance() {
        BankAccount account = new BankAccount(100.0);
        assertEquals(100.0, account.getBalance());
    }

    @Test
    void deposit_positiveAmount_increasesBalance() {
        BankAccount account = new BankAccount(100.0);
        account.deposit(50.0);
        assertEquals(150.0, account.getBalance());
    }

    @Test
    void deposit_negativeAmount_balanceUnchanged() {
        BankAccount account = new BankAccount(100.0);
        account.deposit(-50.0);
        assertEquals(100.0, account.getBalance());
    }
}
```

### Week 11: File Handling

**Test file operations with temporary files!**

```java
class FileProcessorTest {
    private File tempFile;

    @BeforeEach
    void setUp() throws IOException {
        tempFile = File.createTempFile("test", ".txt");
    }

    @AfterEach
    void tearDown() {
        tempFile.delete();
    }

    @Test
    void writeAndRead_returnsOriginalContent() throws IOException {
        FileProcessor processor = new FileProcessor();

        processor.writeToFile(tempFile.getPath(), "Hello World");
        String content = processor.readFromFile(tempFile.getPath());

        assertEquals("Hello World", content);
    }
}
```

---

## Common Struggles and How to Overcome Them

### Struggle 1: What to Test vs. How to Test

**The problem:** "I don't know what to test!"

**Solution:** Think about your method's contract:
- What inputs can it receive?
- What should it return for each input?
- What happens with edge cases (null, empty, negative)?
- What exceptions should it throw?

```java
// Method to test:
public int divide(int a, int b) { return a / b; }

// What to test:
// - Normal case: divide(10, 2) should return 5
// - Negative numbers: divide(-10, 2) should return -5
// - Zero dividend: divide(0, 5) should return 0
// - Zero divisor: divide(10, 0) should throw ArithmeticException
```

### Struggle 2: Writing Testable Code

**The problem:** "My code is hard to test!"

**Why it happens:** Code with too many dependencies or side effects is hard to test.

**Solution:** Write methods that:
- Take inputs as parameters (instead of reading from files/databases)
- Return results (instead of printing directly)
- Have single responsibility

```java
// HARD TO TEST - mixes logic with I/O
public void processAndPrint() {
    Scanner scanner = new Scanner(System.in);
    int value = scanner.nextInt();  // Depends on user input!
    System.out.println(value * 2);  // Outputs directly!
}

// EASY TO TEST - pure logic
public int doubleValue(int value) {
    return value * 2;
}

@Test
void doubleValue_returnsDoubled() {
    assertEquals(10, calculator.doubleValue(5));
}
```

### Struggle 3: Understanding Coverage Metrics

**The problem:** "I have 100% coverage but still have bugs!"

**Remember:** Coverage measures what code RUNS, not what is TESTED correctly.

```java
// 100% coverage, but terrible test!
public int add(int a, int b) {
    return a + b;
}

@Test
void testAdd() {
    add(2, 3);  // Code runs (100% coverage!) but no assertion!
}

// Better:
@Test
void testAdd() {
    assertEquals(5, add(2, 3));  // Actually verifies the result!
}
```

### Struggle 4: Test Naming Conventions

**The problem:** "How do I name my tests?"

**Use a consistent pattern:**
- `methodName_condition_expectedResult`
- `should_expectedResult_when_condition`

Pick one and stick with it!

```java
// Pattern 1: method_condition_result
void add_positiveNumbers_returnsPositiveSum()
void add_negativeNumbers_returnsNegativeSum()
void divide_byZero_throwsException()

// Pattern 2: should_result_when_condition
void shouldReturnPositiveSum_whenAddingPositiveNumbers()
void shouldThrowException_whenDividingByZero()
```

---

## Practice Exercises

### Exercise 1: Calculator Testing (meget hjaelp - Maximum Guidance)

**Goal:** Write your first unit tests using JUnit 5.

**Part A: Test basic operations**

Given this Calculator class:

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public int subtract(int a, int b) {
        return a - b;
    }

    public int multiply(int a, int b) {
        return a * b;
    }

    public int divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Cannot divide by zero");
        }
        return a / b;
    }
}
```

Write tests for:
1. `add` with two positive numbers
2. `add` with a negative number
3. `subtract` returning positive result
4. `subtract` returning negative result
5. `multiply` basic case
6. `divide` basic case
7. `divide` by zero (should throw!)

**Template to complete:**

```java
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    private Calculator calc;

    @BeforeEach
    void setUp() {
        calc = new Calculator();
    }

    @Test
    void add_twoPositiveNumbers_returnsSum() {
        // TODO: assertEquals(expected, calc.add(?, ?));
    }

    @Test
    void add_negativeAndPositive_returnsCorrectSum() {
        // TODO: Test adding -3 and 5
    }

    @Test
    void subtract_largerMinusSmaller_returnsPositive() {
        // TODO: Test 10 - 4
    }

    @Test
    void subtract_smallerMinusLarger_returnsNegative() {
        // TODO: Test 4 - 10
    }

    @Test
    void multiply_twoNumbers_returnsProduct() {
        // TODO: Test 3 * 4
    }

    @Test
    void divide_evenlyDivisible_returnsQuotient() {
        // TODO: Test 10 / 2
    }

    @Test
    void divide_byZero_throwsArithmeticException() {
        // TODO: Use assertThrows
    }
}
```

### Exercise 2: Person Class Testing (nogen hjaelp - Moderate Guidance)

**Goal:** Test a class with validation and custom exceptions.

**Part A: Create the Person class with validation**

```java
public class Person {
    private String name;
    private int age;
    private String email;

    // TODO: Implement setters with validation:
    // - setName: throws IllegalArgumentException if null or empty
    // - setAge: throws IllegalArgumentException if < 0 or > 150
    // - setEmail: throws IllegalArgumentException if doesn't contain "@"

    // TODO: Implement getters
}
```

**Part B: Write comprehensive tests**

Test each setter for:
- Valid input (should work)
- Invalid input (should throw with appropriate message)
- Edge cases

Write at least 9 tests:
- 3 for name validation
- 3 for age validation
- 3 for email validation

Use @BeforeEach to create fresh Person objects.

### Exercise 3: Shopping Cart Testing (ingen hjaelp - Minimal Guidance)

**Goal:** Build and thoroughly test a shopping cart system.

**Requirements:**

Create these classes:
1. `Product` - name, price
2. `ShoppingCart` - add/remove products, calculate total, apply discounts

Test these behaviors:
- Adding products increases cart size
- Removing products decreases cart size
- Total is calculated correctly
- Discount applies correctly (e.g., 10% off for orders over $100)
- Cannot add null products
- Cannot add products with negative price
- Removing non-existent product throws exception

Write at least 15 tests covering:
- Normal operations
- Edge cases
- Error conditions

Achieve high code coverage for your ShoppingCart class.

### Exercise 4: Test the User Admin System (ingen hjaelp - Minimal Guidance)

**Goal:** Write tests for the User Admin system from Week 12.

If you built the User Admin system in Week 12, write tests for:
- Adding users successfully
- Adding duplicate users (throws DuplicateUserException)
- Finding existing users
- Finding non-existent users (throws UserNotFoundException)
- Updating passwords
- Invalid password validation
- File operations (save and load)

Use @BeforeEach to reset the UserManager before each test.
Use temporary files for testing file operations.

This exercise connects Week 12 (exceptions) with Week 13 (testing)!

---

## Looking Ahead

### Week 14: Simple Sorting with Comparable

Testing becomes even more valuable when sorting:

```java
// Testing that your Comparable implementation is correct
@Test
void compareTo_olderPerson_returnsPositive() {
    Person older = new Person("Alice", 30);
    Person younger = new Person("Bob", 20);

    assertTrue(older.compareTo(younger) > 0);
}

@Test
void compareTo_samePerson_returnsZero() {
    Person person = new Person("Alice", 30);

    assertEquals(0, person.compareTo(person));
}
```

### Week 15: Interfaces and Advanced Sorting

Testing Comparator implementations:

```java
// Test your custom Comparator
@Test
void compareByName_alphabeticalOrder() {
    Comparator<Person> byName = new NameComparator();
    Person alice = new Person("Alice", 30);
    Person bob = new Person("Bob", 25);

    assertTrue(byName.compare(alice, bob) < 0);  // Alice before Bob
}
```

### Professional Development

Unit testing opens doors to:
- **Continuous Integration**: Automated testing in build pipelines
- **Test-Driven Development**: Writing tests first
- **Behavior-Driven Development**: Tests that read like specifications
- **Code Quality**: Better, more maintainable code

---

## Key Takeaways

1. **Unit testing tests individual methods (units)** in isolation to verify they work correctly

2. **JUnit 5 is the standard Java testing framework** - it provides @Test, assertions, and lifecycle hooks

3. **The @Test annotation marks a method as a test** - JUnit runs all @Test methods automatically

4. **Assertions verify expected results**:
   - assertEquals(expected, actual)
   - assertTrue(condition)
   - assertFalse(condition)
   - assertNull(value)
   - assertNotNull(value)
   - assertThrows(ExceptionType.class, () -> code)

5. **Good test names document behavior** - use patterns like method_condition_expectedResult

6. **assertThrows tests exception handling** - connect to your Week 12 knowledge!

7. **@BeforeEach runs setup before each test** - ensures tests are independent

8. **@AfterEach runs cleanup after each test** - useful for resources

9. **Code coverage measures what percentage of code is tested** - aim for 80% but focus on quality

10. **TDD = write tests first** - Red, Green, Refactor cycle

11. **Good tests are FIRST**: Fast, Independent, Repeatable, Self-validating, Timely

12. **Tests make you faster, not slower** - bugs caught early are cheap to fix!

13. **This is a professional skill** - every Java developer writes tests

---

## For the Next Topic Agent

### Terminology Established This Week

- **unit**: The smallest testable piece of code (typically a method)
- **unit testing**: Testing individual units in isolation
- **JUnit**: Java's standard testing framework (JUnit 5 = JUnit Jupiter)
- **@Test**: Annotation marking a method as a test
- **assertion**: Statement verifying expected results
- **assertEquals**: Assertion checking equality
- **assertTrue/assertFalse**: Assertions checking boolean conditions
- **assertNull/assertNotNull**: Assertions checking null status
- **assertThrows**: Assertion verifying exception is thrown
- **assertDoesNotThrow**: Assertion verifying no exception is thrown
- **@BeforeEach**: Annotation for code running before each test
- **@AfterEach**: Annotation for code running after each test
- **@BeforeAll/@AfterAll**: Annotations for one-time setup/teardown (static methods)
- **AAA pattern**: Arrange, Act, Assert test structure
- **code coverage**: Percentage of code executed by tests
- **TDD (Test-Driven Development)**: Practice of writing tests before code
- **Red-Green-Refactor**: TDD cycle (failing test, passing test, improve code)
- **FIRST principles**: Fast, Independent, Repeatable, Self-validating, Timely

### Concepts From Prior Weeks Applied

| Prior Week | Concept | Week 13 Application |
|------------|---------|---------------------|
| Weeks 4-5 | Methods | Unit = method; tests verify method behavior |
| Week 12 | Custom exceptions | assertThrows tests exception handling |
| Week 12 | throw keyword | Testing that exceptions ARE thrown |
| Week 12 | try-catch | Understanding what code paths to test |
| Weeks 7-10 | Classes/Objects | Test objects created from classes |
| Weeks 7-10 | Constructors | Test object initialization |
| Week 11 | File handling | Test with temporary files |

### Student Capabilities After This Week

Students can now:
- Write unit tests using JUnit 5
- Use @Test annotation to mark test methods
- Apply assertion methods (assertEquals, assertTrue, assertFalse, assertNull, assertNotNull)
- Test exception throwing with assertThrows
- Use @BeforeEach and @AfterEach for test setup and cleanup
- Follow test naming conventions
- Understand code coverage concepts
- Explain TDD principles conceptually
- Recognize characteristics of good tests
- Connect testing to methods (units) from Weeks 4-5
- Test custom exceptions from Week 12

### Critical Concepts for Week 14 (Simple Sorting)

Week 14 should build on these Week 13 foundations:
- **Testing compareTo()**: Verify Comparable implementation with unit tests
- **Testing sort results**: Assert that collections are correctly sorted
- **Edge case testing**: Empty arrays, single elements, already sorted

Testing patterns students can use:

```java
// Testing Comparable implementation
@Test
void compareTo_olderStudent_returnsPositive() {
    Student s1 = new Student("Alice", 30);
    Student s2 = new Student("Bob", 20);
    assertTrue(s1.compareTo(s2) > 0);
}

// Testing sorted array
@Test
void sort_unsortedArray_returnsSortedArray() {
    int[] arr = {3, 1, 4, 1, 5};
    Arrays.sort(arr);
    assertArrayEquals(new int[]{1, 1, 3, 4, 5}, arr);
}
```

### Assessment Notes

**IMPORTANT**: Unit testing and JUnit are NOT part of the final exam.

However, students should understand:
- The concept of testing (why it matters)
- How testing connects to methods (unit = method)
- General testing principles

This week is about professional preparation, not exam preparation.

### Common Misconceptions to Address Later

1. "Tests slow down development" - Tests actually speed up development by catching bugs early
2. "100% coverage = no bugs" - Coverage measures quantity, not quality of tests
3. "I can test later" - Testing is most valuable when done alongside coding
4. "Tests are only for big projects" - Even small projects benefit from tests
5. "Tests are boring" - Tests provide confidence and enable fearless refactoring

### Handoff Notes for Week 14

Students are now ready for:
- Sorting algorithms and their correctness
- Testing that sorted results are correct
- Understanding Comparable interface (will test compareTo)
- More complex assertions (arrays, collections)

The testing mindset will help students verify their sorting implementations work correctly.
