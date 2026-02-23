# Advanced SQL & Database Administration - 2nd Semester Programming

*Prerequisites: SQL Fundamentals (SELECT, JOINs, DML, aggregates, GROUP BY)*
*Phase: 3 - Advanced Database & Collections Integration*
*Exam Weight: Moderate-High (subqueries, views, stored procedures emphasized; admin topics at awareness level)*

---

## What You'll Learn

By the end of this topic, you will be able to:
- **Write complex nested queries** using both correlated and non-correlated subqueries
- **Use EXISTS and IN operators** for set membership testing
- **Create database views** for simplified data access and enhanced security
- **Develop stored procedures and functions** for reusable database logic
- **Implement triggers** for automatic data validation and auditing
- **Understand ACID properties** and why transaction management matters
- **Comprehend database administration concepts** including user privileges and backup strategies

These advanced SQL skills extend everything you learned in SQL Fundamentals. Where basic queries answered "show me this data," advanced SQL answers "how do I organize, protect, and automate my database?" These concepts directly enable the database-Java integration you'll build next.

---

## Why This Matters

### From Simple Queries to Database Architecture

In SQL Fundamentals, you learned to retrieve and modify data. Now you'll learn to *architect* how data is accessed, validated, and protected. This is the difference between writing individual queries and designing systems.

Consider the Kailua Car Rental system:

**Without advanced SQL:**
- Every Java method writes its own complex query
- Business rules are scattered across your Java code
- Any developer can access any data

**With advanced SQL:**
- Views simplify complex queries into reusable "virtual tables"
- Stored procedures encapsulate business logic in the database
- Triggers enforce data integrity automatically
- User privileges control who can do what

### Business Logic: Java vs. Database

A critical architectural decision you'll face: where should business logic live?

**Java-side logic:**
```java
// Checking if customer qualifies for discount - all in Java
public boolean qualifiesForDiscount(int customerId) {
    List<Contract> contracts = contractRepo.findByCustomerId(customerId);
    return contracts.size() >= 5;
}
```

**Database-side logic (stored procedure):**
```sql
-- Same logic, but in the database
CREATE FUNCTION customer_qualifies_for_discount(cust_id INT)
RETURNS BOOLEAN
BEGIN
    RETURN (SELECT COUNT(*) FROM rental_contracts WHERE customer_id = cust_id) >= 5;
END
```

Neither approach is universally "better." The architectural choice depends on:
- **Performance:** Database-side avoids transferring data over the network
- **Consistency:** Database-side ensures all applications use the same logic
- **Testability:** Java-side is easier to unit test
- **Maintainability:** Where does your team's expertise lie?

Understanding both sides makes you a more effective developer. At exam, be prepared to discuss these trade-offs.

### Enabling What Comes Next

Advanced SQL concepts flow directly into Database-Java Integration:

```
[Database with Views, Procedures, Triggers]
          |
          | JdbcTemplate calls
          v
[Java Repository Layer]
          |
          | Returns List<DomainObject>
          v
[Spring Boot Application]
```

Views simplify the queries your repositories execute. Stored procedures can be called from JdbcTemplate. Understanding transactions is essential when your Java code modifies multiple tables. This topic provides the database foundation; the next topic shows how Java connects to it.

---

## Building on What You Know

### From SQL Fundamentals (Just Completed)

You already understand the building blocks:

**SELECT queries:** The foundation for subqueries, views, and stored procedures
```sql
-- Your SQL Fundamentals query
SELECT c.first_name, c.last_name, COUNT(rc.contract_id) AS rental_count
FROM customers c
LEFT JOIN rental_contracts rc ON c.customer_id = rc.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name;
```

**JOINs:** Subqueries offer an alternative approach to combining data

**Aggregate functions:** Subqueries often use aggregates for comparison values

**The safe DML pattern:** Still applies - stored procedures don't exempt you from WHERE clauses

### From 1st Semester Java

**Methods as reusable code blocks:** Stored procedures are the database equivalent
```java
// Java: A reusable method
public double calculateDiscount(Customer customer) { ... }
```
```sql
-- SQL: A reusable function
CREATE FUNCTION calculate_discount(customer_id INT) RETURNS DECIMAL(5,2)
```

**Exception handling:** Database triggers can reject invalid operations, similar to throwing exceptions

**Encapsulation:** Views hide complexity, just as private methods hide implementation details

### From Systems Development (GRASP)

**Information Expert:** Views and stored procedures keep data logic close to the data

**Low Coupling:** Views provide a stable interface even when underlying tables change

These patterns appear throughout this topic - you're applying familiar principles to a new domain.

---

## Subqueries: Queries Within Queries

### What: Nesting SELECT Statements

A subquery is a SELECT statement inside another SQL statement. The inner query executes first, and its result is used by the outer query.

### Why: Solving Complex Problems Step by Step

Some questions can't be answered with a single query:
- "Which customers have spent more than the average?"
- "Which cars have never been rented?"
- "Show contracts for customers from Copenhagen"

Subqueries let you break these into logical steps.

### The Two Types: Non-Correlated vs Correlated

This distinction is **critical** - it affects both how you write subqueries and how the database executes them.

**Non-Correlated Subquery:**
The inner query is independent. It runs once, produces a result, then the outer query uses that result.

