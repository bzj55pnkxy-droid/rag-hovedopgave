---
title: "Object-Oriented Programming: Advanced Design Patterns and Principles"
description: "Master SOLID principles, design patterns, composition vs inheritance, dependency injection, and advanced OOP concepts"
category: "Programming Paradigms"
tags: ["oop", "object-oriented", "design-patterns", "solid-principles", "software-architecture"]
difficulty: "intermediate"
---

# Object-Oriented Programming: Advanced Design Patterns and Principles

## OOP at the Intermediate Level

At the intermediate level, OOP transcends basic class creation to encompass architectural patterns, design principles, and the philosophical trade-offs that shape maintainable software systems.

**Key Focus Areas:**
- SOLID principles and their practical application
- Design patterns for common problems
- Composition vs inheritance trade-offs
- Dependency injection and inversion of control
- Interface segregation and contract-based programming
- Anti-patterns to avoid

## The SOLID Principles

SOLID represents five fundamental principles that lead to maintainable, flexible OOP code.

### S - Single Responsibility Principle (SRP)

**Principle:** A class should have only one reason to change.

**Bad Example:**
```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        # Database logic - reason to change #1
        db.execute(f"INSERT INTO users VALUES ('{self.name}', '{self.email}')")

    def send_welcome_email(self):
        # Email logic - reason to change #2
        smtp.send(self.email, "Welcome!")

    def generate_report(self):
        # Reporting logic - reason to change #3
        return f"User Report: {self.name}"
```

**Good Example:**
```python
class User:
    """Represents a user entity - single responsibility"""
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    """Handles database operations"""
    def save(self, user: User):
        db.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user.name, user.email)
        )

class EmailService:
    """Handles email notifications"""
    def send_welcome_email(self, user: User):
        smtp.send(user.email, f"Welcome {user.name}!")

class UserReportGenerator:
    """Generates user reports"""
    def generate(self, user: User) -> str:
        return f"User Report: {user.name}"
```

**Benefits:**
- Each class has a clear, focused purpose
- Changes to database logic don't affect email logic
- Easier to test each component independently
- Better code reusability

### O - Open/Closed Principle (OCP)

**Principle:** Classes should be open for extension but closed for modification.

**Bad Example:**
```python
class PaymentProcessor:
    def process_payment(self, amount, method):
        if method == "credit_card":
            # Credit card processing logic
            print(f"Processing ${amount} via credit card")
        elif method == "paypal":
            # PayPal processing logic
            print(f"Processing ${amount} via PayPal")
        elif method == "bitcoin":  # Adding new method requires modifying this class
            # Bitcoin processing logic
            print(f"Processing ${amount} via Bitcoin")
```

**Good Example (Strategy Pattern):**
```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount: float):
        pass

class CreditCardPayment(PaymentMethod):
    def process(self, amount: float):
        print(f"Processing ${amount} via credit card")
        # Credit card API integration

class PayPalPayment(PaymentMethod):
    def process(self, amount: float):
        print(f"Processing ${amount} via PayPal")
        # PayPal API integration

class BitcoinPayment(PaymentMethod):
    def process(self, amount: float):
        print(f"Processing ${amount} via Bitcoin")
        # Bitcoin API integration

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount: float):
        self.payment_method.process(amount)

# Usage - easily extensible without modifying existing code
processor = PaymentProcessor(CreditCardPayment())
processor.process_payment(100.00)

processor = PaymentProcessor(BitcoinPayment())
processor.process_payment(50.00)
```

### L - Liskov Substitution Principle (LSP)

**Principle:** Subtypes must be substitutable for their base types without altering program correctness.

**Bad Example (Violates LSP):**
```python
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")  # Violates LSP!

# Code expecting any Bird to fly will break with Penguin
def make_bird_fly(bird: Bird):
    return bird.fly()  # Crashes if bird is a Penguin
```

**Good Example:**
```python
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        return self.fly()

    def fly(self):
        return "Flying through the air"

class Sparrow(FlyingBird):
    pass

class Eagle(FlyingBird):
    def fly(self):
        return "Soaring at high altitude"

class Penguin(Bird):
    def move(self):
        return self.swim()

    def swim(self):
        return "Swimming in water"

# Now all Birds can move, but not all must fly
def make_bird_move(bird: Bird):
    return bird.move()  # Works for all bird types
```

### I - Interface Segregation Principle (ISP)

**Principle:** Clients shouldn't be forced to depend on interfaces they don't use.

**Bad Example:**
```python
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

class Robot(Worker):
    def work(self):
        print("Robot working")

    def eat(self):
        pass  # Robots don't eat - forced to implement anyway

    def sleep(self):
        pass  # Robots don't sleep - forced to implement anyway
```

