# Simple Sorting with Comparable - Week 14

*Prerequisites: Week 6 (Arrays), Weeks 7-10 (Complete OOP Foundation), Week 10 (ArrayList)*
*Phase: Phase 5: Advanced Abstractions*

---

## What You'll Learn

By the end of this week, you will be able to:

- **Understand why sorting matters** and when you need it in real programs
- **Explain natural ordering** - what it means for objects to have a "default" way to be sorted
- **Implement the Comparable interface** to make your own classes sortable
- **Write a correct compareTo() method** that follows the contract
- **Understand return values**: negative, zero, positive and what they mean
- **Use Collections.sort()** to sort ArrayList objects
- **Use Arrays.sort()** to sort arrays
- **Find minimum and maximum values** using sorting
- **Maintain consistency between compareTo() and equals()** (an important detail!)
- **Choose appropriate sort criteria** for your domain objects

**EXAM NOTE**: Sorting and Comparable represent 20-25% of your exam weight. This is important material that you will definitely encounter!

**CONNECTION TO WEEK 6**: Remember arrays from Week 6? Now we learn how to PUT THEM IN ORDER!

**CONNECTION TO WEEK 10**: Remember ArrayList? Now we can sort those too - and sort the objects WE created!

**CONNECTION TO WEEKS 7-10**: Remember the Student and Car classes you built? Now we teach them HOW to compare themselves!

---

## Why This Matters

### The Everyday Need for Order

Think about your daily life. How often do you encounter sorted data?

- Your contacts app shows names in alphabetical order
- Your email shows newest messages first
- Spotify shows your playlists by recently played
- Online stores show products by price (low to high, or high to low)
- Your grades are listed by course name or date
- Leaderboards show players ranked by score

**Without sorting, finding anything would be chaos!**

Imagine searching through 1000 unsorted contacts to find "Maria". You would have to check every single one. But if they are sorted alphabetically, you can jump straight to the M section!

### Why Objects Need to Know How to Compare Themselves

In Week 6, you learned to sort arrays of numbers:

```java
int[] numbers = {5, 2, 8, 1, 9};
Arrays.sort(numbers);
// Now: {1, 2, 5, 8, 9}
```

This works because Java KNOWS how to compare numbers. 2 is less than 5. Simple.

But what about YOUR objects?

```java
Student[] students = {alice, bob, charlie};
Arrays.sort(students);  // ???
```

How should Java sort students? By name? By age? By GPA? By student ID?

**Java does not know! YOU must tell it.**

That is what the Comparable interface does - it lets YOU define how YOUR objects should be compared.

### Real-World Applications

| Domain | Objects | Sorted By |
|--------|---------|-----------|
| University | Students | Name, GPA, Student ID |
| E-commerce | Products | Price, Rating, Name |
| Music App | Songs | Title, Artist, Duration |
| Email | Messages | Date, Sender, Subject |
| Games | Players | Score, Level, Username |
| Banking | Transactions | Date, Amount |

Every application you will ever build will probably need sorting!

---

## Building Your Intuition

### Analogy 1: The Library Card Catalog

Before computers, libraries used card catalogs - drawers full of cards, one for each book, sorted alphabetically by author.

```
LIBRARY CARD CATALOG
    |
    v
[A] Adams, Douglas - Hitchhiker's Guide
[A] Austen, Jane - Pride and Prejudice
[B] Bradbury, Ray - Fahrenheit 451
[C] Christie, Agatha - Murder on the Orient Express
    ...
```

Each card "knows" how to compare itself to other cards - by author's last name. That is natural ordering! The cards have ONE standard way to be sorted.

**In Java terms:**
- Each card = an object (Book)
- The comparison rule (by author) = the compareTo() method
- The Comparable interface = the agreement that cards CAN be compared

### Analogy 2: Racing Numbers

At a marathon, each runner has a bib number. After the race, results are posted.

The default (natural) ordering might be by finish time:
```
1st: Runner #234 - 2:15:30
2nd: Runner #891 - 2:18:45
3rd: Runner #156 - 2:22:10
```

Every Runner object "knows" that when compared to another runner, finish time is what matters.

This is natural ordering - the ONE obvious way to sort runners in race context.

(Later, in Week 15, you will learn about Comparator - which lets you sort the SAME runners by age, by name, or by bib number without changing the Runner class!)

### Analogy 3: The compareTo Contract as Traffic Rules

Think of compareTo() as traffic rules that everyone follows:

**"Who goes first at the intersection?"**

- If I arrived BEFORE you: I go first (negative number = I am "less than")
- If we arrived at the SAME time: We negotiate (zero = we are "equal")
- If I arrived AFTER you: You go first (positive number = I am "greater than")

Everyone on the road follows the SAME rules. That is the "contract" - a promise about how comparison works.

If some drivers followed different rules, chaos would ensue! Similarly, if your compareTo() method does not follow the contract, sorting will produce unpredictable results.

