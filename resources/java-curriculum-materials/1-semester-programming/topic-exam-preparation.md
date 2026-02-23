# Exam Preparation and Integration - Week 16

*Prerequisites: ALL 15 weeks of the course*
*Phase: Phase 6: Synthesis and Review*

---

## What You Will Learn

By the end of this week, you will be able to:

- **Understand the exam format** - 15-minute practical programming examination
- **Know the weight distribution** - what topics matter most for your grade
- **Review all major concepts** organized by exam weight and importance
- **Connect topics together** - see how 15 weeks of learning form a complete picture
- **Manage your time effectively** during the exam
- **Avoid common mistakes** that cost students points
- **Apply problem-solving strategies** for quick design decisions
- **Feel confident** - you have learned a LOT this semester!

**THIS IS REVIEW AND INTEGRATION** - no new concepts, just bringing together everything you have learned.

**EXAM FORMAT**: 15-minute practical programming examination with live coding

**YOU ARE READY**: After 15 weeks and 46+ exercises, you have built a complete Java foundation!

---

## Why This Matters

### You Have Come So Far!

Think about where you started and where you are now:

**Week 1**: "What is a variable? How do I print something?"

**Week 16**: You can:
- Design complete object-oriented systems
- Create class hierarchies with inheritance and polymorphism
- Read and write files with proper exception handling
- Sort objects using multiple criteria
- Implement interfaces as contracts
- Build menu-driven applications with CRUD operations

**That is an incredible transformation in just 16 weeks!**

### The Exam Is Your Chance to Demonstrate Mastery

The 15-minute practical exam is not about tricks or surprises. It tests whether you can:

1. **Understand a problem** and decompose it
2. **Make design decisions** quickly and correctly
3. **Write working code** that follows Java conventions
4. **Apply OOP principles** appropriately
5. **Handle data** (arrays, files, collections)

You have practiced ALL of these skills throughout the semester. The exam is simply asking you to demonstrate them one more time.

### Integration Is the Key

The exam typically combines multiple topics in one problem. For example:

- Create a class with proper encapsulation (Weeks 7-8)
- That implements Comparable for sorting (Week 14)
- Store objects in an ArrayList (Week 10)
- Read/write from/to a file (Week 11)
- Handle exceptions properly (Week 12)

**If you can integrate topics, you can solve any exam problem.**

---

## Building Your Intuition: The Complete Picture

### The Semester Journey - A Story in Six Phases

Think of your semester as a journey with six distinct chapters:

```
PHASE 1: FOUNDATION BUILDING (Weeks 1-3)
"Learning to speak the language"
- Variables, types, operators
- If/else, switch
- For, while, do-while loops
Result: You can write simple programs that make decisions and repeat actions

PHASE 2: DECOMPOSITION (Weeks 4-6)
"Learning to organize your thoughts"
- Methods with parameters and returns
- Arrays as your first data structure
Result: You can break problems into manageable pieces

PHASE 3: OBJECT-ORIENTED THINKING (Weeks 7-10) **** THE PIVOT ****
"Learning to think in objects"
- Classes and objects
- Encapsulation (private attributes, getters/setters)
- Inheritance and polymorphism
- ArrayList and wrapper classes
Result: You think in terms of objects with state and behavior

PHASE 4: PRACTICAL DEVELOPMENT (Weeks 11-13)
"Learning to handle the real world"
- File I/O (reading and writing data)
- Exception handling (graceful error management)
- Unit testing (Week 13 - NOT on exam)
Result: You can build robust, persistent applications

PHASE 5: ADVANCED ABSTRACTIONS (Weeks 14-15)
"Learning the final layer of abstraction"
- Comparable (natural ordering)
- Comparator (custom ordering)
- Interfaces (contracts)
Result: You can design flexible, extensible systems

PHASE 6: SYNTHESIS (Week 16 - NOW!)
"Bringing it all together"
Result: You are ready for the exam!
```

### How Topics Connect

