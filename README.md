# Secure Student Records API

A backend RESTful API built with Django and Django REST Framework (DRF) implementing JSON Web Token (JWT) authentication and Role-Based Access Control (RBAC) to secure student record management.

## Tech Stack
* **Backend:** Python, Django, Django REST Framework (DRF)
* **Authentication:** SimpleJWT (`djangorestframework-simplejwt`)
* **Database:** SQLite
* **Testing Tool:** Postman

## Key Features
* **JWT Authentication:** Issues secure `access` and `refresh` tokens via `/api/token/` for stateless API authentication.
* **Role-Based Access Control (RBAC):** Enforces distinct permissions between user groups (`faculty_user` and `student_user`), restricting unauthorized write/creation actions with `403 Forbidden` responses.
* **Protected Endpoints:** Secures `/api/student-records/` against unauthenticated and unauthorized access.

## Lab Deliverables (Screenshots)

### 1. JWT Authentication
Proof of obtaining a secure `access` and `refresh` token.
![JWT Token](./screenshots/jwt_token.png)

### 2. Successful Access (Authorized)
Showing a successful `200 OK` response when accessing protected data.
![Success](./screenshots/success.png)

### 3. Denied Access (Unauthorized)
Proof of the system blocking unauthorized actions with a `403 Forbidden` status.
![Denied](./screenshots/denied.png)

### 4. User & Group Configuration (Django Admin)
Proof of the `faculty_user` and `student_user` being assigned to their respective groups.
![Admin Panel](./screenshots/admin_panel.png)

---

## How to Run and Test

### 1. Clone the Repository
    git clone [https://github.com/rocrisjoygerongano/secure_student_api.git](https://github.com/rocrisjoygerongano/secure_student_api.git)
    cd secure_student_api

### 2. Set Up a Virtual Environment
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate

### 3. Install Dependencies
    pip install django djangorestframework djangorestframework-simplejwt

### 4. Run Database Migrations
    python manage.py makemigrations
    python manage.py migrate

### 5. Create a Superuser & Configure Roles (Optional)
Create an admin account to set up `faculty_user` and `student_user` groups in the Django Admin panel:

    python manage.py createsuperuser

### 6. Start the Development Server
    python manage.py runserver

The API will be available at `[http://127.0.0.1:8000/](http://127.0.0.1:8000/)`.