# OOP Part 4: Inheritance and Polymorphism - Week 9

*Prerequisites: Week 7 - OOP Part 1: Classes and Objects, Week 8 - OOP Part 2: Encapsulation*
*Phase: Phase 3: Object-Oriented Thinking*

---

## What You'll Learn

By the end of this week, you will be able to:

- **Understand inheritance** as an IS-A relationship between classes
- **Apply the extends keyword** to create subclasses from superclasses
- **Use the super keyword** to call parent constructors and methods
- **Implement method overriding** with the @Override annotation
- **Apply the protected access modifier** for inheritance-friendly access
- **Design and use abstract classes** that cannot be instantiated
- **Understand polymorphism** as "one interface, many forms"
- **Work with polymorphic references** (parent type, child object)
- **Apply dynamic method dispatch** (runtime method binding)
- **Use the instanceof operator** for safe type checking
- **Perform safe downcasting and upcasting** between class types
- **Design inheritance hierarchies** that model real-world relationships

**CRITICAL EXAM TOPIC**: Inheritance and polymorphism comprise 40-50% of your exam. This is the culmination of everything you have learned about object-oriented programming.

This week completes your transformation from procedural programmer to object-oriented programmer. The classes you encapsulated in Week 8 will now form the foundation of inheritance hierarchies.

---

## Why This Matters

### The Problem: Code Duplication

Imagine you are building a vehicle management system. You need classes for different vehicle types:

```java
// Car class
public class Car {
    private String brand;
    private String model;
    private int year;
    private int speed;
    private int maxSpeed;

    // Constructor, getters, setters, accelerate(), brake()...
    // ~50 lines of code
}

// Motorcycle class
public class Motorcycle {
    private String brand;    // Same as Car!
    private String model;    // Same as Car!
    private int year;        // Same as Car!
    private int speed;       // Same as Car!
    private int maxSpeed;    // Same as Car!

    // Nearly identical constructor, getters, setters...
    // Another ~50 lines of DUPLICATE code
}

// Truck class
public class Truck {
    private String brand;    // Same again!
    private String model;    // Same again!
    private int year;        // Same again!
    // ... you see the pattern
}
```

**Problems with this approach:**
1. **Massive code duplication** - The same attributes and methods written repeatedly
2. **Maintenance nightmare** - Fix a bug in `accelerate()`? Fix it in ALL vehicle classes!
3. **No relationship** - Java doesn't know that Car and Motorcycle are both "vehicles"
4. **Inflexible** - Cannot treat all vehicles the same way

### How Inheritance Solves This

```java
// ONE parent class with shared code
public class Vehicle {
    private String brand;
    private String model;
    private int year;
    private int speed;
    private int maxSpeed;

    // Constructor, getters, setters - written ONCE
    public void accelerate(int amount) { /* ... */ }
    public void brake(int amount) { /* ... */ }
}

// Each child class INHERITS the common code
public class Car extends Vehicle {
    private int numberOfDoors;  // Only car-specific stuff
    // Inherits brand, model, year, speed, maxSpeed, accelerate(), brake()
}

public class Motorcycle extends Vehicle {
    private boolean hasSidecar;  // Only motorcycle-specific stuff
    // Inherits brand, model, year, speed, maxSpeed, accelerate(), brake()
}

public class Truck extends Vehicle {
    private double cargoCapacity;  // Only truck-specific stuff
    // Inherits brand, model, year, speed, maxSpeed, accelerate(), brake()
}
```

**Benefits:**
1. **Write once, use everywhere** - Common code in parent class
2. **Easy maintenance** - Fix bugs in ONE place
3. **Relationship established** - Java knows Car IS-A Vehicle
4. **Polymorphism enabled** - Treat all vehicles uniformly when needed

### Real-World Applications

Inheritance and polymorphism are everywhere in software:

- **GUI frameworks**: Button, TextField, Label all extend Component
- **Games**: Warrior, Mage, Archer all extend Character
- **E-commerce**: DigitalProduct, PhysicalProduct, Subscription all extend Product
- **Java itself**: Every class extends Object; all exceptions extend Exception

---

## Building Your Intuition

Polymorphism and inheritance are abstract concepts. Multiple analogies will help you understand them from different angles.

### Analogy 1: The Family Tree (Inheritance)

Think of biological inheritance. When you inherit traits from your parents:

- You get their genes (attributes and methods)
- You also have your own unique traits
- You can do everything a "human" can do, plus your own skills
- You cannot "un-inherit" being human

```
         Human (parent class)
        /      \
    Parent1   Parent2
       |
      You (child class)

You ARE-A Human
You have Human capabilities + your own
```

In Java:

```java
public class Human {
    protected String name;
    public void breathe() { /* all humans breathe */ }
    public void eat() { /* all humans eat */ }
}

public class Student extends Human {
    private String major;
    public void study() { /* students can study */ }
    // Can still breathe() and eat() - inherited!
}
```

A Student **IS-A** Human. A Student can do everything a Human can do, plus student-specific things.

### Analogy 2: The Biological Taxonomy (Inheritance Hierarchy)

Think of how biologists classify living things:

```
                    Animal
                   /      \
            Mammal          Bird
           /      \            \
        Dog       Cat         Eagle
       /   \
   Labrador  Poodle
```

Each level **inherits** from the level above:
- A Labrador IS-A Dog
- A Dog IS-A Mammal
- A Mammal IS-A Animal
- Therefore, a Labrador IS-A Animal (transitive!)

A Labrador has all the characteristics of a Dog, all the characteristics of a Mammal, and all the characteristics of an Animal.

### Analogy 3: Universal Remotes (Polymorphism)

Here is the key insight about polymorphism. Think about a universal remote control:

**The remote has ONE "power" button** that works with:
- Your TV (turns TV on/off)
- Your DVD player (turns DVD on/off)
- Your sound system (turns sound system on/off)

**Same button, different behaviors!** The remote doesn't know exactly which device will respond - it just sends the "power" signal. Each device responds IN ITS OWN WAY.

```java
// The "universal remote" in Java
public void togglePower(Device device) {
    device.power();  // ONE method call
    // Different devices respond differently!
}

// Each device has its own implementation
class TV extends Device {
    public void power() { /* TV-specific power behavior */ }
}

class DVDPlayer extends Device {
    public void power() { /* DVD-specific power behavior */ }
}
```

**Polymorphism means: ONE interface (method call), MANY forms (implementations).**

### Analogy 4: The Shape Drawing Program (Classic Example)

Imagine a drawing program that can draw shapes:

```
          Shape (abstract)
         /   |    \
    Circle  Square  Triangle
```

