# GRASP Design Principles in Spring Boot - 2nd Semester Programming

*Prerequisites: Spring Boot & Web Development Fundamentals, Sessions/IoC/DI (all prior 2nd semester topics)*
*Phase: Cross-cutting (Phases 3, 5, 6, 7) - Applied throughout Spring Boot development*
*Exam Weight: MODERATE-HIGH - Students must evaluate program quality and articulate design decisions*

---

## What You'll Learn

By the end of this topic, you will be able to:
- **Identify GRASP principles** in your existing Spring Boot code
- **Articulate design decisions** using GRASP vocabulary (critical for oral exam)
- **Connect abstract principles** to concrete Spring Boot implementations
- **Evaluate code quality** by recognizing GRASP violations and proper implementations
- **Justify architectural choices** in your Onskeskyen project using design principles
- **Explain "why"** certain designs are better, not just "what" they are

This topic bridges theory and practice. You learned GRASP in Systems Development last semester as abstract concepts. Now you'll see that you've been implementing these principles all along in Spring Boot - you just didn't have the vocabulary to describe it.

---

## Why This Matters

### The Exam Reality

The exam learning outcome explicitly states: **"Evaluate program quality according to GRASP design principles."**

This means examiners will ask questions like:
- "Which GRASP principle does your Repository class implement?"
- "Why did you create a separate Service layer?"
- "How does @Autowired relate to design principles?"

If you can't answer these questions confidently, you're missing points on a moderate-to-high emphasis exam topic.

### The Gap Between Theory and Practice

In 1st semester Systems Development, GRASP was presented theoretically:
- "High Cohesion means classes should have focused responsibilities"
- "Low Coupling means minimizing dependencies"

But how do you actually achieve these in code? What does "focused responsibility" look like in a real Spring Boot application?

**This topic closes that gap.** You'll learn that your `@Controller`, `@Service`, and `@Repository` classes aren't just Spring conventions - they're implementations of specific GRASP principles.

### Professional Communication

Senior developers and architects use GRASP vocabulary daily:
- "That class has too many responsibilities - violates High Cohesion"
- "Using interfaces here gives us Low Coupling for testing"
- "The Repository is the Information Expert for data access"

Understanding GRASP helps you communicate professionally about code quality.

---

## The Nine GRASP Principles

GRASP (General Responsibility Assignment Software Patterns) consists of nine principles for assigning responsibilities to classes. Let's examine each one through the lens of Spring Boot.

---

## Principle 1: Information Expert

### The Concept

**Assign responsibility to the class that has the information needed to fulfill it.**

The class that "knows" the most about something should handle operations related to it. Don't ask another class to do something when you already have the information yourself.

### In Spring Boot: The Repository Pattern

Your `@Repository` classes are the canonical example of Information Expert. They have expertise about:
- Database connections
- SQL syntax
- Table structures
- How to map rows to objects

**Why Repository is Information Expert:**

The Repository knows how to connect to the database, how to write SQL queries, and how to convert `ResultSet` data into Java objects. When the Service needs data, it doesn't write SQL itself - it asks the expert.

```java
@Repository
public class WishlistRepository {
    private final JdbcTemplate jdbcTemplate;

    // Repository has the information needed for data access
    public List<Wishlist> findByUserId(int userId) {
        String sql = "SELECT * FROM wishlists WHERE user_id = ?";
        return jdbcTemplate.query(sql, new WishlistRowMapper(), userId);
    }
}
```

**The Service doesn't know SQL.** It doesn't know about JdbcTemplate, RowMappers, or database connections. It only knows that it can ask the Repository for wishlists.

### Violation Example: SQL in the Service

```java
// BAD - Service pretending to be the expert
@Service
public class WishlistService {
    @Autowired
    private JdbcTemplate jdbcTemplate;  // Service shouldn't know about this!

    public List<Wishlist> findByUserId(int userId) {
        String sql = "SELECT * FROM wishlists WHERE user_id = ?";
        return jdbcTemplate.query(sql, mapper, userId);  // Wrong layer
    }
}
```

This violates Information Expert. The Service doesn't have expertise about database access - it's forcing itself to know things it shouldn't.

### Why This Matters for Your Project

In Onskeskyen, ask yourself: "Who is the expert?"

| Operation | Expert | Reasoning |
|-----------|--------|-----------|
| Get wishlist from database | WishlistRepository | Has database connection knowledge |
| Apply business rules to wishlist | WishlistService | Knows business logic |
| Decide which template to render | WishlistController | Knows about HTTP/web flow |
| Convert ResultSet to Wishlist object | WishlistRowMapper | Expert at object mapping |

