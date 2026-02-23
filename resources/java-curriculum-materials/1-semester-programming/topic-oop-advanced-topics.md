# Additional OOP Topics - Week 10

*Prerequisites: Week 7 - OOP Part 1: Classes and Objects, Week 8 - OOP Part 2: Encapsulation, Week 9 - OOP Part 4: Inheritance and Polymorphism*
*Phase: Phase 3: Object-Oriented Thinking (Final Week)*

---

## What You'll Learn

By the end of this week, you will be able to:

- **Understand wrapper classes** (Integer, Double, Boolean, Character) and why they exist
- **Apply autoboxing and unboxing** correctly in your code
- **Use ArrayList with wrapper classes** (ArrayList<Integer> instead of int[])
- **Distinguish when to use ArrayList vs arrays** for different scenarios
- **Apply the enhanced for loop** (for-each) to iterate collections elegantly
- **Understand the final keyword** in different contexts (variables, methods, classes)
- **Work with static members** effectively (class variables vs instance variables)
- **Understand object relationships** (association, aggregation, composition - the HAS-A patterns)
- **Compare objects correctly** using == vs .equals()
- **Understand hashCode basics** and why it matters for collections

**MILESTONE**: This week completes your Object-Oriented Programming foundation. Everything from Weeks 7-9 comes together here. You are now ready for practical applications starting in Week 11!

---

## Why This Matters

### The Bridge Between Two Worlds

Think about what you have learned so far:

- **Week 1**: Primitive types (int, double, boolean, char) - simple values
- **Weeks 7-9**: Objects and classes - complex, full-featured entities

But here is a problem: **primitives and objects live in different worlds.**

```java
// Objects can go in ArrayList
ArrayList<String> names = new ArrayList<>();  // Works!

// But primitives cannot...
ArrayList<int> numbers = new ArrayList<>();  // ERROR! int is not an object!
```

**Wrapper classes are the bridge.** They turn primitives INTO objects:

```java
ArrayList<Integer> numbers = new ArrayList<>();  // Works! Integer is an object
numbers.add(42);  // Looks like you're adding an int, but Java converts it!
```

### Completing Your OOP Toolkit

This week adds the final pieces to your object-oriented programming understanding:

| Week | What You Learned | Building Block |
|------|------------------|----------------|
| 7 | Classes and objects | Creating blueprints |
| 8 | Encapsulation | Protecting data |
| 9 | Inheritance and polymorphism | Reusing and extending |
| **10** | **Wrapper classes, ArrayList, final, static, equals** | **Connecting everything** |

After this week, you have a COMPLETE OOP foundation for building real applications.

### Real-World Applications

Everything in this week appears constantly in real software:

- **Wrapper classes**: Every time you store numbers in a database or send data over a network
- **ArrayList**: The most commonly used collection in Java - far more flexible than arrays
- **equals() vs ==**: Every time you check if two things are "the same"
- **final keyword**: Constants, immutable objects, security
- **static members**: Utility methods, counters, shared configuration

---

## Building Your Intuition

### Analogy 1: Primitives as Letters, Wrappers as Envelopes

Imagine you want to mail a letter. The letter itself is the content (your primitive value). But the postal service needs:
- An envelope (the wrapper class)
- An address on the envelope (object features like methods)
- The ability to track the envelope (object identity)

**A primitive is just the content. A wrapper puts it in an envelope so it can travel through the "object world."**

```
Primitive:    42         (just a number, no features)
                ↓
Wrapper:    [Integer]    (an object containing 42)
            | value: 42 |
            | methods   |
            | identity  |
            +-----------+
```

The wrapper "wraps" the primitive, giving it object powers.

### Analogy 2: Arrays as Filing Cabinets, ArrayList as Smart Storage

**Arrays** are like a traditional filing cabinet:
- Fixed number of drawers (size set at creation)
- You must count drawers yourself
- Adding a new drawer means buying a whole new cabinet
- Simple, efficient, but inflexible

**ArrayList** is like a smart expandable storage system:
- Grows automatically when you add items
- Shrinks when you remove items
- Keeps track of how many items you have
- Slightly more overhead, but incredibly convenient

```
Array (fixed size):       ArrayList (dynamic size):
+---+---+---+---+         +---+---+---+---+...
| 0 | 1 | 2 | 3 |         | 0 | 1 | 2 | 3 | (grows!)
+---+---+---+---+         +---+---+---+---+...
   Can't add more!           Can always add more
```

### Analogy 3: final as "Written in Permanent Ink"

When something is `final`, it cannot be changed:

- **final variable**: Like a value written in permanent ink - cannot be erased and rewritten
- **final method**: Like a locked recipe - subclasses cannot change it
- **final class**: Like a sealed family - cannot have children (subclasses)

### Analogy 4: static as "Belonging to the Blueprint"

Remember from Week 7: a class is like a blueprint, objects are houses built from it.

- **Instance variables**: Each house has its own color, address, furniture
- **Static variables**: Things that belong to the BLUEPRINT, not individual houses

```
BLUEPRINT (Class)              HOUSES (Objects)
+------------------+           +-------+  +-------+  +-------+
| static counter=3 |  ------>  |House 1|  |House 2|  |House 3|
+------------------+           |color:R|  |color:B|  |color:G|
                               +-------+  +-------+  +-------+

The counter is ON THE BLUEPRINT.
All houses share the same counter.
Each house has its own color.
```

### Analogy 5: == vs .equals() - Identity vs Appearance

Imagine you have two identical red apples:

- **== asks**: "Are these the SAME apple?" (same physical object)
- **.equals() asks**: "Do these apples LOOK the same?" (same content)

