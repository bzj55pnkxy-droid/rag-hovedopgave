---
title: "APIs: How Software Talks to Each Other"
description: "Learn about APIs, REST endpoints, HTTP methods, authentication, and how software communicates"
category: "Backend Development"
tags: ["apis", "rest", "http", "web-development", "backend"]
difficulty: "beginner"
---

# APIs: How Software Talks to Each Other

## What is an API?

API stands for Application Programming Interface. It's a way for different programs to communicate with each other.

**Real-world analogy**: A restaurant
- **You** (the client): Want food but don't want to cook
- **Menu** (the API): Lists what you can order and how
- **Waiter** (the API interface): Takes your order and brings back food
- **Kitchen** (the server): Prepares the food

You don't need to know how the kitchen works - you just order from the menu and get food back!

## Why Do We Need APIs?

### Problem: Every App Can't Do Everything
- You're building a weather app
- You don't have weather satellites
- Someone else (like NOAA) has the weather data

### Solution: Use Their API!
```python
# Your app asks the weather API
response = get("https://api.weather.com/current?city=NYC")
# You get back: {"temp": 72, "condition": "sunny"}
```

You get access to their data without building satellites!

## Types of APIs

### 1. REST APIs (Most Common)
Uses HTTP requests (like websites):

```
GET    /users      → Get all users
GET    /users/5    → Get user #5
POST   /users      → Create new user
PUT    /users/5    → Update user #5
DELETE /users/5    → Delete user #5
```

### 2. SOAP APIs (Older, More Complex)
Uses XML and strict rules. Common in enterprise/banking.

### 3. GraphQL APIs (Modern, Flexible)
Ask for exactly what you need:
```graphql
{
  user(id: 5) {
    name
    email
  }
}
```

### 4. WebSocket APIs (Real-time)
Two-way communication for chat apps, live updates.

## How REST APIs Work

### The Request
```
GET /api/users/123 HTTP/1.1
Host: example.com
Authorization: Bearer abc123token
Content-Type: application/json
```

**Parts:**
- **Method**: GET (what action)
- **Endpoint**: /api/users/123 (what resource)
- **Headers**: Extra information
- **Body**: Data (for POST/PUT)

### The Response
```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 123,
  "name": "Alice",
  "email": "alice@example.com",
  "age": 25
}
```

**Parts:**
- **Status code**: 200 (success!)
- **Headers**: Metadata
- **Body**: The actual data

## Common HTTP Methods

### GET - Read Data
```python
# Get all users
GET /api/users

# Get specific user
GET /api/users/123

# Get with filters
GET /api/users?age=25&city=NYC
```

**Characteristics:**
- Safe (doesn't change anything)
- Can be cached
- Appears in browser history

### POST - Create New Data
```python
POST /api/users
{
  "name": "Bob",
  "email": "bob@example.com",
  "age": 30
}

# Response:
{
  "id": 124,  # New ID assigned
  "name": "Bob",
  "email": "bob@example.com",
  "age": 30
}
```

### PUT - Update Entire Resource
```python
PUT /api/users/123
{
  "name": "Alice Smith",
  "email": "alice@example.com",
  "age": 26
}
```

### PATCH - Update Part of Resource
```python
PATCH /api/users/123
{
  "age": 26  # Only update age
}
```

### DELETE - Remove Data
```python
DELETE /api/users/123

# Response:
{
  "message": "User deleted successfully"
}
```

## API Endpoints

Endpoints are URLs that represent resources:

```
https://api.example.com/v1/users           # Collection of users
https://api.example.com/v1/users/123       # Specific user
https://api.example.com/v1/users/123/posts # User's posts
https://api.example.com/v1/posts?author=123 # Posts by author
```

**Best practices:**
- Use nouns, not verbs (`/users` not `/getUsers`)
- Use plurals (`/users` not `/user`)
- Nest resources logically
- Version your API (`/v1/`, `/v2/`)

## Status Codes

### 2xx - Success
- **200 OK**: Request succeeded
- **201 Created**: New resource created
- **204 No Content**: Success, but no data to return

### 3xx - Redirection
- **301 Moved Permanently**: Resource has new URL
- **304 Not Modified**: Cached version is still good

### 4xx - Client Errors (Your Mistake)
- **400 Bad Request**: Invalid request
- **401 Unauthorized**: Need to log in
- **403 Forbidden**: Logged in but not allowed
- **404 Not Found**: Resource doesn't exist
- **429 Too Many Requests**: Rate limit exceeded

### 5xx - Server Errors (Their Mistake)
- **500 Internal Server Error**: Something broke
- **502 Bad Gateway**: Intermediate server issue
- **503 Service Unavailable**: Server overloaded/down

## Authentication

APIs need to know who you are:

### 1. API Keys (Simple)
```python
GET /api/users
Headers:
  X-API-Key: abc123xyz789
```

Like a membership card.

### 2. Bearer Tokens (Common)
```python
GET /api/users
Headers:
  Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

Like a temporary pass.

### 3. OAuth (Secure)
"Log in with Google/Facebook" - lets apps access your data without seeing your password.

## Real-World Example: Weather API

```python
import requests

# Make API request
response = requests.get(
    'https://api.openweathermap.org/data/2.5/weather',
    params={
        'q': 'New York',
        'appid': 'your_api_key',
        'units': 'imperial'
    }
)

# Check if successful
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    print(f"It's {temp}°F and {description} in New York")
else:
    print(f"Error: {response.status_code}")
```

## Making API Requests

### Python:
```python
import requests

# GET request
response = requests.get('https://api.example.com/users/123')
data = response.json()

# POST request
response = requests.post(
    'https://api.example.com/users',
    json={'name': 'Alice', 'age': 25},
    headers={'Authorization': 'Bearer token123'}
)
```

### JavaScript:
```javascript
// GET request
fetch('https://api.example.com/users/123')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));