Every topic builds on previous ones. Here is the web of connections:

```
Variables & Types (Week 1)
    |
    +--> Control Flow (Week 2-3) --> Methods (Week 4-5)
                                          |
                                          v
    Arrays (Week 6) <------------------> OOP Core (Weeks 7-10)
         |                                    |
         |                                    v
         +-----------------------> File I/O (Week 11)
                                          |
                                          v
                                  Exceptions (Week 12)
                                          |
         Sorting (Weeks 14-15) <----------+
               |
               v
         Interfaces (Week 15)
               |
               v
         INTEGRATION (Week 16) = EXAM!
```

**Key insight**: The exam tests your ability to navigate this web, combining concepts from multiple weeks.

---

## Comprehensive Topic Review by Exam Weight

### Object-Oriented Programming (40-50% of Exam)

This is the BIGGEST portion of your exam. Master OOP and you are halfway to success!

#### Classes and Objects (Week 7)

**What you must know:**
- A class is a blueprint; an object is an instance
- Classes have attributes (state) and methods (behavior)
- Objects are created with `new`: `Student s = new Student();`

**Quick review:**

```java
// Class definition
public class Student {
    // Attributes (fields)
    private String name;
    private int age;

    // Constructor
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Methods
    public void study() {
        System.out.println(name + " is studying");
    }
}

// Creating objects
Student alice = new Student("Alice", 20);
Student bob = new Student("Bob", 22);
alice.study();  // "Alice is studying"
```

#### Encapsulation (Week 8)

**CRITICAL EXAM RULE: Attributes must ALWAYS be private!**

**What you must know:**
- ALL attributes are private (including object types!)
- Provide getters and setters as needed
- Constructors initialize object state
- `this` refers to the current object

**Quick review:**

```java
public class BankAccount {
    // ALWAYS private!
    private String accountNumber;
    private double balance;
    private Customer owner;  // Even object types are private!

    // Constructor
    public BankAccount(String accountNumber, Customer owner) {
        this.accountNumber = accountNumber;
        this.owner = owner;
        this.balance = 0.0;
    }

    // Getter
    public double getBalance() {
        return balance;
    }

    // Setter with validation
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    // No setter for accountNumber - it should not change!
}
```

**Common exam mistake**: Making attributes public or forgetting getters/setters.

#### Inheritance and Polymorphism (Week 9)

**What you must know:**
- Inheritance: `class Dog extends Animal`
- Subclass inherits attributes and methods from parent
- `super` refers to the parent class
- `@Override` indicates method replacement
- Polymorphism: parent type can hold child objects

**Quick review:**

```java
// Parent class
public abstract class Animal {
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    public abstract void makeSound();  // Abstract - must be implemented

    public void eat() {
        System.out.println(name + " is eating");
    }
}

// Child class
public class Dog extends Animal {
    private String breed;

    public Dog(String name, String breed) {
        super(name);  // Call parent constructor
        this.breed = breed;
    }

    @Override
    public void makeSound() {
        System.out.println(name + " says Woof!");
    }
}

// Polymorphism
Animal myPet = new Dog("Rex", "German Shepherd");
myPet.makeSound();  // "Rex says Woof!" - calls Dog's version!
```

#### ArrayList and Generics (Week 10)

**What you must know:**
- `ArrayList<Type>` is a dynamic list
- Common methods: add(), get(), remove(), size()
- Wrapper classes: Integer, Double, Boolean for primitives

**Quick review:**

```java
ArrayList<Student> students = new ArrayList<>();
students.add(new Student("Alice", 20));
students.add(new Student("Bob", 22));

// Iterate
for (Student s : students) {
    System.out.println(s.getName());
}

// Access by index
Student first = students.get(0);

// Remove
students.remove(0);  // Remove first element

// Size
int count = students.size();
```

#### Interface vs. Abstract Class Decision (Week 15)

**Common exam question!** Know when to use each:

