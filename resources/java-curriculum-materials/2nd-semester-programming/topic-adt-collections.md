# Abstract Data Types & Collections Framework - 2nd Semester Programming

*Prerequisites: 1st Semester Java (ArrayList, OOP, interfaces, Comparable)*
*Phase: 1 - Foundation & Data Structures*
*Exam Weight: Moderate (ADT concepts) to High (Collections usage)*

---

## What You'll Learn

By the end of this topic, you will be able to:
- **Think abstractly** about data structures by separating *what* they do from *how* they work
- **Choose the right collection** (List, Set, Map) based on your application's needs
- **Analyze performance** using Big-O notation to make informed implementation choices
- **Traverse collections safely** using the Iterator pattern
- **Write type-safe code** using generic type parameters

These skills form the foundation for everything you'll build this semester: database results will be stored in Collections, web applications will pass Collections to templates, and your project code quality will depend on choosing appropriate data structures.

---

## Why This Matters

### The Real-World Problem

Imagine you're building the Kailua Car Rental system. You need to manage:
- A collection of available cars
- A list of customers
- A set of unique license plates (no duplicates allowed)
- A mapping from rental contract IDs to contract details

Each of these requires a different data structure. Using the wrong one doesn't just make your code messy - it can make your application slow or even incorrect.

### Collections Appear Everywhere

Throughout this semester, you'll use Collections in three distinct contexts:

1. **Console Applications** (Kailua Project): `ArrayList<Car> inventory`, `List<RentalContract> contracts`
2. **Database Results**: `List<Customer> customers = jdbcTemplate.query(sql, rowMapper)`
3. **Web Applications**: Passing `List<Wishlist> wishlists` from Controller to Thymeleaf template

The same abstract concepts (List, Set, Map) apply in all contexts. Master them now, and they'll serve you through database integration, web development, and beyond.

### Connection to Your Exam

At the oral exam, you'll be asked to:
- Explain *why* you chose a particular collection type
- Justify your data structure selection based on performance requirements
- Demonstrate understanding of the distinction between abstract concepts and concrete implementations

This isn't about memorizing syntax - it's about demonstrating architectural thinking.

---

## Building on What You Know

### From 1st Semester

You've already used `ArrayList` extensively. Think back to code like this:

```java
ArrayList<String> names = new ArrayList<>();
names.add("Alice");
names.add("Bob");
String first = names.get(0);
```

You know *how* to use ArrayList. This semester, we'll understand *what ArrayList really is* - one specific implementation of the abstract concept "List."

You also implemented `Comparable` for sorting objects. That experience with interfaces prepares you for understanding how the Collections Framework uses interfaces to define behavior.

### The Conceptual Shift

In 1st semester, you thought: "I need an ArrayList to store my cars."

This semester, you'll think: "I need a **List** to store my cars. ArrayList is one way to implement that List - but there are others, and the choice matters."

This shift from *implementation* to *abstraction* is fundamental to professional software development.

---

## Understanding Abstract Data Types (ADT)

### What Is an Abstract Data Type?

An Abstract Data Type (ADT) is a **mathematical model** for a data structure that defines:
- **What operations** can be performed (add, remove, get, contains)
- **What behavior** those operations have (add puts an element at the end)

An ADT does **not** define:
- How data is stored in memory
- What algorithms implement the operations
- Performance characteristics

Think of an ADT like a *contract*. It says "here's what you can do" without saying "here's how it works internally."

### Why Do We Need This Abstraction?

Consider this scenario: You write a car rental application using `ArrayList<Car>`. Later, you discover that searching for cars by license plate is slow because ArrayList requires checking every element.

Without ADT thinking, you're stuck rewriting your entire application.

With ADT thinking, you wrote code against the `List` interface. Now you can swap `ArrayList` for a different implementation without changing any code that *uses* the list.

**This is the power of abstraction: flexibility to change implementations without breaking your application.**

