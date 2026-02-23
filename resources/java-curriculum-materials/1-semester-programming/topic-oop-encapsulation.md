# OOP Part 2: Encapsulation and Data Hiding - Week 8

*Prerequisites: Week 7 - OOP Part 1: Classes and Objects*
*Phase: Phase 3: Object-Oriented Thinking*

---

## What You'll Learn

By the end of this week, you will be able to:

- **Understand encapsulation** as the bundling of data with methods that operate on that data
- **Explain why attributes must be private** and the dangers of public fields
- **Apply access modifiers** correctly: private, public (and awareness of protected, package-private)
- **Design getter methods** (accessors) that safely return attribute values
- **Design setter methods** (mutators) with proper validation
- **Implement class invariants** - rules that must always be true about your objects
- **Write robust constructors** including default, parameterized, and overloaded versions
- **Use constructor chaining** with `this()` to reduce code duplication
- **Master the `this` keyword** for disambiguation and constructor chaining
- **Understand shadowing** when local variables hide instance variables
- **Work with enum types** that have attributes and getters
- **Use ArrayList** as a flexible alternative to arrays

**CRITICAL EXAM REQUIREMENT**: ALL attributes MUST be private - no exceptions! This is non-negotiable in your assessments.

This week transforms your Week 7 classes from "working" to "properly designed." You will learn to protect your objects from invalid states and create classes that are safe to use.

---

## Why This Matters

### The Problem with Unprotected Data

Last week, you created classes with private attributes. But did you really understand *why* they must be private? Let's see what happens when they are not:

```java
// DANGEROUS: Public attributes (NEVER do this!)
public class Car {
    public String brand;
    public String model;
    public int year;
    public int speed;
}
```

This seems simpler - no getters or setters needed! But watch what happens:

```java
Car myCar = new Car();
myCar.brand = "Toyota";
myCar.speed = -500;        // Negative speed? Cars can't do that!
myCar.speed = 999999;      // Speed of light? Impossible!
myCar.year = -2000;        // Year before cars existed!
myCar.model = null;        // Oops, now we have broken data
```

**With public attributes, ANYONE can put your object into an invalid, impossible, or broken state.** Your Car object now represents something that cannot exist in reality.

### How Encapsulation Solves This

```java
// SAFE: Private attributes with controlled access
public class Car {
    private String brand;
    private String model;
    private int year;
    private int speed;

    public void setSpeed(int newSpeed) {
        if (newSpeed >= 0 && newSpeed <= 300) {  // Validate!
            speed = newSpeed;
        }
        // If invalid, speed stays unchanged - object stays valid
    }
}
```

Now the `Car` class CONTROLS how its data changes. Invalid values are rejected. The object always represents a real, possible car.

### This Is How Professional Software Works

Every Java application you use relies on encapsulation:

- **Banking apps**: Cannot directly set account.balance = 1000000 (nice try!)
- **Games**: Cannot set player.health = 99999 or enemy.isAlive = false
- **Social media**: Cannot directly modify post.likeCount or user.followerCount
- **Your phone**: Cannot set battery.level = 200 or signal.strength = -50

Encapsulation ensures data integrity. Without it, software would be unreliable and hackable.

---

## Building Your Intuition

### The Phone Interface Analogy

This is the most important analogy for understanding encapsulation. Take your smartphone:

**What You See (The Interface)**
- A touchscreen to tap
- Buttons to press (volume, power)
- Settings you can adjust
- Apps you can use

**What You Cannot See (The Implementation)**
- The CPU processing your inputs
- The memory storing your data
- The radio waves connecting to networks
- The battery management system
- Thousands of software processes

**Why This Design Works:**

1. **You don't NEED to know** how the phone internally manages calls - you just tap "Call"
2. **You CAN'T break** the internal circuitry by tapping the screen wrong
3. **Apple/Samsung can CHANGE** the internal hardware without changing how you use the phone
4. **The phone PROTECTS itself** - you can't tell it to use 500% battery or receive signals that don't exist

```
+------------------------------------------------------+
|                    YOUR PHONE                         |
|                                                       |
|   INTERFACE (public)        IMPLEMENTATION (private)  |
|   ==================        =======================   |
|   [Touchscreen]             CPU, Memory, Radio,       |
|   [Volume Button]    ->     Battery Management,       |
|   [Settings App]            Network Protocols,        |
|   [Phone App]               Signal Processing,        |
|                             Encryption Systems...     |
|                                                       |
|   You interact here         Hidden and protected      |
+------------------------------------------------------+
```

**In Java terms:**
- The **interface** is your `public` methods - what other code can use
- The **implementation** is your `private` attributes and helper methods - hidden inside
- **Encapsulation** is this separation of "what you can do" from "how it's done"

### The Thermostat Analogy

Think of a home thermostat:

**What You Can Do (Interface)**
- Set desired temperature (within limits, e.g., 15-30 degrees Celsius)
- Turn heating/cooling on or off
- View current temperature

**What You Cannot Do**
- Set temperature to 1000 degrees (thermostat rejects this)
- Access the internal temperature sensor directly
- Bypass the safety limits
- Tell the thermostat to heat AND cool simultaneously

```java
public class Thermostat {
    private double currentTemp;     // Only thermostat knows actual temp
    private double targetTemp;      // Controlled by setter
    private boolean heatingOn;      // Internal state

    public void setTargetTemp(double temp) {
        // VALIDATES input - protects the system
        if (temp >= 15 && temp <= 30) {
            targetTemp = temp;
        }
        // Invalid temperatures are simply ignored
    }

    public double getTargetTemp() {
        return targetTemp;  // Safe to read
    }

    // No setCurrentTemp() - only the sensor can change this!
}
```

### The Bank Vault Analogy

Consider a bank vault:

**Public Access (The Interface)**
- Tellers who can help you
- Forms to fill out for deposits/withdrawals
- ATM machines with controlled access

