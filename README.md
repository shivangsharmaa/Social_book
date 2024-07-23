# Social_Book

Social_Book is a social networking application built with Django. Users can sign up, sign in, upload posts, like posts, follow other users, and view profiles. The project includes a fully functional backend with user authentication, a media handling system, and dynamic content generation.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)

## Features

- User Registration and Authentication
- Profile Management
- Post Uploading
- Like and Follow Functionality
- User Feed
- Profile Search
- Responsive Design

## Project Structure


### Core

- **`__init__.py`**: Marks the directory as a Python package.
- **admin.py**: Registers models with the Django admin site.
- **apps.py**: Configuration for the Core app.
- **models.py**: Contains all database models.
- **tests.py**: Contains tests for the application.
- **urls.py**: URL patterns for the Core app.
- **views.py**: Handles HTTP requests and responses.

### Media

- **Images**: Directory for user-uploaded images.

### Social_book

- **`__init__.py`**: Marks the directory as a Python package.
- **asgi.py**: ASGI configuration for async support.
- **settings.py**: Project settings.
- **urls.py**: Root URL configurations.
- **wsgi.py**: WSGI configuration for deployment.

### Static

- Directory for static files (CSS, JS, images).

### Template

- HTML files for rendering views.

### Database

- **db.sqlite3**: SQLite database file.

### Root

- **manage.py**: Command-line utility for project management.

### Usage
- Home Page: Displays the user feed.
- Sign Up: Allows new users to create an account.
- Sign In: Allows existing users to log in.
- Profile: Users can view and edit their profile.
- Upload Post: Users can upload new posts.
- Like Post: Users can like posts.
- Follow: Users can follow other users.
- Search: Users can search for other users.