### Analogy 4: Natural Order vs. Special Orders

Think of a deck of playing cards.

**Natural ordering** (how cards "usually" sort):
- By suit: Clubs < Diamonds < Hearts < Spades
- Within suit: 2 < 3 < ... < 10 < J < Q < K < A

This is the "default" - what everyone expects when you say "sort these cards."

But sometimes you want a DIFFERENT order:
- In some games, Aces are low (A < 2)
- In some games, only rank matters, not suit
- In War, you might only care about the number

**Comparable gives you the natural (default) order. One per class.**
**Comparator (Week 15) gives you alternative orders. As many as you want!**

---

## Understanding Natural Ordering

### What Is Natural Ordering?

**Natural ordering** is the "default" or "obvious" way to sort objects of a particular type.

Some examples:
- Numbers: ascending order (1, 2, 3, 4, 5)
- Strings: alphabetical order ("apple", "banana", "cherry")
- Dates: chronological order (earlier dates before later dates)

These feel "natural" because they match our expectations.

### Why Is It Called "Natural"?

It is the ONE ordering that makes the most sense for a type. When someone says "sort these students," there should be ONE obvious answer.

For a Student class, natural ordering might be:
- By name (alphabetical) - makes sense for a roster
- By student ID (numeric) - makes sense for administrative systems

You choose what is "natural" for YOUR application.

### How Java Uses Natural Ordering

When you call `Collections.sort()` or `Arrays.sort()` without extra arguments, Java uses natural ordering:

```java
List<String> names = new ArrayList<>();
names.add("Charlie");
names.add("Alice");
names.add("Bob");

Collections.sort(names);  // Uses String's natural ordering
// Result: ["Alice", "Bob", "Charlie"]
```

String already implements Comparable, so it has a natural ordering (alphabetical, case-sensitive).

### Example: Why Defining Order Matters

Without defined ordering:

```java
Student alice = new Student("Alice", 3.8);
Student bob = new Student("Bob", 3.5);

// How should these be compared?
// By name? Alice < Bob (alphabetically)
// By GPA? Alice > Bob (higher GPA)

// Java has no idea! It cannot guess your intent.
```

With Comparable:

```java
public class Student implements Comparable<Student> {
    // ... fields and constructor ...

    @Override
    public int compareTo(Student other) {
        return this.name.compareTo(other.name);  // Natural order = by name
    }
}

// Now Java knows! Alice comes before Bob.
```

---

## Understanding the Comparable Interface

### What Is an Interface?

Before we dive into Comparable, let us briefly explain what an interface is. (You will learn much more in Week 15!)

An **interface** is like a contract or promise. When a class "implements" an interface, it promises to provide certain methods.

Think of it like a job requirement:
- Job posting: "Must speak English" (the interface)
- Applicant: "I speak English" (implements the interface)
- Employer can trust: This person CAN communicate in English

Similarly:
- Comparable interface: "Must have compareTo() method"
- Your class: "I have compareTo()"
- Java can trust: This class CAN be sorted

### Why Is Comparable an Interface?

Java's sorting methods (like `Arrays.sort()` and `Collections.sort()`) need to know:
- "Can I sort these objects?"
- "How do I compare two objects?"

The Comparable interface answers both:
- YES, you can sort (the class implements Comparable)
- Use compareTo() to compare (the method we must provide)

### How to Implement Comparable

Here is the template:

```java
public class YourClass implements Comparable<YourClass> {
    // Your fields and methods...

    @Override
    public int compareTo(YourClass other) {
        // Return negative if this < other
        // Return zero if this == other
        // Return positive if this > other
    }
}
```

**Key points:**
- Add `implements Comparable<YourClass>` to your class declaration
- The `<YourClass>` part is called a "type parameter" - it says what type we compare to
- You MUST write a `compareTo()` method
- The `@Override` annotation tells Java (and humans) we are implementing an interface method

### Example: Making Student Comparable

```java
public class Student implements Comparable<Student> {
    private String name;
    private int age;
    private double gpa;

    public Student(String name, int age, double gpa) {
        this.name = name;
        this.age = age;
        this.gpa = gpa;
    }

    // Getters...
    public String getName() { return name; }
    public int getAge() { return age; }
    public double getGpa() { return gpa; }

    @Override
    public int compareTo(Student other) {
        // Natural ordering: by name (alphabetical)
        return this.name.compareTo(other.name);
    }
}
```

Now Student objects can be sorted!

```java
List<Student> students = new ArrayList<>();
students.add(new Student("Charlie", 20, 3.5));
students.add(new Student("Alice", 22, 3.8));
students.add(new Student("Bob", 19, 3.2));

Collections.sort(students);
// Now: Alice, Bob, Charlie (alphabetical by name)
```

---

## Understanding the compareTo() Method

### What Is compareTo()?