**Private (The Implementation)**
- The actual vault with money
- Security systems
- Transaction records

You cannot walk into the vault and take money directly. You must go through the proper channels (tellers, ATMs), which:
1. Verify your identity
2. Check your balance
3. Ensure you have permission
4. Record the transaction
5. Only THEN give you money

This is exactly how encapsulated classes work - controlled access through defined methods.

---

## Understanding Access Modifiers

### What Are Access Modifiers?

**Access modifiers** are keywords that control WHO can access (see, use, modify) parts of your class. They are the locks on your doors.

### The Four Access Levels

| Modifier | Same Class | Same Package | Subclass | Everywhere |
|----------|------------|--------------|----------|------------|
| `private` | Yes | No | No | No |
| (none/package-private) | Yes | Yes | No | No |
| `protected` | Yes | Yes | Yes | No |
| `public` | Yes | Yes | Yes | Yes |

### For This Course: Focus on Private and Public

**`private`** - Only accessible within the same class

```java
public class Student {
    private String name;  // Only Student class can access

    public void printName() {
        System.out.println(name);  // OK - same class
    }
}

// In another class:
Student s = new Student();
System.out.println(s.name);  // ERROR! name is private
```

**`public`** - Accessible from anywhere

```java
public class Student {
    private String name;

    public String getName() {  // Anyone can call this
        return name;
    }
}

// In another class:
Student s = new Student();
System.out.println(s.getName());  // OK - getName() is public
```

### Why Private for Attributes, Public for Methods?

Think of it this way:

- **Private attributes** = Your personal thoughts, your wallet, your diary
- **Public methods** = How you interact with the world, what you let others do

You don't let strangers directly access your wallet. But you might let them ASK you to buy something, and YOU decide whether to open your wallet.

```java
public class Person {
    private double moneyInWallet;  // Private - it's MY wallet

    // Public - you can ASK me to spend money
    public void buyItem(double price) {
        if (price <= moneyInWallet && price > 0) {  // I decide if I can afford it
            moneyInWallet -= price;
        }
    }

    // Public - you can see how much I have (if I choose to tell you)
    public double getMoney() {
        return moneyInWallet;
    }

    // NO setMoney() - you can't just put money in my wallet or take it out!
}
```

### EXAM RULE: All Attributes Must Be Private

**This is not optional.** On your exam:

```java
// CORRECT - will pass
public class Car {
    private String brand;
    private int speed;
}

// WRONG - will lose marks
public class Car {
    public String brand;   // WRONG!
    int speed;             // WRONG! (package-private)
}
```

No exceptions. No excuses. Every single attribute is `private`.

---

## Understanding Getters (Accessor Methods)

### What Is a Getter?

A **getter** (also called an **accessor method**) is a method that returns the value of a private attribute. It's how you let others READ your data without giving them direct access.

### Why "Getter"?

The method "gets" a value for you. By convention, getter names start with `get` followed by the attribute name:

- `name` attribute -> `getName()` getter
- `age` attribute -> `getAge()` getter
- `speed` attribute -> `getSpeed()` getter

### Exception: Boolean Getters Use "is"

For `boolean` attributes, use `is` instead of `get`:

- `moving` attribute -> `isMoving()` (not `getMoving()`)
- `active` attribute -> `isActive()` (not `getActive()`)
- `passing` attribute -> `isPassing()` (not `getPassing()`)

### Writing Basic Getters

```java
public class Student {
    private String name;
    private int age;
    private boolean passing;

    // Getter for String attribute
    public String getName() {
        return name;
    }

    // Getter for int attribute
    public int getAge() {
        return age;
    }

    // Getter for boolean attribute (uses "is")
    public boolean isPassing() {
        return passing;
    }
}
```

### The Pattern

Every getter follows this exact pattern:

```java
public <returnType> get<AttributeName>() {
    return <attributeName>;
}
```

Or for booleans:

```java
public boolean is<AttributeName>() {
    return <attributeName>;
}
```

### Why Not Just Make Attributes Public?

"But getters just return the value anyway - why not make the attribute public?"

Here's why getters are better:

**1. You can add behavior later without changing the interface:**

```java
// Version 1: Simple getter
public int getAge() {
    return age;
}

// Version 2: Later you add logging
public int getAge() {
    System.out.println("Age was accessed");  // Added behavior!
    return age;
}

// Version 3: Later you calculate from birthdate
public int getAge() {
    return currentYear - birthYear;  // Changed implementation!
}
```

If `age` were public, any code using `student.age` would break when you change to calculating from birthdate.

**2. You can control WHAT is returned:**

```java
public class BankAccount {
    private String accountNumber;  // e.g., "1234567890"

    // Return a masked version for security
    public String getAccountNumber() {
        return "******" + accountNumber.substring(6);  // Returns "******7890"
    }
}
```

**3. You can make attributes read-only:**

```java
public class Student {
    private final String studentId;  // Set once in constructor

    public String getStudentId() {
        return studentId;  // Can read, but no setter = cannot change
    }
    // No setStudentId() - the ID is permanent!
}
```

---

## Understanding Setters (Mutator Methods)

### What Is a Setter?

A **setter** (also called a **mutator method**) is a method that modifies the value of a private attribute. It's how you let others CHANGE your data in a controlled way.

### Why "Setter"?

The method "sets" a new value. By convention, setter names start with `set` followed by the attribute name:

- `name` attribute -> `setName(String name)`
- `age` attribute -> `setAge(int age)`
- `speed` attribute -> `setSpeed(int speed)`

### The Critical Feature: Validation

The whole POINT of setters is that they can **validate** the input before accepting it:

```java
public class Car {
    private int speed;

    // Setter WITH validation
    public void setSpeed(int newSpeed) {
        // Only accept valid speeds
        if (newSpeed >= 0 && newSpeed <= 300) {
            speed = newSpeed;
        }
        // If invalid, do nothing - speed stays as it was
    }
}
```

Compare this to public attributes:

```java
// With public attribute (BAD):
car.speed = -500;  // Accepted! Car is now in invalid state

// With setter (GOOD):
car.setSpeed(-500);  // Rejected! Car stays valid
```

### Setter Validation Patterns

**Pattern 1: Ignore Invalid Values (Silent Rejection)**

```java
public void setAge(int newAge) {
    if (newAge >= 0 && newAge <= 150) {
        age = newAge;
    }
    // Invalid ages are simply ignored
}
```

**Pattern 2: Use Default for Invalid Values**

```java
public void setAge(int newAge) {
    if (newAge >= 0 && newAge <= 150) {
        age = newAge;
    } else {
        age = 0;  // Default value for invalid input
    }
}
```

**Pattern 3: Clamp to Valid Range**

```java
public void setSpeed(int newSpeed) {
    if (newSpeed < 0) {
        speed = 0;        // Minimum
    } else if (newSpeed > 300) {
        speed = 300;      // Maximum
    } else {
        speed = newSpeed; // Valid, use as-is
    }
}
```

**Pattern 4: Throw an Exception (Week 12 topic)**

```java
public void setAge(int newAge) {
    if (newAge < 0 || newAge > 150) {
        throw new IllegalArgumentException("Age must be 0-150");
    }
    age = newAge;
}
```

### Not All Attributes Need Setters

Some attributes should NEVER be changed after creation:

```java
public class Student {
    private final String studentId;  // Set once, never changed
    private String name;             // Can be changed (marriage, etc.)
    private int graduationYear;      // Set once in constructor

    public Student(String studentId, String name, int gradYear) {
        this.studentId = studentId;
        this.name = name;
        this.graduationYear = gradYear;
    }

    // Getter for studentId (no setter - ID is permanent)
    public String getStudentId() {
        return studentId;
    }

    // Getter AND setter for name (name can change)
    public String getName() {
        return name;
    }

    public void setName(String newName) {
        if (newName != null && !newName.isEmpty()) {
            name = newName;
        }
    }

    // Getter for graduationYear (no setter - graduation year is set)
    public int getGraduationYear() {
        return graduationYear;
    }
}
```

### Common Setter Validations

| Attribute Type | Common Validations |
|----------------|-------------------|
| Age | >= 0, <= 150 (or reasonable max) |
| Name | Not null, not empty |
| Speed | >= 0, <= maxSpeed |
| Grade | 0-100 or valid grade scale |
| Year | >= minYear, <= currentYear (or max) |
| Price | > 0 |
| Quantity | >= 0 |

---

## Transforming Week 7's Car Class

Let's evolve the Car class from Week 7 into a properly encapsulated class:

### Before (Week 7 Basic Version)

```java
public class Car {
    private String brand;
    private String model;
    private int year;
    private int speed;

    public Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.speed = 0;
    }

    public void accelerate(int amount) {
        speed += amount;  // No validation!
    }

    public int getSpeed() {
        return speed;
    }
}
```

**Problems:**
- `accelerate(-100)` works - but you can't accelerate negatively!
- `accelerate(10000)` works - no speed limit!
- No way to set maximum speed per car type
- Constructor accepts any year, even -5000

### After (Week 8 Encapsulated Version)

```java
/**
 * Represents a car with proper encapsulation.
 * All attributes are private with controlled access.
 * Invariants:
 * - Speed is always 0 <= speed <= maxSpeed
 * - Year is always 1886 <= year <= current year
 * - Brand and model are never null
 */
public class Car {
    // Class constant for validation
    private static final int FIRST_CAR_YEAR = 1886;  // First car invented
    private static final int MAX_REASONABLE_SPEED = 400;  // km/h

    // Private attributes (always!)
    private String brand;
    private String model;
    private int year;
    private int speed;
    private int maxSpeed;  // New: each car has its own max speed

    // Constructor with validation
    public Car(String brand, String model, int year, int maxSpeed) {
        // Validate and set brand
        if (brand == null || brand.isEmpty()) {
            this.brand = "Unknown";
        } else {
            this.brand = brand;
        }

        // Validate and set model
        if (model == null || model.isEmpty()) {
            this.model = "Unknown";
        } else {
            this.model = model;
        }

        // Validate and set year
        int currentYear = java.time.Year.now().getValue();
        if (year < FIRST_CAR_YEAR) {
            this.year = FIRST_CAR_YEAR;
        } else if (year > currentYear + 1) {  // Allow next year's models
            this.year = currentYear;
        } else {
            this.year = year;
        }

        // Validate and set maxSpeed
        if (maxSpeed < 0) {
            this.maxSpeed = 200;  // Default
        } else if (maxSpeed > MAX_REASONABLE_SPEED) {
            this.maxSpeed = MAX_REASONABLE_SPEED;
        } else {
            this.maxSpeed = maxSpeed;
        }

        // Speed always starts at 0
        this.speed = 0;
    }

    // Convenience constructor (common case)
    public Car(String brand, String model, int year) {
        this(brand, model, year, 200);  // Default maxSpeed of 200 km/h
    }

    // Getters (safe to read any time)
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

    public int getMaxSpeed() {
        return maxSpeed;
    }

    // Boolean getter
    public boolean isMoving() {
        return speed > 0;
    }

    // Behavior methods with validation
    public void accelerate(int amount) {
        if (amount > 0) {  // Can only accelerate by positive amounts
            speed += amount;
            if (speed > maxSpeed) {
                speed = maxSpeed;  // Cap at max speed
            }
        }
    }

    public void brake(int amount) {
        if (amount > 0) {  // Can only brake by positive amounts
            speed -= amount;
            if (speed < 0) {
                speed = 0;  // Can't have negative speed
            }
        }
    }

    public void stop() {
        speed = 0;
    }

    // No setSpeed() - speed can only change through accelerate/brake
    // No setBrand(), setModel(), setYear() - these are fixed after creation

    public String toString() {
        return year + " " + brand + " " + model +
               " (speed: " + speed + "/" + maxSpeed + " km/h)";
    }
}
```