### The Interface-Implementation Distinction

In Java, this abstraction is implemented through **interfaces**:

| Level | Java Concept | Example |
|-------|--------------|---------|
| **Abstract** (What) | Interface | `List`, `Set`, `Map` |
| **Concrete** (How) | Class | `ArrayList`, `HashSet`, `HashMap` |

When you write:
```java
List<Car> cars = new ArrayList<>();
```

You're saying: "I need something that behaves like a List. I'll use ArrayList for now, but my code only depends on List behavior."

### Seeing ADT Separation in Action

```java
// POOR PRACTICE: Declaring with implementation type
ArrayList<Customer> customers = new ArrayList<>();

// GOOD PRACTICE: Declaring with interface type (ADT)
List<Customer> customers = new ArrayList<>();
```

**Why the second approach is better:**

1. **Flexibility**: You can change `ArrayList` to `LinkedList` without touching other code
2. **Clarity**: Anyone reading knows you only need List operations
3. **Testability**: You can mock the List interface in unit tests
4. **GRASP Principle**: This is "programming to interfaces" - achieving Low Coupling

### Common Mistakes

**Mistake: Thinking ArrayList *is* a List**

ArrayList is an *implementation of* List. The relationship is "is-a" in the inheritance sense, but conceptually they're at different levels:
- List is the *abstract concept*
- ArrayList is the *concrete reality*

**Mistake: Ignoring the interface**

```java
// Wrong mindset:
"I'll use ArrayList because that's what I learned"

// Correct mindset:
"I need ordered elements with duplicates allowed - that's a List.
ArrayList gives me O(1) access by index, which I need here."
```

---

## Java Collections Framework Interfaces

### The Big Picture

The Java Collections Framework provides a unified architecture for representing and manipulating collections. At its core are four main interfaces:

| Interface | Purpose | Duplicates? | Ordered? | Key Operations |
|-----------|---------|-------------|----------|----------------|
| **List** | Sequential elements | Yes | Yes (by index) | get(index), add(index, element) |
| **Set** | Unique elements | No | Varies | add(), contains() |
| **Map** | Key-value pairs | Keys: No | Varies | put(key, value), get(key) |
| **Queue** | Processing order | Yes | Yes (FIFO/priority) | offer(), poll(), peek() |

### When to Use Each Type

**Use List when:**
- Order matters (first customer in line should be served first)
- Duplicates are allowed or expected
- You need to access elements by position

*Kailua Example*: `List<RentalContract> contracts` - contracts have a sequence, and the same car could have multiple rental periods

**Use Set when:**
- You need guaranteed uniqueness
- You frequently check "is X in the collection?"
- Order doesn't matter (or you want sorted order with TreeSet)

*Kailua Example*: `Set<String> licensePlates` - each license plate must be unique

**Use Map when:**
- You need to look up values by a unique key
- You're modeling relationships (ID to object)
- You need fast retrieval by identifier

*Kailua Example*: `Map<Integer, Customer> customersById` - quickly find customer by their ID

### The Interface Hierarchy

```
                    Iterable<E>
                        |
                   Collection<E>
                   /    |    \
               List<E> Set<E> Queue<E>

                    Map<K,V>  (separate hierarchy)
```

All collections (except Map) extend `Collection`, which extends `Iterable`. This means everything can be traversed with an Iterator or enhanced for-loop.

### Concrete Implementations Overview

Each interface has multiple implementations with different characteristics:

**List Implementations:**
- `ArrayList`: Array-backed, fast random access, slow insertion in middle
- `LinkedList`: Node-based, fast insertion/deletion, slow random access

**Set Implementations:**
- `HashSet`: Hash table-backed, unordered, fastest operations
- `TreeSet`: Red-black tree, sorted order, O(log n) operations

**Map Implementations:**
- `HashMap`: Hash table-backed, unordered, fastest operations
- `TreeMap`: Red-black tree, sorted by key, O(log n) operations

