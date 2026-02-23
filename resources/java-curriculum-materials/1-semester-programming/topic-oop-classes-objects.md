# OOP Part 1: Classes and Objects - Week 7

*Prerequisites: Week 4 - Methods Part 1, Week 5 - Methods Part 2, Week 6 - Arrays*
*Phase: Phase 3: Object-Oriented Thinking*

---

## What You'll Learn

By the end of this week, you will be able to:

- **Understand the paradigm shift** from procedural to object-oriented programming
- **Explain the difference** between a class and an object
- **Create your own classes** with attributes (fields) and behaviors (methods)
- **Instantiate objects** using the `new` keyword
- **Access and modify object state** through methods
- **Understand object references** versus primitive values
- **Implement the `toString()` method** for object representation
- **Understand the `this` keyword** for referring to the current object
- **Create basic constructors** to initialize objects
- **Organize code** using packages
- **Distinguish between static and instance** members (introduction)

This week marks the most significant transition in your programming journey. For six weeks, you have been writing **procedural programs** - sequences of instructions that manipulate data. Now, you will learn to think in **objects** - self-contained units that combine data and behavior. This is not just a new technique; it is an entirely new way of thinking about software.

---

## Why This Matters

### The Limitations of Procedural Programming

Consider a program to manage student information. With your current procedural approach:

```java
// Procedural approach - separate data scattered everywhere
String student1Name = "Alice";
int student1Age = 20;
int[] student1Grades = {85, 92, 78};

String student2Name = "Bob";
int student2Age = 21;
int[] student2Grades = {79, 88, 91};

// Methods are separate from the data they operate on
public static double calculateAverage(int[] grades) { ... }
public static boolean isPassing(int[] grades) { ... }
```

**Problems with this approach:**

1. **Data is scattered** - Nothing groups a student's name, age, and grades together
2. **No protection** - Any code can change any data at any time
3. **Hard to scale** - What if you need 1000 students? 1000 separate variables?
4. **Methods are disconnected** - `calculateAverage` does not "belong" to any student

### How Object-Oriented Programming Solves This

```java
// Object-oriented approach - data and behavior unified
Student alice = new Student("Alice", 20);
alice.addGrade(85);
alice.addGrade(92);
alice.addGrade(78);

Student bob = new Student("Bob", 21);
bob.addGrade(79);
bob.addGrade(88);
bob.addGrade(91);

// Each student knows its own data and behavior
double aliceAverage = alice.getAverage();
boolean bobPassing = bob.isPassing();
```

**Benefits of OOP:**

1. **Data is organized** - Each student object contains ALL its information
2. **Data is protected** - Only the Student class controls how data changes
3. **Easy to scale** - Create as many Student objects as needed
4. **Behavior belongs to objects** - Each student "knows" how to calculate its own average

### Real-World Software Uses OOP

Nearly all modern software is built with object-oriented programming:

- **Games**: Characters, items, enemies, weapons are all objects
- **Banking apps**: Accounts, transactions, customers are objects
- **Social media**: Users, posts, comments, likes are objects
- **E-commerce**: Products, carts, orders, customers are objects
- **Your phone**: Contacts, messages, apps are all objects

Learning OOP opens the door to building real software. This is not just academic - it is how professional programmers think and work.

---

## Building Your Intuition

This is the most abstract concept you have encountered so far. Take your time with these analogies - they are the foundation for understanding everything that follows.

### Analogy 1: Blueprint and Houses

Imagine you are an architect designing houses:

**The Blueprint (Class)**
- A blueprint is a **design document** - it specifies what a house should have
- It defines: number of rooms, bathroom locations, kitchen layout, garage size
- The blueprint itself is NOT a house - you cannot live in a blueprint
- From one blueprint, you can build many identical houses

**The Houses (Objects)**
- Each house is a **specific instance** built from the blueprint
- House #1 at 123 Main St and House #2 at 456 Oak Ave are different houses
- They have the same structure (same blueprint) but different contents
- Each house has its own furniture, paint colors, residents (its own state)

```
BLUEPRINT (Class)              HOUSES (Objects)
+------------------+           +------------------+
|    House         |           |  House at 123 Main |
|    Design        |  builds   |  - Blue paint      |
|                  |  ------> |  - Smith family    |
|  - Rooms: 3      |           |  - Furniture set A |
|  - Bathrooms: 2  |           +------------------+
|  - Has garage    |
+------------------+           +------------------+
                               |  House at 456 Oak  |
        One blueprint          |  - Yellow paint    |
        Many houses            |  - Jones family    |
                               |  - Furniture set B |
                               +------------------+
```

**In Java terms:**
- **Class** = Blueprint (the design/template)
- **Object** = House (a specific thing built from the blueprint)
- **Attributes** = Features (rooms, bathrooms, paint color)
- **State** = Current values (3 rooms, 2 bathrooms, blue paint)

### Analogy 2: Cookie Cutter and Cookies

Think of baking cookies:

**The Cookie Cutter (Class)**
- Defines the **shape** of cookies (star, heart, gingerbread man)
- The cutter itself is NOT a cookie - you cannot eat a cookie cutter
- One cookie cutter can make unlimited cookies