---

## Principle 2: High Cohesion

### The Concept

**Classes should have focused, well-defined responsibilities. Each class should do one thing well.**

A highly cohesive class has methods that are strongly related to each other. They work toward a common purpose. A class with low cohesion is a "jack of all trades" - it does many unrelated things.

### In Spring Boot: Layered Architecture

Spring Boot's layered architecture enforces High Cohesion through separation:

**Controller Layer (HTTP handling cohesion):**
- Receives HTTP requests
- Extracts parameters
- Calls services
- Returns view names or redirects

**Service Layer (business logic cohesion):**
- Implements business rules
- Coordinates between repositories
- Handles transactions
- Contains validation logic

**Repository Layer (data access cohesion):**
- Executes SQL queries
- Maps results to objects
- Handles database connections

Each layer has one clear responsibility. They don't leak into each other's domains.

### Visualizing Cohesion

```
+----------------------------------+
|       WishlistController         |
|----------------------------------|
| - showWishlists()   <-- HTTP     |
| - createWishlist()  <-- HTTP     |
| - deleteWishlist()  <-- HTTP     |
|                                  |
| All methods: HTTP request/response|
+----------------------------------+

+----------------------------------+
|        WishlistService           |
|----------------------------------|
| - getAllByUser()    <-- Business |
| - create()          <-- Business |
| - validateName()    <-- Business |
|                                  |
| All methods: Business logic      |
+----------------------------------+

+----------------------------------+
|       WishlistRepository         |
|----------------------------------|
| - findByUserId()    <-- Data     |
| - save()            <-- Data     |
| - delete()          <-- Data     |
|                                  |
| All methods: Data access         |
+----------------------------------+
```

### Violation Example: The "God Controller"

```java
// BAD - Low Cohesion "God Controller"
@Controller
public class WishlistController {
    @Autowired
    private JdbcTemplate jdbcTemplate;  // Why is controller doing data access?

    @GetMapping("/wishlists")
    public String showWishlists(Model model) {
        // HTTP handling (correct)
        // But also...

        // Data access (wrong layer!)
        String sql = "SELECT * FROM wishlists";
        List<Wishlist> wishlists = jdbcTemplate.query(sql, mapper);

        // Business logic (wrong layer!)
        for (Wishlist w : wishlists) {
            if (w.getItems().size() > 100) {
                w.setWarning("Too many items!");
            }
        }

        model.addAttribute("wishlists", wishlists);
        return "wishlist-list";
    }
}
```

This controller handles HTTP, data access, AND business logic. It has low cohesion - its methods serve multiple unrelated purposes.

### The Proper Implementation

```java
// GOOD - High Cohesion through layering
@Controller
public class WishlistController {
    private final WishlistService wishlistService;

    @GetMapping("/wishlists")
    public String showWishlists(HttpSession session, Model model) {
        User user = (User) session.getAttribute("currentUser");
        if (user == null) return "redirect:/login";

        // Controller only handles HTTP - delegates business logic
        List<Wishlist> wishlists = wishlistService.findByUserId(user.getUserId());
        model.addAttribute("wishlists", wishlists);
        return "wishlist-list";
    }
}
```

The controller is now cohesive - every method deals with HTTP request/response handling.

---

## Principle 3: Low Coupling

### The Concept

**Minimize dependencies between components. Changes in one class should not require changes in many others.**

Coupling is the degree to which one component depends on another. Tight coupling means changing Class A forces changes in Classes B, C, and D. Loose coupling means components can change independently.

### In Spring Boot: Dependency Injection

This is where your IoC/DI knowledge from the previous topic pays off. **Dependency Injection is the primary mechanism for achieving Low Coupling in Spring Boot.**

**Without DI (High Coupling):**
```java
public class WishlistController {
    // Controller creates its own dependencies
    private WishlistService service = new WishlistService(
        new WishlistRepository(
            new JdbcTemplate(dataSource)
        )
    );
}
```

The controller is tightly coupled to:
- `WishlistService` concrete class
- `WishlistRepository` concrete class
- `JdbcTemplate` class
- `DataSource` configuration

Change how the repository is configured? Update the controller. Change the service implementation? Update the controller. This is a maintenance nightmare.

**With DI (Low Coupling):**
```java
@Controller
public class WishlistController {
    private final WishlistService wishlistService;

    // Spring provides the dependency - controller doesn't know how it's created
    public WishlistController(WishlistService wishlistService) {
        this.wishlistService = wishlistService;
    }
}
```