```java
Apple apple1 = new Apple("red", 150);  // Create an apple
Apple apple2 = new Apple("red", 150);  // Create another identical apple
Apple apple3 = apple1;                  // Same apple, different name

apple1 == apple2;      // false - two different apples
apple1 == apple3;      // true - same apple, just two names
apple1.equals(apple2); // true - they look identical
```

---

## Understanding Wrapper Classes

### What Are Wrapper Classes?

**Wrapper classes** are object versions of primitive types. Each primitive has a corresponding wrapper:

| Primitive | Wrapper Class | Example Value |
|-----------|---------------|---------------|
| `int` | `Integer` | `Integer.valueOf(42)` |
| `double` | `Double` | `Double.valueOf(3.14)` |
| `boolean` | `Boolean` | `Boolean.valueOf(true)` |
| `char` | `Character` | `Character.valueOf('A')` |
| `byte` | `Byte` | `Byte.valueOf((byte)127)` |
| `short` | `Short` | `Short.valueOf((short)100)` |
| `long` | `Long` | `Long.valueOf(1000000L)` |
| `float` | `Float` | `Float.valueOf(2.5f)` |

### Why Do Wrapper Classes Exist?

**Three main reasons:**

**1. Collections require objects**

```java
// Primitives cannot go in ArrayList
ArrayList<int> numbers;    // ERROR!

// Wrappers can!
ArrayList<Integer> numbers;  // Works!
```

**2. Null values**

```java
int score = null;      // ERROR! Primitives cannot be null
Integer score = null;  // OK! "No score recorded yet"
```

**3. Utility methods**

```java
// Parse a string to a number
int value = Integer.parseInt("42");

// Get min/max values
int biggest = Integer.MAX_VALUE;  // 2,147,483,647
int smallest = Integer.MIN_VALUE; // -2,147,483,648

// Convert to other types
String text = Integer.toString(42);  // "42"
```

### Creating Wrapper Objects

There are several ways to create wrapper objects:

```java
// Method 1: valueOf() - PREFERRED
Integer num1 = Integer.valueOf(42);
Double num2 = Double.valueOf(3.14);

// Method 2: Autoboxing (automatic conversion) - MOST COMMON
Integer num3 = 42;        // Java converts automatically!
Double num4 = 3.14;       // Java converts automatically!

// Method 3: Constructor - DEPRECATED (don't use)
Integer num5 = new Integer(42);  // Old way, avoid this
```

### Getting the Primitive Value Back

To extract the primitive from a wrapper:

```java
Integer wrapped = Integer.valueOf(42);

// Method 1: xxxValue() method
int primitive1 = wrapped.intValue();
double asDouble = wrapped.doubleValue();

// Method 2: Unboxing (automatic conversion)
int primitive2 = wrapped;  // Java extracts automatically!
```

### Common Mistakes with Wrapper Classes

**Mistake 1: Comparing wrappers with ==**

```java
Integer a = Integer.valueOf(1000);
Integer b = Integer.valueOf(1000);

System.out.println(a == b);      // false! Different objects!
System.out.println(a.equals(b)); // true! Same value!
```

**Why does this happen?** `==` compares object identity (are they the same object in memory?), not value.

**Warning about caching:** For small numbers (-128 to 127), Java caches Integer objects, so `==` may SOMETIMES work. This is deceptive!

```java
Integer x = 100;
Integer y = 100;
System.out.println(x == y);  // true (cached) - DON'T RELY ON THIS!

Integer p = 1000;
Integer q = 1000;
System.out.println(p == q);  // false (not cached)
```

**Always use .equals() for comparing wrapper values!**

**Mistake 2: NullPointerException with null wrappers**

```java
Integer score = null;  // No score yet

// This CRASHES!
int primitive = score;  // NullPointerException!

// Safe way:
if (score != null) {
    int primitive = score;
}
```

When you unbox `null`, Java tries to call `.intValue()` on `null`, which crashes.

---

## Understanding Autoboxing and Unboxing

### What Is Autoboxing?

**Autoboxing** is Java's automatic conversion from primitive to wrapper:

```java
// Without autoboxing (old Java)
Integer num = Integer.valueOf(42);

// With autoboxing (modern Java)
Integer num = 42;  // Java does valueOf() for you!
```

Java automatically "boxes" the primitive into a wrapper object.

### What Is Unboxing?

**Unboxing** is the reverse - automatic conversion from wrapper to primitive:

```java
Integer wrapped = Integer.valueOf(42);

// Without unboxing (old Java)
int primitive = wrapped.intValue();

// With unboxing (modern Java)
int primitive = wrapped;  // Java does intValue() for you!
```

Java automatically "unboxes" the wrapper to get the primitive.

### When Does Autoboxing/Unboxing Happen?

**Autoboxing (primitive to wrapper) happens:**

```java
// Assignment to wrapper type
Integer num = 42;

// Adding to a collection
ArrayList<Integer> list = new ArrayList<>();
list.add(42);  // 42 is autoboxed to Integer

// Method call expecting object
public void process(Integer value) { }
process(42);  // 42 is autoboxed
```

**Unboxing (wrapper to primitive) happens:**

```java
// Assignment to primitive type
Integer wrapped = Integer.valueOf(42);
int primitive = wrapped;

// Arithmetic operations
Integer a = 10;
Integer b = 20;
int sum = a + b;  // Both unboxed for addition

// Comparison operations
if (wrapped > 50) { }  // Unboxed for comparison
```

### Performance Considerations

Autoboxing and unboxing are convenient, but they have a cost:

```java
// SLOW - creates many Integer objects
Integer total = 0;
for (int i = 0; i < 1000000; i++) {
    total = total + i;  // Unbox, add, box, repeat!
}

// FAST - uses primitive
int total = 0;
for (int i = 0; i < 1000000; i++) {
    total = total + i;  // Just addition!
}
```

**Rule of thumb:**
- Use primitives (`int`, `double`) for calculations and local variables
- Use wrappers (`Integer`, `Double`) for collections and when you need null

---

## ArrayList - Better Than Arrays

### Why ArrayList Is Usually Better

Remember arrays from Week 6? They have limitations:

| Arrays | ArrayList |
|--------|-----------|
| Fixed size forever | Grows and shrinks automatically |
| Must track count manually | .size() always correct |
| Inserting is complex | .add(index, value) handles it |
| Removing leaves holes | .remove() closes gaps |
| Works with primitives | Works with objects (use wrappers) |

### Creating an ArrayList

```java
import java.util.ArrayList;  // Must import!

// Create empty ArrayList of Integers
ArrayList<Integer> numbers = new ArrayList<>();

// Create empty ArrayList of Strings
ArrayList<String> names = new ArrayList<>();

// Create with initial capacity (optimization, not required)
ArrayList<Integer> bigList = new ArrayList<>(1000);
```

**Note:** The angle brackets `<Integer>` specify what type the list holds. This is called a **generic type**.

### Essential ArrayList Methods

```java
ArrayList<String> fruits = new ArrayList<>();

// Adding elements
fruits.add("Apple");           // Add at end
fruits.add("Banana");          // Add at end
fruits.add(1, "Orange");       // Insert at index 1

// List is now: [Apple, Orange, Banana]

// Accessing elements
String first = fruits.get(0);  // "Apple"
int size = fruits.size();      // 3

// Modifying elements
fruits.set(0, "Apricot");      // Replace index 0

// Removing elements
fruits.remove(1);              // Remove by index
fruits.remove("Banana");       // Remove by value

// Checking contents
boolean hasApricot = fruits.contains("Apricot");  // true
int index = fruits.indexOf("Apricot");            // 0

// Clearing
fruits.clear();                // Remove all elements
boolean empty = fruits.isEmpty();  // true
```

### ArrayList with Wrapper Classes

Since ArrayList requires objects, use wrappers for primitive types:

```java
// Storing integers
ArrayList<Integer> scores = new ArrayList<>();
scores.add(95);   // Autoboxing: 95 becomes Integer
scores.add(87);
scores.add(92);

// Calculate average
int sum = 0;
for (int score : scores) {  // Unboxing: Integer becomes int
    sum += score;
}
double average = (double) sum / scores.size();

// Find maximum
int max = scores.get(0);
for (int score : scores) {
    if (score > max) {
        max = score;
    }
}
```

### Converting Between Arrays and ArrayList

```java
// Array to ArrayList
String[] arr = {"A", "B", "C"};
ArrayList<String> list = new ArrayList<>(Arrays.asList(arr));

// ArrayList to Array
ArrayList<String> list2 = new ArrayList<>();
list2.add("X");
list2.add("Y");
String[] arr2 = list2.toArray(new String[0]);
```

### When to Use Arrays vs ArrayList

**Use Arrays when:**
- Size is fixed and known at creation
- Working with primitives in performance-critical code
- Working with multi-dimensional data (int[][])
- Memory efficiency is critical

**Use ArrayList when:**
- Size changes during program execution
- You need add/remove functionality
- You want built-in search (contains, indexOf)
- Code clarity is more important than tiny performance gains

**In practice:** Use ArrayList by default. Only use arrays when you have a specific reason.

---

## The Enhanced For Loop (For-Each)

### What Is the Enhanced For Loop?

The **enhanced for loop** (also called **for-each loop**) provides a cleaner way to iterate through collections and arrays:

```java
// Traditional for loop
ArrayList<String> names = new ArrayList<>();
names.add("Alice");
names.add("Bob");
names.add("Charlie");

for (int i = 0; i < names.size(); i++) {
    System.out.println(names.get(i));
}

// Enhanced for loop - CLEANER!
for (String name : names) {
    System.out.println(name);
}
```

**Read it as:** "For each name in names, do..."

### Syntax

```java
for (ElementType variable : collection) {
    // Use variable
}
```

- `ElementType`: The type of elements in the collection
- `variable`: A name for each element (you choose this)
- `collection`: An array or Iterable (like ArrayList)

### Works with Both Arrays and ArrayList

```java
// With array
int[] scores = {95, 87, 92, 78, 88};
for (int score : scores) {
    System.out.println(score);
}

// With ArrayList
ArrayList<Integer> grades = new ArrayList<>();
grades.add(95);
grades.add(87);
for (int grade : grades) {  // Unboxing happens automatically
    System.out.println(grade);
}
```

### When NOT to Use Enhanced For Loop

**1. When you need the index:**

```java
// Need to know position - use traditional loop
for (int i = 0; i < names.size(); i++) {
    System.out.println("Position " + i + ": " + names.get(i));
}
```

**2. When modifying the list:**

```java
// DON'T do this - causes ConcurrentModificationException!
for (String name : names) {
    if (name.startsWith("A")) {
        names.remove(name);  // CRASH!
    }
}

// Use iterator or traditional loop with index adjustment
for (int i = names.size() - 1; i >= 0; i--) {
    if (names.get(i).startsWith("A")) {
        names.remove(i);  // Safe - going backwards
    }
}
```

**3. When you need to modify the element itself:**