**The Cookies (Objects)**
- Each cookie is a **specific instance** created using the cutter
- All cookies have the same shape but can have different decorations
- Cookie #1 has red frosting, Cookie #2 has blue frosting (different state)
- Each cookie is independent - eating one does not affect others

### Analogy 3: Car Factory and Cars

Consider a car manufacturing plant:

**The Car Design Specification (Class)**
- Defines what a "Car" is: has engine, wheels, doors, color, speed capability
- Specifies behaviors: can accelerate, brake, turn, honk
- The specification is NOT a car - you cannot drive a document

**The Actual Cars (Objects)**
- Each car is built from the specification
- Car #1 is red with 50,000 km, Car #2 is blue with 10,000 km
- Each car has its own current speed, fuel level, mileage (its own state)
- Accelerating Car #1 does not affect Car #2 - they are independent

```
CAR FACTORY (Class)                    CARS (Objects)
+----------------------+               +----------------------+
|        Car           |               |   Car #1             |
|                      |               |   - Brand: Toyota    |
|  Attributes:         |   creates     |   - Color: Red       |
|  - brand             |   -------->   |   - Speed: 60 km/h   |
|  - model             |               |   - Mileage: 50000   |
|  - color             |               +----------------------+
|  - currentSpeed      |
|  - mileage           |               +----------------------+
|                      |               |   Car #2             |
|  Behaviors:          |   creates     |   - Brand: Honda     |
|  - accelerate()      |   -------->   |   - Color: Blue      |
|  - brake()           |               |   - Speed: 0 km/h    |
|  - honk()            |               |   - Mileage: 10000   |
+----------------------+               +----------------------+
```

### Analogy 4: Defining a Word vs Using a Word

Think about the dictionary:

**Dictionary Definition (Class)**
- The dictionary defines what "dog" means: a domesticated canine animal
- The definition is not a dog itself

**Actual Dogs (Objects)**
- "Fido" is a specific dog - a beagle, 5 years old, brown and white
- "Rex" is another specific dog - a German shepherd, 3 years old, black and tan
- Both fit the definition of "dog" but are different individual dogs

### The Critical Distinction

| Concept | Definition | Examples |
|---------|------------|----------|
| **Class** | A template/blueprint that defines what something IS | `Car`, `Student`, `Die` |
| **Object** | A specific instance created from a class | `myCar`, `alice`, `die1` |

A class is like a **noun** (a general concept): "dog", "car", "student"
An object is like a **specific thing**: "Fido", "my red Toyota", "Alice"

**Remember:** You can pet a dog (object), but you cannot pet the concept of "dog" (class).

---

## Understanding Classes

### What Is a Class?

A **class** is a blueprint or template that defines:

1. **Attributes (Fields)** - The data that objects of this class will hold
2. **Methods (Behaviors)** - The actions that objects of this class can perform

Think of it as: **"A class describes what something IS and what it can DO."**

### Why Do We Need Classes?

Classes allow us to:

1. **Model real-world things** - Represent students, cars, games, accounts in code
2. **Bundle related data** - Keep all student info together instead of scattered
3. **Bundle related behavior** - Methods that operate on the data live with the data
4. **Create multiple instances** - Make as many students, cars, etc. as needed
5. **Protect data** - Control how data is accessed and changed

### Basic Class Structure

```java
// A class definition - the blueprint
public class Car {
    // Attributes (fields) - the data
    // By convention, attributes are ALWAYS private
    private String brand;
    private String model;
    private int year;
    private int speed;

    // Methods (behaviors) - what the object can do
    public void accelerate(int amount) {
        speed = speed + amount;
    }

    public void brake() {
        speed = 0;
    }

    public int getSpeed() {
        return speed;
    }
}
```

**Anatomy of a class:**

```
public class ClassName {
    |      |      |
    |      |      +-- The name of the class (capitalize first letter)
    |      +--------- The "class" keyword declares this is a class
    +---------------- Access modifier (public means accessible from anywhere)

    // Instance variables (attributes/fields)
    private dataType variableName;

    // Methods (behaviors)
    public returnType methodName(parameters) {
        // method body
    }
}
```

### Naming Conventions for Classes

- Class names start with an **uppercase letter**: `Car`, `Student`, `BankAccount`
- Use **PascalCase** (capitalize each word): `StudentRecord`, `CarEngine`
- Choose **meaningful names** that describe what the class represents
- Class names are typically **nouns**: `Person`, `Book`, `Game`

### Common Mistake: Confusing Class with Object

```java
// WRONG thinking:
Car;  // "I have a car" - NO! This is just the class name

// CORRECT thinking:
Car myCar = new Car();  // "I have created a specific car object"
```

A class by itself does nothing - it is just a definition. You must CREATE objects from the class to actually use it.

---

## Understanding Objects

### What Is an Object?

An **object** is a specific instance of a class. When you create an object, you are:

1. Allocating memory for the object's data
2. Creating an entity that can perform the class's defined behaviors
3. Getting a reference to access and manipulate the object

Think of it as: **"An object is a specific, concrete thing created from a class blueprint."**

### Creating Objects: The `new` Keyword

To create an object, use the `new` keyword:

```java
// Creating objects from the Car class
Car myCar = new Car();
Car friendsCar = new Car();
```

