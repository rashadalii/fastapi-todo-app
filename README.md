# FastAPI Todo App

A modern, secure REST API for managing todo tasks built with FastAPI, SQLAlchemy, and PostgreSQL. Features user authentication, task management, and comprehensive API documentation.

## 🚀 Features

- **User Authentication**: Secure JWT-based authentication with refresh tokens
- **Task Management**: Create, read, update, and delete tasks
- **Task Status Tracking**: Track tasks as New, In Progress, or Completed
- **User-specific Tasks**: Each user can only access their own tasks
- **RESTful API**: Clean, well-documented REST endpoints
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Docker Support**: Easy deployment with Docker and Docker Compose
- **Testing**: Comprehensive test suite with pytest
- **API Documentation**: Auto-generated OpenAPI/Swagger documentation

## 📋 Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Docker and Docker Compose (optional)

## 🛠️ Installation

### Option 1: Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-todo-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   DATABASE_URL=postgresql://fastapi_user:fastapi_password@localhost:5432/fastapi_db
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   REFRESH_TOKEN_EXPIRE_DAYS=7
   ```

5. **Set up the database**
   ```bash
   # Start PostgreSQL (if not already running)
   # Create database and user as needed
   
   # Run database migrations
   alembic upgrade head
   ```

6. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

### Option 2: Docker Deployment

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-todo-app
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

The application will be available at `http://localhost:8000`

## 📚 API Documentation

Once the application is running, you can access:

- **Interactive API Documentation**: `http://localhost:8000/docs`
- **ReDoc Documentation**: `http://localhost:8000/redoc`

## 🔐 Authentication

The API uses JWT tokens for authentication. Here's how to use it:

### 1. Register a new user
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "username": "johndoe",
    "password": "password123"
  }'
```

### 2. Login to get access token
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=johndoe&password=password123"
```

### 3. Use the access token
Include the token in the Authorization header:
```bash
curl -X GET "http://localhost:8000/api/v1/user/tasks" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 📖 API Endpoints

### Authentication (`/api/v1/auth`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and get access token |
| POST | `/refresh` | Refresh access token |

### User Tasks (`/api/v1/user`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | Get user's tasks (paginated) |
| GET | `/tasks/filter` | Filter tasks by status |
| POST | `/task` | Create a new task |
| PATCH | `/{task_id}` | Update a task |
| PATCH | `/{task_id}/complete` | Mark task as completed |
| DELETE | `/{task_id}` | Delete a task |

### All Tasks (`/api/v1/tasks`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Get all tasks (paginated) |
| GET | `/{task_id}` | Get a specific task |

## 📊 Data Models

### User
```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "username": "johndoe"
}
```

### Task
```json
{
  "id": 1,
  "title": "Complete project",
  "description": "Finish the FastAPI todo app",
  "status": "In Progress",
  "user_id": 1
}
```

### Task Status Options
- `"New"`
- `"In Progress"`
- `"Completed"`

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_auth.py
```

## 🐳 Docker Commands

```bash
# Build and start services
docker-compose up --build

# Start services in background
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild and restart
docker-compose down && docker-compose up --build
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | Required |
| `SECRET_KEY` | JWT secret key | Required |
| `ALGORITHM` | JWT algorithm | HS256 |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Access token expiry | 30 |
| `REFRESH_TOKEN_EXPIRE_DAYS` | Refresh token expiry | 7 |

### Database Configuration

The application uses PostgreSQL with the following default settings:
- **Database**: `fastapi_db`
- **User**: `fastapi_user`
- **Password**: `fastapi_password`
- **Port**: `5432`

## 📁 Project Structure

```
fastapi-todo-app/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── auth.py              # Authentication utilities
│   ├── crud.py              # Database operations
│   ├── database.py          # Database configuration
│   ├── dependencies.py      # FastAPI dependencies
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   └── routes/
│       ├── __init__.py
│       ├── auths.py         # Authentication routes
│       ├── tasks.py         # Task management routes
│       └── users.py         # User-specific routes
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Test configuration
│   ├── test_auth.py         # Authentication tests
│   ├── test_tasks.py        # Task management tests
│   └── test_users.py        # User tests
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile              # Docker image configuration
├── requirements.txt         # Python dependencies
└── README.md              # This file
```

## 🚀 Deployment

### Production Considerations

1. **Environment Variables**: Set proper production values for all environment variables
2. **Database**: Use a production PostgreSQL instance
3. **Security**: Use strong secret keys and HTTPS
4. **Monitoring**: Add logging and monitoring
5. **CORS**: Configure CORS settings for your frontend

### Example Production Docker Compose

```yaml
version: '3.8'
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web:
    build: .
    environment:
      DATABASE_URL: ${DATABASE_URL}
      SECRET_KEY: ${SECRET_KEY}
    ports:
      - "8000:8000"
    depends_on:
      - db
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the API documentation at `/docs`
2. Review the test files for usage examples
3. Open an issue on GitHub

## 🔄 Version History

- **v0.1.0**: Initial release with basic CRUD operations and authentication