```sql
-- "Find customers who have spent more than the average contract value"
SELECT c.first_name, c.last_name
FROM customers c
WHERE c.customer_id IN (
    SELECT rc.customer_id
    FROM rental_contracts rc
    GROUP BY rc.customer_id
    HAVING SUM(rc.total_price) > (SELECT AVG(total_price) FROM rental_contracts)
);
```

**Mental model:** The inner query is like calling a method that returns a value. The outer query uses that value.

```
Step 1: (SELECT AVG(total_price) FROM rental_contracts) --> 450.00
Step 2: Use 450.00 in: HAVING SUM(rc.total_price) > 450.00
```

**Correlated Subquery:**
The inner query references the outer query. It must re-execute for EACH row of the outer query.

```sql
-- "Find cars that have been rented more than 5 times"
SELECT car.license_plate, car.brand, car.model
FROM cars car
WHERE (
    SELECT COUNT(*)
    FROM rental_contracts rc
    WHERE rc.car_id = car.car_id  -- References outer query!
) > 5;
```

**Mental model:** For each car, ask "how many contracts does THIS car have?" The subquery can't run independently because it needs to know which car.

```
For car_id = 1: (SELECT COUNT(*) ... WHERE rc.car_id = 1) --> 3
For car_id = 2: (SELECT COUNT(*) ... WHERE rc.car_id = 2) --> 7  <-- Include!
For car_id = 3: (SELECT COUNT(*) ... WHERE rc.car_id = 3) --> 2
...
```

### Recognizing the Difference

**Key question:** Does the inner query reference any column from the outer query?

- **Yes:** Correlated (inner depends on outer)
- **No:** Non-correlated (inner is independent)

This matters for:
1. **Performance:** Correlated subqueries execute once per outer row (can be slow for large tables)
2. **Debugging:** You can run non-correlated subqueries alone; correlated ones can't run independently
3. **Exam:** "Is this correlated or non-correlated?" is a common oral exam question

### Subquery Placement: WHERE, FROM, SELECT

**In WHERE clause (most common):**
```sql
-- Cars cheaper than average
SELECT * FROM cars
WHERE price_per_day < (SELECT AVG(price_per_day) FROM cars);
```

**In FROM clause (derived table):**
```sql
-- Treat subquery result as a temporary table
SELECT category, avg_price
FROM (
    SELECT category, AVG(price_per_day) AS avg_price
    FROM cars
    GROUP BY category
) AS category_averages
WHERE avg_price > 500;
```

Note: Subqueries in FROM clause MUST have an alias (`AS category_averages`).

**In SELECT clause (scalar subquery):**
```sql
-- Include a calculated value in each row
SELECT
    c.first_name,
    c.last_name,
    (SELECT COUNT(*) FROM rental_contracts rc
     WHERE rc.customer_id = c.customer_id) AS rental_count
FROM customers c;
```

### EXISTS and IN Operators

**IN:** Tests if a value matches any value in a set.
```sql
-- Customers who have made at least one rental
SELECT * FROM customers
WHERE customer_id IN (SELECT customer_id FROM rental_contracts);
```

**EXISTS:** Tests if a subquery returns any rows (true/false).
```sql
-- Same result, different approach
SELECT * FROM customers c
WHERE EXISTS (
    SELECT 1 FROM rental_contracts rc
    WHERE rc.customer_id = c.customer_id
);
```

**When to use which:**

| Use IN when... | Use EXISTS when... |
|----------------|-------------------|
| Subquery returns a small set of values | Subquery might return many rows |
| Checking against a list of specific values | You just need to know if rows exist |
| The subquery is non-correlated | The subquery is correlated |

**NOT EXISTS for "never" queries:**
```sql
-- Customers who have NEVER rented
SELECT * FROM customers c
WHERE NOT EXISTS (
    SELECT 1 FROM rental_contracts rc
    WHERE rc.customer_id = c.customer_id
);
```

This is often more efficient than `NOT IN`, especially with potential NULL values.

### Subqueries vs JOINs

Many subqueries can be rewritten as JOINs:

```sql
-- Subquery approach
SELECT * FROM customers
WHERE customer_id IN (SELECT customer_id FROM rental_contracts WHERE total_price > 1000);

-- JOIN approach (often preferred)
SELECT DISTINCT c.*
FROM customers c
INNER JOIN rental_contracts rc ON c.customer_id = rc.customer_id
WHERE rc.total_price > 1000;
```

**Choose subqueries when:**
- You need an aggregate value for comparison
- The logic naturally expresses as "check if exists"
- You want to emphasize the filtering step

**Choose JOINs when:**
- You need columns from both tables in the result
- Performance is critical (JOINs are often optimized better)
- The relationship is direct

### Action: Kailua Subquery Scenarios

```sql
-- Cars that have never been rented (NOT EXISTS)
SELECT license_plate, brand, model
FROM cars c
WHERE NOT EXISTS (
    SELECT 1 FROM rental_contracts rc
    WHERE rc.car_id = c.car_id
);

-- Customers with above-average spending (non-correlated)
SELECT c.first_name, c.last_name
FROM customers c
INNER JOIN rental_contracts rc ON c.customer_id = rc.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING SUM(rc.total_price) > (SELECT AVG(total_price) FROM rental_contracts);

-- Most recently rented car in each category (correlated)
SELECT c.category, c.brand, c.model
FROM cars c
WHERE c.car_id = (
    SELECT rc.car_id
    FROM rental_contracts rc
    INNER JOIN cars c2 ON rc.car_id = c2.car_id
    WHERE c2.category = c.category
    ORDER BY rc.start_date DESC
    LIMIT 1
);
```