---

## Big-O Complexity: Choosing Wisely

### What Is Big-O Notation?

Big-O notation describes how an algorithm's time or space requirements **grow** as input size increases. It's not about milliseconds - it's about scalability.

| Notation | Name | Meaning | Example |
|----------|------|---------|---------|
| O(1) | Constant | Same time regardless of size | HashMap.get() |
| O(log n) | Logarithmic | Doubles input, adds one step | TreeMap.get() |
| O(n) | Linear | Time grows proportionally | ArrayList.contains() |
| O(n log n) | Linearithmic | Efficient sorting | Collections.sort() |
| O(n^2) | Quadratic | Nested loops over data | Bubble sort |

### ArrayList vs LinkedList: The Classic Comparison

This comparison illustrates why implementation choice matters:

| Operation | ArrayList | LinkedList |
|-----------|-----------|------------|
| get(index) | **O(1)** - direct array access | O(n) - must traverse |
| add(end) | **O(1)** amortized | **O(1)** - add to tail |
| add(middle) | O(n) - shift elements | **O(1)** - relink nodes |
| contains() | O(n) - linear search | O(n) - linear search |

**Practical Guidance:**
- Use `ArrayList` by default (90% of cases)
- Use `LinkedList` when you frequently insert/remove from the middle and rarely access by index

### HashSet vs TreeSet

| Operation | HashSet | TreeSet |
|-----------|---------|---------|
| add() | **O(1)** average | O(log n) |
| contains() | **O(1)** average | O(log n) |
| Iteration order | Unpredictable | Sorted |

**When to use TreeSet:** You need elements in sorted order, or you need operations like "find all elements greater than X."

### Making Performance Decisions

In your Kailua project, consider:

```java
// If you frequently search for customers by ID:
Map<Integer, Customer> customers = new HashMap<>();  // O(1) lookup

// If you need customers sorted by name:
Map<String, Customer> customers = new TreeMap<>();  // O(log n) but sorted

// If you just need to iterate through all customers:
List<Customer> customers = new ArrayList<>();  // Simple, fast iteration
```

The right choice depends on your *usage patterns*, not just what feels familiar.

---

## The Iterator Pattern

### What Problem Does Iterator Solve?

Consider this code:

```java
List<Car> cars = getAvailableCars();
for (int i = 0; i < cars.size(); i++) {
    Car car = cars.get(i);
    // process car
}
```

This works for ArrayList, but what if `cars` is a LinkedList? The `get(i)` operation is O(n), making the whole loop O(n^2)!

The Iterator pattern provides a **uniform way** to traverse any collection without knowing its internal structure.

### Using Iterators

```java
List<Car> cars = getAvailableCars();
Iterator<Car> iterator = cars.iterator();

while (iterator.hasNext()) {
    Car car = iterator.next();
    // process car
}
```

This code works efficiently regardless of whether `cars` is an ArrayList, LinkedList, or any other List implementation.

### The Enhanced For-Loop

Java's enhanced for-loop uses Iterator internally:

```java
for (Car car : cars) {
    // This uses Iterator behind the scenes
}
```

This is the preferred syntax when you don't need to remove elements during iteration.

### Safe Removal with Iterator

**The Problem: ConcurrentModificationException**

```java
// WRONG: Will throw ConcurrentModificationException
for (Car car : cars) {
    if (car.isOutOfService()) {
        cars.remove(car);  // Modifying collection during iteration!
    }
}
```

**The Solution: Use Iterator.remove()**

```java
// CORRECT: Safe removal during iteration
Iterator<Car> iterator = cars.iterator();
while (iterator.hasNext()) {
    Car car = iterator.next();
    if (car.isOutOfService()) {
        iterator.remove();  // Remove through the iterator
    }
}
```

This is a common exam topic. Know why ConcurrentModificationException occurs and how to avoid it.

---

## Generic Type Parameters