Let's break down `Car myCar = new Car();`:

```
Car myCar = new Car();
 |    |    |    |
 |    |    |    +-- Calls the constructor to initialize the object
 |    |    +------- The "new" keyword creates the object in memory
 |    +------------ The variable name (reference) - our handle to the object
 +----------------- The type - what kind of object this variable can hold
```

### Objects Have Their Own State

Each object maintains its own **state** (the values of its attributes):

```java
Car car1 = new Car();
Car car2 = new Car();

// Each car has its own speed
car1.accelerate(50);  // car1's speed is now 50
car2.accelerate(30);  // car2's speed is now 30

// They are independent!
System.out.println(car1.getSpeed());  // Prints 50
System.out.println(car2.getSpeed());  // Prints 30
```

Changing `car1` does NOT affect `car2` - they are separate objects with separate memory.

### Objects Can Perform Actions

Objects can execute the methods defined in their class:

```java
Car myCar = new Car();

myCar.accelerate(60);  // "myCar, please accelerate by 60"
myCar.honk();          // "myCar, please honk"
myCar.brake();         // "myCar, please brake"
```

The dot notation (`myCar.accelerate()`) means "tell this object to do this action."

### Multiple Objects from One Class

One class can create unlimited objects:

```java
// One Student class, many Student objects
Student alice = new Student();
Student bob = new Student();
Student carol = new Student();
Student david = new Student();
// ... create as many as needed
```

Each student is independent with its own name, age, grades, etc.

---

## Understanding Attributes (Instance Variables)

### What Are Attributes?

**Attributes** (also called **fields** or **instance variables**) are the data that each object holds. They define the **state** of an object.

Think of it as: **"Attributes are the properties or characteristics that describe an object."**

### Declaring Attributes

Attributes are declared inside the class but outside any method:

```java
public class Student {
    // Attributes (instance variables)
    private String name;
    private int age;
    private int[] grades;
    private double gpa;
}
```

### Why Attributes Are ALWAYS Private

You will notice we use `private` for all attributes. This is a fundamental OOP principle:

```java
// CORRECT - attributes are private
private String name;
private int age;

// WRONG - never make attributes public in this course
public String name;  // Bad practice!
```

**Why private?**

1. **Protection** - Prevents invalid data from being set directly
2. **Control** - The class controls how data is accessed and modified
3. **Flexibility** - You can change internal implementation without breaking other code

This concept is called **encapsulation** - you will explore it deeply in Week 8.

### Accessing Attributes: Getter Methods

Since attributes are private, we provide **getter methods** to read them:

```java
public class Student {
    private String name;
    private int age;

    // Getter for name
    public String getName() {
        return name;
    }

    // Getter for age
    public int getAge() {
        return age;
    }
}
```

### Modifying Attributes: Setter Methods

We provide **setter methods** to modify attributes with validation:

```java
public class Student {
    private String name;
    private int age;

    // Setter for name
    public void setName(String newName) {
        name = newName;
    }

    // Setter for age with validation
    public void setAge(int newAge) {
        if (newAge >= 0 && newAge <= 120) {  // Valid age range
            age = newAge;
        }
    }
}
```

### Using Getters and Setters

```java
Student alice = new Student();

// Set values using setters
alice.setName("Alice");
alice.setAge(20);

// Read values using getters
System.out.println(alice.getName());  // Prints: Alice
System.out.println(alice.getAge());   // Prints: 20

// Cannot access directly (because private)
// alice.name = "Bob";  // ERROR! name is private
```

---

## Understanding Instance Methods

### What Are Instance Methods?

**Instance methods** are methods that belong to objects. They:

1. Can access and modify the object's attributes
2. Define the behavior of objects
3. Are called ON a specific object

### Instance vs Static Methods

Until now, all your methods have been `static`:

```java
// Week 4-5: Static methods - belong to the CLASS
public static double calculateArea(double radius) {
    return Math.PI * radius * radius;
}

// Usage: Called on the class name
double area = MyClass.calculateArea(5.0);
```

Instance methods remove the `static` keyword:

```java
// Week 7: Instance methods - belong to OBJECTS
public class Circle {
    private double radius;

    public double calculateArea() {  // No static!
        return Math.PI * radius * radius;  // Uses object's own radius
    }
}

// Usage: Called on an object
Circle myCircle = new Circle();
double area = myCircle.calculateArea();  // Uses myCircle's radius
```

**Key difference:** Instance methods operate on a specific object's data.

### Defining Instance Methods

```java
public class Car {
    private int speed;
    private String brand;

    // Instance method - modifies this object's speed
    public void accelerate(int amount) {
        speed = speed + amount;
    }

    // Instance method - reads this object's data
    public String getInfo() {
        return brand + " traveling at " + speed + " km/h";
    }

    // Instance method - performs action using this object's state
    public boolean isSpeeding(int limit) {
        return speed > limit;
    }
}
```

### Calling Instance Methods

```java
Car myCar = new Car();
myCar.setBrand("Toyota");

myCar.accelerate(60);              // Modify state
String info = myCar.getInfo();     // Read state
boolean speeding = myCar.isSpeeding(50);  // Use state
```

---

## Understanding Constructors

### What Is a Constructor?