### Common Mistakes

**Mistake: Treating correlated as non-correlated**
```sql
-- WRONG: Trying to run this subquery alone for testing
SELECT COUNT(*) FROM rental_contracts rc WHERE rc.car_id = car.car_id;
-- Error: 'car' is not recognized (it's from the outer query)

-- CORRECT approach: Test with a specific value
SELECT COUNT(*) FROM rental_contracts rc WHERE rc.car_id = 5;
```

**Mistake: Using = with subqueries that return multiple rows**
```sql
-- WRONG: Subquery returns multiple customer_ids
SELECT * FROM customers WHERE customer_id = (SELECT customer_id FROM rental_contracts);

-- CORRECT: Use IN for multiple values
SELECT * FROM customers WHERE customer_id IN (SELECT customer_id FROM rental_contracts);
```

---

## Database Views: Virtual Tables

### What: Saved Queries as "Tables"

A view is a named SELECT query stored in the database. When you query a view, the database executes the underlying SELECT.

```sql
CREATE VIEW available_luxury_cars AS
SELECT car_id, license_plate, brand, model, price_per_day
FROM cars
WHERE category = 'Luxury' AND available = true;
```

Now you can query it like a table:
```sql
SELECT * FROM available_luxury_cars WHERE price_per_day < 1000;
```

### Why: Simplification, Security, and Abstraction

**Simplification:** Complex queries become simple
```sql
-- Without view: Repeat this complex JOIN everywhere
SELECT c.first_name, c.last_name, car.brand, car.model, rc.start_date
FROM rental_contracts rc
INNER JOIN customers c ON rc.customer_id = c.customer_id
INNER JOIN cars car ON rc.car_id = car.car_id;

-- With view: Query it simply
SELECT * FROM rental_details;
```

**Security:** Hide sensitive columns
```sql
-- Users see this view (no salary column)
CREATE VIEW public_employees AS
SELECT employee_id, first_name, last_name, department
FROM employees;  -- Original table has salary column

-- Even if users query the view, they can't see salaries
```

**Abstraction:** Shield applications from schema changes
```sql
-- If you rename a column in the base table, update the view
-- Applications querying the view don't need to change
CREATE OR REPLACE VIEW customer_summary AS
SELECT customer_id, full_name AS customer_name  -- Column renamed internally
FROM customers;
```

### How: Creating and Managing Views

**Basic view creation:**
```sql
CREATE VIEW view_name AS
SELECT ...;
```

**Replace existing view:**
```sql
CREATE OR REPLACE VIEW view_name AS
SELECT ...;
```

**Remove a view:**
```sql
DROP VIEW view_name;
```

**View with calculated columns:**
```sql
CREATE VIEW rental_statistics AS
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(rc.contract_id) AS total_rentals,
    COALESCE(SUM(rc.total_price), 0) AS total_spent,
    COALESCE(AVG(rc.total_price), 0) AS avg_rental_value
FROM customers c
LEFT JOIN rental_contracts rc ON c.customer_id = rc.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name;
```

### Updatable Views

Some views can be used for INSERT, UPDATE, DELETE:

```sql
CREATE VIEW copenhagen_customers AS
SELECT * FROM customers WHERE city = 'Copenhagen';

-- This works if the view meets certain criteria
INSERT INTO copenhagen_customers (first_name, last_name, email, city)
VALUES ('Anders', 'Jensen', 'anders@example.com', 'Copenhagen');
```

**Conditions for updatable views:**
- Based on a single table (no JOINs)
- No aggregate functions
- No DISTINCT, GROUP BY, HAVING
- No subqueries in SELECT list

### WITH CHECK OPTION

Prevents inserting/updating data that would disappear from the view:

```sql
CREATE VIEW copenhagen_customers AS
SELECT * FROM customers WHERE city = 'Copenhagen'
WITH CHECK OPTION;

-- This INSERT would fail - 'Aarhus' doesn't satisfy the view's WHERE
INSERT INTO copenhagen_customers (first_name, last_name, city)
VALUES ('Maria', 'Nielsen', 'Aarhus');
-- Error: CHECK OPTION failed
```

**Why this matters:** Without WITH CHECK OPTION, you could insert a row that immediately becomes invisible in the view - confusing and potentially a bug.

### Views in Application Architecture

In your Kailua or Onskeskyen projects:

```
[Java Repository] --> [View: rental_summary] --> [Base Tables: customers, cars, contracts]
```

**Benefits:**
- Repository queries are simpler
- Complex JOIN logic lives in one place (the view)
- If schema changes, update the view - not every repository method

```java
// Java repository using a view
public List<RentalSummary> findAllRentalSummaries() {
    String sql = "SELECT * FROM rental_summary WHERE status = 'active'";
    return jdbcTemplate.query(sql, rentalSummaryRowMapper);
}
```

### Action: Kailua View Examples

```sql
-- View for available cars with category details
CREATE VIEW available_cars_detail AS
SELECT c.car_id, c.license_plate, c.brand, c.model, c.category,
       c.price_per_day, c.mileage
FROM cars c
WHERE c.available = true;

-- View for active rentals with full details
CREATE VIEW active_rentals AS
SELECT rc.contract_id,
       CONCAT(cust.first_name, ' ', cust.last_name) AS customer_name,
       cust.phone AS customer_phone,
       CONCAT(car.brand, ' ', car.model) AS vehicle,
       car.license_plate,
       rc.start_date, rc.end_date, rc.total_price
FROM rental_contracts rc
INNER JOIN customers cust ON rc.customer_id = cust.customer_id
INNER JOIN cars car ON rc.car_id = car.car_id
WHERE rc.end_date >= CURRENT_DATE;
```

