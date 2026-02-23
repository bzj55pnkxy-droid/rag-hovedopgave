# JavaDoc & Exam Preparation - 2nd Semester Programming

*Prerequisites: ALL previous 2nd semester topics (ADT & Collections, HTML, SQL, Database-Java Integration, Spring Boot, Sessions/IoC/DI, GRASP Design Principles)*
*Phase: 8 - Final Preparation (Week 21, May)*
*Exam Weight: MODERATE - but this topic synthesizes ALL other topics for oral examination*

---

## What You'll Learn

By the end of this topic, you will be able to:
- **Write professional JavaDoc documentation** for classes, methods, and APIs
- **Present your project confidently** in a 2-4 minute product demonstration
- **Articulate design decisions** using proper vocabulary (GRASP, Big-O, normalization)
- **Answer "why" questions** rather than just explaining "what" you implemented
- **Navigate all four subject areas** during the oral exam (Programming, Systems Development, Technology, Business)
- **Connect code to business requirements** and explain broader implications
- **Trace requests through your full-stack application** from HTML to database and back

This is the capstone topic. Everything you've learned this semester comes together here - not to add new knowledge, but to synthesize and articulate what you already know.

---

## Understanding the Exam Format

### The Oral Examination Structure

Your exam is an oral presentation with project demonstration. It typically lasts 20-30 minutes and follows this structure:

**1. Product Demonstration (2-4 minutes)**

You begin with a live demo of your exam project. This is your chance to control the narrative and show your best work.

Key requirements:
- Have test data pre-loaded. Do not spend demo time creating accounts or entering data.
- Show all major features systematically. Plan your demo flow in advance.
- The application must be deployed and functional. No "it works on my machine."
- Demonstrate the complete user workflow from start to finish.

**2. Technical Presentation (variable)**

After the demo, you discuss your implementation. The examiner asks about:
- How specific features work
- Why you made certain architectural decisions
- What GRASP principles you applied
- How data flows through your layers

**3. Examiner Questions (variable)**

Questions cover all four subject areas:
- **Programming:** ADT concepts, Collections, Big-O, OOP
- **Systems Development:** GRASP principles, UML diagrams, design decisions
- **Technology:** SQL, Spring Boot, HTTP, sessions, databases
- **Business:** User requirements, feasibility, real-world implications

**4. Reflection (brief)**

You may be asked:
- What would you do differently?
- What did you learn?
- What improvements would you make?

### The Critical Mindset Shift

**The exam is NOT a regurgitation of what the examiner has just read in your documentation.**

Examiners want to see that you understand, not that you memorized. They assess:
- Can you explain **why** something works, not just that it works?
- Can you connect code to **principles** (GRASP, normalization, Big-O)?
- Can you discuss **trade-offs** and alternative approaches?
- Do you understand the **broader context** beyond your specific code?

The phrase "proud egentilstand" (proud state of being) captures the desired mindset. You've built something substantial. You understand it deeply. Present with confidence.

---

## JavaDoc Documentation Standards

### Why Document Code?

Professional code documentation serves multiple purposes:

**For Other Developers:**
- API consumers need to understand how to use your classes
- Future maintainers need context for design decisions
- Team members need to understand responsibilities

**For Your Exam:**
- JavaDoc demonstrates professionalism
- Writing documentation forces you to clarify your own understanding
- Well-documented code is easier to explain during the oral exam

### JavaDoc Syntax Fundamentals

JavaDoc comments use a special format that starts with `/**` and ends with `*/`. They appear immediately before the element they document.

**Class-Level Documentation:**

```java
/**
 * Repository class for Wishlist data access operations.
 * Handles all database interactions for wishlist entities.
 *
 * Implements Information Expert pattern - this class has the
 * database expertise needed to persist and retrieve wishlists.
 *
 * @author YourName
 * @see WishlistService
 */
@Repository
public class WishlistRepository {
    // ...
}
```

**Method-Level Documentation:**

