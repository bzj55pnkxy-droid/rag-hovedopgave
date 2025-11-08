---
title: "APIs: Advanced Integration and Design Patterns"
description: "Master REST architecture, authentication strategies, API design principles, and modern API patterns"
category: "Backend Development"
tags: ["apis", "rest", "http", "web-development", "backend", "authentication", "microservices"]
difficulty: "intermediate"
---

# APIs: Advanced Integration and Design Patterns

## API Architecture Fundamentals

An API (Application Programming Interface) serves as a contract between systems, defining how they communicate. At the intermediate level, understanding API design goes beyond basic CRUD operations to encompass architectural patterns, security, performance, and scalability.

**Key Architectural Concerns:**
- **Statelessness**: Each request contains all information needed
- **Resource-oriented design**: URLs represent resources, not actions
- **Uniform interface**: Consistent patterns across endpoints
- **Client-server separation**: Independent evolution of frontend and backend

## RESTful Design Principles

### Richardson Maturity Model

Understanding REST maturity levels:

**Level 0 - The Swamp of POX**: Single endpoint, all operations via POST
**Level 1 - Resources**: Multiple resource-based URIs
**Level 2 - HTTP Verbs**: Proper use of HTTP methods and status codes
**Level 3 - Hypermedia (HATEOAS)**: Self-descriptive API responses with links

### Resource Design Best Practices

```
GET    /api/v1/users                    # List users (collection)
GET    /api/v1/users/{id}               # Get specific user
POST   /api/v1/users                    # Create user
PUT    /api/v1/users/{id}               # Full update
PATCH  /api/v1/users/{id}               # Partial update
DELETE /api/v1/users/{id}               # Delete user

# Nested resources
GET    /api/v1/users/{id}/orders        # User's orders
GET    /api/v1/users/{id}/orders/{orderId}  # Specific order

# Filtering, sorting, pagination
GET    /api/v1/users?role=admin&sort=-created_at&page=2&limit=20
```

**Design Guidelines:**
- Use nouns for resources, not verbs
- Plural names for collections
- Hierarchical relationships in URLs
- Query parameters for filtering/sorting
- Avoid deep nesting (max 2-3 levels)

## Authentication and Authorization

### API Key Authentication

```python
# Server-side validation
import hashlib
import hmac

def validate_api_key(request):
    provided_key = request.headers.get('X-API-Key')
    expected_key = get_key_from_database(provided_key)

    if not constant_time_compare(provided_key, expected_key):
        raise UnauthorizedException()
```

**Pros:** Simple, good for server-to-server
**Cons:** Less secure, can't be revoked easily, no user context

### JWT (JSON Web Tokens)

```python
import jwt
from datetime import datetime, timedelta

# Create token
def create_token(user_id, role):
    payload = {
        'sub': user_id,
        'role': role,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

# Validate token
def validate_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise TokenExpiredException()
    except jwt.InvalidTokenError:
        raise InvalidTokenException()

# Usage in request
headers = {
    'Authorization': f'Bearer {token}'
}
```

**JWT Structure:**
- **Header**: Algorithm and token type
- **Payload**: Claims (user data, permissions, expiration)
- **Signature**: Verification hash

**Best Practices:**
- Short expiration times (15 min - 1 hour)
- Refresh token pattern for extended sessions
- Store sensitive data server-side, not in JWT
- Use RS256 (asymmetric) for distributed systems

### OAuth 2.0 Flow

```python
# Authorization Code Flow (most secure)

# Step 1: Redirect user to authorization server
authorization_url = (
    f"https://auth.example.com/oauth/authorize?"
    f"client_id={CLIENT_ID}&"
    f"redirect_uri={REDIRECT_URI}&"
    f"response_type=code&"
    f"scope=read write&"
    f"state={random_state}"
)

# Step 2: User authorizes, gets redirected back with code
# Step 3: Exchange code for access token
token_response = requests.post(
    'https://auth.example.com/oauth/token',
    data={
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
)

access_token = token_response.json()['access_token']
refresh_token = token_response.json()['refresh_token']

# Step 4: Use access token for API requests
response = requests.get(
    'https://api.example.com/user/profile',
    headers={'Authorization': f'Bearer {access_token}'}
)
```

**Grant Types:**
- **Authorization Code**: Web applications
- **PKCE**: Mobile/SPA applications
- **Client Credentials**: Server-to-server
- **Password**: Legacy (avoid if possible)

## Advanced HTTP Concepts

### Idempotency