### Common Mistakes

**Mistake: Expecting views to store data**
Views don't store data - they're saved queries. Every time you SELECT from a view, the underlying query runs.

**Mistake: Creating views with ambiguous column names**
```sql
-- WRONG: Both tables have 'id' column
CREATE VIEW rental_info AS
SELECT * FROM customers INNER JOIN rental_contracts ON ...;

-- CORRECT: Explicitly name columns
CREATE VIEW rental_info AS
SELECT c.customer_id, c.first_name, rc.contract_id, rc.start_date
FROM customers c INNER JOIN rental_contracts rc ON ...;
```

---

## Stored Procedures and Functions

### What: Reusable Database Programs

Stored procedures and functions are SQL code blocks stored in the database, similar to methods in Java.

**Function:** Returns a single value, used in expressions
**Procedure:** May return multiple values or result sets, called with CALL

### Why: Encapsulating Business Logic

**Consistency:** The same logic applies whether accessed from Java, Python, or manual SQL
**Performance:** Logic runs on the database server, avoiding network round-trips
**Security:** Users can execute procedures without direct table access

### Functions: Returning Single Values

```sql
DELIMITER //

CREATE FUNCTION calculate_rental_price(
    daily_rate DECIMAL(10,2),
    rental_days INT
)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    RETURN daily_rate * rental_days;
END //

DELIMITER ;
```

**Usage:**
```sql
SELECT license_plate, brand,
       calculate_rental_price(price_per_day, 7) AS weekly_price
FROM cars;
```

**Key syntax elements:**
- `DELIMITER //` - Changes statement terminator (semicolons inside function body need this)
- `RETURNS type` - What type the function returns
- `DETERMINISTIC` - Same inputs always produce same output (helps optimizer)
- `BEGIN...END` - Function body

### Stored Procedures: Complex Operations

```sql
DELIMITER //

CREATE PROCEDURE create_rental(
    IN p_customer_id INT,
    IN p_car_id INT,
    IN p_start_date DATE,
    IN p_end_date DATE,
    OUT p_contract_id INT
)
BEGIN
    DECLARE v_daily_rate DECIMAL(10,2);
    DECLARE v_days INT;
    DECLARE v_total DECIMAL(10,2);

    -- Get the car's daily rate
    SELECT price_per_day INTO v_daily_rate
    FROM cars WHERE car_id = p_car_id;

    -- Calculate rental duration and total
    SET v_days = DATEDIFF(p_end_date, p_start_date);
    SET v_total = v_daily_rate * v_days;

    -- Insert the contract
    INSERT INTO rental_contracts (customer_id, car_id, start_date, end_date, total_price)
    VALUES (p_customer_id, p_car_id, p_start_date, p_end_date, v_total);

    -- Return the new contract ID
    SET p_contract_id = LAST_INSERT_ID();

    -- Mark car as unavailable
    UPDATE cars SET available = false WHERE car_id = p_car_id;
END //

DELIMITER ;
```

**Calling the procedure:**
```sql
CALL create_rental(1, 5, '2024-03-01', '2024-03-08', @new_id);
SELECT @new_id;  -- Shows the generated contract_id
```

### Parameter Types

| Type | Direction | Usage |
|------|-----------|-------|
| IN | Input only | Pass values to procedure |
| OUT | Output only | Return values from procedure |
| INOUT | Both | Modify input and return it |

### Control Flow in Procedures

**IF statements:**
```sql
IF v_days > 7 THEN
    SET v_discount = 0.10;  -- 10% discount for week+ rentals
ELSEIF v_days > 3 THEN
    SET v_discount = 0.05;  -- 5% discount for 4+ days
ELSE
    SET v_discount = 0;
END IF;
```

**WHILE loops:**
```sql
WHILE v_counter < 10 DO
    -- loop body
    SET v_counter = v_counter + 1;
END WHILE;
```

### Connecting to Java

Procedures can be called from JdbcTemplate:

```java
// Calling stored procedure from Java
public int createRental(int customerId, int carId, LocalDate start, LocalDate end) {
    SimpleJdbcCall call = new SimpleJdbcCall(jdbcTemplate)
        .withProcedureName("create_rental");

    MapSqlParameterSource params = new MapSqlParameterSource()
        .addValue("p_customer_id", customerId)
        .addValue("p_car_id", carId)
        .addValue("p_start_date", start)
        .addValue("p_end_date", end);

    Map<String, Object> result = call.execute(params);
    return (Integer) result.get("p_contract_id");
}
```

### Functions vs Procedures: When to Use Each

| Use a Function when... | Use a Procedure when... |
|------------------------|------------------------|
| You need a calculated value in a query | You need to perform multiple operations |
| The operation is read-only | You need to INSERT/UPDATE/DELETE |
| You want to use it in SELECT, WHERE | You need to return multiple values |

### Common Mistakes

**Mistake: Forgetting DELIMITER**
```sql
-- WRONG: The CREATE stops at the first semicolon
CREATE FUNCTION my_func() RETURNS INT
BEGIN
    RETURN 1;  -- CREATE statement ends here!
END

-- CORRECT: Change delimiter first
DELIMITER //
CREATE FUNCTION my_func() RETURNS INT
BEGIN
    RETURN 1;
END //
DELIMITER ;
```