```java
int[] numbers = {1, 2, 3};
for (int num : numbers) {
    num = num * 2;  // This does NOT modify the array!
}
// numbers is still {1, 2, 3}

// Use traditional loop
for (int i = 0; i < numbers.length; i++) {
    numbers[i] = numbers[i] * 2;  // This DOES modify the array
}
// numbers is now {2, 4, 6}
```

---

## The final Keyword

### Three Uses of final

The `final` keyword means "cannot be changed" but applies differently in three contexts:

### 1. final Variables (Constants)

A `final` variable can only be assigned once:

```java
final int MAX_SCORE = 100;
MAX_SCORE = 200;  // ERROR! Cannot reassign

final String SCHOOL_NAME = "DTU";
SCHOOL_NAME = "MIT";  // ERROR! Cannot reassign
```

**Naming convention:** Constants are written in ALL_CAPS with underscores.

**final instance variables:**

```java
public class Student {
    private final String studentId;  // Set once, never changes
    private String name;             // Can change

    public Student(String id, String name) {
        this.studentId = id;  // Must be set in constructor
        this.name = name;
    }

    public void setName(String name) {
        this.name = name;  // OK
    }

    // No setStudentId() - cannot change final field
}
```

**Important:** `final` means the REFERENCE cannot change, not the object itself:

```java
final ArrayList<String> list = new ArrayList<>();
list.add("Hello");    // OK! Modifying the list's contents
list.add("World");    // OK! Still the same list object

list = new ArrayList<>();  // ERROR! Cannot reassign the reference
```

### 2. final Methods (Cannot Override)

A `final` method cannot be overridden by subclasses:

```java
public class BankAccount {
    private double balance;

    // This method CANNOT be overridden - security critical!
    public final void deductFee(double fee) {
        if (fee > 0 && fee <= balance) {
            balance -= fee;
        }
    }

    // This method CAN be overridden
    public void deposit(double amount) {
        balance += amount;
    }
}

public class PremiumAccount extends BankAccount {
    @Override
    public void deposit(double amount) {
        super.deposit(amount * 1.01);  // 1% bonus - OK to override
    }

    // @Override
    // public void deductFee(double fee) { }  // ERROR! Cannot override final
}
```

**Use final methods for:**
- Security-critical operations
- Methods that must work exactly as designed
- Template method patterns where some steps are fixed

### 3. final Classes (Cannot Extend)

A `final` class cannot have subclasses:

```java
public final class String {  // The actual String class is final!
    // Cannot create class that extends String
}

public class MyString extends String {  // ERROR! Cannot extend final class
}
```

**Why make a class final?**
- Security (prevent malicious subclasses)
- Design (the class is complete as-is)
- Optimization (JVM can inline method calls)

**Examples in Java:** String, Integer, Double, Boolean are all final classes.

---

## Static Members Revisited

### Instance vs Static Members

From Week 8, you learned about instance variables (each object has its own). Now let's understand static members fully.

**Instance members** belong to each OBJECT:

```java
public class Student {
    private String name;  // Each student has their own name
    private int age;      // Each student has their own age
}

Student s1 = new Student("Alice", 20);
Student s2 = new Student("Bob", 22);
// s1.name = "Alice", s2.name = "Bob" - different values
```

**Static members** belong to the CLASS:

```java
public class Student {
    private static int totalStudents = 0;  // Shared by ALL students
    private String name;                    // Each student's own

    public Student(String name) {
        this.name = name;
        totalStudents++;  // Increment the shared counter
    }

    public static int getTotalStudents() {
        return totalStudents;
    }
}

Student s1 = new Student("Alice");  // totalStudents = 1
Student s2 = new Student("Bob");    // totalStudents = 2
Student s3 = new Student("Charlie"); // totalStudents = 3

System.out.println(Student.getTotalStudents());  // 3
```

### Static Variables (Class Variables)

Static variables are shared across ALL instances:

```java
public class Car {
    private static int carsProduced = 0;  // Shared counter
    private static final String MANUFACTURER = "CarCo";  // Shared constant

    private String model;  // Instance variable
    private int serialNumber;  // Instance variable

    public Car(String model) {
        this.model = model;
        carsProduced++;
        this.serialNumber = carsProduced;
    }

    public static int getCarsProduced() {
        return carsProduced;
    }
}
```

### Static Methods (Class Methods)

Static methods belong to the class, not instances:

```java
public class MathHelper {
    // No instance variables needed - pure utility class

    public static int add(int a, int b) {
        return a + b;
    }

    public static double circleArea(double radius) {
        return Math.PI * radius * radius;
    }
}

// Call without creating an object
int sum = MathHelper.add(5, 3);
double area = MathHelper.circleArea(10);
```

### Rules for Static Methods

**1. Static methods CANNOT access instance members directly:**

```java
public class Student {
    private String name;  // Instance variable
    private static int count = 0;  // Static variable

    public static void printCount() {
        System.out.println(count);  // OK - static can access static
        // System.out.println(name);  // ERROR! Static cannot access instance
        // System.out.println(this.name);  // ERROR! No 'this' in static
    }

    public void printInfo() {
        System.out.println(name);   // OK - instance can access instance
        System.out.println(count);  // OK - instance can access static
    }
}
```

**2. Static methods are NOT polymorphic:**

```java
public class Parent {
    public static void greet() {
        System.out.println("Hello from Parent");
    }
}

public class Child extends Parent {
    public static void greet() {  // This HIDES, not overrides!
        System.out.println("Hello from Child");
    }
}

Parent p = new Child();
p.greet();  // Prints "Hello from Parent"!
// Static methods use compile-time type, not runtime type
```

### When to Use Static

**Use static for:**
- Constants: `public static final double PI = 3.14159;`
- Counters: tracking how many objects exist
- Utility methods: methods that don't need object state
- Factory methods: `Integer.valueOf(42)`

