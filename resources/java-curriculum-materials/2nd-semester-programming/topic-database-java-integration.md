# Database-Java Integration - 2nd Semester Programming

*Prerequisites: ADT & Collections (List, ArrayList), SQL Fundamentals (SELECT, JOINs, DML), SQL Advanced (subqueries, views, stored procedures)*
*Phase: 3-4 (Advanced Database & Collections Integration / Kailua Project)*
*Exam Weight: High (JdbcTemplate, RowMapper, and layered architecture are heavily emphasized)*

---

## What You'll Learn

By the end of this topic, you will be able to:
- **Integrate Collections with database results** using the `List<DomainObject>` pattern
- **Implement RowMapper** to convert SQL ResultSet rows into Java objects
- **Use JdbcTemplate** for all database operations (query, queryForObject, update)
- **Design repository classes** following the Information Expert principle
- **Understand the complete data flow** from MySQL through Java layers
- **Map database columns to Java properties** with correct type conversions
- **Handle nested object relationships** from SQL JOIN results

This is a **critical integration topic**. Everything you've learned - Collections from Phase 1, SQL from Phases 2-3, and OOP from 1st semester - converges here. You're not learning isolated skills anymore; you're learning how they work *together* to build real applications.

---

## Why This Matters

### The Integration Challenge

Until now, you've worked with:
- **Collections in isolation:** Creating `ArrayList<Car>`, iterating, sorting
- **SQL in isolation:** Writing queries, getting results in MySQL Workbench
- **Java classes in isolation:** Building domain objects with constructors, getters, setters

But real applications don't work in isolation. Consider Kailua Car Rental:

**The problem:** Customer data lives in MySQL. Your Java application needs that data as `Customer` objects stored in a `List<Customer>`.

**The gap:** SQL returns rows of strings and numbers. Java expects typed objects with methods.

**The solution:** Database-Java integration patterns bridge this gap.

### The Data Flow You'll Build

```
[MySQL Database]
       |
       | SQL Query: "SELECT * FROM customers"
       v
[JDBC ResultSet] -- Row-by-row data
       |
       | RowMapper: rs -> new Customer(rs.getInt("id"), rs.getString("name"))
       v
[List<Customer>] -- Java objects ready for your application
       |
       | Repository returns to Service
       v
[Service Layer / Controller]
```

This data flow is **the same pattern** you'll use in:
- Kailua Car Rental (console application this week)
- Onskeskyen Wishlist (web application in Phase 7)
- Your exam project
- Professional Java development

Learning this pattern well now pays dividends throughout the semester and your career.

### Connecting to What You Already Know

**From Collections (Phase 1):** You learned that `List<Car>` declares *what* you want (a list of cars) without specifying *how* (ArrayList, LinkedList). Database integration uses this same pattern - your repository returns `List<Customer>`, and the caller doesn't care how it was populated.

**From SQL (Phases 2-3):** You learned to write queries that return exactly the data you need. Those same queries now execute from Java, and their results become objects.

**From 1st Semester OOP:** Your domain classes (Car, Customer, RentalContract) with constructors and getters are the "destination" for database data.

**From GRASP (Systems Development):** The Repository pattern is the **Information Expert** principle in action - the class with database connection knowledge handles database operations.

---

## The Architecture: Where This Fits

### Layered Application Architecture

Professional Java applications organize code into layers with distinct responsibilities:

```
[User Interface / Controller]
           |
           | calls
           v
[@Service - Business Logic Layer]
           |
           | calls
           v
[@Repository - Data Access Layer]    <-- YOU ARE HERE
           |
           | JdbcTemplate + RowMapper
           v
[MySQL Database]
```

**Repository Layer Responsibilities:**
- Execute SQL queries using JdbcTemplate
- Convert ResultSet rows to domain objects using RowMapper
- Return `List<DomainObject>` or single objects to the service layer
- Handle database-specific concerns (connection, exceptions)

**Service Layer Responsibilities:**
- Contain business logic (calculations, validations)
- Coordinate between repositories
- Transaction management (all-or-nothing operations)

**Controller Responsibilities:**
- Handle user input (console) or HTTP requests (web)
- Call appropriate services
- Present results to users

### Why Layered Architecture Matters

**Separation of concerns:** If your database changes (MySQL to PostgreSQL), only the repository layer changes. Service and controller code remains untouched.

**Testability:** You can test service logic without a database by mocking the repository.

**Team collaboration:** Different team members can work on different layers.

**Exam relevance:** When asked about your project architecture, you should be able to explain this layered structure and why each layer exists.

---

## JdbcTemplate: Spring's Database Access Tool

### What Is JdbcTemplate?

JdbcTemplate is Spring's abstraction over raw JDBC. It handles:
- Opening and closing database connections
- Creating and managing PreparedStatements
- Iterating through ResultSets
- Translating SQL exceptions to Spring's exception hierarchy