**Good Example:**
```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Human(Workable, Eatable, Sleepable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

    def sleep(self):
        print("Human sleeping")

class Robot(Workable):
    def work(self):
        print("Robot working")
    # Only implements what it needs
```

### D - Dependency Inversion Principle (DIP)

**Principle:** High-level modules shouldn't depend on low-level modules. Both should depend on abstractions.

**Bad Example:**
```python
class MySQLDatabase:
    def connect(self):
        return "Connected to MySQL"

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  # Tightly coupled to MySQL

    def get_user(self, user_id):
        connection = self.db.connect()
        # Get user logic
```

**Good Example (Dependency Injection):**
```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql: str):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL"

    def query(self, sql: str):
        return f"MySQL executing: {sql}"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connected to PostgreSQL"

    def query(self, sql: str):
        return f"PostgreSQL executing: {sql}"

class UserService:
    def __init__(self, database: Database):  # Depends on abstraction
        self.db = database

    def get_user(self, user_id: int):
        self.db.connect()
        return self.db.query(f"SELECT * FROM users WHERE id = {user_id}")

# Easy to swap implementations
service = UserService(MySQLDatabase())
service = UserService(PostgreSQLDatabase())  # Same interface, different implementation
```

## Composition Over Inheritance

**The Debate:** When should you use composition vs. inheritance?

### Inheritance (IS-A Relationship)

```python
class Animal:
    def breathe(self):
        return "Breathing"

class Dog(Animal):  # Dog IS-A Animal
    def bark(self):
        return "Woof!"
```

**Pros:**
- Natural model for "is-a" relationships
- Automatic code reuse
- Polymorphism support

**Cons:**
- Tight coupling to parent class
- Changes to parent affect all children
- Can't change inheritance at runtime
- Diamond problem in multiple inheritance

### Composition (HAS-A Relationship)

```python
class Engine:
    def start(self):
        return "Engine starting"

class Wheels:
    def roll(self):
        return "Wheels rolling"

class Car:  # Car HAS-A Engine and Wheels
    def __init__(self):
        self.engine = Engine()
        self.wheels = Wheels()

    def drive(self):
        return f"{self.engine.start()}, {self.wheels.roll()}"
```

**Pros:**
- Flexible - can change components at runtime
- Loose coupling
- Easier to test
- Can compose behavior from multiple sources

**Cons:**
- More code (explicit delegation)
- Less intuitive for true "is-a" relationships

### When to Use Each

**Use Inheritance:**
- Clear "is-a" relationship
- Shared interface/contract needed
- Polymorphism required
- Stable, unlikely to change hierarchy

**Use Composition:**
- "Has-a" or "uses-a" relationship
- Need runtime flexibility
- Want to avoid deep inheritance hierarchies
- Multiple behaviors to combine

### Real-World Example: Game Characters

**Inheritance Approach (Rigid):**
```python
class Character:
    pass

class FlyingCharacter(Character):
    def fly(self):
        pass

class ShootingCharacter(Character):
    def shoot(self):
        pass

class FlyingShootingCharacter(FlyingCharacter, ShootingCharacter):  # Combinatorial explosion!
    pass
```

**Composition Approach (Flexible):**
```python
class FlyBehavior:
    def fly(self):
        return "Flying"

class ShootBehavior:
    def shoot(self):
        return "Shooting"

class Character:
    def __init__(self, behaviors=None):
        self.behaviors = behaviors or []

    def perform_actions(self):
        return [behavior() for behavior in self.behaviors]

# Easy to compose any combination
superman = Character([
    lambda: FlyBehavior().fly(),
    lambda: ShootBehavior().shoot()
])

soldier = Character([
    lambda: ShootBehavior().shoot()
])
```

## Design Patterns

Design patterns are reusable solutions to common problems in software design.

### Creational Patterns

#### Factory Pattern

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        return "MySQL connection"

class PostgreSQL(Database):
    def connect(self):
        return "PostgreSQL connection"

class DatabaseFactory:
    @staticmethod
    def create_database(db_type: str) -> Database:
        if db_type == "mysql":
            return MySQL()
        elif db_type == "postgresql":
            return PostgreSQL()
        else:
            raise ValueError(f"Unknown database type: {db_type}")

# Usage
db = DatabaseFactory.create_database("mysql")
db.connect()
```

#### Singleton Pattern

```python
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self):
        if not self.connection:
            self.connection = "Database connected"
        return self.connection

# Always returns the same instance
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True
```

### Structural Patterns

#### Decorator Pattern

```python
from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 2.0

    def description(self) -> str:
        return "Simple coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()

    def description(self) -> str:
        return self._coffee.description()