### Why Generics Exist

Before Java 5, collections stored `Object` references:

```java
List cars = new ArrayList();
cars.add(new Car("Toyota"));
cars.add("Oops, a String!");  // Compiles! Runtime error later...

Car car = (Car) cars.get(0);  // Explicit cast required
```

Generics provide **compile-time type safety**:

```java
List<Car> cars = new ArrayList<>();
cars.add(new Car("Toyota"));
cars.add("Oops");  // COMPILE ERROR - caught early!

Car car = cars.get(0);  // No cast needed
```

### Reading Generic Syntax

```java
List<Car>           // "a List of Car objects"
Map<String, Car>    // "a Map from String keys to Car values"
List<?>             // "a List of unknown type" (wildcard)
```

### The Diamond Operator

Since Java 7, you can omit the type on the right side:

```java
// Before Java 7:
List<Car> cars = new ArrayList<Car>();

// Java 7+: Diamond operator infers the type
List<Car> cars = new ArrayList<>();
```

### Bounded Type Parameters (Preview)

You'll see this in Spring Boot code:

```java
public <T extends Comparable<T>> void sort(List<T> list)
```

This means: "T must be a type that implements Comparable." You don't need to write such code yet, but you should recognize it.

---

## Integration Patterns

### How Collections Connect Technologies

Collections are the universal mechanism for moving data between application layers:

```
[Database]                                      [Browser]
    |                                               ^
    v                                               |
SQL Query → ResultSet → RowMapper → List<Domain> → Controller → Model → Thymeleaf → HTML
                            |
                     Collections!
```

### Pattern 1: Database to Java

When you query the database, results come back as a `List`:

```java
// In your Repository class
public List<Customer> findAll() {
    String sql = "SELECT * FROM customer";
    return jdbcTemplate.query(sql, new CustomerRowMapper());
}
```

The `RowMapper` converts each database row to a Java object. The result is a `List<Customer>` - a Collection you already understand!

### Pattern 2: Java to Web Template

Controllers pass Collections to Thymeleaf templates:

```java
// In your Controller
@GetMapping("/customers")
public String listCustomers(Model model) {
    List<Customer> customers = customerService.findAll();
    model.addAttribute("customers", customers);  // Collection in Model
    return "customer-list";
}
```

### Pattern 3: Thymeleaf Iteration

Templates iterate over Collections:

```html
<!-- In customer-list.html -->
<table>
    <tr th:each="customer : ${customers}">
        <td th:text="${customer.name}">Name</td>
        <td th:text="${customer.email}">Email</td>
    </tr>
</table>
```

The `th:each` attribute uses Iterator internally to traverse your Collection.

### Data Flow Visualization

```
[User requests /customers]
         |
         v
[@GetMapping method called]
         |
         v
[Service.findAll() returns List<Customer>]
         |
         v
[model.addAttribute("customers", list)]
         |
         v
[Thymeleaf processes template]
         |
         v
[th:each iterates over List]
         |
         v
[HTML table rows generated]
         |
         v
[Browser displays customer list]
```

---

## Common Struggles and How to Overcome Them

### Struggle 1: Confusing Interface (List) with Implementation (ArrayList)

**Why this confuses students:** In 1st semester, you always wrote `ArrayList<String>`. Now we're saying to write `List<String>`. It feels like extra complexity.

**How to think about it:** The interface is what you *need*. The implementation is what you *choose*. When declaring variables and parameters, express what you need. When creating objects, choose how to provide it.

**Strategy:** When writing code, ask: "Do I care *how* this collection works, or just *what* it does?" If you only care about adding and getting elements, use `List`. The implementation choice (`new ArrayList<>()`) is separate.

**Exam tip:** When asked "why did you use ArrayList?", don't just say "because it stores things." Say "I needed a List for ordered elements, and ArrayList provides O(1) index access which I needed for quick lookups."

### Struggle 2: Not Understanding Why ADT Abstraction Is Valuable