**What you write:**
```java
String sql = "SELECT * FROM customers WHERE city = ?";
List<Customer> customers = jdbcTemplate.query(sql, customerRowMapper, "Copenhagen");
```

**What JdbcTemplate does for you:**
1. Gets a connection from the connection pool
2. Creates a PreparedStatement from your SQL
3. Sets the parameter ("Copenhagen")
4. Executes the query
5. Iterates through the ResultSet, calling your RowMapper for each row
6. Closes the ResultSet, Statement, and returns the connection to the pool
7. Returns your `List<Customer>`

Without JdbcTemplate, that's 30+ lines of boilerplate code with try-catch-finally blocks.

### The Three Essential Methods

JdbcTemplate provides many methods, but you'll use three constantly:

**1. `query()` - Returns multiple rows as a List**
```java
public List<Car> findAllAvailableCars() {
    String sql = "SELECT * FROM cars WHERE available = true";
    return jdbcTemplate.query(sql, carRowMapper);
}
```

**2. `queryForObject()` - Returns exactly one row**
```java
public Customer findById(int customerId) {
    String sql = "SELECT * FROM customers WHERE customer_id = ?";
    return jdbcTemplate.queryForObject(sql, customerRowMapper, customerId);
}
```

Note: `queryForObject()` throws an exception if zero rows or multiple rows are returned. Use it only when you expect exactly one result.

**3. `update()` - For INSERT, UPDATE, DELETE operations**
```java
public void saveCustomer(Customer customer) {
    String sql = "INSERT INTO customers (first_name, last_name, email) VALUES (?, ?, ?)";
    jdbcTemplate.update(sql, customer.getFirstName(), customer.getLastName(), customer.getEmail());
}

public void updateCustomerEmail(int customerId, String newEmail) {
    String sql = "UPDATE customers SET email = ? WHERE customer_id = ?";
    jdbcTemplate.update(sql, newEmail, customerId);
}

public void deleteCustomer(int customerId) {
    String sql = "DELETE FROM customers WHERE customer_id = ?";
    jdbcTemplate.update(sql, customerId);
}
```

### Choosing the Right Method

| You want to... | Use this method | Returns |
|----------------|-----------------|---------|
| Get multiple rows | `query(sql, rowMapper, params...)` | `List<T>` |
| Get exactly one row | `queryForObject(sql, rowMapper, params...)` | `T` |
| Get a single value (count, max, etc.) | `queryForObject(sql, Integer.class, params...)` | Wrapper type |
| INSERT, UPDATE, or DELETE | `update(sql, params...)` | `int` (rows affected) |

### Parameter Binding and SQL Injection Prevention

**Never concatenate user input into SQL strings:**
```java
// DANGEROUS - SQL injection vulnerability!
String sql = "SELECT * FROM customers WHERE name = '" + userInput + "'";
```

**Always use parameter placeholders:**
```java
// SAFE - parameters are escaped automatically
String sql = "SELECT * FROM customers WHERE name = ?";
jdbcTemplate.query(sql, customerRowMapper, userInput);
```

The `?` placeholders are replaced with properly escaped values, preventing SQL injection attacks.

---

## RowMapper: The Translator Pattern

### Understanding the Problem

A SQL query returns a ResultSet - essentially a cursor that moves through rows of raw data. Each column is accessible by name or index, but the data is strings, integers, dates - not objects.

Your Java code wants `Customer` objects with typed fields and methods.

RowMapper bridges this gap. It's a **translator** that converts one row of database data into one Java object.

### How RowMapper Works

```java
public class CustomerRowMapper implements RowMapper<Customer> {

    @Override
    public Customer mapRow(ResultSet rs, int rowNum) throws SQLException {
        Customer customer = new Customer();
        customer.setCustomerId(rs.getInt("customer_id"));
        customer.setFirstName(rs.getString("first_name"));
        customer.setLastName(rs.getString("last_name"));
        customer.setEmail(rs.getString("email"));
        customer.setPhone(rs.getString("phone"));
        return customer;
    }
}
```

**Key points:**
- `mapRow()` is called **once for each row** in the ResultSet
- `rs` provides access to the current row's column values
- `rowNum` is the row index (rarely used, but available)
- You return a fully constructed domain object

### The Mental Model: Assembly Line

Think of RowMapper as a worker on an assembly line:

```
ResultSet (conveyor belt of raw parts)
    [customer_id=1, first_name="Hans", last_name="Jensen", email="hans@example.com"]
    [customer_id=2, first_name="Maria", last_name="Nielsen", email="maria@example.com"]
    ...
           |
           v
RowMapper (assembly worker)
    - Takes one row of parts
    - Assembles them into a Customer object
    - Passes it along
           |
           v
List<Customer> (finished products)
    [Customer{id=1, name="Hans Jensen"}, Customer{id=2, name="Maria Nielsen"}, ...]
```

### ResultSet Extraction Methods

The ResultSet provides typed extraction methods. Use the one matching your database column type:

| Database Type | ResultSet Method | Java Type |
|---------------|-----------------|-----------|
| INT, INTEGER | `rs.getInt("column_name")` | `int` |
| VARCHAR, TEXT | `rs.getString("column_name")` | `String` |
| DATE | `rs.getDate("column_name")` | `java.sql.Date` |
| DATETIME, TIMESTAMP | `rs.getTimestamp("column_name")` | `java.sql.Timestamp` |
| DECIMAL, NUMERIC | `rs.getBigDecimal("column_name")` | `BigDecimal` |
| BOOLEAN, TINYINT(1) | `rs.getBoolean("column_name")` | `boolean` |
| DOUBLE | `rs.getDouble("column_name")` | `double` |

### Converting to Java 8+ Date Types

MySQL DATE columns come as `java.sql.Date`. For modern Java, convert to `LocalDate`:

```java
@Override
public RentalContract mapRow(ResultSet rs, int rowNum) throws SQLException {
    RentalContract contract = new RentalContract();
    contract.setContractId(rs.getInt("contract_id"));

    // Convert SQL Date to LocalDate
    java.sql.Date sqlStartDate = rs.getDate("start_date");
    if (sqlStartDate != null) {
        contract.setStartDate(sqlStartDate.toLocalDate());
    }

    java.sql.Date sqlEndDate = rs.getDate("end_date");
    if (sqlEndDate != null) {
        contract.setEndDate(sqlEndDate.toLocalDate());
    }

    return contract;
}
```

### Handling NULL Values

Database columns can be NULL, which requires careful handling in Java:

**For objects (String, Date, BigDecimal):** `getString()` returns `null` - usually fine.

**For primitives (int, double, boolean):** `getInt()` returns 0 for NULL, which may be misleading.

```java
// Check for NULL when it matters
int mileage = rs.getInt("mileage");
if (rs.wasNull()) {
    // The column was actually NULL, not zero
    contract.setMileage(null); // Assuming mileage is Integer, not int
}
```

**Better approach:** Use wrapper types (`Integer` instead of `int`) when NULL is meaningful.

### Lambda Syntax for Simple Mappings

For straightforward mappings, you can use lambda syntax instead of a separate class:

```java
public List<Customer> findAll() {
    String sql = "SELECT * FROM customers";
    return jdbcTemplate.query(sql, (rs, rowNum) -> {
        Customer c = new Customer();
        c.setCustomerId(rs.getInt("customer_id"));
        c.setFirstName(rs.getString("first_name"));
        c.setLastName(rs.getString("last_name"));
        return c;
    });
}
```

This is functionally identical to implementing RowMapper in a separate class. Use whichever style your team prefers.

---

## The Repository Pattern

### What: Data Access Layer Organization

A Repository class encapsulates all database operations for a specific domain entity. Following the **Information Expert** principle (GRASP), the repository is the expert on how to fetch, save, and delete that entity.

```java
@Repository
public class CustomerRepository {

    private final JdbcTemplate jdbcTemplate;

    public CustomerRepository(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    // All customer-related database operations go here
    public List<Customer> findAll() { ... }
    public Customer findById(int id) { ... }
    public void save(Customer customer) { ... }
    public void update(Customer customer) { ... }
    public void delete(int id) { ... }
}
```

### Why: Separation of Concerns

Without repositories, database code scatters throughout your application:

```java
// BAD: Database code in controller
public void displayCustomer(int id) {
    String sql = "SELECT * FROM customers WHERE id = ?";
    Customer c = jdbcTemplate.queryForObject(sql, customerMapper, id);
    System.out.println(c.getName());
}
```

**Problems:**
- Controller knows about SQL and JDBC
- Same query might be written multiple times
- Changing database logic requires changing multiple files
- Hard to test without a database

**With Repository:**
```java
// GOOD: Controller calls repository
public void displayCustomer(int id) {
    Customer c = customerRepository.findById(id);  // Clean!
    System.out.println(c.getName());
}
```

### The @Repository Annotation

In Spring applications, `@Repository` marks a class as a data access component:

```java
@Repository
public class CarRepository {
    // Spring will manage this class and provide JdbcTemplate
}
```