The `compareTo()` method answers the question: **"How does THIS object compare to THAT object?"**

It returns an integer that indicates the relationship:

| Return Value | Meaning | Memory Aid |
|-------------|---------|------------|
| Negative (< 0) | this comes BEFORE other | "I'm less, so negative" |
| Zero (= 0) | this and other are EQUAL | "Same, so zero difference" |
| Positive (> 0) | this comes AFTER other | "I'm more, so positive" |

### The Memory Trick

Think of it as subtraction: `this - other`

- If I am smaller than you: `this - other` is negative
- If we are equal: `this - other` is zero
- If I am bigger than you: `this - other` is positive

For numbers, you can actually USE subtraction (with care):

```java
// Comparing ages (integers)
return this.age - other.age;

// If this.age = 20, other.age = 25:
// 20 - 25 = -5 (negative, so this < other)

// If this.age = 25, other.age = 20:
// 25 - 20 = 5 (positive, so this > other)

// If this.age = 20, other.age = 20:
// 20 - 20 = 0 (zero, so equal)
```

**WARNING**: Subtraction can cause overflow with very large numbers! For safety, use `Integer.compare()`:

```java
// SAFER approach for integers:
return Integer.compare(this.age, other.age);
```

### Comparing Different Types

**For Strings** - use String's compareTo():
```java
return this.name.compareTo(other.name);
```

**For integers** - use subtraction or Integer.compare():
```java
return this.age - other.age;           // Simple but can overflow
return Integer.compare(this.age, other.age);  // Safe, preferred
```

**For doubles** - use Double.compare():
```java
return Double.compare(this.gpa, other.gpa);
```

**Why Double.compare()?** Because floating-point comparison is tricky. 0.1 + 0.2 might not equal 0.3 exactly! `Double.compare()` handles these edge cases.

### Example: Sorting Students by Age

```java
public class Student implements Comparable<Student> {
    private String name;
    private int age;

    // Constructor and getters...

    @Override
    public int compareTo(Student other) {
        // Natural ordering: by age (youngest first)
        return Integer.compare(this.age, other.age);
    }
}
```

Usage:
```java
List<Student> students = new ArrayList<>();
students.add(new Student("Alice", 22));
students.add(new Student("Bob", 19));
students.add(new Student("Charlie", 25));

Collections.sort(students);
// Now: Bob (19), Alice (22), Charlie (25)
```

### Example: Sorting Students by GPA (Highest First!)

Sometimes you want DESCENDING order (highest first, like a leaderboard):

```java
@Override
public int compareTo(Student other) {
    // REVERSE: highest GPA first (descending order)
    return Double.compare(other.gpa, this.gpa);  // Note: other before this!
}
```

**The trick**: Swap `this` and `other` to reverse the order!

Or equivalently:
```java
return -Double.compare(this.gpa, other.gpa);  // Negate the result
```

---

## The compareTo() Contract

### What Is a Contract?

In programming, a **contract** is a set of rules that MUST be followed. If you break the contract, things stop working correctly.

The compareTo() contract has specific rules that ensure sorting works properly.

### The Three Rules

**Rule 1: Antisymmetry**
If `x.compareTo(y)` is positive, then `y.compareTo(x)` must be negative.
(If I am greater than you, you must be less than me.)

```java
// If this returns positive (Alice > Bob)
alice.compareTo(bob)

// Then this MUST return negative (Bob < Alice)
bob.compareTo(alice)
```

**Rule 2: Transitivity**
If `x > y` and `y > z`, then `x > z`.
(If I am older than you, and you are older than Charlie, then I am older than Charlie.)

```java
// If Alice > Bob and Bob > Charlie
// Then Alice > Charlie MUST be true
```

**Rule 3: Consistency**
If `x.compareTo(y) == 0`, then `x.compareTo(z)` and `y.compareTo(z)` must have the same sign.
(If two things are "equal," they should compare the same way to everything else.)

### Why the Contract Matters

Sorting algorithms DEPEND on these rules. If you break them:

```
What you expect:        What you might get:
[Alice, Bob, Charlie]   [Bob, Charlie, Alice]  <- Wrong order!
                        [Infinite loop]         <- Even worse!
                        [Exception]             <- Crashes!
```

### Common Contract Violations

**Bad: Not handling null**
```java
// BROKEN: crashes if other is null
@Override
public int compareTo(Student other) {
    return this.name.compareTo(other.name);  // NullPointerException!
}
```

**Bad: Inconsistent logic**
```java
// BROKEN: breaks transitivity
@Override
public int compareTo(Student other) {
    if (this.age > other.age) return 1;
    if (this.age < other.age) return -1;
    return 1;  // BUG! Should return 0 for equal ages!
}
```

**Good: Follow the contract**
```java
@Override
public int compareTo(Student other) {
    return Integer.compare(this.age, other.age);  // Correct!
}
```

---

