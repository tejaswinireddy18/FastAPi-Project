# FastAPI Project Task

A complete FastAPI starter project with:

- `main.py` entry point
- modular routers for `users` and `items`
- Pydantic schemas for validation
- in-memory data stores (no database)
- environment variable support with `.env`

## Project Structure

```text
Fastapi-project-task/
|-- main.py
|-- Dockerfile
|-- .dockerignore
|-- requirements.txt
|-- .env
|-- .github/
|   `-- workflows/
|       `-- ci.yml
|-- routers/
|   |-- __init__.py
|   |-- users.py
|   `-- items.py
|-- schemas/
|   |-- __init__.py
|   |-- users.py
|   `-- items.py
|-- models/
|   |-- __init__.py
|   |-- users.py
|   `-- items.py
`-- README.md
```

## Virtual Environment Setup (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the Development Server

```powershell
python -m uvicorn main:app --reload
```

Server runs at:

- API base: `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`
- ReDoc docs: `http://127.0.0.1:8000/redoc`

## API Endpoints

### Users CRUD

- `GET /users/` - list users
- `GET /users/{user_id}` - get one user
- `POST /users/` - create user
- `PUT /users/{user_id}` - update user
- `DELETE /users/{user_id}` - delete user

Example request body for `POST /users/`:

```json
{
  "name": "Alice",
  "email": "alice@example.com"
}
```

### Items CRUD

- `GET /items/` - list items
- `GET /items/{item_id}` - get one item
- `POST /items/` - create item
- `PUT /items/{item_id}` - update item
- `DELETE /items/{item_id}` - delete item

Example request body for `POST /items/`:

```json
{
  "name": "Laptop",
  "description": "14-inch ultrabook",
  "price": 999.99
}
```

## Notes

- Data is stored in-memory and resets when the server restarts.
- `.env` is included for environment configuration and future extension.

## Run Tests

```powershell
pytest -v
```

The test suite covers:

- root health endpoint
- users CRUD flow
- items CRUD flow

## Docker Run

Build the image:

```powershell
docker build -t fastapi-project-task .
```

Run the container:

```powershell
docker run --name fastapi-project-task -p 8000:8000 fastapi-project-task
```

Stop and remove container:

```powershell
docker stop fastapi-project-task
docker rm fastapi-project-task
```

## CI (GitHub Actions)

CI workflow file is at `.github/workflows/ci.yml`.
It runs `pytest -v` on each push and pull request to `main`.
