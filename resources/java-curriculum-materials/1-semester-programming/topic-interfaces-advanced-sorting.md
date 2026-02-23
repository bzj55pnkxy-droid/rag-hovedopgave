# Interfaces and Advanced Sorting - Week 15

*Prerequisites: Week 14 (Simple Sorting with Comparable), Week 9 (Inheritance and Polymorphism), Weeks 7-10 (Complete OOP Foundation)*
*Phase: Phase 5: Advanced Abstractions*

---

## What You'll Learn

By the end of this week, you will be able to:

- **Understand what an interface really is** - not just syntax, but the concept of a contract
- **Design your own interfaces** for real-world problems
- **Explain the difference between interfaces and abstract classes** and when to use each
- **Implement multiple interfaces** in a single class
- **Use default, private, and static methods** in interfaces (modern Java features)
- **Master the Comparator interface** for flexible sorting strategies
- **Create multiple Comparators** for the same class (the power of interfaces!)
- **Understand Comparable vs. Comparator** and make the right choice
- **Write anonymous classes** for quick Comparator implementations
- **Use lambda expressions** for concise Comparator definitions
- **Chain Comparators** for multi-level sorting (sort by X, then by Y)
- **Apply the Bean Comparator pattern** for reusable sorting code
- **Use enum-based sorting strategies** for type-safe sort options

**EXAM NOTE**: Interfaces and advanced sorting represent 20-25% of your exam weight. This is the FINAL major topic before exam review!

**CONNECTION TO WEEK 14**: Remember Comparable and natural ordering? Now we add Comparator for UNLIMITED sorting strategies!

**CONNECTION TO WEEK 9**: Remember abstract classes and polymorphism? Interfaces are the next level of abstraction!

**CONNECTION TO WEEKS 7-10**: Your complete OOP foundation enables you to understand interfaces as the ultimate abstraction tool.

---

## Why This Matters

### The Real World Runs on Contracts

Think about your daily life. Contracts are everywhere:

- When you plug a device into a wall outlet, you trust the outlet provides standard power (the "contract")
- When you insert a USB drive, any USB port works because they follow the USB "contract"
- When you hire a plumber, you expect them to know how to fix pipes (their professional "contract")
- When you order food delivery, you expect it to arrive at your door (the delivery "contract")

**Interfaces are programming contracts.** They define WHAT must be done, without specifying HOW.

### Why One Sorting Strategy Is Not Enough

Last week, you made Student sortable by implementing Comparable. But think about this real scenario:

**University Admin System - Different Views Need Different Sorts:**

| View | Sort Needed |
|------|-------------|
| Class Roster | By last name (alphabetical) |
| Grade Report | By GPA (highest first) |
| ID Card Printing | By student ID (numerical) |
| Birthday List | By birth date (chronological) |
| Attendance Sheet | By first name |

With only Comparable (Week 14), you could define ONE natural ordering. To sort differently, you would have to CHANGE your Student class each time!

**With Comparator, you create SEPARATE sorting strategies. Your Student class stays unchanged, but you can sort it ANY way you want!**

This is the power of interfaces - they let you define capabilities OUTSIDE the class, giving you ultimate flexibility.

### Industry Reality

Every professional Java codebase uses interfaces extensively:

- **Spring Framework**: Services, repositories, controllers are all defined as interfaces
- **Java Collections**: List, Set, Map are all interfaces - you choose the implementation
- **Android Development**: Event listeners, callbacks all use interfaces
- **Web Services**: REST APIs are essentially contracts (interfaces) between systems
- **Plugin Systems**: Plugins implement interfaces to extend applications

Understanding interfaces is not optional - it is essential for professional Java development.

---

## Building Your Intuition

### Analogy 1: The Power Outlet Contract

Think about electrical outlets around the world:

```
THE "ELECTRICAL OUTLET" CONTRACT
================================
Promises:
- Provides consistent voltage
- Has a standard plug shape
- Delivers electricity safely

Does NOT specify:
- How electricity is generated (coal, solar, nuclear?)
- The wire color inside the wall
- The brand of the outlet
```

Any device that follows this contract (has the right plug) can use ANY outlet. The device does not care HOW the electricity is generated - it just trusts the contract.

**In Java terms:**
- The outlet contract = an **interface**
- The plug shape = **method signatures**
- Any device using the outlet = a class that **implements** the interface
- The device working = **polymorphism** - any implementation works!

### Analogy 2: Job Requirements vs. Job Training

Imagine a job posting:

```
JOB: Software Developer
REQUIREMENTS (the CONTRACT):
  [x] Can write Java code
  [x] Can work in a team
  [x] Can solve problems

NOT SPECIFIED:
  - Where they learned Java
  - Their personality type
  - What laptop they use
```

The company defines WHAT skills are needed (the interface), not HOW the candidate acquired them (the implementation).

Multiple candidates can meet these requirements in different ways:
- Alice learned Java at university
- Bob learned Java through online courses
- Charlie is self-taught

They all "implement" the same "Developer interface" but in different ways!

**In Java terms:**
- Job requirements = interface methods
- Different candidates = different classes implementing the interface
- Hiring any qualified candidate = using any implementing class

### Analogy 3: Comparable vs. Comparator - Built-In vs. External Expert

**Comparable (Week 14)**: Objects know how to compare THEMSELVES.

Think of it like asking someone: "How do you rank yourself?"

```
Student Alice says: "I compare myself by my GPA. I have 3.8, so I'm pretty high!"
Student Bob says: "I compare myself by my GPA too. I have 3.5, so I'm below Alice."
```