## Using Collections.sort() and Arrays.sort()

### Sorting ArrayList with Collections.sort()

Remember ArrayList from Week 10? Now we can sort it!

```java
import java.util.ArrayList;
import java.util.Collections;

public class SortingDemo {
    public static void main(String[] args) {
        // Create a list of students
        ArrayList<Student> students = new ArrayList<>();
        students.add(new Student("Charlie", 20, 3.5));
        students.add(new Student("Alice", 22, 3.8));
        students.add(new Student("Bob", 19, 3.2));

        System.out.println("Before sorting:");
        for (Student s : students) {
            System.out.println(s.getName());
        }
        // Output: Charlie, Alice, Bob

        // Sort using natural ordering (compareTo method)
        Collections.sort(students);

        System.out.println("\nAfter sorting:");
        for (Student s : students) {
            System.out.println(s.getName());
        }
        // Output: Alice, Bob, Charlie (if sorted by name)
    }
}
```

### Sorting Arrays with Arrays.sort()

Remember arrays from Week 6? Same idea!

```java
import java.util.Arrays;

public class ArraySortingDemo {
    public static void main(String[] args) {
        Student[] students = new Student[3];
        students[0] = new Student("Charlie", 20, 3.5);
        students[1] = new Student("Alice", 22, 3.8);
        students[2] = new Student("Bob", 19, 3.2);

        System.out.println("Before sorting:");
        for (Student s : students) {
            System.out.println(s.getName());
        }

        // Sort the array
        Arrays.sort(students);

        System.out.println("\nAfter sorting:");
        for (Student s : students) {
            System.out.println(s.getName());
        }
    }
}
```

### What Happens If You Forget Comparable?

```java
public class UnsortableStudent {  // Does NOT implement Comparable
    private String name;
    // ... no compareTo method
}

public class Main {
    public static void main(String[] args) {
        ArrayList<UnsortableStudent> students = new ArrayList<>();
        // Add students...

        Collections.sort(students);  // CRASH! ClassCastException
    }
}
```

Error message:
```
java.lang.ClassCastException: UnsortableStudent cannot be cast to java.lang.Comparable
```

This error tells you: "I tried to sort, but these objects do not know how to compare themselves!"

---

## Finding Min and Max Using Sorting

### The Simple Approach

Once your list is sorted, finding minimum and maximum is trivial:

```java
Collections.sort(students);  // Sort first

// After sorting (ascending order):
// - First element is the MINIMUM
// - Last element is the MAXIMUM

Student youngest = students.get(0);               // First = minimum
Student oldest = students.get(students.size() - 1);  // Last = maximum
```

### Using Collections.min() and Collections.max()

Even simpler - Java provides methods that use compareTo:

```java
Student youngest = Collections.min(students);  // Uses compareTo
Student oldest = Collections.max(students);    // Uses compareTo
```

These methods:
- Require that objects implement Comparable
- Do NOT sort the list (they just scan it)
- Are efficient for finding just min or max

### Complete Example: Class Roster Statistics

```java
import java.util.ArrayList;
import java.util.Collections;

public class RosterStatistics {
    public static void main(String[] args) {
        ArrayList<Student> roster = new ArrayList<>();
        roster.add(new Student("Alice", 22, 3.8));
        roster.add(new Student("Bob", 19, 3.2));
        roster.add(new Student("Charlie", 25, 3.5));
        roster.add(new Student("Diana", 20, 3.9));

        // Sort by age (assuming natural ordering is by age)
        Collections.sort(roster);

        // First = youngest, Last = oldest
        Student youngest = roster.get(0);
        Student oldest = roster.get(roster.size() - 1);

        System.out.println("Youngest: " + youngest.getName() +
                          " (age " + youngest.getAge() + ")");
        System.out.println("Oldest: " + oldest.getName() +
                          " (age " + oldest.getAge() + ")");
    }
}
```

---

## Consistency Between compareTo() and equals()

### The Recommendation

Java strongly recommends that compareTo() and equals() be **consistent**:

- If `x.compareTo(y) == 0`, then `x.equals(y)` should return `true`
- If `x.equals(y)` returns `true`, then `x.compareTo(y)` should return `0`

### Why Does This Matter?

Some Java collections (like TreeSet and TreeMap) use compareTo() for equality checks. If your compareTo() and equals() disagree, strange things happen:

```java
// INCONSISTENT: compareTo says equal, equals says not equal
Student s1 = new Student("Alice", 22, 3.8);
Student s2 = new Student("Alice", 25, 3.5);  // Different age and GPA

// If compareTo only checks name:
s1.compareTo(s2)  // Returns 0 (equal by name)

// But equals checks everything:
s1.equals(s2)     // Returns false (different age and GPA)

// In a TreeSet:
TreeSet<Student> set = new TreeSet<>();
set.add(s1);
set.add(s2);  // Might be treated as duplicate! Set.size() could be 1!
```