**Don't use static for:**
- Data that varies per object
- Methods that need access to instance variables
- When polymorphism is needed

---

## Object Relationships: HAS-A Patterns

### Three Types of Object Relationships

In Week 9, you learned about IS-A (inheritance). Now let's understand HAS-A (composition) relationships more deeply.

**IS-A (Inheritance):** "A SportsCar IS-A Car"
**HAS-A (Composition):** "A Car HAS-A Engine"

There are three variations of HAS-A relationships:

### 1. Association (Weakest)

**Definition:** Objects know about each other but have independent lifecycles.

**Real-world example:** A student attends a university. The student existed before enrolling and continues to exist after graduating.

```java
public class Student {
    private String name;
    private University university;  // Student knows about university

    public void enrollAt(University uni) {
        this.university = uni;
    }

    public void graduate() {
        this.university = null;  // Student still exists!
    }
}

public class University {
    private String name;
    // University can exist without any students
}
```

### 2. Aggregation (Medium)

**Definition:** One object contains others, but the contained objects can exist independently.

**Real-world example:** A classroom has desks. If the classroom is demolished, the desks can be moved elsewhere.

```java
public class Classroom {
    private ArrayList<Desk> desks;

    public Classroom() {
        this.desks = new ArrayList<>();
    }

    public void addDesk(Desk desk) {
        desks.add(desk);  // Desk existed before, added to room
    }

    public void removeDesk(Desk desk) {
        desks.remove(desk);  // Desk still exists, just not in this room
    }
}

public class Desk {
    private int number;
    // Desk can exist without being in a classroom
}
```

### 3. Composition (Strongest)

**Definition:** One object owns another. The contained object cannot exist without its container.

**Real-world example:** A house has rooms. If the house is demolished, the rooms are destroyed too.

```java
public class House {
    private ArrayList<Room> rooms;

    public House(int numberOfRooms) {
        this.rooms = new ArrayList<>();
        // Rooms are CREATED by the house
        for (int i = 0; i < numberOfRooms; i++) {
            rooms.add(new Room());  // Created inside constructor
        }
    }
    // When House is garbage collected, Rooms are destroyed too
}

public class Room {
    private double area;
    // Room cannot exist without a House
}
```

### Summary Table

| Relationship | Strength | Lifecycle | Example |
|--------------|----------|-----------|---------|
| Association | Weak | Independent | Student - University |
| Aggregation | Medium | Independent | Classroom - Desks |
| Composition | Strong | Dependent | House - Rooms |

### Why Does This Matter?

Understanding these relationships helps you:
1. **Design better classes:** Know when objects should create vs receive other objects
2. **Manage memory:** Understand what happens when objects are destroyed
3. **Read UML diagrams:** These relationships are shown in class diagrams
4. **Communicate with other programmers:** Use precise vocabulary

---

## Object Equality: == vs .equals()

### The Problem

```java
String s1 = new String("Hello");
String s2 = new String("Hello");

System.out.println(s1 == s2);      // false
System.out.println(s1.equals(s2)); // true
```

Why the difference?

### Understanding ==

The `==` operator compares **references** (memory addresses):

```java
Student a = new Student("Alice");
Student b = new Student("Alice");  // Same name, different object
Student c = a;                      // Same object, different name

a == b;  // false - different objects in memory
a == c;  // true - same object in memory
```

Think of it as asking: "Are these the SAME object?"

### Understanding .equals()

The `.equals()` method compares **content** (what you define as equal):

```java
// Default equals() from Object class compares references (same as ==)
// You must OVERRIDE equals() to compare content

public class Student {
    private String name;
    private int id;

    @Override
    public boolean equals(Object obj) {
        // Check for null and type
        if (obj == null || !(obj instanceof Student)) {
            return false;
        }

        // Check for same reference
        if (this == obj) {
            return true;
        }

        // Compare content
        Student other = (Student) obj;
        return this.id == other.id &&
               this.name.equals(other.name);
    }
}
```

### When to Use Which

| Use `==` for: | Use `.equals()` for: |
|---------------|---------------------|
| Checking if same object | Checking if same content |
| Primitives (int, double) | Objects (String, Integer, your classes) |
| Null checks | Value comparison |

```java
// Primitives - use ==
int a = 5;
int b = 5;
if (a == b) { }  // true

// Objects - use equals()
String s1 = "Hello";
String s2 = "Hello";
if (s1.equals(s2)) { }  // true

// Null check - use ==
if (object == null) { }
```

### The String Pool Exception

Java optimizes String literals by reusing them:

```java
String a = "Hello";  // String literal - goes to pool
String b = "Hello";  // Same literal - reuses from pool

a == b;  // true! Same object in the pool

String c = new String("Hello");  // Explicit new object
a == c;  // false! Different objects

a.equals(c);  // true! Same content
```

**Warning:** Never rely on `==` for Strings! Always use `.equals()`.

### The equals() Contract

When overriding equals(), it must be:

1. **Reflexive:** `a.equals(a)` returns true
2. **Symmetric:** If `a.equals(b)` then `b.equals(a)`
3. **Transitive:** If `a.equals(b)` and `b.equals(c)` then `a.equals(c)`
4. **Consistent:** Multiple calls return the same result
5. **Null-safe:** `a.equals(null)` returns false (not NullPointerException)

---

## Understanding hashCode()

### What Is hashCode?

A **hash code** is an integer that represents an object, used by hash-based collections like HashMap and HashSet.

```java
String s = "Hello";
int hash = s.hashCode();  // Some integer like 69609650
```

### Why hashCode Matters