### Using the Encapsulated Car Class

```java
public class CarDemo {
    public static void main(String[] args) {
        // Create a car
        Car myCar = new Car("Toyota", "Camry", 2020, 180);

        // Try to break it - you can't!
        myCar.accelerate(-50);  // Ignored - can't accelerate negatively
        System.out.println(myCar.getSpeed());  // Still 0

        myCar.accelerate(100);
        System.out.println(myCar.getSpeed());  // 100

        myCar.accelerate(200);  // Tries to go to 300
        System.out.println(myCar.getSpeed());  // Capped at 180 (maxSpeed)

        myCar.brake(50);
        System.out.println(myCar.getSpeed());  // 130

        myCar.brake(500);  // Tries to go to -370
        System.out.println(myCar.getSpeed());  // Capped at 0

        // Invalid construction values are handled
        Car weirdCar = new Car(null, "", -1000, 9999);
        System.out.println(weirdCar);
        // Prints: 1886 Unknown Unknown (speed: 0/400 km/h)
    }
}
```

The class is now **bulletproof** - no matter how you try to misuse it, the Car object always represents a valid car.

---

## Understanding Class Invariants

### What Is a Class Invariant?

A **class invariant** is a condition that is ALWAYS true for every object of the class, at all times after construction. It's a promise your class makes.

### Examples of Class Invariants

**Car class invariants:**
- Speed is always between 0 and maxSpeed (inclusive)
- Year is always between 1886 and currentYear+1
- Brand and model are never null

**Student class invariants:**
- Age is always between 0 and 150
- Name is never null or empty
- GPA is always between 0.0 and 4.0

**BankAccount class invariants:**
- Balance is always >= 0 (no overdraft allowed)
- AccountNumber never changes after creation

### How to Maintain Invariants

1. **Validate in constructors** - Objects start in a valid state
2. **Validate in setters** - Changes maintain validity
3. **Control how values change** - Only allow valid transitions
4. **Document your invariants** - So others know what to expect

```java
/**
 * Represents a student's grade (0-100).
 *
 * Class invariant: score is always 0 <= score <= 100
 */
public class Grade {
    private int score;

    public Grade(int score) {
        // Ensure invariant from creation
        if (score < 0) {
            this.score = 0;
        } else if (score > 100) {
            this.score = 100;
        } else {
            this.score = score;
        }
    }

    public void setScore(int newScore) {
        // Maintain invariant during modification
        if (newScore >= 0 && newScore <= 100) {
            score = newScore;
        }
        // Invalid values rejected - invariant preserved
    }

    public int getScore() {
        return score;
    }
}
```

---

## Understanding Constructors (Deep Dive)

In Week 7, you learned the basics of constructors. Now let's master them.

### What Makes Constructors Special?

Constructors are different from regular methods:

| Regular Method | Constructor |
|----------------|-------------|
| Has a return type | No return type (not even void) |
| Any name | Must match class name exactly |
| Called explicitly | Called automatically with `new` |
| Can be called many times | Called once per object creation |

### The Default Constructor

If you write NO constructor, Java provides a **default constructor** that does nothing:

```java
public class Student {
    private String name;
    private int age;
    // No constructor written
}

// Java secretly adds:
// public Student() { }

Student s = new Student();  // Works! Uses default constructor
// But s.name is null and s.age is 0
```

**Important:** If you write ANY constructor, Java stops providing the default:

```java
public class Student {
    private String name;
    private int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

Student s = new Student();  // ERROR! No matching constructor
Student s = new Student("Alice", 20);  // Works!
```

### Constructor Overloading

Like method overloading, you can have multiple constructors with different parameters:

```java
public class Student {
    private String name;
    private int age;
    private String major;

    // Constructor 1: All parameters
    public Student(String name, int age, String major) {
        this.name = name;
        this.age = age;
        this.major = major;
    }

    // Constructor 2: Name and age only
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
        this.major = "Undeclared";  // Default value
    }

    // Constructor 3: Name only
    public Student(String name) {
        this.name = name;
        this.age = 18;              // Default value
        this.major = "Undeclared";  // Default value
    }

    // Constructor 4: No parameters (default-like)
    public Student() {
        this.name = "Unknown";
        this.age = 18;
        this.major = "Undeclared";
    }
}

// All valid:
Student s1 = new Student("Alice", 20, "Computer Science");
Student s2 = new Student("Bob", 21);      // major = "Undeclared"
Student s3 = new Student("Carol");        // age = 18, major = "Undeclared"
Student s4 = new Student();               // All defaults
```

### Constructor Chaining with `this()`

Notice the repeated code in the constructors above? We can eliminate it using `this()`:

```java
public class Student {
    private String name;
    private int age;
    private String major;

    // Primary constructor - all the validation and assignment happens here
    public Student(String name, int age, String major) {
        // Validate name
        if (name == null || name.isEmpty()) {
            this.name = "Unknown";
        } else {
            this.name = name;
        }

        // Validate age
        if (age < 0 || age > 150) {
            this.age = 18;
        } else {
            this.age = age;
        }

        // Validate major
        if (major == null || major.isEmpty()) {
            this.major = "Undeclared";
        } else {
            this.major = major;
        }
    }

    // Chain to primary constructor - provide default for major
    public Student(String name, int age) {
        this(name, age, "Undeclared");  // Calls 3-parameter constructor
    }

    // Chain to 2-parameter constructor - provide defaults for age and major
    public Student(String name) {
        this(name, 18);  // Calls 2-parameter constructor
    }

    // Chain to 1-parameter constructor - all defaults
    public Student() {
        this("Unknown");  // Calls 1-parameter constructor
    }
}
```

**Benefits of constructor chaining:**
1. Validation logic is in ONE place (the primary constructor)
2. Changes to validation only need to be made once
3. Less code duplication
4. Fewer bugs