A **constructor** is a special method that initializes a new object. It:

1. Has the **same name as the class**
2. Has **no return type** (not even void)
3. Is called automatically when you use `new`
4. Sets up the initial state of the object

### The Default Constructor

If you don't write a constructor, Java provides a **default constructor**:

```java
public class Student {
    private String name;
    private int age;
    // No constructor written - Java provides default
}

// The default constructor does nothing special
Student s = new Student();  // name is null, age is 0
```

### Writing Your Own Constructor

```java
public class Student {
    private String name;
    private int age;

    // Constructor - initializes new Student objects
    public Student(String studentName, int studentAge) {
        name = studentName;
        age = studentAge;
    }
}

// Using the constructor
Student alice = new Student("Alice", 20);
// alice.name is "Alice", alice.age is 20
```

### Why Constructors Matter

Without constructors, you need multiple steps to set up an object:

```java
// Without proper constructor - tedious and error-prone
Student s = new Student();
s.setName("Alice");
s.setAge(20);
// Easy to forget a step!

// With constructor - clean and complete
Student s = new Student("Alice", 20);
// Object is ready to use immediately!
```

### Constructor Overloading

You can have multiple constructors with different parameters:

```java
public class Student {
    private String name;
    private int age;
    private String major;

    // Constructor with all parameters
    public Student(String name, int age, String major) {
        this.name = name;
        this.age = age;
        this.major = major;
    }

    // Constructor with just name and age
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
        this.major = "Undeclared";  // Default value
    }

    // Constructor with just name
    public Student(String name) {
        this.name = name;
        this.age = 18;              // Default value
        this.major = "Undeclared";  // Default value
    }
}

// All valid ways to create a Student
Student s1 = new Student("Alice", 20, "Computer Science");
Student s2 = new Student("Bob", 19);
Student s3 = new Student("Carol");
```

---

## Understanding the `this` Keyword

### What Is `this`?

The `this` keyword refers to **the current object** - the object on which a method is being called.

### Why Do We Need `this`?

Most commonly, to distinguish between:
- **Parameters** with the same name as **attributes**

```java
public class Student {
    private String name;  // Attribute

    // Without 'this' - confusing!
    public void setName(String name) {  // Parameter also called 'name'
        name = name;  // Which 'name' is which? This assigns parameter to itself!
    }

    // With 'this' - clear!
    public void setName(String name) {
        this.name = name;  // this.name is the attribute, name is the parameter
    }
}
```

### Using `this` in Constructors

```java
public class Car {
    private String brand;
    private String model;
    private int year;

    public Car(String brand, String model, int year) {
        this.brand = brand;  // Assign parameter 'brand' to attribute 'this.brand'
        this.model = model;  // Assign parameter 'model' to attribute 'this.model'
        this.year = year;    // Assign parameter 'year' to attribute 'this.year'
    }
}
```

### Reading `this`

- `this.name` means "the name attribute of THIS object"
- `this.getAge()` means "call getAge() on THIS object"
- Think of `this` as "me" - the object referring to itself

---

## Understanding the `toString()` Method

### What Is `toString()`?

Every class can have a `toString()` method that returns a String representation of the object. This is called automatically when you:

- Print the object: `System.out.println(myObject)`
- Concatenate with a String: `"Info: " + myObject`

### Without `toString()` - Unhelpful Output

```java
public class Student {
    private String name;
    private int age;

    // No toString() method
}

Student alice = new Student("Alice", 20);
System.out.println(alice);  // Prints: Student@15db9742 (memory address - useless!)
```

### With `toString()` - Meaningful Output

```java
public class Student {
    private String name;
    private int age;

    public String toString() {
        return "Student: " + name + ", Age: " + age;
    }
}

Student alice = new Student("Alice", 20);
System.out.println(alice);  // Prints: Student: Alice, Age: 20
```

### Writing Good `toString()` Methods

```java
public class Car {
    private String brand;
    private String model;
    private int year;
    private int speed;

    public String toString() {
        return year + " " + brand + " " + model + " (currently " + speed + " km/h)";
    }
}

Car myCar = new Car("Toyota", "Camry", 2020);
System.out.println(myCar);  // Prints: 2020 Toyota Camry (currently 0 km/h)
```

**Good `toString()` practices:**
- Include key identifying information
- Make it human-readable
- Keep it concise

---

## Understanding Object References

### Objects Are Different from Primitives

Remember from Week 6: arrays are **references**. Objects work the same way!

**Primitives** (int, double, boolean, char) hold the actual value:

```java
int x = 5;
int y = x;  // y gets a COPY of the value 5
x = 10;     // Changing x does NOT affect y
System.out.println(y);  // Still 5
```

**Objects** are accessed through references:

```java
Student s1 = new Student("Alice", 20);
Student s2 = s1;  // s2 points to the SAME object as s1!
s1.setAge(21);    // Change through s1
System.out.println(s2.getAge());  // Prints 21! Same object!
```

### Visualizing Object References

```
Primitives:
int x = 5;     x: [5]
int y = x;     y: [5]    (separate boxes, separate values)

Objects:
Student s1 = new Student("Alice", 20);

s1 -----> +------------------+
          | Student Object   |
          | name: "Alice"    |
          | age: 20          |
          +------------------+

Student s2 = s1;

s1 ----+
       |---> +------------------+
s2 ----+     | Student Object   |
             | name: "Alice"    |
             | age: 20          |
             +------------------+

Both s1 and s2 point to the SAME object!
```

