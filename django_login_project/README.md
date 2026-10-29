# Django User Login and Validation Using Regular Expressions

## 1. Project Title
**User Login and Form Validation Application Using Django and Regular Expressions**

## 2. Aim
To develop a simple web application using the Django framework that demonstrates user login form handling and input validation using Python's built-in regular expression (`re`) module.

## 3. Introduction to Django
Django is a high-level Python web framework designed for rapid development and clean, pragmatic design. It follows the Model-View-Template (MVT) architectural pattern:
* **Model**: Handles data structure and database operations.
* **View**: Processes user HTTP requests, performs business logic and validation, and returns HTTP responses.
* **Template**: Renders dynamic HTML content presented to the user.

Django provides built-in tools such as URL routing, template rendering, Cross-Site Request Forgery (CSRF) protection, and an administrative interface, making it an ideal framework for building robust web applications.

## 4. Features of Django
* **MVT Architecture**: Clean separation between database models, business logic views, and HTML presentation templates.
* **Built-in Security**: Automatic protection against common web vulnerabilities, including CSRF, SQL injection, and cross-site scripting (XSS).
* **URL Routing**: Intuitive and clean URL design mapped directly to Python functions or classes.
* **Built-in Development Server**: Lightweight local web server for testing and debugging during development without external software.
* **Integrated ORM and SQLite**: Native database management with zero initial setup required.

## 5. Installation Instructions

### Prerequisites
* Python 3.10 or higher installed on your computer.
* `pip` (Python package manager).

### Step 1: Create a Project Directory and Virtual Environment
```bash
python -m venv venv
```

### Step 2: Activate the Virtual Environment
* On Windows (Command Prompt):
  ```cmd
  venv\Scripts\activate
  ```
* On Windows (PowerShell):
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
* On macOS / Linux:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Required Packages
```bash
pip install django
```
Or install directly using the requirements file:
```bash
pip install -r requirements.txt
```

## 6. Django File Structure
The project is organized in a modular structure:

```
django_login_project/
│
├── manage.py              # Command-line utility for administrative tasks
│
├── loginproject/          # Project configuration directory
│   ├── __init__.py        # Marks directory as a Python package
│   ├── settings.py        # Django project settings and configurations
│   ├── urls.py            # Main URL declarations and routing
│   ├── asgi.py            # ASGI configuration for async web servers
│   └── wsgi.py            # WSGI configuration for production deployment
│
├── accounts/              # Django application for user management
│   ├── __init__.py        # Package initialization
│   ├── views.py           # Contains login_view with regex validation logic
│   ├── apps.py            # App configuration for the accounts module
│   ├── models.py          # Data models (standard Django structure)
│   ├── admin.py           # Django admin registration
│   └── tests.py           # Automated unit tests for validation cases
│
├── templates/             # HTML templates directory
│   └── login.html         # Login page with CSRF token and alert messages
│
├── static/                # Static files directory
│   └── style.css          # Blue-and-white responsive CSS stylesheet
│
├── requirements.txt       # List of Python dependencies
└── README.md              # Project documentation for practical submission
```

## 7. Description of Regular-Expression Validation

Input validation is performed in `accounts/views.py` using Python's standard `re` module.

### Regular Expression Pattern
```python
^[A-Za-z][A-Za-z0-9_]{2,15}$
```

### Pattern Breakdown
* `^`: Asserts the start of the string.
* `[A-Za-z]`: Enforces that the first character must be an English letter (uppercase or lowercase).
* `[A-Za-z0-9_]{2,15}`: Specifies that the next 2 to 15 characters can only be uppercase letters, lowercase letters, digits (0-9), or underscores (`_`).
* `$`: Asserts the end of the string.

### Rules Enforced by Pattern
1. **Starting Character**: Must begin with an alphabetical letter (`a-z` or `A-Z`). Usernames beginning with numbers or symbols are rejected.
2. **Allowed Characters**: Only letters, numbers, and underscores are permitted. Special characters like `@`, `#`, `$`, `-`, and spaces are rejected.
3. **Length Constraint**: Minimum length is 3 characters (1 starting letter + 2 allowed characters), and maximum length is 16 characters (1 starting letter + 15 allowed characters).

### Password Validation
* Enforces a minimum length of 8 characters (`len(password) >= 8`).
* Passwords are never returned in template context, rendered in HTML, or logged in plain text.
* Because this is a college practical demonstration of form validation, successful validation reports `"Input validation successful"`.

## 8. Commands to Run the Application

Navigate to the project root directory where `manage.py` is located:

```bash
cd django_login_project
```

### Run Database Migrations
```bash
python manage.py migrate
```

### Run Automated Tests
```bash
python manage.py test
```

### Start the Development Server
```bash
python manage.py runserver
```

Open a web browser and visit:
```
http://127.0.0.1:8000/
```

## 9. Test Cases

| Test Case | Username Input | Password Input | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Valid username | `chetan123` | `password123` | Username accepted; validation successful | Input validation successful | Pass |
| Valid username with underscore | `chetan_123` | `password123` | Username accepted; validation successful | Input validation successful | Pass |
| Username too short | `ab` | `password123` | Validation error (username length < 3) | Invalid username error displayed | Pass |
| Username starts with number | `123chetan` | `password123` | Validation error (first character must be a letter) | Invalid username error displayed | Pass |
| Username with special characters | `chetan@123` | `password123` | Validation error (`@` is not allowed) | Invalid username error displayed | Pass |
| Password too short | `chetan123` | `abc123` | Password validation error (length < 8) | Password must be at least 8 characters long | Pass |
| Valid input formats | `chetan123` | `mypassword` | Form inputs accepted | Input validation successful | Pass |

## 10. Result
A complete, functioning Django web application demonstrating user login form processing and regular-expression input validation has been successfully developed, configured, and tested. All test cases passed with zero errors, confirming proper form handling, CSRF security, regex validation, and responsive UI presentation.

