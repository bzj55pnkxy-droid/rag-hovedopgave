# Sessions, IoC & Dependency Injection - 2nd Semester Programming

*Prerequisites: Spring Boot & Web Development Fundamentals (MVC, @Controller, @Service, @Repository, Thymeleaf, layered architecture, Model object)*
*Phase: 6 (Advanced Web Concepts & Enterprise Patterns)*
*Exam Weight: HIGH - Both Sessions/Cookies and IoC/DI are high emphasis exam topics*

---

## What You'll Learn

By the end of this topic, you will be able to:
- **Understand HTTP statelessness** and why sessions and cookies exist
- **Implement login/logout functionality** using HttpSession for user authentication
- **Maintain user state** across multiple HTTP requests
- **Create and manage cookies** for client-side state persistence
- **Explain Inversion of Control (IoC)** - the "magic" behind Spring's object management
- **Apply Dependency Injection patterns** using constructor, setter, and field injection
- **Connect IoC/DI to GRASP principles** - especially Low Coupling
- **Design testable, maintainable architectures** through proper dependency management

This topic pulls back the curtain on Spring's "magic." You've been using `@Autowired` and constructor injection since Phase 5 without fully understanding how it works. Now we explain why Spring creates objects for you, why you don't write `new ProfileService()`, and how this connects to the design principles you learned in Systems Development.

---

## Why This Matters

### The Statelessness Problem

In the previous topic, you learned the request-response cycle: browser sends request, controller processes it, template renders response. What we didn't emphasize is that HTTP is **stateless** - each request is completely independent. The server has no memory of previous requests.

**The problem this creates:**

Consider logging into Onskeskyen. You enter username and password, the server validates them. Great - you're logged in! But then you click "View My Wishlists." That's a new HTTP request. The server has forgotten that you just logged in. It doesn't know who you are.

Without sessions, every single page would require you to enter your credentials. Every. Single. Page.

**Sessions solve this:** When you log in successfully, the server creates a session - a container for storing information about you. It gives your browser a session ID (stored in a cookie). On subsequent requests, your browser sends that ID, and the server looks up your session to remember who you are.

### The Dependency Management Problem

In 1st semester, you created objects like this:

```java
ProfileService profileService = new ProfileService();
```

Simple and direct. But what if `ProfileService` needs a `ProfileRepository`? And `ProfileRepository` needs a `JdbcTemplate`? And `JdbcTemplate` needs a `DataSource`?

```java
DataSource dataSource = new HikariDataSource(...);
JdbcTemplate jdbcTemplate = new JdbcTemplate(dataSource);
ProfileRepository profileRepository = new ProfileRepository(jdbcTemplate);
ProfileService profileService = new ProfileService(profileRepository);
```

Now your controller needs to know how to create everything. It's **tightly coupled** to all these implementation details. Change how the repository is configured? Update every class that creates it.

**Inversion of Control solves this:** Instead of your code controlling object creation, you invert control to the framework. Spring creates objects, manages their lifecycle, and provides them where needed. Your code just declares what it needs.

This is why you write:

```java
@Controller
public class ProfileController {
    private final ProfileService profileService;

    public ProfileController(ProfileService profileService) {
        this.profileService = profileService;
    }
}
```

Spring sees that `ProfileController` needs a `ProfileService` and provides one. You don't care how it's created or configured.

### Connecting to GRASP Principles

**Low Coupling** is the GRASP principle stating that classes should minimize dependencies on other classes. Dependency Injection is the primary mechanism to achieve Low Coupling in Spring Boot:

| Without DI (High Coupling) | With DI (Low Coupling) |
|---------------------------|------------------------|
| `new ProfileService()` | Constructor receives `ProfileService` |
| Class knows how to create dependency | Class only knows the interface |
| Changing ProfileService affects this class | Changing ProfileService doesn't affect this class |
| Hard to test - can't substitute mock | Easy to test - inject mock service |

You learned GRASP in Systems Development. Now you see how Spring Boot implements these principles architecturally.

---

## Part 1: Understanding HTTP Statelessness

### The Fundamental Limitation

HTTP (Hypertext Transfer Protocol) was designed as a request-response protocol. Each request is self-contained, carrying all information needed to process it. The server processes the request, sends a response, and forgets everything.

**Why stateless?**
- **Scalability:** Any server can handle any request (no need to remember previous interactions)
- **Simplicity:** Servers don't need to track millions of client states
- **Reliability:** If a server fails, another can take over without lost state

**The tradeoff:** Statelessness is great for serving static web pages. But modern applications need to remember things: who is logged in, what's in the shopping cart, user preferences.

