# HTML5 Fundamentals - 2nd Semester Programming

*Prerequisites: Basic web browser usage, understanding of client-server communication*
*Phase: 2 - Database Fundamentals*
*Exam Weight: Moderate (foundational for web development)*

---

## What You'll Learn

By the end of this topic, you will be able to:
- **Create semantically structured HTML pages** using HTML5 elements that describe their meaning
- **Build functional forms** for user data collection with appropriate input types
- **Organize document structure** with proper head, body, and meta information
- **Use common HTML elements** effectively for content presentation
- **Understand HTML's role** in the Model-View-Controller (MVC) architecture as the View layer

This knowledge is foundational for Phase 5 when you'll use Thymeleaf to add dynamic behavior to HTML templates. Every Spring Boot web application you build will rely on these HTML skills.

---

## Why This Matters

### The Visual Layer of Your Applications

Until now, your Java programs have communicated through the console - text output that disappears when the window closes. HTML transforms your applications into something users can see, interact with, and navigate.

When you build the Onskeskyen (Wishlist) project, users will:
- See their wishlists in a structured, readable format
- Fill out forms to add new items
- Navigate between different pages
- Submit data back to your Java controllers

HTML is the language that makes all of this possible.

### HTML Is the "V" in MVC

Understanding HTML's role in architecture is crucial for your exam:

```
[Controller]     [Model]          [View]
@Controller  --> Collections --> HTML Template
Java code        Domain objects   What user sees
```

Your Spring Boot controllers will pass data to HTML templates. The template's job is to present that data in a structured, meaningful way. Semantic HTML ensures that:
- The structure is meaningful to both browsers and developers
- Accessibility tools can understand your content
- Search engines can properly index your pages
- Future developers (including you) can maintain the code

### Foundation for Thymeleaf

In Phase 5, you'll learn Thymeleaf - a template engine that adds dynamic behavior to HTML. Thymeleaf syntax looks like this:

```html
<p th:text="${customer.name}">Placeholder Name</p>
```

Notice that this is valid HTML with an extra attribute (`th:text`). Thymeleaf works *with* HTML, not instead of it. Strong HTML fundamentals make Thymeleaf learning straightforward.

---

## Building on What You Know

### From 1st Semester

While HTML isn't a programming language like Java, your programming background helps in several ways:

**Structured Thinking**: HTML documents have a tree structure (parent-child relationships) similar to object hierarchies in Java. Just as a `Car` object might contain `Engine` and `Wheel` objects, an HTML `<body>` contains `<header>`, `<main>`, and `<footer>` elements.

**Attributes as Parameters**: HTML elements can have attributes, similar to method parameters:
```html
<input type="email" name="customerEmail" required>
```
This is conceptually similar to calling a method with specific parameters.

**Interfaces and Contracts**: In 1st semester, you learned that interfaces define *what* something does, not *how*. Similarly, semantic HTML elements define *what* content means, not how it looks. A `<nav>` element means "this is navigation" regardless of whether it displays as a horizontal menu, sidebar, or dropdown.

### From Earlier This Semester

**Collections Flow to Views**: In the ADT & Collections topic, you learned about data flow through application layers. You saw this visualization:

```
[Database] --> [Java Collections] --> [Web Template] --> [Browser]
```

HTML is where this flow terminates. When your controller passes a `List<Wishlist>` to a template, HTML (enhanced with Thymeleaf) displays that collection to the user.

**Choosing the Right Tool**: Just as you learned to choose between List, Set, and Map based on requirements, you'll now learn to choose between HTML elements based on content meaning. A navigation menu goes in `<nav>`, not `<div>`. An article goes in `<article>`, not just `<p>` tags.

---

## HTML Document Structure

### What: The Foundation of Every Web Page

Every HTML document follows a standard structure that browsers expect:

```html
<!DOCTYPE html>
<html lang="da">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kailua Car Rental</title>
    <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
    <!-- Visible content goes here -->
</body>
</html>
```

### Why: Each Part Has a Purpose