**Rules for `this()`:**
1. Must be the FIRST statement in the constructor
2. Can only call ONE other constructor
3. Prevents infinite recursion (A calls B calls A...)

### Validation in Constructors

Constructors should ensure objects start in a valid state:

```java
public class Die {
    private int sides;
    private int currentValue;
    private java.util.Random random;

    public Die(int sides) {
        // Validate: dice must have at least 2 sides
        if (sides < 2) {
            this.sides = 6;  // Default to standard die
        } else {
            this.sides = sides;
        }

        this.random = new java.util.Random();
        roll();  // Ensure currentValue is valid from start
    }

    public Die() {
        this(6);  // Default: 6-sided die
    }

    public int roll() {
        currentValue = random.nextInt(sides) + 1;
        return currentValue;
    }

    public int getValue() {
        return currentValue;
    }

    public int getSides() {
        return sides;
    }
}
```

---

## Mastering the `this` Keyword

### Uses of `this`

The `this` keyword has three main uses:

**1. Disambiguate attribute from parameter (most common):**

```java
public class Student {
    private String name;

    public Student(String name) {  // Parameter has same name as attribute
        this.name = name;  // this.name = attribute, name = parameter
    }

    public void setName(String name) {
        this.name = name;  // Same pattern
    }
}
```

**2. Call another constructor (constructor chaining):**

```java
public class Student {
    private String name;
    private int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public Student(String name) {
        this(name, 18);  // Calls the 2-parameter constructor
    }
}
```

**3. Pass the current object as an argument:**

```java
public class Student {
    private String name;

    public void printMe(Printer printer) {
        printer.print(this);  // Pass this Student object to printer
    }
}
```

### Understanding Shadowing

**Shadowing** occurs when a local variable (or parameter) has the same name as an instance variable. The local variable "shadows" (hides) the instance variable.

```java
public class Student {
    private String name = "Original";  // Instance variable

    public void confusingMethod(String name) {  // Parameter shadows attribute
        System.out.println(name);       // Prints the PARAMETER
        System.out.println(this.name);  // Prints the ATTRIBUTE
    }

    public void moreConfusion() {
        String name = "Local";  // Local variable shadows attribute
        System.out.println(name);       // Prints "Local"
        System.out.println(this.name);  // Prints "Original"
    }
}
```

**Rule:** Always use `this.` when you want the instance variable, especially when there's any possibility of shadowing.

### Best Practice: Consistent Use of `this`

Some programmers use `this.` for ALL attribute access, even without shadowing:

```java
public class Student {
    private String name;
    private int age;

    // Consistent use of 'this' - always clear what's an attribute
    public String getDetails() {
        return this.name + " is " + this.age + " years old";
    }
}
```

This makes code more readable because it's always obvious which variables are attributes.

---

## Enum Types with Attributes

### What Is an Enum?

An **enum** (enumeration) is a special type that represents a fixed set of constants. You've seen simple enums:

```java
public enum Day {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
}
```

### Enums Can Have Attributes!

Enums become powerful when you add attributes:

```java
public enum Suit {
    HEARTS("Hearts", "Red"),
    DIAMONDS("Diamonds", "Red"),
    CLUBS("Clubs", "Black"),
    SPADES("Spades", "Black");

    // Attributes
    private final String name;
    private final String color;

    // Constructor (always private for enums)
    Suit(String name, String color) {
        this.name = name;
        this.color = color;
    }

    // Getters
    public String getName() {
        return name;
    }

    public String getColor() {
        return color;
    }
}
```

### Using Enums with Attributes

```java
public class Card {
    private Suit suit;
    private int value;  // 1-13 (Ace=1, Jack=11, Queen=12, King=13)

    public Card(Suit suit, int value) {
        this.suit = suit;
        if (value < 1 || value > 13) {
            this.value = 1;
        } else {
            this.value = value;
        }
    }

    public boolean isRed() {
        return suit.getColor().equals("Red");
    }

    public String toString() {
        String valueName;
        switch (value) {
            case 1:  valueName = "Ace"; break;
            case 11: valueName = "Jack"; break;
            case 12: valueName = "Queen"; break;
            case 13: valueName = "King"; break;
            default: valueName = String.valueOf(value);
        }
        return valueName + " of " + suit.getName();
    }
}

// Usage:
Card card = new Card(Suit.HEARTS, 12);
System.out.println(card);  // "Queen of Hearts"
System.out.println(card.isRed());  // true
```

### Enum Example: Grade Scale

```java
public enum DanishGrade {
    MINUS_THREE(-3, "Unacceptable"),
    ZERO(0, "Inadequate"),
    TWO(2, "Adequate"),
    FOUR(4, "Fair"),
    SEVEN(7, "Good"),
    TEN(10, "Excellent"),
    TWELVE(12, "Outstanding");

    private final int value;
    private final String description;

    DanishGrade(int value, String description) {
        this.value = value;
        this.description = description;
    }

    public int getValue() {
        return value;
    }

    public String getDescription() {
        return description;
    }

    public boolean isPassing() {
        return value >= 2;
    }
}
```

---

## ArrayList Introduction

### The Problem with Arrays

Remember your Student class with grades? Arrays have limitations:

```java
public class Student {
    private int[] grades;       // Fixed size!
    private int gradeCount;     // Manual tracking

    public Student() {
        grades = new int[100];  // What if student has 101 grades?
        gradeCount = 0;         // Have to track manually
    }

    public void addGrade(int grade) {
        if (gradeCount < grades.length) {  // Manual bounds checking
            grades[gradeCount] = grade;
            gradeCount++;
        }
        // If full, grade is silently lost!
    }
}
```

### ArrayList: A Flexible Array

`ArrayList` is a class that works like an array but:
- **Grows automatically** when you add elements
- **Tracks size** automatically
- **Has helpful methods** for adding, removing, searching

### Basic ArrayList Usage