### The `null` Reference

A reference can point to nothing, represented by `null`:

```java
Student alice = new Student("Alice", 20);  // alice points to an object
Student nobody = null;  // nobody points to nothing

System.out.println(alice.getName());   // Works fine: "Alice"
System.out.println(nobody.getName());  // ERROR! NullPointerException
```

Always check for null before using a reference if there is any chance it could be null.

### Comparing Objects

```java
Student s1 = new Student("Alice", 20);
Student s2 = new Student("Alice", 20);
Student s3 = s1;

// == compares REFERENCES (are they the same object?)
System.out.println(s1 == s2);  // false (different objects, same data)
System.out.println(s1 == s3);  // true (same object)

// To compare content, you need .equals() method (covered later)
```

---

## Understanding Static vs Instance (Introduction)

### The Two Types of Members

Classes can have two types of members:

1. **Instance members** - Belong to individual objects
2. **Static (class) members** - Belong to the class itself, shared by all objects

### Instance Members

```java
public class Car {
    private String color;    // Each car has its own color
    private int speed;       // Each car has its own speed

    public void accelerate(int amount) {  // Each car accelerates independently
        speed += amount;
    }
}
```

### Static Members

```java
public class Car {
    private static int totalCarsCreated = 0;  // Shared by ALL Car objects

    private String color;  // Instance - each car has its own

    public Car(String color) {
        this.color = color;
        totalCarsCreated++;  // Every new car increments the shared counter
    }

    public static int getTotalCars() {  // Static method - belongs to class
        return totalCarsCreated;
    }
}

// Usage:
Car car1 = new Car("Red");
Car car2 = new Car("Blue");
Car car3 = new Car("Green");

// Static member accessed on the CLASS, not objects
System.out.println(Car.getTotalCars());  // Prints 3
```

### When to Use Static

Use `static` for:
- Constants shared by all objects (`static final double PI = 3.14159`)
- Counters or trackers across all objects
- Utility methods that don't need object state

For now, most of your methods will be **instance methods**. You will learn more about when to use `static` as you gain experience.

---

## Understanding Packages

### What Are Packages?

**Packages** organize related classes into groups, like folders organize files.

```
myproject/
    animals/
        Dog.java
        Cat.java
        Bird.java
    vehicles/
        Car.java
        Truck.java
        Motorcycle.java
    people/
        Student.java
        Teacher.java
```

### Declaring a Package

At the top of each Java file:

```java
package animals;

public class Dog {
    // Dog class code
}
```

### Why Use Packages?

1. **Organization** - Group related classes together
2. **Avoid name conflicts** - Two packages can have classes with the same name
3. **Access control** - Some access modifiers work at package level
4. **Standard practice** - Professional Java code uses packages

### Package Naming Conventions

- Use lowercase letters
- Often based on organization domain (reversed): `com.company.project`
- Example: `dk.kea.programming.week7`

---

## Putting It All Together: Complete Examples

### Example 1: The Car Class

This is a core example that will be used throughout Weeks 7-10:

```java
/**
 * Represents a car with brand, model, year, and current speed.
 * This class demonstrates basic OOP concepts including:
 * - Private attributes
 * - Constructor initialization
 * - Getter and setter methods
 * - Instance methods for behavior
 * - toString for string representation
 */
public class Car {
    // Attributes (always private)
    private String brand;
    private String model;
    private int year;
    private int speed;  // Current speed in km/h

    // Constructor - initializes a new Car
    public Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.speed = 0;  // Cars start stationary
    }

    // Getters - read attribute values
    public String getBrand() {
        return brand;
    }

    public String getModel() {
        return model;
    }

    public int getYear() {
        return year;
    }

    public int getSpeed() {
        return speed;
    }

    // Behavior methods
    public void accelerate(int amount) {
        if (amount > 0) {
            speed += amount;
        }
    }

    public void brake(int amount) {
        speed -= amount;
        if (speed < 0) {
            speed = 0;  // Cannot have negative speed
        }
    }

    public void stop() {
        speed = 0;
    }

    public boolean isMoving() {
        return speed > 0;
    }

    // toString - string representation
    public String toString() {
        return year + " " + brand + " " + model + " @ " + speed + " km/h";
    }
}
```

**Using the Car class:**

```java
public class CarDemo {
    public static void main(String[] args) {
        // Create car objects
        Car myCar = new Car("Toyota", "Camry", 2020);
        Car friendsCar = new Car("Honda", "Civic", 2019);

        // Use the cars
        System.out.println(myCar);  // 2020 Toyota Camry @ 0 km/h

        myCar.accelerate(60);
        System.out.println(myCar);  // 2020 Toyota Camry @ 60 km/h

        myCar.brake(20);
        System.out.println(myCar);  // 2020 Toyota Camry @ 40 km/h

        System.out.println("Is my car moving? " + myCar.isMoving());  // true

        myCar.stop();
        System.out.println("Is my car moving? " + myCar.isMoving());  // false
    }
}
```