**`<!DOCTYPE html>`**: Tells the browser this is an HTML5 document. Without it, browsers may render pages in "quirks mode" with inconsistent behavior.

**`<html lang="da">`**: The root element. The `lang` attribute helps screen readers pronounce content correctly and assists search engines. Use "da" for Danish, "en" for English.

**`<head>`**: Contains metadata - information *about* the page, not displayed content. This includes:
- `<meta charset="UTF-8">`: Character encoding supporting Danish characters (ø, æ, å)
- `<meta name="viewport">`: Essential for mobile-responsive design
- `<title>`: Appears in browser tabs and bookmarks
- `<link>`: References to CSS stylesheets

**`<body>`**: All visible content. This is where you build your page structure.

### How: Creating Well-Structured Documents

**Step 1**: Start with the doctype and html element
**Step 2**: Add essential meta tags in the head
**Step 3**: Set a meaningful title
**Step 4**: Link your CSS files
**Step 5**: Build your content in the body

### Action: Apply to Your Projects

In your Kailua or Onskeskyen projects, every HTML file should begin with this structure. The title should reflect the current page: "Kailua - Available Cars", "Onskeskyen - My Wishlists".

### Common Mistakes

**Missing DOCTYPE**: Can cause rendering inconsistencies across browsers.

**No charset declaration**: Danish characters may display incorrectly (showing ? or garbled text instead of ø, æ, å).

**Missing viewport meta**: Pages won't scale properly on mobile devices.

**Title describes the whole site, not the page**: Each page should have a unique, descriptive title.

---

## HTML5 Semantic Elements

### What: Elements That Describe Their Meaning

Semantic elements tell browsers (and developers) what kind of content they contain. Compare:

**Non-semantic** (tells you nothing about content):
```html
<div class="header">...</div>
<div class="navigation">...</div>
<div class="main-content">...</div>
```

**Semantic** (self-describing):
```html
<header>...</header>
<nav>...</nav>
<main>...</main>
```

### Why: Meaningful Structure Matters

**Accessibility**: Screen readers use semantic elements to help visually impaired users navigate. They can announce "navigation, 5 links" or "main content starts here."

**Maintainability**: When you return to your code after the exam break, `<article>` immediately tells you what that section contains. `<div class="article-wrapper">` requires you to read the class name and hope it's accurate.

**SEO and Indexing**: Search engines understand that content in `<main>` is the primary content, while content in `<aside>` is supplementary.

**GRASP Connection**: Using semantic elements follows the Information Expert principle - each element "knows" what kind of content it should contain and communicates that clearly.

### How: The Core Semantic Elements

| Element | Purpose | Example Content |
|---------|---------|-----------------|
| `<header>` | Introductory content, usually contains navigation | Logo, site title, main menu |
| `<nav>` | Navigation links | Menu, breadcrumbs, pagination |
| `<main>` | The dominant, unique content | Only one per page |
| `<article>` | Self-contained, independently distributable content | Blog post, product card, wishlist item |
| `<section>` | Thematic grouping with a heading | Chapter, tab content, feature section |
| `<aside>` | Content tangentially related to main content | Sidebar, pull quotes, related links |
| `<footer>` | Footer for its nearest sectioning content | Copyright, contact info, secondary links |

### Structural Example

Here's how these elements combine in a typical page structure:

```html
<body>
    <header>
        <h1>Onskeskyen</h1>
        <nav>
            <a href="/wishlists">My Wishlists</a>
            <a href="/shared">Shared With Me</a>
            <a href="/logout">Log Out</a>
        </nav>
    </header>

    <main>
        <section>
            <h2>My Wishlists</h2>
            <!-- List of wishlists -->
        </section>
    </main>

    <footer>
        <p>Onskeskyen - KEA 2024</p>
    </footer>
</body>
```

### Action: Think Structure Before Coding

Before writing HTML, sketch your page structure:
1. What's in the header?
2. What navigation does the user need?
3. What's the main content?
4. Is there sidebar content?
5. What goes in the footer?