**Why this confuses students:** For small programs, the flexibility seems unnecessary. Why not just use ArrayList everywhere?

**How to think about it:** Professional applications change. Requirements change. By programming to interfaces, you can adapt without rewriting. It's an investment in future flexibility.

**Strategy:** Think about the Wishlist project. What if you later need to ensure unique items? If you coded to `Collection`, you could switch from `ArrayList` to `HashSet`. If you hardcoded `ArrayList`, you'd rewrite everything.

**Exam tip:** Connect to GRASP's Low Coupling principle: "Programming to interfaces reduces coupling between components, making the system more maintainable."

### Struggle 3: Difficulty Choosing Between Set, List, and Map

**Why this confuses students:** The differences seem subtle, and ArrayList "works" for everything.

**How to think about it:** Use a decision tree:
1. Do I need key-value pairs? **Yes = Map**
2. Must elements be unique? **Yes = Set**
3. Do I need ordered access by index? **Yes = List**

**Strategy:** Practice by describing your data in plain English before coding:
- "I need a collection of cars" = probably List
- "I need unique license plates" = Set
- "I need to find customers by their ID" = Map

**Exam tip:** Be able to justify your choice with a specific reason: "I chose Set because license plates must be unique and duplicate plates would indicate a data error."

### Struggle 4: Understanding When to Use LinkedList vs ArrayList

**Why this confuses students:** Big-O notation is abstract and hard to apply.

**How to think about it:** ArrayList is like a bookshelf where books have numbered slots. Finding book #47 is instant, but inserting a new book in the middle means moving every book after it.

LinkedList is like a train where each car is connected to the next. To find car #47, you must walk through 46 cars. But adding a new car between two existing ones just requires reconnecting two links.

**Strategy:** Default to ArrayList. Only consider LinkedList if profiling shows that middle insertions are a bottleneck.

**Exam tip:** "ArrayList is my default choice because random access is O(1). I would consider LinkedList if I had frequent insertions/deletions in the middle of a large collection and rarely needed random access."

### Struggle 5: Iterator ConcurrentModificationException Issues

**Why this confuses students:** The for-each loop hides the Iterator, so the error seems mysterious.

**How to think about it:** When you iterate, the Iterator has expectations about the collection's state. If something changes the collection behind its back, the Iterator can't guarantee correct behavior, so it fails fast.

**Strategy:** When you need to remove during iteration, use `iterator.remove()`. When modifying is complex, build a list of items to remove, then remove them after the loop.

**Exam tip:** "ConcurrentModificationException occurs when the collection is structurally modified outside the Iterator. The solution is to use Iterator.remove() for safe removal during traversal."

### Struggle 6: Seeing Collections in Multiple Contexts Causes Confusion

**Why this confuses students:** Collections appear in console apps, then with databases, then with web templates. It can seem like they're different things in different contexts.

**How to think about it:** Collections are always the same. They're Java's way of grouping objects. What changes is *where the data comes from* and *where it goes*.

**Strategy:** When you see `List<Customer>` in any context, ask:
- Where does this data come from? (User input? Database? Hardcoded?)
- Where is this data going? (Display? Save to DB? Pass to another method?)

The Collection is just the container. It doesn't know or care about its context.

**Exam tip:** "Collections serve as the universal data transport mechanism in Java applications. The same List that holds database results can be passed to a web template for display."

---

## Practice Exercises

### Exercise 1: 1st Semester Repetition (Maximum Guidance)

**What you'll build:** Review exercises to refresh core Java OOP skills and ArrayList operations.

**Connection to Kailua:** These foundational skills are directly applied when building the car rental system.

**Skills you'll practice:**
- ArrayList manipulation (add, get, remove, size)
- Object-oriented design
- Basic algorithms with Collections

