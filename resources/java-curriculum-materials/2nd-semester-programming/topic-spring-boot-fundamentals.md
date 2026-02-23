# Spring Boot & Web Development Fundamentals - 2nd Semester Programming

*Prerequisites: HTML Fundamentals (semantic elements, forms), Database-Java Integration (JdbcTemplate, RowMapper, Repository pattern), ADT & Collections (List, ArrayList, iteration)*
*Phase: 5 (Web Development Fundamentals)*
*Exam Weight: VERY HIGH - This is the highest emphasis area for the exam*

---

## What You'll Learn

By the end of this topic, you will be able to:
- **Understand MVC architecture** - the foundational pattern separating Model, View, and Controller responsibilities
- **Create Spring Boot controllers** using `@Controller` annotation with handler methods
- **Map HTTP requests to methods** using `@GetMapping` and `@PostMapping`
- **Pass data to views** using the `Model` object and `model.addAttribute()`
- **Build dynamic templates** with Thymeleaf syntax (`th:text`, `th:each`, `th:if`, `th:object`, `th:field`)
- **Process HTML forms** with proper GET/POST handling and redirect-after-POST pattern
- **Integrate database operations** connecting controllers to repositories through services
- **Trace the complete request flow** from browser through all layers and back

This is where everything converges. Collections from Phase 1 become lists displayed with `th:each`. HTML from Phase 2 becomes Thymeleaf templates. SQL and JdbcTemplate from Phases 3-4 feed data to your web pages. This topic synthesizes the entire semester into working web applications.

---

## Why This Matters

### The Transformation: Console to Web

Until now, your Java applications have been console-based. Users interact through `Scanner` and see output through `System.out.println()`. That's fine for learning, but professional applications are web-based.

**Kailua Car Rental (console):**
```
Enter car ID to view: 5
Car: Mercedes S-Class, Luxury, Available
```

**Onskeskyen Wishlist (web):**
A browser displays a styled page with your wishlist items, buttons to add/edit/delete, and navigation to other pages.

The shift from console to web isn't just about prettier output. It's about:
- **Multiple users simultaneously** accessing your application
- **Stateless communication** via HTTP requests and responses
- **Separation of concerns** keeping business logic away from presentation
- **Professional deployment** to cloud servers accessible from anywhere

### The MVC Paradigm Shift

In console applications, your code does everything: read input, process data, display output. In MVC web applications, these concerns are separated:

**Model:** The data and business logic (your domain classes, services, repositories)
**View:** The presentation layer (Thymeleaf templates rendering HTML)
**Controller:** The coordinator (receives requests, calls services, prepares data for views)

This separation is not arbitrary. It enables:
- **Team collaboration:** Front-end developers work on views while back-end developers handle logic
- **Testability:** Test business logic without a browser; test views without a database
- **Maintainability:** Change the look without touching logic; change logic without touching presentation
- **Scalability:** Deploy components separately; optimize bottlenecks independently

### Connecting to What You Know

**From HTML (Phase 2):** Your knowledge of semantic elements, forms, and structure becomes the foundation of Thymeleaf templates. The HTML you wrote is now dynamic, populated with data from Java.

**From Database-Java Integration (Phase 4):** The repository pattern you learned for Kailua works identically here. `CarRepository.findAll()` returns `List<Car>` - now that list flows through a controller to a template, displaying cars in a browser.

**From Collections (Phase 1):** `List<Car>` is still your container. The `th:each` directive iterates over it just like an enhanced for-loop would.

**From GRASP (Systems Development):** The Controller principle maps directly to `@Controller` classes. Information Expert places database access in repositories. Pure Fabrication justifies service classes.

---

## MVC Architecture: The Foundation

### Understanding the Three Components

**Model** represents your application's data and business logic. In Spring Boot, this includes:
- Domain classes (`Car`, `Customer`, `Wishlist`)
- Service classes containing business rules
- Repository classes accessing the database
- The `Model` object that carries data to views

**View** renders the user interface. In our stack:
- Thymeleaf templates (`.html` files in `src/main/resources/templates/`)
- These are HTML files with special `th:` attributes
- Thymeleaf processes these server-side, producing pure HTML sent to browsers

**Controller** handles HTTP requests and coordinates between Model and View:
- Receives browser requests (GET for viewing, POST for submitting)
- Calls services to perform business operations
- Prepares data and adds it to the Model
- Returns the name of the view to render

### Why MVC Matters for Exams

When asked "explain MVC," don't just list the components. Explain the **separation of concerns**:

*"MVC separates the application into three interconnected parts. The Controller handles user requests and decides what to do. It calls the Model layer for data and business logic. The Model doesn't know about web requests - it just provides data. The View renders the response using data from the Model, without containing business logic. This separation means I can change how something looks without changing how it works, and vice versa."*

### The Request-Response Cycle

Every web interaction follows this cycle:

1. **Browser sends HTTP request** (GET /cars or POST /cars/create)
2. **DispatcherServlet receives it** (Spring's front controller)
3. **Routes to your @Controller method** based on URL mapping
4. **Controller executes:**
   - Calls services for business operations
   - Adds data to Model
   - Returns view name
5. **Thymeleaf processes template** using Model data
6. **HTML response sent to browser**

This cycle is the heartbeat of web applications. Every click, every form submission, every page view follows this pattern.

---

## Controllers: Handling HTTP Requests

### What is a Controller?

A Controller is a Java class that handles web requests. The `@Controller` annotation tells Spring that this class contains handler methods for HTTP requests.

```java
@Controller
public class CarController {

    private final CarService carService;

    public CarController(CarService carService) {
        this.carService = carService;
    }

    @GetMapping("/cars")
    public String listCars(Model model) {
        List<Car> cars = carService.getAllCars();
        model.addAttribute("cars", cars);
        return "car-list";  // renders templates/car-list.html
    }
}
```

**Key points:**
- `@Controller` marks this class for component scanning
- Constructor injection provides the `CarService` dependency
- `@GetMapping("/cars")` maps HTTP GET requests to `/cars` URL
- `Model model` is provided by Spring to pass data to the view
- The return value `"car-list"` is the template name (without `.html`)

### @GetMapping vs @PostMapping

HTTP defines different methods for different purposes. We use two primarily:

**GET requests** retrieve data without changing server state:
- Viewing a page
- Searching (parameters in URL)
- Navigation links

**POST requests** submit data that changes server state:
- Creating new records
- Updating existing records
- Submitting forms

```java
// GET: Display the form for creating a new car
@GetMapping("/cars/new")
public String showCreateForm(Model model) {
    model.addAttribute("car", new Car());  // Empty object for form binding
    return "car-form";
}

// POST: Process the submitted form
@PostMapping("/cars/create")
public String createCar(@RequestParam String brand,
                        @RequestParam String model,
                        @RequestParam String category) {
    carService.createCar(brand, model, category);
    return "redirect:/cars";  // Redirect to list page
}
```

### Request Parameter Extraction

Controllers need data from requests. Spring provides annotations to extract this data:

**@RequestParam** extracts query parameters or form fields:
```java
// URL: /cars/search?category=Luxury
@GetMapping("/cars/search")
public String searchCars(@RequestParam String category, Model model) {
    List<Car> cars = carService.findByCategory(category);
    model.addAttribute("cars", cars);
    return "car-list";
}
```

**@PathVariable** extracts values from URL path:
```java
// URL: /cars/5
@GetMapping("/cars/{id}")
public String viewCar(@PathVariable int id, Model model) {
    Car car = carService.findById(id);
    model.addAttribute("car", car);
    return "car-detail";
}
```

**When to use which:**
- Use `@PathVariable` for resource identifiers (`/cars/5`, `/users/hans`)
- Use `@RequestParam` for optional filters (`/cars?category=Luxury&available=true`)

### The Model Object

The `Model` interface is Spring's container for passing data from controllers to views. Think of it as a map of name-value pairs that Thymeleaf can access.

```java
@GetMapping("/dashboard")
public String showDashboard(Model model) {
    model.addAttribute("username", "Hans Jensen");
    model.addAttribute("cars", carService.getAllCars());
    model.addAttribute("totalRentals", rentalService.countActive());
    return "dashboard";
}
```

In the template, these become available as `${username}`, `${cars}`, `${totalRentals}`.

**Important:** Model data only lasts for one request. When the browser makes a new request, previous Model data is gone. This is fundamental to understanding stateless HTTP.

---

## Thymeleaf: Dynamic Templates

### What is Thymeleaf?

Thymeleaf is a server-side template engine. It takes HTML files with special attributes (`th:*`) and processes them into pure HTML before sending to the browser.

**Key insight:** Thymeleaf templates are valid HTML. You can open them directly in a browser for design preview. The `th:` attributes are ignored by browsers but processed by Thymeleaf on the server.

### Template Location

Thymeleaf templates live in `src/main/resources/templates/`. When a controller returns `"car-list"`, Thymeleaf looks for `templates/car-list.html`.

### Expression Types

Thymeleaf uses three expression syntaxes:

**Variable Expression `${...}`** - Access Model attributes:
```html
<p th:text="${username}">Default Name</p>
<p th:text="${car.brand}">Default Brand</p>
```

**Selection Expression `*{...}`** - Access properties of `th:object`:
```html
<form th:object="${car}">
    <input type="text" th:field="*{brand}" />  <!-- Same as ${car.brand} -->
</form>
```

**URL Expression `@{...}`** - Build URLs with context path:
```html
<a th:href="@{/cars}">View All Cars</a>
<a th:href="@{/cars/{id}(id=${car.carId})}">View Details</a>
```

### Core Thymeleaf Attributes

#### th:text - Setting Text Content

Replaces element content with evaluated expression:

```html
<h1 th:text="${pageTitle}">Default Title</h1>
<span th:text="${car.brand + ' ' + car.model}">Mercedes S-Class</span>
```

The text inside the element ("Default Title") is replaced when Thymeleaf processes it. This default text enables design preview without running the server.

#### th:each - Iterating Collections

This is where Collections from Phase 1 connect to web development. `th:each` iterates over any `Iterable`:

```html
<table>
    <tr th:each="car : ${cars}">
        <td th:text="${car.brand}">Mercedes</td>
        <td th:text="${car.model}">S-Class</td>
        <td th:text="${car.pricePerDay}">1200</td>
    </tr>
</table>
```

**How it works:**
- `${cars}` is the `List<Car>` from the Model
- `car` is the iteration variable (like `for (Car car : cars)`)
- The `<tr>` element is repeated for each car in the list

**Connecting to Collections:** The `List<Car>` returned by `carRepository.findAll()` flows unchanged from repository to service to controller to template. `th:each` is the template equivalent of your enhanced for-loop.

#### th:if and th:unless - Conditional Rendering

Show or hide elements based on conditions:

```html
<div th:if="${cars.isEmpty()}">
    <p>No cars available at this time.</p>
</div>

<table th:unless="${cars.isEmpty()}">
    <tr th:each="car : ${cars}">
        <!-- Car rows -->
    </tr>
</table>

<span th:if="${car.available}" class="badge-available">Available</span>
<span th:unless="${car.available}" class="badge-unavailable">Rented</span>
```

`th:if` renders the element only when the expression is true.
`th:unless` renders the element only when the expression is false.

#### th:href - Dynamic Links

Build navigation links with URL expressions:

```html
<!-- Simple link -->
<a th:href="@{/cars}">All Cars</a>

<!-- Link with path variable -->
<a th:href="@{/cars/{id}(id=${car.carId})}">View Details</a>

<!-- Link with query parameters -->
<a th:href="@{/cars/search(category=${selectedCategory})}">Search</a>
```

**Why @{} instead of hardcoding?** The URL expression handles context paths automatically. If your app deploys at `/myapp/`, `@{/cars}` becomes `/myapp/cars`. Hardcoded `/cars` would break.

#### th:action - Form Submission URL

Sets where forms submit their data:

```html
<form th:action="@{/cars/create}" method="post">
    <!-- Form fields -->
    <button type="submit">Create Car</button>
</form>
```

#### th:object and th:field - Form Binding

These work together to bind forms to Java objects:

```html
<form th:action="@{/cars/create}" th:object="${car}" method="post">
    <input type="text" th:field="*{brand}" placeholder="Brand" />
    <input type="text" th:field="*{model}" placeholder="Model" />
    <input type="number" th:field="*{pricePerDay}" placeholder="Price/Day" />
    <button type="submit">Create</button>
</form>
```

**How binding works:**
- `th:object="${car}"` sets the form's backing object
- `th:field="*{brand}"` binds to `car.getBrand()`/`car.setBrand()`
- On GET: Field displays current property value
- On POST: Field value sets the property

**Controller for form binding:**
```java
@GetMapping("/cars/new")
public String showForm(Model model) {
    model.addAttribute("car", new Car());  // Empty object for binding
    return "car-form";
}

@PostMapping("/cars/create")
public String processForm(@ModelAttribute Car car) {
    carService.save(car);
    return "redirect:/cars";
}
```

---

## Form Processing: GET and POST Patterns

### The Two-Method Form Pattern

Most forms require two controller methods:

1. **GET method** displays the form (empty or pre-populated)
2. **POST method** processes the submission

```java
// Display form for new wishlist item
@GetMapping("/items/new")
public String showItemForm(Model model) {
    model.addAttribute("item", new WishlistItem());
    return "item-form";
}

// Process form submission
@PostMapping("/items/create")
public String createItem(@ModelAttribute WishlistItem item) {
    itemService.save(item);
    return "redirect:/items";
}
```

### Redirect After POST (PRG Pattern)

**The Problem:** If a POST request returns a view directly, browser refresh resubmits the form, creating duplicate data.

**The Solution:** Post-Redirect-Get (PRG) pattern. After processing POST, redirect to a GET endpoint:

```java
@PostMapping("/items/create")
public String createItem(@ModelAttribute WishlistItem item) {
    itemService.save(item);
    return "redirect:/items";  // Redirect, don't return view directly
}
```

**Flow:**
1. User submits form (POST /items/create)
2. Server processes, saves data
3. Server responds with redirect (302) to /items
4. Browser makes GET request to /items
5. User sees updated list

Now if user refreshes, they refresh the GET /items - no duplicate submission.

### Editing Existing Records

For edit forms, load the existing object:

```java
@GetMapping("/items/{id}/edit")
public String showEditForm(@PathVariable int id, Model model) {
    WishlistItem item = itemService.findById(id);
    model.addAttribute("item", item);
    return "item-form";  // Same form, pre-populated
}

@PostMapping("/items/{id}/update")
public String updateItem(@PathVariable int id, @ModelAttribute WishlistItem item) {
    item.setItemId(id);  // Ensure ID is set
    itemService.update(item);
    return "redirect:/items";
}
```

---

## Complete Request Flow: Tracing Data Through the System

### Understanding the Full Journey

This is a critical exam topic. You must be able to trace a request from browser to database and back. Let's follow a request to view all wishlist items:

**Step 1: Browser Request**
User clicks "View My Wishlist" link. Browser sends:
```
GET /items HTTP/1.1
Host: localhost:8080
```

**Step 2: DispatcherServlet Routing**
Spring's DispatcherServlet receives the request and finds a matching handler:
- URL `/items` matches `@GetMapping("/items")`
- Method `listItems()` in `ItemController` is selected

**Step 3: Controller Executes**
```java
@GetMapping("/items")
public String listItems(Model model) {
    List<WishlistItem> items = itemService.getAllItems();
    model.addAttribute("items", items);
    return "item-list";
}
```

**Step 4: Service Layer**
```java
public List<WishlistItem> getAllItems() {
    return itemRepository.findAll();
}
```

**Step 5: Repository Layer**
```java
public List<WishlistItem> findAll() {
    String sql = "SELECT * FROM wishlist_items ORDER BY priority";
    return jdbcTemplate.query(sql, itemRowMapper);
}
```

**Step 6: Database Query**
JdbcTemplate executes: `SELECT * FROM wishlist_items ORDER BY priority`
MySQL returns result rows.

**Step 7: RowMapper Conversion**
For each row, RowMapper creates a `WishlistItem` object:
```java
item.setItemId(rs.getInt("item_id"));
item.setName(rs.getString("name"));
item.setPriority(rs.getInt("priority"));
```

**Step 8: Data Returns Up the Stack**
- RowMapper returns `WishlistItem` objects
- JdbcTemplate collects them into `List<WishlistItem>`
- Repository returns the List
- Service returns the List (potentially with business logic)
- Controller adds List to Model

**Step 9: Thymeleaf Processing**
Thymeleaf finds `templates/item-list.html`:
```html
<tr th:each="item : ${items}">
    <td th:text="${item.name}">Item Name</td>
    <td th:text="${item.priority}">1</td>
</tr>
```
It iterates over `${items}`, generating HTML rows.

**Step 10: Browser Receives HTML**
```html
<tr>
    <td>Nintendo Switch</td>
    <td>1</td>
</tr>
<tr>
    <td>Wireless Headphones</td>
    <td>2</td>
</tr>
```
Browser renders the table for the user.

### Visual Representation

```
Browser (User clicks "View Wishlist")
    |
    | GET /items
    v
DispatcherServlet
    |
    | Routes to handler
    v
ItemController.listItems(Model model)
    |
    | itemService.getAllItems()
    v
ItemService
    |
    | itemRepository.findAll()
    v
ItemRepository
    |
    | jdbcTemplate.query(sql, rowMapper)
    v
MySQL Database
    |
    | Returns ResultSet rows
    v
RowMapper (converts each row to WishlistItem)
    |
    v
List<WishlistItem> returns up through layers
    |
    v
Controller: model.addAttribute("items", items)
    |
    | return "item-list"
    v
Thymeleaf processes item-list.html with Model data
    |
    v
HTML Response sent to Browser
    |
    v
User sees wishlist items displayed
```

---

## Layered Architecture and GRASP Principles

### Controller -> Service -> Repository

Spring Boot applications follow a layered architecture with clear responsibilities:

**Controller Layer (@Controller)**
- Receives HTTP requests
- Extracts parameters
- Calls services
- Prepares Model for views
- Returns view names

**Service Layer (@Service)**
- Contains business logic
- Coordinates between repositories
- Transaction boundaries
- No HTTP or view concerns

**Repository Layer (@Repository)**
- Database access
- SQL execution via JdbcTemplate
- RowMapper implementations
- No business logic

### GRASP Principles in Spring Boot

This architecture isn't arbitrary - it embodies GRASP principles you learned in Systems Development:

**Controller (GRASP):** The `@Controller` class handles incoming requests and delegates work. It doesn't contain business logic; it coordinates.

**Information Expert:** Repository classes have the database connection and SQL knowledge, so they handle data access operations. `CarRepository` knows how to find cars because it has `JdbcTemplate` and the RowMapper.

**Pure Fabrication:** Service classes don't represent real-world objects. They're invented to hold business logic that doesn't belong in domain classes or repositories. `RentalService` calculates prices and validates availability - logic too complex for controllers, not database-specific enough for repositories.

**Low Coupling:** By injecting dependencies through constructors, classes don't create their own dependencies. Controllers receive services; services receive repositories. Changing a repository implementation doesn't require changing the controller.

**High Cohesion:** Each class has a focused purpose. `ItemController` handles item-related requests. `ItemService` handles item business logic. `ItemRepository` handles item data access.

### Why This Matters for Exams

When discussing your project architecture:

*"I organized my code following the Controller-Service-Repository pattern. Controllers handle HTTP concerns and delegate to services. Services contain business logic like calculating rental prices or validating that items aren't duplicated. Repositories handle database access using JdbcTemplate and RowMapper. This separation follows GRASP principles - repositories are Information Experts for data access, services are Pure Fabrications for business logic, and the layered structure achieves Low Coupling between components."*

---

## Progressive Complexity: Building Your Understanding

### Step 1: Hello World

The minimal Spring Boot application demonstrates the foundation:

```java
@Controller
public class HelloController {

    @GetMapping("/")
    public String hello() {
        return "hello";  // templates/hello.html
    }
}
```

```html
<!-- templates/hello.html -->
<!DOCTYPE html>
<html>
<head><title>Hello</title></head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
```

**Concepts introduced:** @Controller, @GetMapping, view name return

### Step 2: Passing Data

Add dynamic content:

```java
@GetMapping("/greeting")
public String greeting(Model model) {
    model.addAttribute("name", "KEA Student");
    model.addAttribute("currentDate", LocalDate.now());
    return "greeting";
}
```

```html
<h1>Hello, <span th:text="${name}">Guest</span>!</h1>
<p>Today is <span th:text="${currentDate}">2024-01-01</span></p>
```

**Concepts introduced:** Model object, th:text, variable expressions

### Step 3: Multiple Pages

Add navigation between pages:

```java
@GetMapping("/")
public String home() {
    return "home";
}

@GetMapping("/about")
public String about() {
    return "about";
}

@GetMapping("/contact")
public String contact() {
    return "contact";
}
```

```html
<nav>
    <a th:href="@{/}">Home</a>
    <a th:href="@{/about}">About</a>
    <a th:href="@{/contact}">Contact</a>
</nav>
```

**Concepts introduced:** Multiple endpoints, th:href, URL expressions

### Step 4: Displaying Lists

Connect Collections to templates:

```java
@GetMapping("/items")
public String listItems(Model model) {
    List<WishlistItem> items = itemService.getAllItems();
    model.addAttribute("items", items);
    return "item-list";
}
```

```html
<ul>
    <li th:each="item : ${items}" th:text="${item.name}">Item</li>
</ul>
```

**Concepts introduced:** th:each, iteration, Collection integration

### Step 5: Forms and POST

Add user input:

```java
@GetMapping("/items/new")
public String showForm() {
    return "item-form";
}

@PostMapping("/items/create")
public String createItem(@RequestParam String name,
                          @RequestParam int priority) {
    itemService.create(name, priority);
    return "redirect:/items";
}
```

```html
<form th:action="@{/items/create}" method="post">
    <input type="text" name="name" required />
    <input type="number" name="priority" value="1" />
    <button type="submit">Add Item</button>
</form>
```

**Concepts introduced:** @PostMapping, @RequestParam, redirect after POST

### Step 6: Database Integration

Complete the stack with JdbcTemplate:

```java
@GetMapping("/items")
public String listItems(Model model) {
    List<WishlistItem> items = itemService.getAllItems();
    // items came from repository -> JdbcTemplate -> MySQL
    model.addAttribute("items", items);
    return "item-list";
}
```

**Concepts integrated:** Everything from Database-Java Integration flows through to web display

---

## Application Configuration

### application.properties

Spring Boot uses `src/main/resources/application.properties` for configuration:

```properties
# Database connection
spring.datasource.url=jdbc:mysql://localhost:3306/wishlist_db
spring.datasource.username=root
spring.datasource.password=your_password

# Server configuration
server.port=8080

# Development helpers
server.error.include-stacktrace=always
spring.thymeleaf.cache=false
```

**Key properties:**
- `spring.datasource.*` - Database connection (from Database-Java Integration)
- `server.port` - Which port to run on (default 8080)
- `server.error.include-stacktrace=always` - Shows full errors during development
- `spring.thymeleaf.cache=false` - Disable caching for live template updates

### Project Structure

A typical Spring Boot project:

```
src/
├── main/
│   ├── java/
│   │   └── com/example/wishlist/
│   │       ├── WishlistApplication.java     # Main class
│   │       ├── controller/
│   │       │   └── ItemController.java
│   │       ├── service/
│   │       │   └── ItemService.java
│   │       ├── repository/
│   │       │   └── ItemRepository.java
│   │       └── model/
│   │           └── WishlistItem.java
│   └── resources/
│       ├── application.properties
│       ├── templates/
│       │   ├── home.html
│       │   └── item-list.html
│       └── static/
│           └── css/
│               └── style.css
└── test/
```

---

## Common Struggles and Solutions

### Struggle 1: MVC Separation Confusion

**Question:** "Where should this code go - controller, service, or repository?"

**Decision Framework:**
- Does it handle HTTP request/response? **Controller**
- Does it contain business rules or coordinate operations? **Service**
- Does it access the database? **Repository**
- Is it just data with getters/setters? **Domain class**

**Example:**
- Calculating total wishlist value: **Service** (business logic)
- Getting items from database: **Repository** (data access)
- Formatting value for display: **Template** (presentation)
- Deciding which template to show: **Controller** (request handling)

### Struggle 2: Thymeleaf Syntax Errors

**Problem:** Template doesn't render data.

**Common causes:**
1. Typo in variable name (`${itms}` instead of `${items}`)
2. Missing `th:` prefix (`text="${x}"` instead of `th:text="${x}"`)
3. Model attribute not added in controller
4. Template file name mismatch

**Debugging approach:**
1. Check controller adds the attribute
2. Check attribute name matches template exactly
3. Check template file exists in `templates/`
4. Look at browser page source - is data missing or is template not found?

### Struggle 3: @GetMapping vs @PostMapping

**Confusion:** "When do I use which?"

**Rule of thumb:**
- **GET:** User wants to see something (view page, search, list items)
- **POST:** User wants to change something (create, update, delete)

**Warning signs you're using the wrong one:**
- GET method that modifies database data
- POST method that just displays a page
- Form with `method="get"` that creates records

### Struggle 4: th:object and th:field Relationship

**Problem:** Form binding doesn't work.

**Requirements for binding:**
1. Controller must add object to model: `model.addAttribute("car", new Car())`
2. Form must have `th:object="${car}"`
3. Fields must use selection expression: `th:field="*{brand}"` (not `${car.brand}`)
4. For POST, use `@ModelAttribute Car car` parameter

**Debugging:**
```html
<!-- Check object is available -->
<p th:text="${car}">Car object here</p>
```

### Struggle 5: Variable vs URL vs Selection Expressions

**Confusion:** "When do I use ${}, @{}, or *{}?"

| Expression | Purpose | Example |
|------------|---------|---------|
| `${...}` | Access Model data | `th:text="${user.name}"` |
| `@{...}` | Build URLs | `th:href="@{/users/{id}(id=1)}"` |
| `*{...}` | Access th:object properties | `th:field="*{email}"` |

**Memory aid:**
- `$` for **D**ata (dollar = data)
- `@` for **A**ddresses/URLs (at = address)
- `*` for **S**election within object (star = selection)

---

## Debugging Spring Boot Applications

### Reading Error Pages

Spring Boot shows detailed error pages in development. Learn to read them:

1. **Check the exception type:** `NullPointerException`, `TemplateProcessingException`, etc.
2. **Find the root cause:** Scroll down for "Caused by"
3. **Look for your code:** Stack trace shows line numbers in your classes

### Common Errors

**Whitelabel Error Page (404):**
- Template file not found
- Check file name and location in `templates/`
- Check controller return value matches file name

**TemplateProcessingException:**
- Thymeleaf can't process template
- Check for syntax errors in `th:` attributes
- Check referenced variables exist in Model

**NullPointerException in Controller:**
- Service or repository not injected
- Missing `@Service` or `@Repository` annotation
- Missing constructor injection

**Database Connection Error:**
- Check `application.properties` values
- Verify MySQL is running
- Check database name, username, password

---

## Preparing for the Oral Exam

### Questions You Must Answer Confidently

**1. "Explain MVC architecture and how Spring Boot implements it."**

*"MVC separates applications into Model, View, and Controller. In Spring Boot, Controllers are classes annotated with @Controller that handle HTTP requests and return view names. Views are Thymeleaf templates that render HTML using data from the Model. The Model is represented both by domain classes and the Model object that passes data from controller to view. This separation ensures that presentation logic stays in templates, business logic stays in services, and controllers just coordinate between them."*

**2. "Walk me through what happens when a user requests a page."**

*"When a user requests /items, Spring's DispatcherServlet receives the request and finds the matching @GetMapping method. That method calls the service layer for business logic, which calls the repository for database access. The repository uses JdbcTemplate to execute SQL and RowMapper to convert results to domain objects. The List returns up through the layers. The controller adds it to the Model and returns the view name. Thymeleaf processes the template using Model data and produces HTML that's sent to the browser."*

**3. "What Thymeleaf attributes would you use to display a list of items?"**

*"I would use th:each to iterate over the collection. For example, th:each='item : ${items}' creates a loop variable 'item' for each element. Inside, I'd use th:text to display properties like th:text='${item.name}'. For conditional display, th:if shows elements when true. For links, th:href with @{} builds URLs properly."*

**4. "How do you handle form submission in Spring Boot?"**

*"I use two controller methods. A GET method displays the form, adding an empty object to the model for binding. The form uses th:object to bind to that object and th:field for individual fields. When submitted, a POST method receives the data - either through @RequestParam for individual values or @ModelAttribute for object binding. After processing, I redirect to avoid duplicate submissions on refresh."*

**5. "How does your Spring Boot architecture follow GRASP principles?"**

*"Controllers follow the Controller principle - they handle requests and delegate work. Repositories follow Information Expert - they have the database connection and SQL knowledge, so they handle data access. Services are Pure Fabrication - they don't represent real-world concepts but exist to contain business logic. The layered structure achieves Low Coupling through dependency injection. Each layer has High Cohesion with focused responsibilities."*

### Demonstration Tips

When showing your Onskeskyen project:

1. **Start with a user flow:** "A user can create a wishlist, add items, and share it. Let me show you."

2. **Trace through the layers:** "When I click Add Item, this controller method handles it. It calls the service, which validates and calls the repository. The repository saves to MySQL."

3. **Show the Thymeleaf:** "This template uses th:each to iterate over wishlist items. The th:if shows different content when the list is empty."

4. **Connect to architecture:** "Notice how the controller doesn't know about SQL. That's the repository's job. The service handles business rules like preventing duplicate items."

5. **Explain design decisions:** "I put the price calculation in the service because it's business logic, not data access or presentation."

---

## Key Takeaways

- **MVC separates concerns:** Controllers handle requests, Services contain logic, Repositories access data, Views render output. Each has a single responsibility.

- **@Controller and @GetMapping/@PostMapping** map HTTP requests to Java methods. GET for viewing, POST for modifying.

- **Model passes data to templates.** `model.addAttribute("key", value)` makes data available as `${key}` in Thymeleaf.

- **Thymeleaf attributes process server-side:** `th:text` sets content, `th:each` iterates collections, `th:if` conditionally renders, `th:href` builds URLs, `th:object`/`th:field` bind forms.

- **The complete flow:** Browser -> Controller -> Service -> Repository -> Database -> RowMapper -> back up through layers -> Model -> Thymeleaf -> HTML -> Browser.

- **GRASP principles apply:** Controller pattern, Information Expert (repositories), Pure Fabrication (services), Low Coupling (dependency injection).

- **Redirect after POST** prevents duplicate submissions.

- **This topic integrates everything:** Collections for data structures, HTML for template structure, SQL for database queries, JdbcTemplate for Java-database bridge.

---

## For the Next Topic Agent

### Terminology Established This Topic

- **MVC Architecture:** Model-View-Controller pattern separating data (Model), presentation (View), and request handling (Controller). Spring Boot implements this with `@Controller` classes, Thymeleaf templates, and the `Model` object.

- **@Controller:** Spring annotation marking a class as a web controller. Handles HTTP requests, coordinates with services, adds data to Model, returns view names.

- **@GetMapping / @PostMapping:** Annotations mapping HTTP GET and POST requests to handler methods. Include URL path as argument: `@GetMapping("/items")`.

- **Model Object:** Spring interface for passing data from controller to view. Methods: `addAttribute(String name, Object value)`. Data available in templates as `${name}`.

- **Thymeleaf:** Server-side template engine processing HTML with `th:*` attributes. Key attributes:
  - `th:text="${variable}"` - set element text content
  - `th:each="item : ${items}"` - iterate collection
  - `th:if="${condition}"` - conditional rendering
  - `th:unless="${condition}"` - inverse conditional
  - `th:href="@{/path}"` - build URLs
  - `th:action="@{/submit}"` - form submission URL
  - `th:object="${obj}"` - form binding context
  - `th:field="*{property}"` - bind form field to object property

- **Expression Types:**
  - `${...}` Variable Expression - access Model attributes
  - `@{...}` URL Expression - build URLs with context path
  - `*{...}` Selection Expression - access properties of th:object

- **Request Parameters:**
  - `@RequestParam` - extract from query string or form fields
  - `@PathVariable` - extract from URL path segments
  - `@ModelAttribute` - bind form to object

- **Redirect After POST (PRG):** Pattern preventing duplicate submissions. POST handler returns `"redirect:/path"` instead of view name.

- **Layered Architecture:** Controller -> Service -> Repository pattern organizing code by responsibility. Implements GRASP principles.

- **application.properties:** Spring Boot configuration file in `src/main/resources/`. Contains database connection, server settings, development options.

### Example Classes/Code Created

- **ItemController:** Complete controller with list view, create form (GET), create handler (POST), edit form, update handler. Demonstrates all major patterns.

- **Thymeleaf Templates:** Examples of item list with th:each iteration, conditional empty state with th:if, form with th:object/th:field binding, navigation with th:href.

- **Complete Request Flow Trace:** Step-by-step walkthrough from browser request through all layers to database and back, with visual diagram.

### Student Capabilities After This Topic

Students who complete this material can now:
- Create Spring Boot web applications with multiple pages
- Implement controllers with GET and POST mappings
- Pass data from controllers to Thymeleaf templates
- Use all core Thymeleaf attributes (th:text, th:each, th:if, th:href, th:object, th:field)
- Process form submissions with proper redirect-after-POST
- Connect web layer to database through service and repository layers
- Trace requests through the complete MVC stack
- Explain architecture decisions using GRASP principles
- Debug common Spring Boot and Thymeleaf errors

### Pedagogical Patterns Used

- **Progressive Complexity Sequence:** Hello World -> Data Passing -> Multiple Pages -> Lists -> Forms -> Database. Each step adds one concept.

- **Complete Flow Tracing:** Detailed step-by-step walkthrough of request lifecycle, connecting all layers students have learned.

- **GRASP Connection:** Explicit mapping of Spring Boot patterns to GRASP principles from Systems Development course.

- **Prior Topic Integration:** Collections (th:each iterates List), HTML (Thymeleaf templates are HTML), Database-Java Integration (JdbcTemplate/RowMapper unchanged in web context).

- **Exam Question Anticipation:** Sample questions with model answers demonstrating expected depth of understanding.

- **Common Struggles Section:** Targeted solutions for MVC confusion, Thymeleaf syntax, expression selection.

### Integration Notes for Next Topic (Sessions, IoC & DI)

The next topic builds on Spring Boot fundamentals:

1. **Sessions extend statelessness:** HTTP is stateless; sessions enable user state across requests. Controller methods gain `HttpSession` parameter.

2. **IoC/DI explains "magic":** Students have been using `@Autowired` (constructor injection) without understanding why. Next topic explains Inversion of Control principle.

3. **Architecture deepens:** Same Controller -> Service -> Repository pattern, but with explicit discussion of Spring container, bean lifecycle, scopes.

4. **Authentication pattern:** Sessions enable login/logout functionality for Onskeskyen project.

The critical insight: Spring Boot's convenient annotations hide complex IoC/DI machinery. The next topic pulls back the curtain, explaining why constructor injection works and how Spring manages object lifecycles.