Every student has ONE built-in way to compare themselves.

**Comparator (This Week)**: An EXTERNAL judge compares objects.

Think of hiring different judges for different competitions:

```
GPA Judge says: "Looking at Alice and Bob... Alice wins (higher GPA)!"
Name Judge says: "Looking at Alice and Bob... Alice wins (A comes before B)!"
Age Judge says: "Looking at Alice and Bob... Bob wins (he's younger)!"
```

The students do not change - but different judges give different rankings!

**Key insight:**
- Comparable = "I know how to compare myself" (ONE way, built into the class)
- Comparator = "An expert compares us" (MANY ways, external to the class)

### Analogy 4: Abstract Class vs. Interface - Family vs. Certification

**Abstract class (Week 9)**: Like being part of a family. You inherit traits.

```
The "Bird" Family:
- All members HAVE feathers (inherited field)
- All members CAN fly (but each does it differently)
- You can only be in ONE family
```

**Interface**: Like having a certification. Anyone can earn it.

```
The "Flyable" Certification:
- Anyone who can fly gets this certification
- Birds have it
- Planes have it
- Superheroes have it
- You can have MANY certifications!
```

A bird IS a bird (inheritance). A bird CAN fly (interface capability).

Superman is NOT a bird, but he CAN fly. He cannot inherit from Bird, but he CAN implement Flyable!

---

## Understanding Interfaces in Depth

### What Is an Interface?

An **interface** is a contract that defines WHAT a class must do, without specifying HOW.

Think of it as a promise: "Any class that implements this interface PROMISES to provide these methods."

### Why Do We Need Interfaces?

**Problem without interfaces:**

```java
// Three different sorting systems - no common ground!
class StudentSorter {
    void sort(Student[] students) { ... }
}

class ProductSorter {
    void sortProducts(Product[] products) { ... }
}

class EmployeeSorter {
    void arrangeEmployees(Employee[] employees) { ... }
}

// Each has different method names!
// No way to write generic sorting code!
```

**Solution with interfaces:**

```java
// One contract for ALL sortable things:
interface Comparable<T> {
    int compareTo(T other);
}

// Now ANY class can promise to be sortable:
class Student implements Comparable<Student> { ... }
class Product implements Comparable<Product> { ... }
class Employee implements Comparable<Employee> { ... }

// One sort method works for ALL:
Collections.sort(anyComparableList);
```

### Interface Syntax

Here is how you define an interface:

```java
// Defining an interface
public interface Drawable {
    // Method signature only - NO body!
    void draw();

    // Another method signature
    double getArea();
}
```

**Key points:**
- Use the `interface` keyword (not `class`)
- Methods have NO body - just signatures (in basic interfaces)
- All methods are implicitly `public abstract`
- Interfaces cannot have instance variables (only constants)

### Implementing an Interface

A class "signs the contract" using `implements`:

```java
public class Circle implements Drawable {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    // MUST provide implementation - it's the contract!
    @Override
    public void draw() {
        System.out.println("Drawing a circle with radius " + radius);
    }

    // MUST provide this too!
    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }
}
```

If you implement an interface, you MUST provide ALL the methods. Otherwise, your code will not compile!

### Interfaces vs. Abstract Classes: The Decision Guide

This is a critical exam concept. Here is when to use each:

**Use an INTERFACE when:**

| Criterion | Interface |
|-----------|-----------|
| What it defines | Pure capability/contract |
| Inheritance | Class can implement MANY interfaces |
| Fields | Only constants (public static final) |
| Methods | Originally only abstract; now also default, static, private |
| "Is-a" vs "Can-do" | "Can-do" relationship |
| Example | Comparable, Runnable, Serializable |

**Use an ABSTRACT CLASS when:**

| Criterion | Abstract Class |
|-----------|----------------|
| What it defines | Partial implementation + contract |
| Inheritance | Class can extend only ONE |
| Fields | Can have instance variables |
| Methods | Mix of abstract and concrete |
| "Is-a" vs "Can-do" | "Is-a" relationship |
| Example | Animal, Shape, Employee |

**The Decision Flowchart:**

```
Do unrelated classes need this capability?
    |
    +-- YES --> Use INTERFACE (Comparable, Serializable)
    |
    +-- NO --> Are you defining a family with shared code?
                  |
                  +-- YES --> Use ABSTRACT CLASS (Animal, Shape)
                  |
                  +-- NO --> Use INTERFACE (more flexible)
```

**Real examples:**

```java
// INTERFACE: Any class can be comparable - unrelated classes share this
interface Comparable<T> {
    int compareTo(T other);
}

// ABSTRACT CLASS: Only animals belong to the Animal family
abstract class Animal {
    protected String name;  // Shared field

    public Animal(String name) {
        this.name = name;
    }

    public abstract void makeSound();  // Abstract - each animal differs

    public void sleep() {              // Concrete - all animals sleep similarly
        System.out.println(name + " is sleeping");
    }
}
```

### Multiple Interface Implementation

A class can implement MANY interfaces - this is the key difference from inheritance!

```java
// Multiple interfaces
interface Drawable { void draw(); }
interface Colorable { void setColor(String color); }
interface Resizable { void resize(double factor); }

// One class, many capabilities!
public class Shape implements Drawable, Colorable, Resizable {
    private String color;
    private double size;

    @Override
    public void draw() {
        System.out.println("Drawing shape in " + color);
    }

    @Override
    public void setColor(String color) {
        this.color = color;
    }

    @Override
    public void resize(double factor) {
        size *= factor;
    }
}
```