### Example 2: The Student Class

Another core example for the course:

```java
/**
 * Represents a student with name, age, and grade tracking.
 * Demonstrates arrays as attributes and methods that operate on object state.
 */
public class Student {
    // Attributes
    private String name;
    private int age;
    private int[] grades;
    private int gradeCount;  // How many grades have been added

    // Constructor
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
        this.grades = new int[100];  // Room for up to 100 grades
        this.gradeCount = 0;
    }

    // Getters
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    // Behavior methods
    public void addGrade(int grade) {
        if (gradeCount < grades.length && grade >= 0 && grade <= 100) {
            grades[gradeCount] = grade;
            gradeCount++;
        }
    }

    public double getAverage() {
        if (gradeCount == 0) {
            return 0.0;
        }
        int sum = 0;
        for (int i = 0; i < gradeCount; i++) {
            sum += grades[i];
        }
        return (double) sum / gradeCount;
    }

    public int getHighestGrade() {
        if (gradeCount == 0) {
            return -1;  // No grades
        }
        int highest = grades[0];
        for (int i = 1; i < gradeCount; i++) {
            if (grades[i] > highest) {
                highest = grades[i];
            }
        }
        return highest;
    }

    public boolean isPassing() {
        return getAverage() >= 60;
    }

    public String toString() {
        return name + " (Age: " + age + ", Avg: " +
               String.format("%.1f", getAverage()) + ")";
    }
}
```

### Example 3: The Die Class

A simple but powerful example for games:

```java
import java.util.Random;

/**
 * Represents a die (singular of dice) with configurable sides.
 * Can roll to get a random value between 1 and the number of sides.
 */
public class Die {
    // Attributes
    private int sides;
    private int currentValue;
    private Random random;

    // Constructor for standard 6-sided die
    public Die() {
        this.sides = 6;
        this.random = new Random();
        roll();  // Start with a random value
    }

    // Constructor for custom-sided die
    public Die(int sides) {
        if (sides < 2) {
            this.sides = 6;  // Default to 6 if invalid
        } else {
            this.sides = sides;
        }
        this.random = new Random();
        roll();
    }

    // Getters
    public int getSides() {
        return sides;
    }

    public int getValue() {
        return currentValue;
    }

    // Behavior
    public int roll() {
        currentValue = random.nextInt(sides) + 1;
        return currentValue;
    }

    public String toString() {
        return "Die [" + sides + " sides]: " + currentValue;
    }
}
```

**Using the Die class:**

```java
public class DiceGame {
    public static void main(String[] args) {
        // Create two standard dice
        Die die1 = new Die();
        Die die2 = new Die();

        // Roll and display
        die1.roll();
        die2.roll();

        System.out.println(die1);  // Die [6 sides]: 4 (random)
        System.out.println(die2);  // Die [6 sides]: 2 (random)

        int total = die1.getValue() + die2.getValue();
        System.out.println("Total: " + total);

        // Create a 20-sided die for D&D
        Die d20 = new Die(20);
        System.out.println("D20 roll: " + d20.roll());
    }
}
```

---

## Connecting to What You Already Know

### From Week 3: Loops

Your loop skills are essential for methods that process internal data:

```java
public class Student {
    private int[] grades;
    private int gradeCount;

    public double getAverage() {
        int sum = 0;
        // Your familiar for loop!
        for (int i = 0; i < gradeCount; i++) {
            sum += grades[i];
        }
        return (double) sum / gradeCount;
    }
}
```

### From Weeks 4-5: Methods

All your method skills transfer directly:

| Procedural (Weeks 4-5) | Object-Oriented (Week 7) |
|------------------------|--------------------------|
| `static` methods | Instance methods (no `static`) |
| Parameters passed in | Data stored in attributes |
| Return values | Return values (same!) |
| Method overloading | Constructor overloading |

```java
// Week 5: Static method
public static double calculateArea(double radius) {
    return Math.PI * radius * radius;
}

// Week 7: Instance method - uses object's own data
public class Circle {
    private double radius;

    public double calculateArea() {  // No parameter needed!
        return Math.PI * radius * radius;  // Uses this.radius
    }
}
```

### From Week 6: Arrays

Arrays become attributes inside classes:

```java
// Week 6: Standalone array with separate methods
int[] scores = {85, 92, 78};
int sum = calculateSum(scores);  // Pass array to method

// Week 7: Array as part of an object
public class Gradebook {
    private int[] scores;  // Array is an attribute

    public int getSum() {
        // Method operates on its own array
        int sum = 0;
        for (int score : scores) {
            sum += score;
        }
        return sum;
    }
}
```

### Understanding the Paradigm Shift

| Procedural (Weeks 1-6) | Object-Oriented (Week 7+) |
|------------------------|---------------------------|
| Data and functions are separate | Data and methods are bundled together |
| Functions operate on external data | Methods operate on internal state |
| `calculateArea(circle)` | `circle.calculateArea()` |
| Data can be changed by anyone | Data is protected (private) |
| Think: "What steps to perform?" | Think: "What objects exist? What can they do?" |

---

## Common Struggles and How to Overcome Them

### Struggle 1: Confusing Classes and Objects

**The confusion:** "Is `Student` the class or the object?"

