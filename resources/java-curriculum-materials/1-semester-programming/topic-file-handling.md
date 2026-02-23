# File Handling - Week 11

*Prerequisites: Weeks 7-10 (Complete OOP Foundation), Week 1 (Scanner basics), Week 3 (Loops)*
*Phase: Phase 4: Practical Software Development (First Week)*

---

## What You'll Learn

By the end of this week, you will be able to:

- **Understand why file I/O matters** and how it enables data persistence
- **Work with file paths** (absolute vs relative) confidently
- **Read text files** using Scanner (the same Scanner you know from Week 1!)
- **Write text files** using PrintWriter and PrintStream
- **Parse structured data** from CSV and delimited files
- **Use try-with-resources** for safe file handling (your introduction to exception handling)
- **Save objects to files** using toString() and getters
- **Load objects from files** by parsing text back into objects
- **Understand the difference** between text files and binary files

**PHASE SHIFT**: This week marks a major transition! Weeks 7-10 taught you OOP *theory*. Now you apply that knowledge to *practical* problems. Your well-designed objects can finally live beyond program execution!

---

## Why This Matters

### The Problem: Your Data Disappears!

Think about every program you have written so far. What happens when you close it?

```java
public class StudentTracker {
    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();
        students.add(new Student("Alice", 101));
        students.add(new Student("Bob", 102));
        students.add(new Student("Charlie", 103));

        System.out.println("I have " + students.size() + " students!");
        // Program ends... and ALL YOUR DATA IS GONE FOREVER!
    }
}
```

You spent time entering that data. The next time you run the program? It starts empty. All your students vanished. This is the **persistence problem**.

### The Solution: Files!

Files let your data survive after the program stops:

```
When program RUNS:                When program STOPS:
+------------------+              +------------------+
| Memory (RAM)     |              | Memory (RAM)     |
| [Alice, Bob,     |   ------->   | [empty]          |
|  Charlie]        |   program    |                  |
+------------------+   ends       +------------------+

        BUT with FILE I/O:

+------------------+              +------------------+
| students.txt     |              | students.txt     |
| Alice,101        |   ------->   | Alice,101        |
| Bob,102          |   file       | Bob,102          |
| Charlie,103      |   remains!   | Charlie,103      |
+------------------+              +------------------+
```

**Files are permanent storage.** RAM is temporary. Files persist.

### Real-World Everywhere

Think about programs you use daily:

| Application | What Gets Saved | Without File I/O |
|-------------|-----------------|------------------|
| Text editor | Your documents | You'd retype everything each time |
| Music player | Playlists | Rebuild playlists daily |
| Game | Save progress | Start from level 1 always |
| Settings app | Preferences | Reconfigure every launch |
| Your future programs | User data | No practical use! |

### This Is Exam-Critical (20-25%)

File handling accounts for 20-25% of your exam. You WILL be asked to:
- Read data from a file
- Parse that data into objects
- Process or modify the objects
- Write results back to a file

Master this week, and you unlock a significant portion of exam points!

---

## Building Your Intuition

### Analogy 1: Files as Filing Cabinets, Programs as Desks

Imagine your program is a desk where you work. RAM is the desk surface - you can spread papers out, organize them, work with them. But when you leave for the day, everything on the desk gets cleared.

**Files are the filing cabinet next to your desk.**

- To use information, you PULL a file from the cabinet TO your desk (reading)
- When you are done, you PUT the file back IN the cabinet (writing)
- The cabinet keeps files even when you go home (persistence)
- Tomorrow, you can PULL the same files again

```
FILING CABINET          DESK (Program)
+-------------+         +------------------+
| students.txt|  READ   | ArrayList<Student>|
|             | ------> |   [Alice, Bob]   |
|             |         |                  |
|             | <------ |                  |
|             |  WRITE  |                  |
+-------------+         +------------------+
```

### Analogy 2: Scanner as a Reading Assistant

Remember Week 1? Scanner read YOUR KEYBOARD input. Scanner was like an assistant listening to what you type.

**Week 11 twist: Scanner can also read FILES!**

Same assistant, different source:

```
Week 1:                          Week 11:
+--------+                       +--------+
|KEYBOARD|                       |  FILE  |
| Hello! |                       | Hello! |
+---+----+                       +---+----+
    |                                |
    v                                v
+--------+                       +--------+
|Scanner |                       |Scanner |
| reads  |                       | reads  |
+---+----+                       +---+----+
    |                                |
    v                                v
"Hello!" in your program         "Hello!" in your program
```

The Scanner methods you already know (`nextLine()`, `nextInt()`, `hasNext()`) work exactly the same way with files!

### Analogy 3: PrintWriter as Your Secretary

If Scanner is your reading assistant, PrintWriter is your writing secretary.

When you want something written down:
- You tell PrintWriter what to write (`println("Hello")`)
- PrintWriter puts it in the file
- Just like `System.out.println()` puts text on screen

```
System.out.println("Hi")  -->  Text appears on SCREEN
writer.println("Hi")      -->  Text appears in FILE
```

Same methods, different destination!

### Analogy 4: File Paths as Addresses

Every file has an address called a **path**. Just like mailing a letter, you need the right address.

**Absolute path**: The FULL address from the root of the filesystem
- Like: "123 Main Street, Copenhagen, Denmark, Earth"
- In code: `/Users/alice/Documents/students.txt` (Mac/Linux)
- Or: `C:\Users\alice\Documents\students.txt` (Windows)

**Relative path**: Directions FROM WHERE YOU ARE
- Like: "The house three doors down"
- In code: `students.txt` (in current folder)
- Or: `data/students.txt` (in subfolder called "data")