This is incredibly powerful! A Shape CAN be drawn, CAN be colored, AND CAN be resized.

Think of it like a person having multiple certifications:
- A doctor who is ALSO a pilot AND a scuba diver
- Each certification is a separate interface they implement!

---

## Modern Interface Features (Java 8+)

### Default Methods: Providing Optional Implementations

Sometimes you want to add a new method to an interface, but you do not want to break all existing implementations. Default methods solve this!

```java
public interface Moveable {
    void move(int x, int y);  // Abstract - must implement

    // Default method - has a body!
    default void moveHome() {
        move(0, 0);  // Default implementation
    }
}

public class Player implements Moveable {
    private int x, y;

    @Override
    public void move(int x, int y) {
        this.x = x;
        this.y = y;
    }

    // moveHome() is inherited from the interface - no need to implement!
}
```

**When to use default methods:**
- Adding new methods to existing interfaces without breaking implementations
- Providing common utility methods that most implementations would use
- Avoiding code duplication across implementations

### Static Methods in Interfaces

Interfaces can have static utility methods:

```java
public interface StringUtils {
    // Static method - called on the interface, not instances
    static boolean isEmpty(String str) {
        return str == null || str.isEmpty();
    }

    static String capitalize(String str) {
        if (isEmpty(str)) return str;
        return Character.toUpperCase(str.charAt(0)) + str.substring(1);
    }
}

// Usage:
String name = StringUtils.capitalize("alice");  // "Alice"
```

### Private Methods in Interfaces (Java 9+)

Private methods help avoid code duplication in default methods:

```java
public interface Loggable {
    default void logInfo(String message) {
        log("INFO", message);  // Uses private helper
    }

    default void logError(String message) {
        log("ERROR", message);  // Same helper!
    }

    // Private helper - not visible to implementing classes
    private void log(String level, String message) {
        System.out.println("[" + level + "] " + message);
    }
}
```

### Constants in Interfaces

Interfaces can define constants (implicitly `public static final`):

```java
public interface GameConstants {
    int MAX_PLAYERS = 4;        // Actually: public static final int
    int DEFAULT_LIVES = 3;
    String GAME_VERSION = "1.0";
}

// Usage:
int lives = GameConstants.DEFAULT_LIVES;
```

---

## The Comparator Interface: Flexible Sorting

### Why Comparator When We Have Comparable?

Remember from Week 14: Comparable defines ONE natural ordering built into the class.

But what if you need DIFFERENT orderings? You cannot change the class every time!

**Comparator solves this by defining sorting logic OUTSIDE the class.**

### Comparable vs. Comparator: The Complete Picture

| Aspect | Comparable (Week 14) | Comparator (Week 15) |
|--------|---------------------|---------------------|
| Package | java.lang | java.util |
| Method | compareTo(T other) | compare(T o1, T o2) |
| Compares | this to other | two separate objects |
| Location | Inside the class | Outside the class |
| Count | ONE per class | UNLIMITED per class |
| Purpose | Natural ordering | Custom ordering |
| Modifies class? | Yes | No! |

**Think of it this way:**
- `Comparable`: The class says "This is how I compare myself"
- `Comparator`: An external judge says "This is how I compare these two"

### Creating a Comparator

Here is how to create a Comparator:

```java
import java.util.Comparator;

// A separate class that knows how to compare Students by age
public class StudentAgeComparator implements Comparator<Student> {
    @Override
    public int compare(Student s1, Student s2) {
        return Integer.compare(s1.getAge(), s2.getAge());
    }
}
```

**Key differences from compareTo:**
- Method is `compare(T o1, T o2)` not `compareTo(T other)`
- You compare TWO objects, not `this` to another
- It is in a SEPARATE class (not inside Student)

### Using Comparators with Collections.sort()

```java
List<Student> students = new ArrayList<>();
students.add(new Student("Charlie", 20, 3.5));
students.add(new Student("Alice", 22, 3.8));
students.add(new Student("Bob", 19, 3.2));

// Sort by natural ordering (Comparable - by name)
Collections.sort(students);
// Result: Alice, Bob, Charlie

// Sort by age using Comparator
Collections.sort(students, new StudentAgeComparator());
// Result: Bob (19), Charlie (20), Alice (22)

// Sort by GPA using different Comparator
Collections.sort(students, new StudentGpaComparator());
// Result: Bob (3.2), Charlie (3.5), Alice (3.8)
```

**The same list, three different orderings - without changing the Student class!**

### Multiple Comparators for One Class

This is the power of interfaces! Create as many Comparators as you need:

```java
// Compare by name (alphabetical)
public class StudentNameComparator implements Comparator<Student> {
    @Override
    public int compare(Student s1, Student s2) {
        return s1.getName().compareTo(s2.getName());
    }
}

// Compare by age (youngest first)
public class StudentAgeComparator implements Comparator<Student> {
    @Override
    public int compare(Student s1, Student s2) {
        return Integer.compare(s1.getAge(), s2.getAge());
    }
}

// Compare by GPA (highest first - descending!)
public class StudentGpaComparator implements Comparator<Student> {
    @Override
    public int compare(Student s1, Student s2) {
        // Note: s2 before s1 for descending order!
        return Double.compare(s2.getGpa(), s1.getGpa());
    }
}

// Compare by student ID
public class StudentIdComparator implements Comparator<Student> {
    @Override
    public int compare(Student s1, Student s2) {
        return Integer.compare(s1.getStudentId(), s2.getStudentId());
    }
}
```