Every Shape has a `draw()` method, but each shape draws differently:
- Circle draws a circle
- Square draws a square
- Triangle draws a triangle

The drawing program can say "draw yourself!" to ANY shape without knowing what kind of shape it is:

```java
public void drawAllShapes(Shape[] shapes) {
    for (Shape s : shapes) {
        s.draw();  // Each shape draws itself correctly!
    }
}
```

The program doesn't need separate code for circles, squares, and triangles. **One loop draws them all** because each shape knows how to draw itself.

### Analogy 5: The Restaurant (Polymorphism with Override)

Consider a restaurant where all employees can `work()`:

```java
public class Employee {
    public void work() {
        System.out.println("Working at the restaurant");
    }
}

public class Chef extends Employee {
    @Override
    public void work() {
        System.out.println("Cooking delicious food");
    }
}

public class Waiter extends Employee {
    @Override
    public void work() {
        System.out.println("Serving customers");
    }
}

public class Manager extends Employee {
    @Override
    public void work() {
        System.out.println("Managing the restaurant");
    }
}
```

At opening time, the restaurant can tell ALL employees to `work()`:

```java
Employee[] staff = { new Chef(), new Waiter(), new Manager() };
for (Employee e : staff) {
    e.work();  // Each does their OWN kind of work!
}
```

**Output:**
```
Cooking delicious food
Serving customers
Managing the restaurant
```

Same method call (`work()`), different behaviors. That's polymorphism!

### Analogy 6: The Substitute Teacher (Runtime Type vs Compile-Time Type)

Here's a tricky but important concept. Imagine:

```java
Employee substitute = new Chef();  // A chef is substituting today
```

On the schedule (compile-time), it says "Employee" will be here.
In reality (runtime), a **Chef** shows up.

When you call `substitute.work()`:
- The schedule says it's an Employee
- But the actual person is a Chef
- The Chef does Chef work, not generic Employee work!

```java
Employee substitute = new Chef();
substitute.work();  // Prints "Cooking delicious food" - Chef behavior!
```

Java looks at the **actual object** (Chef) at runtime, not the **declared type** (Employee).

---

## Understanding Inheritance with the `extends` Keyword

### What Is Inheritance?

**Inheritance** is a mechanism where a new class (child/subclass) is derived from an existing class (parent/superclass). The child class automatically receives all non-private members of the parent class.

### Why "extends"?

The keyword `extends` means the child class **extends** (builds upon) the parent class:
- Takes everything the parent has
- Can add new attributes and methods
- Can modify (override) inherited methods

### Basic Syntax

```java
public class ChildClass extends ParentClass {
    // Child-specific code here
}
```

### Inheriting from the Week 8 Car Class

Let's create a `SportsCar` that extends our encapsulated `Car` class:

```java
// Parent class (from Week 8)
public class Car {
    private String brand;
    private String model;
    private int year;
    private int speed;
    private int maxSpeed;

    public Car(String brand, String model, int year, int maxSpeed) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.maxSpeed = maxSpeed;
        this.speed = 0;
    }

    public void accelerate(int amount) {
        if (amount > 0) {
            speed += amount;
            if (speed > maxSpeed) {
                speed = maxSpeed;
            }
        }
    }

    public void brake(int amount) {
        if (amount > 0) {
            speed -= amount;
            if (speed < 0) {
                speed = 0;
            }
        }
    }

    // Getters
    public String getBrand() { return brand; }
    public String getModel() { return model; }
    public int getYear() { return year; }
    public int getSpeed() { return speed; }
    public int getMaxSpeed() { return maxSpeed; }

    public String toString() {
        return year + " " + brand + " " + model;
    }
}

// Child class
public class SportsCar extends Car {
    private boolean turboEnabled;

    public SportsCar(String brand, String model, int year) {
        super(brand, model, year, 300);  // Sports cars have high max speed
        this.turboEnabled = false;
    }

    public void enableTurbo() {
        turboEnabled = true;
    }

    public void disableTurbo() {
        turboEnabled = false;
    }

    public boolean isTurboEnabled() {
        return turboEnabled;
    }
}
```

### What SportsCar Automatically Gets (Inheritance)

Without writing any additional code, `SportsCar` has:
- All the inherited methods: `accelerate()`, `brake()`, `getBrand()`, `getModel()`, etc.
- Access to parent functionality through `super`
- The IS-A relationship: SportsCar IS-A Car

```java
SportsCar ferrari = new SportsCar("Ferrari", "488", 2023);
ferrari.accelerate(100);        // Inherited method!
System.out.println(ferrari.getBrand());  // "Ferrari" - inherited getter!
ferrari.enableTurbo();          // SportsCar-specific method
```

### What SportsCar CANNOT Access Directly

**Private members are NOT directly accessible** in child classes:

```java
public class SportsCar extends Car {
    public void showDetails() {
        // This FAILS - brand is private in Car
        // System.out.println(brand);  // ERROR!

        // This WORKS - use the inherited getter
        System.out.println(getBrand());  // OK!
    }
}
```

**This is encapsulation working with inheritance.** Even child classes must use getters and setters to access private parent data.

---

## Understanding the `super` Keyword

### What Is `super`?

The `super` keyword refers to the **parent class**. It has two main uses:

1. **`super()`** - Call the parent's constructor
2. **`super.methodName()`** - Call a parent's method

### Use 1: Calling Parent Constructor with `super()`

When you create a child object, the parent's constructor MUST run first. Use `super()` to call it:

```java
public class Car {
    private String brand;
    private String model;
    private int year;
    private int maxSpeed;

    public Car(String brand, String model, int year, int maxSpeed) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.maxSpeed = maxSpeed;
    }
}

public class ElectricCar extends Car {
    private int batteryCapacity;  // in kWh

    public ElectricCar(String brand, String model, int year, int batteryCapacity) {
        // MUST call parent constructor first
        super(brand, model, year, 200);  // Electric cars: 200 km/h max

        // Then initialize child-specific attributes
        this.batteryCapacity = batteryCapacity;
    }

    public int getBatteryCapacity() {
        return batteryCapacity;
    }
}
```

**Critical Rules for `super()`:**

1. **Must be the FIRST statement** in the child constructor
2. **Must provide arguments** matching a parent constructor
3. **If omitted**, Java calls `super()` (no-argument) automatically - but this only works if the parent HAS a no-argument constructor!

```java
// This FAILS if Car has no no-argument constructor
public class BadSportsCar extends Car {
    public BadSportsCar() {
        // Java secretly tries: super();
        // But Car requires 4 arguments!
        // COMPILER ERROR!
    }
}
```

### Use 2: Calling Parent Method with `super.method()`

