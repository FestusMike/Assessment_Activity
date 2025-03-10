# Assessment Activity API

This project provides a RESTful API for managing user accounts, including user creation and updates.

## Live Documentation
- **Production**: [API Docs](https://assessment-test-thra.onrender.com/api/docs)
- **Localhost**: Open [127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs) after running the server.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/FestusMike/Assessment_Activity.git
   cd Assessment_Activity
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```sh
   python manage.py makemigrations users
   python manage.py migrate
   ```
5. Start the development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### Create User
**Endpoint:** `POST /api/users/create`
```json
{
  "email": "user@example.com"
}
```

### Update User
**Endpoint:** `PATCH /api/users/populate`
```json
{
  "email": "existing@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "age": 30
}
```

## Running Tests
To run the tests, use:
```sh
pytest
```