```java
import java.util.ArrayList;

public class ArrayListDemo {
    public static void main(String[] args) {
        // Create an ArrayList that holds Strings
        ArrayList<String> names = new ArrayList<>();

        // Add elements (grows automatically!)
        names.add("Alice");
        names.add("Bob");
        names.add("Carol");

        // Get size
        System.out.println("Size: " + names.size());  // 3

        // Access by index
        System.out.println(names.get(0));  // "Alice"
        System.out.println(names.get(1));  // "Bob"

        // Change an element
        names.set(1, "Barbara");

        // Remove an element
        names.remove("Carol");  // Remove by value
        names.remove(0);        // Remove by index

        // Check if contains
        System.out.println(names.contains("Barbara"));  // true

        // Iterate with for-each
        for (String name : names) {
            System.out.println(name);
        }
    }
}
```

### The Generic Type `<Type>`

The `<String>` in `ArrayList<String>` is called a **generic type parameter**. It tells Java what type of objects the ArrayList will hold:

```java
ArrayList<String> names = new ArrayList<>();      // Holds Strings
ArrayList<Integer> numbers = new ArrayList<>();   // Holds Integers (not int!)
ArrayList<Student> students = new ArrayList<>();  // Holds Student objects
ArrayList<Car> cars = new ArrayList<>();          // Holds Car objects
```

**Note:** You cannot use primitive types (`int`, `double`, `boolean`) directly. Use wrapper classes instead:
- `int` -> `Integer`
- `double` -> `Double`
- `boolean` -> `Boolean`

### ArrayList for Student Grades

Let's improve our Student class:

```java
import java.util.ArrayList;

public class Student {
    private String name;
    private int age;
    private ArrayList<Integer> grades;  // Flexible size!

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
        this.grades = new ArrayList<>();  // Empty list to start
    }

    public void addGrade(int grade) {
        if (grade >= 0 && grade <= 100) {
            grades.add(grade);  // Automatically grows!
        }
    }

    public double getAverage() {
        if (grades.isEmpty()) {
            return 0.0;
        }
        int sum = 0;
        for (int grade : grades) {  // Enhanced for loop works!
            sum += grade;
        }
        return (double) sum / grades.size();
    }

    public int getGradeCount() {
        return grades.size();  // No manual tracking needed!
    }

    public int getHighestGrade() {
        if (grades.isEmpty()) {
            return -1;
        }
        int highest = grades.get(0);
        for (int grade : grades) {
            if (grade > highest) {
                highest = grade;
            }
        }
        return highest;
    }
}
```

### Common ArrayList Methods

| Method | Description | Example |
|--------|-------------|---------|
| `add(element)` | Add to end | `names.add("Alice")` |
| `add(index, element)` | Insert at position | `names.add(0, "First")` |
| `get(index)` | Get element at index | `names.get(0)` |
| `set(index, element)` | Replace element | `names.set(0, "New")` |
| `remove(index)` | Remove by index | `names.remove(0)` |
| `remove(object)` | Remove first occurrence | `names.remove("Alice")` |
| `size()` | Get number of elements | `names.size()` |
| `isEmpty()` | Check if empty | `names.isEmpty()` |
| `contains(object)` | Check if contains | `names.contains("Alice")` |
| `clear()` | Remove all elements | `names.clear()` |

---

## Connecting to What You Already Know

### From Week 7: Building on Classes and Objects

Everything from Week 7 applies - we're just doing it BETTER:

| Week 7 Concept | Week 8 Enhancement |
|----------------|-------------------|
| Private attributes | Now you understand WHY (protection!) |
| Basic constructors | Validation + overloading + chaining |
| Simple getters | Still simple, but now you know alternatives |
| Basic setters | Now with validation |
| `this` keyword | Disambiguation + constructor chaining |

### The Same Classes, Now Bulletproof

Your Week 7 Car class worked, but could be broken. Your Week 8 Car class is solid:

```java
// Week 7: Trusting
public void accelerate(int amount) {
    speed += amount;  // Trusts the caller
}

// Week 8: Defensive
public void accelerate(int amount) {
    if (amount > 0) {
        speed += amount;
        if (speed > maxSpeed) {
            speed = maxSpeed;
        }
    }
}
```

### From Weeks 4-5: Method Overloading to Constructor Overloading

You learned method overloading in Week 5:

```java
// Week 5: Method overloading
public static int add(int a, int b) { return a + b; }
public static int add(int a, int b, int c) { return a + b + c; }
```

Constructor overloading is the same concept:

```java
// Week 8: Constructor overloading
public Student(String name, int age, String major) { ... }
public Student(String name, int age) { ... }
public Student(String name) { ... }
```

### From Week 6: Arrays to ArrayList

Arrays taught you collections. ArrayList is the grown-up version:

| Array (Week 6) | ArrayList (Week 8) |
|----------------|-------------------|
| `int[] grades = new int[100]` | `ArrayList<Integer> grades = new ArrayList<>()` |
| Fixed size | Grows automatically |
| `grades[0]` | `grades.get(0)` |
| `grades[0] = 85` | `grades.set(0, 85)` or `grades.add(85)` |
| `grades.length` | `grades.size()` |
| Manual bounds checking | Automatic |

---

## Common Struggles and How to Overcome Them

### Struggle 1: "Why Must Attributes Be Private?"

**The confusion:** "Making everything public is easier - why all this getter/setter work?"

**The answer:** Protection and control.

```java
// Public attribute - anyone can break your object
public int age;
student.age = -50;  // Broken object!
student.age = 999999;  // Nonsense!

// Private with setter - you control what's allowed
private int age;
public void setAge(int newAge) {
    if (newAge >= 0 && newAge <= 150) {
        age = newAge;
    }
}
student.setAge(-50);  // Rejected - object stays valid
```

**Remember:** You're protecting your objects from mistakes (yours and others').

### Struggle 2: "When Should I Use Getters vs Direct Access?"

**The confusion:** Inside the class, should I use `name` or `getName()`?