// POST request
fetch('https://api.example.com/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token123'
  },
  body: JSON.stringify({name: 'Alice', age: 25})
})
  .then(response => response.json())
  .then(data => console.log(data));
```

## API Response Formats

### JSON (Most Common):
```json
{
  "id": 123,
  "name": "Alice",
  "email": "alice@example.com",
  "posts": [
    {"id": 1, "title": "First Post"},
    {"id": 2, "title": "Second Post"}
  ]
}
```

### XML (Older):
```xml
<user>
  <id>123</id>
  <name>Alice</name>
  <email>alice@example.com</email>
</user>
```

## Rate Limiting

APIs limit how many requests you can make:

```
X-RateLimit-Limit: 1000      # Max requests per hour
X-RateLimit-Remaining: 543   # Requests left
X-RateLimit-Reset: 1609459200 # When limit resets
```

**Why?**
- Prevent abuse
- Manage server load
- Fairness for all users

## Pagination

Getting large datasets in chunks:

```
GET /api/users?page=1&limit=20

Response:
{
  "data": [...20 users...],
  "page": 1,
  "total_pages": 50,
  "total_users": 1000,
  "next": "/api/users?page=2&limit=20"
}
```

## Error Handling

```python
try:
    response = requests.get('https://api.example.com/users/123')
    response.raise_for_status()  # Raises error for 4xx/5xx

    data = response.json()
    print(data)

except requests.exceptions.HTTPError as e:
    if response.status_code == 404:
        print("User not found")
    elif response.status_code == 429:
        print("Rate limit exceeded")
    else:
        print(f"HTTP error: {e}")

except requests.exceptions.ConnectionError:
    print("Connection failed")

except requests.exceptions.Timeout:
    print("Request timed out")
```

## Popular Public APIs

### Free APIs to Practice:
- **JSONPlaceholder**: Fake REST API for testing
- **OpenWeatherMap**: Weather data
- **Dog API**: Random dog pictures
- **PokeAPI**: Pokemon data
- **REST Countries**: Country information
- **GitHub API**: Repository data
- **SpaceX API**: Rocket launch data

## Creating Your Own API

### Flask (Python):
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/api/users', methods=['POST'])
def create_user():
    new_user = request.json
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

app.run(debug=True)
```

## API Best Practices

### 1. Use HTTPS
Always encrypt data in transit.

### 2. Version Your API
```
/v1/users
/v2/users
```

### 3. Return Appropriate Status Codes
Don't return 200 for errors!

### 4. Provide Clear Error Messages
```json
{
  "error": "Invalid email format",
  "field": "email",
  "code": "INVALID_EMAIL"
}
```

### 5. Document Your API
Provide clear documentation with examples.

### 6. Be Consistent
Use same patterns for all endpoints.

## The Bottom Line

APIs are how modern applications communicate. They let you:

- **Access data** from other services (weather, maps, social media)
- **Connect apps** together (mobile app to backend)
- **Build ecosystems** (let others build on your platform)
- **Separate concerns** (frontend and backend independently)

Think of APIs as:
- **Restaurant menus**: Clear list of what you can order
- **Contracts**: Both sides know what to expect
- **Bridges**: Connecting different systems

Every major app uses APIs - Twitter, Instagram, Google Maps, weather apps, and more. Master APIs, and you can build apps that leverage the entire internet!