When you put objects in a HashMap or HashSet, Java uses hashCode for fast lookup:

```java
HashSet<Student> students = new HashSet<>();
students.add(new Student("Alice", 101));
students.add(new Student("Bob", 102));

// To find if "Alice" is in the set:
// 1. Calculate hashCode of search object
// 2. Jump directly to that bucket (fast!)
// 3. Use equals() to confirm (may be multiple objects per bucket)
```

### The hashCode Contract

**If you override equals(), you MUST override hashCode():**

1. If `a.equals(b)` is true, then `a.hashCode() == b.hashCode()` must be true
2. If `a.hashCode() != b.hashCode()`, then `a.equals(b)` must be false
3. If `a.hashCode() == b.hashCode()`, `a.equals(b)` may or may not be true

```java
public class Student {
    private String name;
    private int id;

    @Override
    public boolean equals(Object obj) {
        if (obj == null || !(obj instanceof Student)) {
            return false;
        }
        Student other = (Student) obj;
        return this.id == other.id && this.name.equals(other.name);
    }

    @Override
    public int hashCode() {
        // Use same fields as equals()
        int result = 17;  // Start with a non-zero constant
        result = 31 * result + id;
        result = 31 * result + (name != null ? name.hashCode() : 0);
        return result;
    }
}
```

### Modern Java Approach

Java provides a helper method:

```java
import java.util.Objects;

@Override
public int hashCode() {
    return Objects.hash(name, id);  // Easy!
}

@Override
public boolean equals(Object obj) {
    if (this == obj) return true;
    if (obj == null || getClass() != obj.getClass()) return false;
    Student other = (Student) obj;
    return id == other.id && Objects.equals(name, other.name);
}
```

---

## Connecting to What You Already Know

### Week 10 Completes the OOP Picture

| Week | Concept | Week 10 Connection |
|------|---------|-------------------|
| 1 | Primitives (int, double) | Wrapper classes bridge primitives to objects |
| 6 | Arrays | ArrayList is the flexible alternative |
| 7 | Classes and Objects | Static belongs to class, instance belongs to object |
| 8 | Encapsulation | final enforces immutability |
| 9 | Inheritance | equals()/hashCode() from Object class |

### From Week 1: Primitives Get Object Powers

```java
// Week 1: primitives
int x = 42;
double pi = 3.14;

// Week 10: same values, now as objects!
Integer x = 42;        // Can go in collections
Double pi = 3.14;      // Can be null

ArrayList<Integer> list = new ArrayList<>();
list.add(x);  // Primitives couldn't do this!
```

### From Week 6: Arrays Evolve to ArrayList

```java
// Week 6: fixed-size array
int[] scores = new int[5];  // Exactly 5 elements forever

// Week 10: dynamic ArrayList
ArrayList<Integer> scores = new ArrayList<>();
scores.add(95);
scores.add(87);  // Grows automatically!
scores.add(92);  // No size limit!
```

### From Week 9: Everything Is an Object

```java
// Week 9: Custom class hierarchy
Car
├── SportsCar
└── ElectricCar

// Week 10: Java's built-in hierarchy
Object           // Everything extends Object!
├── String       // equals(), hashCode(), toString()
├── Integer      // Wrapper for int
└── YourClass    // Your classes too!
```

### The Complete OOP Toolkit

After Week 10, you have ALL the OOP fundamentals:

| Concept | Purpose | Week Learned |
|---------|---------|--------------|
| Classes/Objects | Define blueprints, create instances | 7 |
| Encapsulation | Protect data with private + getters/setters | 8 |
| Constructors | Initialize objects properly | 7-8 |
| Inheritance | Reuse code with IS-A relationships | 9 |
| Polymorphism | One interface, many behaviors | 9 |
| Wrapper Classes | Bridge primitives to object world | 10 |
| ArrayList | Flexible collections | 10 |
| equals/hashCode | Compare objects properly | 10 |
| static/final | Class-level members, immutability | 10 |

---

## Common Struggles and How to Overcome Them

### Struggle 1: When Autoboxing/Unboxing Occurs

**The confusion:** "Does Java automatically convert here?"

**The answer:** Autoboxing happens when:
- Assigning primitive to wrapper type
- Adding primitive to collection
- Passing primitive to method expecting object

Unboxing happens when:
- Assigning wrapper to primitive type
- Using wrapper in arithmetic
- Comparing wrapper to primitive

```java
// Autoboxing examples
Integer num = 42;                    // int to Integer
list.add(42);                        // int to Integer
someMethod(42);                      // if method expects Integer

// Unboxing examples
int x = num;                         // Integer to int
int sum = num + 10;                  // Integer to int for arithmetic
if (num > 50) { }                    // Integer to int for comparison
```

### Struggle 2: Performance Implications of Wrapper Classes

**The confusion:** "Is using Integer instead of int slow?"

**The answer:** Yes, wrappers have overhead:

```java
// Each Integer is an object on the heap
// Creating millions causes: more memory, more garbage collection

// For tight loops with many iterations, prefer primitives:
int sum = 0;  // NOT Integer sum = 0;
for (int i = 0; i < 1000000; i++) {
    sum += i;
}

// For collections, you must use wrappers:
ArrayList<Integer> list = new ArrayList<>();  // No choice here
```

**Rule of thumb:** Use primitives for calculations, wrappers for collections.

### Struggle 3: NullPointerException with Wrappers

**The confusion:** "My Integer was fine, why did it crash?"

**The answer:** Wrappers can be null, and unboxing null crashes:

```java
Integer score = null;

// This crashes! Cannot unbox null.
int value = score;  // NullPointerException!

// Safe patterns:
if (score != null) {
    int value = score;
}

// Or use a default:
int value = (score != null) ? score : 0;
```