class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.5

    def description(self) -> str:
        return self._coffee.description() + ", milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.2

    def description(self) -> str:
        return self._coffee.description() + ", sugar"

# Usage - dynamically add features
coffee = SimpleCoffee()
print(f"{coffee.description()}: ${coffee.cost()}")  # Simple coffee: $2.0

coffee = MilkDecorator(coffee)
print(f"{coffee.description()}: ${coffee.cost()}")  # Simple coffee, milk: $2.5

coffee = SugarDecorator(coffee)
print(f"{coffee.description()}: ${coffee.cost()}")  # Simple coffee, milk, sugar: $2.7
```

#### Adapter Pattern

```python
class EuropeanSocket:
    def voltage(self):
        return 230

    def plug_type(self):
        return "Type C"

class USASocket:
    def voltage(self):
        return 110

    def plug_type(self):
        return "Type A"

class SocketAdapter:
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        # Convert to standard voltage
        return 110

    def plug_type(self):
        return "Universal"

# Usage
eu_socket = EuropeanSocket()
adapter = SocketAdapter(eu_socket)
print(adapter.voltage())  # 110 (converted)
```

### Behavioral Patterns

#### Observer Pattern

```python
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass

class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):
        self._state = state
        self.notify()

class EmailNotifier(Observer):
    def update(self, data):
        print(f"Email notification: {data}")

class SMSNotifier(Observer):
    def update(self, data):
        print(f"SMS notification: {data}")

# Usage
subject = Subject()
subject.attach(EmailNotifier())
subject.attach(SMSNotifier())

subject.set_state("Order shipped!")
# Output:
# Email notification: Order shipped!
# SMS notification: Order shipped!
```

#### Strategy Pattern

```python
from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(SortingStrategy):
    def sort(self, data):
        # Bubble sort implementation
        return sorted(data)  # Simplified

class QuickSort(SortingStrategy):
    def sort(self, data):
        # Quick sort implementation
        return sorted(data)  # Simplified

class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort_data(self, data):
        return self.strategy.sort(data)

# Usage - can swap strategies at runtime
data = [3, 1, 4, 1, 5, 9, 2, 6]

sorter = Sorter(BubbleSort())
print(sorter.sort_data(data))

sorter = Sorter(QuickSort())
print(sorter.sort_data(data))
```

## Dependency Injection

Dependency Injection (DI) is a technique where an object receives its dependencies from external sources rather than creating them.

### Manual Dependency Injection

```python
class EmailService:
    def send(self, to: str, message: str):
        print(f"Sending email to {to}: {message}")

class SMSService:
    def send(self, to: str, message: str):
        print(f"Sending SMS to {to}: {message}")

class NotificationService:
    def __init__(self, sender):  # Dependency injected
        self.sender = sender

    def notify(self, recipient: str, message: str):
        self.sender.send(recipient, message)

# Usage
email_notifier = NotificationService(EmailService())
email_notifier.notify("user@example.com", "Hello!")

sms_notifier = NotificationService(SMSService())
sms_notifier.notify("+1234567890", "Hello!")
```

### Constructor Injection vs Setter Injection

```python
# Constructor Injection (preferred - required dependencies)
class UserService:
    def __init__(self, database, logger):
        self.database = database
        self.logger = logger

# Setter Injection (optional dependencies)
class UserService:
    def __init__(self, database):
        self.database = database
        self.logger = None

    def set_logger(self, logger):
        self.logger = logger
```

## Anti-Patterns to Avoid

### God Object

**Bad:**
```python
class Application:
    def handle_http_request(self): pass
    def connect_to_database(self): pass
    def send_email(self): pass
    def process_payment(self): pass
    def generate_report(self): pass
    # Does everything!
```

### Circular Dependencies

**Bad:**
```python
class A:
    def __init__(self):
        self.b = B(self)  # A depends on B

class B:
    def __init__(self, a):
        self.a = a  # B depends on A
```

### Yo-Yo Problem (Deep Inheritance)

**Bad:**
```python
class A: pass
class B(A): pass
class C(B): pass
class D(C): pass
class E(D): pass  # Too deep!
```

## The Bottom Line

Intermediate OOP requires mastering:

- **SOLID principles** for maintainable design
- **Composition over inheritance** for flexibility
- **Design patterns** for common problems
- **Dependency injection** for loose coupling
- **Interface-based programming** for contracts
- **Recognizing anti-patterns** to avoid pitfalls

The goal isn't to use every pattern and principle everywhere, but to understand the trade-offs and apply them judiciously based on your specific needs. Good OOP design balances flexibility, simplicity, and maintainability.
