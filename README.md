# How to install Django

`pip install django`

# How django create project

`django-admin startproject <projectname>`

# How django create app

`python manage.py startapp <appname>`

# How django create admin

## Need to migrate for let django know

`python manage.py migrate`

## Then create super user

`python manage.py createsuperuser`

# User for test

## user: evadaisie

    pass: eve555%%

## user: Newuser3

    pass: passpass55

# How migration?

- After you create model Post (for example)
  ** then `python manage.py makemigrations`
  ** to build migrations file.
- Next is you need django create database from migrations file for you
  \*\* just type `python manage.py sqlmigrate blog 0001 (blog = project name, 0001 is migration file)

## What's migration?

### migration cmd for prepare every thing like a create Post model

### Cart model, it generate file under migrations folder

### migrate cmd is execute every thing from migration.

# Resource

https://stackoverflow.com/questions/26713443/django-delete-superuser
https://stackoverflow.com/questions/52351756/django-typeerror-save-got-an-unexpected-keyword-argument-force-insert