### Struggle 4: Understanding Reference Semantics

**The confusion:** "I changed one list and both changed!"

**The answer:** Object variables are REFERENCES:

```java
ArrayList<String> list1 = new ArrayList<>();
list1.add("Hello");

ArrayList<String> list2 = list1;  // Same list, two names!
list2.add("World");

System.out.println(list1);  // [Hello, World] - both changed!

// To copy, create a new list:
ArrayList<String> list3 = new ArrayList<>(list1);  // Copy!
list3.add("Goodbye");
System.out.println(list1);  // [Hello, World] - unchanged!
```

### Struggle 5: == vs .equals() with Wrappers

**The confusion:** "Sometimes == works, sometimes it doesn't!"

**The answer:** Java caches small Integer values (-128 to 127):

```java
Integer a = 100;
Integer b = 100;
System.out.println(a == b);  // true (cached)

Integer c = 1000;
Integer d = 1000;
System.out.println(c == d);  // false (not cached)
```

**Solution:** ALWAYS use .equals() for comparing wrapper values!

```java
if (a.equals(b)) { }  // Correct!
if (c.equals(d)) { }  // Correct!
```

---

## Practice Exercises

### Exercise 1: Number Statistics (meget hjaelp - Maximum Guidance)

**Goal:** Practice ArrayList with wrapper classes and enhanced for loop.

**Part A: Create the data structure**

```java
import java.util.ArrayList;

public class NumberStats {
    private ArrayList<Integer> numbers;

    public NumberStats() {
        numbers = new ArrayList<>();
    }

    public void addNumber(int number) {
        numbers.add(number);  // Autoboxing happens here
    }

    public int getCount() {
        return numbers.size();
    }
}
```

**Part B: Implement statistics methods**

```java
// TODO: Implement getSum() - add all numbers using enhanced for loop

// TODO: Implement getAverage() - use getSum() / getCount()

// TODO: Implement getMax() - find the largest number

// TODO: Implement getMin() - find the smallest number
```

**Part C: Test your class**

```java
public class NumberStatsDemo {
    public static void main(String[] args) {
        NumberStats stats = new NumberStats();
        stats.addNumber(10);
        stats.addNumber(25);
        stats.addNumber(7);
        stats.addNumber(42);
        stats.addNumber(15);

        System.out.println("Count: " + stats.getCount());    // 5
        System.out.println("Sum: " + stats.getSum());        // 99
        System.out.println("Average: " + stats.getAverage()); // 19.8
        System.out.println("Max: " + stats.getMax());        // 42
        System.out.println("Min: " + stats.getMin());        // 7
    }
}
```

### Exercise 2: Transports (nogen hjaelp - Moderate Guidance)

**Goal:** Practice inheritance hierarchy with wrapper classes.

Create a vehicle hierarchy:

**Requirements:**
- Abstract class `Transport` with: name, maxSpeed, currentPassengers
- `Car extends Transport`: numberOfDoors, hasTrunk
- `Ship extends Transport`: numberOfDecks, lifeBoats
- `Plane extends Transport`: flightNumber, altitudeMeters

**Special behaviors:**
- Each transport calculates `getTicketPrice()` differently:
  - Car: $0.50 per km
  - Ship: $0.20 per km (slow but cheap)
  - Plane: $0.10 per km + $50 base fee (fast but has a fee)

- Use `ArrayList<Transport>` to store all vehicles
- Calculate total capacity of all transports
- Find the fastest transport
- Calculate average ticket price for a 100km journey

### Exercise 3: Event Manager (nogen hjaelp - Moderate Guidance)

**Goal:** Practice multiple classes working together with composition.

**Classes to create:**

```
Event (abstract)
├── Concert (artist, venueName)
├── Conference (speakerName, topic)
└── SportsGame (team1, team2)

EventManager
├── ArrayList<Event> events
├── addEvent(Event e)
├── getEventsByType(String type)
└── getTotalCapacity()

Ticket
├── event (reference)
├── price
├── seatNumber
└── isSold
```

**Requirements:**
- Event has: name, date (String), capacity, ArrayList<Ticket>
- EventManager manages all events
- Each event type calculates base ticket price differently
- Override equals() and toString() for all classes

### Exercise 4: Disappearing Spy (ingen hjaelp - Minimal Guidance)

**Goal:** Deeply understand object references and memory.

Create a spy agency simulation:

**Scenario:**
- Spies have names and code numbers
- Spies can be assigned to missions
- Multiple handlers can reference the same spy
- When a spy is "erased", all references should become invalid

**Explore:**
- What happens when you set a spy reference to null?
- Do other references to the same spy still work?
- How would you truly "erase" a spy (make all references invalid)?
- Implement a solution using a SpyRegistry pattern

**Challenge questions:**
1. Create three references to the same Spy object. Set one to null. What do the others show?
2. If you modify the spy through one reference, do others see the change?
3. Design a system where setting a spy as "inactive" makes all references return "CLASSIFIED"

---

## Looking Ahead

This week completes your Object-Oriented Programming foundation. You now understand:
- How primitives and objects connect (wrapper classes)
- Flexible collections (ArrayList)
- Class-level vs instance-level concepts (static)
- Immutability patterns (final)
- Object comparison (equals, hashCode)

**In Week 11 (File Handling):**
- Reading and writing data to files
- Saving objects to permanent storage
- Working with structured data (CSV files)
- Your wrapper classes and ArrayList skills will be essential!

**In Week 12 (Exception Handling):**
- Handling errors gracefully
- try-catch-finally patterns
- Creating custom exceptions