```
Absolute: "Go to Denmark, Copenhagen, Main Street 123"
          Works no matter where you start!

Relative: "Walk three doors down"
          Only works if you're already on the right street!
```

---

## Understanding File Paths

### What Is a File Path?

A **file path** is the location of a file on your computer. Think of it as the file's home address. Without the correct address, your program cannot find the file.

### Why This Confuses Beginners

File paths are the **#1 source of confusion** for beginners. Here is why:

1. Different operating systems use different separators (`/` vs `\`)
2. "Current directory" changes depending on how you run your program
3. IDEs often set unexpected working directories
4. The same file can have multiple valid paths

### Absolute Paths: The Full Address

An **absolute path** starts from the root of your filesystem and specifies every folder along the way.

**On Mac/Linux:**
```
/Users/alice/Documents/Projects/MyApp/data/students.txt
^    ^      ^          ^        ^     ^    ^
|    |      |          |        |     |    |
root user   Documents  Projects  app  data actual file
```

**On Windows:**
```
C:\Users\alice\Documents\Projects\MyApp\data\students.txt
^ ^     ^      ^          ^        ^     ^    ^
| |     |      |          |        |     |    |
drive root    Documents  Projects  app  data actual file
```

**Advantages of absolute paths:**
- Always work, no matter where your program runs from
- Unambiguous - there is only ONE file at that address

**Disadvantages:**
- Long and hard to type
- Different on every computer (alice vs bob, C: vs D:)
- If you share code, paths break

### Relative Paths: Directions from Here

A **relative path** is relative to your program's **current working directory**.

If your program runs from `/Users/alice/Projects/MyApp/`:

```java
// Relative path - file is IN the current directory
"students.txt"
// Means: /Users/alice/Projects/MyApp/students.txt

// Relative path - file is in a SUBFOLDER
"data/students.txt"
// Means: /Users/alice/Projects/MyApp/data/students.txt

// Relative path - file is in PARENT folder
"../other.txt"
// Means: /Users/alice/Projects/other.txt
```

**Advantages of relative paths:**
- Short and readable
- Work on any computer if folder structure matches
- Good for projects you share

**Disadvantages:**
- Depend on where program runs from
- IDEs may set unexpected working directories

### The IDE Trap

**WARNING**: When you run from an IDE, the working directory is often NOT what you expect!

```
Your project structure:
MyApp/
  src/
    Main.java
  data/
    students.txt

You write: new File("data/students.txt")

BUT the IDE runs from: MyApp/
So it looks for:       MyApp/data/students.txt  --> FOUND!

OR the IDE runs from:  MyApp/src/
So it looks for:       MyApp/src/data/students.txt  --> NOT FOUND!
```

**Solution**: Check what the File class thinks is the current directory:

```java
// Print the current working directory
System.out.println(System.getProperty("user.dir"));
// This tells you WHERE relative paths start from!
```

### Best Practice: Use Relative Paths in Projects

```java
// Good - works if project structure is maintained
File file = new File("data/students.txt");

// Also good for files in same folder as project root
File file = new File("students.txt");

// Use absolute only when you NEED a specific location
File file = new File("/tmp/tempdata.txt");  // System temp folder
```

---

## The File Class

### What Is the File Class?

The `File` class represents a file or directory path. **Important**: Creating a File object does NOT create an actual file on disk! It is just a representation of a path.

```java
import java.io.File;

// This creates a File OBJECT, not an actual file!
File myFile = new File("students.txt");

// The file may or may not exist yet
// File object just represents the path
```

### Why File Class Exists

**Think of it this way:**

- A `String` like `"students.txt"` is just text
- A `File` object KNOWS it represents a file path
- `File` has useful methods for working with files

### Essential File Methods

```java
File file = new File("students.txt");

// Does this file actually exist on disk?
boolean exists = file.exists();  // true or false

// Is it a file (not a directory)?
boolean isFile = file.isFile();  // true or false

// Is it a directory (folder)?
boolean isDir = file.isDirectory();  // true or false

// What is the file name?
String name = file.getName();  // "students.txt"

// What is the full path?
String path = file.getAbsolutePath();  // "/Users/.../students.txt"

// How big is the file in bytes?
long size = file.length();  // e.g., 1024

// Can we read this file?
boolean readable = file.canRead();  // true or false

// Can we write to this file?
boolean writable = file.canWrite();  // true or false
```

### Checking Before Opening

**Always check if a file exists before reading!**

```java
File file = new File("students.txt");

if (file.exists()) {
    // Safe to read
    Scanner scanner = new Scanner(file);
    // ... read data
} else {
    System.out.println("Error: File not found at " + file.getAbsolutePath());
}
```

### Creating Directories

Sometimes you need to create folders for your files:

```java
File dataFolder = new File("data");

if (!dataFolder.exists()) {
    boolean created = dataFolder.mkdir();  // Create single directory
    if (created) {
        System.out.println("Created data folder");
    }
}

// For nested folders like data/backup/2024
File nestedFolder = new File("data/backup/2024");
nestedFolder.mkdirs();  // Creates ALL necessary parent folders
```

### Listing Files in a Directory

```java
File folder = new File("data");

if (folder.isDirectory()) {
    File[] files = folder.listFiles();
    for (File f : files) {
        System.out.println(f.getName());
    }
}
```

---

## Reading Files with Scanner

### The Big Connection: Scanner Revisited!

Remember Week 1? You used Scanner to read keyboard input:

```java
// Week 1: Reading from keyboard
Scanner keyboard = new Scanner(System.in);
String name = keyboard.nextLine();
```

**Week 11 revelation**: Scanner can read from files too! Same methods, different source.

```java
// Week 11: Reading from file
File file = new File("students.txt");
Scanner fileScanner = new Scanner(file);
String line = fileScanner.nextLine();
```

The difference is what you pass to the Scanner constructor:
- `System.in` = keyboard
- `File object` = file

### Basic File Reading

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadFileDemo {
    public static void main(String[] args) {
        try {
            File file = new File("message.txt");
            Scanner scanner = new Scanner(file);

            // Read entire file line by line
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                System.out.println(line);
            }

            scanner.close();  // Always close when done!

        } catch (FileNotFoundException e) {
            System.out.println("Could not find the file!");
        }
    }
}
```

### Understanding the try-catch

**Why the try-catch?** Files can be missing, locked, or corrupted. Java REQUIRES you to handle the possibility of file problems. This is called **exception handling**.

For now, think of it as:

```java
try {
    // "Try to do this risky thing..."
    Scanner scanner = new Scanner(file);
    // work with file

} catch (FileNotFoundException e) {
    // "...but if the file isn't found, do this instead"
    System.out.println("File not found!");
}
```

Week 12 will explain exceptions in depth. For now, just include this pattern when working with files.

### Scanner Methods You Already Know

All the Scanner methods from Week 1 work with files:

| Method | What It Does | Returns |
|--------|--------------|---------|
| `hasNextLine()` | Is there another line to read? | boolean |
| `nextLine()` | Read and return the next line | String |
| `hasNext()` | Is there another word/token? | boolean |
| `next()` | Read and return next word/token | String |
| `hasNextInt()` | Is the next token an integer? | boolean |
| `nextInt()` | Read and return next integer | int |
| `hasNextDouble()` | Is the next token a double? | boolean |
| `nextDouble()` | Read and return next double | double |

### Reading Line by Line

The most common pattern - read each line as a String:

```java
// students.txt contains:
// Alice
// Bob
// Charlie

File file = new File("students.txt");
Scanner scanner = new Scanner(file);

while (scanner.hasNextLine()) {
    String name = scanner.nextLine();
    System.out.println("Found student: " + name);
}

scanner.close();

// Output:
// Found student: Alice
// Found student: Bob
// Found student: Charlie
```

### Reading Word by Word

Use `next()` to read individual words (separated by whitespace):

```java
// words.txt contains:
// Hello world this is Java

File file = new File("words.txt");
Scanner scanner = new Scanner(file);

while (scanner.hasNext()) {
    String word = scanner.next();
    System.out.println("Word: " + word);
}

scanner.close();

// Output:
// Word: Hello
// Word: world
// Word: this
// Word: is
// Word: Java
```

### Reading Numbers

If your file contains numbers, read them directly:

```java
// numbers.txt contains:
// 10 20 30 40 50

File file = new File("numbers.txt");
Scanner scanner = new Scanner(file);

int sum = 0;
while (scanner.hasNextInt()) {
    int number = scanner.nextInt();
    sum += number;
}

scanner.close();
System.out.println("Sum: " + sum);  // Sum: 150
```

### The Importance of Closing

**Always close your Scanner when done!**

```java
Scanner scanner = new Scanner(file);
// ... use scanner
scanner.close();  // IMPORTANT!
```

**Why?** Open files consume system resources. If you open many files without closing them, your program (or even your computer) can run out of resources.

---

## Try-With-Resources: Automatic Closing

### The Problem with Manual Closing

Manual closing has a problem - what if an error occurs BEFORE close()?

```java
Scanner scanner = new Scanner(file);
String line = scanner.nextLine();  // What if this throws an exception?
int value = Integer.parseInt(line); // Or this?
scanner.close();  // This might never run!
```

If an exception occurs, `close()` is skipped, and resources leak.

### The Solution: Try-With-Resources

Java provides **try-with-resources** syntax that GUARANTEES closing:

```java
try (Scanner scanner = new Scanner(file)) {
    // Use scanner here
    while (scanner.hasNextLine()) {
        System.out.println(scanner.nextLine());
    }
}  // Scanner is AUTOMATICALLY closed here, even if an error occurs!
```

**How to read this:**
- `try (resource declaration)` - create resource in parentheses
- Resource is automatically closed when the block ends
- Works even if an exception is thrown!

### Combining with Exception Handling

```java
try (Scanner scanner = new Scanner(file)) {
    while (scanner.hasNextLine()) {
        System.out.println(scanner.nextLine());
    }
} catch (FileNotFoundException e) {
    System.out.println("File not found: " + file.getAbsolutePath());
}
// Scanner is closed automatically in ALL cases
```

### Multiple Resources

You can declare multiple resources:

```java
try (Scanner scanner = new Scanner(inputFile);
     PrintWriter writer = new PrintWriter(outputFile)) {

    while (scanner.hasNextLine()) {
        String line = scanner.nextLine();
        writer.println(line.toUpperCase());
    }
}  // Both scanner AND writer are closed automatically
```

### Best Practice

**Always use try-with-resources for file operations!** It is cleaner and safer.

```java
// Old way (avoid)
Scanner scanner = null;
try {
    scanner = new Scanner(file);
    // use scanner
} finally {
    if (scanner != null) {
        scanner.close();
    }
}

// Modern way (use this!)
try (Scanner scanner = new Scanner(file)) {
    // use scanner
}
```

---

## Writing Files with PrintWriter

### PrintWriter: Your Writing Secretary

Just as Scanner reads files, **PrintWriter** writes files. And just as Scanner mirrors keyboard input, PrintWriter mirrors console output.

```java
// Console output (you know this):
System.out.println("Hello");
System.out.printf("Value: %d", 42);

// File output (same methods!):
PrintWriter writer = new PrintWriter("output.txt");
writer.println("Hello");
writer.printf("Value: %d", 42);
writer.close();
```

### Basic File Writing

```java
import java.io.PrintWriter;
import java.io.FileNotFoundException;

public class WriteFileDemo {
    public static void main(String[] args) {
        try (PrintWriter writer = new PrintWriter("output.txt")) {

            writer.println("Line 1");
            writer.println("Line 2");
            writer.println("Line 3");

        } catch (FileNotFoundException e) {
            System.out.println("Could not create file!");
        }
    }
}

// output.txt now contains:
// Line 1
// Line 2
// Line 3
```

### PrintWriter Methods

| Method | What It Does |
|--------|--------------|
| `print(value)` | Write value without newline |
| `println(value)` | Write value with newline |
| `printf(format, args)` | Formatted output (like System.out.printf) |
| `flush()` | Force buffered data to be written |
| `close()` | Close the file |

### Writing Different Data Types

```java
try (PrintWriter writer = new PrintWriter("data.txt")) {

    // Write String
    writer.println("Hello World");

    // Write numbers
    writer.println(42);
    writer.println(3.14159);

    // Write formatted
    writer.printf("Name: %s, Age: %d%n", "Alice", 25);

    // Write without newline
    writer.print("Same ");
    writer.print("line");
    writer.println();  // Now add newline
}
```

### WARNING: Overwrite Mode by Default

**PrintWriter OVERWRITES existing files by default!**

```java
// File has: "Important data"

try (PrintWriter writer = new PrintWriter("file.txt")) {
    writer.println("New data");
}

// File now has: "New data"
// Old data is GONE!
```

### Append Mode: Adding to Existing Files

To ADD to a file instead of overwriting, use FileWriter with append flag:

```java
import java.io.FileWriter;
import java.io.PrintWriter;

// Append mode - adds to end of file
try (PrintWriter writer = new PrintWriter(new FileWriter("log.txt", true))) {
    writer.println("New log entry");
}  // Existing content preserved, new content added at end
```

The `true` parameter enables **append mode**.

---

## PrintWriter vs PrintStream vs FileOutputStream

### Why Three Options?

Java offers multiple ways to write files. Here is when to use each:

| Class | Use When | Example |
|-------|----------|---------|
| **PrintWriter** | Text files, formatted output | Writing CSV, logs, reports |
| **PrintStream** | Same as PrintWriter | System.out IS a PrintStream! |
| **FileOutputStream** | Binary files, raw bytes | Images, compiled code, databases |

### For This Course: Use PrintWriter

PrintWriter is the right choice for text files:
- Same methods as System.out
- Easy formatted output
- Human-readable files

```java
// PrintWriter for text files (USE THIS)
try (PrintWriter writer = new PrintWriter("students.txt")) {
    writer.println("Alice,101");
    writer.println("Bob,102");
}
```

### PrintStream: System.out's Type

`System.out` is actually a PrintStream! So PrintStream methods are identical:

```java
// These are essentially the same
PrintStream out = System.out;
out.println("Hello");

PrintWriter writer = new PrintWriter("file.txt");
writer.println("Hello");
```

### FileOutputStream: For Binary Data

FileOutputStream writes raw bytes - for images, audio, or data files:

```java
// Binary output - NOT for this course's exercises
try (FileOutputStream fos = new FileOutputStream("data.bin")) {
    fos.write(65);  // Writes the byte 65 (letter 'A' in ASCII)
}
```

**For Week 11**: Focus on PrintWriter for text files!

---

## Parsing Structured Data

### What Is Structured Data?

Real files often have **structure** - data organized in a specific format.

**CSV (Comma-Separated Values)** is the most common:

```
name,age,grade
Alice,20,A
Bob,22,B
Charlie,19,A
```

Each line is a record. Each comma separates a field.

### Reading CSV Files

**Strategy**: Read line by line, then split each line.

```java
// students.csv contains:
// Alice,101,A
// Bob,102,B
// Charlie,103,A

try (Scanner scanner = new Scanner(new File("students.csv"))) {
    while (scanner.hasNextLine()) {
        String line = scanner.nextLine();

        // Split the line by commas
        String[] parts = line.split(",");

        String name = parts[0];           // "Alice"
        int id = Integer.parseInt(parts[1]); // 101
        String grade = parts[2];          // "A"

        System.out.println(name + " (ID: " + id + ") has grade " + grade);
    }
}
```

### Understanding String.split()

`split()` divides a String into an array based on a delimiter:

```java
String line = "Alice,101,A";
String[] parts = line.split(",");

// parts[0] = "Alice"
// parts[1] = "101"
// parts[2] = "A"
// parts.length = 3
```

### Different Delimiters

Not all files use commas. Split works with any delimiter:

```java
// Semicolons
String line = "Alice;101;A";
String[] parts = line.split(";");

// Tabs
String line = "Alice\t101\tA";  // \t is tab character
String[] parts = line.split("\t");

// Multiple spaces (regex)
String line = "Alice    101    A";
String[] parts = line.split("\\s+");  // One or more whitespace
```

### Handling Headers

Many CSV files have a header row:

```
name,id,grade
Alice,101,A
Bob,102,B
```

Skip the header:

```java
try (Scanner scanner = new Scanner(new File("students.csv"))) {
    // Skip header line
    if (scanner.hasNextLine()) {
        scanner.nextLine();  // Read and discard header
    }

    // Process data lines
    while (scanner.hasNextLine()) {
        String line = scanner.nextLine();
        String[] parts = line.split(",");
        // ... process parts
    }
}
```

### Edge Case: Empty Lines

Files sometimes have empty lines. Handle them:

```java
while (scanner.hasNextLine()) {
    String line = scanner.nextLine();

    // Skip empty lines
    if (line.trim().isEmpty()) {
        continue;
    }

    String[] parts = line.split(",");
    // ... process
}
```

### Edge Case: Values Containing Delimiters

What if a value CONTAINS a comma?

```
name,description,price
Widget,"A small, useful item",9.99
```

This is tricky! The simple `split(",")` breaks:
- parts[0] = "Widget"
- parts[1] = "\"A small"
- parts[2] = " useful item\""
- parts[3] = "9.99"

**For this course**: Assume clean data without this problem. In real projects, use a CSV library.

---

## Saving Objects to Files

### The Big Picture: Persistence!

Now we combine EVERYTHING you have learned:
- **Objects** from Weeks 7-10
- **File I/O** from this week
- Result: **Persistent objects that survive program restarts!**

### Strategy 1: Using toString()

If your class has a good toString(), use it:

```java
public class Student {
    private String name;
    private int id;

    public Student(String name, int id) {
        this.name = name;
        this.id = id;
    }

    @Override
    public String toString() {
        return name + "," + id;  // CSV format!
    }
}

// Saving students to file
ArrayList<Student> students = new ArrayList<>();
students.add(new Student("Alice", 101));
students.add(new Student("Bob", 102));

try (PrintWriter writer = new PrintWriter("students.txt")) {
    for (Student s : students) {
        writer.println(s.toString());
        // Or simply: writer.println(s); - toString() called automatically
    }
}

// students.txt now contains:
// Alice,101
// Bob,102
```

### Strategy 2: Using Getters

For more control over the format:

```java
try (PrintWriter writer = new PrintWriter("students.txt")) {
    for (Student s : students) {
        writer.printf("%s;%d%n", s.getName(), s.getId());
    }
}

// students.txt:
// Alice;101
// Bob;102
```

### Which Strategy to Choose?

| Use toString() when: | Use getters when: |
|---------------------|-------------------|
| Format is simple | Need different formats for file vs display |
| One format is enough | File format differs from display format |
| Quick and easy | More control needed |

### Example: Saving Your Car Objects

Remember the Car class from Week 7?

```java
public class Car {
    private String brand;
    private String model;
    private int year;
    private double price;

    // ... constructor, getters ...

    @Override
    public String toString() {
        return brand + "," + model + "," + year + "," + price;
    }
}

// Save cars to file
ArrayList<Car> cars = new ArrayList<>();
cars.add(new Car("Toyota", "Camry", 2020, 25000.00));
cars.add(new Car("Honda", "Civic", 2021, 22000.00));

try (PrintWriter writer = new PrintWriter("cars.csv")) {
    // Write header
    writer.println("brand,model,year,price");

    // Write data
    for (Car car : cars) {
        writer.println(car);
    }
}

// cars.csv:
// brand,model,year,price
// Toyota,Camry,2020,25000.0
// Honda,Civic,2021,22000.0
```

---

## Loading Objects from Files

### Reversing the Process

Saving is only half the story. We need to load objects back!

**The process:**
1. Read a line from file
2. Split into parts
3. Parse parts into appropriate types
4. Create object with parsed values
5. Add to collection

### Loading Students

```java
public static ArrayList<Student> loadStudents(String filename) {
    ArrayList<Student> students = new ArrayList<>();

    try (Scanner scanner = new Scanner(new File(filename))) {
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            String[] parts = line.split(",");

            String name = parts[0];
            int id = Integer.parseInt(parts[1]);

            Student student = new Student(name, id);
            students.add(student);
        }
    } catch (FileNotFoundException e) {
        System.out.println("Could not load students: " + e.getMessage());
    }

    return students;
}

// Usage:
ArrayList<Student> students = loadStudents("students.txt");
```

### Loading Cars (With Header)

```java
public static ArrayList<Car> loadCars(String filename) {
    ArrayList<Car> cars = new ArrayList<>();

    try (Scanner scanner = new Scanner(new File(filename))) {
        // Skip header line
        if (scanner.hasNextLine()) {
            scanner.nextLine();
        }

        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();

            if (line.trim().isEmpty()) {
                continue;  // Skip empty lines
            }

            String[] parts = line.split(",");

            String brand = parts[0];
            String model = parts[1];
            int year = Integer.parseInt(parts[2]);
            double price = Double.parseDouble(parts[3]);

            cars.add(new Car(brand, model, year, price));
        }
    } catch (FileNotFoundException e) {
        System.out.println("File not found: " + filename);
    }

    return cars;
}
```

### Complete CRUD Pattern

A real application needs all four operations:

```java
public class StudentManager {
    private ArrayList<Student> students;
    private String filename;

    public StudentManager(String filename) {
        this.filename = filename;
        this.students = new ArrayList<>();
    }

    // CREATE
    public void addStudent(Student s) {
        students.add(s);
    }

    // READ
    public Student findById(int id) {
        for (Student s : students) {
            if (s.getId() == id) {
                return s;
            }
        }
        return null;
    }

    // UPDATE
    public void updateStudent(int id, String newName) {
        Student s = findById(id);
        if (s != null) {
            s.setName(newName);
        }
    }

    // DELETE
    public void removeStudent(int id) {
        Student s = findById(id);
        if (s != null) {
            students.remove(s);
        }
    }

    // LOAD from file
    public void load() {
        students.clear();
        try (Scanner scanner = new Scanner(new File(filename))) {
            while (scanner.hasNextLine()) {
                String[] parts = scanner.nextLine().split(",");
                students.add(new Student(parts[0], Integer.parseInt(parts[1])));
            }
        } catch (FileNotFoundException e) {
            System.out.println("No existing file, starting fresh.");
        }
    }

    // SAVE to file
    public void save() {
        try (PrintWriter writer = new PrintWriter(filename)) {
            for (Student s : students) {
                writer.println(s);
            }
        } catch (FileNotFoundException e) {
            System.out.println("Could not save!");
        }
    }
}
```

---

## INI File Reading

### What Is an INI File?

INI files are a simple configuration format:

```ini
[Settings]
language=Danish
theme=dark
volume=75

[User]
name=Alice
level=5
```

Sections are in `[brackets]`, settings are `key=value` pairs.

### Parsing INI Files

```java
public class IniReader {

    public static void readIniFile(String filename) {
        try (Scanner scanner = new Scanner(new File(filename))) {
            String currentSection = "";

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine().trim();

                // Skip empty lines and comments
                if (line.isEmpty() || line.startsWith(";") || line.startsWith("#")) {
                    continue;
                }

                // Check for section header
                if (line.startsWith("[") && line.endsWith("]")) {
                    currentSection = line.substring(1, line.length() - 1);
                    System.out.println("Section: " + currentSection);
                }
                // Parse key=value
                else if (line.contains("=")) {
                    String[] parts = line.split("=", 2);  // Split into max 2 parts
                    String key = parts[0].trim();
                    String value = parts[1].trim();
                    System.out.println("  " + key + " = " + value);
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("INI file not found!");
        }
    }
}
```

---

## Text Files vs Binary Files

### Conceptual Understanding

**Text files** store data as human-readable characters:
- You can open them in Notepad/TextEdit
- Characters are encoded (UTF-8, ASCII)
- Examples: .txt, .csv, .java, .html

**Binary files** store data as raw bytes:
- Opening in Notepad shows garbage
- More compact and faster
- Examples: .jpg, .mp3, .exe, .class

```
Text file (students.txt):        Binary equivalent:
A l i c e , 1 0 1               41 6C 69 63 65 2C 31 30 31
(readable characters)            (raw byte values)
```

### For This Course

**Focus on text files!** They are:
- Easier to debug (you can read them)
- Good for data interchange
- Sufficient for most programming exercises

Binary files are for specialized applications (images, audio, databases) which are beyond this course.

---

## Connecting to What You Already Know

### Week 1: Scanner Gets a New Job

```java
// Week 1: Reading from keyboard
Scanner keyboard = new Scanner(System.in);
String input = keyboard.nextLine();

// Week 11: Same Scanner, reading from file!
Scanner file = new Scanner(new File("data.txt"));
String line = file.nextLine();

// Same methods: nextLine(), nextInt(), hasNext(), etc.
// Different source: System.in vs File
```

### Week 3: Loops Power File Reading

```java
// Week 3: Loop basics
while (condition) {
    // do something
}

// Week 11: Loops read entire files
while (scanner.hasNextLine()) {
    String line = scanner.nextLine();
    // process line
}
```

### Week 6: Arrays Store File Data

```java
// Week 6: Array of primitives
int[] numbers = new int[5];

// Week 11: Parse file line into array
String line = "10,20,30,40,50";
String[] parts = line.split(",");  // String array!
```

### Week 10: ArrayList for Dynamic Data

```java
// Week 10: ArrayList grows as needed
ArrayList<String> lines = new ArrayList<>();

// Week 11: Perfect for unknown file size
while (scanner.hasNextLine()) {
    lines.add(scanner.nextLine());
}
// lines.size() tells you how many lines were read
```

### Weeks 7-10: Objects Get Persistence

```java
// Weeks 7-10: Creating objects
Student alice = new Student("Alice", 101);

// Week 11: Saving objects
writer.println(alice.toString());

// Week 11: Loading objects
String[] parts = line.split(",");
Student loaded = new Student(parts[0], Integer.parseInt(parts[1]));
```

### The Complete Picture

| Week | Skill | File I/O Application |
|------|-------|---------------------|
| 1 | Scanner | Read files instead of keyboard |
| 1 | System.out | PrintWriter mirrors it for files |
| 3 | Loops | while(hasNextLine()) pattern |
| 6 | Arrays | split() returns String[] |
| 10 | ArrayList | Store loaded objects |
| 10 | Wrapper classes | Integer.parseInt() for loading |
| 7-9 | Objects | toString() and constructors for save/load |

---

## Common Struggles and How to Overcome Them

### Struggle 1: File Path Confusion

**The problem:** "File not found!" even though the file exists.

**Why it happens:** Relative paths depend on the working directory, which varies by how you run the program.

**Solution:**

```java
// Step 1: Find out where your program thinks it is
System.out.println("Working directory: " + System.getProperty("user.dir"));

// Step 2: Use absolute path to test
File file = new File("/Users/alice/projects/myapp/data.txt");

// Step 3: Check if file exists
File file = new File("data.txt");
System.out.println("Looking for: " + file.getAbsolutePath());
System.out.println("Exists: " + file.exists());
```

### Struggle 2: Forgetting to Close Files

**The problem:** Resources leak, files stay locked.

**Solution:** Always use try-with-resources!

```java
// BAD - might forget to close
Scanner scanner = new Scanner(file);
// ... use scanner
scanner.close();  // What if an exception happens before this?

// GOOD - automatic closing
try (Scanner scanner = new Scanner(file)) {
    // ... use scanner
}  // Automatically closed!
```

### Struggle 3: Scanner Delimiter Issues

**The problem:** Data does not parse correctly.

**Why:** Scanner's default delimiter is whitespace, but your file might use commas.

**Solutions:**

```java
// Option 1: Read line, then split
String line = scanner.nextLine();
String[] parts = line.split(",");

// Option 2: Change Scanner's delimiter
scanner.useDelimiter(",");
String field1 = scanner.next();
String field2 = scanner.next();
```

### Struggle 4: Number Parsing Errors

**The problem:** `NumberFormatException` when parsing.

**Why:** Extra whitespace, wrong format, or non-numeric data.

**Solution:**

```java
String value = parts[1];

// Trim whitespace first!
int number = Integer.parseInt(value.trim());

// Or handle the possibility of bad data
try {
    int number = Integer.parseInt(value.trim());
} catch (NumberFormatException e) {
    System.out.println("Invalid number: " + value);
    // Use default or skip this record
}
```

### Struggle 5: Choosing Output Method

**The problem:** When to use `print()` vs `println()` vs `printf()`?

**Answer:**

| Method | When to Use |
|--------|-------------|
| `println(x)` | One value per line, simple output |
| `print(x)` | Multiple values on same line |
| `printf(format, args)` | Formatted output, alignment, decimal places |

```java
// println - each on its own line
writer.println("Alice");
writer.println("Bob");

// print - build up a line
writer.print("Alice");
writer.print(",");
writer.println("101");  // End the line

// printf - formatted
writer.printf("%s,%d,%.2f%n", "Alice", 101, 95.5);
```

### Struggle 6: Overwriting vs Appending

**The problem:** File gets overwritten when you wanted to add to it.

**Solution:** Use append mode:

```java
// OVERWRITES (default)
PrintWriter writer = new PrintWriter("log.txt");

// APPENDS (adds to end)
PrintWriter writer = new PrintWriter(new FileWriter("log.txt", true));
```

---

## Practice Exercises

### Exercise 1: FileFunReading (meget hjaelp - Maximum Guidance)

**Goal:** Practice basic file reading with Scanner.

Create a file called `greetings.txt` with these contents:
```
Hello World
Welcome to Java
File I/O is fun
Happy coding!
```

**Part A: Read and print all lines**

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FileFunReading {
    public static void main(String[] args) {
        // TODO: Create a File object for "greetings.txt"

        // TODO: Create a Scanner for the file (use try-with-resources)

        // TODO: Use while(hasNextLine()) to read each line

        // TODO: Print each line with a line number prefix
        // Expected output:
        // Line 1: Hello World
        // Line 2: Welcome to Java
        // Line 3: File I/O is fun
        // Line 4: Happy coding!
    }
}
```

**Part B: Count words**

Modify your program to also count the total number of words in the file.

**Part C: Find longest line**

Add code to find and print the longest line in the file.

### Exercise 2: FileFunWriting (meget hjaelp - Maximum Guidance)

**Goal:** Practice writing files with PrintWriter.

**Part A: Write multiplication table**

```java
import java.io.PrintWriter;
import java.io.FileNotFoundException;

public class FileFunWriting {
    public static void main(String[] args) {
        // TODO: Create PrintWriter for "multiplication.txt"

        // TODO: Write a 10x10 multiplication table
        // Each row should be: 1x1=1, 1x2=2, ..., 1x10=10
        // Use printf for nice formatting!

        // Expected file content:
        //  1   2   3   4   5   6   7   8   9  10
        //  2   4   6   8  10  12  14  16  18  20
        // ...
    }
}
```

**Part B: Number statistics**

Write a program that:
1. Asks user to enter numbers (use Scanner with System.in)
2. Stores them in an ArrayList<Integer>
3. When user enters -1, stop collecting
4. Write statistics to "stats.txt": count, sum, average, min, max

### Exercise 3: Init From File (nogen hjaelp - Moderate Guidance)

**Goal:** Parse an INI configuration file.

Create `config.ini`:
```ini
[Application]
name=MyAwesomeApp
version=1.0.0
debug=true

[User]
username=alice
theme=dark
language=danish

[Limits]
max_items=100
timeout=30
```

Write a program that:
1. Reads the INI file
2. Stores settings in appropriate data structures
3. Provides methods to get settings by section and key
4. Prints all settings in a formatted way

**Hints:**
- Use a Map<String, Map<String, String>> to store sections and their key-value pairs
- Detect sections with line.startsWith("[")
- Split key=value lines on "="

### Exercise 4: MyFriends (ingen hjaelp - Minimal Guidance)

**Goal:** Build a complete CRUD application with file persistence.

Create a friend management system:

**Friend class:**
- name (String)
- phone (String)
- email (String)
- birthday (String in format "DD-MM-YYYY")

**FriendManager class:**
- ArrayList<Friend> friends
- Load friends from "friends.csv" on startup
- Save friends to "friends.csv" on exit
- Methods: addFriend, removeFriend, findByName, listAll, updateFriend

**Main program (text menu):**
```
=== My Friends ===
1. List all friends
2. Add new friend
3. Find friend by name
4. Update friend
5. Remove friend
6. Save and exit
Choose:
```

**Requirements:**
- Friends persist between program runs
- Handle file not existing on first run
- Validate input (non-empty names, valid email format)
- Use try-with-resources for all file operations

---

## Looking Ahead

### Week 12: Exception Handling

This week you used basic try-catch for file operations. Week 12 dives deep:

- **What exceptions really are** - objects representing errors
- **Checked vs unchecked exceptions** - why files require try-catch but arrays don't
- **Creating custom exceptions** - your own error types
- **The exception hierarchy** - how exceptions are organized
- **Best practices** - when to catch, when to throw

Your FileNotFoundException experience prepares you perfectly!

### Week 13: Unit Testing

Your file I/O code needs testing:
- Does loading work with empty files?
- Does saving handle special characters?
- What happens with missing files?

Unit testing lets you verify these scenarios automatically.

### Weeks 14-15: Sorting and Interfaces

Your loaded data often needs sorting:

```java
ArrayList<Student> students = loadFromFile("students.csv");
Collections.sort(students);  // How does Java know how to sort Students?
// Week 14-15 will teach you!
```

---

## Key Takeaways

1. **Files provide persistence** - data survives after program ends

2. **File paths** are addresses: absolute (full path) or relative (from current location)

3. **Scanner reads files** the same way it reads keyboard - same methods, different source

4. **PrintWriter writes files** the same way System.out prints - same methods, different destination

5. **Try-with-resources** guarantees files are closed: `try (Scanner s = new Scanner(file)) { }`

6. **String.split()** parses delimited data: `"Alice,101".split(",")` returns `["Alice", "101"]`

7. **Save objects** using toString() or getters

8. **Load objects** by parsing strings back into constructor arguments

9. **Always close files** - use try-with-resources to do it automatically

10. **PrintWriter overwrites by default** - use FileWriter with append flag to add to files

11. **Check file.exists()** before reading to avoid errors

12. **Text files are human-readable**, binary files store raw bytes

13. **File I/O + OOP = Persistent applications** - your Week 7-10 objects can now live forever!

---

## For the Next Topic Agent

### Terminology Established This Week

- **file path**: Location of a file on the computer's filesystem
- **absolute path**: Full path from filesystem root (/Users/alice/file.txt)
- **relative path**: Path relative to current working directory (data/file.txt)
- **File class**: Java class representing a file or directory path (not the actual file)
- **Scanner (for files)**: Same Scanner class from Week 1, now reading from File instead of System.in
- **PrintWriter**: Class for writing text to files, mirrors System.out methods
- **PrintStream**: Similar to PrintWriter, System.out is a PrintStream
- **FileOutputStream**: Low-level class for writing binary data
- **try-with-resources**: `try (resource) { }` syntax that auto-closes resources
- **delimiter**: Character(s) separating values in structured data (comma in CSV)
- **CSV**: Comma-Separated Values file format
- **INI file**: Configuration file format with [sections] and key=value pairs
- **parsing**: Converting text representation back into data types/objects
- **persistence**: Data that survives after program terminates
- **append mode**: Adding to end of file instead of overwriting
- **overwrite mode**: Replacing entire file contents (PrintWriter default)
- **text file**: Human-readable file storing characters
- **binary file**: File storing raw byte data

### Concepts From Prior Weeks Applied

| Prior Week | Concept | Week 11 Application |
|------------|---------|---------------------|
| Week 1 | Scanner | Now reads from files |
| Week 1 | System.out.println | PrintWriter.println mirrors it |
| Week 3 | while loops | while(hasNextLine()) pattern |
| Week 6 | Arrays | String[] from split() |
| Week 10 | ArrayList | Store loaded objects dynamically |
| Week 10 | Wrapper classes | Integer.parseInt(), Double.parseDouble() |
| Week 7-9 | Objects/OOP | toString() for saving, constructors for loading |
| Week 8 | Encapsulation | Getters for custom save formats |

### Student Capabilities After This Week

Students can now:
- Work with file paths (absolute and relative)
- Read text files line by line with Scanner
- Write text files with PrintWriter
- Use try-with-resources for safe file handling
- Parse CSV and delimited files with String.split()
- Save object collections to files
- Load object collections from files
- Handle basic file I/O exceptions (FileNotFoundException)
- Choose between overwrite and append mode
- Check file existence and properties with File class

### Critical Concepts for Week 12 (Exceptions)

Week 12 should build on these Week 11 foundations:
- **FileNotFoundException** already encountered - expand to full exception hierarchy
- **try-catch basics** introduced - now add finally, multi-catch, throw, throws
- **Checked exceptions** - explain why file operations require try-catch
- **Resource management** - deepen try-with-resources understanding

Exception patterns students have seen:
```java
try {
    Scanner s = new Scanner(new File("data.txt"));
} catch (FileNotFoundException e) {
    System.out.println("File not found!");
}
```

Week 12 will explain:
- What FileNotFoundException actually IS (an object!)
- The exception class hierarchy
- Creating custom exceptions
- When to catch vs when to throw
- Best practices for exception handling

### Common Misconceptions to Address Later

1. "Files automatically close when the program ends" - True eventually, but relying on this is bad practice
2. "PrintWriter creates the file if it doesn't exist" - True, but important to understand
3. "Scanner and PrintWriter are the only options" - BufferedReader/Writer exist for efficiency
4. "All file operations need try-catch" - Only checked exceptions like FileNotFoundException

### Assessment Preparation Notes

File handling comprises 20-25% of exam. Key patterns:
1. Read a file and process each line
2. Parse CSV into objects
3. Save a collection of objects to file
4. Load objects from file into ArrayList
5. Handle FileNotFoundException appropriately
6. Use try-with-resources for resource management
7. Choose appropriate file output method

Typical exam question pattern:
- Given: A file format (CSV, custom delimited)
- Task: Read file, create objects, process, save results
- Requirements: Proper exception handling, resource management