Now you can sort the SAME list any way you want:

```java
Collections.sort(students, new StudentNameComparator());  // By name
Collections.sort(students, new StudentAgeComparator());   // By age
Collections.sort(students, new StudentGpaComparator());   // By GPA (descending)
Collections.sort(students, new StudentIdComparator());    // By ID
```

### Reversing Sort Order with Comparators

Several ways to reverse:

**Option 1: Swap parameters in compare()**
```java
// Normal (ascending)
return Integer.compare(s1.getAge(), s2.getAge());

// Reversed (descending)
return Integer.compare(s2.getAge(), s1.getAge());  // Swapped!
```

**Option 2: Negate the result**
```java
return -Integer.compare(s1.getAge(), s2.getAge());  // Negated
```

**Option 3: Use Comparator.reversed()**
```java
Comparator<Student> byAge = new StudentAgeComparator();
Comparator<Student> byAgeReversed = byAge.reversed();

Collections.sort(students, byAgeReversed);
```

**Option 4: Use Collections.reverseOrder() with natural ordering**
```java
Collections.sort(students, Collections.reverseOrder());
```

---

## Anonymous Classes for Comparators

Creating a separate class file for each Comparator is tedious. Anonymous classes let you create a Comparator inline!

### What Is an Anonymous Class?

An anonymous class is a class without a name, created and used in one place:

```java
// Instead of this:
public class StudentAgeComparator implements Comparator<Student> {
    @Override
    public int compare(Student s1, Student s2) {
        return Integer.compare(s1.getAge(), s2.getAge());
    }
}
Collections.sort(students, new StudentAgeComparator());

// You can write this:
Collections.sort(students, new Comparator<Student>() {
    @Override
    public int compare(Student s1, Student s2) {
        return Integer.compare(s1.getAge(), s2.getAge());
    }
});
```

**The anonymous class:**
- Has no name
- Is created right where it is needed
- Implements the interface immediately
- Is perfect for one-time-use Comparators

### When to Use Anonymous Classes

- When you need a Comparator only once
- When the logic is simple
- When you do not want to create a separate file

### Example: Multiple Anonymous Comparators

```java
List<Student> students = new ArrayList<>();
// ... add students ...

// Sort by name (anonymous class)
Collections.sort(students, new Comparator<Student>() {
    @Override
    public int compare(Student s1, Student s2) {
        return s1.getName().compareTo(s2.getName());
    }
});

// Sort by GPA descending (another anonymous class)
Collections.sort(students, new Comparator<Student>() {
    @Override
    public int compare(Student s1, Student s2) {
        return Double.compare(s2.getGpa(), s1.getGpa());
    }
});
```

---

## Lambda Expressions for Comparators

Lambda expressions (Java 8+) make anonymous classes even shorter!

### What Is a Lambda Expression?

A lambda is a compact way to write a single-method interface implementation:

```java
// Anonymous class (verbose)
Collections.sort(students, new Comparator<Student>() {
    @Override
    public int compare(Student s1, Student s2) {
        return Integer.compare(s1.getAge(), s2.getAge());
    }
});

// Lambda expression (concise!)
Collections.sort(students, (s1, s2) -> Integer.compare(s1.getAge(), s2.getAge()));
```

### Lambda Syntax

```
(parameters) -> expression
or
(parameters) -> { statements; }
```

**Breaking it down:**
- `(s1, s2)` - the parameters (two Students to compare)
- `->` - the arrow, meaning "goes to" or "becomes"
- `Integer.compare(s1.getAge(), s2.getAge())` - what to return

### Examples: Comparator Lambdas

```java
// By name
Collections.sort(students, (s1, s2) -> s1.getName().compareTo(s2.getName()));

// By age
Collections.sort(students, (s1, s2) -> Integer.compare(s1.getAge(), s2.getAge()));

// By GPA (descending)
Collections.sort(students, (s1, s2) -> Double.compare(s2.getGpa(), s1.getGpa()));

// By student ID
Collections.sort(students, (s1, s2) -> s1.getStudentId() - s2.getStudentId());
```

### Even Simpler: Method References and Comparator.comparing()

Java provides utility methods that make it even easier:

```java
// Using Comparator.comparing() with method reference
Collections.sort(students, Comparator.comparing(Student::getName));

// By age
Collections.sort(students, Comparator.comparing(Student::getAge));

// By GPA (reversed for descending)
Collections.sort(students, Comparator.comparing(Student::getGpa).reversed());
```

**How to read this:**
- `Comparator.comparing(Student::getName)` means "compare by the result of getName()"
- `Student::getName` is a "method reference" - a shortcut for `s -> s.getName()`

---

## Multi-Level Sorting (Sort by X, then by Y)

What if you want to sort students by GPA, and for equal GPAs, sort by name?

### The Problem

```java
// Three students with same GPA:
Student s1 = new Student("Charlie", 3.5);
Student s2 = new Student("Alice", 3.5);
Student s3 = new Student("Bob", 3.5);

// Sorting by GPA alone - order among equal GPAs is undefined!
```

### Solution: Chaining Comparators

```java
// Sort by GPA, then by name for equal GPAs
Collections.sort(students, Comparator
    .comparing(Student::getGpa)
    .thenComparing(Student::getName));

// Result: Alice (3.5), Bob (3.5), Charlie (3.5)
// (All have same GPA, so sorted alphabetically by name)
```

