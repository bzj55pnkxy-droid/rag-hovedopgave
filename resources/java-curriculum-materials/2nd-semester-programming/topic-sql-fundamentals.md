# SQL Fundamentals - 2nd Semester Programming

*Prerequisites: Basic understanding of data modeling, logical operators from Java programming*
*Phase: 2 - Database Fundamentals*
*Exam Weight: High (foundational for all database work)*

---

## What You'll Learn

By the end of this topic, you will be able to:
- **Write SQL queries** to retrieve data from single tables using SELECT statements
- **Combine data from related tables** using various JOIN types (INNER, LEFT, RIGHT, FULL OUTER)
- **Perform CRUD operations** using INSERT, UPDATE, and DELETE statements
- **Calculate summary data** using aggregate functions (COUNT, SUM, AVG, MIN, MAX)
- **Group and filter data** using GROUP BY and HAVING clauses
- **Sort query results** using ORDER BY clause
- **Understand the relationship** between SQL operations and application requirements

These SQL skills are the foundation for ALL database work this semester. Every database operation in your Kailua Car Rental project and Onskeskyen Wishlist application will use the queries you learn here. Later, these exact queries will be executed from your Java code using JdbcTemplate.

---

## Why This Matters

### SQL Is Your Communication Language with Data

Up to this point, your Java programs have stored data in memory - in ArrayLists, HashMaps, and other collections. But memory is volatile. When your program stops, the data disappears.

Databases solve this problem by persisting data to disk. But databases don't speak Java. They speak SQL - Structured Query Language. SQL is how you:
- Ask the database questions ("What cars are available?")
- Tell the database to remember things ("Add this new customer")
- Update existing information ("Change this customer's phone number")
- Remove data you no longer need ("Delete this cancelled contract")

### SQL Is Declarative, Not Imperative

This is a fundamental shift in thinking. In Java, you tell the computer *how* to accomplish something:

```java
// Java: IMPERATIVE - you specify the steps
List<Car> luxuryCars = new ArrayList<>();
for (Car car : allCars) {
    if (car.getCategory().equals("Luxury")) {
        luxuryCars.add(car);
    }
}
```

In SQL, you describe *what* you want, and the database figures out how to get it:

```sql
-- SQL: DECLARATIVE - you specify the desired result
SELECT * FROM cars WHERE category = 'Luxury';
```

This declarative approach is powerful. The database engine can optimize execution based on indexes, table statistics, and query patterns - optimizations that would take you weeks to implement manually.

### Foundation for Everything Ahead

SQL Fundamentals is a prerequisite for:
- **SQL Advanced (Phase 3)**: Subqueries, views, stored procedures build on these fundamentals
- **Database-Java Integration (Phase 3-4)**: These queries will be executed from Java using JdbcTemplate
- **Spring Boot Web Applications (Phase 5)**: Data displayed in your web pages comes from SQL queries

Every feature in your projects - viewing car inventory, creating wishlists, generating rental reports - depends on the SQL skills you learn now.

---

## Building on What You Know

### From 1st Semester

**Logical Operators Transfer Directly:**
You already know AND, OR, NOT from Java conditionals:

```java
// Java
if (car.getPrice() > 400 && car.getCategory().equals("Luxury")) { }
```

```sql
-- SQL uses the same logic
SELECT * FROM cars WHERE price > 400 AND category = 'Luxury';
```

**Comparison Operators Are Identical:**
`=`, `<`, `>`, `<=`, `>=`, `<>` (or `!=`) work exactly as you expect from Java.

**Collections Provide Mental Models:**
When you query a database, think of results as a `List<DomainObject>`. A SELECT query is conceptually similar to filtering an ArrayList - you're asking "which elements meet these criteria?"

```java
// In Java, you might filter like this:
List<Car> filtered = cars.stream()
    .filter(c -> c.getPrice() > 400)
    .collect(Collectors.toList());
```

```sql
-- SQL achieves the same result declaratively
SELECT * FROM cars WHERE price > 400;
```

### From Earlier This Semester

**Collections Are the Bridge:**
In the ADT & Collections topic, you saw this data flow:

```
[Database] --> [Java Collections] --> [Web Template] --> [Browser]
```

SQL operates at the first step - extracting data from the database. The results become Collections in your Java code:

```java
List<Car> cars = jdbcTemplate.query("SELECT * FROM cars", rowMapper);
```

**HTML Forms Will Send Data to SQL:**
In HTML Fundamentals, you learned about form submissions. When a user fills out a "New Customer" form and clicks Submit:
1. HTML form sends data to your Spring Boot controller
2. Controller calls a service method
3. Service calls repository
4. Repository executes an INSERT query to add the customer to the database

The `name` attributes from your HTML forms become column values in your INSERT statements.

---

## SELECT Queries: Retrieving Data

### What: The Foundation of SQL

SELECT is the most common SQL operation - you'll write SELECT queries constantly. It retrieves data from one or more tables based on criteria you specify.

The basic syntax:

```sql
SELECT columns
FROM table
WHERE conditions
ORDER BY column;
```

### Why: Declarative Data Retrieval

Instead of writing loops to search through data, you describe what you want. The database engine:
- Decides the fastest way to find that data
- Uses indexes to speed up searches
- Returns exactly what you asked for

### How: Building SELECT Queries Step by Step

**Step 1: Select All Columns**
```sql
SELECT * FROM customers;
```
Returns every column and every row from the customers table. The `*` means "all columns."

**Step 2: Select Specific Columns (Projection)**
```sql
SELECT first_name, last_name, email FROM customers;
```
Returns only the columns you need. This is more efficient - especially over a network connection.

**Step 3: Filter Rows (WHERE Clause)**
```sql
SELECT first_name, last_name, email
FROM customers
WHERE city = 'Copenhagen';
```
Returns only rows where the condition is true.