**What @Repository does:**
1. Marks the class for component scanning (Spring creates an instance)
2. Enables exception translation (converts JDBC exceptions to Spring's DataAccessException)
3. Documents the class's architectural role

### Complete Repository Example: CarRepository

```java
@Repository
public class CarRepository {

    private final JdbcTemplate jdbcTemplate;
    private final RowMapper<Car> carRowMapper;

    public CarRepository(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
        this.carRowMapper = (rs, rowNum) -> {
            Car car = new Car();
            car.setCarId(rs.getInt("car_id"));
            car.setLicensePlate(rs.getString("license_plate"));
            car.setBrand(rs.getString("brand"));
            car.setModel(rs.getString("model"));
            car.setCategory(rs.getString("category"));
            car.setPricePerDay(rs.getBigDecimal("price_per_day"));
            car.setAvailable(rs.getBoolean("available"));
            return car;
        };
    }

    public List<Car> findAll() {
        String sql = "SELECT * FROM cars ORDER BY brand, model";
        return jdbcTemplate.query(sql, carRowMapper);
    }

    public List<Car> findAvailableByCategory(String category) {
        String sql = "SELECT * FROM cars WHERE category = ? AND available = true";
        return jdbcTemplate.query(sql, carRowMapper, category);
    }

    public Car findById(int carId) {
        String sql = "SELECT * FROM cars WHERE car_id = ?";
        return jdbcTemplate.queryForObject(sql, carRowMapper, carId);
    }

    public void save(Car car) {
        String sql = "INSERT INTO cars (license_plate, brand, model, category, price_per_day, available) " +
                     "VALUES (?, ?, ?, ?, ?, ?)";
        jdbcTemplate.update(sql,
            car.getLicensePlate(),
            car.getBrand(),
            car.getModel(),
            car.getCategory(),
            car.getPricePerDay(),
            car.isAvailable());
    }

    public void updateAvailability(int carId, boolean available) {
        String sql = "UPDATE cars SET available = ? WHERE car_id = ?";
        jdbcTemplate.update(sql, available, carId);
    }

    public void delete(int carId) {
        String sql = "DELETE FROM cars WHERE car_id = ?";
        jdbcTemplate.update(sql, carId);
    }
}
```

### Naming Conventions

Standard repository method names communicate intent clearly:

| Method Name | Purpose | Returns |
|-------------|---------|---------|
| `findAll()` | Get all entities | `List<T>` |
| `findById(id)` | Get one by primary key | `T` |
| `findByXxx(value)` | Get all matching a condition | `List<T>` |
| `save(entity)` | Insert new entity | `void` |
| `update(entity)` | Update existing entity | `void` |
| `delete(id)` | Remove by primary key | `void` |
| `existsById(id)` | Check if exists | `boolean` |
| `count()` | Total count | `int` or `long` |

---

## Complete Data Flow: From Database to List

### Tracing a Query Through the System

Let's trace what happens when you call `carRepository.findAvailableByCategory("Luxury")`:

**Step 1: Repository receives the call**
```java
public List<Car> findAvailableByCategory(String category) {
    String sql = "SELECT * FROM cars WHERE category = ? AND available = true";
    return jdbcTemplate.query(sql, carRowMapper, category);
}
```

**Step 2: JdbcTemplate prepares the query**
- Gets database connection from pool
- Creates PreparedStatement: `SELECT * FROM cars WHERE category = ? AND available = true`
- Binds parameter: `category = "Luxury"`

**Step 3: Query executes against MySQL**
```
MySQL returns:
+--------+---------------+------------+---------+---------+---------------+-----------+
| car_id | license_plate | brand      | model   | category| price_per_day | available |
+--------+---------------+------------+---------+---------+---------------+-----------+
|      1 | AB 12345      | Mercedes   | S-Class | Luxury  |       1200.00 |         1 |
|      5 | CD 67890      | BMW        | 7-Series| Luxury  |       1100.00 |         1 |
+--------+---------------+------------+---------+---------+---------------+-----------+
```

**Step 4: JdbcTemplate iterates, calling RowMapper for each row**

For row 1:
```java
Car car = new Car();
car.setCarId(1);                          // rs.getInt("car_id")
car.setLicensePlate("AB 12345");          // rs.getString("license_plate")
car.setBrand("Mercedes");                  // rs.getString("brand")
car.setModel("S-Class");                   // rs.getString("model")
car.setCategory("Luxury");                 // rs.getString("category")
car.setPricePerDay(new BigDecimal("1200.00")); // rs.getBigDecimal("price_per_day")
car.setAvailable(true);                    // rs.getBoolean("available")
// Car object added to internal list
```

For row 2: Same process, creating second Car object

**Step 5: JdbcTemplate returns the List**
```java
List<Car> result = [Car{id=1, "Mercedes S-Class"}, Car{id=5, "BMW 7-Series"}]
```

**Step 6: Repository returns to caller**
Your service or controller now has a `List<Car>` ready to use.

### The Pattern in Pictures

```
findAvailableByCategory("Luxury")
            |
            v
   "SELECT * FROM cars WHERE category = ? AND available = true"
            |
            | JdbcTemplate executes
            v
   MySQL returns ResultSet (2 rows)
            |
            | For each row:
            v
   RowMapper creates Car object
            |
            v
   List<Car> with 2 Car objects
```

---

## Handling Relationships: Nested Objects

### The Challenge: JOIN Results to Nested Objects

Real applications have relationships. In Social Medium:
- A Profile has many Posts
- Your Java model: `Profile` contains `List<Post>`

The SQL query uses JOIN:
```sql
SELECT p.profile_id, p.username, p.bio,
       post.post_id, post.content, post.created_at
FROM profiles p
LEFT JOIN posts post ON p.profile_id = post.profile_id
ORDER BY p.profile_id, post.created_at DESC
```

This returns **one row per post**, with profile data repeated:
```
| profile_id | username | bio    | post_id | content      | created_at |
|------------|----------|--------|---------|--------------|------------|
|          1 | hans     | Hello  |     101 | First post!  | 2024-02-01 |
|          1 | hans     | Hello  |     102 | Second post  | 2024-02-02 |
|          2 | maria    | Hi all |     201 | Maria's post | 2024-02-01 |
```

Your goal: `List<Profile>` where each Profile contains its `List<Post>`.

### Approach 1: ResultSetExtractor for Complex Mapping

For nested objects, use `ResultSetExtractor` instead of `RowMapper`:

```java
public List<Profile> findAllWithPosts() {
    String sql = "SELECT p.profile_id, p.username, p.bio, " +
                 "post.post_id, post.content, post.created_at " +
                 "FROM profiles p " +
                 "LEFT JOIN posts post ON p.profile_id = post.profile_id " +
                 "ORDER BY p.profile_id, post.created_at DESC";

    return jdbcTemplate.query(sql, rs -> {
        Map<Integer, Profile> profileMap = new LinkedHashMap<>();

        while (rs.next()) {
            int profileId = rs.getInt("profile_id");

            // Get or create profile
            Profile profile = profileMap.computeIfAbsent(profileId, id -> {
                Profile p = new Profile();
                try {
                    p.setProfileId(id);
                    p.setUsername(rs.getString("username"));
                    p.setBio(rs.getString("bio"));
                    p.setPosts(new ArrayList<>());
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
                return p;
            });

            // Add post if exists (LEFT JOIN may have NULL post columns)
            if (rs.getObject("post_id") != null) {
                Post post = new Post();
                post.setPostId(rs.getInt("post_id"));
                post.setContent(rs.getString("content"));
                post.setCreatedAt(rs.getTimestamp("created_at").toLocalDateTime());
                profile.getPosts().add(post);
            }
        }

        return new ArrayList<>(profileMap.values());
    });
}
```

**Key insight:** The ResultSetExtractor processes the *entire* ResultSet at once, allowing you to build complex object graphs.

### Approach 2: Separate Queries (Simpler, N+1 Tradeoff)

Sometimes separate queries are clearer:

```java
public List<Profile> findAllWithPosts() {
    // Query 1: Get all profiles
    List<Profile> profiles = findAllProfiles();

    // Query 2: Get all posts, grouped by profile
    for (Profile profile : profiles) {
        List<Post> posts = postRepository.findByProfileId(profile.getProfileId());
        profile.setPosts(posts);
    }

    return profiles;
}
```

**Trade-off:** This makes N+1 queries (1 for profiles, N for posts). For small datasets, it's fine. For large datasets, the JOIN approach is more efficient.

### Kailua Example: RentalContract with Customer and Car

In Kailua, a RentalContract relates to both Customer and Car:

```java
public List<RentalContract> findAllWithDetails() {
    String sql = "SELECT rc.contract_id, rc.start_date, rc.end_date, rc.total_price, " +
                 "c.customer_id, c.first_name, c.last_name, " +
                 "car.car_id, car.brand, car.model " +
                 "FROM rental_contracts rc " +
                 "INNER JOIN customers c ON rc.customer_id = c.customer_id " +
                 "INNER JOIN cars car ON rc.car_id = car.car_id";

    return jdbcTemplate.query(sql, (rs, rowNum) -> {
        RentalContract contract = new RentalContract();
        contract.setContractId(rs.getInt("contract_id"));
        contract.setStartDate(rs.getDate("start_date").toLocalDate());
        contract.setEndDate(rs.getDate("end_date").toLocalDate());
        contract.setTotalPrice(rs.getBigDecimal("total_price"));

        // Create nested Customer
        Customer customer = new Customer();
        customer.setCustomerId(rs.getInt("customer_id"));
        customer.setFirstName(rs.getString("first_name"));
        customer.setLastName(rs.getString("last_name"));
        contract.setCustomer(customer);

        // Create nested Car
        Car car = new Car();
        car.setCarId(rs.getInt("car_id"));
        car.setBrand(rs.getString("brand"));
        car.setModel(rs.getString("model"));
        contract.setCar(car);

        return contract;
    });
}
```

---

## CRUD Operations Pattern

### The Complete CRUD Repository

Here's the full pattern for a typical entity, using Customer as an example:

```java
@Repository
public class CustomerRepository {

    private final JdbcTemplate jdbcTemplate;

    public CustomerRepository(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    // CREATE
    public void save(Customer customer) {
        String sql = "INSERT INTO customers (first_name, last_name, email, phone, license_number) " +
                     "VALUES (?, ?, ?, ?, ?)";
        jdbcTemplate.update(sql,
            customer.getFirstName(),
            customer.getLastName(),
            customer.getEmail(),
            customer.getPhone(),
            customer.getLicenseNumber());
    }

    // READ (all)
    public List<Customer> findAll() {
        String sql = "SELECT * FROM customers ORDER BY last_name, first_name";
        return jdbcTemplate.query(sql, this::mapRowToCustomer);
    }

    // READ (by ID)
    public Customer findById(int customerId) {
        String sql = "SELECT * FROM customers WHERE customer_id = ?";
        return jdbcTemplate.queryForObject(sql, this::mapRowToCustomer, customerId);
    }

    // UPDATE
    public void update(Customer customer) {
        String sql = "UPDATE customers SET first_name = ?, last_name = ?, email = ?, " +
                     "phone = ?, license_number = ? WHERE customer_id = ?";
        jdbcTemplate.update(sql,
            customer.getFirstName(),
            customer.getLastName(),
            customer.getEmail(),
            customer.getPhone(),
            customer.getLicenseNumber(),
            customer.getCustomerId());
    }

    // DELETE
    public void delete(int customerId) {
        String sql = "DELETE FROM customers WHERE customer_id = ?";
        jdbcTemplate.update(sql, customerId);
    }

    // Reusable RowMapper as method reference
    private Customer mapRowToCustomer(ResultSet rs, int rowNum) throws SQLException {
        Customer customer = new Customer();
        customer.setCustomerId(rs.getInt("customer_id"));
        customer.setFirstName(rs.getString("first_name"));
        customer.setLastName(rs.getString("last_name"));
        customer.setEmail(rs.getString("email"));
        customer.setPhone(rs.getString("phone"));
        customer.setLicenseNumber(rs.getString("license_number"));
        return customer;
    }
}
```

### Getting the Generated ID After Insert

When inserting a new row, you often need the auto-generated primary key:

```java
public int saveAndReturnId(Customer customer) {
    String sql = "INSERT INTO customers (first_name, last_name, email) VALUES (?, ?, ?)";

    KeyHolder keyHolder = new GeneratedKeyHolder();

    jdbcTemplate.update(connection -> {
        PreparedStatement ps = connection.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
        ps.setString(1, customer.getFirstName());
        ps.setString(2, customer.getLastName());
        ps.setString(3, customer.getEmail());
        return ps;
    }, keyHolder);

    return keyHolder.getKey().intValue();
}
```

This is more complex than a simple insert but necessary when you need the generated ID immediately.

---

## Common Struggles and Solutions

### Struggle 1: RowMapper Execution Timing

**Confusion:** "When does mapRow() actually run?"

**Understanding:** mapRow() is called by JdbcTemplate **once for each row** in the ResultSet. If your query returns 50 rows, mapRow() executes 50 times.

**Visual model:**
```
ResultSet cursor: [Row 1] [Row 2] [Row 3] ... [Row 50]
                     |       |       |           |
                  mapRow  mapRow  mapRow     mapRow
                     |       |       |           |
                  Object  Object  Object     Object
                     \       |       /           /
                      \      |      /           /
                       List<Customer> with 50 objects
```

### Struggle 2: Column Name Mismatches

**Symptom:** "My object fields are all null/zero"

**Cause:** Column names in SQL don't match what you pass to `rs.getString()`.

**Debug approach:**
```java
// Print column names to verify
ResultSetMetaData meta = rs.getMetaData();
for (int i = 1; i <= meta.getColumnCount(); i++) {
    System.out.println("Column " + i + ": " + meta.getColumnName(i));
}
```

**Prevention:** Use explicit column names in SELECT, not `SELECT *`, and verify they match your getString/getInt calls.

### Struggle 3: queryForObject() Exceptions

**Symptom:** "EmptyResultDataAccessException when finding by ID"

**Understanding:** `queryForObject()` expects exactly one result. Zero or multiple results throw exceptions.

**Solution 1:** Handle the exception
```java
public Customer findById(int id) {
    try {
        return jdbcTemplate.queryForObject(sql, mapper, id);
    } catch (EmptyResultDataAccessException e) {
        return null; // or throw a custom exception
    }
}
```

**Solution 2:** Use query() and handle the list
```java
public Customer findById(int id) {
    List<Customer> results = jdbcTemplate.query(sql, mapper, id);
    return results.isEmpty() ? null : results.get(0);
}
```

### Struggle 4: NULL Values in Primitives

**Symptom:** Database has NULL, but `rs.getInt()` returns 0.

**Understanding:** JDBC returns 0 for NULL integers. Use `rs.wasNull()` to check.

**Better design:** Use wrapper types (`Integer` instead of `int`) when NULL is a valid business value.

```java
// If mileage can be NULL
Integer mileage = rs.getObject("mileage", Integer.class);
car.setMileage(mileage); // Will be null if database value is NULL
```

### Struggle 5: Method Selection Confusion

**Question:** "query() or queryForObject()?"

**Decision framework:**

| Scenario | Method |
|----------|--------|
| Could return 0, 1, or many rows | `query()` returns `List<T>` |
| Always exactly 1 row (by unique key) | `queryForObject()` returns `T` |
| Need a single aggregate value | `queryForObject(sql, Integer.class)` |
| INSERT, UPDATE, DELETE | `update()` returns `int` |

When in doubt, use `query()` and handle the list - it's more flexible.

---

## Integration Patterns

### Pattern: View Simplifies Repository

**From SQL Advanced:** You created views to simplify complex queries. Use them:

```java
// Instead of complex JOIN SQL in Java
public List<ActiveRental> findAllActiveRentals() {
    String sql = "SELECT * FROM active_rentals";  // View handles the complexity
    return jdbcTemplate.query(sql, activeRentalRowMapper);
}
```

**Benefits:**
- Repository code stays clean
- Complex SQL logic lives in one place (the view)
- Schema changes update the view, not Java code

### Pattern: Stored Procedure Call

**From SQL Advanced:** You created stored procedures for complex operations:

```java
public void processCarReturn(int contractId, int finalMileage) {
    String sql = "CALL process_car_return(?, ?)";
    jdbcTemplate.update(sql, contractId, finalMileage);
}
```

The procedure handles multiple operations atomically (update contract, mark car available, calculate final price).

### Pattern: Collections as the Universal Container

**From ADT & Collections:** `List<DomainObject>` is your standard return type:

```java
// Same pattern everywhere:
List<Car> cars = carRepository.findAll();
List<Customer> customers = customerRepository.findByCity("Copenhagen");
List<RentalContract> contracts = contractRepository.findActive();
```

This consistency makes code predictable. Callers always know what to expect.

---

## Kailua Project Application

### Required Repositories

Based on the Kailua requirements, you'll need:

1. **CarRepository** - CRUD for cars, filtered queries by category/availability
2. **CustomerRepository** - CRUD for customers
3. **RentalContractRepository** - CRUD for contracts, with joins for full details

### Sample Kailua Repository Structure

```
kailua/
├── domain/
│   ├── Car.java
│   ├── Customer.java
│   └── RentalContract.java
├── repository/
│   ├── CarRepository.java
│   ├── CustomerRepository.java
│   └── RentalContractRepository.java
├── service/
│   └── RentalService.java
└── KailuaApplication.java
```

### Sample Queries for Kailua

```java
// Cars
"SELECT * FROM cars WHERE category = ? AND available = true"
"UPDATE cars SET available = ? WHERE car_id = ?"

// Customers
"SELECT * FROM customers WHERE customer_id = ?"
"INSERT INTO customers (first_name, last_name, email, phone, license_number) VALUES (?, ?, ?, ?, ?)"

// Contracts
"SELECT rc.*, c.first_name, c.last_name, car.brand, car.model " +
"FROM rental_contracts rc " +
"JOIN customers c ON rc.customer_id = c.customer_id " +
"JOIN cars car ON rc.car_id = car.car_id " +
"WHERE rc.status = 'active'"

"INSERT INTO rental_contracts (customer_id, car_id, start_date, end_date, total_price, status) " +
"VALUES (?, ?, ?, ?, ?, 'active')"
```

---

## Preparing for the Oral Exam

### Key Questions You Should Answer Confidently

1. **"What is RowMapper and when is mapRow() called?"**

   "RowMapper is an interface that converts one database row to one Java object. The mapRow method is called once for each row in the ResultSet. JdbcTemplate iterates through the results and calls my implementation to create each object."

2. **"Explain the difference between query() and queryForObject()."**

   "query() returns a List and handles zero, one, or many results. queryForObject() expects exactly one result and throws an exception otherwise. I use queryForObject() for lookups by unique key, and query() for everything else."

3. **"Why use the Repository pattern?"**

   "The repository encapsulates all database operations for an entity. It follows the Information Expert principle - the class with database connection knowledge handles database access. This separates data access from business logic, making code more testable and maintainable."

4. **"Trace the data flow from database to Java List."**

   "JdbcTemplate executes the SQL query and receives a ResultSet. It iterates through each row, calling my RowMapper to convert the row data to a domain object. These objects are collected into a List, which the repository returns to the service layer."

5. **"How do you handle NULL database values?"**

   "For reference types like String, rs.getString() returns null automatically. For primitives, I either use rs.wasNull() to check, or I use wrapper types (Integer instead of int) when NULL is a meaningful business value."

### Demo Tips

When demonstrating database integration:

1. **Show the complete flow:** "This repository method queries the database... the RowMapper converts each row... and we get back this List of Car objects."

2. **Explain architectural choices:** "We put this in the repository because it's database-specific logic. The service layer above doesn't know or care that we're using MySQL and JdbcTemplate."

3. **Connect to GRASP:** "The repository is the Information Expert for database operations. It has the JdbcTemplate, it knows the SQL, it knows how to map results to objects."

4. **Highlight Collections integration:** "Notice we're returning List<Car> - the same Collection type from Phase 1. Everything flows through these standard collection types."

---

## Key Takeaways

- **JdbcTemplate simplifies database access** by handling connections, exceptions, and resource cleanup. You focus on SQL and mapping.

- **RowMapper is a translator** - it converts one database row to one Java object. mapRow() is called once per row.

- **The Repository pattern implements Information Expert** - database operations live in classes designed for that purpose.

- **Use query() for multiple results, queryForObject() for exactly one, update() for modifications.**

- **Collections unify everything** - database results become `List<DomainObject>`, the same pattern from Phase 1.

- **The data flow is predictable:** Query -> ResultSet -> RowMapper -> List<T> -> Your code.

- **This pattern applies everywhere:** Console apps (Kailua), web apps (Onskeskyen), exam project, professional work.

---

## For the Next Topic Agent

### Terminology Established This Topic

- **JdbcTemplate:** Spring's database access abstraction. Executes SQL, manages connections, handles exceptions. Three key methods: `query()` (returns List), `queryForObject()` (returns single object), `update()` (for DML operations returning int rows affected).

- **RowMapper<T>:** Functional interface for converting one ResultSet row to one Java object. Method signature: `T mapRow(ResultSet rs, int rowNum) throws SQLException`. Called once per row by JdbcTemplate.

- **Repository Pattern:** Data access layer class encapsulating all database operations for a domain entity. Annotated with `@Repository` in Spring. Implements Information Expert (GRASP).

- **ResultSet:** JDBC cursor for iterating query results. Key methods: `getString(columnName)`, `getInt(columnName)`, `getDate(columnName)`, `getBigDecimal(columnName)`, `wasNull()`.

- **Data Flow Pattern:** Database -> SQL Query -> JdbcTemplate -> ResultSet -> RowMapper -> List<DomainObject> -> Service/Controller.

- **Parameter Binding:** Using `?` placeholders in SQL with parameter values passed to JdbcTemplate methods. Prevents SQL injection.

- **Layered Architecture:** Controller -> Service -> Repository -> Database. Each layer has distinct responsibilities. Changes to one layer don't affect others.

### Example Classes/Code Created

- **CustomerRepository:** Complete CRUD implementation with `findAll()`, `findById()`, `save()`, `update()`, `delete()` methods.

- **CarRepository:** Domain-specific queries like `findAvailableByCategory(String category)`.

- **RowMapper as lambda:** `(rs, rowNum) -> { Car car = new Car(); car.setCarId(rs.getInt("car_id")); ... return car; }`

- **Nested object mapping:** RentalContract with embedded Customer and Car objects from JOIN query.

- **Date conversion:** `rs.getDate("column").toLocalDate()` for SQL Date to Java 8 LocalDate.

### Student Capabilities After This Topic

Students who complete this material can now:
- Create repository classes with full CRUD operations
- Implement RowMapper to convert any ResultSet to domain objects
- Choose appropriate JdbcTemplate methods (query, queryForObject, update)
- Handle NULL values and type conversions correctly
- Map JOIN results to nested object structures
- Explain the complete data flow from database to Java List
- Connect repository pattern to Information Expert (GRASP)
- Design layered application architecture (Controller -> Service -> Repository)
- Apply these patterns to Kailua Car Rental project

### Pedagogical Patterns Used

- **Assembly Line Metaphor:** RowMapper as a worker converting raw parts (ResultSet data) into finished products (domain objects) on a conveyor belt.

- **Data Flow Tracing:** Step-by-step walkthrough of what happens when a repository method is called, from SQL execution through object creation.

- **Method Selection Table:** Clear decision framework for query() vs queryForObject() vs update() based on expected results.

- **Pattern Connection:** Explicit links to Collections (Phase 1), SQL (Phases 2-3), and GRASP (Information Expert, Layered Architecture).

- **Console-to-Web Continuity:** Emphasizing that Kailua (console) uses identical patterns to Onskeskyen (web) and exam project.

- **Common Struggles Section:** Anticipating confusion points (mapRow timing, NULL handling, method selection) with targeted solutions.

- **Exam Question Anticipation:** Sample questions with model answers showing depth of understanding expected.

### Integration Notes for Next Topic (Spring Boot Fundamentals)

The next topic builds directly on this foundation:

1. **Repository stays the same:** The CarRepository from Kailua works identically in Spring Boot web applications.

2. **Data flow extends:** Database -> Repository -> Service -> Controller -> Thymeleaf template.

3. **@Repository becomes automatic:** Spring Boot's component scanning finds and instantiates repositories.

4. **JdbcTemplate is auto-configured:** application.properties defines datasource; JdbcTemplate is available for injection.

5. **Collections to templates:** `List<Car>` from repository goes to `Model`, then `th:each="car : ${cars}"` in Thymeleaf.

The critical insight: students aren't learning new database patterns in Spring Boot - they're learning how to expose their existing repository layer through web controllers.
