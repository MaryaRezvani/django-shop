<h1>Django Shop</h1>
<h3>a example of a Django application which indicates a shop written in python</h3>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="40" height="40"/> </a>
<a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a>
<a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
</a>
<a href="https://www.postgresql.org/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/postgresql/postgresql-icon.svg" alt="ppostgresql" width="40" height="40"/> </a>
</p>

# Goal

This is a sample project to show you how to create a ecommerce website, and how to interact with users and payment gateway and also how to manage orders and products.


## Setup and Run the Project

1. **Clone the repository**:
   ```bash
   git clone git@github.com:MaryaRezvani/django-shop.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd django-shop
   ```

3. Copy the `.env-sample` file to `.env`:
   ```bash
   cp .env-sample .env


4. **Build the Docker images**:
   Build the Docker containers using the provided `docker-compose.yml` file.
   ```bash
   docker-compose build
   ```

5. **Run the project**:
   Start the Django application and its associated services by running:
   ```bash
   docker-compose up
   ```


## Database Migrations

1. **Apply migrations**:
   Run the migrations inside the Django container:
   ```bash
   docker compose exec backend sh -c "python manage.py makemigrations && python manage.py migrate"
   ```

2. **Create a superuser**:
   To create a superuser for accessing the Django admin panel:
   ```bash
   docker compose exec backend sh -c "python manage.py createsuperuser"
   ```
3. **Access the application**:
   Once the containers are up, you can access the application by visiting:
   ```bash
   http://localhost:8000
   ```


# Demo

<p align="center">
<img src="./docs/cover.png" width="100%">
</p>

# Database Schema

the provided schema is the main database design of the project based on the models we have used in django project.

<p align="center">
<img src="./docs/db-diagram.png" width="100%">
</p>