The controller only knows it needs "something that acts like a WishlistService." It doesn't know:
- How the service is created
- What dependencies the service has
- Whether it's the real service or a mock

### The @Autowired Connection

When you learned `@Autowired` in the previous topic, you learned it "injects dependencies." Now you understand the design principle behind it: **@Autowired achieves Low Coupling by inverting dependency creation.**

```java
@Service
public class WishlistService {
    @Autowired  // Low Coupling - Spring provides the repository
    private WishlistRepository repository;

    // Service doesn't create the repository
    // Service doesn't know how repository connects to database
    // Service only knows the repository interface
}
```

### Why Low Coupling Enables Testing

The testability benefit from the previous topic is actually a Low Coupling benefit:

```java
// Because WishlistService has low coupling...
// We can inject a mock repository for testing
WishlistRepository mockRepo = mock(WishlistRepository.class);
when(mockRepo.findByUserId(1)).thenReturn(testWishlists);

WishlistService service = new WishlistService(mockRepo);
// Test service without a real database!
```

If the service was tightly coupled (using `new WishlistRepository()`), we couldn't substitute the mock.

---

## Principle 4: Controller (GRASP Controller)

### The Concept

**A controller is a coordinating object that receives system events and delegates work to other objects.**

The GRASP Controller doesn't contain business logic itself. It coordinates - receiving requests, delegating to appropriate objects, and returning results.

### In Spring Boot: @Controller Classes

Your `@Controller` classes implement the GRASP Controller pattern directly. The naming is not a coincidence.

**The Controller's Job:**
1. Receive the HTTP request
2. Extract necessary parameters
3. Check authorization (session)
4. Delegate to the appropriate service
5. Add results to the model
6. Return the view name

**What the Controller Does NOT Do:**
- Business logic calculations
- Direct database access
- Complex data transformations

```java
@Controller
public class ItemController {
    private final ItemService itemService;

    @GetMapping("/items")
    public String listItems(HttpSession session, Model model) {
        // 1. Check authorization
        User user = (User) session.getAttribute("currentUser");
        if (user == null) return "redirect:/login";

        // 2. Delegate to service
        List<Item> items = itemService.findByUser(user);

        // 3. Prepare response
        model.addAttribute("items", items);
        return "item-list";
    }
}
```

Notice the controller doesn't know:
- How items are stored
- What SQL retrieves them
- What business rules apply

It coordinates the flow, trusting each layer to do its job.

### Controller vs. Service Responsibility

A common question: "Where does this logic belong?"

| Put in Controller | Put in Service |
|-------------------|----------------|
| Session checks | Business validation |
| Request parameter extraction | Data processing |
| Redirect decisions | Calculations |
| Model population | Multi-repository coordination |
| View name returns | Transaction handling |

**Rule of thumb:** If it requires domain knowledge or business rules, it belongs in the Service.

---

## Principle 5: Creator

### The Concept

**Assign responsibility for creating objects to a class that aggregates, contains, or closely uses those objects.**

Who should create a new object? The class that:
- Contains the object (composition)
- Aggregates the object (collection)
- Closely uses the object
- Has the initialization data

### In Spring Boot: The IoC Container as Creator

In traditional Java, you decide which class creates objects:

```java
// Traditional: Service creates Repository
public class WishlistService {
    private WishlistRepository repo = new WishlistRepository();
}
```

But in Spring Boot, the **IoC Container is the Creator**. It creates all `@Component`, `@Service`, `@Repository`, and `@Controller` objects.

**Why Spring is the Creator:**
- Spring has the configuration data (application.properties)
- Spring knows the dependency graph
- Spring manages the lifecycle
- Spring can optimize creation (singleton beans)

```java
@Service  // Spring creates this
public class WishlistService {
    private final WishlistRepository repository;

    // Spring injects the repository it created
    public WishlistService(WishlistRepository repository) {
        this.repository = repository;
    }
}
```

**You still create domain objects.** Spring creates infrastructure objects (controllers, services, repositories). Your code creates domain objects:

```java
@PostMapping("/wishlists")
public String createWishlist(@RequestParam String name, HttpSession session) {
    User user = (User) session.getAttribute("currentUser");

    // You create domain objects - you have the data
    Wishlist wishlist = new Wishlist(name, user.getUserId());

    // Spring-created service saves it
    wishlistService.create(wishlist);

    return "redirect:/wishlists";
}
```