### State Management Solutions

There are two places to store state:

**Server-side (Sessions):**
- Data stored on the server
- More secure (users can't tamper with it)
- Limited by server memory
- Lost if server restarts (without persistence)

**Client-side (Cookies):**
- Data stored in the browser
- Sent with every request automatically
- Limited size (4KB typical)
- User can see and potentially modify
- Persists across browser restarts (if configured)

**The typical pattern:** Use a small cookie to identify the session, store actual data on the server in the session.

---

## Part 2: HTTP Sessions with HttpSession

### What is a Session?

A session is a server-side container for storing user-specific data across multiple HTTP requests. Each session has:
- A unique **session ID** (automatically managed)
- A **key-value store** for your data
- A **timeout** (when the session expires if inactive)
- A **lifecycle** (created, used, invalidated)

### Accessing HttpSession in Controllers

Spring provides the `HttpSession` object as a controller method parameter:

```java
@GetMapping("/dashboard")
public String dashboard(HttpSession session, Model model) {
    User currentUser = (User) session.getAttribute("currentUser");
    if (currentUser == null) {
        return "redirect:/login";  // Not logged in
    }
    model.addAttribute("user", currentUser);
    return "dashboard";
}
```

**Key insight:** You declare `HttpSession session` as a parameter, and Spring provides it. This is itself an example of dependency injection - Spring injects the session object.

### Core Session Operations

**Storing data in the session:**
```java
session.setAttribute("currentUser", user);
session.setAttribute("cartItems", itemList);
```

**Retrieving data from the session:**
```java
User user = (User) session.getAttribute("currentUser");
// Returns null if attribute doesn't exist
```

**Checking if user is logged in:**
```java
if (session.getAttribute("currentUser") != null) {
    // User is logged in
}
```

**Ending the session (logout):**
```java
session.invalidate();  // Destroys all session data
```

### The Login/Logout Pattern for Onskeskyen

This is the authentication pattern you'll implement in your Wishlist project:

**Login Controller:**
```java
@GetMapping("/login")
public String showLoginForm() {
    return "login";  // Display login form
}

@PostMapping("/login")
public String processLogin(@RequestParam String username,
                          @RequestParam String password,
                          HttpSession session) {
    User user = userService.authenticate(username, password);
    if (user != null) {
        session.setAttribute("currentUser", user);
        return "redirect:/wishlists";
    }
    return "redirect:/login?error";
}
```

**Logout Controller:**
```java
@GetMapping("/logout")
public String logout(HttpSession session) {
    session.invalidate();
    return "redirect:/";
}
```

**Authorization Check (protecting pages):**
```java
@GetMapping("/wishlists")
public String myWishlists(HttpSession session, Model model) {
    User user = (User) session.getAttribute("currentUser");
    if (user == null) {
        return "redirect:/login";
    }
    List<Wishlist> wishlists = wishlistService.findByUserId(user.getUserId());
    model.addAttribute("wishlists", wishlists);
    return "wishlist-list";
}
```

### Session Lifecycle

**Creation:** Session is created on first access (first `setAttribute` or when accessing `session`)

**Duration:** Session remains active as long as:
- User is active (requests reset the timeout)
- Session hasn't been invalidated
- Server hasn't restarted

**Timeout:** Default is typically 30 minutes of inactivity. Can be configured:
```java
session.setMaxInactiveInterval(60 * 60);  // 1 hour in seconds
```

**Invalidation:** Call `session.invalidate()` to explicitly destroy (logout)

### Session vs Model: Understanding the Difference

Students often confuse session attributes with Model attributes:

| Model | Session |
|-------|---------|
| Lasts for one request | Persists across requests |
| For passing data to view | For maintaining user state |
| `model.addAttribute("items", items)` | `session.setAttribute("user", user)` |
| Not available after redirect | Available after redirect |
| No security implications | Contains authentication state |

**Use Model for:** Data specific to rendering one page (list of cars, form object)

**Use Session for:** Data that persists across navigation (logged-in user, shopping cart)

---

## Part 3: Cookies

### What is a Cookie?

A cookie is a small piece of data stored in the browser and sent automatically with every request to the matching domain. Cookies enable client-side state persistence.

**How cookies work:**
1. Server sends `Set-Cookie` header in response
2. Browser stores the cookie
3. Browser sends cookie with every subsequent request to that domain
4. Server reads cookie from request

### Session Cookies vs Persistent Cookies

**Session cookies** expire when the browser closes:
```java
Cookie cookie = new Cookie("preference", "dark-mode");
// No setMaxAge - cookie disappears when browser closes
response.addCookie(cookie);
```

**Persistent cookies** survive browser restarts:
```java
Cookie cookie = new Cookie("rememberMe", "user123");
cookie.setMaxAge(60 * 60 * 24 * 30);  // 30 days in seconds
response.addCookie(cookie);
```

### Creating and Reading Cookies

**Creating a cookie:**
```java
@PostMapping("/preferences")
public String savePreference(@RequestParam String theme,
                            HttpServletResponse response) {
    Cookie cookie = new Cookie("theme", theme);
    cookie.setMaxAge(60 * 60 * 24 * 365);  // 1 year
    cookie.setPath("/");  // Available to all paths
    response.addCookie(cookie);
    return "redirect:/settings";
}
```

**Reading cookies:**
```java
@GetMapping("/settings")
public String settings(@CookieValue(value = "theme",
                                     defaultValue = "light") String theme,
                       Model model) {
    model.addAttribute("currentTheme", theme);
    return "settings";
}
```

### URL Encoding for Special Characters

Cookie values can only contain certain characters. If you need to store values with spaces or special characters, use URL encoding:

```java
String value = "Hello World";
String encoded = URLEncoder.encode(value, StandardCharsets.UTF_8);
// encoded = "Hello+World" or "Hello%20World"

Cookie cookie = new Cookie("greeting", encoded);
response.addCookie(cookie);
```

**Reading encoded cookies:**
```java
String encoded = getCookieValue(request, "greeting");
String decoded = URLDecoder.decode(encoded, StandardCharsets.UTF_8);
// decoded = "Hello World"
```

### When to Use Cookies vs Sessions

| Use Cookies For | Use Sessions For |
|-----------------|------------------|
| User preferences (theme, language) | Authentication state |
| "Remember me" functionality | Shopping cart contents |
| Non-sensitive, small data | Sensitive user data |
| Data that should persist across visits | Data that should end with visit |

**Security note:** Never store sensitive data (passwords, credit cards) directly in cookies. Cookies can be seen and modified by users.

---

## Part 4: Inversion of Control (IoC)

### The Traditional Approach

Without IoC, your code controls object creation:

```java
public class WishlistController {
    private WishlistService service;

    public WishlistController() {
        // Controller creates its own dependency
        JdbcTemplate jdbc = new JdbcTemplate(dataSource);
        WishlistRepository repo = new WishlistRepository(jdbc);
        this.service = new WishlistService(repo);
    }
}
```

**Problems with this approach:**
1. **Tight coupling:** Controller knows about repository, jdbc, datasource
2. **Hard to test:** Can't substitute mock service for testing
3. **Configuration scattered:** Database settings in multiple places
4. **Changes cascade:** Modify repository constructor, update all places that create it

### The Inversion

"Inversion of Control" means inverting who controls object creation. Instead of your code creating dependencies, the framework creates them and provides them to your code.

**The Hollywood Principle:** "Don't call us, we'll call you."

Your code doesn't create objects. It declares what it needs, and the framework provides it.

```java
@Controller
public class WishlistController {
    private final WishlistService service;

    // Declare the dependency, don't create it
    public WishlistController(WishlistService service) {
        this.service = service;
    }
}
```

**What changed:**
- Controller doesn't create the service
- Controller doesn't know how service is created
- Controller doesn't know about repository or jdbc
- Controller just declares it needs a WishlistService

### The IoC Container (ApplicationContext)

Spring's IoC container is called `ApplicationContext`. It:
1. **Scans** for classes with stereotype annotations (@Component, @Service, @Repository, @Controller)
2. **Creates** instances of those classes (beans)
3. **Wires** dependencies by matching types
4. **Manages** the lifecycle of all beans

**The startup sequence:**
```
Spring Application starts
    |
    v
Component Scan finds:
  - WishlistController (@Controller)
  - WishlistService (@Service)
  - WishlistRepository (@Repository)
    |
    v
Container determines dependency order:
  - Repository has no dependencies (create first)
  - Service needs Repository (create second)
  - Controller needs Service (create third)
    |
    v
Container creates beans in order:
  1. WishlistRepository instance
  2. WishlistService instance (inject repository)
  3. WishlistController instance (inject service)
    |
    v
Application ready to handle requests
```

### Why This Matters

**1. Loose Coupling (GRASP):**
Classes don't know how dependencies are created. Change the repository implementation, and controllers/services don't care.

**2. Testability:**
In tests, inject mock dependencies:
```java
WishlistService mockService = mock(WishlistService.class);
WishlistController controller = new WishlistController(mockService);
// Test controller with controlled mock behavior
```

**3. Configuration Centralization:**
Database settings, bean scopes, initialization logic - all managed in one place by the container.

**4. Flexibility:**
Swap implementations without changing consuming code. Use `JdbcWishlistRepository` in production, `InMemoryWishlistRepository` in tests.

---

## Part 5: Dependency Injection (DI)

### What is Dependency Injection?

Dependency Injection is the pattern where dependencies are **provided to** objects rather than **created by** them. It's the mechanism through which IoC is achieved.

**Three forms of DI in Spring:**
1. Constructor Injection
2. Setter Injection
3. Field Injection

### Constructor Injection (Recommended)

Dependencies are provided through the constructor:

```java
@Service
public class WishlistService {
    private final WishlistRepository repository;

    // Dependencies injected via constructor
    public WishlistService(WishlistRepository repository) {
        this.repository = repository;
    }

    public List<Wishlist> findByUserId(int userId) {
        return repository.findByUserId(userId);
    }
}
```

**Why constructor injection is preferred:**
- **Immutability:** Dependencies can be `final` - they can't change after construction
- **Required dependencies:** Object can't be created without all dependencies
- **Explicit contract:** Constructor signature documents what the class needs
- **Testability:** Easy to provide mock dependencies in tests
- **No @Autowired needed:** Since Spring 4.3, single constructor doesn't require `@Autowired`

### Field Injection

Dependencies are injected directly into fields using `@Autowired`:

```java
@Service
public class WishlistService {
    @Autowired
    private WishlistRepository repository;  // Injected by Spring

    public List<Wishlist> findByUserId(int userId) {
        return repository.findByUserId(userId);
    }
}
```

**Why field injection is common but not recommended:**
- **Convenient:** Less code to write
- **Hidden dependencies:** Not visible in constructor signature
- **Harder to test:** Can't easily inject mocks without Spring context
- **Not immutable:** Field can't be `final`
- **NPE risk:** Object exists in invalid state before injection

**Field injection is fine for learning** but prefer constructor injection in production code.

### Setter Injection

Dependencies are provided through setter methods:

```java
@Service
public class NotificationService {
    private EmailService emailService;

    @Autowired
    public void setEmailService(EmailService emailService) {
        this.emailService = emailService;
    }
}
```

**When to use setter injection:**
- Optional dependencies that have reasonable defaults
- Dependencies that might change during object lifetime
- Breaking circular dependencies

### Comparing Injection Types

| Aspect | Constructor | Field | Setter |
|--------|-------------|-------|--------|
| Immutability | Yes (final) | No | No |
| Required deps | Enforced | Not enforced | Not enforced |
| Testability | Easy | Hard | Medium |
| Code verbosity | More | Less | Medium |
| Readability | Clear contract | Hidden deps | Moderate |
| Spring @Autowired | Optional | Required | Required |
| Recommended | Yes | For learning | Optional deps |

### The @Autowired Annotation

`@Autowired` tells Spring to inject a matching bean:

```java
@Autowired
private WishlistRepository repository;
```

Spring finds a bean of type `WishlistRepository` and injects it.

**How Spring matches beans:**
1. **By type:** Finds bean matching the field/parameter type
2. **By qualifier:** If multiple matches, use `@Qualifier("beanName")`
3. **By name:** If qualified, match bean name

**Since Spring 4.3:** If a class has only one constructor, `@Autowired` is optional. Spring injects constructor parameters automatically.

---

## Part 6: Spring Beans

### What is a Bean?

A bean is simply an object managed by Spring's IoC container. When you annotate a class with a stereotype annotation, Spring creates an instance and manages its lifecycle.

**Stereotype annotations create beans:**
- `@Component` - Generic managed component
- `@Service` - Business logic layer
- `@Repository` - Data access layer
- `@Controller` - Web request handling layer

These are all specializations of `@Component`. Spring treats them identically for bean creation, but the different names communicate intent.

### Bean Lifecycle

Beans go through several phases:

```
1. Instantiation
   Spring calls the constructor
       |
       v
2. Dependency Injection
   Spring injects @Autowired dependencies
       |
       v
3. Initialization (@PostConstruct)
   Optional setup code runs
       |
       v
4. Bean is Ready
   Available for use by application
       |
       v
5. Destruction (@PreDestroy)
   Cleanup code when container shuts down
```

**Using lifecycle hooks:**
```java
@Service
public class CacheService {
    private Map<String, Object> cache;

    @PostConstruct
    public void initialize() {
        this.cache = new ConcurrentHashMap<>();
        // Load initial cache data
    }

    @PreDestroy
    public void cleanup() {
        // Flush cache before shutdown
        cache.clear();
    }
}
```

### Bean Scope

Scope determines how many instances exist and how long they live:

**Singleton (default):** One instance per container. Same object injected everywhere.
```java
@Service  // Singleton by default
public class WishlistService { }
```

**Prototype:** New instance every time the bean is requested.
```java
@Service
@Scope("prototype")
public class ReportGenerator { }  // New instance each injection
```

**Request:** One instance per HTTP request (web applications).
```java
@Component
@RequestScope
public class RequestContext { }
```

**Session:** One instance per HTTP session (web applications).
```java
@Component
@SessionScope
public class ShoppingCart { }  // One cart per user session
```

**For most services:** Singleton scope is appropriate. Services are stateless and thread-safe.

**Session scope for user state:** If you need per-user data managed by Spring (alternative to HttpSession), use `@SessionScope`.

---

## Part 7: Programming to Interfaces

### The Principle

"Program to an interface, not an implementation" means declaring dependencies as interface types:

```java
// Interface defines the contract
public interface WishlistRepository {
    List<Wishlist> findByUserId(int userId);
    void save(Wishlist wishlist);
    void delete(int wishlistId);
}

// Implementation fulfills the contract
@Repository
public class JdbcWishlistRepository implements WishlistRepository {
    private final JdbcTemplate jdbcTemplate;

    public JdbcWishlistRepository(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    @Override
    public List<Wishlist> findByUserId(int userId) {
        // SQL implementation
    }
    // ... other methods
}
```

**Service depends on interface, not implementation:**
```java
@Service
public class WishlistService {
    private final WishlistRepository repository;  // Interface type!

    public WishlistService(WishlistRepository repository) {
        this.repository = repository;
    }
}
```

### Why This Matters

**1. Swappable implementations:**
- `JdbcWishlistRepository` for production
- `InMemoryWishlistRepository` for testing
- `MockWishlistRepository` for unit tests
- No code changes in WishlistService

**2. Testability:**
```java
@Test
void testGetUserWishlists() {
    // Create mock that returns controlled data
    WishlistRepository mockRepo = mock(WishlistRepository.class);
    when(mockRepo.findByUserId(1)).thenReturn(List.of(testWishlist));

    // Inject mock into service
    WishlistService service = new WishlistService(mockRepo);

    // Test service behavior
    List<Wishlist> result = service.findByUserId(1);
    assertEquals(1, result.size());
}
```

**3. Low Coupling (GRASP):**
Service doesn't know or care if data comes from MySQL, PostgreSQL, files, or mocks. It only knows the interface contract.

### Connection to 1st Semester

You learned this pattern with Collections:

```java
List<String> names = new ArrayList<>();  // Interface type, implementation instance
```

You used `List` (interface) even though the object was `ArrayList` (implementation). Same principle applies to your own interfaces.

---

## Part 8: Big-O Notation Revisited

### Connecting to Phase 1

In Phase 1, you learned Big-O notation for classifying algorithm efficiency. Now we apply it practically.

**Common complexities:**
- O(1) - Constant time (HashMap.get)
- O(log n) - Logarithmic (binary search)
- O(n) - Linear (simple loop through array)
- O(n log n) - Log-linear (efficient sorting)
- O(n^2) - Quadratic (nested loops, bubble sort)

### Practical Measurement

While Big-O gives theoretical classification, practical measurement shows real-world behavior:

```java
public void measureSortingPerformance() {
    int[] sizes = {1000, 10000, 100000};

    for (int size : sizes) {
        int[] data = generateRandomArray(size);

        long start = System.nanoTime();
        bubbleSort(data);
        long end = System.nanoTime();

        System.out.println("Bubble sort " + size + " elements: "
                          + (end - start) / 1_000_000 + " ms");
    }
}
```

**Expected results:**
- Bubble sort (O(n^2)): Time increases 100x when input increases 10x
- Merge sort (O(n log n)): Time increases ~13x when input increases 10x

### Application to Web Development

Big-O matters in web applications:

**Bad pattern (O(n^2)):**
```java
// For each wishlist, query items separately
for (Wishlist wishlist : wishlists) {
    List<Item> items = repository.findItemsByWishlistId(wishlist.getId());
    wishlist.setItems(items);
}
// N wishlists x M items = N queries
```

**Better pattern (O(n)):**
```java
// One query with JOIN
List<Wishlist> wishlists = repository.findAllWithItems();
// Single query returns all data
```

Understanding complexity helps you write efficient code and choose appropriate algorithms.

---

## Part 9: Exam Preparation

### High-Emphasis Exam Topics

**Sessions & Cookies:**
- What HttpSession is and why it's needed
- How to store and retrieve session data
- Login/logout implementation pattern
- Difference between session cookies and persistent cookies
- When to use sessions vs. cookies

**IoC & Dependency Injection:**
- What "Inversion of Control" means
- Why we don't use `new` to create services
- How @Autowired works (bean matching by type)
- Constructor injection vs. field injection (and why constructor is preferred)
- Connection to Low Coupling (GRASP)
- How the ApplicationContext manages beans

### Questions You Must Answer Confidently

**1. "Why are sessions needed in web applications?"**

*"HTTP is stateless - each request is independent, and the server doesn't remember previous requests. When a user logs in, we need to remember that across subsequent page views. Sessions provide server-side storage tied to a session ID. The browser stores the session ID in a cookie and sends it with each request, allowing the server to look up the user's session data."*

**2. "Walk me through how login works in your Onskeskyen project."**

*"When the user submits the login form, a POST request goes to my login controller. The controller calls userService.authenticate() to validate credentials against the database. If valid, I store the User object in the session with session.setAttribute("currentUser", user). On protected pages like viewing wishlists, I first check if session.getAttribute("currentUser") returns a user. If null, I redirect to the login page. If present, I use the user's ID to fetch their wishlists from the database."*

**3. "What is Inversion of Control and why do we use it?"**

*"Traditionally, objects create their own dependencies using 'new'. With IoC, control is inverted - the framework creates and provides dependencies. In Spring, I declare that my controller needs a service through constructor parameters. Spring's IoC container creates the service instance and injects it. This achieves Low Coupling because my controller doesn't know how the service is created or configured. It also enables testing because I can inject mock services."*

**4. "Explain how @Autowired works."**

*"When Spring scans my application, it finds classes with @Component, @Service, @Repository, and @Controller annotations and creates instances of them (beans). When it sees a constructor parameter or field marked with @Autowired, it looks for a bean matching that type. If my controller has a constructor with WishlistService parameter, Spring finds the bean annotated with @Service that implements WishlistService and injects it. Since Spring 4.3, single constructors don't even need @Autowired - Spring injects automatically."*

**5. "Why is constructor injection preferred over field injection?"**

*"Constructor injection allows dependencies to be final, ensuring immutability. It makes dependencies explicit in the constructor signature - you can see what a class needs. It enforces that all required dependencies are provided at construction time, so objects are never in an invalid state. For testing, I can create an instance with mock dependencies without needing the Spring context. Field injection hides dependencies and makes testing harder because you need reflection or Spring to inject the fields."*

**6. "How does IoC/DI relate to GRASP principles?"**

*"IoC/DI directly implements Low Coupling. With `new WishlistService()`, my controller is tightly coupled to that specific class and all its dependencies. With constructor injection, the controller only knows it needs something that provides wishlist operations - the interface. It doesn't create the dependency, doesn't know the implementation, and doesn't care about the repository or database inside. IoC also connects to Creator - instead of each class creating dependencies, the framework (Creator) creates all objects in a centralized, managed way."*

### Demonstration Strategy for Onskeskyen

When showing session management in your project:

**1. Show the login flow:**
"When I log in here, watch the controller method - it creates the session with session.setAttribute. Now I'm on the dashboard showing my name."

**2. Show session check:**
"If I try to access wishlists without logging in - let me open an incognito window - the controller checks session.getAttribute and redirects me to login."

**3. Show logout:**
"Clicking logout calls session.invalidate(), destroying all session data. Now I'm redirected to the home page."

**4. Show IoC in action:**
"Notice how my WishlistController receives WishlistService through the constructor. I never write `new WishlistService()`. Spring creates it and injects it. If I change how the service is configured, the controller doesn't change at all."

---

## Complete Data Flow: Session-Based Authentication

Understanding the complete flow demonstrates mastery:

```
1. User visits /wishlists (not logged in)
      |
      v
2. Controller: session.getAttribute("currentUser") returns null
      |
      v
3. return "redirect:/login"
      |
      v
4. User fills login form, clicks Submit
      |
      v
5. POST /login with username, password
      |
      v
6. Controller receives credentials
      |
      v
7. userService.authenticate(username, password)
      |
      v
8. userRepository.findByUsernameAndPassword(...)
      |
      v
9. JdbcTemplate executes SELECT query
      |
      v
10. RowMapper creates User object
       |
       v
11. User returns to controller
       |
       v
12. session.setAttribute("currentUser", user)
       |
       v
13. Server generates session ID, stores in JSESSIONID cookie
       |
       v
14. return "redirect:/wishlists"
       |
       v
15. Browser requests /wishlists with JSESSIONID cookie
       |
       v
16. Server looks up session by ID
       |
       v
17. Controller: session.getAttribute("currentUser") returns User
       |
       v
18. wishlistService.findByUserId(user.getUserId())
       |
       v
19. Repository queries database
       |
       v
20. List<Wishlist> returned to controller
       |
       v
21. model.addAttribute("wishlists", wishlists)
       |
       v
22. Thymeleaf renders wishlist-list.html
       |
       v
23. User sees their wishlists
```

---

## Common Struggles and Solutions

### Struggle 1: Session vs Model Confusion

**Problem:** "When do I use session.setAttribute vs model.addAttribute?"

**Clarification:**
- **Model:** Data for rendering THIS request's view. Gone after response.
- **Session:** Data that persists across requests. Lives until logout or timeout.

**Rule of thumb:**
- User identity (logged-in user): Session
- Data to display on page (list of items): Model
- Shopping cart: Session
- Form validation errors: Model

### Struggle 2: Understanding Why IoC Matters

**Problem:** "Why not just use `new`? It's simpler."

**Answer with testability:**
```java
// With 'new' - hard to test
public class WishlistController {
    private WishlistService service = new WishlistService();

    // How do I test this without a real database?
    // I can't substitute a mock service.
}

// With DI - easy to test
public class WishlistController {
    private final WishlistService service;

    public WishlistController(WishlistService service) {
        this.service = service;
    }

    // Test: new WishlistController(mockService)
}
```

### Struggle 3: Session Lifecycle Confusion

**Problem:** "My session data disappeared!"

**Common causes:**
1. **Server restart:** Sessions in memory are lost
2. **Browser closed:** Session cookies expire
3. **Timeout:** Inactive session destroyed
4. **Invalidate called:** Logout destroys session

**Debugging:**
```java
@GetMapping("/debug-session")
public String debugSession(HttpSession session) {
    System.out.println("Session ID: " + session.getId());
    System.out.println("User: " + session.getAttribute("currentUser"));
    System.out.println("Created: " + new Date(session.getCreationTime()));
    return "debug";
}
```

### Struggle 4: Choosing Injection Type

**Problem:** "Which injection method should I use?"

**Simple answer:** Use constructor injection for required dependencies.

```java
@Controller
public class WishlistController {
    private final WishlistService wishlistService;
    private final UserService userService;

    // Single constructor - Spring injects both
    public WishlistController(WishlistService wishlistService,
                              UserService userService) {
        this.wishlistService = wishlistService;
        this.userService = userService;
    }
}
```

Use field injection only in:
- Quick prototypes
- Tests (with `@Autowired` in test classes)
- When learning (less code to understand)

### Struggle 5: Cookie Encoding Issues

**Problem:** "My cookie value shows weird characters"

**Solution:** URL encode values with special characters:
```java
// Storing
String value = "Hello World";
String encoded = URLEncoder.encode(value, StandardCharsets.UTF_8);
response.addCookie(new Cookie("greeting", encoded));

// Reading
String encoded = cookieValue;
String decoded = URLDecoder.decode(encoded, StandardCharsets.UTF_8);
```

---

## Key Takeaways

- **HTTP is stateless** - each request is independent. Sessions and cookies solve this.

- **HttpSession** provides server-side storage for user state across requests. Use for authentication, shopping carts, user-specific data.

- **Cookies** provide client-side storage sent automatically with requests. Use for preferences, remember-me, session IDs.

- **Inversion of Control** means the framework controls object creation instead of your code. You declare dependencies; Spring provides them.

- **Dependency Injection** is how IoC is achieved. Dependencies are provided to objects, not created by them.

- **Constructor injection is preferred** because it enables immutability, explicit contracts, and easy testing.

- **@Autowired** tells Spring to inject a matching bean. Optional on single constructors since Spring 4.3.

- **Spring Beans** are objects managed by the IoC container. Created from @Component, @Service, @Repository, @Controller classes.

- **Program to interfaces** for flexibility and testability. Declare dependencies as interface types.

- **IoC/DI implements GRASP Low Coupling** - classes don't create their own dependencies.

- **Session-based authentication** pattern: Store user in session on login, check session on protected pages, invalidate on logout.

---

## For the Next Topic Agent

### Terminology Established This Topic

- **HTTP Statelessness:** HTTP protocol treats each request independently with no memory of previous requests. Sessions and cookies are solutions to maintain state across requests.

- **HttpSession:** Server-side storage associated with a user's browsing session. Identified by session ID (JSESSIONID cookie). Methods: `setAttribute(name, value)`, `getAttribute(name)`, `invalidate()`, `getId()`.

- **Session Lifecycle:** Creation (first access) -> Use (setAttribute/getAttribute) -> Timeout or Invalidation -> Destruction.

- **Session Cookie:** Cookie that expires when browser closes (no maxAge set).

- **Persistent Cookie:** Cookie with explicit expiration date that survives browser restarts.

- **URL Encoding:** Encoding special characters for safe transmission in URLs/cookies. `URLEncoder.encode()`, `URLDecoder.decode()`.

- **Inversion of Control (IoC):** Design principle where framework controls object lifecycle instead of application code. Spring container creates, configures, and manages objects.

- **Dependency Injection (DI):** Pattern where dependencies are provided to objects rather than created by them. Three types: constructor injection, setter injection, field injection.

- **Constructor Injection:** Dependencies provided via constructor parameters. Preferred because it enables immutability (final fields), explicit contracts, and easy testing. `@Autowired` optional for single constructor since Spring 4.3.

- **Field Injection:** Dependencies injected directly into fields using `@Autowired`. Convenient but less testable, not recommended for production.

- **ApplicationContext:** Spring's IoC container. Scans for components, creates beans, resolves dependencies, manages lifecycle.

- **Spring Bean:** Object managed by the IoC container. Created from classes with stereotype annotations (@Component, @Service, @Repository, @Controller).

- **Bean Scope:** How many instances exist. Singleton (default, one per container), Prototype (new instance each injection), Request (one per HTTP request), Session (one per HTTP session).

- **Bean Lifecycle:** Instantiation -> Dependency Injection -> @PostConstruct -> Ready for use -> @PreDestroy -> Destruction.

- **Programming to Interfaces:** Declaring dependencies as interface types for flexibility and testability. Enables swapping implementations without code changes.

- **GRASP Connection - Low Coupling:** IoC/DI implements Low Coupling by ensuring classes don't create their own dependencies. They only know interfaces, not implementations.

- **GRASP Connection - Creator:** Spring IoC container is the Creator - it creates and manages all beans centrally instead of scattered `new` calls.

### Example Classes/Code Created

- **Login Controller Pattern:** GET /login shows form, POST /login authenticates and creates session, GET /logout invalidates session.

- **Authorization Check Pattern:** Controller method checking `session.getAttribute("currentUser")` before allowing access to protected resources.

- **Constructor Injection Example:** Controller with final service field and single constructor receiving service parameter.

- **Session-Based Authentication Flow:** Complete 23-step trace from login form through database authentication to displaying personalized content.

### Student Capabilities After This Topic

Students who complete this material can now:
- Implement login/logout using HttpSession
- Check session for user authorization on protected pages
- Create and read cookies with proper URL encoding
- Explain why IoC inverts traditional control flow
- Implement constructor injection for services and repositories
- Explain how @Autowired resolves dependencies
- Connect IoC/DI to GRASP Low Coupling principle
- Compare session cookies vs. persistent cookies
- Design testable architectures through proper dependency management
- Trace complete authentication flow through all layers

### Pedagogical Patterns Used

- **"Magic" Reveal:** Students have been using @Autowired without understanding it. This topic explains the underlying IoC principle.

- **GRASP Integration:** Explicit connection to Systems Development course principles (Low Coupling, Creator).

- **Prior Topic Building:** Session management extends the stateless HTTP understanding from Spring Boot fundamentals.

- **Project Context:** All examples connect to Onskeskyen Wishlist project authentication requirements.

- **Exam Question Anticipation:** Model answers for high-emphasis topics (Sessions, IoC/DI).

- **Comparative Tables:** Session vs Model, constructor vs field injection, cookies vs sessions.

### Integration Notes for Next Topic (JavaDoc & Exam Prep)

The next topic is the capstone exam preparation:

1. **Documentation:** Students can now document the IoC/DI patterns and session management they've implemented.

2. **Explanation skills:** Practice explaining "why" behind architectural decisions (IoC, layered architecture, session-based auth).

3. **Complete application:** Students have all pieces for Onskeskyen - database, web, sessions, authentication.

4. **GRASP articulation:** Students should connect their implementation choices to GRASP principles in exam presentations.

5. **Code quality focus:** IoC/DI and proper injection patterns are part of the "high internal code quality" requirement for the project.