### How to Maintain Consistency

Compare the SAME fields in both methods:

```java
public class Student implements Comparable<Student> {
    private String name;
    private int age;

    @Override
    public int compareTo(Student other) {
        return this.name.compareTo(other.name);  // Compare by name
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Student other = (Student) obj;
        return this.name.equals(other.name);  // ALSO compare by name only!
    }

    @Override
    public int hashCode() {
        return name.hashCode();  // Hash by name too!
    }
}
```

### When Inconsistency Is Acceptable

It is okay to be inconsistent IF you never use TreeSet/TreeMap with these objects. But it is better to be consistent when possible!

---

## Complete Example: The Car Class from Earlier Weeks

Remember the Car class from Weeks 7-10? Let us make it sortable!

```java
public class Car implements Comparable<Car> {
    private String make;
    private String model;
    private int year;
    private double price;

    public Car(String make, String model, int year, double price) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.price = price;
    }

    // Getters
    public String getMake() { return make; }
    public String getModel() { return model; }
    public int getYear() { return year; }
    public double getPrice() { return price; }

    // Natural ordering: by price (cheapest first)
    @Override
    public int compareTo(Car other) {
        return Double.compare(this.price, other.price);
    }

    @Override
    public String toString() {
        return year + " " + make + " " + model + " ($" + price + ")";
    }
}
```

Using the sortable Car class:

```java
import java.util.ArrayList;
import java.util.Collections;

public class CarDealership {
    public static void main(String[] args) {
        ArrayList<Car> inventory = new ArrayList<>();
        inventory.add(new Car("Toyota", "Camry", 2022, 25000));
        inventory.add(new Car("Honda", "Civic", 2023, 23000));
        inventory.add(new Car("BMW", "3 Series", 2021, 45000));
        inventory.add(new Car("Ford", "Focus", 2020, 18000));

        System.out.println("Inventory (unsorted):");
        for (Car car : inventory) {
            System.out.println("  " + car);
        }

        // Sort by price (our natural ordering)
        Collections.sort(inventory);

        System.out.println("\nInventory (sorted by price):");
        for (Car car : inventory) {
            System.out.println("  " + car);
        }

        // Find cheapest and most expensive
        Car cheapest = Collections.min(inventory);
        Car mostExpensive = Collections.max(inventory);

        System.out.println("\nCheapest: " + cheapest);
        System.out.println("Most expensive: " + mostExpensive);
    }
}
```

Output:
```
Inventory (unsorted):
  2022 Toyota Camry ($25000.0)
  2023 Honda Civic ($23000.0)
  2021 BMW 3 Series ($45000.0)
  2020 Ford Focus ($18000.0)

Inventory (sorted by price):
  2020 Ford Focus ($18000.0)
  2023 Honda Civic ($23000.0)
  2022 Toyota Camry ($25000.0)
  2021 BMW 3 Series ($45000.0)

Cheapest: 2020 Ford Focus ($18000.0)
Most expensive: 2021 BMW 3 Series ($45000.0)
```

---

## Sorting Numbers vs. Strings

### Numbers Sort Numerically

Numbers have natural numerical order:
```java
int[] numbers = {5, 2, 8, 1, 9};
Arrays.sort(numbers);
// Result: {1, 2, 5, 8, 9}
```

### Strings Sort Lexicographically (Like a Dictionary)

Strings are compared character by character, using Unicode values:

```java
String[] words = {"banana", "Apple", "cherry"};
Arrays.sort(words);
// Result: {"Apple", "banana", "cherry"}
// Note: "Apple" comes first because uppercase letters have lower Unicode values!
```

### The Case-Sensitivity Surprise

```java
String[] names = {"bob", "Alice", "Charlie"};
Arrays.sort(names);
// Result: {"Alice", "Charlie", "bob"}
// Uppercase comes BEFORE lowercase in Unicode!
```

If you want case-insensitive sorting, you will learn about `String.CASE_INSENSITIVE_ORDER` in Week 15.

### The Number-as-String Problem

```java
String[] numberStrings = {"100", "20", "3"};
Arrays.sort(numberStrings);
// Result: {"100", "20", "3"}  <- NOT numerical order!
// "1" comes before "2" comes before "3" lexicographically
```

If you need numerical sorting, convert to integers first!

---

## Reversing Sort Order

### Approach 1: Swap this and other

```java
@Override
public int compareTo(Student other) {
    // ASCENDING (youngest first):
    return Integer.compare(this.age, other.age);

    // DESCENDING (oldest first):
    return Integer.compare(other.age, this.age);  // Swapped!
}
```

### Approach 2: Negate the Result

```java
@Override
public int compareTo(Student other) {
    // ASCENDING (normal):
    return Integer.compare(this.age, other.age);

    // DESCENDING (reversed):
    return -Integer.compare(this.age, other.age);  // Negated!
}
```