| Use Interface When... | Use Abstract Class When... |
|----------------------|---------------------------|
| Unrelated classes share capability | Related classes share code |
| Need multiple "contracts" | Need shared instance variables |
| Defining what something CAN DO | Defining what something IS |
| Example: Comparable, Runnable | Example: Animal, Shape |

---

### File Handling (20-25% of Exam)

#### Reading Files (Week 11)

**What you must know:**
- Use Scanner with File object
- Always handle FileNotFoundException
- Use try-with-resources for automatic closing
- Parse lines with split()

**Quick review:**

```java
public ArrayList<Student> loadStudents(String filename) {
    ArrayList<Student> students = new ArrayList<>();

    try (Scanner scanner = new Scanner(new File(filename))) {
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            String[] parts = line.split(";");  // semicolon separator
            String name = parts[0];
            int age = Integer.parseInt(parts[1]);
            students.add(new Student(name, age));
        }
    } catch (FileNotFoundException e) {
        System.out.println("File not found: " + filename);
    }

    return students;
}
```

#### Writing Files (Week 11)

**What you must know:**
- Use PrintWriter for writing
- FileWriter(filename, true) for append mode
- Always close resources (or use try-with-resources)

**Quick review:**

```java
public void saveStudents(ArrayList<Student> students, String filename) {
    try (PrintWriter writer = new PrintWriter(new FileWriter(filename))) {
        for (Student s : students) {
            writer.println(s.getName() + ";" + s.getAge());
        }
    } catch (IOException e) {
        System.out.println("Error writing file: " + e.getMessage());
    }
}
```

**Design decision - toString() vs. getters for file writing:**
- Use getters when you need specific format for files
- toString() is for human-readable display, not file storage

---

### Sorting and Interfaces (20-25% of Exam)

#### Comparable (Week 14)

**What you must know:**
- Implements Comparable<T> in the class itself
- Method: `public int compareTo(T other)`
- Returns: negative (before), zero (equal), positive (after)
- Defines ONE natural ordering

**Quick review:**

```java
public class Student implements Comparable<Student> {
    private String name;
    private double gpa;

    @Override
    public int compareTo(Student other) {
        // Natural ordering by name
        return this.name.compareTo(other.name);
    }
}

// Usage
Collections.sort(students);  // Sorts by name
```

#### Comparator (Week 15)

**What you must know:**
- Separate class that implements Comparator<T>
- Method: `public int compare(T o1, T o2)`
- Defines EXTERNAL ordering - class does not change
- Can have MANY Comparators for same class

**Quick review:**

```java
// Comparator class
public class StudentGpaComparator implements Comparator<Student> {
    @Override
    public int compare(Student s1, Student s2) {
        return Double.compare(s1.getGpa(), s2.getGpa());
    }
}

// Usage
Collections.sort(students, new StudentGpaComparator());

// Lambda version
Collections.sort(students, (s1, s2) -> Double.compare(s1.getGpa(), s2.getGpa()));

// Comparator.comparing version
Collections.sort(students, Comparator.comparing(Student::getGpa));
```

#### Comparable vs. Comparator - The Quick Decision

| Aspect | Comparable | Comparator |
|--------|-----------|-----------|
| Method | compareTo(other) | compare(o1, o2) |
| Location | Inside the class | Separate class |
| Count | ONE per class | MANY per class |
| Use case | Default ordering | Custom orderings |

---

### Foundational Programming (10-15% of Exam)

These are the basics - you should know them cold!

#### Data Types and Variables (Week 1)

- **Primitive types**: int, double, boolean, char
- **Reference types**: String, arrays, objects
- **Declaration**: `int age;`
- **Initialization**: `int age = 25;`

#### Control Flow (Week 2)

```java
// If-else
if (score >= 90) {
    grade = "A";
} else if (score >= 80) {
    grade = "B";
} else {
    grade = "C";
}

// Switch
switch (day) {
    case "Monday":
        System.out.println("Start of week");
        break;
    case "Friday":
        System.out.println("Weekend!");
        break;
    default:
        System.out.println("Regular day");
}
```

