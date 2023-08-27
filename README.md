# Base Django Project

This is a base project to start a new React project.

To start a new project use [base-react-project](https://github.com/ClarenceLindh/base-react-project) for the frontend.

## Available Scripts

In the scripts directory, you can run:

### `docker-setup.sh`

Starts a docker container with a postgres database.

### `env-setup.sh`

Sets up a Python virtual environment and installs the required packages.

### `logs.sh`
Shows logs from the docker container.

## Django Commands

In the backend directory, you can run:

### `python manage.py runserver`

Runs the server in the development mode.<br />
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

### `python manage.py test`

Launches the test runner in the interactive watch mode.

### `python manage.py migrate`

Migrates the database to the latest version.

### `python manage.py makemigrations`

Creates new migrations based on the changes you have made to your models.

### `python manage.py createsuperuser`

Creates a superuser for the admin interface.

### `python manage.py shell`

Starts a Python shell with the Django environment loaded.

## Django REST Framework

The API is built using the Django REST Framework. You can find the documentation [here](https://www.django-rest-framework.org/).

For the API endpoints, you can open:

[http://localhost:8000/api/articles/](http://localhost:8000/api/articles/)

## Django Admin

The admin interface is available at:

[http://localhost:8000/admin/](http://localhost:8000/admin/)

## Database

The database is a PostgreSQL database run in a docker container.