### Complex Multi-Level Sorting

```java
// Sort by GPA (descending), then by age (ascending), then by name
Comparator<Student> complexComparator = Comparator
    .comparing(Student::getGpa).reversed()  // GPA: highest first
    .thenComparing(Student::getAge)         // Age: youngest first
    .thenComparing(Student::getName);       // Name: alphabetical

Collections.sort(students, complexComparator);
```

### Manual Multi-Level Comparator

If you need more control, write it manually:

```java
public class StudentMultiComparator implements Comparator<Student> {
    @Override
    public int compare(Student s1, Student s2) {
        // First: compare by GPA (descending)
        int gpaComparison = Double.compare(s2.getGpa(), s1.getGpa());
        if (gpaComparison != 0) {
            return gpaComparison;  // Different GPAs - we have our answer
        }

        // GPAs are equal, so compare by name
        int nameComparison = s1.getName().compareTo(s2.getName());
        if (nameComparison != 0) {
            return nameComparison;
        }

        // Names are also equal, so compare by age
        return Integer.compare(s1.getAge(), s2.getAge());
    }
}
```

---

## The Bean Comparator Pattern

The Bean Comparator pattern creates reusable, configurable Comparators.

### What Is a Bean Comparator?

A "bean" in Java is a class with properties (fields with getters/setters). The Bean Comparator pattern lets you compare beans by any property, specified at runtime.

### Simple Bean Comparator Example

```java
public class StudentBeanComparator implements Comparator<Student> {
    private String sortBy;  // Which property to sort by

    public StudentBeanComparator(String sortBy) {
        this.sortBy = sortBy;
    }

    @Override
    public int compare(Student s1, Student s2) {
        switch (sortBy) {
            case "name":
                return s1.getName().compareTo(s2.getName());
            case "age":
                return Integer.compare(s1.getAge(), s2.getAge());
            case "gpa":
                return Double.compare(s1.getGpa(), s2.getGpa());
            case "id":
                return Integer.compare(s1.getStudentId(), s2.getStudentId());
            default:
                throw new IllegalArgumentException("Unknown sort field: " + sortBy);
        }
    }
}
```

### Using the Bean Comparator

```java
// Sort by different properties using the same Comparator class
Collections.sort(students, new StudentBeanComparator("name"));
Collections.sort(students, new StudentBeanComparator("gpa"));
Collections.sort(students, new StudentBeanComparator("age"));
```

### Enhanced Bean Comparator with Direction

```java
public class StudentBeanComparator implements Comparator<Student> {
    private String sortBy;
    private boolean ascending;

    public StudentBeanComparator(String sortBy, boolean ascending) {
        this.sortBy = sortBy;
        this.ascending = ascending;
    }

    @Override
    public int compare(Student s1, Student s2) {
        int result;
        switch (sortBy) {
            case "name":
                result = s1.getName().compareTo(s2.getName());
                break;
            case "gpa":
                result = Double.compare(s1.getGpa(), s2.getGpa());
                break;
            default:
                result = 0;
        }
        return ascending ? result : -result;  // Reverse if descending
    }
}

// Usage:
Collections.sort(students, new StudentBeanComparator("gpa", false));  // Descending
```

---

## Enum-Based Sorting Strategies

Enums provide a type-safe way to define sorting strategies.

### Why Use Enums for Sorting?

- Type safety: Only valid sort options are allowed
- Self-documenting: Enum values show all available options
- IDE support: Autocomplete shows all choices
- No magic strings: "nme" typo caught at compile time, not runtime

### Defining Sorting Strategies as Enum

```java
public enum StudentSortStrategy {
    BY_NAME,
    BY_AGE,
    BY_GPA,
    BY_STUDENT_ID
}
```

### Comparator Factory Using Enum

```java
public class StudentComparatorFactory {
    public static Comparator<Student> getComparator(StudentSortStrategy strategy) {
        switch (strategy) {
            case BY_NAME:
                return Comparator.comparing(Student::getName);
            case BY_AGE:
                return Comparator.comparing(Student::getAge);
            case BY_GPA:
                return Comparator.comparing(Student::getGpa);
            case BY_STUDENT_ID:
                return Comparator.comparing(Student::getStudentId);
            default:
                throw new IllegalArgumentException("Unknown strategy");
        }
    }
}

// Usage:
Collections.sort(students, StudentComparatorFactory.getComparator(StudentSortStrategy.BY_GPA));
```

### Enum with Built-in Comparator (Advanced)

```java
public enum StudentSortStrategy {
    BY_NAME(Comparator.comparing(Student::getName)),
    BY_AGE(Comparator.comparing(Student::getAge)),
    BY_GPA(Comparator.comparing(Student::getGpa).reversed()),
    BY_STUDENT_ID(Comparator.comparing(Student::getStudentId));

    private final Comparator<Student> comparator;

    StudentSortStrategy(Comparator<Student> comparator) {
        this.comparator = comparator;
    }

    public Comparator<Student> getComparator() {
        return comparator;
    }
}

// Usage:
Collections.sort(students, StudentSortStrategy.BY_GPA.getComparator());
```

---

## Connecting to What You Already Know

### Week 14: Simple Sorting with Comparable

| Week 14 Concept | Week 15 Extension |
|-----------------|-------------------|
| Comparable interface | Comparator interface |
| ONE natural ordering | UNLIMITED custom orderings |
| compareTo(other) | compare(o1, o2) |
| Built into the class | External to the class |
| Collections.sort(list) | Collections.sort(list, comparator) |
| Cannot change without modifying class | Add new orderings without touching class |