---

## Triggers: Automatic Actions

### What: Code That Runs on Data Changes

A trigger is a stored program that automatically executes when data is inserted, updated, or deleted.

### Why: Enforcing Rules and Auditing

**Data validation beyond constraints:**
```sql
-- Ensure rental end_date is after start_date
CREATE TRIGGER validate_rental_dates
BEFORE INSERT ON rental_contracts
FOR EACH ROW
BEGIN
    IF NEW.end_date <= NEW.start_date THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'End date must be after start date';
    END IF;
END
```

**Automatic auditing:**
```sql
-- Log every price change
CREATE TRIGGER log_price_changes
AFTER UPDATE ON cars
FOR EACH ROW
BEGIN
    IF OLD.price_per_day <> NEW.price_per_day THEN
        INSERT INTO price_audit (car_id, old_price, new_price, changed_at)
        VALUES (NEW.car_id, OLD.price_per_day, NEW.price_per_day, NOW());
    END IF;
END
```

### Trigger Timing and Events

| Timing | Meaning |
|--------|---------|
| BEFORE | Run before the data change |
| AFTER | Run after the data change |

| Event | Meaning |
|-------|---------|
| INSERT | New row being added |
| UPDATE | Existing row being modified |
| DELETE | Row being removed |

**Combinations:** BEFORE INSERT, AFTER INSERT, BEFORE UPDATE, AFTER UPDATE, BEFORE DELETE, AFTER DELETE

### NEW and OLD References

- **NEW:** The row data after the change (available for INSERT and UPDATE)
- **OLD:** The row data before the change (available for UPDATE and DELETE)

```sql
-- On UPDATE, you can access both
IF NEW.price_per_day <> OLD.price_per_day THEN ...
```

### Action: Kailua Trigger Scenario

```sql
DELIMITER //

-- When a rental contract ends, make the car available again
CREATE TRIGGER mark_car_available_on_return
AFTER UPDATE ON rental_contracts
FOR EACH ROW
BEGIN
    -- Check if this update marks the rental as returned
    IF OLD.status = 'active' AND NEW.status = 'returned' THEN
        UPDATE cars SET available = true WHERE car_id = NEW.car_id;
    END IF;
END //

-- Prevent deleting customers with active rentals
CREATE TRIGGER prevent_customer_delete_with_rentals
BEFORE DELETE ON customers
FOR EACH ROW
BEGIN
    DECLARE active_count INT;

    SELECT COUNT(*) INTO active_count
    FROM rental_contracts
    WHERE customer_id = OLD.customer_id AND status = 'active';

    IF active_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot delete customer with active rentals';
    END IF;
END //

DELIMITER ;
```

### Common Mistakes

**Mistake: Infinite trigger loops**
```sql
-- DANGEROUS: This trigger updates the same table, causing infinite recursion
CREATE TRIGGER bad_trigger
AFTER UPDATE ON cars
FOR EACH ROW
BEGIN
    UPDATE cars SET updated_at = NOW() WHERE car_id = NEW.car_id;
    -- This UPDATE triggers the trigger again!
END
```

**Solution:** Use BEFORE trigger to modify NEW values, or carefully design to avoid self-updates.

---

## Transaction Management and ACID

### What: Ensuring Data Integrity Across Multiple Operations

A transaction groups multiple SQL statements into a single unit - either all succeed, or all fail.

### Why: The Bank Transfer Problem

Imagine transferring money between accounts:
```sql
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
-- What if the system crashes HERE?
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;
```

If the first UPDATE succeeds but the second fails, money disappears. Transactions prevent this.

### ACID Properties

Every database transaction should be:

**Atomicity:** All or nothing. If any part fails, the entire transaction rolls back.

**Consistency:** The database moves from one valid state to another. Constraints are always satisfied.

**Isolation:** Concurrent transactions don't interfere with each other.

**Durability:** Once committed, changes survive system failures.

### Transaction Syntax

```sql
START TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

-- Everything worked
COMMIT;

-- OR if something went wrong
ROLLBACK;
```

### In Kailua Context

Creating a rental involves multiple operations:
1. Insert contract record
2. Mark car as unavailable
3. Record initial payment

These should either all succeed or all fail:

```sql
START TRANSACTION;

INSERT INTO rental_contracts (customer_id, car_id, start_date, end_date)
VALUES (1, 5, '2024-03-01', '2024-03-08');

UPDATE cars SET available = false WHERE car_id = 5;

INSERT INTO payments (contract_id, amount, payment_date)
VALUES (LAST_INSERT_ID(), 3500, CURRENT_DATE);

COMMIT;
```

### Transactions in Java

When you start working with JdbcTemplate, Spring handles transactions:

```java
@Transactional
public void createRentalWithPayment(RentalRequest request) {
    // Both operations are in one transaction
    contractRepository.save(contract);
    paymentRepository.save(payment);
    // If either fails, both roll back
}
```

The `@Transactional` annotation gives you ACID guarantees - but you need to understand the concept to use it effectively.

---

## Database Administration Concepts

### Understanding the Big Picture

Database administration (DBA) topics are covered at **awareness level** - you should understand *why* these concepts matter, not memorize complex implementation details.

### User Management: Why It Matters