Operations that produce the same result regardless of how many times they're executed:

```
GET    /users/123     # Idempotent - always returns same data
PUT    /users/123     # Idempotent - setting state to same value
DELETE /users/123     # Idempotent - deleting already deleted resource
POST   /users         # NOT idempotent - creates new resource each time
```

**Idempotency Keys** for POST requests:
```python
response = requests.post(
    'https://api.payment.com/charges',
    json={'amount': 1000, 'currency': 'usd'},
    headers={'Idempotency-Key': str(uuid.uuid4())}
)
```

### Content Negotiation

```python
# Client specifies acceptable formats
headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br'
}

# Server responds with appropriate format
response = requests.get('https://api.example.com/data', headers=headers)

# Server indicates what it sent
print(response.headers['Content-Type'])  # application/json; charset=utf-8
print(response.headers['Content-Encoding'])  # gzip
```

### Conditional Requests and ETags

```python
# First request
response = requests.get('https://api.example.com/users/123')
etag = response.headers['ETag']  # "33a64df551425fcc55e4d42a148795d9f25f89d4"

# Subsequent request with conditional header
response = requests.get(
    'https://api.example.com/users/123',
    headers={'If-None-Match': etag}
)

if response.status_code == 304:  # Not Modified
    print("Use cached version")
else:  # 200 OK
    updated_data = response.json()
    new_etag = response.headers['ETag']
```

## Rate Limiting and Throttling

### Implementation Patterns

```python
from datetime import datetime, timedelta
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests=100, window_seconds=3600):
        self.max_requests = max_requests
        self.window = timedelta(seconds=window_seconds)
        self.requests = defaultdict(list)

    def is_allowed(self, client_id):
        now = datetime.utcnow()
        cutoff = now - self.window

        # Remove old requests
        self.requests[client_id] = [
            req_time for req_time in self.requests[client_id]
            if req_time > cutoff
        ]

        if len(self.requests[client_id]) < self.max_requests:
            self.requests[client_id].append(now)
            return True
        return False

# Response headers
"""
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 456
X-RateLimit-Reset: 1640995200
Retry-After: 3600
"""
```

**Strategies:**
- **Fixed Window**: Simple but allows bursts at window boundaries
- **Sliding Window**: More accurate, complex implementation
- **Token Bucket**: Allows bursts, smooths traffic
- **Leaky Bucket**: Strict constant rate

## Pagination Strategies

### Offset-Based Pagination

```python
# Request
GET /api/users?page=3&limit=20

# Response
{
    "data": [...],
    "pagination": {
        "page": 3,
        "limit": 20,
        "total_pages": 50,
        "total_items": 1000,
        "has_next": true,
        "has_prev": true
    },
    "links": {
        "first": "/api/users?page=1&limit=20",
        "prev": "/api/users?page=2&limit=20",
        "next": "/api/users?page=4&limit=20",
        "last": "/api/users?page=50&limit=20"
    }
}
```

**Issues:** Performance degrades with large offsets, inconsistent with concurrent modifications

### Cursor-Based Pagination

```python
# Request (initial)
GET /api/users?limit=20

# Response
{
    "data": [...],
    "pagination": {
        "next_cursor": "eyJpZCI6MTAwLCJ0aW1lIjoiMjAyNC0wMS0wMVQxMjowMDowMFoifQ==",
        "has_more": true
    }
}

# Subsequent request
GET /api/users?limit=20&cursor=eyJpZCI6MTAwLCJ0aW1lIjoiMjAyNC0wMS0wMVQxMjowMDowMFoifQ==
```

**Benefits:** Consistent results, better performance, handles real-time data

## API Versioning

### Strategies

**1. URI Versioning** (most common):
```
GET /api/v1/users
GET /api/v2/users
```

**2. Header Versioning**:
```python
headers = {'API-Version': '2'}
```

**3. Content Negotiation**:
```python
headers = {'Accept': 'application/vnd.company.v2+json'}
```

**4. Query Parameter**:
```
GET /api/users?version=2
```

### Deprecation Strategy

```python
# Response headers for deprecated endpoints
{
    "Deprecation": "true",
    "Sunset": "Sat, 31 Dec 2024 23:59:59 GMT",
    "Link": '<https://api.example.com/v2/users>; rel="successor-version"'
}
```

## Error Handling Patterns

### Structured Error Responses