**Step 4: Combine Conditions**
```sql
SELECT * FROM cars
WHERE category = 'Luxury' AND price_per_day <= 1000;
```
Multiple conditions combined with AND/OR. Use parentheses to control precedence:

```sql
SELECT * FROM cars
WHERE category = 'Luxury' AND (price_per_day <= 1000 OR available = true);
```

### Comparison Operators in WHERE

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` | Equal to | `category = 'Luxury'` |
| `<>` or `!=` | Not equal to | `status <> 'cancelled'` |
| `<` | Less than | `price < 500` |
| `>` | Greater than | `mileage > 50000` |
| `<=` | Less than or equal | `price <= 800` |
| `>=` | Greater than or equal | `year >= 2020` |
| `BETWEEN` | Within range (inclusive) | `price BETWEEN 400 AND 800` |
| `IN` | Matches any in list | `category IN ('Luxury', 'Sport')` |
| `LIKE` | Pattern matching | `name LIKE 'Anders%'` |
| `IS NULL` | Is null value | `phone IS NULL` |
| `IS NOT NULL` | Is not null | `email IS NOT NULL` |

### Pattern Matching with LIKE

The `%` wildcard matches any sequence of characters:
```sql
-- Names starting with 'A'
SELECT * FROM customers WHERE first_name LIKE 'A%';

-- Names ending with 'sen'
SELECT * FROM customers WHERE last_name LIKE '%sen';

-- Names containing 'berg'
SELECT * FROM customers WHERE last_name LIKE '%berg%';
```

The `_` wildcard matches exactly one character:
```sql
-- License plates like 'AB12345' (2 letters, 5 digits)
SELECT * FROM cars WHERE license_plate LIKE '__[0-9][0-9][0-9][0-9][0-9]';
```

### Action: Apply to Kailua Project

In your Kailua Car Rental system, you'll write queries like:

```sql
-- Find all available luxury cars
SELECT * FROM cars
WHERE category = 'Luxury' AND available = true;

-- Find customers from specific cities
SELECT first_name, last_name, phone
FROM customers
WHERE city IN ('Copenhagen', 'Frederiksberg', 'Gentofte');

-- Find cars needing service soon
SELECT license_plate, brand, model, mileage
FROM cars
WHERE mileage > 45000;
```

### Common Mistakes

**Mistake: Using single equals for null comparison**
```sql
-- WRONG: This won't work!
SELECT * FROM customers WHERE phone = NULL;

-- CORRECT: Use IS NULL
SELECT * FROM customers WHERE phone IS NULL;
```

**Mistake: Forgetting quotes around strings**
```sql
-- WRONG: SQL thinks Luxury is a column name
SELECT * FROM cars WHERE category = Luxury;

-- CORRECT: String values need quotes
SELECT * FROM cars WHERE category = 'Luxury';
```

**Mistake: Case sensitivity issues**
In MySQL, string comparisons are case-insensitive by default, but don't rely on this. Be consistent with your data.

---

## JOIN Operations: Combining Related Tables

### What: Bringing Tables Together

Real databases split data across multiple tables to avoid duplication. A `rental_contracts` table might store `customer_id` instead of repeating customer name, email, and phone for every rental.

JOINs combine these related tables back together when you need the complete picture.

### Why: The Power of Relational Databases

Consider the Kailua database structure:

```
customers table:
| customer_id | first_name | last_name | email |

cars table:
| car_id | license_plate | brand | model | category |

rental_contracts table:
| contract_id | customer_id | car_id | start_date | end_date |
```

The `rental_contracts` table references customers and cars by their IDs. To see "which customer rented which car," you need to JOIN these tables.

### How: Understanding JOIN Types

**Visualizing JOINs:**
Think of two tables as two circles that may overlap (like a Venn diagram):

```
   TableA       TableB
    ____         ____
   /    \       /    \
  |  A   |-----|  B   |
   \____/   |   \____/
           AB
           (matching rows)
```

**INNER JOIN**: Returns only rows where there's a match in BOTH tables (the intersection)

**LEFT JOIN**: Returns all rows from the left table, plus matching rows from the right (or NULL if no match)

**RIGHT JOIN**: Returns all rows from the right table, plus matching rows from the left (or NULL if no match)

**FULL OUTER JOIN**: Returns all rows from both tables, with NULLs where there's no match

### INNER JOIN: The Most Common

Returns only rows where the join condition is satisfied in both tables.

```sql
-- Get rental contracts with customer names
SELECT
    c.first_name,
    c.last_name,
    rc.start_date,
    rc.end_date
FROM rental_contracts rc
INNER JOIN customers c ON rc.customer_id = c.customer_id;
```

**Reading this query:**
1. Start with `rental_contracts` (aliased as `rc`)
2. For each rental contract, find the matching customer (where IDs match)
3. Return the combined data

**Result:** Only contracts that have a valid customer will appear. If a contract had an invalid `customer_id`, it would be excluded.

### LEFT JOIN: Include All From Left Table

Returns all rows from the left table, even if there's no match in the right table.

```sql
-- Get all customers and their rental history (including customers who never rented)
SELECT
    c.first_name,
    c.last_name,
    rc.contract_id,
    rc.start_date
FROM customers c
LEFT JOIN rental_contracts rc ON c.customer_id = rc.customer_id;
```

**Result:** Every customer appears at least once. Customers with no rentals have NULL for the contract columns.

**Use case:** Finding customers who have never rented (those with NULL contract_id):
```sql
SELECT c.first_name, c.last_name, c.email
FROM customers c
LEFT JOIN rental_contracts rc ON c.customer_id = rc.customer_id
WHERE rc.contract_id IS NULL;
```

### RIGHT JOIN: Include All From Right Table

The mirror of LEFT JOIN - returns all rows from the right table.

```sql
-- Get all rental contracts, even if customer data is missing
SELECT
    c.first_name,
    c.last_name,
    rc.contract_id