**Step-by-step approach:**
1. Create a `Car` class with attributes: licensePlate, brand, model, pricePerDay
2. Implement getters and a meaningful `toString()` method
3. Create an `ArrayList<Car>` and add several car objects
4. Write a method `findCarByPlate(List<Car> cars, String plate)` that returns the matching Car or null
5. Write a method `filterByBrand(List<Car> cars, String brand)` that returns a new List containing only cars of that brand

**Hints:**
- Use enhanced for-loop for iteration
- Remember: return type should be `List<Car>`, not `ArrayList<Car>`
- Consider what happens if no car matches - should you return null or an empty list?

**What success looks like:** You can add cars to a list, search for specific cars, and filter cars by criteria. Your code uses `List` interface types in method signatures.

---

### Exercise 2: Collection Type Selection (Moderate Guidance)

**What you'll build:** A small system that uses List, Set, and Map appropriately.

**Skills you'll practice:**
- Choosing appropriate collection types
- Interface-based programming
- Understanding uniqueness and key-value relationships

**Approach:** Create a simple order management system with:
- A List of orders (ordered by submission time)
- A Set of unique customer emails
- A Map from order ID to Order object

Implement methods to:
- Add a new order (should also register customer email)
- Find an order by ID
- Get all unique customer emails
- List all orders

**Key concepts to apply:**
- List for ordered sequences with potential duplicates
- Set for automatic uniqueness enforcement
- Map for O(1) lookup by key

**Success criteria:** You can explain why you chose each collection type for its purpose.

---

### Exercise 3: Custom LinkedIntList (Minimal Guidance)

**What you'll build:** Your own implementation of a linked list for integers.

**Requirements:**
- Create a `Node` class with an `int value` and a `Node next` reference
- Create a `LinkedIntList` class that manages a chain of Nodes
- Implement: `addFirst(int)`, `addLast(int)`, `size()`, `get(int index)`, `toString()`

**Skills you'll practice:**
- Understanding node-based data structures internally
- Reference manipulation
- Edge case handling (empty list, single element, end of list)

You'll implement this independently. This exercise provides deep understanding of how LinkedList works internally.

---

## Preparing for the Oral Exam

### Key Questions You Should Be Able to Answer

- "Why did you choose ArrayList instead of LinkedList here?"
- "Explain the difference between a List and an ArrayList."
- "When would you use a Set instead of a List?"
- "What's the time complexity of looking up a customer by ID in your system?"
- "How does the Iterator pattern help when working with collections?"
- "What GRASP principles relate to interface-based programming?"

### Demo Tips

When demonstrating Collections in your project:

1. **Show the declaration:** Point out that you declared `List<Car>` not `ArrayList<Car>` and explain why
2. **Trace the data flow:** Show how a Collection moves from database query to web display
3. **Explain your choices:** Be ready to justify why you chose a particular collection type
4. **Discuss alternatives:** "I could have used a Set here, but I needed to maintain insertion order"

### What NOT to Do

- Don't just describe syntax: "This line creates an ArrayList"
- Don't focus on memorized definitions without application
- Don't say "I just used ArrayList because that's what we learned"

### What TO Do

- Explain the design decision: "I used Map<String, Customer> because I needed O(1) lookup by customer ID"
- Connect to principles: "This follows the Low Coupling principle because I'm programming to the List interface"
- Show understanding of tradeoffs: "ArrayList gives me fast random access at the cost of slow middle insertions"

---

## Looking Ahead

### What You Can Do Now

- Choose appropriate collection types based on use case
- Write flexible code using interface types
- Analyze performance implications of collection choices
- Traverse collections safely with Iterator
- Use generics for type-safe collections

### How This Will Be Used in Upcoming Topics

- **Database-Java Integration**: JdbcTemplate returns `List<DomainObject>` from database queries. RowMapper converts each row to an object in your collection.

- **Spring Boot Fundamentals**: Controllers pass Collections to templates via Model. `model.addAttribute("items", itemList)` moves your Collection to the view layer.