The controller creates the `Wishlist` object because it has the necessary data (name from form, userId from session).

---

## Principle 6: Pure Fabrication

### The Concept

**Create a class that doesn't represent a domain concept but provides needed services.**

Sometimes no domain class is the natural home for certain functionality. Rather than forcing it into an existing class (violating cohesion), create a new class specifically for that purpose.

### In Spring Boot: The Service Layer

The Service layer is the prime example of Pure Fabrication.

**What is a "domain concept"?**
- Wishlist (a real thing users create)
- Item (a real thing on a wishlist)
- User (a real person)

**What is NOT a domain concept?**
- WishlistService (not a real "thing")
- UserService (not a physical entity)

Your Service classes don't represent anything in the real world. You can't touch a "WishlistService." It's a fabrication - a convenient class created purely for code organization.

```java
@Service  // Pure Fabrication - exists for code organization, not domain modeling
public class WishlistService {
    private final WishlistRepository wishlistRepository;
    private final ItemRepository itemRepository;

    public List<Wishlist> findByUserWithItems(int userId) {
        List<Wishlist> wishlists = wishlistRepository.findByUserId(userId);
        for (Wishlist w : wishlists) {
            List<Item> items = itemRepository.findByWishlistId(w.getId());
            w.setItems(items);
        }
        return wishlists;
    }
}
```

**Why Pure Fabrication is Valuable:**