```java
/**
 * Retrieves all wishlists belonging to a specific user.
 *
 * Uses JdbcTemplate to execute parameterized SQL query,
 * preventing SQL injection attacks.
 *
 * @param userId the unique identifier of the user
 * @return a List of Wishlist objects, empty list if none found
 * @throws IllegalArgumentException if userId is negative
 */
public List<Wishlist> findByUserId(int userId) {
    // ...
}
```

### Essential JavaDoc Tags

| Tag | Purpose | Example |
|-----|---------|---------|
| `@param name description` | Document a method parameter | `@param userId the user's unique ID` |
| `@return description` | Document what the method returns | `@return the created wishlist` |
| `@throws ExceptionType description` | Document when exceptions occur | `@throws IllegalArgumentException if name is empty` |
| `@author name` | Document the class author | `@author YourName` |
| `@see reference` | Cross-reference related classes | `@see WishlistService` |
| `@since version` | Document when feature was added | `@since 1.0` |

### What to Document and When

**Always Document:**
- Public classes (especially Controllers, Services, Repositories)
- Public methods that other code calls
- Methods with non-obvious behavior
- Custom exceptions
- Complex algorithms or business rules

**Documentation Focus by Layer:**

| Layer | Documentation Focus |
|-------|---------------------|
| Controller | HTTP endpoints, request parameters, return views |
| Service | Business logic, validation rules, coordinated operations |
| Repository | SQL operations, mapping strategies, query purposes |
| Domain Objects | Entity meaning, relationships, constraints |

### Documentation as Design Explanation

The best JavaDoc connects implementation to design principles:

```java
/**
 * Service layer for wishlist business operations.
 *
 * This class is a Pure Fabrication - it doesn't represent a real-world
 * entity but exists to provide a home for business logic that doesn't
 * belong in controllers (HTTP handling) or repositories (data access).
 *
 * Achieves High Cohesion by focusing exclusively on wishlist-related
 * business rules: creation validation, sharing logic, item management.
 *
 * @author YourName
 */
@Service
public class WishlistService {
    // ...
}
```

This documentation helps you during the exam. When asked "Why did you create a Service layer?", you can point to your JavaDoc and explain: "As documented here, WishlistService is a Pure Fabrication that gives business logic a proper home."

---

## Synthesizing the Semester: The Full Picture

Your exam project integrates everything from this semester. Let's trace how each topic contributes to the complete application.

### The Full-Stack Request Flow

When a user creates a wishlist in your Onskeskyen project, this happens:

```
1. User fills out HTML form (HTML Fundamentals)
   └─> Browser sends POST request

2. Spring Boot receives request (Spring Boot Fundamentals)
   └─> @PostMapping method in WishlistController
   └─> Controller is GRASP Controller pattern

3. Controller checks session (Sessions, IoC & DI)
   └─> HttpSession for logged-in user verification
   └─> Redirect to login if not authenticated

4. Controller delegates to service (GRASP: Indirection, Low Coupling)
   └─> @Autowired WishlistService handles business logic
   └─> Service is Pure Fabrication

5. Service validates and processes (GRASP: High Cohesion)
   └─> Business rules applied
   └─> Domain objects created

6. Service calls repository (GRASP: Information Expert)
   └─> @Repository has database expertise
   └─> JdbcTemplate executes SQL (Database-Java Integration)

7. Repository executes INSERT (SQL Fundamentals)
   └─> Parameterized query with proper constraints
   └─> Foreign key to users table (SQL Advanced)

8. Response returns through layers
   └─> Repository returns saved object
   └─> Service returns to controller
   └─> Controller redirects to list view

9. List view renders (Spring Boot + Thymeleaf)
   └─> th:each iterates over wishlists (ADT & Collections)
   └─> HTML rendered and sent to browser
```

**Practice articulating this flow.** An examiner might ask: "Walk me through what happens when a user creates a wishlist."

### Topic Integration Map

This table shows how each semester topic manifests in your project:

| Semester Topic | Manifests In Your Project As |
|----------------|------------------------------|
| **ADT & Collections** | `List<Wishlist>` returned from repository, Collections in controllers |
| **HTML Fundamentals** | Thymeleaf templates, form structure, semantic elements |
| **SQL Fundamentals** | SELECT queries in repositories, CRUD operations |
| **SQL Advanced** | Constraints, foreign keys, possible views or procedures |
| **Database-Java Integration** | JdbcTemplate, RowMapper classes, layered data access |
| **Spring Boot Fundamentals** | @Controller, @Service, @Repository, MVC architecture |
| **Sessions, IoC & DI** | HttpSession for login, @Autowired for dependencies |
| **GRASP Principles** | Layered architecture, separation of concerns |

### Architecture Explanation Template

For your exam, prepare to explain your architecture using this structure:

**"My application follows Spring Boot's MVC pattern with three main layers:**

**Controller layer** handles HTTP requests. Controllers receive parameters, check sessions, call services, and return view names. This implements the GRASP Controller pattern - they coordinate but don't contain business logic.

**Service layer** is a Pure Fabrication that contains business logic. Services validate data, coordinate between repositories, and implement business rules. They achieve High Cohesion by focusing on one domain area.

**Repository layer** implements Information Expert for database access. Repositories know SQL, use JdbcTemplate, and convert ResultSets to domain objects using RowMappers.

**Dependency Injection** connects these layers with Low Coupling. Controllers don't create services - Spring injects them. This means I can test layers in isolation and change implementations without affecting other layers."

---

## Preparing for Each Subject Area

### Programming Questions

**Topics to Review:**
- Abstract Data Types: concept vs. implementation
- Java Collections Framework: when to use List vs. Set vs. Map
- Big-O notation: O(1) vs O(n) vs O(n²) and when it matters
- OOP concepts: inheritance, polymorphism, interfaces
- Exception handling: custom exceptions, when to throw vs. catch

**Sample Questions and Strong Answers:**

**Q: "Why do you use List instead of ArrayList in your method signatures?"**

*"This applies the Polymorphism GRASP principle and Programming to Interfaces. By declaring `List<Wishlist>` instead of `ArrayList<Wishlist>`, my code depends on the interface, not the implementation. If I later need to change from ArrayList to LinkedList, I only change the creation point, not every method that uses the list. It also enables Low Coupling - my services don't depend on specific collection implementations."*

**Q: "What's the Big-O complexity of finding an item in your wishlist?"**

*"If the wishlist items are stored in an ArrayList and I search by iterating, it's O(n) - linear time proportional to the number of items. If I needed faster lookups, I could use a HashMap with item ID as the key for O(1) average-case lookup. For our project scale with typically under 100 items per wishlist, O(n) is acceptable, but I understand the trade-off."*

**Q: "Why use custom exceptions instead of generic RuntimeException?"**

*"Custom exceptions like `WishlistNotFoundException` communicate intent more clearly than generic exceptions. They enable specific error handling - I can catch `WishlistNotFoundException` and show a user-friendly message, while letting other exceptions propagate for debugging. It follows Information Expert: the custom exception knows about its specific error condition."*

### Database Design & SQL Questions

**Topics to Review:**
- Normalization: 1NF, 2NF, 3NF and why
- EER/ERD diagrams: entities, relationships, cardinality
- JOINs: INNER, LEFT, when to use each
- Constraints: PRIMARY KEY, FOREIGN KEY, CASCADE, NOT NULL
- Subqueries: when useful vs. when JOINs are better

**Sample Questions and Strong Answers:**

**Q: "Explain your database design. Why did you structure it this way?"**

*"My database has three main tables: users, wishlists, and items. I normalized to Third Normal Form to prevent data redundancy. The users table stores account information. The wishlists table has a foreign key to users - each wishlist belongs to one user, but a user can have many wishlists. The items table has a foreign key to wishlists. I used ON DELETE CASCADE so deleting a wishlist automatically removes its items, maintaining referential integrity without manual cleanup."*

**Q: "When would you use a LEFT JOIN vs INNER JOIN?"**

*"INNER JOIN returns only matching rows from both tables - I use it when I need related data that must exist. For example, getting wishlist items where both the wishlist and items must exist. LEFT JOIN returns all rows from the left table even without matches - I use it when I want to include entities that might have no related records, like showing all wishlists including empty ones."*

**Q: "Why use foreign key constraints? Couldn't you just be careful in your code?"**