### Approach 3: Use Collections.reverseOrder() (Preview of Week 15)

In Week 15, you will learn about Comparator, which provides:

```java
Collections.sort(students, Collections.reverseOrder());
```

This reverses the natural order without changing your compareTo() method!

---

## Connecting to What You Already Know

### Week 6: Arrays

You learned how to work with arrays. Now you can SORT them!

| Week 6 | Week 14 |
|--------|---------|
| `int[] arr = new int[5];` | `Student[] arr = new Student[5];` |
| Arrays store multiple values | Arrays can store objects |
| `arr[0] = 5;` | `arr[0] = new Student("Alice", 20);` |
| `arr.length` | Still `arr.length`! |
| Loop through array | Still loop the same way |
| **NEW**: | `Arrays.sort(arr);` requires Comparable! |

### Week 10: ArrayList

You learned about ArrayList, a more flexible collection. Now you can sort it!

| Week 10 | Week 14 |
|---------|---------|
| `ArrayList<Student> list` | Same list |
| `list.add(student)` | Still works |
| `list.get(0)` | First (or minimum after sort!) |
| `list.size()` | Number of elements |
| Loop with for-each | Still works |
| **NEW**: | `Collections.sort(list);` |

### Weeks 7-10: OOP

Remember classes, objects, and methods? Comparable connects them!

| OOP Concept | Sorting Application |
|-------------|---------------------|
| Class | The blueprint we make sortable |
| Object | Individual things we sort |
| Instance variables | What we compare BY (name, age, etc.) |
| Methods | compareTo() is just another method |
| Interface | Comparable is our first interface! |

### Week 13: Unit Testing

From last week, you can TEST your sorting!

```java
@Test
void compareTo_youngerStudent_returnsNegative() {
    Student younger = new Student("Bob", 19);
    Student older = new Student("Alice", 25);

    assertTrue(younger.compareTo(older) < 0);
}

@Test
void sort_unsortedList_sortsByAge() {
    List<Student> students = Arrays.asList(
        new Student("Alice", 25),
        new Student("Bob", 19)
    );

    Collections.sort(students);

    assertEquals("Bob", students.get(0).getName());  // Youngest first
    assertEquals("Alice", students.get(1).getName());
}
```

---

## Common Struggles and How to Overcome Them

### Struggle 1: Understanding compareTo Return Values

**The problem:** "I keep getting confused about negative, zero, positive!"

**Solution:** Use this memory trick:

```
Think: "this MINUS other"

this < other  -->  negative (this - other = negative number)
this == other -->  zero     (this - other = 0)
this > other  -->  positive (this - other = positive number)
```

Or remember: **"I come first, so I'm negative!"**
- If `this` should come BEFORE `other` in sorted order, return negative

### Struggle 2: When to Use Comparable vs. Direct Sorting

**The problem:** "Why can not I just sort without Comparable?"

**Answer:** You CAN sort primitive types and Strings directly - they already have natural ordering!

```java
// These work without YOU implementing anything:
int[] numbers = {3, 1, 2};
Arrays.sort(numbers);  // Java knows how to compare ints

String[] words = {"c", "a", "b"};
Arrays.sort(words);  // Java knows how to compare Strings
```

You need Comparable for YOUR classes, because Java does not know how to compare YOUR objects.

### Struggle 3: Maintaining Transitivity

**The problem:** "My sorting gives weird results!"

**Check for this common bug:**

```java
// BUG: Returns 0 or 1, never negative!
@Override
public int compareTo(Student other) {
    if (this.age >= other.age) return 1;
    return 0;
}

// FIXED: Returns all three cases
@Override
public int compareTo(Student other) {
    return Integer.compare(this.age, other.age);
}
```

### Struggle 4: Consistency with equals()

**The problem:** "TreeSet is behaving strangely!"

**Check:** Do compareTo() and equals() agree?

```java
// If compareTo returns 0 for two objects:
student1.compareTo(student2) == 0  // "Equal" for sorting

// Then equals should also return true:
student1.equals(student2)  // Should also be true!
```

If they disagree, TreeSet and TreeMap will be confused.

### Struggle 5: Choosing Natural Ordering

**The problem:** "How do I decide what my natural ordering should be?"

**Ask yourself:**
1. What is the MOST COMMON way users will want to sort this?
2. What makes sense for this domain?
3. If someone says "sort the students," what would they expect?

| Class | Likely Natural Ordering |
|-------|-------------------------|
| Student | By name (alphabetical) |
| Employee | By employee ID |
| Product | By name or product code |
| BankTransaction | By date (chronological) |
| HighScore | By score (highest first) |

---

## Practice Exercises

### Exercise 1: Student Roster (meget hjaelp - Maximum Guidance)

**Goal:** Create a sortable Student class and sort a roster.

**Part A: Create the Student class**