Without the Service layer, where would this logic go?
- In the Controller? Violates cohesion (controller shouldn't do business logic)
- In the Repository? Violates cohesion (repository should only do data access)
- In the Wishlist class? Couples Wishlist to multiple repositories

The Service is "fabricated" to give this logic a proper home.

### Pure Fabrication vs. Domain Objects

| Domain Object | Pure Fabrication |
|---------------|------------------|
| Represents real-world thing | Exists for technical convenience |
| Has meaningful state | Primarily has behavior |
| Examples: Wishlist, User, Item | Examples: WishlistService, EmailSender, Validator |
| Created by your code | Created by Spring |

---

## Principle 7: Polymorphism

### The Concept

**Use polymorphism to handle alternative behaviors based on type, instead of using conditional logic.**

Rather than writing `if/else` statements to handle different cases, define a common interface and let different implementations handle the variation.

### In Spring Boot: Programming to Interfaces

You've applied this principle since 1st semester with Collections:

```java
List<String> names = new ArrayList<>();  // Polymorphism
```

You use `List` (interface) instead of `ArrayList` (implementation). If you later need `LinkedList`, only the creation changes.

In Spring Boot, the same principle applies to your own code:

```java
// Interface defines the contract
public interface NotificationService {
    void notify(User user, String message);
}

// Email implementation
@Service
@Primary
public class EmailNotificationService implements NotificationService {
    public void notify(User user, String message) {
        // Send email
    }
}

// SMS implementation (for future use)
@Service
public class SmsNotificationService implements NotificationService {
    public void notify(User user, String message) {
        // Send SMS
    }
}
```

The WishlistService uses the interface:

```java
@Service
public class WishlistService {
    private final NotificationService notificationService;

    public void shareWishlist(Wishlist wishlist, User recipient) {
        // Doesn't know if it's email or SMS - polymorphism!
        notificationService.notify(recipient, "A wishlist was shared with you");
    }
}
```

### Why Polymorphism Matters

**Without polymorphism (bad):**
```java
public void notify(User user, String message, String method) {
    if (method.equals("email")) {
        // Send email
    } else if (method.equals("sms")) {
        // Send SMS
    } else if (method.equals("push")) {
        // Send push notification
    }
    // Every new notification type = modify this method
}
```

**With polymorphism (good):**
```java
public void notify(User user, String message) {
    notificationService.notify(user, message);  // Polymorphic call
}
// Add new notification type = add new class, no changes here
```

---

## Principle 8: Indirection

### The Concept

**Introduce an intermediate object between components to reduce direct coupling.**

Instead of A calling B directly, A calls C which calls B. This indirection allows A and B to evolve independently.

### In Spring Boot: The Service Layer (Again)

The Service layer provides indirection between Controller and Repository:

```
Without Indirection:
Controller ---------> Repository

With Indirection:
Controller --> Service --> Repository
```

**Why this matters:**

If the Controller called the Repository directly:
- Controller knows about data access details
- Changing database logic affects controllers
- No place for business rules between "receive request" and "get data"

With the Service as indirection:
- Controller only knows about services
- Service handles business logic and repository coordination
- Repository changes don't affect controllers

**The Service as a Buffer:**

```java
@Controller
public class WishlistController {
    private final WishlistService service;  // Knows service, not repository

    @GetMapping("/wishlists/{id}")
    public String viewWishlist(@PathVariable int id, Model model) {
        Wishlist wishlist = service.findById(id);  // Indirect data access
        model.addAttribute("wishlist", wishlist);
        return "wishlist-detail";
    }
}

@Service
public class WishlistService {
    private final WishlistRepository repo;
    private final ItemRepository itemRepo;  // Multiple repos coordinated here

    public Wishlist findById(int id) {
        Wishlist wishlist = repo.findById(id);
        wishlist.setItems(itemRepo.findByWishlistId(id));
        return wishlist;  // Business logic (loading items) hidden from controller
    }
}
```

The controller doesn't know that loading a wishlist involves two repositories. That complexity is hidden behind the service indirection.

---

## Principle 9: Protected Variations

### The Concept

**Shield components from variations in other components by using interfaces and abstraction.**

When you know something might change, wrap it behind an interface. Components that depend on the interface are protected from implementation changes.

### In Spring Boot: Interface-Based Design

Protected Variations is the architectural reason for programming to interfaces:

```java
public interface WishlistRepository {
    List<Wishlist> findByUserId(int userId);
    void save(Wishlist wishlist);
    void delete(int id);
}
```

The Service depends on this interface:

```java
@Service
public class WishlistService {
    private final WishlistRepository repository;  // Interface type

    // Protected from changes in how wishlists are stored
}
```

**What variations are we protecting against?**

| Potential Change | Service Impact |
|------------------|----------------|
| Switch from MySQL to PostgreSQL | None - same interface |
| Change SQL queries | None - service doesn't see SQL |
| Add caching to repository | None - caching inside implementation |
| Switch to NoSQL | None - implement same interface |
| Mock for testing | None - inject mock implementation |

The service is "protected" from all these variations because it only knows the interface contract, not the implementation details.

---

## Complete GRASP-Spring Boot Mapping

This table is exam-critical. Be able to explain each mapping:

| GRASP Principle | Spring Boot Implementation | Your Project Application |
|-----------------|---------------------------|--------------------------|
| **Information Expert** | `@Repository` - has database expertise | WishlistRepository handles all SQL for wishlists |
| **High Cohesion** | Layered architecture (Controller/Service/Repository) | Each package has single responsibility |
| **Low Coupling** | `@Autowired` dependency injection | Components don't create their dependencies |
| **Controller** | `@Controller` classes | WishlistController delegates to services |
| **Creator** | Spring IoC Container | Spring creates all @Component beans |
| **Pure Fabrication** | `@Service` layer | WishlistService provides business logic home |
| **Polymorphism** | Interface-based design (`List`, not `ArrayList`) | Repository interfaces allow mock testing |
| **Indirection** | Service layer between Controller and Repository | Controller doesn't touch repositories directly |
| **Protected Variations** | Programming to interfaces | Changes in repository don't affect services |

---

## Identifying GRASP Violations

Part of "evaluating program quality" is recognizing violations. Here are patterns to watch for:

### Violation: Business Logic in Controller

```java
// BAD - Controller doing too much
@PostMapping("/wishlists")
public String createWishlist(@RequestParam String name, HttpSession session, Model model) {
    // Business validation in controller - violates High Cohesion
    if (name.length() < 3) {
        model.addAttribute("error", "Name too short");
        return "wishlist-form";
    }
    if (name.length() > 100) {
        model.addAttribute("error", "Name too long");
        return "wishlist-form";
    }
    // ... more business logic ...
}
```

**Fix:** Move validation to service, controller just delegates.

### Violation: Repository Logic in Service

```java
// BAD - Service writing SQL
@Service
public class WishlistService {
    @Autowired
    private JdbcTemplate jdbcTemplate;  // Service shouldn't know about JdbcTemplate

    public List<Wishlist> findByUserId(int userId) {
        String sql = "SELECT * FROM wishlists WHERE user_id = ?";
        // Service shouldn't know SQL - violates Information Expert
    }
}
```

**Fix:** Move SQL to repository, service calls repository method.

### Violation: Direct Repository Access from Controller

```java
// BAD - Skipping the service layer
@Controller
public class WishlistController {
    @Autowired
    private WishlistRepository repository;  // Controller shouldn't use repository directly

    @GetMapping("/wishlists")
    public String listWishlists(Model model) {
        List<Wishlist> wishlists = repository.findAll();  // Missing indirection
    }
}
```

**Fix:** Create service method, controller calls service.

### Violation: Creating Dependencies with 'new'

```java
// BAD - High coupling
@Controller
public class WishlistController {
    private WishlistService service = new WishlistService();  // Tight coupling
}
```

**Fix:** Use constructor injection, let Spring create dependencies.

---

## Tracing GRASP Through a Request

For exam preparation, practice tracing a complete request through your application, identifying GRASP principles at each step:

```
1. User submits "Create Wishlist" form

2. WishlistController receives POST request
   GRASP: Controller pattern (receives system event, coordinates)

3. Controller checks session for logged-in user
   GRASP: Controller pattern (authorization check is system coordination)

4. Controller calls wishlistService.create(wishlist)
   GRASP: Low Coupling (uses injected service, not 'new')
   GRASP: Indirection (doesn't call repository directly)

5. WishlistService validates business rules
   GRASP: Pure Fabrication (service exists for business logic)
   GRASP: High Cohesion (business logic in appropriate layer)

6. WishlistService calls wishlistRepository.save(wishlist)
   GRASP: Low Coupling (service uses injected repository)

7. WishlistRepository executes INSERT SQL
   GRASP: Information Expert (repository has database expertise)

8. Control returns to Controller

9. Controller returns "redirect:/wishlists"
   GRASP: Controller pattern (determines response)
```

---

## Exam Preparation: Key Questions and Answers

### Question 1: "What GRASP principles does your layered architecture implement?"

*"Our layered architecture implements High Cohesion by giving each layer a focused responsibility - controllers handle HTTP, services handle business logic, repositories handle data access. It implements Indirection through the service layer, which sits between controllers and repositories. This achieves Low Coupling because controllers don't depend on repository implementations. The architecture also demonstrates Information Expert, as repositories have the database expertise needed for data access."*

### Question 2: "Explain how @Autowired relates to GRASP principles."

*"@Autowired achieves Low Coupling by removing the need to create dependencies manually. Instead of writing `new WishlistService()` which couples my controller to that specific implementation, I declare the dependency and Spring injects it. This means my controller only knows it needs something providing wishlist operations - it doesn't know how that object is created or configured. Additionally, Spring's IoC container acts as the Creator, centralizing object creation instead of scattering 'new' statements throughout the codebase."*

### Question 3: "Why did you create a Service layer? What GRASP principle justifies it?"

*"The Service layer is a Pure Fabrication. WishlistService doesn't represent a real-world object - you can't touch a 'service.' But it exists to provide a proper home for business logic that doesn't belong in controllers (HTTP handling) or repositories (data access). Without the service layer, business logic would either leak into controllers, violating High Cohesion, or be forced into domain objects, making them complex. The service is 'fabricated' purely for good code organization."*

### Question 4: "How does your Repository implement Information Expert?"

*"The Repository is the Information Expert for data access because it has the necessary information to fulfill that responsibility. It knows how to connect to the database via JdbcTemplate, how to write SQL queries, and how to map ResultSet data to Java objects using RowMapper. The service doesn't have this expertise - it only knows to ask the repository for data. This follows Information Expert: assign responsibility to the class that has the information."*

### Question 5: "Show me Low Coupling in your Onskeskyen project."

*"Looking at my WishlistController, it receives WishlistService through constructor injection. The controller never writes `new WishlistService()`. This achieves Low Coupling because:*
1. *The controller doesn't know how the service is created*
2. *The controller doesn't know what dependencies the service has*
3. *I can change the service implementation without touching the controller*
4. *In tests, I can inject a mock service without a real database*

*The same pattern repeats: service doesn't know how repository is created, repository doesn't know how JdbcTemplate is created. Each layer only knows its immediate dependencies through interfaces."*

### Question 6: "What would happen if you didn't follow GRASP principles?"

*"Without these principles, we'd have a maintenance nightmare:*
- *Without High Cohesion, controllers would contain SQL, business logic, and validation - changing one thing requires understanding everything*
- *Without Low Coupling, changing the database configuration might require updates in dozens of classes*
- *Without Information Expert, SQL would be scattered across services and controllers*
- *Without Indirection, controllers would directly access repositories, making business logic hard to add*

*The project would work initially, but every change would become harder. GRASP principles make code maintainable over time."*

---

## Connecting All Semester Topics Through GRASP

Your entire 2nd semester curriculum implements GRASP:

| Topic | GRASP Connection |
|-------|------------------|
| ADT & Collections | Polymorphism (List interface, not ArrayList implementation) |
| SQL Fundamentals | Information Expert (Repository has database expertise) |
| Database-Java Integration | Information Expert (RowMapper has mapping expertise) |
| Spring Boot MVC | Controller pattern, High Cohesion (layered architecture) |
| Sessions/IoC/DI | Low Coupling (DI), Creator (Spring container) |
| Onskeskyen Project | All principles applied in full-stack application |

---

## Before/After: GRASP Violation vs. Proper Implementation

### Scenario: User Creates a Wishlist

**Before (GRASP Violations):**

```java
@Controller
public class WishlistController {
    // Violation: Controller has database connection (Information Expert)
    private JdbcTemplate jdbcTemplate = new JdbcTemplate(dataSource);

    @PostMapping("/wishlists")
    public String createWishlist(@RequestParam String name, HttpSession session) {
        User user = (User) session.getAttribute("currentUser");

        // Violation: Business logic in controller (High Cohesion)
        if (name == null || name.trim().isEmpty()) {
            return "redirect:/wishlists?error=invalid";
        }
        if (name.length() > 100) {
            name = name.substring(0, 100);
        }

        // Violation: SQL in controller (Information Expert)
        // Violation: Creating own SQL statement (Low Coupling)
        String sql = "INSERT INTO wishlists (name, user_id) VALUES (?, ?)";
        jdbcTemplate.update(sql, name, user.getUserId());

        return "redirect:/wishlists";
    }
}
```

**Problems:**
- Controller has 3 responsibilities: HTTP, business logic, data access
- Tightly coupled to JdbcTemplate and SQL
- Can't test without database
- Business rules hidden in controller
- No service layer (missing indirection)

**After (GRASP Applied):**

```java
// Controller - GRASP Controller pattern
@Controller
public class WishlistController {
    private final WishlistService wishlistService;  // Low Coupling via DI

    public WishlistController(WishlistService wishlistService) {
        this.wishlistService = wishlistService;
    }

    @PostMapping("/wishlists")
    public String createWishlist(@RequestParam String name, HttpSession session) {
        User user = (User) session.getAttribute("currentUser");
        if (user == null) return "redirect:/login";

        // Controller delegates - doesn't do business logic
        wishlistService.createWishlist(name, user.getUserId());
        return "redirect:/wishlists";
    }
}

// Service - Pure Fabrication
@Service
public class WishlistService {
    private final WishlistRepository wishlistRepository;  // Low Coupling

    public WishlistService(WishlistRepository wishlistRepository) {
        this.wishlistRepository = wishlistRepository;
    }

    public void createWishlist(String name, int userId) {
        // Business logic in service - High Cohesion
        String validatedName = validateAndNormalizeName(name);

        Wishlist wishlist = new Wishlist(validatedName, userId);
        wishlistRepository.save(wishlist);  // Delegates to expert
    }

    private String validateAndNormalizeName(String name) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Wishlist name required");
        }
        return name.length() > 100 ? name.substring(0, 100) : name;
    }
}

// Repository - Information Expert
@Repository
public class WishlistRepository {
    private final JdbcTemplate jdbcTemplate;  // Expert has the tools

    public WishlistRepository(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    public void save(Wishlist wishlist) {
        // Information Expert handles SQL
        String sql = "INSERT INTO wishlists (name, user_id) VALUES (?, ?)";
        jdbcTemplate.update(sql, wishlist.getName(), wishlist.getUserId());
    }
}
```

**GRASP Principles Applied:**
- **Controller:** WishlistController coordinates, delegates to service
- **High Cohesion:** Each class has one responsibility
- **Low Coupling:** Dependencies injected, not created
- **Information Expert:** Repository handles SQL
- **Pure Fabrication:** Service provides business logic home
- **Indirection:** Service sits between controller and repository
- **Creator:** Spring creates all components

---

## Key Takeaways

- **GRASP principles are already in your code** - the layered Spring Boot architecture implements them naturally.

- **You must articulate them verbally** - the exam requires explaining "why" using GRASP vocabulary.

- **Information Expert** means assigning work to the class with the expertise - Repositories know databases.

- **High Cohesion** means focused responsibilities - Controllers do HTTP, Services do business logic, Repositories do data access.

- **Low Coupling** means minimizing dependencies - @Autowired injects dependencies instead of using 'new'.

- **Controller pattern** means coordinating without containing logic - delegate to services.

- **Creator** in Spring Boot is the IoC Container - it creates all managed beans.

- **Pure Fabrication** justifies your Service layer - it exists for organization, not domain modeling.

- **Polymorphism** means programming to interfaces - List instead of ArrayList.

- **Indirection** is the Service layer - a buffer between Controller and Repository.

- **Protected Variations** shields components from change - interfaces protect from implementation changes.

- **Practice tracing requests** through your code, naming the GRASP principle at each step.

---

## For the Next Topic Agent

### Terminology Established This Topic

- **GRASP (General Responsibility Assignment Software Patterns):** Nine principles for assigning responsibilities to classes: Information Expert, High Cohesion, Low Coupling, Controller, Creator, Pure Fabrication, Polymorphism, Indirection, Protected Variations.

- **Information Expert:** Assign responsibility to the class that has the information needed to fulfill it. In Spring Boot, Repositories are information experts for data access.

- **High Cohesion:** Classes should have focused, well-defined responsibilities. Achieved in Spring Boot through layered architecture where each layer (Controller, Service, Repository) has a single purpose.

- **Low Coupling:** Minimize dependencies between components. Achieved in Spring Boot through Dependency Injection with @Autowired - components don't create their own dependencies.

- **Controller (GRASP):** A coordinating object that receives system events and delegates work. Maps directly to @Controller classes in Spring MVC.

- **Creator:** The class responsible for creating instances of another class. In Spring Boot, the IoC Container is the primary Creator for managed components.

- **Pure Fabrication:** A class created for design convenience that doesn't represent a domain concept. The @Service layer is Pure Fabrication - services don't represent real-world things.

- **Polymorphism (GRASP):** Handle variations through interfaces rather than conditionals. Applied by programming to interfaces (List, not ArrayList; WishlistRepository interface, not JdbcWishlistRepository).

- **Indirection:** Introduce intermediate objects to reduce direct coupling. The Service layer provides indirection between Controllers and Repositories.

- **Protected Variations:** Shield components from changes by using interfaces. Services depend on Repository interfaces, protecting them from database implementation changes.

### Example Classes/Code Created

- **GRASP-Spring Boot Mapping Table:** Complete table connecting all nine principles to Spring Boot implementations.

- **Before/After Comparison:** Complete code example showing GRASP violations vs. proper implementation for wishlist creation.

- **Request Trace:** Step-by-step trace of a request through the application, naming GRASP principles at each step.

- **GRASP Violation Examples:** Code patterns showing Information Expert violation (SQL in Service), High Cohesion violation (business logic in Controller), Low Coupling violation (using 'new').

### Student Capabilities After This Topic

Students who complete this material can now:
- Identify each GRASP principle in their Spring Boot code
- Articulate why @Service is Pure Fabrication
- Explain why @Repository is Information Expert
- Connect @Autowired to Low Coupling
- Recognize GRASP violations in code
- Trace a request through all layers naming principles
- Answer exam questions about design decisions using GRASP vocabulary
- Evaluate code quality using GRASP principles
- Justify their Onskeskyen architectural choices

### Pedagogical Patterns Used

- **Theory-to-Practice Bridge:** Students learned GRASP abstractly in 1st semester. This topic shows the concrete implementations they've been using.

- **Vocabulary Acquisition:** Heavy emphasis on naming principles - students must articulate design decisions verbally for exam.

- **Before/After Comparison:** Shows GRASP violations vs. proper implementation to make abstract principles concrete.

- **Request Tracing:** Practice identifying principles in the context of a complete request flow.

- **Table-Based Learning:** GRASP-Spring Boot mapping table provides exam-ready reference.

- **Violation Recognition:** Teaching through anti-patterns helps students identify poor code.

### Integration Notes for Next Topic (JavaDoc & Exam Prep)

The next topic is the capstone exam preparation:

1. **Documentation skills:** Students should document their GRASP implementations in JavaDoc comments explaining design decisions.

2. **Verbal articulation:** The exam preparation should include practice explaining GRASP principles aloud - students need to verbalize design decisions.

3. **Project connection:** Help students map their Onskeskyen code to specific GRASP principles for the project demonstration.

4. **Complete integration:** All semester topics (ADT, SQL, Spring Boot, Sessions, IoC/DI) should be connected to GRASP in exam preparation materials.

5. **"Why" emphasis:** The exam requires explaining "why" certain designs are better - GRASP provides the vocabulary for this.

6. **Code quality evaluation:** Students should practice evaluating code snippets using GRASP criteria as exam practice.