### Week 9: Inheritance and Polymorphism

| Week 9 Concept | Week 15 Connection |
|----------------|-------------------|
| Abstract classes | Interfaces are "purer" abstraction |
| extends one class | implements MANY interfaces |
| "Is-a" relationship | "Can-do" relationship |
| Partial implementation | Pure contract (usually) |
| @Override | Still use @Override for interface methods! |
| Polymorphism | Works with interfaces too! |

### How They Work Together

```java
// Week 9 abstract class: Animal IS a living thing
abstract class Animal {
    abstract void makeSound();
    void breathe() { System.out.println("Breathing..."); }
}

// Week 14 Comparable: Animal knows how to compare ITSELF
// Week 15 interface: Animal CAN be compared externally
class Dog extends Animal implements Comparable<Dog> {
    private String name;
    private int age;

    @Override
    void makeSound() { System.out.println("Woof!"); }

    @Override
    public int compareTo(Dog other) {
        return this.name.compareTo(other.name);  // Natural order by name
    }
}

// Week 15 Comparator: Compare Dogs externally by age
class DogAgeComparator implements Comparator<Dog> {
    @Override
    public int compare(Dog d1, Dog d2) {
        return Integer.compare(d1.getAge(), d2.getAge());
    }
}
```

---

## Common Struggles and How to Overcome Them

### Struggle 1: Interface vs. Abstract Class Decision

**The problem:** "I never know which one to use!"

**Solution - Ask these questions:**

1. **Can unrelated classes share this capability?**
   - YES: Use interface (Comparable, Serializable, Runnable)
   - NO: Consider abstract class

2. **Do you need to provide shared code?**
   - YES: Abstract class (or interface with default methods)
   - NO: Interface

3. **Does a class need multiple of these?**
   - YES: Must be interface (can implement many)
   - NO: Could be either

**Memory trick:** "Interface = capability, Abstract class = category"
- A Dog CAN be Comparable (capability)
- A Dog IS an Animal (category)

### Struggle 2: Comparable vs. Comparator Choice

**The problem:** "When do I use which?"

**Simple rule:**

- **Comparable**: For the ONE obvious, default way to sort
- **Comparator**: For any OTHER way to sort

**Ask yourself:**
- "Is there ONE natural way everyone expects?" -> Comparable
- "Do I need multiple sorting options?" -> Comparator
- "Can I modify the class?" -> If no, must use Comparator

**Example:**
```java
class Student implements Comparable<Student> {
    // Natural ordering by student ID (the one "official" way)
    @Override
    public int compareTo(Student other) {
        return Integer.compare(this.studentId, other.studentId);
    }
}

// But sometimes we need other orderings - use Comparator!
Comparator<Student> byName = Comparator.comparing(Student::getName);
Comparator<Student> byGpa = Comparator.comparing(Student::getGpa);
```

### Struggle 3: compare() vs. compareTo() Confusion

**The problem:** "They look so similar!"

**Key difference:**

```java
// Comparable.compareTo: I compare MYSELF to another
public int compareTo(Student other) {
    return this.name.compareTo(other.name);
    //     ^^^^
    //     "this" is being compared
}

// Comparator.compare: I compare TWO objects (neither is "this")
public int compare(Student s1, Student s2) {
    return s1.getName().compareTo(s2.getName());
    //     ^^          ^^
    //     Two separate objects, not "this"
}
```

