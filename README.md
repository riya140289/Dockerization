Step 1: Install Prerequisites
Ensure you have the following installed on your machine:

Python (version 3.8 or higher)
Docker
Docker Compose

Step 2: Create a directory for your Django project
mkdir my_django_project
cd my_django_project


Step 3: Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate 

Step 4: Create a new Django project
django-admin startproject authortodo

Step 5: Create a New App
python manage.py startapp users


Step 6: Add your app to the INSTALLED_APPS list in myproject/settings.py

Step 7: Add the Rest framework details in Settings.py after installing the required packages


Step 7: Create Models and apply migrations to create the database tables
python manage.py makemigrations
python manage.py migrate


Step 8: Create Superuser if required
python manage.py createsuperuser

Step 9: Create an Admin Interface in admin.py if required

Step 10: Create a urls.py file in your app directory and configure URLs. Also create the views with business logic

Step 11: Configure static files in settings.py

Step 12: Run the project
python manage.py runserver

Step 13: Create a Dockerfile in the project directory

Step 14: Create a docker-compose.yml file and dockerignore in the project directory

Step 15: Create .env.web and .env.db files in the project directory

Step 16: Open the desktop Docker installed in your machine

Step 17: Build and start your containers in the docker
docker-compose up --build

Step 18: Your Django application should now be running and accessible at http://localhost:8000