#### Loops (Week 3)

```java
// For loop - when you know the count
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}

// While loop - when condition determines end
while (input != 0) {
    input = scanner.nextInt();
}

// For-each loop - for collections
for (Student s : students) {
    System.out.println(s.getName());
}
```

#### Methods (Weeks 4-5)

```java
// Method with parameters and return value
public double calculateAverage(int[] numbers) {
    int sum = 0;
    for (int num : numbers) {
        sum += num;
    }
    return (double) sum / numbers.length;
}

// Void method - no return
public void printGreeting(String name) {
    System.out.println("Hello, " + name);
}
```

#### Arrays (Week 6)

```java
// Declaration and initialization
int[] numbers = new int[5];
String[] names = {"Alice", "Bob", "Charlie"};

// Access and modify
numbers[0] = 10;
String first = names[0];

// Common operations
int sum = 0;
for (int num : numbers) {
    sum += num;
}
double average = (double) sum / numbers.length;
```

---

### Exception Handling (Part of Advanced Features - 20-25%)

#### Basic try-catch (Week 12)

```java
try {
    int result = 10 / 0;  // Will throw ArithmeticException
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero!");
}
```

#### try-catch-finally

```java
try {
    // risky code
} catch (Exception e) {
    // handle error
} finally {
    // always runs - clean up resources
}
```

#### try-with-resources (preferred for files)

```java
try (Scanner scanner = new Scanner(new File("data.txt"))) {
    // use scanner
} catch (FileNotFoundException e) {
    // handle error
}
// scanner is automatically closed!
```

#### throws Declaration

```java
public void readFile(String filename) throws FileNotFoundException {
    Scanner scanner = new Scanner(new File(filename));
    // ...
}
```

---

## Topics NOT on the Exam

These topics are explicitly EXCLUDED from the exam:

1. **JUnit and formal unit testing** (Week 13)
2. **Clean Code as formal theory** (though clean code IS noticed and valued!)
3. **printf or Formatter formatting codes**
4. **UI class implementation**
5. **Extra exercises not covered in regular coursework**

Focus your study time on the topics that ARE on the exam!

---

## Integration Patterns: Combining Topics

The exam typically tests your ability to combine multiple concepts. Here are common integration patterns:

### Pattern 1: Class + File I/O

**Scenario**: Read objects from file, store in ArrayList, write back to file

```java
public class StudentManager {
    private ArrayList<Student> students = new ArrayList<>();

    public void loadFromFile(String filename) {
        try (Scanner scanner = new Scanner(new File(filename))) {
            while (scanner.hasNextLine()) {
                String[] parts = scanner.nextLine().split(";");
                students.add(new Student(parts[0], Integer.parseInt(parts[1])));
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }
    }

    public void saveToFile(String filename) {
        try (PrintWriter writer = new PrintWriter(filename)) {
            for (Student s : students) {
                writer.println(s.getName() + ";" + s.getAge());
            }
        } catch (IOException e) {
            System.out.println("Error writing file");
        }
    }
}
```

### Pattern 2: Inheritance + Sorting

**Scenario**: Create class hierarchy, sort objects polymorphically

```java
public abstract class Employee implements Comparable<Employee> {
    protected String name;
    protected double salary;

    @Override
    public int compareTo(Employee other) {
        return Double.compare(this.salary, other.salary);
    }
}

public class Manager extends Employee {
    private int teamSize;
    // ...
}

public class Developer extends Employee {
    private String language;
    // ...
}

// Can sort mixed list of Managers and Developers!
ArrayList<Employee> employees = new ArrayList<>();
Collections.sort(employees);  // Sorts by salary
```

### Pattern 3: Class + Comparator + File I/O

**Scenario**: Load data, sort by multiple criteria, save sorted result

