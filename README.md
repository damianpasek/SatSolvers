# Sat Solvers

## Building frontend application

To build frontend application is required `npm` and `angular cli`

```
ng build -d static
```

## Django installation

```
pip install django
```

## Django Rest Framework

Django Rest Framework installation 
```
pip install djangorestframework
pip install django-cors-headers #required for CORS requests
```

## Django Server

To run Django server
```
python manage.py runserver
```

We are using Python 3, so on linux it might be `python3`

## Database

To create database make migrations
```
python manage.py makemigrations
```

Then migrate data
```
python manage.py migrate
```

## Admin panel

By default admin panel should be available at `/admin` endpoint. 

Creating admin account
```
python manage.py createsuperuser
```