In development, you might use a root account. In production, this is dangerous:
- Root has unlimited access - any bug or hack affects everything
- You can't track who did what
- No principle of least privilege

**The principle:** Each application should have a database user with only the permissions it needs.

```sql
-- Create a user for the Kailua application
CREATE USER 'kailua_app'@'localhost' IDENTIFIED BY 'secure_password';

-- Grant only what it needs
GRANT SELECT, INSERT, UPDATE ON kailua.customers TO 'kailua_app'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON kailua.rental_contracts TO 'kailua_app'@'localhost';
GRANT SELECT ON kailua.cars TO 'kailua_app'@'localhost';  -- Read-only for cars table

-- Apply changes
FLUSH PRIVILEGES;
```

**Key commands:**
- `GRANT`: Give permissions
- `REVOKE`: Remove permissions
- `SHOW GRANTS FOR 'user'@'host'`: See what a user can do

### Roles: Grouping Permissions

Instead of granting permissions to each user individually:

```sql
-- Create a role for rental clerks
CREATE ROLE 'rental_clerk';
GRANT SELECT, INSERT ON kailua.rental_contracts TO 'rental_clerk';
GRANT SELECT ON kailua.customers TO 'rental_clerk';
GRANT SELECT ON kailua.cars TO 'rental_clerk';

-- Assign role to users
GRANT 'rental_clerk' TO 'employee1'@'localhost';
GRANT 'rental_clerk' TO 'employee2'@'localhost';
```

### Backup and Restore: Why It Matters

Data is valuable. Without backups:
- Hardware failures destroy everything
- Accidental `DELETE FROM table` is permanent
- Ransomware attacks win

**Backup strategies:**
- **Full backup:** Copy entire database (simple, but large and slow)
- **Incremental backup:** Copy only changes since last backup (faster, but more complex to restore)
- **Point-in-time recovery:** Restore to any moment (requires transaction logs)

**mysqldump basics (for awareness):**
```bash
# Export database to file
mysqldump -u root -p kailua > kailua_backup.sql

# Restore from backup
mysql -u root -p kailua < kailua_backup.sql
```

### What Examiners Want to Hear

For admin topics, focus on **why** over **how**:

"We created a separate database user for our Kailua application with only SELECT and INSERT privileges on relevant tables. This follows the principle of least privilege - if the application is compromised, the attacker can't DROP tables or access other databases."

"Before deploying to production, we'd implement a backup strategy. Full backups weekly, with incremental backups daily, so we could recover to any point in time if something goes wrong."

---

## Integration Patterns

### How Advanced SQL Fits in the Stack

```
[Browser]
    |
    | HTTP Request
    v
[@Controller]
    |
    | Calls service
    v
[@Service with @Transactional]
    |
    | Transaction boundary
    v
[@Repository]
    |
    | Simple query (thanks to views)
    | Or procedure call
    v
[MySQL]
    |
    +-- Views: Simplify complex JOINs
    +-- Stored Procedures: Encapsulate business logic
    +-- Triggers: Automatic validation/auditing
    +-- User Privileges: Security layer
```

### Pattern: View Simplifies Repository

**Without view:**
```java
public List<RentalDetails> findActiveRentals() {
    String sql = "SELECT rc.contract_id, c.first_name, c.last_name, " +
                 "car.brand, car.model, rc.start_date, rc.end_date " +
                 "FROM rental_contracts rc " +
                 "INNER JOIN customers c ON rc.customer_id = c.customer_id " +
                 "INNER JOIN cars car ON rc.car_id = car.car_id " +
                 "WHERE rc.end_date >= CURRENT_DATE";
    return jdbcTemplate.query(sql, rentalDetailsRowMapper);
}
```

**With view:**
```java
public List<RentalDetails> findActiveRentals() {
    String sql = "SELECT * FROM active_rentals";
    return jdbcTemplate.query(sql, rentalDetailsRowMapper);
}
```

### Pattern: Stored Procedure for Complex Operations

When an operation involves multiple tables and validation:

```java
public void processReturn(int contractId, int returnMileage) {
    // Procedure handles: update contract, mark car available, calculate final price
    jdbcTemplate.update("CALL process_return(?, ?)", contractId, returnMileage);
}
```

The procedure encapsulates:
1. Update contract status
2. Mark car as available
3. Record final mileage
4. Calculate any additional charges

### Pattern: Trigger for Audit Trail

Your Java code doesn't need to explicitly log changes:

```sql
CREATE TRIGGER audit_price_changes
AFTER UPDATE ON cars
FOR EACH ROW
BEGIN
    IF OLD.price_per_day <> NEW.price_per_day THEN
        INSERT INTO audit_log (table_name, record_id, field_name, old_value, new_value, changed_at)
        VALUES ('cars', NEW.car_id, 'price_per_day', OLD.price_per_day, NEW.price_per_day, NOW());
    END IF;
END
```

Now every price change is automatically logged, regardless of which application made the change.

---

## Common Struggles and How to Overcome Them

### Struggle 1: Correlated vs Non-Correlated Subqueries

**Why this confuses students:** Both are "queries inside queries" - the distinction seems academic.

**How to think about it:** Ask: "Can I copy the inner query and run it alone?"
- **Yes:** Non-correlated. The inner query is independent.
- **No (it references the outer query):** Correlated. It needs context from each outer row.

**Visual test:** Look for outer table aliases in the inner query.