FROM customers c
RIGHT JOIN rental_contracts rc ON c.customer_id = rc.customer_id;
```

In practice, you can always rewrite a RIGHT JOIN as a LEFT JOIN by switching the table order. Most developers prefer LEFT JOIN for consistency.

### FULL OUTER JOIN: Include Everything

Returns all rows from both tables, matching where possible.

```sql
-- Note: MySQL doesn't support FULL OUTER JOIN directly
-- You'd use UNION of LEFT and RIGHT JOINs
SELECT c.first_name, c.last_name, rc.contract_id
FROM customers c
LEFT JOIN rental_contracts rc ON c.customer_id = rc.customer_id
UNION
SELECT c.first_name, c.last_name, rc.contract_id
FROM customers c
RIGHT JOIN rental_contracts rc ON c.customer_id = rc.customer_id;
```

### Multi-Table JOINs

Real queries often join multiple tables:

```sql
-- Get complete rental information: customer name, car details, dates
SELECT
    c.first_name,
    c.last_name,
    car.brand,
    car.model,
    car.license_plate,
    rc.start_date,
    rc.end_date
FROM rental_contracts rc
INNER JOIN customers c ON rc.customer_id = c.customer_id
INNER JOIN cars car ON rc.car_id = car.car_id
WHERE rc.start_date >= '2024-01-01';
```

**Reading multi-table JOINs:**
1. Start with the "central" table (often the one with foreign keys)
2. JOIN each related table one at a time
3. Each JOIN adds more columns to your result

### Table Aliases: Writing Readable JOINs

Aliases shorten table names and make queries cleaner:

```sql
-- Without aliases (verbose)
SELECT customers.first_name, rental_contracts.start_date
FROM customers
INNER JOIN rental_contracts ON customers.customer_id = rental_contracts.customer_id;

-- With aliases (cleaner)
SELECT c.first_name, rc.start_date
FROM customers c
INNER JOIN rental_contracts rc ON c.customer_id = rc.customer_id;
```

Use meaningful aliases: `c` for customers, `rc` for rental_contracts, `car` for cars.

### Action: Kailua JOIN Scenarios

```sql
-- List all active rentals with customer and car information
SELECT
    c.first_name || ' ' || c.last_name AS customer_name,
    car.brand || ' ' || car.model AS vehicle,
    car.license_plate,
    rc.start_date,
    rc.end_date
FROM rental_contracts rc
INNER JOIN customers c ON rc.customer_id = c.customer_id
INNER JOIN cars car ON rc.car_id = car.car_id
WHERE rc.end_date >= CURRENT_DATE;

-- Find cars that have never been rented
SELECT car.license_plate, car.brand, car.model
FROM cars car
LEFT JOIN rental_contracts rc ON car.car_id = rc.car_id
WHERE rc.contract_id IS NULL;
```

### Common Mistakes

**Mistake: Forgetting the ON clause**
```sql
-- WRONG: This creates a Cartesian product (every row paired with every other row!)
SELECT * FROM customers, rental_contracts;

-- CORRECT: Always specify the join condition
SELECT * FROM customers c
INNER JOIN rental_contracts rc ON c.customer_id = rc.customer_id;
```

**Mistake: Ambiguous column names**
```sql
-- WRONG: Both tables have 'customer_id'
SELECT customer_id, first_name FROM customers
INNER JOIN rental_contracts ON customers.customer_id = rental_contracts.customer_id;

-- CORRECT: Prefix with table alias
SELECT c.customer_id, c.first_name FROM customers c
INNER JOIN rental_contracts rc ON c.customer_id = rc.customer_id;
```

**Mistake: Using wrong JOIN type**
If you need "all customers including those without rentals," INNER JOIN will exclude them. Think carefully about what data you need to see.

---

## DML Operations: INSERT, UPDATE, DELETE

### What: Modifying Database Data

DML (Data Manipulation Language) operations change the data stored in tables:
- **INSERT**: Add new rows
- **UPDATE**: Modify existing rows
- **DELETE**: Remove rows

### Why: CRUD Operations in Applications

Every application needs to Create, Read, Update, and Delete data. When a user:
- Fills out a registration form -> INSERT
- Views their profile -> SELECT
- Changes their email address -> UPDATE
- Deletes their account -> DELETE

Your Java application will execute these SQL statements through JdbcTemplate.

### INSERT: Adding New Data

**Single Row Insert:**
```sql
INSERT INTO customers (first_name, last_name, email, phone, city)
VALUES ('Anders', 'Jensen', 'anders@example.com', '12345678', 'Copenhagen');
```

**Column order matters:** The VALUES must match the column order specified.

**Letting the Database Generate IDs:**
If your table has an auto-increment primary key:
```sql
-- customer_id is auto-generated
INSERT INTO customers (first_name, last_name, email)
VALUES ('Maria', 'Nielsen', 'maria@example.com');
```

**Multiple Rows at Once:**
```sql
INSERT INTO customers (first_name, last_name, email) VALUES
    ('Anders', 'Jensen', 'anders@example.com'),
    ('Maria', 'Nielsen', 'maria@example.com'),
    ('Peter', 'Hansen', 'peter@example.com');
```

### UPDATE: Modifying Existing Data

**Basic UPDATE:**
```sql
UPDATE customers
SET phone = '87654321'
WHERE customer_id = 5;
```

**CRITICAL:** Always include a WHERE clause! Without it, you update EVERY row:
```sql
-- DANGEROUS: Updates ALL customers!
UPDATE customers SET phone = '00000000';
```

**Updating Multiple Columns:**
```sql
UPDATE customers
SET phone = '87654321',
    email = 'new_email@example.com',
    city = 'Aarhus'