```python
# Consistent error format (RFC 7807 - Problem Details)
{
    "type": "https://api.example.com/errors/insufficient-funds",
    "title": "Insufficient Funds",
    "status": 400,
    "detail": "Your account balance is $30 but the transfer amount is $50",
    "instance": "/account/12345/transfers/abc123",
    "balance": 30,
    "required": 50,
    "trace_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

### Client Implementation

```python
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Automatic retry with exponential backoff
def create_session_with_retries():
    session = requests.Session()

    retry_strategy = Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS", "PUT", "DELETE"],
        backoff_factor=1  # Wait 1s, 2s, 4s between retries
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session

# Usage
session = create_session_with_retries()
try:
    response = session.get('https://api.example.com/users', timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.Timeout:
    logger.error("Request timed out")
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 429:
        retry_after = int(e.response.headers.get('Retry-After', 60))
        logger.warning(f"Rate limited. Retry after {retry_after} seconds")
    else:
        logger.error(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    logger.error(f"Request failed: {e}")
```

## Async API Patterns

### Webhooks

```python
# Server registers webhook
POST /api/webhooks
{
    "url": "https://client.example.com/webhook",
    "events": ["order.created", "order.updated"],
    "secret": "whsec_xyz123"
}

# Server sends notification when event occurs
POST https://client.example.com/webhook
Headers:
    X-Webhook-Signature: sha256=abc123...
    X-Webhook-Id: evt_123
    X-Webhook-Timestamp: 1609459200

{
    "event": "order.created",
    "data": {
        "order_id": "ord_123",
        "amount": 1000,
        "status": "pending"
    }
}

# Client validation
import hmac
import hashlib

def validate_webhook(payload, signature, secret):
    expected = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(f"sha256={expected}", signature)
```

### Long Polling

```python
# Client
def long_poll(url, timeout=30):
    while True:
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                data = response.json()
                process_update(data)
        except requests.exceptions.Timeout:
            continue  # No updates, try again
```

### WebSockets for Real-Time

```python
import asyncio
import websockets
import json

async def consume_api_stream():
    uri = "wss://api.example.com/stream"

    async with websockets.connect(uri) as websocket:
        # Authenticate
        await websocket.send(json.dumps({
            "type": "auth",
            "token": "Bearer xyz123"
        }))

        # Subscribe to events
        await websocket.send(json.dumps({
            "type": "subscribe",
            "channels": ["orders", "notifications"]
        }))

        # Receive messages
        async for message in websocket:
            data = json.loads(message)
            await process_message(data)

asyncio.run(consume_api_stream())
```

## CORS Configuration

```python
# Server-side CORS headers
response.headers.update({
    'Access-Control-Allow-Origin': 'https://app.example.com',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Access-Control-Allow-Credentials': 'true',
    'Access-Control-Max-Age': '3600'  # Cache preflight for 1 hour
})

# Handling preflight OPTIONS request
@app.route('/api/users', methods=['OPTIONS'])
def handle_preflight():
    return '', 204, cors_headers
```

## API Testing

```python
import pytest
import requests_mock

def test_get_user():
    with requests_mock.Mocker() as m:
        m.get(
            'https://api.example.com/users/123',
            json={'id': 123, 'name': 'Alice'},
            status_code=200,
            headers={'X-RateLimit-Remaining': '99'}
        )

        response = api_client.get_user(123)

        assert response['name'] == 'Alice'
        assert m.call_count == 1

def test_rate_limit_handling():
    with requests_mock.Mocker() as m:
        m.get(
            'https://api.example.com/users/123',
            status_code=429,
            headers={'Retry-After': '60'}
        )

        with pytest.raises(RateLimitException) as exc_info:
            api_client.get_user(123)

        assert exc_info.value.retry_after == 60
```

## API Documentation with OpenAPI

```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
paths:
  /users/{userId}:
    get:
      summary: Get user by ID
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          description: User not found
      security:
        - bearerAuth: []

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
        name:
          type: string
        email:
          type: string
          format: email
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

## The Bottom Line

Intermediate API development requires understanding:

- **RESTful design principles** and resource modeling
- **Authentication/authorization** patterns (JWT, OAuth, API keys)
- **Performance optimization** through caching, rate limiting, and pagination
- **Error handling** with proper status codes and structured responses
- **Versioning strategies** for API evolution
- **Async patterns** (webhooks, WebSockets, long polling)
- **Security considerations** (CORS, validation, encryption)
- **Testing and documentation** for maintainability

Master these concepts to build robust, scalable, and secure APIs that serve as the backbone of modern distributed systems.