```java
public class ReportGenerator {
    public void generateSortedReport(String inputFile, String outputFile) {
        ArrayList<Student> students = loadStudents(inputFile);

        // Sort by GPA descending, then by name
        Collections.sort(students, Comparator
            .comparing(Student::getGpa).reversed()
            .thenComparing(Student::getName));

        saveStudents(students, outputFile);
    }
}
```

### Pattern 4: Enum + Class Design

**Scenario**: Use enum for category classification

```java
public enum StudentCategory {
    FRESHMAN(1),
    SOPHOMORE(2),
    JUNIOR(3),
    SENIOR(4);

    private final int year;

    StudentCategory(int year) {
        this.year = year;
    }

    public int getYear() {
        return year;
    }
}

public class Student {
    private String name;
    private StudentCategory category;

    public String getFullDescription() {
        return name + " (Year " + category.getYear() + ")";
    }
}
```

---

## Exam Strategy and Time Management

### The 15-Minute Framework

You have 15 minutes. Here is how to use them wisely:

**Minutes 0-2: READ and UNDERSTAND**
- Read the ENTIRE problem before writing code
- Identify what classes/methods are needed
- Note any special requirements

**Minutes 2-4: PLAN**
- Sketch class structure mentally
- Decide: What attributes? What methods?
- Identify which concepts to apply (inheritance? file I/O? sorting?)

**Minutes 4-12: IMPLEMENT**
- Start with class skeleton
- Add attributes FIRST (always private!)
- Add constructor
- Add methods
- Handle special requirements

**Minutes 12-15: VERIFY**
- Quick syntax check
- Make sure all requirements are met
- Check that attributes are private
- Verify naming conventions

### Quick Decision Checklist

When designing your solution, ask yourself:

**For Classes:**
- [ ] Are ALL attributes private?
- [ ] Do I need a constructor?
- [ ] What getters/setters are needed?
- [ ] Do I need toString()?

**For Inheritance:**
- [ ] Is there a clear "is-a" relationship?
- [ ] What should the parent class contain?
- [ ] What should be abstract?
- [ ] Am I calling super() correctly?

**For Sorting:**
- [ ] Is there ONE natural ordering? --> Comparable
- [ ] Do I need MULTIPLE orderings? --> Comparator
- [ ] Am I using the right comparison method?

**For File I/O:**
- [ ] Am I handling FileNotFoundException?
- [ ] Am I using try-with-resources?
- [ ] Is my delimiter consistent (semicolon vs comma)?

---

## Common Mistakes to Avoid

### Mistake 1: Public Attributes

**WRONG:**
```java
public class Student {
    public String name;  // NO! Never public!
}
```

**CORRECT:**
```java
public class Student {
    private String name;  // Always private!

    public String getName() {
        return name;
    }
}
```

### Mistake 2: Forgetting super() in Constructor

**WRONG:**
```java
public class Dog extends Animal {
    public Dog(String name) {
        // Forgot to call super!
        this.name = name;  // This won't work!
    }
}
```

**CORRECT:**
```java
public class Dog extends Animal {
    public Dog(String name) {
        super(name);  // Must call parent constructor!
    }
}
```

### Mistake 3: Not Closing File Resources

**WRONG:**
```java
Scanner scanner = new Scanner(new File("data.txt"));
// read data...
// Forgot to close! Resource leak!
```

**CORRECT:**
```java
try (Scanner scanner = new Scanner(new File("data.txt"))) {
    // read data...
}  // Automatically closed!
```

### Mistake 4: Comparing Objects with ==

**WRONG:**
```java
String a = "hello";
String b = new String("hello");
if (a == b) {  // Compares references, not content!
    // This might not work!
}
```

**CORRECT:**
```java
if (a.equals(b)) {  // Compares content!
    // This works correctly!
}
```

### Mistake 5: Wrong Comparison Return Value

**WRONG:**
```java
@Override
public int compareTo(Student other) {
    if (this.age > other.age) return 1;  // Incomplete!
}
```

**CORRECT:**
```java
@Override
public int compareTo(Student other) {
    return Integer.compare(this.age, other.age);  // Handles all cases!
}
```