```java
public class Student implements Comparable<Student> {
    private String name;
    private int studentId;
    private double gpa;

    // TODO: Constructor taking all three parameters

    // TODO: Getters for all fields

    // TODO: toString() that returns: "name (ID: studentId, GPA: gpa)"

    // TODO: compareTo that orders by student ID (ascending)
    @Override
    public int compareTo(Student other) {
        // Hint: Use Integer.compare(this.studentId, other.studentId)
    }
}
```

**Part B: Test your sorting**

```java
public class RosterTest {
    public static void main(String[] args) {
        ArrayList<Student> roster = new ArrayList<>();
        roster.add(new Student("Charlie", 1003, 3.5));
        roster.add(new Student("Alice", 1001, 3.8));
        roster.add(new Student("Bob", 1002, 3.2));

        // TODO: Print roster before sorting

        // TODO: Sort the roster

        // TODO: Print roster after sorting
        // Expected: Alice, Bob, Charlie (sorted by ID)

        // TODO: Find student with lowest and highest ID
    }
}
```

### Exercise 2: Largest and Smallest (nogen hjaelp - Moderate Guidance)

**Goal:** Create a generic method to find min/max in any Comparable list.

Based on the curriculum exercise "Storst og mindst":

**Part A: Create a Product class**

```java
public class Product implements Comparable<Product> {
    private String name;
    private double price;

    // Constructor, getters, toString...

    // Natural ordering: by price (cheapest first)
    @Override
    public int compareTo(Product other) {
        // Your implementation
    }
}
```

**Part B: Find extremes**

Write a program that:
1. Creates an ArrayList of at least 5 products
2. Prints all products
3. Uses `Collections.min()` to find cheapest
4. Uses `Collections.max()` to find most expensive
5. Also sorts the list and gets first/last for the same result

**Bonus:** What happens if you try to find min/max of an empty list?

### Exercise 3: FriendSorter (ingen hjaelp - Minimal Guidance)

**Goal:** Create a complete contact management system with sorting.

**Requirements:**

1. Create a `Friend` class with:
   - name, phoneNumber, email, birthday (as String "YYYY-MM-DD")
   - Natural ordering by name (alphabetical)
   - toString() showing all information nicely

2. Create a `FriendSorter` class with:
   - An ArrayList of Friend objects
   - Method to add a friend
   - Method to print all friends
   - Method to print all friends sorted
   - Method to find friend with earliest birthday (alphabetically)
   - Method to find friend with latest birthday

3. Test thoroughly:
   - Add at least 5 friends with various names and birthdays
   - Print unsorted
   - Print sorted
   - Print earliest and latest birthday friends

4. Challenge: What if you want to sort by birthday instead of name? (Think about this - you will learn the answer in Week 15!)

### Exercise 4: Car Dealership Inventory (ingen hjaelp - Minimal Guidance)

**Goal:** Build on the Car example to create a full inventory system.

**Requirements:**

1. Create a `Car` class implementing Comparable:
   - make, model, year, price, mileage
   - Natural ordering by price (cheapest first)

2. Create a `CarDealership` class with methods:
   - `addCar(Car car)`
   - `printInventory()` - all cars
   - `printSortedByPrice()` - sorted list
   - `getCheapestCar()` - uses sorting or Collections.min()
   - `getMostExpensiveCar()` - uses sorting or Collections.max()
   - `getCarsUnderPrice(double maxPrice)` - returns filtered list
   - `printInventoryAsTable()` - formatted output

3. Main program that:
   - Creates dealership with 8+ cars
   - Demonstrates all methods
   - Shows both sorted and unsorted output

---

## Looking Ahead

### Week 15: Interfaces and Advanced Sorting

This week you learned ONE way to sort objects (Comparable = natural ordering).

But what if you want to sort students:
- Sometimes by name
- Sometimes by GPA
- Sometimes by age
- Sometimes by student ID

With Comparable alone, you would have to change your compareTo() method each time!

**Next week introduces Comparator** - a way to define MULTIPLE sorting strategies:

```java
// Preview of Week 15:
Collections.sort(students, new NameComparator());     // By name
Collections.sort(students, new GpaComparator());      // By GPA
Collections.sort(students, new AgeComparator());      // By age

// Or even more elegantly with lambdas:
Collections.sort(students, (s1, s2) -> s1.getName().compareTo(s2.getName()));
```

You will also dive deeper into **interfaces** as a concept - not just Comparable, but how to design with interfaces for flexibility.

### The Bigger Picture

```
Week 14 (This Week)             Week 15 (Next Week)
------------------              ------------------
Comparable interface            Comparator interface
ONE natural ordering            MANY custom orderings
Class defines its own order     External classes define order
compareTo() method              compare() method
"How do I compare to you?"      "How do these two compare?"
```

Think of it this way:
- **Comparable**: "I know how to sort myself" (built into the class)
- **Comparator**: "Someone else decides how to sort us" (external strategy)