When you override a parent method but still want its original behavior:

```java
public class Car {
    public String toString() {
        return year + " " + brand + " " + model;
    }
}

public class ElectricCar extends Car {
    private int batteryCapacity;

    @Override
    public String toString() {
        // Call parent's toString, then add our info
        return super.toString() + " (Electric, " + batteryCapacity + " kWh)";
    }
}
```

```java
ElectricCar tesla = new ElectricCar("Tesla", "Model 3", 2023, 75);
System.out.println(tesla.toString());
// Output: 2023 Tesla Model 3 (Electric, 75 kWh)
```

### Constructor Chaining in Inheritance

Remember `this()` from Week 8 for chaining constructors within a class? With inheritance, you combine `super()` and `this()`:

```java
public class SportsCar extends Car {
    private boolean turboEnabled;
    private String engineType;

    // Primary constructor
    public SportsCar(String brand, String model, int year, String engineType) {
        super(brand, model, year, 300);  // Call parent constructor
        this.turboEnabled = false;
        this.engineType = engineType;
    }

    // Overloaded constructor - chains to primary
    public SportsCar(String brand, String model, int year) {
        this(brand, model, year, "V8");  // Call other SportsCar constructor
    }
}
```

**Note:** You can use EITHER `super()` OR `this()` as the first line, but not both!

---

## The `protected` Access Modifier

### Expanding Beyond Private and Public

In Week 8, you learned about `private` and `public`. Now we add `protected`:

| Modifier | Same Class | Same Package | Subclass | Everywhere |
|----------|------------|--------------|----------|------------|
| `private` | Yes | No | No | No |
| (package-private) | Yes | Yes | No | No |
| **`protected`** | Yes | Yes | **Yes** | No |
| `public` | Yes | Yes | Yes | Yes |

### Why Protected?

`protected` allows **subclasses** to access a member, even if they are in a different package:

```java
// In file Vehicle.java
public class Vehicle {
    protected int speed;  // Subclasses can access directly
    private String vin;   // Only Vehicle class can access

    protected void internalCheck() {
        // Subclasses can call this
    }
}

// In file Car.java (even in different package)
public class Car extends Vehicle {
    public void accelerate(int amount) {
        speed += amount;  // OK - protected is accessible in subclass
        // vin = "123";   // ERROR - private is not accessible
        internalCheck();  // OK - protected method accessible
    }
}
```

### When to Use Protected

Use `protected` when:
- Subclasses need direct access to the member
- You don't want random external code to access it
- The member is part of the "internal API" for the class family

**Best practice:** Start with `private`. Only use `protected` when you design a class specifically for inheritance and subclasses truly need direct access.

```java
public class Car {
    // Private - only Car manages this directly
    private String brand;

    // Protected - subclasses might need direct access for special operations
    protected int internalTemperature;

    // Public - anyone can read the brand
    public String getBrand() {
        return brand;
    }
}
```

---

## Method Overriding

### What Is Method Overriding?

**Method overriding** occurs when a subclass provides its own implementation of a method that exists in the parent class. The child's version **replaces** the parent's version for objects of the child type.

### Why Override?

Subclasses often need to modify inherited behavior:

- A `SportsCar` might accelerate faster than a regular `Car`
- An `ElectricCar` might brake differently (regenerative braking)
- A `GraduateStudent` might have different graduation requirements than a regular `Student`

### The @Override Annotation

Always use `@Override` when overriding a method:

```java
public class Car {
    protected int speed;
    protected int maxSpeed;

    public void accelerate(int amount) {
        if (amount > 0) {
            speed += amount;
            if (speed > maxSpeed) {
                speed = maxSpeed;
            }
        }
    }
}

public class SportsCar extends Car {
    private boolean turboEnabled;

    @Override  // ALWAYS use this annotation
    public void accelerate(int amount) {
        if (amount > 0) {
            int boost = turboEnabled ? 2 : 1;  // Turbo doubles acceleration
            speed += amount * boost;
            if (speed > maxSpeed) {
                speed = maxSpeed;
            }
        }
    }
}
```

### Why @Override Is Important

1. **Compiler verification** - Catches mistakes:

```java
@Override
public void acelerate(int amount) {  // Typo in method name
    // COMPILER ERROR: Method does not override from superclass
}
```

Without `@Override`, this would silently create a NEW method (not override).

2. **Documentation** - Clearly shows intent to override
3. **Maintenance** - If parent method changes, compiler warns you

### Rules for Overriding