*"Foreign key constraints enforce referential integrity at the database level, which is more reliable than application-level checks. If my application has a bug, the database still prevents orphaned items. Constraints also document the data model explicitly - anyone reading the schema understands the relationships. The CASCADE option automates cleanup when parent records are deleted."*

### Web Development with Spring Boot Questions

**Topics to Review:**
- MVC architecture: flow from request to response
- Spring annotations: @Controller, @Service, @Repository, @Autowired
- Thymeleaf: th:each, th:if, th:object, th:field
- Sessions and cookies: when to use, how they work
- HTTP: GET vs POST, request/response cycle

**Sample Questions and Strong Answers:**

**Q: "Walk me through what happens when a user submits a form."**

*"The browser sends an HTTP POST request to the URL in the form's action attribute. Spring Boot's DispatcherServlet routes this to my controller method marked with @PostMapping. Spring extracts form fields using @RequestParam or binds them to an object. My controller validates the session, calls the service to process the data, and returns either a view name or a redirect. If redirecting, Spring sends a 302 response and the browser makes a new GET request."*

**Q: "Why do you use sessions instead of just passing user data in each request?"**

*"HTTP is stateless - each request is independent. But my application needs to know who's logged in across multiple requests. Sessions solve this by storing user data server-side, identified by a session ID cookie. The browser sends this cookie with each request, and Spring retrieves the associated HttpSession. This is more secure than passing user IDs in form fields (which could be manipulated) and more practical than requiring login on every page."*

**Q: "How does Thymeleaf work with your controller?"**

*"Thymeleaf is the View in MVC. My controller adds data to the Model object, then returns a template name. Spring passes the Model to Thymeleaf, which processes the template. Thymeleaf expressions like `${wishlist.name}` access Model attributes. Iteration with `th:each` loops over collections. The processed HTML is sent to the browser. This separation means I can change templates without touching controller logic."*

### Systems Development & GRASP Questions

**Topics to Review:**
- All nine GRASP principles (review the previous topic material)
- Layered architecture justification
- UML diagram purposes: Use Case, Domain Model, Class, Package, ERD
- Design decision vocabulary

**Sample Questions and Strong Answers:**

**Q: "Which GRASP principle justifies your Service layer?"**

*"The Service layer is a Pure Fabrication. A 'WishlistService' doesn't represent a real-world entity - you can't touch a service. But it provides a home for business logic that doesn't belong in controllers (HTTP handling) or repositories (data access). Without services, business logic would leak into controllers, violating High Cohesion, or into domain objects, creating excessive coupling."*

**Q: "How does @Autowired relate to design principles?"**

*"@Autowired implements Low Coupling through Dependency Injection. Instead of writing `new WishlistService()` in my controller, which couples it to that specific implementation, I declare a dependency and Spring injects it. My controller only knows it needs 'something providing wishlist operations.' This means I can test with mock services, swap implementations, and change service internals without affecting controllers."*

**Q: "Why did you create separate packages for controllers, services, and repositories?"**

*"This reflects High Cohesion at the package level and makes the architecture visible. Anyone looking at the project structure immediately understands the layers. Each package contains classes with related responsibilities. The package diagram in our documentation shows these layers and their dependencies - controllers depend on services, services depend on repositories, but not the reverse."*

---

## Demo Preparation Checklist

### Before Your Exam Day

**Technical Preparation:**
- [ ] Application deployed and accessible
- [ ] Test data pre-loaded (users, wishlists, items)
- [ ] Backup plan if deployment fails (local demo capability)
- [ ] Test all features work in the deployed environment
- [ ] Know how to access your deployed application URL

**Demo Script:**
- [ ] Plan your 2-4 minute walkthrough
- [ ] Choose a narrative: follow a user's journey
- [ ] Identify which features demonstrate which concepts
- [ ] Practice the demo multiple times

**Code Familiarity:**
- [ ] Review all your controller methods
- [ ] Understand every SQL query in your repositories
- [ ] Know which services handle which business logic
- [ ] Be able to find any code the examiner asks about

### Demo Flow Template

A strong demo follows a user story:

**1. Login (30 seconds)**
- Show the login form
- Login with pre-created test user
- Briefly mention: "This uses session management to track the logged-in user"

**2. View Existing Data (30 seconds)**
- Show the wishlist overview
- Click into a wishlist with items
- Mention: "This data comes from our MySQL database through the repository layer"

**3. Create Something (45 seconds)**
- Create a new wishlist or item
- Show form validation in action
- Mention: "The service layer validates this before persisting"

**4. Edit/Update (30 seconds)**
- Modify an existing record
- Show the update reflected
- Mention: "This demonstrates full CRUD operations"

**5. Key Feature (45 seconds)**
- Show your most impressive feature
- This might be sharing, filtering, or searching
- Connect it to the project requirements

**6. Close (20 seconds)**
- Logout to show session cleanup
- End with the application in a good state

### What to Avoid in Your Demo

**Do NOT:**
- Create new accounts during the demo (waste of time)
- Show the IDE or terminal (focus on the application)
- Debug or fix issues live (have working code)
- Read from notes (know your application)
- Apologize for features ("this doesn't quite work...")
- Rush through without explaining what you're showing

---

## Sample Exam Questions Across All Topics

### Programming Domain

1. "Explain the difference between an ADT and its implementation."
2. "When would you choose a Set over a List?"
3. "What's the time complexity of your wishlist search?"
4. "How does your application handle exceptions?"
5. "Why use interfaces in your repository design?"

### Database Domain

6. "Walk me through your database schema."
7. "Explain the relationships between your tables."
8. "When did you use JOINs in your queries?"
9. "What constraints protect your data integrity?"
10. "How would you optimize a slow query?"

### Web Development Domain

11. "Trace a request from form submission to database and back."
12. "How does session management work in your application?"
13. "Explain the MVC pattern as implemented in your project."
14. "What's the difference between GET and POST in your controllers?"
15. "How does Thymeleaf render your wishlist data?"

### Systems Development Domain

16. "Which GRASP principles does your architecture implement?"
17. "Why did you separate controllers, services, and repositories?"
18. "How does dependency injection benefit your design?"
19. "Explain your class diagram."
20. "What trade-offs did you make in your design?"

### Reflection Questions

21. "What was the most challenging part of this project?"
22. "What would you do differently if you started over?"
23. "What did you learn that surprised you?"
24. "How would you extend this project in the future?"
25. "What features didn't you have time to implement?"

---

## Model Answers for Common Questions

### "Explain your layered architecture."

*"My application uses Spring Boot's three-layer architecture. The Controller layer receives HTTP requests, checks sessions, and coordinates responses - implementing the GRASP Controller pattern. The Service layer contains business logic as a Pure Fabrication - it doesn't represent real-world entities but provides a home for validation and business rules, achieving High Cohesion. The Repository layer is the Information Expert for database access, containing all SQL and JdbcTemplate usage. These layers connect through Dependency Injection, achieving Low Coupling - each layer depends on interfaces, not implementations."*

### "Why did you normalize your database?"

*"Normalization to Third Normal Form prevents data redundancy and update anomalies. If I stored the user's name in every wishlist row, updating a username would require changing multiple rows - risking inconsistency. Instead, wishlists store only a user_id foreign key referencing the users table. There's one source of truth for user data. The JOIN to get user information for wishlists is a small performance cost for significant data integrity benefits."*

### "How does your application maintain user state?"

*"HTTP is stateless, but my application needs to track logged-in users. I use Spring's HttpSession. On successful login, I store the User object in the session with `session.setAttribute()`. On each subsequent request, controllers retrieve this with `session.getAttribute()` to verify the user is authenticated. The session ID is stored in a cookie, automatically sent by the browser. When the user logs out, I call `session.invalidate()` to destroy the session."*

### "What GRASP principle justifies @Autowired?"

*"@Autowired implements Low Coupling through Dependency Injection. My WishlistController declares `private final WishlistService wishlistService` but never creates it. Spring's IoC container - acting as Creator - instantiates the service and injects it. This means my controller doesn't know how the service is constructed or what dependencies it has. I can change the service implementation without touching the controller. For testing, I can inject mock services. This is Inversion of Control - instead of my code controlling object creation, the framework controls it."*