WHERE customer_id = 5;
```

**Conditional Updates:**
```sql
-- Update price for all luxury cars
UPDATE cars
SET price_per_day = price_per_day * 1.10  -- 10% increase
WHERE category = 'Luxury';
```

### DELETE: Removing Data

**Basic DELETE:**
```sql
DELETE FROM rental_contracts
WHERE contract_id = 123;
```

**CRITICAL:** Always include a WHERE clause! Without it, you delete EVERY row:
```sql
-- EXTREMELY DANGEROUS: Deletes ALL contracts!
DELETE FROM rental_contracts;
```

**Conditional Deletes:**
```sql
-- Delete old contracts (more than 5 years old)
DELETE FROM rental_contracts
WHERE end_date < DATE_SUB(CURRENT_DATE, INTERVAL 5 YEAR);
```

### Action: Safe DML Practices

**Always write WHERE first when writing UPDATE/DELETE:**
```sql
-- Step 1: Write the WHERE clause
WHERE customer_id = 5

-- Step 2: Add the operation
DELETE FROM customers
WHERE customer_id = 5
```

**Test with SELECT first:**
```sql
-- Before deleting, see what would be deleted
SELECT * FROM rental_contracts
WHERE end_date < '2020-01-01';

-- If the result looks correct, then delete
DELETE FROM rental_contracts
WHERE end_date < '2020-01-01';
```

### Common Mistakes

**Mistake: Forgetting WHERE clause**
The most dangerous SQL mistake. A WHERE-less UPDATE or DELETE affects ALL rows.

**Mistake: Wrong column in WHERE clause**
```sql
-- WRONG: 'email' is not unique, might update multiple customers!
UPDATE customers SET phone = '12345678' WHERE email = 'common@example.com';

-- SAFER: Use the primary key
UPDATE customers SET phone = '12345678' WHERE customer_id = 5;
```

**Mistake: Foreign key violations**
You can't delete a customer who has rental contracts (if foreign keys are enforced). Delete the contracts first, or use cascading deletes.

---

## Aggregate Functions: Summarizing Data

### What: Calculations Across Multiple Rows

Aggregate functions perform calculations on a set of rows and return a single value:
- **COUNT**: Number of rows
- **SUM**: Total of numeric values
- **AVG**: Average of numeric values
- **MIN**: Smallest value
- **MAX**: Largest value

### Why: Business Intelligence and Reporting

Real applications need summaries, not just raw data:
- "How many cars do we have?" (COUNT)
- "What's our total revenue this month?" (SUM)
- "What's the average rental duration?" (AVG)
- "What's the cheapest car available?" (MIN)
- "When was the most recent rental?" (MAX)

These queries power dashboards, reports, and business decisions.

### How: Using Aggregate Functions

**COUNT: Counting Rows**
```sql
-- Total number of customers
SELECT COUNT(*) FROM customers;

-- Number of customers in Copenhagen
SELECT COUNT(*) FROM customers WHERE city = 'Copenhagen';

-- Number of customers with phone numbers
SELECT COUNT(phone) FROM customers;  -- Excludes NULLs
```

**Important distinction:**
- `COUNT(*)` counts all rows
- `COUNT(column)` counts non-NULL values in that column

**SUM: Adding Values**
```sql
-- Total mileage across all cars
SELECT SUM(mileage) FROM cars;

-- Total revenue from luxury car rentals
SELECT SUM(total_price) FROM rental_contracts rc
INNER JOIN cars c ON rc.car_id = c.car_id
WHERE c.category = 'Luxury';
```

**AVG: Computing Averages**
```sql
-- Average price per day across all cars
SELECT AVG(price_per_day) FROM cars;

-- Average rental duration (in days)
SELECT AVG(DATEDIFF(end_date, start_date)) FROM rental_contracts;
```

**MIN and MAX: Finding Extremes**
```sql
-- Cheapest and most expensive cars
SELECT MIN(price_per_day), MAX(price_per_day) FROM cars;

-- Oldest and newest rental dates
SELECT MIN(start_date), MAX(end_date) FROM rental_contracts;
```

### Column Aliases: Naming Your Results

Aggregate results don't have meaningful column names by default. Use AS to name them:

```sql
SELECT
    COUNT(*) AS total_customers,
    COUNT(phone) AS customers_with_phone,
    COUNT(*) - COUNT(phone) AS customers_without_phone
FROM customers;
```

### Combining Aggregates with WHERE

The WHERE clause filters rows BEFORE aggregation:

```sql
-- Average price of luxury cars only
SELECT AVG(price_per_day) AS avg_luxury_price
FROM cars
WHERE category = 'Luxury';

-- Count rentals from 2024
SELECT COUNT(*) AS rentals_2024
FROM rental_contracts
WHERE start_date >= '2024-01-01';
```

### Action: Kailua Reporting Queries

```sql
-- Fleet statistics
SELECT
    COUNT(*) AS total_cars,
    COUNT(CASE WHEN available = true THEN 1 END) AS available_cars,
    AVG(price_per_day) AS avg_daily_rate,
    AVG(mileage) AS avg_mileage
FROM cars;

-- Revenue summary
SELECT
    SUM(total_price) AS total_revenue,
    AVG(total_price) AS avg_contract_value,
    COUNT(*) AS total_contracts
FROM rental_contracts
WHERE start_date >= '2024-01-01';
```

### Common Mistakes

**Mistake: Selecting non-aggregated columns without GROUP BY**
```sql
-- WRONG: What 'brand' should it show with the average?
SELECT brand, AVG(price_per_day) FROM cars;

-- CORRECT: Either aggregate all columns, or use GROUP BY (covered next)
SELECT AVG(price_per_day) FROM cars;
```

**Mistake: Using WHERE to filter aggregates**
```sql
-- WRONG: WHERE runs before aggregation
SELECT COUNT(*) FROM customers WHERE COUNT(*) > 10;