1. **Same method signature** (name and parameter types)
2. **Same or more accessible** (can't make a public method private)
3. **Same or narrower return type** (covariant return types)
4. **Cannot override final methods** (final prevents overriding)

```java
public class Car {
    public Car getCar() { return this; }
    public void drive() { /* ... */ }
    public final void getVIN() { /* ... */ }  // Cannot be overridden
}

public class SportsCar extends Car {
    @Override
    public SportsCar getCar() { return this; }  // OK - narrower return type

    @Override
    public void drive() { /* ... */ }  // OK - same signature

    // @Override
    // public void getVIN() { }  // ERROR - cannot override final method
}
```

### Overriding vs Overloading - Important Distinction!

| Overriding | Overloading |
|------------|-------------|
| Same method signature | Different parameters |
| Replaces parent behavior | Adds new method |
| Happens in inheritance | Can happen in same class |
| Runtime decision | Compile-time decision |

```java
public class Car {
    public void accelerate(int amount) { /* ... */ }
}

public class SportsCar extends Car {
    // OVERRIDING - replaces parent's accelerate(int)
    @Override
    public void accelerate(int amount) { /* different implementation */ }

    // OVERLOADING - adds new accelerate with different parameters
    public void accelerate(int amount, boolean useTurbo) { /* new method */ }
}
```

---

## Understanding Polymorphism

### What Is Polymorphism?

**Polymorphism** (from Greek: "poly" = many, "morph" = form) means "many forms." In Java:

**One variable type can refer to objects of different actual types, and method calls behave according to the actual object's type.**

### The Power of Polymorphism - One Array, Many Types

```java
// One array can hold different types of cars!
Car[] garage = new Car[3];
garage[0] = new Car("Toyota", "Camry", 2020, 180);
garage[1] = new SportsCar("Ferrari", "488", 2023);
garage[2] = new ElectricCar("Tesla", "Model 3", 2023, 75);

// One loop processes all of them
for (Car car : garage) {
    car.accelerate(50);  // Each car accelerates in its own way!
    System.out.println(car);  // Each car prints itself correctly!
}
```

**Without polymorphism**, you would need:
- A separate array for each car type
- Separate loops for each car type
- Separate handling code everywhere

**With polymorphism**, ONE piece of code handles ALL car types!

### Compile-Time Type vs Runtime Type

This is crucial to understand:

```java
Car myCar = new SportsCar("Ferrari", "488", 2023);
```

- **Compile-time type** (declared type): `Car`
- **Runtime type** (actual type): `SportsCar`

**What you can CALL is determined by compile-time type:**

```java
Car myCar = new SportsCar("Ferrari", "488", 2023);
myCar.accelerate(50);  // OK - Car has accelerate()
myCar.enableTurbo();   // ERROR! Car doesn't have enableTurbo()
                       // Even though the actual object does!
```

**What BEHAVIOR you GET is determined by runtime type:**

```java
Car myCar = new SportsCar("Ferrari", "488", 2023);
myCar.accelerate(50);  // Calls SportsCar's accelerate() method!
                       // Because the actual object is a SportsCar
```

### Visual Model: Compile vs Runtime

```
COMPILE TIME (What Java checks)          RUNTIME (What actually happens)
================================         ================================

Car myCar = ...                          ... = new SportsCar(...)

   +----------+                             +---------------+
   |   Car    |                             |   SportsCar   |
   +----------+                             +---------------+
   | brand    |                             | brand         |
   | model    |                             | model         |
   | year     |                             | year          |
   +----------+                             | turboEnabled  |
   |accelerate|  <--- Java checks           +---------------+
   |brake     |       this exists           |accelerate     | <-- Java RUNS this
   |toString  |                             |brake          |
   +----------+                             |enableTurbo    |
                                            |toString       |
Compiler sees: "Can I call                  +---------------+
accelerate() on a Car? Yes!"                JVM sees: "What's the actual
                                            accelerate()? SportsCar's!"
```

### Dynamic Method Dispatch

**Dynamic method dispatch** (also called **dynamic binding** or **late binding**) is the mechanism Java uses to decide which method to call at runtime.

When you call an overridden method through a parent reference:

1. Java looks at the **actual object type** (runtime type)
2. Java calls the method from **that class**

```java
Car[] cars = {
    new Car("Toyota", "Camry", 2020, 180),
    new SportsCar("Ferrari", "488", 2023),
    new ElectricCar("Tesla", "Model 3", 2023, 75)
};

for (Car c : cars) {
    System.out.println(c.toString());  // Dynamic dispatch!
}
```

**Output:**
```
2020 Toyota Camry
2023 Ferrari 488 (Turbo Available)
2023 Tesla Model 3 (Electric, 75 kWh)
```

Each object's OWN `toString()` is called, even though `c` is declared as `Car`.

---

## The `instanceof` Operator and Casting

### What Is `instanceof`?

The `instanceof` operator checks if an object is an instance of a specific class (or a subclass):

```java
Car myCar = new SportsCar("Ferrari", "488", 2023);

System.out.println(myCar instanceof SportsCar);  // true
System.out.println(myCar instanceof Car);        // true (SportsCar IS-A Car)
System.out.println(myCar instanceof ElectricCar); // false

Car regularCar = new Car("Toyota", "Camry", 2020, 180);
System.out.println(regularCar instanceof SportsCar);  // false
```

### Why Do We Need `instanceof`?

Remember: with a parent reference, you can only call parent methods:

```java
Car myCar = new SportsCar("Ferrari", "488", 2023);
myCar.enableTurbo();  // ERROR! Car doesn't have enableTurbo()
```

But the object IS a SportsCar! To access SportsCar methods, you need to:
1. Check if it's really a SportsCar (`instanceof`)
2. Cast it to SportsCar

### Upcasting and Downcasting

**Upcasting** (automatic): Child to parent - always safe

```java
SportsCar ferrari = new SportsCar("Ferrari", "488", 2023);
Car car = ferrari;  // Upcasting - automatic, always safe
```

**Downcasting** (explicit): Parent to child - MUST check first!

```java
Car car = new SportsCar("Ferrari", "488", 2023);
SportsCar sports = (SportsCar) car;  // Downcasting - requires cast
sports.enableTurbo();  // Now we can access SportsCar methods
```

### Safe Casting Pattern

**ALWAYS check with `instanceof` before downcasting:**

```java
public void processCar(Car car) {
    // All cars can accelerate
    car.accelerate(50);

    // Only SportsCars have turbo
    if (car instanceof SportsCar) {
        SportsCar sports = (SportsCar) car;  // Safe to cast
        sports.enableTurbo();
    }

    // Only ElectricCars have battery info
    if (car instanceof ElectricCar) {
        ElectricCar electric = (ElectricCar) car;  // Safe to cast
        System.out.println("Battery: " + electric.getBatteryCapacity() + " kWh");
    }
}
```

### What Happens Without Checking?

```java
Car car = new Car("Toyota", "Camry", 2020, 180);  // Regular car
SportsCar sports = (SportsCar) car;  // CRASH! ClassCastException!
```

**ClassCastException** is a runtime error - your program crashes. Always use `instanceof` first!

### Enhanced instanceof with Pattern Matching (Java 16+)

Modern Java combines instanceof and casting in one step:

```java
// Old way
if (car instanceof SportsCar) {
    SportsCar sports = (SportsCar) car;
    sports.enableTurbo();
}

// New way (Java 16+) - pattern matching
if (car instanceof SportsCar sports) {
    sports.enableTurbo();  // sports is already cast!
}
```

The variable `sports` is automatically created and cast for you.

---

## Abstract Classes and Methods

### What Is an Abstract Class?

An **abstract class** is a class that:
1. Cannot be instantiated directly (can't use `new`)
2. May contain abstract methods (methods without implementation)
3. Is designed to be extended

### Why Abstract Classes?

Sometimes a parent class is too general to exist on its own:

- You can have a `Dog` or a `Cat`, but not a generic "Animal" with no species
- You can have a `Circle` or a `Square`, but not a generic "Shape" with no form
- You can have a `Car` or a `Truck`, but maybe not a generic "Vehicle"

Abstract classes express: "This is a template - create specific versions!"

### Abstract Class Syntax

```java
public abstract class Animal {
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    // Concrete method - has implementation
    public String getName() {
        return name;
    }

    // Abstract method - NO implementation
    // Subclasses MUST provide implementation
    public abstract void makeSound();

    public abstract void move();
}
```

### Implementing Abstract Methods

Subclasses MUST implement all abstract methods (or be abstract themselves):

```java
public class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println(name + " barks: Woof!");
    }

    @Override
    public void move() {
        System.out.println(name + " runs on four legs");
    }
}

public class Bird extends Animal {
    public Bird(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println(name + " chirps: Tweet!");
    }

    @Override
    public void move() {
        System.out.println(name + " flies through the air");
    }
}
```

### Abstract Classes Cannot Be Instantiated

```java
Animal animal = new Animal("Generic");  // ERROR! Cannot instantiate abstract class

Animal dog = new Dog("Buddy");    // OK! Dog is concrete
Animal bird = new Bird("Tweety"); // OK! Bird is concrete
```

### Polymorphism with Abstract Classes

Abstract classes work perfectly with polymorphism:

```java
Animal[] pets = new Animal[3];
pets[0] = new Dog("Buddy");
pets[1] = new Bird("Tweety");
pets[2] = new Dog("Max");

for (Animal pet : pets) {
    pet.makeSound();  // Polymorphic call!
    pet.move();       // Polymorphic call!
}
```

**Output:**
```
Buddy barks: Woof!
Buddy runs on four legs
Tweety chirps: Tweet!
Tweety flies through the air
Max barks: Woof!
Max runs on four legs
```

### Abstract Class Design Pattern: Template Method

Abstract classes are great for the "template method" pattern - define the structure, let subclasses fill in details:

```java
public abstract class Document {
    // Template method - defines the algorithm structure
    public final void generate() {
        addHeader();
        addContent();   // Abstract - subclasses implement
        addFooter();
    }

    private void addHeader() {
        System.out.println("=== DOCUMENT ===");
    }

    private void addFooter() {
        System.out.println("=== END ===");
    }

    // Abstract - each document type has different content
    protected abstract void addContent();
}

public class Report extends Document {
    @Override
    protected void addContent() {
        System.out.println("Report data and analysis...");
    }
}

public class Invoice extends Document {
    @Override
    protected void addContent() {
        System.out.println("Line items and total...");
    }
}
```

---

## Extending Week 8's Classes: Full Examples

### ElectricCar extends Car

```java
/**
 * An electric car that extends the basic Car class.
 * Adds battery management and regenerative braking.
 */
public class ElectricCar extends Car {
    private int batteryCapacity;    // in kWh
    private int currentCharge;      // in kWh
    private static final int CHARGE_PER_KM = 1;  // Simplified

    public ElectricCar(String brand, String model, int year, int batteryCapacity) {
        super(brand, model, year, 200);  // Electric cars: 200 km/h max

        if (batteryCapacity < 20) {
            this.batteryCapacity = 20;
        } else if (batteryCapacity > 150) {
            this.batteryCapacity = 150;
        } else {
            this.batteryCapacity = batteryCapacity;
        }
        this.currentCharge = this.batteryCapacity;  // Starts fully charged
    }

    // Getters for electric-specific attributes
    public int getBatteryCapacity() {
        return batteryCapacity;
    }

    public int getCurrentCharge() {
        return currentCharge;
    }

    public int getChargePercentage() {
        return (currentCharge * 100) / batteryCapacity;
    }

    // Charge the battery
    public void charge(int amount) {
        if (amount > 0) {
            currentCharge += amount;
            if (currentCharge > batteryCapacity) {
                currentCharge = batteryCapacity;
            }
        }
    }

    // Override accelerate to consume battery
    @Override
    public void accelerate(int amount) {
        if (currentCharge > 0) {
            super.accelerate(amount);  // Use parent's accelerate logic
            currentCharge -= CHARGE_PER_KM;  // Use battery
            if (currentCharge < 0) {
                currentCharge = 0;
            }
        } else {
            System.out.println("Cannot accelerate - battery empty!");
        }
    }

    // Override brake with regenerative braking
    @Override
    public void brake(int amount) {
        super.brake(amount);  // Normal braking
        // Regenerative braking recovers some charge
        currentCharge += amount / 10;
        if (currentCharge > batteryCapacity) {
            currentCharge = batteryCapacity;
        }
    }

    @Override
    public String toString() {
        return super.toString() + " (Electric, " +
               getChargePercentage() + "% charge)";
    }
}
```

### GraduateStudent extends Student

```java
import java.util.ArrayList;

/**
 * A graduate student extends the basic Student class.
 * Adds thesis topic, advisor, and teaching assistant status.
 */
public class GraduateStudent extends Student {
    private String thesisTopic;
    private String advisor;
    private boolean isTA;  // Teaching Assistant
    private ArrayList<String> publications;

    public GraduateStudent(String name, int age, String thesisTopic, String advisor) {
        super(name, age);  // Call parent constructor
        this.thesisTopic = thesisTopic;
        this.advisor = advisor;
        this.isTA = false;
        this.publications = new ArrayList<>();
    }

    // Convenience constructor
    public GraduateStudent(String name, int age) {
        this(name, age, "Undeclared", "Unassigned");
    }

    // Getters
    public String getThesisTopic() {
        return thesisTopic;
    }

    public String getAdvisor() {
        return advisor;
    }

    public boolean isTA() {
        return isTA;
    }

    // Setters with validation
    public void setThesisTopic(String topic) {
        if (topic != null && !topic.isEmpty()) {
            this.thesisTopic = topic;
        }
    }

    public void setAdvisor(String advisor) {
        if (advisor != null && !advisor.isEmpty()) {
            this.advisor = advisor;
        }
    }

    public void setTA(boolean isTA) {
        this.isTA = isTA;
    }

    // Publications management
    public void addPublication(String publication) {
        if (publication != null && !publication.isEmpty()) {
            publications.add(publication);
        }
    }

    public int getPublicationCount() {
        return publications.size();
    }

    // Override isPassing - graduate students need higher standards
    @Override
    public boolean isPassing() {
        return getAverage() >= 70.0;  // Higher threshold than undergrad
    }

    // New method for graduate students
    public boolean canGraduate() {
        return isPassing() &&
               !thesisTopic.equals("Undeclared") &&
               publications.size() >= 1;
    }

    @Override
    public String toString() {
        String status = isTA ? " (TA)" : "";
        return super.getName() + status +
               ", Thesis: " + thesisTopic +
               ", Advisor: " + advisor +
               ", Publications: " + publications.size();
    }
}
```

### LoadedDie extends Die

```java
/**
 * A loaded die that can be biased toward certain values.
 * Demonstrates inheritance from the Die class.
 */
public class LoadedDie extends Die {
    private int favoredValue;
    private int biasStrength;  // 1-5, higher = more biased

    public LoadedDie(int sides, int favoredValue, int biasStrength) {
        super(sides);  // Call parent constructor

        // Validate favored value
        if (favoredValue < 1 || favoredValue > sides) {
            this.favoredValue = sides;  // Default to highest value
        } else {
            this.favoredValue = favoredValue;
        }

        // Validate bias strength
        if (biasStrength < 1) {
            this.biasStrength = 1;
        } else if (biasStrength > 5) {
            this.biasStrength = 5;
        } else {
            this.biasStrength = biasStrength;
        }
    }

    // Constructor for default 6-sided loaded die
    public LoadedDie(int favoredValue) {
        this(6, favoredValue, 3);
    }

    // Default loaded die favoring 6
    public LoadedDie() {
        this(6, 6, 3);
    }

    // Getters
    public int getFavoredValue() {
        return favoredValue;
    }

    public int getBiasStrength() {
        return biasStrength;
    }

    // Override roll with biased behavior
    @Override
    public int roll() {
        // Roll multiple times and sometimes pick the favored value
        int normalRoll = super.roll();

        // Bias chance increases with bias strength
        // biasStrength 5 = 50% chance, 1 = 10% chance
        int biasChance = biasStrength * 10;

        java.util.Random random = new java.util.Random();
        if (random.nextInt(100) < biasChance) {
            return favoredValue;  // Loaded roll!
        }

        return normalRoll;  // Normal roll
    }

    @Override
    public String toString() {
        return "Loaded " + getSides() + "-sided die (favors " +
               favoredValue + ", bias " + biasStrength + "/5)";
    }
}
```

---

## The Object Class - Parent of All

### Every Class Extends Object

In Java, every class implicitly extends `Object`:

```java
public class Car {  // Actually: public class Car extends Object
    // ...
}
```

This means EVERY object has these methods:
- `toString()` - String representation
- `equals(Object obj)` - Compare for equality
- `hashCode()` - Hash code for collections
- `getClass()` - Get runtime class information

### The toString() Method

`Object.toString()` returns something like `Car@1a2b3c` (classname@hashcode), which is not useful. Override it:

```java
public class Car {
    private String brand;
    private String model;
    private int year;

    @Override
    public String toString() {
        return year + " " + brand + " " + model;
    }
}
```

Now `System.out.println(car)` automatically calls YOUR `toString()`.

### The equals() Method

`Object.equals()` compares references by default (same as `==`). Override for content comparison:

```java
public class Car {
    private String brand;
    private String model;
    private int year;

    @Override
    public boolean equals(Object obj) {
        // Check for self-comparison
        if (this == obj) return true;

        // Check for null and type
        if (obj == null || getClass() != obj.getClass()) return false;

        // Cast and compare attributes
        Car other = (Car) obj;
        return year == other.year &&
               brand.equals(other.brand) &&
               model.equals(other.model);
    }
}
```

**Now:**
```java
Car car1 = new Car("Toyota", "Camry", 2020, 180);
Car car2 = new Car("Toyota", "Camry", 2020, 180);

System.out.println(car1 == car2);      // false - different objects
System.out.println(car1.equals(car2)); // true - same content
```

---

## Connecting to What You Already Know

### From Week 8: Encapsulation Enables Safe Inheritance

Your Week 8 encapsulation skills are crucial:

| Week 8 Concept | Week 9 Connection |
|----------------|-------------------|
| Private attributes | Subclasses use inherited getters/setters |
| Validation in setters | Inherited validation protects subclass too |
| Constructor validation | `super()` calls validated parent constructor |
| `this()` chaining | Now combined with `super()` for inheritance |
| Class invariants | Maintained across inheritance hierarchy |

### From Week 7: Classes as Building Blocks

Your Week 7 classes are now EXTENDED:

| Week 7 Class | Week 9 Extension |
|--------------|------------------|
| `Car` | `ElectricCar`, `SportsCar`, `Truck` |
| `Student` | `GraduateStudent`, `UndergraduateStudent` |
| `Die` | `LoadedDie`, `ColoredDie` |

### From Week 5: Overloading to Overriding

| Week 5 Overloading | Week 9 Overriding |
|-------------------|-------------------|
| Same name, different parameters | Same name AND same parameters |
| Multiple methods in same class | Method in child replaces parent's |
| Compile-time resolution | Runtime resolution |

### From Week 6: Arrays to Polymorphic Arrays

```java
// Week 6: Array of one type
int[] numbers = {1, 2, 3};

// Week 9: Array of parent type holds different child types!
Car[] cars = new Car[3];
cars[0] = new Car("Toyota", "Camry", 2020, 180);
cars[1] = new SportsCar("Ferrari", "488", 2023);
cars[2] = new ElectricCar("Tesla", "Model 3", 2023, 75);
```

---

## Common Struggles and How to Overcome Them

### Struggle 1: When to Use Inheritance vs Composition

**The confusion:** "Should `Engine` inherit from `Car`, or should `Car` HAVE an `Engine`?"

**The test:** Use the IS-A vs HAS-A test:
- "An Engine IS-A Car" - No! Engines are not cars.
- "A Car HAS-A Engine" - Yes! Cars contain engines.

```java
// WRONG - Engine is not a type of Car
public class Engine extends Car { }

// RIGHT - Car contains an Engine
public class Car {
    private Engine engine;  // HAS-A (composition)
}

// RIGHT - SportsCar is a type of Car
public class SportsCar extends Car { }  // IS-A (inheritance)
```

**Rule of thumb:** If you can say "X IS-A Y" naturally, use inheritance. Otherwise, use composition.

### Struggle 2: Understanding Polymorphic Behavior

**The confusion:** "I declared it as `Car`, why does it act like a `SportsCar`?"

**The key insight:** The DECLARED type controls what you can CALL. The ACTUAL type controls what RUNS.

```java
Car myCar = new SportsCar("Ferrari", "488", 2023);

// What can I call? Only Car methods (compile-time check)
myCar.accelerate(50);  // OK - Car has this
// myCar.enableTurbo();  // ERROR - Car doesn't have this

// What runs? SportsCar's version (runtime decision)
myCar.accelerate(50);  // SportsCar's accelerate runs!
```

Think of it like this:
- The label on the box says "Car" (compile-time type)
- Inside the box is a SportsCar (runtime type)
- You can only ask for what the label promises
- But you get behavior from what's actually inside

### Struggle 3: Constructor Chaining Complexity

**The confusion:** "When do I use `super()` vs `this()`? Which comes first?"

**Rules:**
1. `super()` or `this()` MUST be the first statement
2. You can use ONLY ONE (not both)
3. If you use neither, Java adds `super()` automatically

```java
public class SportsCar extends Car {
    private boolean turbo;

    // Uses super() - calls parent constructor
    public SportsCar(String brand, String model, int year, boolean turbo) {
        super(brand, model, year, 300);  // FIRST LINE
        this.turbo = turbo;
    }

    // Uses this() - calls another SportsCar constructor
    public SportsCar(String brand, String model, int year) {
        this(brand, model, year, false);  // FIRST LINE
    }

    // CANNOT do both:
    // public SportsCar() {
    //     super("Unknown", "Unknown", 2020, 200);
    //     this("Ferrari", "488", 2023);  // ERROR - second call!
    // }
}
```

### Struggle 4: Abstract Class Instantiation Restrictions

**The confusion:** "Why can't I create an Animal if I defined the Animal class?"

**The answer:** Abstract classes are incomplete templates. They have abstract methods with no implementation. You cannot create something incomplete.

```java
public abstract class Animal {
    public abstract void makeSound();  // No body! Not implemented!
}

Animal a = new Animal("Generic");  // ERROR! What would makeSound() do?

Animal dog = new Dog("Buddy");  // OK! Dog HAS a makeSound() implementation
```

**Analogy:** An abstract class is like a job description. You can't hire "a generic employee" - you hire a specific person (Software Engineer, Designer, Manager) who fulfills the job description.

### Struggle 5: instanceof and Casting Safety

**The confusion:** "My cast crashed even though I knew it was the right type!"

**The problem:** You didn't CHECK first:

```java
// DANGEROUS
public void process(Car car) {
    SportsCar sports = (SportsCar) car;  // CRASH if car isn't a SportsCar!
}

// SAFE
public void process(Car car) {
    if (car instanceof SportsCar) {  // Check first!
        SportsCar sports = (SportsCar) car;  // Now safe
        sports.enableTurbo();
    }
}
```

**Rule:** ALWAYS use `instanceof` before casting down the hierarchy.

---

## Practice Exercises

### Exercise 1: Kinds of Animal (meget hjaelp - Maximum Guidance)

**Goal:** Practice basic inheritance with the `extends` keyword.

**Part A: Create the Animal hierarchy**

```java
// Parent class
public abstract class Animal {
    private String name;
    private int age;

    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getters
    public String getName() { return name; }
    public int getAge() { return age; }

    // Abstract method - subclasses must implement
    public abstract void makeSound();

    // Concrete method - inherited by all
    public void sleep() {
        System.out.println(name + " is sleeping...");
    }
}
```

**Part B: Create Dog subclass**

```java
public class Dog extends Animal {
    private String breed;

    // TODO: Constructor that calls super() and sets breed

    // TODO: Getter for breed

    // TODO: Implement makeSound() - dogs bark

    // TODO: Add fetch() method - dog-specific behavior
}
```

**Part C: Create Cat subclass**

```java
public class Cat extends Animal {
    private boolean isIndoor;

    // TODO: Constructor

    // TODO: Getter for isIndoor

    // TODO: Implement makeSound() - cats meow

    // TODO: Add scratch() method - cat-specific behavior
}
```

**Part D: Test the hierarchy**

```java
public class AnimalDemo {
    public static void main(String[] args) {
        Dog dog = new Dog("Buddy", 3, "Labrador");
        Cat cat = new Cat("Whiskers", 5, true);

        // Test inherited methods
        System.out.println(dog.getName());  // From Animal
        dog.sleep();                        // From Animal

        // Test overridden methods
        dog.makeSound();  // Bark!
        cat.makeSound();  // Meow!

        // Test subclass-specific methods
        dog.fetch();
        cat.scratch();
    }
}
```

### Exercise 2: Authors and Books (nogen hjaelp - Moderate Guidance)

**Goal:** Practice one-to-many relationships and inheritance together.

Create a system where:
- `Person` class with name and age
- `Author` extends `Person`, adds ArrayList of books written
- `Book` class with title, year, and reference to author
- Author can have many books (one-to-many)

**Requirements:**
- Author has `addBook()`, `getBookCount()`, `getBooks()`
- Book has `getAuthor()` that returns the Author object
- Override `toString()` for both classes
- `Author.getBookTitles()` returns comma-separated list of book titles

**Test scenario:**
- Create author "J.K. Rowling", age 58
- Add 3 Harry Potter books to her
- Print the author (should show book count)
- Print each book (should show author name)

### Exercise 3: AnimalsActingSpecifically (nogen hjaelp - Moderate Guidance)

**Goal:** Practice polymorphism, instanceof, and casting.

**Part A: Extend the Animal hierarchy**

Add these classes to Exercise 1's hierarchy:
- `Bird extends Animal` - can `fly()` and `sing()`
- `Fish extends Animal` - can `swim()` and `blow bubbles`

**Part B: Create a polymorphic method**

```java
public class AnimalShelter {
    private Animal[] animals;
    private int count;

    public AnimalShelter(int capacity) {
        animals = new Animal[capacity];
        count = 0;
    }

    public void addAnimal(Animal animal) {
        if (count < animals.length) {
            animals[count++] = animal;
        }
    }

    // TODO: makeAllSound() - iterate and call makeSound() on each

    // TODO: countByType() - returns count of dogs, cats, birds, fish

    // TODO: doSpecificAction(Animal a) - uses instanceof to call
    //       the specific action: fetch/scratch/fly/swim
}
```

**Part C: Test polymorphism**

```java
public class ShelterDemo {
    public static void main(String[] args) {
        AnimalShelter shelter = new AnimalShelter(10);

        shelter.addAnimal(new Dog("Max", 3, "German Shepherd"));
        shelter.addAnimal(new Cat("Luna", 2, false));
        shelter.addAnimal(new Bird("Tweety", 1));
        shelter.addAnimal(new Dog("Bella", 5, "Golden Retriever"));
        shelter.addAnimal(new Fish("Nemo", 1));

        // All animals make their sound (polymorphism!)
        shelter.makeAllSound();

        // Each animal does its specific action
        for (Animal a : shelter.getAnimals()) {
            shelter.doSpecificAction(a);
        }
    }
}
```

### Exercise 4: Loan Items (ingen hjaelp - Minimal Guidance)

**Goal:** Design a complete inheritance hierarchy with abstract class.

Create a library loan system:

**Requirements:**
- `LoanItem` abstract class with: title, item ID, checkout date, due date
- `Book extends LoanItem` with: author, ISBN, page count
- `DVD extends LoanItem` with: director, duration, rating
- `Magazine extends LoanItem` with: issue number, publication date

**Behavior:**
- All loan items can be `checkOut()` and `returnItem()`
- Abstract method `calculateLateFee()` - each type calculates differently:
  - Books: $0.25 per day late
  - DVDs: $1.00 per day late
  - Magazines: $0.10 per day late
- `isOverdue()` checks if current date > due date

**Advanced:**
- Create `Library` class with ArrayList<LoanItem>
- `getTotalLateFees()` - sum of all overdue items' fees
- `getOverdueItems()` - returns ArrayList of only overdue items
- `searchByTitle(String keyword)` - returns items with matching title

**Demo:**
- Create library with mix of books, DVDs, magazines
- Check out several items with different due dates
- Calculate total late fees
- Print all overdue items
- Search for items by title

---

## Looking Ahead

This week you mastered the final pillars of object-oriented programming: inheritance and polymorphism. Combined with Week 7's classes and Week 8's encapsulation, you now have a complete OOP foundation.

**In Week 10 (Additional OOP Topics):**
- Wrapper classes (Integer, Double, etc.) and autoboxing
- The relationship between primitives and objects
- Enhanced for loops and ArrayList features
- More on static members

**In Week 14-15 (Sorting and Interfaces):**
- Interfaces take polymorphism further - define behavior contracts
- Comparable interface for natural ordering
- Comparator interface for custom sorting
- Interface vs abstract class decisions

Your inheritance hierarchies (Car/Vehicle, Student, Animal) will continue to grow. The polymorphic patterns you learned this week are the foundation for:
- Implementing interfaces
- Working with Java collections
- Understanding exception hierarchies (Week 12)
- Building flexible, extensible software

---

## Key Takeaways

1. **Inheritance** creates IS-A relationships: `SportsCar IS-A Car`

2. **`extends` keyword** creates a subclass that inherits from a superclass

3. **`super()` in constructors** calls the parent constructor - MUST be first line

4. **`super.method()`** calls the parent's version of an overridden method

5. **Method overriding** replaces inherited behavior with subclass-specific implementation

6. **Always use `@Override`** annotation - catches errors and documents intent

7. **`protected` access** allows subclass access, unlike `private`

8. **Abstract classes** cannot be instantiated; define templates for subclasses

9. **Polymorphism** = one interface, many forms (one method call, different behaviors)

10. **Compile-time type** determines what you CAN call; **runtime type** determines what RUNS

11. **`instanceof`** checks the actual type at runtime - ALWAYS use before downcasting

12. **Upcasting** (child to parent) is automatic and safe; **downcasting** requires explicit cast and `instanceof` check

13. **All classes extend Object** - inherit toString(), equals(), hashCode()

14. **Use inheritance for IS-A relationships; use composition for HAS-A relationships**

---

## For the Next Topic Agent

### Terminology Established This Week

- **inheritance**: A mechanism where a subclass inherits members from a superclass
- **superclass/parent class**: The class being inherited from
- **subclass/child class**: The class that inherits from another class
- **extends**: Keyword to declare inheritance relationship
- **super**: Keyword to reference parent class (constructor or methods)
- **method overriding**: Providing new implementation for inherited method
- **@Override annotation**: Declares intent to override and enables compiler checking
- **protected access modifier**: Accessible in same class, same package, and subclasses
- **abstract class**: Class that cannot be instantiated, may have abstract methods
- **abstract method**: Method declared without implementation
- **polymorphism**: Ability of one interface to be used for multiple forms
- **dynamic method dispatch**: Runtime selection of which method implementation to execute
- **compile-time type**: The declared type of a variable
- **runtime type**: The actual type of the object a variable references
- **instanceof operator**: Tests if an object is an instance of a specific class
- **upcasting**: Converting child reference to parent type (automatic)
- **downcasting**: Converting parent reference to child type (explicit cast required)
- **IS-A relationship**: Inheritance relationship (SportsCar IS-A Car)
- **HAS-A relationship**: Composition relationship (Car HAS-A Engine)

### Inheritance Hierarchies Created

1. **Vehicle Hierarchy**
   ```
   Car (from Week 8)
   ├── SportsCar (turboEnabled, enhanced acceleration)
   └── ElectricCar (batteryCapacity, regenerative braking)
   ```

2. **Person/Student Hierarchy**
   ```
   Student (from Week 8)
   └── GraduateStudent (thesisTopic, advisor, publications, isTA)
   ```

3. **Die Hierarchy**
   ```
   Die (from Week 8)
   └── LoadedDie (favoredValue, biasStrength, biased roll)
   ```

4. **Animal Hierarchy (exercises)**
   ```
   Animal (abstract)
   ├── Dog (breed, fetch(), bark)
   ├── Cat (isIndoor, scratch(), meow)
   ├── Bird (fly(), sing())
   └── Fish (swim(), bubbles)
   ```

5. **LoanItem Hierarchy (exercises)**
   ```
   LoanItem (abstract)
   ├── Book (author, ISBN, pages, $0.25/day late fee)
   ├── DVD (director, duration, rating, $1.00/day late fee)
   └── Magazine (issueNumber, pubDate, $0.10/day late fee)
   ```

### Student Capabilities After This Week

Students can now:
- Design and implement inheritance hierarchies using `extends`
- Use `super()` to properly chain constructors
- Override methods using `@Override` annotation
- Apply the `protected` access modifier appropriately
- Create and use abstract classes and methods
- Understand and apply polymorphism with parent type references
- Safely use `instanceof` and casting for type-specific operations
- Distinguish between compile-time and runtime types
- Choose between inheritance (IS-A) and composition (HAS-A)

### Critical Concepts for Week 10 (Advanced OOP Topics)

Week 10 should build on:
- **Wrapper classes** relate to polymorphism - Integer, Double extend Number
- **Autoboxing** relates to type conversion in polymorphic contexts
- **ArrayList generic types** work with inheritance (ArrayList<Car> can hold SportsCar)
- **Static members** and how they interact with inheritance (not polymorphic!)

### Critical Concepts for Weeks 14-15 (Interfaces)

Inheritance prepares students for interfaces:
- **Interfaces** are like abstract classes with ALL abstract methods
- **implements** keyword (vs `extends`)
- **Multiple interfaces** (Java's alternative to multiple inheritance)
- **Comparable** interface uses polymorphism for sorting
- **Abstract class vs interface** decision criteria

### Common Misconceptions to Address in Week 10

- "Wrapper classes inherit from primitives" - No, primitives are not objects
- "Static methods are polymorphic" - No, static methods are bound at compile time
- "I can override a static method" - No, you can only hide it (different concept)
- "ArrayList<Car> and ArrayList<SportsCar> are related" - Generics don't work that way!

### Assessment Preparation Notes

This topic comprises 40-50% of exam content. Key exam patterns:
1. Given a hierarchy, identify IS-A relationships
2. Trace method calls through polymorphic references
3. Identify compile-time vs runtime types
4. Write proper `super()` constructor calls
5. Implement abstract methods in concrete classes
6. Use `instanceof` and casting correctly
7. Override `toString()` and `equals()` properly