**In Weeks 14-15 (Sorting and Interfaces):**
- Interfaces build on abstract classes
- Comparable uses wrapper classes
- Collections.sort() works with ArrayList

Your OOP foundation is now complete. You are ready to build real, practical applications that persist data, handle errors gracefully, and work with professional Java patterns.

---

## Key Takeaways

1. **Wrapper classes** (Integer, Double, Boolean, Character) are object versions of primitives

2. **Autoboxing** automatically converts primitives to wrappers; **unboxing** does the reverse

3. **ArrayList** is more flexible than arrays - grows/shrinks automatically, many built-in methods

4. **Use ArrayList<Integer>** for collections of numbers (primitives cannot go in collections)

5. **Enhanced for loop** (`for (String s : list)`) is the cleanest way to iterate collections

6. **final variables** cannot be reassigned; **final methods** cannot be overridden; **final classes** cannot be extended

7. **Static members** belong to the class, not instances; shared by all objects

8. **== compares references** (same object?); **.equals() compares content** (same value?)

9. **Always use .equals()** for comparing objects (especially Strings and wrapper classes!)

10. **If you override equals(), override hashCode()** - required for collections to work correctly

11. **Association, Aggregation, Composition** are three types of HAS-A relationships with different lifecycle implications

12. **ArrayList is usually better than arrays** unless you need fixed size or primitive performance

13. **Wrappers can be null** - always check before unboxing to avoid NullPointerException

14. **This week completes your OOP foundation** - Weeks 7-10 together give you everything needed for professional Java development

---

## For the Next Topic Agent

### Terminology Established This Week

- **wrapper class**: Object version of a primitive type (Integer, Double, Boolean, Character)
- **autoboxing**: Automatic conversion from primitive to wrapper
- **unboxing**: Automatic conversion from wrapper to primitive
- **ArrayList**: Dynamic, resizable list collection (unlike fixed-size arrays)
- **generic type**: Type parameter in angle brackets (ArrayList<Integer>)
- **enhanced for loop / for-each**: `for (Type item : collection)` syntax
- **final variable**: Cannot be reassigned after initialization
- **final method**: Cannot be overridden by subclasses
- **final class**: Cannot be extended
- **static variable**: Class-level variable shared by all instances
- **static method**: Class-level method that doesn't require an instance
- **association**: Weak HAS-A relationship, independent lifecycles
- **aggregation**: Medium HAS-A relationship, contained objects can exist independently
- **composition**: Strong HAS-A relationship, contained objects depend on container
- **reference equality**: Comparing with == (same object in memory?)
- **content equality**: Comparing with .equals() (same content?)
- **hashCode**: Integer value used for hash-based collections

### Concepts From Prior Weeks Now Fully Connected

| Prior Week | Concept | Week 10 Integration |
|------------|---------|---------------------|
| Week 1 | Primitives | Now have wrapper class equivalents |
| Week 6 | Arrays | ArrayList provides flexible alternative |
| Week 7 | Classes | Static belongs to class blueprint |
| Week 8 | Encapsulation | final enforces immutability |
| Week 9 | Object class | equals() and hashCode() from Object |
| Week 9 | Polymorphism | ArrayList<Animal> holds Dog, Cat, etc. |

### Student Capabilities After This Week

Students can now:
- Use wrapper classes appropriately for collections
- Choose between primitives and wrappers based on use case
- Work with ArrayList for dynamic collections
- Apply enhanced for loop for cleaner iteration
- Use final for constants and immutability
- Understand static vs instance members
- Implement equals() and hashCode() correctly
- Compare objects using .equals() instead of ==
- Design class relationships (association, aggregation, composition)
- Handle potential null wrapper values safely

### Critical Concepts for Week 11 (File Handling)

Week 11 should build on:
- **ArrayList** for storing data read from files
- **Wrapper classes** for parsing numeric data from text
- **toString()** for formatting output to files
- **Object relationships** for modeling real data structures

File I/O patterns that use Week 10 concepts:
```java
// Reading numbers from a file
ArrayList<Integer> numbers = new ArrayList<>();
while (scanner.hasNextInt()) {
    numbers.add(scanner.nextInt());  // Autoboxing
}

// Writing objects to a file
for (Student s : students) {
    writer.println(s.toString());
}
```

### Critical Concepts for Week 12 (Exceptions)

Exceptions relate to Week 10:
- **NullPointerException** from null wrapper unboxing
- **NumberFormatException** from Integer.parseInt()
- **IndexOutOfBoundsException** from ArrayList.get()

### Critical Concepts for Weeks 14-15 (Sorting/Interfaces)

Sorting builds directly on Week 10:
- `Collections.sort(ArrayList<T>)` works with ArrayList
- `Comparable<T>` uses wrapper classes for compareTo
- Sorting Integer, Double arrays vs ArrayList<Integer>

### Common Misconceptions to Watch For

1. "Wrapper classes are always better than primitives" - No, primitives are faster for calculations
2. "== works for comparing Integers" - Only sometimes (caching), always use .equals()
3. "ArrayList and array are interchangeable" - Different APIs and capabilities
4. "Static methods can access instance variables" - No, they cannot
5. "final ArrayList means I can't add to it" - No, final means can't reassign the reference

### Assessment Preparation Notes

This topic comprises 10-15% of exam content. Key patterns:
1. Choose between array and ArrayList for a scenario
2. Identify autoboxing/unboxing in code
3. Compare objects correctly (== vs .equals())
4. Use enhanced for loop appropriately
5. Apply final keyword correctly
6. Distinguish static from instance members
7. Implement equals() and hashCode() following the contract