### Mistake 6: Mixing Up compareTo and compare

**compareTo** (Comparable) - inside the class:
```java
public int compareTo(Student other) {
    return this.name.compareTo(other.name);
//         ^^^^
//         Compare THIS to OTHER
}
```

**compare** (Comparator) - separate class:
```java
public int compare(Student s1, Student s2) {
    return s1.getName().compareTo(s2.getName());
//         ^^          ^^
//         Compare TWO separate objects
}
```

### Mistake 7: Forgetting @Override

**WRONG:**
```java
public int compareto(Student other) {  // Typo! Not override!
    return this.name.compareTo(other.name);
}
```

**CORRECT:**
```java
@Override  // Compiler will catch typos!
public int compareTo(Student other) {
    return this.name.compareTo(other.name);
}
```

---

## Practice Exercises: Exam-Style Problems

### Exercise 1: Basic Class Design (15 minutes)

**Problem**: Create a `Book` class for a library system.

Requirements:
- Attributes: title, author, isbn, available (boolean)
- Constructor that initializes all attributes
- Getters for all attributes
- Method `borrow()` that sets available to false (if currently available)
- Method `returnBook()` that sets available to true
- Implement Comparable by title

**Hint**: Start with the class skeleton, then attributes, then constructor, then methods.

### Exercise 2: Inheritance + File I/O (15 minutes)

**Problem**: Create a shape hierarchy with file persistence.

Requirements:
- Abstract class `Shape` with abstract method `getArea()`
- Classes `Circle` (with radius) and `Rectangle` (with width, height)
- Method to save shapes to file (format: type;dimension1;dimension2)
- Method to load shapes from file

**Hint**: Use the type field to determine which class to instantiate when reading.

### Exercise 3: Full Integration (15 minutes)

**Problem**: Create a student grade management system.

Requirements:
- `Student` class with name, studentId, grades (ArrayList<Double>)
- Method `getAverage()` returns average of grades
- Method `getLetterGrade()` returns "A" (>90), "B" (>80), "C" (>70), "D" (>60), "F"
- Implement Comparable by average grade (highest first)
- Create Comparator to sort by name
- Methods to save/load students from file

**Hint**: Break into steps: class first, then methods, then file I/O.

### Exercise 4: Enum + Sorting (15 minutes)

**Problem**: Create a task management system with priority sorting.

Requirements:
- Enum `Priority` with values HIGH, MEDIUM, LOW (with numeric value)
- `Task` class with title, priority, dueDate (String "YYYY-MM-DD")
- Implement Comparable by priority (HIGH first)
- Create Comparator to sort by due date

**Hint**: Enum can have constructor with value.

---

## Key Takeaways and Quick Reference

### The Five Most Important Rules

1. **Attributes are ALWAYS private** - No exceptions on the exam!

2. **Use @Override for inherited/implemented methods** - Helps catch errors

3. **Try-with-resources for file operations** - Automatic resource management

4. **Comparable = ONE ordering inside class, Comparator = MANY orderings outside**

5. **Read the ENTIRE problem before coding** - Understand before you implement

### Quick Syntax Reference

**Class Structure:**
```java
public class ClassName {
    private Type attribute;

    public ClassName(Type param) {
        this.attribute = param;
    }

    public Type getAttribute() { return attribute; }
    public void setAttribute(Type value) { this.attribute = value; }
}
```

**Inheritance:**
```java
public class Child extends Parent {
    public Child(params) {
        super(parentParams);
    }

    @Override
    public void parentMethod() { }
}
```

**Interface:**
```java
public class MyClass implements Comparable<MyClass> {
    @Override
    public int compareTo(MyClass other) {
        return ...;
    }
}
```

**File Read:**
```java
try (Scanner scanner = new Scanner(new File("file.txt"))) {
    while (scanner.hasNextLine()) {
        String line = scanner.nextLine();
        String[] parts = line.split(";");
    }
} catch (FileNotFoundException e) { }
```