**Memory trick:**
- compare**To** = I compare **to** someone (this to other)
- compare = I compare (two objects, I'm the judge)

### Struggle 4: Understanding Default Methods

**The problem:** "Wait, interfaces can have method bodies now?"

**Yes! Since Java 8.** But understand WHY:

1. **Backwards compatibility**: Adding new methods to interfaces would break all implementations
2. **Code reuse**: Common implementation logic can be shared
3. **Evolution**: Interfaces can grow without breaking existing code

**Rule of thumb:**
- Required behavior: abstract methods (no body)
- Optional/common behavior: default methods (with body)

### Struggle 5: Multiple Interface Implementation

**The problem:** "What if two interfaces have the same method?"

```java
interface A { default void hello() { System.out.println("A"); } }
interface B { default void hello() { System.out.println("B"); } }

class C implements A, B {
    // MUST override to resolve conflict!
    @Override
    public void hello() {
        A.super.hello();  // Call A's version
        // or B.super.hello();  // Call B's version
        // or provide your own implementation
    }
}
```

Java forces you to resolve the conflict - no ambiguity allowed!

---

## Practice Exercises

### Exercise 1: Sten Saks Papir (meget hjaelp - Maximum Guidance)

**Goal:** Create a Rock-Paper-Scissors game using interfaces.

**Step 1: Create the GameChoice interface**

```java
public interface GameChoice {
    // Returns the name of this choice
    String getName();

    // Returns true if this choice beats the other choice
    boolean beats(GameChoice other);
}
```

**Step 2: Implement Rock, Paper, Scissors**

```java
public class Rock implements GameChoice {
    @Override
    public String getName() {
        return "Rock";
    }

    @Override
    public boolean beats(GameChoice other) {
        // Rock beats Scissors
        // Hint: use instanceof to check the type
        return other instanceof Scissors;
    }
}

// TODO: Create Paper (beats Rock)
// TODO: Create Scissors (beats Paper)
```

**Step 3: Create the game logic**

```java
public class RockPaperScissors {
    public static String determineWinner(GameChoice player1, GameChoice player2) {
        if (player1.beats(player2)) {
            return "Player 1 wins with " + player1.getName();
        } else if (player2.beats(player1)) {
            return "Player 2 wins with " + player2.getName();
        } else {
            return "It's a tie!";
        }
    }

    public static void main(String[] args) {
        // Test all combinations
        GameChoice rock = new Rock();
        GameChoice paper = new Paper();
        GameChoice scissors = new Scissors();

        System.out.println(determineWinner(rock, scissors));  // Player 1 wins
        System.out.println(determineWinner(paper, rock));     // Player 1 wins
        System.out.println(determineWinner(scissors, paper)); // Player 1 wins
        System.out.println(determineWinner(rock, rock));      // Tie
    }
}
```

### Exercise 2: Geometriske Former (nogen hjaelp - Moderate Guidance)

**Goal:** Create a GeometricShape interface with multiple implementations.

**Requirements:**

1. Create `GeometricShape` interface with:
   - `double getArea()`
   - `double getPerimeter()`
   - `String getShapeName()`

2. Implement:
   - `Circle` (with radius)
   - `Rectangle` (with width and height)
   - `Triangle` (with three sides - use Heron's formula for area)

3. Make `GeometricShape` implement `Comparable<GeometricShape>`:
   - Natural ordering by area (smallest first)

4. Create `ShapeComparators` class with static methods returning Comparators:
   - `byArea()` - sort by area
   - `byPerimeter()` - sort by perimeter
   - `byName()` - sort by shape name alphabetically

5. Test program that:
   - Creates a list of mixed shapes
   - Sorts by natural ordering (area)
   - Sorts by perimeter using Comparator
   - Finds shape with largest area

**Hints:**
- Circle area: PI * r^2, perimeter: 2 * PI * r
- Rectangle area: w * h, perimeter: 2 * (w + h)
- Triangle (Heron's formula): area = sqrt(s * (s-a) * (s-b) * (s-c)) where s = (a+b+c)/2

### Exercise 3: Space Explorer (ingen hjaelp - Minimal Guidance)

**Goal:** Create a game with multiple interfaces representing capabilities.

**Requirements:**

1. Create interfaces:
   - `Being` - `String getName()`, `int getHealth()`, `void takeDamage(int damage)`
   - `Moveable` - `void move(int x, int y)`, `int getX()`, `int getY()`
   - `Attackable` - `int getAttackPower()`, `void attack(Being target)`

2. Create classes implementing various combinations:
   - `Player` implements Being, Moveable, Attackable
   - `Monster` implements Being, Moveable, Attackable
   - `Turret` implements Being, Attackable (cannot move!)
   - `Civilian` implements Being, Moveable (cannot attack!)

3. Create Comparators:
   - `BeingHealthComparator` - sort by health
   - `BeingNameComparator` - sort by name
   - `AttackPowerComparator` - sort by attack power (for Attackable only)

4. Create a `BattleArena` class that:
   - Holds a list of `Being` objects
   - Can list all beings sorted by health
   - Can find the strongest attacker
   - Can simulate a battle round where all Attackable beings attack a random target

### Exercise 4: FriendSorter Complete (ingen hjaelp - Minimal Guidance)

**Goal:** Build on Week 14's FriendSorter with multiple Comparators.

**Requirements:**

1. `Friend` class with:
   - name, phoneNumber, email, birthday (String "YYYY-MM-DD")
   - Implements Comparable (natural ordering by name)

2. Create multiple Comparators:
   - `FriendNameComparator` (alphabetical)
   - `FriendBirthdayComparator` (chronological - earlier first)
   - `FriendEmailComparator` (alphabetical by email domain, then by username)

3. Create enum `FriendSortOption`:
   - BY_NAME, BY_BIRTHDAY, BY_EMAIL
   - Include a method `getComparator()` returning the appropriate Comparator

4. Create `FriendManager` class with:
   - `addFriend(Friend f)`
   - `sortBy(FriendSortOption option)`
   - `sortBy(FriendSortOption option, boolean descending)`
   - `getFriendsWithBirthdayInMonth(int month)`
   - `printAllFriendsSorted(FriendSortOption option)`

5. Main program demonstrating all sorting options

### Exercise 5: Mine Marsvin (Integration Challenge)

**Goal:** Combine file I/O from Week 11 with sorting from Weeks 14-15.

**Requirements:**

1. `GuineaPig` class with:
   - name, age (months), weight (grams), color
   - Implements Comparable (by name)

2. `GuineaPigManager` that:
   - Reads guinea pigs from file (format: name;age;weight;color)
   - Writes guinea pigs to file
   - Sorts using various Comparators

3. Create Comparators:
   - By age (youngest first)
   - By weight (lightest first)
   - By color (alphabetical)
   - By age then weight (multi-level)

4. Main program that:
   - Loads guinea pigs from "marsvin.txt"
   - Displays all guinea pigs
   - Lets user choose sort criteria
   - Saves sorted list to new file

---

## Looking Ahead

### Week 16: Exam Preparation and Integration

**Congratulations!** You have completed ALL the major conceptual topics in this course!

Next week is about INTEGRATION - bringing everything together for your exam.

**What Week 16 will cover:**
- Review of ALL topics (Weeks 1-15)
- Integration exercises combining multiple concepts
- Exam format and expectations
- Timed practice problems
- Common exam mistakes to avoid
- Design decision practice

**Key skills to review:**
- Basic Java (variables, types, operators)
- Control flow (if/else, loops)
- Methods and decomposition
- Arrays and ArrayList
- Complete OOP (classes, encapsulation, inheritance, polymorphism)
- File handling
- Exception handling
- Interfaces
- Comparable and Comparator

### The Big Picture: What You've Learned

```
Week 1-3:   Foundation      (variables, control flow, loops)
Week 4-6:   Decomposition   (methods, arrays)
Week 7-10:  OOP             (classes, encapsulation, inheritance, polymorphism)
Week 11-13: Professional    (files, exceptions, testing)
Week 14-15: Abstraction     (Comparable, Comparator, interfaces)
Week 16:    Integration     (putting it ALL together)
```

You have gone from "What is a variable?" to designing with interfaces!

---

## Key Takeaways

1. **Interfaces are contracts** - they define WHAT must be done, not HOW

2. **A class can implement MANY interfaces** - unlike inheritance (only ONE parent)

3. **Use interfaces for capabilities** ("can do"), abstract classes for categories ("is a")

4. **Comparable vs. Comparator:**
   - Comparable = ONE natural ordering, INSIDE the class
   - Comparator = MANY custom orderings, OUTSIDE the class

5. **compare() vs. compareTo():**
   - compareTo(other) compares `this` to `other`
   - compare(o1, o2) compares two separate objects

6. **Anonymous classes** let you create Comparators inline without separate class files

7. **Lambda expressions** make Comparators even more concise: `(a, b) -> a.getName().compareTo(b.getName())`

8. **Comparator.comparing()** is the most elegant way: `Comparator.comparing(Student::getName)`

9. **Chain comparators** for multi-level sorting: `.thenComparing()` for secondary criteria

10. **Modern interfaces** can have default methods (with body), static methods, and private methods

11. **The Bean Comparator pattern** creates flexible, reusable sorting logic

12. **Enum-based strategies** provide type-safe sorting options

13. **This is exam-relevant material** - interfaces and sorting are 20-25% of your exam!

---

## For the Next Topic Agent

### Terminology Established This Week

- **interface**: A contract defining method signatures without implementations
- **implements**: Keyword to sign an interface contract
- **contract**: The promise that a class provides certain methods
- **capability**: What a class CAN do (vs. what it IS)
- **Comparator**: External comparison strategy (compare two objects)
- **compare()**: Method in Comparator that compares two separate objects
- **anonymous class**: A class without a name, created inline
- **lambda expression**: Concise way to implement single-method interfaces
- **method reference**: Shortcut syntax like `Student::getName`
- **Comparator.comparing()**: Utility method to create Comparators easily
- **thenComparing()**: Chain method for multi-level sorting
- **default method**: Interface method with a body (optional implementation)
- **static method in interface**: Utility method on the interface itself
- **private method in interface**: Helper method for default methods
- **Bean Comparator**: Pattern for configurable property-based comparison
- **enum-based strategy**: Using enum to select sorting approach

### Concepts From Prior Weeks Applied

| Prior Week | Concept | Week 15 Application |
|------------|---------|---------------------|
| Week 14 | Comparable | Contrasted with Comparator |
| Week 14 | Natural ordering | One ordering vs. many orderings |
| Week 14 | compareTo() | compare() has different signature |
| Week 9 | Abstract classes | Compared to interfaces |
| Week 9 | Polymorphism | Works with interfaces too |
| Week 9 | @Override | Used for interface methods |
| Week 10 | ArrayList | Sorted with Comparators |
| Week 11 | File I/O | Integration in exercises |

### Student Capabilities After This Week

Students can now:
- Design and implement custom interfaces
- Choose between interface and abstract class
- Implement multiple interfaces in one class
- Use default, static, and private methods in interfaces
- Create Comparator classes for custom sorting
- Write anonymous classes for Comparators
- Use lambda expressions for concise Comparators
- Chain Comparators for multi-level sorting
- Apply Bean Comparator pattern
- Use enum-based sorting strategies
- Choose between Comparable and Comparator appropriately

### Critical Concepts for Week 16 (Exam Preparation)

Week 16 should integrate ALL topics. Key interface/sorting exam topics:

1. **Interface vs. Abstract Class decision** - Common exam question!
2. **Comparable vs. Comparator choice** - Must know when to use each
3. **Writing correct compareTo() and compare() methods**
4. **Multi-level sorting** - Chaining comparators
5. **Lambda syntax** for Comparators
6. **Integration** - Combining interfaces with OOP, files, exceptions

### Handoff Notes for Week 16

**Students are ready for:**
- Comprehensive review of all topics
- Timed practice problems
- Integration exercises combining multiple concepts
- Exam format discussion
- Common mistake identification

**Key exam topics from this week:**
- Interface design and implementation
- Comparable vs. Comparator (VERY common exam question!)
- Writing compare() methods
- Using Collections.sort() with Comparators
- Interface vs. abstract class decision (VERY common exam question!)

**Common misconceptions to review:**
1. "Interface methods cannot have bodies" - Not true since Java 8!
2. "Comparable and Comparator do the same thing" - Different purposes!
3. "I can only have one way to sort" - Comparator gives unlimited options!
4. "compare() and compareTo() work identically" - Different signatures!
5. "Abstract classes and interfaces are interchangeable" - Different use cases!

**Student confidence level:** HIGH - this is their final major topic and they have built a complete foundation. They should feel ready for exam preparation!
