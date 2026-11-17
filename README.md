
# Secure Student API

A REST API built with Django REST Framework that uses JWT authentication and role-based permissions to manage student records.

## Technologies Used

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- Postman

## Features

- JWT authentication
- Admin, Faculty, and Student roles
- Student record management
- Role-based access permissions
- Student record ownership restrictions

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rocrisjoygerongano/secure_student_api.git
cd secure_student_api
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root (the same folder as `manage.py`).

Add your own Django secret key:

```env
DJANGO_SECRET_KEY=your-generated-secret-key-here
```

Do not upload your `.env` file to GitHub.

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Create Admin Account

```bash
python manage.py createsuperuser
```

### 7. Run the Server

```bash
python manage.py runserver
```

API base URL:

```text
http://127.0.0.1:8000/
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/token/` | Obtain JWT tokens |
| POST | `/api/token/refresh/` | Refresh access token |
| GET | `/api/student-records/` | View student records |
| POST | `/api/student-records/` | Create student record |
| GET | `/api/student-records/{id}/` | View a specific record |
| PUT | `/api/student-records/{id}/` | Update a record |
| PATCH | `/api/student-records/{id}/` | Partially update a record |
| DELETE | `/api/student-records/{id}/` | Delete a record |

## User Roles

| Permission | Admin | Faculty | Student |
|---|---|---|---|
| View all records | Yes | Yes | No |
| View own records | Yes | Yes | Yes |
| Create records | Yes | No | No |
| Update records | Yes | Yes | No |
| Delete records | Yes | No | No |

## Screenshots

### JWT Authentication
![JWT Authentication](screenshots/01_jwt_authentication.png)

### Admin Access
![Admin Access](screenshots/02_admin_access.png)

### Admin Create Record
![Admin Create Record](screenshots/03_admin_create_record.png)

### Admin Delete Record
![Admin Delete Record](screenshots/04_admin_delete_record.png)

### Faculty Access
![Faculty Access](screenshots/05_faculty_access.png)

### Faculty Update Record
![Faculty Update Record](screenshots/06_faculty_update_record.png)

### Student Own Records
![Student Own Records](screenshots/07_student_own_records.png)

### Student Access Denied
![Student Access Denied](screenshots/08_student_access_denied.png)

### Student Record Isolation
![Student Record Isolation](screenshots/09_student_record_isolation.png)

### Owner Protection
![Owner Protection](screenshots/10_owner_protection.png)

### Django Admin Panel
![Admin Panel](screenshots/11_admin_panel.png)