### "Trace a request through your application."

*"When a user clicks 'Create Wishlist,' the browser sends a POST to `/wishlists`. Spring routes this to my `@PostMapping('/wishlists')` method in WishlistController. The controller retrieves the current user from HttpSession. If not logged in, it redirects to `/login`. Otherwise, it calls `wishlistService.create(name, userId)`. The service validates the name - at least 3 characters, no longer than 100 - and creates a Wishlist domain object. It calls `wishlistRepository.save(wishlist)`. The repository executes `INSERT INTO wishlists (name, user_id) VALUES (?, ?)` via JdbcTemplate. The controller returns `redirect:/wishlists`, causing a 302 response. The browser makes a new GET request, which queries all user wishlists and renders the Thymeleaf template."*

---

## Common Exam Pitfalls to Avoid

### Pitfall 1: Explaining "What" Instead of "Why"

**Poor Answer:** "I use @Autowired to inject the service."

**Strong Answer:** "I use @Autowired to achieve Low Coupling. By letting Spring inject the service instead of creating it myself, my controller doesn't depend on the specific service implementation. This makes the code more testable and maintainable."

### Pitfall 2: Reading from Documentation

Examiners know what your code does - they've read it. Don't read back what's obvious. Instead, explain the reasoning behind decisions.

### Pitfall 3: Being Defensive About Design Choices

**Poor Response:** "Well, I know it's not perfect, but..."

**Strong Response:** "I chose this approach because... A trade-off is... An alternative would be..."

Every design has trade-offs. Discussing them shows maturity and understanding.

### Pitfall 4: Not Knowing Your Own Code

If the examiner asks about a specific method and you can't find it or explain it, that's a significant problem. Before the exam, review every controller method, service method, and repository query.

### Pitfall 5: Ignoring the Full Stack

An examiner might ask: "What SQL runs when this button is clicked?" You should be able to trace from UI to database.

### Pitfall 6: Over-Complicating Simple Questions

**Q:** "What does this controller method do?"

**Poor Answer:** *(long rambling explanation of MVC theory)*

**Strong Answer:** "This method handles the wishlist creation form. It validates the session, calls the service to create the wishlist, and redirects to the list view."

Answer the question asked. You can elaborate if prompted.

---

## Connecting All Topics: The Semester Summary

### Your Learning Journey

At the start of this semester, you knew:
- Object-oriented programming in Java
- Unit testing with JUnit
- Basic algorithms and ArrayList

Now you can build and deploy a complete web application:

```
[User Browser]
     │
     ▼
[HTML Forms + Thymeleaf]  ← HTML Fundamentals
     │
     ▼
[Spring Boot Controller]  ← Spring Boot MVC, GRASP Controller
     │
     │ @Autowired (Low Coupling, IoC/DI)
     ▼
[Service Layer]           ← Pure Fabrication, High Cohesion
     │
     │ @Autowired (Low Coupling, Creator)
     ▼
[Repository Layer]        ← Information Expert
     │
     │ JdbcTemplate (Database-Java Integration)
     ▼
[MySQL Database]          ← SQL Fundamentals, Advanced SQL
     │
     ▼
[RowMapper → Domain Objects] → [List<T>]  ← ADT & Collections
     │
     ▼
[Back through layers to Thymeleaf → HTML → User]
```

### The Conceptual Integration

Each topic wasn't isolated - they build on each other:

**ADT & Collections** provides the data structures (List, Set, Map) used everywhere.

**HTML Fundamentals** creates the user interface that Spring Boot serves.

**SQL Fundamentals** enables data persistence that makes your application useful.

**SQL Advanced** adds professional features like constraints and relationships.

**Database-Java Integration** connects your Java code to your database.

**Spring Boot** provides the framework organizing all these pieces.

**Sessions, IoC & DI** adds user state management and explains Spring's "magic."

**GRASP Principles** gives you vocabulary to explain why your architecture is good.

**JavaDoc & Exam Prep** (this topic) synthesizes everything for professional communication.

### The Integration Visualization

