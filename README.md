# Django_Rest_Framework
This is a rest api for Ecommerce Website written in Django Rest API which uses role based access policy. 
User can browse product details and category details.
tested ~~~3.8.5~~~

## Installation
~~~
- pip install -r requirements.txt
~~~
~~~
- python manage.py makemigrations && python mange.py migrate
~~~
**Create a superuser with the command**
~~~
- python manage.py createsuperuser
~~~
**Run the server**
~~~
- python manage.py runserver
~~~
## Test
~~~
- python manage.py test
~~~

## API path
**For Product**
~~~
http://127.0.0.1:8000/api/
~~~
**For category**
~~~
http://127.0.0.1:8000/api/category/
~~~
**For Authentication**
~~~
      http://127.0.0.1:8000/api/rest-auth/login/
      http://127.0.0.1:8000/api/rest-auth/logout/
      http://127.0.0.1:8000/api/rest-auth/password/reset/
      http://127.0.0.1:8000/api/rest-auth/password/reset/confirm/
      http://127.0.0.1:8000/api/rest-auth/registration/
~~~