```sql
-- Non-correlated: No reference to 'c' in subquery
SELECT * FROM cars c WHERE price_per_day > (SELECT AVG(price_per_day) FROM cars);

-- Correlated: 'c.category' references outer query
SELECT * FROM cars c WHERE price_per_day > (
    SELECT AVG(price_per_day) FROM cars c2 WHERE c2.category = c.category
);
```

**Exam tip:** "The subquery references the outer query's table, so it's correlated. This means it executes once for each row in the outer query, which has performance implications for large tables."

### Struggle 2: When to Use Views vs Stored Procedures

**Why this confuses students:** Both "hide complexity" - when do you choose which?

**Decision framework:**

| Use a View when... | Use a Procedure when... |
|--------------------|------------------------|
| You need to simplify a SELECT | You need to modify data |
| You want to restrict column access | You need control flow (IF, loops) |
| You want a reusable "table" | You need to return multiple result sets |
| The operation is read-only | You need output parameters |

**Exam tip:** "I used a view for the rental summary because it's read-only data retrieval - we're just simplifying a complex JOIN. For creating rentals, I'd use a stored procedure because it needs to insert into multiple tables and includes business logic for calculating prices."

### Struggle 3: Trigger Execution Order

**Why this confuses students:** With multiple triggers, which runs first?

**Key rules:**
1. BEFORE triggers run before the operation
2. AFTER triggers run after the operation
3. Multiple triggers of the same type/event: MySQL doesn't guarantee order (avoid depending on order)

**Practical advice:** Keep triggers simple and independent. If you need specific ordering, combine logic into one trigger.

### Struggle 4: Understanding ACID Properties

**Why this confuses students:** The properties seem abstract until you encounter failures.

**Make it concrete:**

- **Atomicity:** "If my INSERT succeeds but the UPDATE fails, I want both to roll back."
- **Consistency:** "After my transaction, all constraints should still be valid."
- **Isolation:** "If two customers try to rent the last car simultaneously, one should get it, one should fail - not both succeed."
- **Durability:** "Once I see 'COMMIT successful,' the data is safe even if the server crashes."

**Exam tip:** "ACID properties ensure that our rental transaction - inserting the contract AND marking the car unavailable - either both happen or neither happens. This prevents situations where a car is rented twice."

### Struggle 5: Admin Topics Depth

**Why this confuses students:** How deep should I go?

**The answer:** Awareness level. Understand *why*, not detailed *how*.

**What to know:**
- Why separate database users matter (security principle of least privilege)
- Why backups matter (disaster recovery)
- That roles simplify permission management
- That GRANT/REVOKE control access

**What NOT to memorize:**
- Complex GRANT syntax for specific privileges
- Detailed backup scheduling commands
- MySQL server configuration parameters

---

## Practice Exercises

### Exercise 1: Subqueries (Maximum Guidance)

**What you'll build:** Queries using both correlated and non-correlated subqueries.

**Step-by-step approach:**

1. Write a non-correlated subquery to find cars priced above average:
   ```sql
   SELECT * FROM cars
   WHERE price_per_day > (SELECT AVG(price_per_day) FROM cars);
   ```

2. Write a non-correlated subquery with IN to find customers who have rented:
   ```sql
   SELECT * FROM customers
   WHERE customer_id IN (SELECT DISTINCT customer_id FROM rental_contracts);
   ```

3. Write a correlated subquery to find customers with more than 3 rentals:
   ```sql
   SELECT * FROM customers c
   WHERE (SELECT COUNT(*) FROM rental_contracts rc
          WHERE rc.customer_id = c.customer_id) > 3;
   ```

4. Use NOT EXISTS to find cars never rented:
   ```sql
   SELECT * FROM cars c
   WHERE NOT EXISTS (
       SELECT 1 FROM rental_contracts rc WHERE rc.car_id = c.car_id
   );
   ```

**What success looks like:** You can identify whether a subquery is correlated or non-correlated.

---

### Exercise 2: Views for Kailua (Moderate Guidance)

**What you'll build:** Views that simplify common queries in the rental system.

**Requirements:**
Create views for:

1. **customer_rental_summary:** Customer name, total rentals, total spent
2. **available_cars_by_category:** Available cars grouped by category with count
3. **overdue_rentals:** Contracts where end_date has passed but status is still 'active'

**Key concepts to apply:**
- JOINs within view definitions
- Aggregate functions in views
- Date comparisons with CURRENT_DATE

---

### Exercise 3: Stored Procedure (Minimal Guidance)

**What you'll build:** A procedure to process a car return.

**Requirements:**
Create `process_car_return` procedure that:
1. Takes contract_id and final_mileage as inputs
2. Updates the contract status to 'completed'
3. Updates the car's mileage
4. Marks the car as available
5. Returns the total_price as an output parameter

**Skills you'll practice:**
- Procedure creation with IN and OUT parameters
- Multiple SQL statements in a procedure
- Variable declaration and assignment

---

## Preparing for the Oral Exam

### Key Questions You Should Be Able to Answer

- "What's the difference between a correlated and non-correlated subquery?"
- "When would you use a view instead of just writing the query?"
- "Why would you put business logic in a stored procedure instead of Java?"
- "Explain ACID properties with an example from your project."
- "Why is user management important in a production database?"

### Demo Tips

When demonstrating advanced SQL in your project:

1. **Show a view:** "This view simplifies our rental summary query. Instead of writing this JOIN every time..."
2. **Trace to Java:** "In our repository, we simply SELECT from this view."
3. **Explain the architectural decision:** "We chose a view here because it's read-only. For creating rentals, we use a procedure because it involves multiple tables."

### What NOT to Do

- Don't memorize GRANT/REVOKE syntax without understanding why user management matters
- Don't skip the correlated vs non-correlated distinction - it's a common exam question
- Don't forget to connect concepts to your project

### What TO Do

- Explain *why* you would use each feature
- Give concrete examples from Kailua or Onskeskyen
- Discuss trade-offs (Java logic vs database logic)
- Show understanding of ACID properties with practical scenarios

---

## Looking Ahead

### What You Can Do Now

- Write complex subqueries (both correlated and non-correlated)
- Create views to simplify data access and enhance security
- Develop stored procedures for reusable database logic
- Implement triggers for automatic data validation
- Explain ACID properties and why transactions matter
- Understand user privileges and backup strategies (conceptual level)

### How This Will Be Used in Upcoming Topics

- **Database-Java Integration (Next):** Views simplify your JdbcTemplate queries. Stored procedures can be called from Java. Transaction annotations build on your ACID understanding.

- **Spring Boot Web Applications:** The layered architecture (Controller -> Service -> Repository -> Database) relies on these database features working correctly.

- **Onskeskyen Project:** Views for wishlist summaries. Triggers for maintaining item counts. User management for production deployment.

### Project Connection

**Kailua Car Rental:**
- Views for common reports (available cars, rental history)
- Stored procedures for complex operations (create rental, process return)
- Triggers for data validation (rental dates, mileage)
- Understanding transactions for multi-table operations

**Onskeskyen Wishlist:**
- Views for user's complete wishlist with items
- Triggers for updating item counts automatically
- User management for production deployment

---

## Key Takeaways

- **Subqueries enable step-by-step problem solving.** Non-correlated run once; correlated run per row.

- **Views are saved queries that act like tables.** Use for simplification, security, and abstraction.

- **Stored procedures encapsulate database logic.** Like Java methods, but running on the database server.

- **Triggers automate data validation and auditing.** They run automatically on data changes.

- **ACID properties ensure transaction reliability.** All-or-nothing operations protect data integrity.

- **Admin topics are awareness-level.** Understand *why* user management and backups matter, not detailed syntax.

**For the exam:** Be able to explain when to use views vs procedures, identify correlated vs non-correlated subqueries, and connect these concepts to your project's architecture.

---

## For the Next Topic Agent

### Terminology Established This Topic

- **Subquery:** A SELECT statement nested inside another SQL statement. Two types: non-correlated (independent, runs once) and correlated (references outer query, runs per row).

- **EXISTS/IN Operators:** Set membership operators. IN checks against a list of values; EXISTS checks if any rows exist.

- **View:** A named SELECT query stored in the database. Acts like a virtual table. Used for simplification, security (column hiding), and abstraction.

- **WITH CHECK OPTION:** View constraint preventing inserts/updates that would create rows invisible to the view.

- **Stored Procedure:** Reusable database program with parameters. Can contain control flow (IF, loops) and modify data. Called with CALL statement.

- **Function:** Reusable database program that returns a single value. Used in SELECT, WHERE clauses.

- **Trigger:** Automatic code that executes on INSERT, UPDATE, or DELETE. Timing: BEFORE or AFTER. References: NEW (post-change data) and OLD (pre-change data).

- **ACID Properties:** Transaction guarantees. Atomicity (all-or-nothing), Consistency (valid states only), Isolation (concurrent transactions don't interfere), Durability (committed data survives failures).

- **GRANT/REVOKE:** Commands for managing user privileges on database objects.

### Example Classes/Concepts Created

- **Kailua View Patterns:** available_cars_detail (filters), active_rentals (JOINed data), rental_statistics (aggregates)

- **Subquery Decision Pattern:**
  - Need aggregate comparison? Use non-correlated subquery
  - Need "exists" check? Use correlated with EXISTS
  - Can reference outer query? Correlated. Independent? Non-correlated.

- **View vs Procedure Decision:**
  - Read-only data access? View
  - Multiple operations with business logic? Procedure

- **Trigger Use Cases:**
  - Data validation (BEFORE INSERT/UPDATE)
  - Audit logging (AFTER UPDATE)
  - Cascading updates (AFTER UPDATE)

### Student Capabilities After This Topic

Students who complete this material can now:
- Write and identify correlated vs non-correlated subqueries
- Create views for data abstraction and security
- Develop stored procedures with parameters and control flow
- Implement triggers for validation and auditing
- Explain ACID properties with concrete examples
- Understand database user management and backup concepts
- Make architectural decisions about Java vs database logic
- Connect advanced SQL features to application architecture

### Pedagogical Patterns Used

- **Correlated/Non-Correlated Visual Test:** "Can you run the inner query alone?" as diagnostic question

- **Architecture Decision Framework:** Tables comparing when to use views vs procedures, IN vs EXISTS

- **Java Method Analogy:** Stored procedures as "database methods" leveraging 1st semester knowledge

- **Business Scenario Grounding:** Bank transfer problem for ACID, Kailua rentals for triggers

- **Awareness vs Deep Knowledge:** Explicit framing that admin topics require understanding "why" not "how"

- **Exam Question Anticipation:** "What examiners want to hear" sections for admin topics

- **Trade-off Discussion:** Java logic vs database logic presented as architectural decision, not right/wrong