Then choose semantic elements that match your sketch.

### Common Mistakes

**Using `<div>` for everything**: If content has meaning, use a semantic element. Reserve `<div>` for pure layout needs.

**Multiple `<main>` elements**: There should be only one `<main>` per page, representing the unique content.

**Confusing `<section>` and `<article>`**: Use `<article>` when content could stand alone (syndicated, shared, reused). Use `<section>` for thematic grouping that requires the page context.

**Putting navigation outside `<nav>`**: The `<nav>` element should wrap navigation links, even if they appear in a header or footer.

---

## Common HTML Elements

### What: The Building Blocks of Content

While semantic elements provide structure, you need content elements to display information:

**Text Elements:**
- `<h1>` through `<h6>`: Headings (h1 is most important, h6 least)
- `<p>`: Paragraphs
- `<span>`: Inline text (for styling or targeting specific text)

**List Elements:**
- `<ul>`: Unordered list (bullet points)
- `<ol>`: Ordered list (numbered)
- `<li>`: List item (goes inside ul or ol)

**Links and Media:**
- `<a>`: Hyperlinks to other pages or resources
- `<img>`: Images (self-closing)

**Tables:**
- `<table>`: Data table container
- `<tr>`: Table row
- `<th>`: Table header cell
- `<td>`: Table data cell

**Generic Containers:**
- `<div>`: Block-level container (for grouping)
- `<span>`: Inline container (for targeting text)

### Why: Content Needs Appropriate Markup

Each element carries meaning and default behavior:

- Headings create document outline and hierarchy
- Lists make content scannable and accessible
- Links are keyboard-navigable and screen-reader friendly
- Tables are for tabular data (not layout)

### How: Displaying Data From Collections

When you display a `List<Car>` in your Kailua project, HTML structure matters:

```html
<table>
    <tr>
        <th>License Plate</th>
        <th>Brand</th>
        <th>Model</th>
        <th>Price/Day</th>
    </tr>
    <tr>
        <td>AB12345</td>
        <td>Toyota</td>
        <td>Corolla</td>
        <td>450 DKK</td>
    </tr>
    <!-- More rows... -->
</table>
```

With Thymeleaf (Phase 5), you'll dynamically generate rows:

```html
<tr th:each="car : ${cars}">
    <td th:text="${car.licensePlate}">AB12345</td>
    <td th:text="${car.brand}">Toyota</td>
    <td th:text="${car.model}">Corolla</td>
    <td th:text="${car.pricePerDay}">450</td>
</tr>
```

### Heading Hierarchy

Headings should follow a logical order - don't skip levels:

```html
<!-- Correct hierarchy -->
<h1>Kailua Car Rental</h1>
  <h2>Available Cars</h2>
    <h3>Economy Class</h3>
    <h3>Luxury Class</h3>
  <h2>Make a Reservation</h2>

<!-- Wrong: skipping from h1 to h3 -->
<h1>Kailua Car Rental</h1>
  <h3>Available Cars</h3>  <!-- Should be h2 -->
```

### Action: Match Elements to Content Type

Ask yourself:
- Is this a heading? Use h1-h6
- Is this a paragraph? Use p
- Is this a list of items? Use ul/ol with li
- Is this tabular data with rows and columns? Use table
- Is this a link to another page? Use a
- Is this an image? Use img

### Common Mistakes

**Using headings for size instead of meaning**: Don't use `<h3>` because you want smaller text. Use CSS for styling.

**Tables for layout**: Tables are for data, not for positioning elements on the page.

**Images without alt text**: Always provide `<img src="car.jpg" alt="Red Toyota Corolla">` for accessibility.

**Skipping heading levels**: Don't jump from h1 to h4. Each level should logically follow the previous.

---

## HTML Forms: Collecting User Data

### What: Interactive Elements for Input

Forms are how users provide data to your application. Every wishlist item, every car rental, every login requires a form.

