# Django

## Setup

 - mkvirtualenv project
 - pip install django psycopg2
 - django-admin startproject project

 - edit manage.py database settings
 - ./manage.py migrate
 - ./manage.py runserver [[0.0.0.0:]8080]

 - ./manage.py startapp app

## Models

 - app/models.py:

    from django.db import models
    class AppClass(models.Model):
        textfield = models.CharField(max_length=200)
        datefield = models.DateTimeField('date published')
        inttfield = models.IntegerField(default=0)

 - settings.py:

    INSTALLED_APPS = (
        'app',
    )

 - ./manage.py makemigrations app
 - ./manage.py sqlmigrate app
 - ./manage.py migrate

 - models can have normal functions etc

## Shell

 - ./manage.py shell
 - from app import AppClass
 - AppClass.objects.all()
