# Assessment Activity API

## Overview
This project provides an API for user account management using Django Rest Framework (DRF). The API supports creating and updating user accounts.

## Features
- Create a user with an email address.
- Update user details including first name, last name, and age.
- Ensure unique email addresses for user accounts.
- Handle cases where a user update is attempted but the user does not exist.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/FestusMike/Assessment_Activity
   cd Assessment_Activity
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run database migrations:
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
- **Endpoint:** `POST /api/users/create`
- **Request Body:**
  ```json
  {
    "email": "user@example.com"
  }
  ```
- **Response:**
  ```json
  {
    "success": true,
    "message": "User created successfully",
    "data": {
      "email": "user@example.com",
      "first_name": null,
      "last_name": null,
      "age": null
    }
  }
  ```

### Update User
- **Endpoint:** `PATCH /api/users/populate`
- **Request Body:**
  ```json
  {
    "email": "existing@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "age": 30
  }
  ```
- **Response:**
  ```json
  {
    "success": true,
    "message": "User updated successfully",
    "data": {
      "email": "existing@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "age": 30
    }
  }
  ```

## Running Tests

The project uses `pytest` for testing. To run the tests, execute:
```sh
pytest
```


This project is licensed under the MIT License.