-- CORRECT: Use HAVING for aggregate conditions (covered next)
```

---

## GROUP BY and HAVING: Aggregating by Categories

### What: Grouping Data for Summarization

GROUP BY divides rows into groups based on column values, then applies aggregate functions to each group separately.

### Why: Category-Based Analysis

Instead of one total, you often need totals by category:
- "How many cars in each category?"
- "What's the average rental price by city?"
- "Which customer has the most rentals?"

### How: Building Grouped Queries

**Basic GROUP BY:**
```sql
-- Count cars in each category
SELECT category, COUNT(*) AS car_count
FROM cars
GROUP BY category;
```

**Result:**
| category | car_count |
|----------|-----------|
| Luxury | 15 |
| Family | 25 |
| Sport | 10 |

**Multiple Grouping Columns:**
```sql
-- Count cars by category AND availability
SELECT category, available, COUNT(*) AS count
FROM cars
GROUP BY category, available;
```

### The Critical Rule: Every Non-Aggregated Column Must Be in GROUP BY

This is the most common GROUP BY error:

```sql
-- WRONG: 'brand' is not in GROUP BY and not aggregated
SELECT category, brand, COUNT(*)
FROM cars
GROUP BY category;

-- CORRECT: Include brand in GROUP BY
SELECT category, brand, COUNT(*)
FROM cars
GROUP BY category, brand;

-- OR: Aggregate brand somehow
SELECT category, COUNT(DISTINCT brand) AS brand_count, COUNT(*) AS total
FROM cars
GROUP BY category;
```

### HAVING: Filtering Grouped Results

WHERE filters rows BEFORE grouping. HAVING filters groups AFTER aggregation.

```sql
-- Categories with more than 10 cars
SELECT category, COUNT(*) AS car_count
FROM cars
GROUP BY category
HAVING COUNT(*) > 10;
```

**The Difference:**
- WHERE: "Only consider luxury cars" (before grouping)
- HAVING: "Only show categories with more than 10 cars" (after grouping)

**Combining WHERE and HAVING:**
```sql
-- Among available cars, which categories have more than 5?
SELECT category, COUNT(*) AS available_count
FROM cars
WHERE available = true          -- Filter rows first
GROUP BY category
HAVING COUNT(*) > 5;            -- Then filter groups
```

### Execution Order

Understanding the order helps you write correct queries:

1. **FROM**: Which tables?
2. **WHERE**: Filter individual rows
3. **GROUP BY**: Form groups
4. **HAVING**: Filter groups
5. **SELECT**: Choose columns (including aggregates)
6. **ORDER BY**: Sort results

### Action: Kailua Grouped Analysis

```sql
-- Revenue by customer (top 10)
SELECT
    c.first_name,
    c.last_name,
    COUNT(rc.contract_id) AS rental_count,
    SUM(rc.total_price) AS total_spent
FROM customers c
LEFT JOIN rental_contracts rc ON c.customer_id = rc.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING SUM(rc.total_price) > 0
ORDER BY total_spent DESC
LIMIT 10;

-- Monthly rental statistics
SELECT
    YEAR(start_date) AS year,
    MONTH(start_date) AS month,
    COUNT(*) AS rentals,
    SUM(total_price) AS revenue
FROM rental_contracts
GROUP BY YEAR(start_date), MONTH(start_date)
ORDER BY year, month;
```

### Common Mistakes

**Mistake: Non-aggregated column not in GROUP BY**
```sql
-- WRONG: first_name is not in GROUP BY
SELECT city, first_name, COUNT(*)
FROM customers
GROUP BY city;

-- CORRECT: Add to GROUP BY or remove from SELECT
SELECT city, COUNT(*)
FROM customers
GROUP BY city;
```

**Mistake: Using column alias in HAVING**
```sql
-- May not work in all databases
SELECT category, COUNT(*) AS car_count
FROM cars
GROUP BY category
HAVING car_count > 10;

-- Safer: Repeat the aggregate expression
SELECT category, COUNT(*) AS car_count
FROM cars
GROUP BY category
HAVING COUNT(*) > 10;
```

**Mistake: WHERE vs HAVING confusion**
```sql
-- WRONG: WHERE can't use aggregates
SELECT category, COUNT(*)
FROM cars
WHERE COUNT(*) > 10
GROUP BY category;

-- CORRECT: HAVING for aggregate conditions
SELECT category, COUNT(*)
FROM cars
GROUP BY category
HAVING COUNT(*) > 10;
```

---

## ORDER BY: Sorting Results

### What: Controlling Result Order

ORDER BY sorts your query results by one or more columns.

### Why: Meaningful Data Presentation

Unsorted data is hard to use. Users expect:
- Alphabetical lists (customers by name)
- Chronological order (rentals by date)
- Ranked results (top customers by spending)

### How: Sorting Basics

**Ascending Order (Default):**
```sql
SELECT * FROM customers ORDER BY last_name;
SELECT * FROM customers ORDER BY last_name ASC;  -- Same as above
```

**Descending Order:**
```sql
SELECT * FROM cars ORDER BY price_per_day DESC;  -- Most expensive first
```

**Multiple Sort Columns:**
```sql
-- Sort by category, then by price within each category
SELECT * FROM cars ORDER BY category ASC, price_per_day DESC;
```

**Sorting by Expressions:**
```sql
-- Sort by rental duration
SELECT *, DATEDIFF(end_date, start_date) AS duration
FROM rental_contracts
ORDER BY DATEDIFF(end_date, start_date) DESC;
```

### ORDER BY with Aggregates

```sql
-- Categories by car count, highest first
SELECT category, COUNT(*) AS car_count
FROM cars
GROUP BY category
ORDER BY car_count DESC;

-- Note: Some databases allow ORDER BY car_count, others need ORDER BY COUNT(*)
```

### LIMIT: Controlling Result Size

Often combined with ORDER BY:
```sql
-- Top 5 most expensive cars
SELECT * FROM cars ORDER BY price_per_day DESC LIMIT 5;