**The solution:** Use this test:
- Can you have MULTIPLE of them? If yes, it is an **object**
- Is it a TEMPLATE/BLUEPRINT? If yes, it is the **class**

```java
Student alice = new Student("Alice", 20);
Student bob = new Student("Bob", 19);
```

- `Student` (without `new`) is the **class** - the blueprint
- `alice` and `bob` are **objects** - specific instances

**Remember:** You can have many houses (objects) from one blueprint (class).

### Struggle 2: Forgetting to Use `new`

**The confusion:** "Why is my object null?"

```java
Student alice;  // Declares variable but NO object exists!
alice.setName("Alice");  // NullPointerException!
```

**The solution:** Always use `new` to create objects:

```java
Student alice = new Student();  // Now an object exists
alice.setName("Alice");  // Works!
```

### Struggle 3: Mixing Up Static and Instance

**The confusion:** "When do I use `static`?"

**Simple rule for now:**
- Main method is always `static`
- Most other methods in your classes should NOT be `static`
- Attributes should almost never be `static`

```java
public class Student {
    private String name;  // Instance (no static) - each student has own name

    public String getName() {  // Instance (no static) - operates on this student
        return name;
    }

    public static void main(String[] args) {  // Static - entry point
        Student s = new Student();
    }
}
```

### Struggle 4: Understanding Object References

**The confusion:** "I changed s2 but s1 changed too!"

```java
Student s1 = new Student("Alice", 20);
Student s2 = s1;  // Both point to SAME object!
s2.setAge(25);    // Changes the ONE object both refer to
System.out.println(s1.getAge());  // 25! Same object!
```

**The solution:** Understand that `=` with objects copies the reference, not the object.

```
s1 ----+
       |---> [Student: Alice, 25]  (ONE object, TWO references)
s2 ----+
```

To have independent objects, use `new`:

```java
Student s1 = new Student("Alice", 20);
Student s2 = new Student("Alice", 20);  // Different object with same data
```

### Struggle 5: When to Create a Class vs Using Primitives

**The confusion:** "Do I really need a class for this?"

**Create a class when:**
- The concept has multiple pieces of data that belong together (Student has name + age + grades)
- The concept has behaviors (Student can calculate average)
- You need multiple instances (multiple students)

**Use primitives when:**
- It is a single, simple value (just an age, just a score)
- No associated behavior is needed

---

## Practice Exercises

### Exercise 1: Hello MyObject (meget hjalp - Maximum Guidance)

**Goal:** Practice creating a simple class with attributes and methods.

**Step-by-step instructions:**

1. Create a new Java file called `Person.java`
2. Add these private attributes: name (String), age (int)
3. Add a constructor that takes name and age
4. Add getter methods for both attributes
5. Add a `toString()` method
6. Create a `PersonDemo.java` to test your class

**Starter code:**

```java
// Person.java
public class Person {
    // Step 1: Declare private attributes
    private String name;
    private int age;

    // Step 2: Constructor
    public Person(String name, int age) {
        // TODO: Use 'this' to assign parameters to attributes
    }

    // Step 3: Getter for name
    public String getName() {
        // TODO: Return the name
        return null;
    }

    // Step 4: Getter for age
    public int getAge() {
        // TODO: Return the age
        return 0;
    }

    // Step 5: toString method
    public String toString() {
        // TODO: Return a string like "Person: Alice, 20 years old"
        return "";
    }
}
```

```java
// PersonDemo.java
public class PersonDemo {
    public static void main(String[] args) {
        // Create a Person object
        Person p1 = new Person("Alice", 20);

        // Test the methods
        System.out.println(p1.getName());  // Should print: Alice
        System.out.println(p1.getAge());   // Should print: 20
        System.out.println(p1);            // Should print: Person: Alice, 20 years old

        // Create another person
        Person p2 = new Person("Bob", 25);
        System.out.println(p2);            // Should print: Person: Bob, 25 years old
    }
}
```

### Exercise 2: My Kids (nogen hjalp - Moderate Guidance)

**Goal:** Practice creating multiple objects and working with their data.

**Instructions:**

Create a `Child` class with:
- Attributes: name, age, favoriteColor
- Constructor with all three parameters
- Getters for all attributes
- A method `describe()` that returns a description like "Emma is 8 years old and loves purple"
- toString method

Then create a demo that:
1. Creates at least 3 Child objects
2. Prints each child's description
3. Finds and prints the oldest child

**Hints:**
- Use a loop or manually compare ages
- Think about how to track "which child is oldest"

### Exercise 3: MyDie (ingen hjalp - Minimal Guidance)

**Goal:** Create a fully encapsulated dice class.

**Requirements:**

Create a `MyDie` class that:
- Has private attributes for number of sides and current value
- Has a constructor that accepts the number of sides (default to 6 if invalid)
- Has a `roll()` method that generates a random value and returns it
- Has a `getValue()` method to get the current value without rolling
- Has a `getSides()` method
- Has a meaningful `toString()` method

Create a demo program that:
1. Creates two 6-sided dice
2. Rolls them 10 times and prints each roll
3. Counts how many times doubles were rolled
4. Creates a 20-sided die (D20) and rolls it 5 times