- **Thymeleaf Templating**: `th:each="item : ${itemList}"` iterates over your Collection to generate HTML.

- **Algorithm Analysis**: Big-O concepts introduced here are expanded with practical measurement and comparison of sorting algorithms.

### Project Connection

**Kailua Car Rental (Phase 4):**
- `List<Car> availableCars` - managing car inventory
- `Map<Integer, Customer> customers` - fast customer lookup
- `Set<String> licensePlates` - ensuring uniqueness

**Onskeskyen Wishlist (Phase 7):**
- `List<Wishlist> wishlists` - user's wishlists
- `List<WishlistItem> items` - items in a wishlist
- `Map<Integer, User> users` - session user lookup

---

## Key Takeaways

- **Abstract Data Types (ADT)**: Separate *what* a data structure does from *how* it does it. Program to interfaces (List) not implementations (ArrayList).

- **Collection Selection**: List for ordered sequences, Set for uniqueness, Map for key-value lookup. Choose based on your actual needs.

- **Big-O Awareness**: Understand that ArrayList.get() is O(1) while LinkedList.get() is O(n). Performance differences matter at scale.

- **Iterator Pattern**: Provides safe, uniform traversal of any collection. Use `iterator.remove()` when modifying during iteration.

- **Generics**: Provide compile-time type safety. `List<Car>` catches type errors early.

**For the exam:** Be able to explain *why* you chose a particular collection type in your project, connecting to performance requirements and design principles.

---

## For the Next Topic Agent

### Terminology Established This Topic

- **Abstract Data Type (ADT)**: A mathematical model defining operations and behavior without specifying implementation. In Java, represented by interfaces.

- **Interface-Based Programming**: Declaring variables and parameters using interface types (List) rather than implementation types (ArrayList). Achieves Low Coupling.

- **Big-O Notation**: Mathematical notation describing how algorithm performance scales with input size. Common complexities: O(1) constant, O(n) linear, O(log n) logarithmic.

- **Iterator Pattern**: Design pattern providing uniform traversal mechanism for collections without exposing internal structure.

- **Generics**: Java's type parameter system (`<T>`) enabling compile-time type safety for collections.

- **Collection**: Generic term for data structures that group objects. In Java, also a specific interface extended by List, Set, and Queue.

### Example Classes/Concepts Created

- **Car class**: Domain object with licensePlate, brand, model, pricePerDay. Used throughout semester as example domain entity.

- **Node class**: For LinkedIntList exercise. Contains `int value` and `Node next`. Demonstrates internal structure of linked lists.

- **LinkedIntList class**: Custom implementation demonstrating node-based structures internally.

- **Collection decision tree**:
  1. Need key-value pairs? Use Map
  2. Need uniqueness? Use Set
  3. Need ordered access? Use List

### Student Capabilities After This Topic

Students who complete this material can now:
- Declare variables using interface types for flexibility
- Select appropriate collection types (List, Set, Map) with justification
- Analyze and compare time complexity of basic operations
- Traverse collections safely using Iterator or enhanced for-loop
- Write type-safe collection code using generics
- Explain the ADT concept and why it matters for maintainability

### Pedagogical Patterns Used

- **Data flow visualization**: Showing how Collections move through application layers (Database -> Java -> Web)

- **Decision tree approach**: Guiding collection type selection through yes/no questions about requirements

- **Contrast with 1st semester**: Building on ArrayList knowledge while elevating to interface thinking

- **Project connection**: Every concept tied to Kailua or Onskeskyen practical applications

- **Big-O as scaling story**: Framing complexity as "what happens when the collection gets big" rather than abstract mathematics

- **Common struggles anticipation**: Week 8 "Collections cleanup" session addresses confusion from seeing Collections in multiple contexts - establish early that Collections are context-independent

- **GRASP integration**: Connect interface-based programming to Low Coupling principle, preparing for deeper GRASP coverage in Phase 6