-- 10 most recent rentals
SELECT * FROM rental_contracts ORDER BY start_date DESC LIMIT 10;
```

### NULL Handling in ORDER BY

NULLs sort first (ASC) or last (DESC) depending on the database. MySQL puts NULLs first for ASC.

```sql
-- If you need specific NULL handling:
SELECT * FROM customers
ORDER BY phone IS NULL, phone;  -- NULLs at end
```

### Action: Kailua Sorted Queries

```sql
-- Available cars sorted by price (cheapest first)
SELECT license_plate, brand, model, price_per_day
FROM cars
WHERE available = true
ORDER BY price_per_day ASC;

-- Recent contracts
SELECT c.first_name, c.last_name, rc.start_date, rc.end_date
FROM rental_contracts rc
INNER JOIN customers c ON rc.customer_id = c.customer_id
ORDER BY rc.start_date DESC
LIMIT 20;
```

---

## Integration Patterns

### SQL in the Application Architecture

Understanding where SQL fits in your full-stack application:

```
User Browser
     |
     | HTTP Request (GET /cars)
     v
[@Controller]
  @GetMapping("/cars")
     |
     | carService.findAvailable()
     v
[@Service]
  CarService
     |
     | carRepository.findByAvailableTrue()
     v
[@Repository]
  CarRepository
     |
     | jdbcTemplate.query("SELECT * FROM cars WHERE available = true", rowMapper)
     v
[MySQL Database]
     |
     | ResultSet (rows and columns)
     v
[RowMapper]
     |
     | Converts to List<Car>
     v
[Back up through layers]
     |
     v
[Thymeleaf Template]
     |
     | th:each="car : ${cars}"
     v
User Browser (HTML table of available cars)
```

The SQL queries you're learning execute at the Repository layer. Everything else in the stack either prepares for the query (parameters) or processes its results (Collections, HTML).

### Pattern: SELECT to Java Collection

```java
// In CarRepository
public List<Car> findAll() {
    String sql = "SELECT car_id, license_plate, brand, model, category, price_per_day " +
                 "FROM cars";
    return jdbcTemplate.query(sql, new CarRowMapper());
}