```
┌─────────────────────────────────────────────────────────────────┐
│                    YOUR EXAM PROJECT                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐    ┌──────────────┐    ┌─────────────────┐    │
│  │ Controllers │───▶│   Services   │───▶│  Repositories   │    │
│  │ (HTTP/View) │    │(Business)    │    │ (Data Access)   │    │
│  └─────────────┘    └──────────────┘    └─────────────────┘    │
│        │                   │                    │               │
│        │                   │                    ▼               │
│        │                   │           ┌─────────────────┐      │
│        ▼                   ▼           │    Database     │      │
│  ┌───────────┐      ┌───────────┐     │ (MySQL + SQL)   │      │
│  │ Thymeleaf │      │  Domain   │     └─────────────────┘      │
│  │  + HTML   │      │  Objects  │                               │
│  └───────────┘      └───────────┘                               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  INFRASTRUCTURE: Sessions, IoC Container, DI, JdbcTemplate     │
├─────────────────────────────────────────────────────────────────┤
│  PRINCIPLES: GRASP (High Cohesion, Low Coupling, Information   │
│              Expert, Controller, Pure Fabrication, etc.)       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Final Preparation Checklist

### Week Before Exam

- [ ] Review all project code - know every method
- [ ] Practice explaining your architecture out loud
- [ ] Do a mock demo with a friend or classmate
- [ ] Review GRASP principles (from previous topic)
- [ ] Review your UML diagrams
- [ ] Ensure deployment is working

### Day Before Exam

- [ ] Test the deployed application
- [ ] Verify test data is loaded
- [ ] Review your demo script
- [ ] Get good sleep

### During the Exam

- [ ] Start with confidence - you built this
- [ ] Listen carefully to questions before answering
- [ ] Connect implementations to principles
- [ ] Admit what you don't know honestly
- [ ] Show enthusiasm for your work

---

## Key Takeaways

- **The exam assesses understanding, not memorization.** Explain "why," not just "what."

- **Your demo sets the tone.** Practice it. Have data ready. Show your best work first.

- **JavaDoc is professional communication.** Document classes and public methods. Connect documentation to design principles.

- **Everything connects.** Each semester topic appears in your project. Be ready to trace from UI to database.

- **GRASP vocabulary is essential.** "This is Information Expert," "That's Pure Fabrication" - use the terminology.

- **Four subject areas means broad preparation.** Review programming, database, web development, AND systems development.

- **Confidence matters.** You've built a complete web application. You understand it. Present with pride.

- **Reflection shows maturity.** Be ready to discuss what you learned, what you'd change, and what could improve.

---

## Preparing the Next Generation

If you're reading this after your exam, consider what you wish you'd known:

- Start demo preparation early
- Practice explaining out loud (to anyone who will listen)
- Know your code deeply - every method, every query
- Connect everything to GRASP principles
- Be ready for "why" questions on every design choice
- The exam is a conversation, not an interrogation

You've learned an enormous amount this semester. From Java collections to SQL to web applications to design principles. It all comes together in your project. Present it with the confidence it deserves.

---

## Quick Reference: What to Review

| Topic | Key Concepts for Exam |
|-------|----------------------|
| **ADT & Collections** | Interface vs. implementation, List/Set/Map choice, Big-O |
| **HTML Fundamentals** | Form structure, semantic elements, Thymeleaf integration |
| **SQL Fundamentals** | SELECT, JOIN, INSERT/UPDATE/DELETE, aggregate functions |
| **SQL Advanced** | Constraints, foreign keys, normalization (3NF), subqueries |
| **Database-Java Integration** | JdbcTemplate, RowMapper, layered data access |
| **Spring Boot** | MVC, @Controller, @Service, @Repository, @GetMapping/@PostMapping |
| **Sessions, IoC & DI** | HttpSession, @Autowired, IoC principle, DI patterns |
| **GRASP Principles** | All nine: Information Expert, High Cohesion, Low Coupling, Controller, Creator, Pure Fabrication, Polymorphism, Indirection, Protected Variations |
| **JavaDoc** | @param, @return, @throws, class documentation |

---

*Good luck with your exam. You've done the work. Now show what you know.*
