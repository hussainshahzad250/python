# CREATE DJANGO PROJECT 
1.	Set up the environment, Make sure you have Python installed. 

2.	Install Django and Django REST framework
Open your command prompt or terminal and run the following command to install Django and Django REST framework:
	
```pip install django djangorestframework```

3.	Create a new Django project, Run the following command to create a new Django project:

``` django-admin startproject your_project_name ```

4.	Navigate to the project directory, Go to the newly created project directory:

``` cd your_project_name```

5.	Create a Django app, Next
create a Django app within the project. Apps are the building blocks of a Django project and provide modularity to your application:

```python manage.py startapp your_app_name```

6. Define your models (optional)
If your application requires a database, define your models in the models.py file inside the app. Models define the structure of your database tables.

7.	Configure Django settings
Open settings.py in your project folder and add 'rest_framework' and your app to the INSTALLED_APPS list:

  ```
  INSTALLED_APPS = [
      # ...
      'rest_framework',
      'your_app_name',
      # ...
  ]
  ```

8. Serializers allow complex data types (e.g., QuerySets and model instances) to be converted to Python data types and rendered into JSON/XML content. Create a file named serializers.py inside your app and define your serializers.

9. Create views
Create a file named views.py inside your app and define the views that handle the API endpoints.

10. Configure URLs
Open urls.py inside your app and define the URL patterns for your API views.

11. Run migrations
Run the following command to apply the database migrations:

	```python manage.py makemigrations```

	```python manage.py migrate```

13.	Run the development server
Start the development server with the following command:

	```python manage.py runserver 8080```

	```http://localhost:8080```


# To install MySQL in your project, run below command
  ``` pip install pymysql ```

```
    DATABASES = {
        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': BASE_DIR / 'db.sqlite3',
        # }
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db_name',
            'USER': 'your_db_username',
            'PASSWORD': 'your_db_password',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
```
# To COR'S in your project, run below command
``` pip install django-cors-headers ```

```commandline
    INSTALLED_APPS = [
        ...
        # CORS
        'corsheaders',
        ...
    ]
```

```commandline
    MIDDLEWARE = [
        ...
        # CORS
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...
    ]
```

# To access django admin page

``` python manage.py createsuperuser ```

``` http://localhost:8080/admin```
  
	

