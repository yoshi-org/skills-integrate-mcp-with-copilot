# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Teacher-only student registration and removal
- Session-based teacher login

## Getting Started

1. Install the dependencies:

   ```
   pip install fastapi uvicorn
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## Teacher Login

Use the account button in the top-right corner to enter teacher mode. Local
development credentials are stored in `teachers.json`:

- Username: `teacher`
- Password: `mergington2026`

The credential file is intended for this local exercise. Production deployments
should use hashed passwords and a persistent identity provider.

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/auth/login`                                                     | Log in with a teacher username and password                          |
| GET    | `/auth/status`                                                    | Get the current teacher session status                               |
| POST   | `/auth/logout`                                                    | Log out of the current teacher session                               |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Register a student; teacher login required                            |
| DELETE | `/activities/{activity_name}/unregister?email=student@mergington.edu` | Unregister a student; teacher login required                       |

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

All data is stored in memory, which means data will be reset when the server restarts.