**File Write:**
```java
try (PrintWriter writer = new PrintWriter("file.txt")) {
    writer.println("data");
} catch (IOException e) { }
```

### Exam Weight Summary

| Topic | Weight | Your Priority |
|-------|--------|---------------|
| OOP (Classes, Encapsulation, Inheritance) | 40-50% | HIGHEST |
| File I/O and Exceptions | 20-25% | HIGH |
| Sorting (Comparable, Comparator) | 20-25% | HIGH |
| Foundational (Variables, Loops, Arrays) | 10-15% | MEDIUM |

---

## Final Encouragement

### You Have Learned So Much!

Take a moment to appreciate your journey:

- **Week 1**: You learned what a variable is
- **Week 3**: You could make programs loop and decide
- **Week 6**: You mastered arrays
- **Week 8**: You understood encapsulation
- **Week 9**: You grasped inheritance and polymorphism
- **Week 11**: You could persist data to files
- **Week 15**: You implemented interfaces and multiple sorting strategies

**That is 15 weeks of consistent growth and learning!**

### Confidence Builders

- You have completed 46+ exercises
- You have written thousands of lines of Java code
- You have debugged countless errors (and learned from each one!)
- You have built complete applications from scratch
- You have tackled progressively harder challenges

**You ARE a Java programmer now!**

### Exam Day Tips

1. **Sleep well** the night before - a rested mind performs better
2. **Arrive early** - reduce stress from rushing
3. **Read carefully** - understand before you code
4. **Start simple** - get the basic structure right first
5. **Stay calm** - if you get stuck, take a breath and think
6. **Trust your training** - you have done this many times before

### The Bigger Picture

This exam is just one step in your programming journey. Whether you ace it or face challenges, remember:

- Every programmer started as a beginner
- Making mistakes is how we learn
- The skills you have built will serve you for years to come
- Second semester and beyond await you with more exciting challenges!

**You have worked hard. You have learned well. You are ready.**

**Good luck on your exam - but you will not need luck. You have skill!**

---

## For the Next Phase of Your Journey

After this course, you will continue to:

- Build on your OOP foundation in second semester
- Learn more advanced Java features
- Work on larger projects
- Develop specialized skills

The foundation you have built in these 16 weeks is solid. Everything you learn from here builds on what you now know.

**Congratulations on completing 1st Semester Programming!**

---

## Checklist: Are You Ready for the Exam?

Use this checklist to assess your preparation:

### OOP Fundamentals (40-50%)
- [ ] I can create a class with private attributes
- [ ] I can write constructors that initialize all attributes
- [ ] I understand when to use getters vs setters
- [ ] I can create a class hierarchy with inheritance
- [ ] I know when to use abstract classes
- [ ] I understand polymorphism (parent type, child behavior)
- [ ] I can use ArrayList to store objects

### File Handling (20-25%)
- [ ] I can read from a file using Scanner
- [ ] I can write to a file using PrintWriter
- [ ] I understand try-with-resources
- [ ] I can parse lines using split()
- [ ] I know how to handle FileNotFoundException

### Sorting (20-25%)
- [ ] I can implement Comparable in a class
- [ ] I understand when Comparable vs Comparator is appropriate
- [ ] I can create a Comparator class
- [ ] I can use Collections.sort() with both
- [ ] I can write lambda expressions for Comparators

### Foundational Skills (10-15%)
- [ ] I know Java data types
- [ ] I can write if/else and switch statements
- [ ] I can write for, while, and for-each loops
- [ ] I can create and use methods with parameters and returns
- [ ] I understand arrays and their operations

### Integration Skills
- [ ] I can combine multiple concepts in one solution
- [ ] I can make quick design decisions
- [ ] I follow naming conventions consistently
- [ ] I can complete a task within 15 minutes

**If you checked most boxes, you are READY!**

**If some boxes are unchecked, focus your remaining study time there.**