**Challenge extension:**
- Add a method `rollUntil(int target)` that keeps rolling until the target is reached and returns how many rolls it took

---

## Looking Ahead

This week introduced the fundamental concepts of object-oriented programming. You now understand:
- The difference between classes (blueprints) and objects (instances)
- How to define state (attributes) and behavior (methods)
- How to create and use objects

**In the coming weeks, you will build on these foundations:**

- **Week 8 (Encapsulation):** You will learn WHY attributes are private and how to properly protect object state. You will also learn ArrayList, which is like a flexible, growable array for storing objects.

- **Week 9 (Inheritance and Polymorphism):** You will learn how to create relationships between classes, where one class inherits from another. A `SportsCar` could inherit from `Car`.

- **Week 10 (Advanced OOP Topics):** You will explore wrapper classes and additional OOP concepts.

The Car, Student, and Die classes you created this week will evolve through these topics. Keep them - you will be adding encapsulation, extending them with inheritance, and using them in more complex programs.

---

## Key Takeaways

- A **class** is a blueprint/template that defines attributes (data) and methods (behavior)
- An **object** is a specific instance created from a class using `new`
- **Attributes** (instance variables) store the object's state - always make them **private**
- **Methods** define what an object can do - instance methods operate on the object's data
- A **constructor** initializes new objects and has the same name as the class
- The **`this`** keyword refers to the current object - useful when parameter names match attribute names
- The **`toString()`** method returns a String representation of the object
- **Object references** work like array references - assignment creates aliases, not copies
- **Static** members belong to the class; **instance** members belong to objects
- **Packages** organize related classes into groups
- OOP bundles data and behavior together, unlike procedural programming which keeps them separate

---

## For the Next Topic Agent

### Terminology Established This Week

- **class**: A blueprint/template defining attributes and methods
- **object**: A specific instance created from a class
- **instance**: Another word for object - a concrete realization of a class
- **attribute/field/instance variable**: Data stored in an object
- **state**: The current values of an object's attributes
- **behavior**: The methods that define what an object can do
- **instantiation**: The process of creating an object using `new`
- **constructor**: Special method that initializes new objects
- **getter**: Method that returns the value of an attribute
- **setter**: Method that modifies the value of an attribute
- **`this`**: Keyword referring to the current object
- **`toString()`**: Method returning a String representation
- **object reference**: A variable that holds the address of an object
- **`null`**: A reference that points to no object
- **static**: Belonging to the class, shared by all objects
- **instance**: Belonging to individual objects
- **package**: Organizational grouping of related classes

### Example Classes Created

The following classes were established as recurring examples:

1. **Car** (brand, model, year, speed)
   - Demonstrates: attributes, constructor, getters, behavior methods, toString
   - Methods: accelerate(), brake(), stop(), isMoving()
   - Will be used in Week 8 for encapsulation (validation, speed limits)
   - Will be used in Week 9 for inheritance (SportsCar extends Car)

2. **Student** (name, age, grades array, gradeCount)
   - Demonstrates: arrays as attributes, methods operating on internal data
   - Methods: addGrade(), getAverage(), getHighestGrade(), isPassing()
   - Will be used in Week 8 with ArrayList instead of array
   - Will be used in Week 9 for inheritance (GraduateStudent extends Student)

3. **Die** (sides, currentValue, Random)
   - Demonstrates: constructor overloading, Random usage, encapsulation preview
   - Methods: roll(), getValue(), getSides()
   - Will be used throughout for game examples

### Student Capabilities After This Week

Students can now:
- Explain the difference between a class and an object
- Create classes with private attributes
- Write constructors to initialize objects
- Implement getter and setter methods
- Write instance methods that operate on object state
- Use the `this` keyword correctly
- Implement toString() for object representation
- Create multiple objects from one class
- Understand that object variables hold references
- Use packages for basic organization
- Recognize static vs instance members (basic understanding)

### Pedagogical Patterns Established

- **Blueprint/House analogy**: Class is the blueprint, objects are houses
- **Cookie cutter analogy**: Class is the cutter, objects are cookies
- **Car factory analogy**: Class is the specification, objects are actual cars
- **Multiple analogies approach**: OOP concepts need multiple explanations
- **Core examples**: Car, Student, Die - used throughout remaining weeks
- **Progressive complexity**: Simple Person -> Child -> Die with Random
- **Emphasis on WHY**: Why private? Why classes? Why OOP?

### Critical Connections for Week 8 (Encapsulation)

Week 8 should build directly on:
- The Car class with its speed attribute - add validation (no negative speed, max speed limit)
- The Student class - convert grades array to ArrayList
- The Die class - already demonstrates good encapsulation

Key concepts to reinforce:
- WHY attributes are private (introduced here, explained deeply in Week 8)
- Constructor overloading (from Week 5 method overloading)
- The relationship between getters/setters and encapsulation
- ArrayList as an evolution of arrays for object storage

### Student Misconceptions to Address in Week 8

- "If attributes are private, how do I use them?" - Week 8 deepens getters/setters
- "Why can't I just make everything public?" - Week 8 shows the dangers
- "What's wrong with using arrays for everything?" - ArrayList introduction
- Static vs instance still confusing - reinforce with more examples
- Object references and aliasing - continue to reinforce