```html
<form action="/submit-rental" method="POST">
    <label for="customer">Customer Name:</label>
    <input type="text" id="customer" name="customerName" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="customerEmail" required>

    <button type="submit">Submit Rental</button>
</form>
```

### Why: Forms Connect Frontend to Backend

Forms are the bridge between what users type and what your Java controller receives. When a user submits this form:

```html
<input type="text" name="customerName" value="Anders Jensen">
```

Your Spring Boot controller receives:
```java
@PostMapping("/submit-rental")
public String submitRental(@RequestParam String customerName) {
    // customerName = "Anders Jensen"
}
```

The `name` attribute determines the parameter name in your Java code. This connection is fundamental to full-stack development.

### How: Form Attributes Explained

**`action`**: The URL to submit to (your controller's @PostMapping endpoint)
**`method`**: HTTP method (GET for queries, POST for data submission)

```html
<form action="/customers/add" method="POST">
```

This submits to a controller method like:
```java
@PostMapping("/customers/add")
public String addCustomer(...) { }
```

### Input Types: Choosing the Right One

HTML5 provides specialized input types that improve user experience and provide basic validation:

| Type | Purpose | Browser Behavior |
|------|---------|------------------|
| `text` | General text | Standard text box |
| `email` | Email address | Validates @ symbol, provides email keyboard on mobile |
| `password` | Passwords | Masks input with dots |
| `number` | Numeric values | Number keyboard on mobile, spinner controls |
| `date` | Date selection | Date picker interface |
| `tel` | Phone numbers | Phone keyboard on mobile |
| `checkbox` | Yes/No options | Checkable box |
| `radio` | One-of-many selection | Mutually exclusive options |

### Input Type Examples

```html
<!-- Customer registration form -->
<label for="name">Full Name:</label>
<input type="text" id="name" name="fullName" required>

<label for="email">Email:</label>
<input type="email" id="email" name="email" required>

<label for="phone">Phone:</label>
<input type="tel" id="phone" name="phone">

<label for="birthdate">Birth Date:</label>
<input type="date" id="birthdate" name="birthDate">

<label for="rentalDays">Number of Days:</label>
<input type="number" id="rentalDays" name="days" min="1" max="30">
```

### Other Form Elements

**Textarea** - For multi-line text:
```html
<label for="notes">Special Requests:</label>
<textarea id="notes" name="specialRequests" rows="4"></textarea>
```

**Select** - Dropdown menu:
```html
<label for="carType">Car Type:</label>
<select id="carType" name="carType">
    <option value="">-- Select --</option>
    <option value="economy">Economy</option>
    <option value="standard">Standard</option>
    <option value="luxury">Luxury</option>
</select>
```

**Radio buttons** - One choice from a group:
```html
<p>Pickup Location:</p>
<input type="radio" id="airport" name="pickup" value="airport">
<label for="airport">Airport</label>

<input type="radio" id="downtown" name="pickup" value="downtown">
<label for="downtown">Downtown</label>
```

**Checkbox** - Multiple selections:
```html
<input type="checkbox" id="gps" name="extras" value="gps">
<label for="gps">GPS Navigation</label>

<input type="checkbox" id="childSeat" name="extras" value="childseat">
<label for="childSeat">Child Seat</label>
```

### Labels: Essential for Usability

Always pair inputs with labels using the `for` attribute:

```html
<!-- Correct: for matches id -->
<label for="customerEmail">Email:</label>
<input type="email" id="customerEmail" name="email">

<!-- Also correct: wrapping -->
<label>
    Email:
    <input type="email" name="email">
</label>
```

Labels are important because:
- Clicking the label focuses the input (larger click target)
- Screen readers announce the label when the input is focused
- Forms without labels are difficult to use and fail accessibility requirements

### Form Validation Attributes

HTML5 provides basic validation:

```html
<input type="email" required>        <!-- Must be filled, must be email format -->
<input type="text" minlength="2">    <!-- At least 2 characters -->
<input type="number" min="1" max="30"> <!-- Between 1 and 30 -->
<input type="text" pattern="[A-Z]{2}\d{5}"> <!-- Danish license plate format -->
```

These provide client-side validation before the form is submitted. But remember: **always validate on the server too**. Users can bypass client-side validation.

### Action: Design Forms for Your Projects

For Kailua, you'll need forms for:
- Adding new cars to inventory
- Registering customers
- Creating rental contracts

For Onskeskyen:
- Creating wishlists
- Adding items to wishlists
- User registration and login

Design these forms with appropriate input types and validation.

### Common Mistakes

**Missing `name` attribute**: Without `name`, the input's value isn't sent to the server.

**Missing `for` attribute on labels**: The label won't associate with the input properly.

**Using GET for data modification**: GET requests should be for retrieving data. POST is for creating/updating.

**No server-side validation**: Client-side validation improves UX but isn't secure. Always validate in your Java controller.

**Same `id` for multiple elements**: IDs must be unique within a page.

---

## Integration Patterns

### HTML in the MVC Architecture

Understanding where HTML fits in your Spring Boot application architecture:

```
User Browser
     |
     | HTTP Request (GET /cars)
     v
[Controller Layer]
  @Controller class
  @GetMapping("/cars")
     |
     | calls
     v
[Service Layer]
  @Service class
  carService.findAll()
     |
     | calls
     v
[Repository Layer]
  @Repository class
  jdbcTemplate.query(...)
     |
     | queries
     v
[Database]
  MySQL tables
     |
     | returns data
     |
     v
[RowMapper]
  Converts rows to Car objects
     |
     | returns List<Car>
     v
[Service Layer]
  Returns List<Car>
     |
     v
[Controller Layer]
  model.addAttribute("cars", carList)
  return "car-list"
     |
     v
[Thymeleaf + HTML]
  Processes template
  Generates final HTML
     |
     | HTTP Response
     v
User Browser
  Displays car list
```

HTML is the final output of this entire chain. All the Java code, database queries, and data transformation ultimately produce an HTML page that users see.

### Static HTML vs. Dynamic Templates

**Static HTML**: Content is fixed, doesn't change based on data
```html
<p>Welcome to our car rental service.</p>
```

**Dynamic HTML with Thymeleaf** (Phase 5): Content comes from Java
```html
<p th:text="'Welcome, ' + ${user.name}">Welcome, Guest</p>
```

In Phase 2, you're learning static HTML structure. This foundation makes dynamic templating straightforward - you're just adding `th:*` attributes to HTML you already understand.

### Form Submission Flow

When a user submits a form, here's the complete data flow:

```
1. User fills form and clicks Submit
     |
     v
2. Browser creates POST request with form data
   POST /rentals/create
   Content-Type: application/x-www-form-urlencoded

   customerName=Anders&carId=42&days=3
     |
     v
3. Spring Boot receives request
   @PostMapping("/rentals/create")
   public String createRental(
       @RequestParam String customerName,
       @RequestParam int carId,
       @RequestParam int days) {
     |
     v
4. Controller calls service
   rentalService.createRental(customerName, carId, days)
     |
     v
5. Service calls repository to save
   rentalRepository.save(rental)
     |
     v
6. Controller returns redirect
   return "redirect:/rentals"
     |
     v
7. Browser follows redirect
   GET /rentals
     |
     v
8. Controller returns view with updated data
   List<Rental> rentals = rentalService.findAll()
   model.addAttribute("rentals", rentals)
   return "rental-list"
```

The HTML form's `name` attributes directly map to Java `@RequestParam` parameters. This is why understanding forms deeply matters.

---

## Common Struggles and How to Overcome Them

### Struggle 1: Difference Between Semantic and Non-Semantic Elements

**Why this confuses students:** Both `<div class="nav">` and `<nav>` achieve the same visual result. Why does it matter?

**How to think about it:** Imagine your HTML is being read aloud. `<nav>` says "this is navigation." `<div class="nav">` says "this is a division" - the class is just a hint for developers who read the code.

**Strategy:** Before using `<div>`, ask: "Is there a semantic element that describes this content?" If yes, use the semantic element. Reserve `<div>` for pure layout grouping.

**Exam tip:** "I used `<nav>` instead of `<div>` because it communicates the element's purpose to browsers, screen readers, and developers. This improves accessibility and maintainability."

### Struggle 2: Form Attributes and Their Purpose

**Why this confuses students:** `id`, `name`, `for`, `value` - many attributes with overlapping purposes.

**How to think about it:**
- `id`: Unique identifier within the page (for CSS, JavaScript, label association)
- `name`: What the server receives as the parameter name
- `for`: On labels, links to the input's `id`
- `value`: The actual data being sent

**Strategy:** Remember this: `name` is for the server, `id` is for the page. They often have the same value, but serve different purposes.

```html
<label for="customerEmail">Email:</label>
<input type="email" id="customerEmail" name="email" value="">
<!--          ^- for page   ^- id for page    ^- for server    -->
```

**Exam tip:** "The `name` attribute determines what parameter name my Java controller receives. The `id` is for page-level operations like label association and JavaScript targeting."

### Struggle 3: Understanding When to Use div vs Semantic Elements

**Why this confuses students:** Not every piece of content maps obviously to a semantic element.

**How to think about it:** Use this decision tree:
1. Is this the main navigation? Use `<nav>`
2. Is this the page header with logo and site title? Use `<header>`
3. Is this the primary content? Use `<main>`
4. Is this a self-contained piece that could stand alone? Use `<article>`
5. Is this a thematic grouping? Use `<section>`
6. Is this sidebar or tangentially related? Use `<aside>`
7. Is this the page footer? Use `<footer>`
8. If none of the above, use `<div>`

**Strategy:** Start with semantic elements. Only fall back to `<div>` when no semantic element fits.

**Exam tip:** "I chose `<section>` for grouping related cars by type because it represents a thematic grouping of content. A `<div>` would work visually but wouldn't convey the structural meaning."

### Struggle 4: Form Input Types and When to Use Each

**Why this confuses students:** Many input types exist, and `type="text"` works for everything.

**How to think about it:** While `type="text"` accepts any input, specialized types provide:
- Better mobile keyboards (email shows @, tel shows numbers)
- Built-in validation (email checks for @)
- Better UX (date shows a date picker)

**Strategy:** Match input type to the data you're collecting:
- Email address? `type="email"`
- Phone number? `type="tel"`
- Password? `type="password"`
- Date? `type="date"`
- Numeric value? `type="number"`
- General text? `type="text"`

**Exam tip:** "I used `type="email"` for the email field because it provides automatic format validation and shows an appropriate keyboard on mobile devices, improving user experience."

### Struggle 5: Connecting HTML to Server-Side Processing

**Why this confuses students:** HTML is learned before Spring Boot, so the connection feels abstract.

**How to think about it:** The form's `action` and `method` define what controller receives the request. The input `name` attributes become `@RequestParam` parameters.

**Strategy:** When designing a form, first think about your controller method signature:
```java
@PostMapping("/items/add")
public String addItem(@RequestParam String title, @RequestParam String url)
```

Then build the form to match:
```html
<form action="/items/add" method="POST">
    <input type="text" name="title">
    <input type="url" name="url">
</form>
```

**Exam tip:** "I designed my HTML form to match my Spring Boot controller's expected parameters. The `name` attribute `customerEmail` in the form becomes `@RequestParam String customerEmail` in my Java method."

---

## Practice Exercises

### Exercise 1: Semantic Page Structure (Maximum Guidance)

**What you'll build:** A properly structured HTML page for Kailua Car Rental's homepage.

**Connection to Projects:** This directly applies to your Kailua and Onskeskyen projects.

**Skills you'll practice:**
- HTML5 document structure
- Semantic elements
- Proper heading hierarchy

**Step-by-step approach:**

1. Create the basic document structure with DOCTYPE, html, head, and body
2. Add essential meta tags (charset, viewport, title)
3. Create a `<header>` with the company name as h1 and navigation links
4. Create a `<main>` section with:
   - A `<section>` for available car categories
   - A `<section>` for rental process information
5. Create a `<footer>` with contact information

**Skeleton to get started:**
```html
<!DOCTYPE html>
<html lang="da">
<head>
    <!-- Add meta tags and title -->
</head>
<body>
    <header>
        <!-- Logo, company name, navigation -->
    </header>

    <main>
        <section>
            <h2>Our Car Categories</h2>
            <!-- Add content -->
        </section>

        <section>
            <h2>How to Rent</h2>
            <!-- Add content -->
        </section>
    </main>

    <footer>
        <!-- Contact info, copyright -->
    </footer>
</body>
</html>
```

**What success looks like:** Your page has a clear visual hierarchy, all content is in appropriate semantic elements, and the document is valid HTML5.

---

### Exercise 2: Customer Registration Form (Moderate Guidance)

**What you'll build:** A complete customer registration form for Kailua Car Rental.

**Skills you'll practice:**
- Form creation
- Input type selection
- Label association
- Basic validation attributes

**Requirements:**
The form should collect:
- Full name (required, minimum 2 characters)
- Email address (required, email format)
- Phone number (optional)
- Driver's license number (required, pattern: 2 letters followed by 6 digits)
- Date of birth (required, must be a date)
- Preferred car type (dropdown: Economy, Standard, Luxury)
- Agreement to terms (checkbox, required)

**Key concepts to apply:**
- Each input needs a label with `for` attribute
- Use appropriate input types
- Add validation attributes where specified
- Use `method="POST"` and an appropriate `action`

**Success criteria:**
- All fields have proper labels
- Input types match the data being collected
- Required fields are marked
- Form would submit to a `/customers/register` endpoint

---

### Exercise 3: Wishlist Display Page (Minimal Guidance)

**What you'll build:** An HTML page that displays a wishlist with its items, ready for Thymeleaf integration.

**Requirements:**
- Page structure with header (site title, navigation), main content, and footer
- Wishlist title displayed as h1
- Items displayed in a table with columns: Item Name, Price, Link, Priority
- Each row should have a "Reserve" button (non-functional for now)
- Navigation includes links to: My Wishlists, Shared With Me, Log Out

**Skills you'll practice:**
- Complete page structure
- Table creation
- Preparing HTML for dynamic content

**Hints:**
- Think about how Thymeleaf will iterate over items (you can add placeholder comments)
- Consider what classes or IDs might be useful for styling later
- The "Reserve" button will eventually need to submit a form

Build this page independently, using the concepts from this topic.

---

## Preparing for the Oral Exam

### Key Questions You Should Be Able to Answer

- "Why did you use semantic elements instead of divs?"
- "Explain the difference between a form's `name` and `id` attributes."
- "How does an HTML form connect to your Spring Boot controller?"
- "What's the purpose of the `<main>` element?"
- "Why use `type="email"` instead of `type="text"` for email fields?"
- "How does HTML fit into the MVC architecture?"

### Demo Tips

When demonstrating HTML in your project:

1. **Show the structure:** Open the HTML source and point out semantic elements
2. **Explain the form flow:** "When the user submits this form, the data goes to my `@PostMapping` controller at `/wishlists/add`"
3. **Connect to architecture:** "The HTML is the View layer - it displays data that came from my Java service"
4. **Mention accessibility:** "I used semantic elements so screen readers can navigate the page structure"

### What NOT to Do

- Don't just say "it's HTML, it makes the page"
- Don't focus only on visual appearance
- Don't forget to connect HTML to the Java backend

### What TO Do

- Explain why you chose specific semantic elements
- Trace a form submission from HTML to Java controller
- Connect HTML to the broader MVC architecture
- Mention how this prepares for Thymeleaf dynamic content

---

## Looking Ahead

### What You Can Do Now

- Create semantically structured HTML5 pages
- Build forms with appropriate input types and validation
- Organize content using proper document structure
- Understand HTML's role in web application architecture

### How This Will Be Used in Upcoming Topics

- **Spring Boot Fundamentals (Phase 5):** Your HTML pages become Thymeleaf templates. You'll add `th:text`, `th:each`, `th:if` to make content dynamic.

- **Form Processing (Phase 5):** HTML forms you build now will submit to `@PostMapping` controllers. The `name` attributes become `@RequestParam` parameters.

- **Database Display (Phase 5):** Collections from your repository (like `List<Car>`) will be displayed using `th:each` to iterate over your HTML structures.

### Project Connection

**Kailua Car Rental (Phase 4):**
- Customer registration forms
- Car inventory display tables
- Rental contract creation forms

**Onskeskyen Wishlist (Phase 7):**
- Login and registration forms
- Wishlist display pages
- Item addition forms
- Shared wishlist views

Every page in these projects starts with the HTML skills you're learning now.

---

## Key Takeaways

- **HTML5 Document Structure:** Every page needs DOCTYPE, html with lang, head with meta tags, and body for content.

- **Semantic Elements:** Use `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>` to communicate content meaning. Reserve `<div>` for pure layout needs.

- **Forms are the Bridge:** HTML forms connect user input to your Java controllers. The `name` attribute becomes your `@RequestParam` parameter name.

- **Input Types Matter:** Use `type="email"`, `type="date"`, `type="number"` for better UX, validation, and mobile keyboards.

- **Labels are Required:** Always pair inputs with labels using `for` and `id` for accessibility and usability.

**For the exam:** Be able to trace data flow from an HTML form through your Spring Boot controller to the database and back to the displayed page.

---

## For the Next Topic Agent

### Terminology Established This Topic

- **Semantic Elements:** HTML5 elements that describe their content's meaning (header, nav, main, section, article, aside, footer).

- **Document Structure:** The required HTML5 structure: DOCTYPE, html (with lang), head (with meta, title), body.

- **Form Submission Flow:** The process by which form data travels from HTML to a Spring Boot controller via HTTP POST.

- **Input Types:** Specialized HTML form input types (text, email, password, number, date, tel, checkbox, radio) that provide validation and UX benefits.

- **Label Association:** Connecting labels to inputs using the `for` attribute matching the input's `id`.

- **Action and Method:** Form attributes that determine the submission endpoint (`action="/path"`) and HTTP method (`method="POST"`).

### Example Classes/Concepts Created

- **Kailua page structure:** Header with navigation, main with sections, footer pattern for car rental application.

- **Customer registration form:** Complete form with text, email, tel, date, select, and checkbox inputs with validation.

- **Form-to-Controller mapping:** Demonstrated how `name="customerEmail"` becomes `@RequestParam String customerEmail`.

- **MVC data flow diagram:** Visual representation of user request through Controller -> Service -> Repository -> Database and back through HTML response.

### Student Capabilities After This Topic

Students who complete this material can now:
- Create valid HTML5 documents with proper structure and meta information
- Use semantic elements to create meaningful page structure
- Build forms with appropriate input types, labels, and validation
- Understand how HTML forms connect to Spring Boot controllers
- Explain HTML's role as the View layer in MVC architecture
- Prepare HTML structures that will become Thymeleaf templates

### Pedagogical Patterns Used

- **Architecture connection:** Constantly relating HTML to its role in MVC and the full-stack data flow.

- **Form-to-Java mapping:** Explicitly showing how HTML `name` attributes become Java `@RequestParam` parameters.

- **Semantic decision tree:** Providing a step-by-step process for choosing between semantic elements and div.

- **Project grounding:** Every concept tied to Kailua or Onskeskyen practical applications.

- **Preview of Thymeleaf:** Showing how current HTML knowledge prepares for dynamic templating, without requiring understanding of Thymeleaf yet.

- **Building on Collections:** Connecting back to how Collections (learned in prior topic) will be displayed in HTML using tables and lists.
