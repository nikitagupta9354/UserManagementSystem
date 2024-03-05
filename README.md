# Django User Management System

This Django project provides a simple user management system with user roles and membership requests.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
Make sure you have Python and Django installed on your machine. If not, you can install them using the following commands:

### Install Python (Ensure "Add Python to PATH" is checked during installation)
[Download Python from the official website](https://www.python.org/downloads/windows/)

### Install Django
pip install django


## Clone the repository:
git clone https://github.com/your-username/django-organization-management.git

Change into the project directory:
cd django-organization-management

Install dependencies:
pip install -r requirements.txt

Database Setup
Apply migrations:
python manage.py migrate

Create a superuser:
python manage.py createsuperuser
Follow the prompts to create a superuser account.

Running the Development Server
Start the development server:
python manage.py runserver
Access the Django admin interface at http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

## Project Structure
models.py: Defines the database models for Organization, Role, UserProfile, and MembershipRequest.
views.py: Contains the views for rendering pages and handling user requests.
templates/: Folder containing HTML templates for different pages.