public List<Car> findByCategory(String category) {
    String sql = "SELECT * FROM cars WHERE category = ?";
    return jdbcTemplate.query(sql, new CarRowMapper(), category);
}
```

The `?` is a parameter placeholder - JdbcTemplate safely inserts the value, preventing SQL injection.

### Pattern: INSERT from Form Data

When a user submits a customer registration form:

1. HTML form has inputs: `name="firstName"`, `name="lastName"`, `name="email"`
2. Controller receives `@RequestParam String firstName`, etc.
3. Service calls repository
4. Repository executes INSERT:

```java
public int save(Customer customer) {
    String sql = "INSERT INTO customers (first_name, last_name, email) VALUES (?, ?, ?)";
    return jdbcTemplate.update(sql,
        customer.getFirstName(),
        customer.getLastName(),
        customer.getEmail());
}
```

### Pattern: Aggregates for Dashboard

Your web application might show a dashboard with summary statistics:

```java
// In ContractRepository
public Map<String, Object> getMonthlyStats() {
    String sql = "SELECT COUNT(*) as total, SUM(total_price) as revenue " +
                 "FROM rental_contracts " +
                 "WHERE MONTH(start_date) = MONTH(CURRENT_DATE)";
    return jdbcTemplate.queryForMap(sql);
}
```

The aggregate query returns a single row with summary data, displayed in your dashboard template.

---

## Common Struggles and How to Overcome Them

### Struggle 1: JOIN Syntax and When to Use Which Type

**Why this confuses students:** JOINs feel abstract, and the different types (INNER, LEFT, RIGHT) seem similar.

**How to think about it:** Draw Venn diagrams. Ask yourself: "Do I need ALL customers (even those without rentals), or only customers who HAVE rentals?"

- INNER JOIN = Only the intersection (rows that match in both tables)
- LEFT JOIN = All of left table + matching from right
- RIGHT JOIN = All of right table + matching from left

**Strategy:** Start with INNER JOIN. If your query is missing expected rows, switch to LEFT JOIN and look for NULLs to understand what's not matching.

**Exam tip:** "I used LEFT JOIN because I needed all customers, including those who haven't rented yet. INNER JOIN would have excluded customers with no rental history."

### Struggle 2: WHERE vs HAVING

**Why this confuses students:** Both filter data, so why two different keywords?

**How to think about it:**
- WHERE filters ROWS before any grouping happens
- HAVING filters GROUPS after aggregation

If your condition involves COUNT(), SUM(), AVG(), etc., use HAVING. If your condition involves regular column values, use WHERE.

**Strategy:** Read your query from FROM clause down:
1. FROM - get tables
2. WHERE - filter individual rows
3. GROUP BY - form groups
4. HAVING - filter those groups
5. SELECT - pick what to show

**Exam tip:** "WHERE runs before GROUP BY, so it filters individual rows. HAVING runs after GROUP BY, so it can filter based on aggregate results like COUNT(*) > 10."

### Struggle 3: GROUP BY Requirements

**Why this confuses students:** The rule "every non-aggregated column must be in GROUP BY" seems arbitrary.

**How to think about it:** If you're grouping by category and selecting brand, which brand should appear? There could be many brands per category. The database can't choose, so it either errors or picks arbitrarily.

**Strategy:** For every column in your SELECT:
- Is it in GROUP BY? OK
- Is it inside an aggregate function? OK
- Neither? ERROR - add to GROUP BY or wrap in aggregate

**Exam tip:** "I included customer_id in GROUP BY even though I'm grouping by customer, because MySQL needs every selected column to be either grouped or aggregated."

### Struggle 4: NULL Behavior

**Why this confuses students:** NULL isn't the same as 0, empty string, or false. It's "unknown."

**How to think about it:** Any comparison with NULL returns NULL (unknown), not true or false:
- `5 = NULL` -> NULL
- `NULL = NULL` -> NULL
- `5 > NULL` -> NULL

That's why `WHERE column = NULL` finds nothing - the comparison never returns true.

**Strategy:** Always use `IS NULL` or `IS NOT NULL` for NULL checks. In JOINs, remember that NULL values won't match anything.

**Exam tip:** "I used IS NULL instead of = NULL because NULL comparisons with = always return NULL, not true or false."

### Struggle 5: Visualizing Multi-Table JOINs

**Why this confuses students:** Joining 3+ tables gets confusing quickly.

**How to think about it:** Build the query incrementally:
1. Start with the central table (usually the one with foreign keys)
2. JOIN one table at a time
3. Run the query after each JOIN to see intermediate results
4. Add the next JOIN only when the current result looks right

**Strategy:** Draw a diagram showing tables and their relationships. Follow the arrows (foreign keys) to determine which columns to join on.

**Exam tip:** "I started with rental_contracts because it's the central table referencing both customers and cars. Then I joined customers first to verify customer names appeared, then added cars."

### Struggle 6: Aggregate Functions Returning Single Values

**Why this confuses students:** It's unclear how aggregates interact with regular columns.

**How to think about it:** Aggregates collapse many rows into one value. If you SELECT both an aggregate and a regular column without GROUP BY, what should the regular column show? There's no sensible answer.

**Strategy:** Either:
- Use ONLY aggregates (no regular columns): `SELECT COUNT(*), AVG(price) FROM cars`
- Or GROUP BY all regular columns: `SELECT category, COUNT(*), AVG(price) FROM cars GROUP BY category`

---

## Practice Exercises

### Exercise 1: Basic SELECT and WHERE (Maximum Guidance)

**What you'll build:** A series of queries to explore a car rental database.

**Connection to Kailua:** These are the exact query patterns you'll use in your project.

**Skills you'll practice:**
- SELECT with column selection
- WHERE with various operators
- Combining conditions with AND/OR

**Step-by-step approach:**

1. Write a query to select all cars:
   ```sql
   SELECT * FROM cars;
   ```

2. Select only specific columns (license_plate, brand, model):
   ```sql
   SELECT license_plate, brand, model FROM cars;
   ```

3. Filter for luxury cars:
   ```sql
   SELECT * FROM cars WHERE category = 'Luxury';
   ```

4. Filter for cars under 600 DKK per day:
   ```sql
   SELECT * FROM cars WHERE price_per_day < 600;
   ```

5. Combine conditions - available luxury cars under 1000 DKK:
   ```sql
   SELECT * FROM cars
   WHERE category = 'Luxury'
     AND price_per_day < 1000
     AND available = true;
   ```

**What success looks like:** You can write SELECT queries with WHERE clauses that filter data by multiple criteria.

---

### Exercise 2: JOIN Operations (Moderate Guidance)

**What you'll build:** Queries that combine data from multiple tables.

**Skills you'll practice:**
- INNER JOIN syntax
- LEFT JOIN for inclusive queries
- Multi-table JOINs

**Requirements:**
Write queries to answer these questions:

1. List all rental contracts with customer names (INNER JOIN customers and rental_contracts)

2. Show all customers and their rental count, including customers with zero rentals (LEFT JOIN, COUNT, GROUP BY)

3. Display complete rental information: customer name, car details (brand, model, license plate), and rental dates (multi-table JOIN)

4. Find cars that have never been rented (LEFT JOIN, WHERE ... IS NULL)

**Key concepts to apply:**
- Choose INNER vs LEFT JOIN based on whether you need "all rows" or "only matching rows"
- Use table aliases for readability
- Remember to specify which table each column comes from

**Success criteria:** You can combine data from multiple tables and explain why you chose each JOIN type.

---

### Exercise 3: Aggregates and Grouping (Minimal Guidance)

**What you'll build:** Management reports for Kailua Car Rental.

**Requirements:**
Create queries for:

1. Fleet summary: total cars, average price, min/max price
2. Cars per category (GROUP BY)
3. Top 5 customers by number of rentals (GROUP BY, ORDER BY, LIMIT)
4. Monthly revenue report for the current year (GROUP BY month, SUM)
5. Categories with more than 10 cars (GROUP BY, HAVING)

**Skills you'll practice:**
- COUNT, SUM, AVG, MIN, MAX
- GROUP BY with aggregates
- HAVING for filtering groups
- Combining JOINs with aggregation

Build these queries independently, applying all concepts from this topic.

---

## Preparing for the Oral Exam

### Key Questions You Should Be Able to Answer

- "Explain the difference between INNER JOIN and LEFT JOIN."
- "When would you use HAVING instead of WHERE?"
- "How do aggregate functions work with GROUP BY?"
- "Why is it dangerous to write UPDATE or DELETE without a WHERE clause?"
- "How does a SQL query in your repository become a List in your Java code?"
- "What's the difference between COUNT(*) and COUNT(column)?"

### Demo Tips

When demonstrating SQL in your project:

1. **Show the query:** Open MySQL Workbench and run a key query from your project
2. **Explain the purpose:** "This query retrieves all active rentals with customer and car information"
3. **Trace to Java code:** Show the same query in your repository class
4. **Connect to the UI:** Show how the query results appear on the web page

### What NOT to Do

- Don't just read the SQL syntax without explaining what it accomplishes
- Don't forget to mention why you chose specific JOIN types
- Don't overlook the connection between SQL and Java Collections

### What TO Do

- Explain the business question each query answers
- Justify your JOIN type selection
- Show how aggregate queries power your dashboards or reports
- Connect SQL results to the `List<DomainObject>` in your Java code

---

## Looking Ahead

### What You Can Do Now

- Write SELECT queries with filtering, sorting, and column selection
- Combine data from multiple tables using appropriate JOIN types
- Perform INSERT, UPDATE, DELETE operations safely
- Calculate summaries using aggregate functions
- Group data and filter groups using GROUP BY and HAVING
- Sort results using ORDER BY

### How This Will Be Used in Upcoming Topics

- **SQL Advanced (Phase 3):** Subqueries let you nest SELECT statements inside other queries. Views let you save complex queries for reuse. Stored procedures let you write SQL logic that runs on the database server.

- **Database-Java Integration (Phase 3-4):** These queries will be executed from Java using JdbcTemplate. The results become `List<Car>`, `List<Customer>`, etc.

- **Spring Boot Web Applications (Phase 5):** Your controllers will call services that call repositories that execute these queries. The data flows through your application to Thymeleaf templates.

### Project Connection

**Kailua Car Rental (Phase 4):**
- SELECT queries for available cars, customer searches, rental history
- INSERT queries for new customers, new contracts
- UPDATE queries for car availability, customer information
- Aggregate queries for fleet statistics, revenue reports
- JOINs to combine customers, cars, and contracts

**Onskeskyen Wishlist (Phase 7):**
- SELECT with JOINs for wishlists with items
- INSERT for new wishlists and items
- UPDATE for item priorities, wishlist sharing
- COUNT for items per wishlist
- GROUP BY for wishlist statistics

---

## Key Takeaways

- **SQL is Declarative:** You describe WHAT you want, not HOW to get it. The database optimizes execution.

- **SELECT is Foundation:** Master SELECT with WHERE, ORDER BY, and column selection before moving to complex queries.

- **JOINs Combine Tables:** Use INNER JOIN when you need only matching rows. Use LEFT JOIN when you need all rows from one table regardless of matches.

- **DML Requires Care:** Always use WHERE with UPDATE and DELETE. Test with SELECT first.

- **Aggregates Summarize:** COUNT, SUM, AVG, MIN, MAX collapse multiple rows into single values.

- **GROUP BY + HAVING:** GROUP BY creates groups for aggregation. HAVING filters groups after aggregation. WHERE filters rows before grouping.

**For the exam:** Be able to write a multi-table JOIN query, explain why you chose that JOIN type, and trace how the results flow from database through Java to the web page.

---

## For the Next Topic Agent

### Terminology Established This Topic

- **SQL (Structured Query Language):** The standard language for interacting with relational databases. Declarative, not imperative.

- **SELECT Query:** SQL statement to retrieve data from tables. Components: SELECT (columns), FROM (tables), WHERE (filter), ORDER BY (sort).

- **JOIN:** Operation combining rows from two or more tables based on related columns. Types: INNER (intersection), LEFT (all left + matching right), RIGHT (all right + matching left), FULL OUTER (all from both).

- **DML (Data Manipulation Language):** SQL statements that modify data: INSERT (add rows), UPDATE (modify rows), DELETE (remove rows).

- **Aggregate Functions:** Functions that calculate a single value from multiple rows: COUNT, SUM, AVG, MIN, MAX.

- **GROUP BY:** Clause that groups rows sharing values in specified columns for aggregate calculations.

- **HAVING:** Clause that filters groups after aggregation (vs WHERE which filters rows before grouping).

- **ORDER BY:** Clause that sorts query results. ASC (ascending, default) or DESC (descending).

- **Table Alias:** Short name for a table used in queries (e.g., `customers c`). Improves readability especially in JOINs.

- **Column Alias:** Renamed column in result set using AS keyword (e.g., `COUNT(*) AS total_count`).

- **NULL:** Special value meaning "unknown" or "no value." Requires IS NULL / IS NOT NULL for comparison.

### Example Classes/Concepts Created

- **Kailua Database Schema:** customers (customer_id, first_name, last_name, email, phone, city), cars (car_id, license_plate, brand, model, category, price_per_day, available, mileage), rental_contracts (contract_id, customer_id, car_id, start_date, end_date, total_price)

- **JOIN Decision Pattern:**
  - Need only matching rows? INNER JOIN
  - Need all from left table? LEFT JOIN
  - Need to find unmatched rows? LEFT JOIN + WHERE ... IS NULL

- **Safe DML Pattern:** Always write WHERE clause first; test with SELECT before UPDATE/DELETE

- **GROUP BY Validation:** Every non-aggregated column in SELECT must appear in GROUP BY

- **Execution Order:** FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY

### Student Capabilities After This Topic

Students who complete this material can now:
- Write SELECT queries with filtering, projection, and sorting
- Combine data from multiple tables using appropriate JOIN types
- Perform safe INSERT, UPDATE, DELETE operations
- Calculate summaries using aggregate functions
- Group data and filter groups with GROUP BY and HAVING
- Explain the difference between WHERE and HAVING
- Describe how SQL queries become Java Collections
- Choose between JOIN types based on requirements

### Pedagogical Patterns Used

- **Declarative vs Imperative Comparison:** Contrasting SQL's "what" approach with Java's "how" approach to build mental model

- **Venn Diagram Visualization:** JOIN types explained as overlapping circles

- **Safety-First DML:** Emphasizing WHERE clause importance with "write WHERE first" pattern

- **Execution Order Walkthrough:** Explaining GROUP BY/HAVING/WHERE confusion through query execution sequence

- **Incremental Query Building:** Starting simple, adding complexity step by step (SELECT * -> specific columns -> WHERE -> JOIN -> aggregate)

- **Project Grounding:** Every concept tied to Kailua or Onskeskyen practical applications

- **Architecture Connection:** Showing SQL's position in the full-stack data flow (Database -> Repository -> Service -> Controller -> Template)

- **Common Mistakes Pattern:** Each section includes explicit "Common Mistakes" with wrong and correct examples