---

## Key Takeaways

1. **Natural ordering is the "default" way to sort objects** - each class can have ONE natural ordering defined by Comparable

2. **Comparable is an interface** that promises your class can be sorted by implementing compareTo()

3. **The compareTo() method returns:**
   - Negative if this < other (this comes first)
   - Zero if this == other (they are equal)
   - Positive if this > other (this comes after)

4. **Memory trick: "this minus other"**
   - If this is smaller, the difference is negative
   - If equal, the difference is zero
   - If this is bigger, the difference is positive

5. **Use helper methods for safe comparison:**
   - `Integer.compare(a, b)` for int
   - `Double.compare(a, b)` for double
   - `String.compareTo()` for String

6. **Collections.sort() and Arrays.sort()** use your compareTo() method automatically

7. **Collections.min() and Collections.max()** also use compareTo()

8. **The compareTo contract must be followed:**
   - Antisymmetry: if x > y, then y < x
   - Transitivity: if x > y and y > z, then x > z
   - Consistency: equal objects compare the same to others

9. **Maintain consistency between compareTo() and equals()** when possible

10. **To reverse sort order:** either swap this/other, negate the result, or use Collections.reverseOrder()

11. **Strings sort lexicographically** (dictionary order, case-sensitive!)

12. **This is exam-relevant material** - sorting is 20-25% of your exam!

---

## For the Next Topic Agent

### Terminology Established This Week

- **natural ordering**: The default, single sorting order for a class
- **Comparable**: Interface that enables natural ordering
- **compareTo()**: Method that compares `this` object to another
- **compareTo contract**: Rules that compareTo must follow (antisymmetry, transitivity, consistency)
- **Collections.sort()**: Sorts ArrayList using natural ordering
- **Arrays.sort()**: Sorts arrays using natural ordering
- **Collections.min()/max()**: Find minimum/maximum using natural ordering
- **ascending order**: Smallest first (default)
- **descending order**: Largest first (reverse)
- **lexicographic order**: Dictionary/alphabetical order for Strings
- **consistency with equals()**: Recommendation that compareTo() and equals() agree

### Concepts From Prior Weeks Applied

| Prior Week | Concept | Week 14 Application |
|------------|---------|---------------------|
| Week 6 | Arrays | Arrays.sort() sorts arrays |
| Week 6 | Array indexing | First/last after sorting = min/max |
| Week 10 | ArrayList | Collections.sort() sorts ArrayList |
| Week 10 | Wrapper classes | Integer.compare(), Double.compare() |
| Weeks 7-10 | Classes | The classes we make Comparable |
| Weeks 7-10 | Objects | The objects we sort |
| Weeks 7-10 | Instance variables | What we compare BY |
| Weeks 7-10 | Methods | compareTo() is just another method |
| Week 13 | Unit testing | Testing compareTo and sorting |

### Student Capabilities After This Week

Students can now:
- Implement Comparable interface on their classes
- Write correct compareTo() methods
- Sort ArrayList with Collections.sort()
- Sort arrays with Arrays.sort()
- Find minimum and maximum using sorting
- Understand and follow the compareTo contract
- Maintain consistency between compareTo() and equals()
- Choose appropriate natural ordering for domain classes
- Reverse sort order when needed

### Critical Concepts for Week 15 (Interfaces and Advanced Sorting)

Week 15 should build on these Week 14 foundations:

1. **From Comparable to Comparator**: Students understand ONE ordering (Comparable). Now introduce MULTIPLE orderings (Comparator).

2. **Interface concept expansion**: Students have now USED an interface (Comparable). Explain what interfaces ARE in depth.

3. **compare() vs compareTo()**:
   - compareTo() compares `this` to another
   - compare() compares two separate objects

4. **Use the same examples**: Continue with Student and Car classes, but show how Comparator allows different sorting strategies.

5. **Pattern preview**: Students learned natural ordering. Introduce:
   - Custom Comparators as classes
   - Anonymous class syntax
   - Lambda expressions (if appropriate)
   - Bean Comparator pattern
   - Enum-based strategies

### Handoff Notes for Week 15

Students are ready for:
- Deep dive into interfaces as a concept
- Comparator interface for multiple sort strategies
- compare() method implementation
- Anonymous classes and lambdas for comparators
- Choosing between Comparable and Comparator
- Interface design principles

**Key transition point**: Week 14 established "one class = one ordering." Week 15 breaks that limitation with "one class = many possible orderings via Comparator."

### Common Misconceptions to Address in Week 15

1. "I need to change compareTo() to sort differently" - No! Use Comparator instead
2. "Comparable and Comparator are the same" - No! Different purposes
3. "I can only have one Comparator" - No! You can have as many as needed
4. "compareTo() and compare() work the same" - Similar concept, different signature
5. "Interfaces are like classes" - No! Interfaces are contracts, not implementations