**The answer:** Inside your own class, direct access is fine:

```java
public class Student {
    private String name;

    public String toString() {
        return name;  // OK - we're inside Student class
        // return getName();  // Also OK, but unnecessary
    }
}
```

Outside the class, you MUST use getters (private attributes aren't accessible).

### Struggle 3: "Understanding `this`"

**The confusion:** When do I need `this`?

**Rules:**
1. **Always** when parameter name matches attribute name
2. **Always** for constructor chaining (`this(...)`)
3. **Optional** elsewhere (but can add clarity)

```java
public class Student {
    private String name;

    // MUST use this - parameter shadows attribute
    public Student(String name) {
        this.name = name;  // this.name = attribute
    }

    // MUST use this() - calling another constructor
    public Student() {
        this("Unknown");
    }

    // Optional - no shadowing
    public void printName() {
        System.out.println(name);       // OK
        System.out.println(this.name);  // Also OK
    }
}
```

### Struggle 4: "Constructor vs Method Confusion"

**The confusion:** Constructors look like methods - what's different?

| Constructor | Method |
|-------------|--------|
| No return type | Has return type (or void) |
| Same name as class | Any name |
| Called with `new` | Called on existing object |
| Runs once per object creation | Can run many times |

```java
public class Student {
    // CONSTRUCTOR: No return type, same name as class
    public Student(String name) {
        // Initialize object
    }

    // METHOD: Has return type, different name
    public String getName() {
        return name;
    }
}
```

### Struggle 5: "Static vs Instance Members"

**The confusion:** When to use `static`?

**Simple rule for now:**

- **Instance** (no static): Different for each object
  - Each car has its own speed
  - Each student has its own name

- **Static**: Shared by ALL objects, or doesn't need an object
  - Counter of all cars created
  - Utility methods like `Math.sqrt()`

```java
public class Car {
    // Instance - each car has its own
    private int speed;
    private String brand;

    // Static - shared by all cars
    private static int totalCarsCreated = 0;

    public Car(String brand) {
        this.brand = brand;
        this.speed = 0;
        totalCarsCreated++;  // Every new car increments the same counter
    }

    // Static method - doesn't need a specific car object
    public static int getTotalCars() {
        return totalCarsCreated;
    }
}
```

---

## Practice Exercises

### Exercise 1: MyCard(s) (meget hjaelp - Maximum Guidance)

**Goal:** Practice enums with attributes and encapsulated classes.

**Part A: Create the Suit Enum**

```java
public enum Suit {
    // TODO: Define HEARTS, DIAMONDS, CLUBS, SPADES
    // Each should have a name and color attribute
    // Hearts and Diamonds are "Red"
    // Clubs and Spades are "Black"
}
```

**Part B: Create the Card Class**

```java
public class Card {
    private Suit suit;
    private int value;  // 1-13

    // TODO: Constructor with validation (value must be 1-13)

    // TODO: Getters for suit and value

    // TODO: isRed() method that uses suit.getColor()

    // TODO: toString() that returns "Queen of Hearts" format
}
```

**Part C: Demo Program**

```java
public class CardDemo {
    public static void main(String[] args) {
        // Create some cards
        Card card1 = new Card(Suit.HEARTS, 12);  // Queen of Hearts
        Card card2 = new Card(Suit.SPADES, 1);   // Ace of Spades

        System.out.println(card1);
        System.out.println(card2);
        System.out.println(card1.isRed());  // true
        System.out.println(card2.isRed());  // false
    }
}
```

### Exercise 2: MyGrades (nogen hjaelp - Moderate Guidance)

**Goal:** Practice encapsulation, ArrayList, and static variables.

Create a `GradeBook` class that:
- Has private attributes: studentName (String), studentId (String), grades (ArrayList<Integer>)
- Has a static counter for generating unique IDs
- Constructor takes name, generates ID automatically (e.g., "STU001", "STU002")
- Has addGrade() with validation (0-100)
- Has getAverage(), getHighestGrade(), getLowestGrade()
- Has isPassing() (average >= 60)
- Has getLetterGrade() using enum: A (90+), B (80-89), C (70-79), D (60-69), F (<60)
- Has toString()

**Create an enum for letter grades:**

```java
public enum LetterGrade {
    A("Excellent", 4.0),
    B("Good", 3.0),
    C("Average", 2.0),
    D("Passing", 1.0),
    F("Failing", 0.0);

    // TODO: Add attributes and constructor
}
```

**Test your GradeBook:**
- Create 3 students
- Add various grades to each
- Print each student's information
- Find which student has the highest average

### Exercise 3: Lamps (nogen hjaelp - Moderate Guidance)

**Goal:** Practice toggle behavior and static counters.

Create a `Lamp` class:
- Private attributes: isOn (boolean), brightness (int 0-100), color (String)
- Static counter for total lamps created
- Static counter for lamps currently on
- Constructor with color parameter, starts off with brightness 50
- toggle() method that turns lamp on/off and updates static counter
- setBrightness() with validation
- dim() and brighten() methods that change brightness by 10
- Getters for all attributes
- Static method getTotalLamps()
- Static method getLampsOn()

**Demo:**
```java
Lamp lamp1 = new Lamp("White");
Lamp lamp2 = new Lamp("Yellow");

lamp1.toggle();  // Now on
System.out.println(Lamp.getLampsOn());  // 1

lamp2.toggle();  // Now on
System.out.println(Lamp.getLampsOn());  // 2

lamp1.toggle();  // Now off
System.out.println(Lamp.getLampsOn());  // 1
```

### Exercise 4: Cars (ingen hjaelp - Minimal Guidance)

**Goal:** Full encapsulation with complex state management.

Create a comprehensive `Car` class with:
- Brand, model, year (set once, validated)
- Current speed, max speed (validated)
- Fuel level (0-100), fuel efficiency (km per unit fuel)
- Odometer (total km driven, never decreases)
- isRunning state

Requirements:
- Can't accelerate if not running or no fuel
- Driving consumes fuel based on efficiency
- Speed automatically reduces if fuel runs out
- All inputs validated
- Static counter for cars created
- Constructor overloading with chaining

Create a simulation that:
1. Creates 3 different cars
2. Starts them, drives them different distances
3. Shows fuel consumption
4. Demonstrates validation (try invalid operations)
5. Shows odometer never decreases

---

## Looking Ahead

This week you transformed your Week 7 classes from "working" to "properly designed." You now understand:
- Why ALL attributes must be private
- How to protect your objects with validation
- How to provide controlled access through getters and setters
- How to initialize objects correctly with constructors

**In the coming weeks, you will build further on these foundations:**

- **Week 9 (Inheritance and Polymorphism):** You will learn how to create relationships between classes where one class inherits from another. A `SportsCar` can inherit from `Car`, getting all its encapsulated attributes and methods while adding its own. The protected access modifier becomes relevant here.

- **Week 10 (Advanced OOP Topics):** You will explore wrapper classes (Integer, Double, etc.), which are themselves encapsulated classes. You'll understand why ArrayList uses `ArrayList<Integer>` instead of `ArrayList<int>`.

The Car, Student, and Die classes you've perfected this week will continue to evolve. In Week 9, you might create:
- `SportsCar extends Car` (faster acceleration, lower max fuel efficiency)
- `GraduateStudent extends Student` (has thesis topic, advisor)
- `LoadedDie extends Die` (weighted dice!)

Your encapsulation skills ensure these new classes start with a solid, protected foundation.

---

## Key Takeaways

1. **Encapsulation** bundles data (attributes) with the methods that operate on that data, hiding internal implementation

2. **ALL attributes MUST be private** - this is a non-negotiable exam requirement and fundamental OOP principle

3. **Access modifiers** control visibility: `private` (class only), `public` (everywhere)

4. **Getters** (accessors) safely return attribute values; boolean getters use `is` prefix

5. **Setters** (mutators) modify attributes with validation to maintain class invariants

6. **Class invariants** are conditions that are always true for valid objects

7. **Constructors** initialize objects; can be overloaded and chained with `this()`

8. **The `this` keyword** refers to the current object; essential for disambiguation and constructor chaining

9. **Shadowing** occurs when a local variable hides an instance variable with the same name

10. **Enums with attributes** combine type safety with data storage

11. **ArrayList** provides flexible, growable collections that track their own size

12. **Validation everywhere** - constructors AND setters must validate to maintain invariants

---

## For the Next Topic Agent

### Terminology Established This Week

- **encapsulation**: Bundling data with methods that operate on that data, hiding implementation details
- **data hiding**: Keeping attributes private to protect object state
- **access modifier**: Keywords (private, public, protected) controlling visibility
- **getter/accessor**: Method returning an attribute's value
- **setter/mutator**: Method modifying an attribute's value with validation
- **class invariant**: A condition that is always true for valid objects
- **validation**: Checking that values meet required constraints
- **constructor chaining**: Using `this()` to call another constructor
- **shadowing**: When a local variable hides an instance variable of the same name
- **ArrayList**: A flexible, growable collection class
- **generic type parameter**: The `<Type>` in `ArrayList<Type>` specifying element type

### Example Classes Evolved from Week 7

The following classes from Week 7 were enhanced with proper encapsulation:

1. **Car** (brand, model, year, speed, maxSpeed)
   - Now has: Validation in constructor and setters, class invariants
   - Speed always 0 <= speed <= maxSpeed
   - Year validated (1886 to current year)
   - Behavior methods validate inputs
   - Ready for Week 9: inheritance (SportsCar, Truck, ElectricCar)

2. **Student** (name, age, ArrayList<Integer> grades)
   - Now uses: ArrayList instead of array for grades
   - Validation on age (0-150) and grades (0-100)
   - getAverage(), getHighestGrade(), isPassing() all work with ArrayList
   - Ready for Week 9: inheritance (GraduateStudent, UndergraduateStudent)

3. **Die** (sides, currentValue, Random)
   - Already well-encapsulated in Week 7
   - Constructor validates sides >= 2
   - No setter for sides (immutable after creation)
   - Ready for Week 9: inheritance (LoadedDie, PolyhedralDie)

### New Classes Introduced

4. **Card with Suit enum**
   - Demonstrates enums with attributes
   - Shows encapsulation with enum integration
   - Suit has name and color attributes

5. **GradeBook with LetterGrade enum**
   - Shows static ID generation
   - ArrayList of grades
   - Enum for letter grade representation

6. **Lamp**
   - Demonstrates static counters
   - Toggle behavior pattern
   - Brightness validation

### Student Capabilities After This Week

Students can now:
- Explain WHY attributes must be private (protection, validation, flexibility)
- Write getters and setters with appropriate validation
- Design class invariants and maintain them
- Write multiple constructors with overloading and chaining
- Use `this` for disambiguation and constructor chaining
- Create enums with attributes and getters
- Use ArrayList as a flexible alternative to arrays
- Distinguish between static and instance members more confidently

### Critical Concepts for Week 9 (Inheritance)

Week 9 should build on:
- The **protected** access modifier (accessible in subclasses)
- Constructor chaining across inheritance hierarchy (`super()`)
- How encapsulated parent classes protect inherited state
- Why getters/setters matter even more with inheritance (subclass access)

Key preparation:
- Students understand that a subclass will inherit private attributes but cannot access them directly
- Students know that getters/setters in the parent class provide controlled access for subclasses
- The Car/Student/Die classes are ready to be extended

### Common Misconceptions to Address in Week 9

- "If I inherit private attributes, why can't I access them directly?" -> Use inherited getters/setters
- "Should subclass constructors validate again?" -> Call super() constructor, let parent validate
- "Can I override getters/setters?" -> Yes, and this is part of polymorphism
- Static members don't inherit the same way instance members do
