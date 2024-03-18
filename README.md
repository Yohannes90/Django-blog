# TechCircle - tech community blog website

## Table of Contents

- [Overview](#overview)
- [Built With](#built-with)
- [File Structure](#file-structure)
- [Features](#features)
- [Usage](#usage)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Overview

- Welcome to my portfolio project, This project is a tech community blogging website that provides a platform for individuals interested in tech to share their thoughts, ideas, opinions, and information.
<div align="center">
    <img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*YhjKgGVWooqS9BHNemL8uQ.png" height=auto>
</ div>
- You can access a blog post about it [here](https://medium.com/@mekonnenyohannes90/portfolio-project-tech-community-blogging-website-e50ada9c841b/).
- You can access the live demo [here](https://www.techcircleethio.me/).


## Built With

- The project website is built using
    - **Python**
    - **Django**
    - **HTML**
    - **CSS**
    - **Bootstrap**
- It also utilizes
    - **Django-mail** for sending password reset emails to users,
    - **pillow** for profile image resizing,
    - **crispy** for elegant and customizable forms
    - **TypedJs** for typeing animation on home section,
    - **VScode** as IDE,
    - **git** and **github** as version control...

## File structure

        .
        ├── blog
        │   ├── admin.py
        │   ├── apps.py
        │   ├── __init__.py
        │   ├── migrations
        │   │   ├── 0001_initial.py
        │   │   ├── 0002_alter_post_date_posted.py
        │   │   ├── 0003_category_post_category.py
        │   │   ├── 0004_post_likes.py
        │   │   ├── __init__.py
        │   │   └── __pycache__
        │   │       ├── 0001_initial.cpython-310.pyc
        │   │       ├── 0002_alter_post_date_posted.cpython-310.pyc
        │   │       ├── 0003_category_post_category.cpython-310.pyc
        │   │       ├── 0004_post_likes.cpython-310.pyc
        │   │       └── __init__.cpython-310.pyc
        │   ├── models.py
        │   ├── __pycache__
        │   │   ├── admin.cpython-310.pyc
        │   │   ├── apps.cpython-310.pyc
        │   │   ├── __init__.cpython-310.pyc
        │   │   ├── models.cpython-310.pyc
        │   │   ├── urls.cpython-310.pyc
        │   │   └── views.cpython-310.pyc
        │   ├── static
        │   │   └── blog
        │   │       └── main.css
        │   ├── templates
        │   │   └── blog
        │   │       ├── about.html
        │   │       ├── base.html
        │   │       ├── categories.html
        │   │       ├── category_form.html
        │   │       ├── category_posts.html
        │   │       ├── home.html
        │   │       ├── post_confirm_delete.html
        │   │       ├── post_detail.html
        │   │       ├── post_form.html
        │   │       └── user_posts.html
        │   ├── tests.py
        │   ├── urls.py
        │   └── views.py
        ├── db.sqlite3
        ├── django_project
        │   ├── asgi.py
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-310.pyc
        │   │   ├── settings.cpython-310.pyc
        │   │   ├── urls.cpython-310.pyc
        │   │   └── wsgi.cpython-310.pyc
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── manage.py
        ├── media
        │   ├── default.jpg
        │   └── profile_pics
        │       ├── male.jpg
        │       ├── male_OKdATbh.jpg
        │       ├── male_UZ0xliT.jpg
        │       ├── male_yNuqvk5.jpg
        │       └── portfolio-7.PNG
        ├── __pycache__
        │   └── manage.cpython-310.pyc
        ├── README.md
        ├── requirements.txt
        ├── tree.txt
        └── users
            ├── admin.py
            ├── apps.py
            ├── forms.py
            ├── __init__.py
            ├── migrations
            │   ├── 0001_initial.py
            │   ├── __init__.py
            │   └── __pycache__
            │       ├── 0001_initial.cpython-310.pyc
            │       └── __init__.cpython-310.pyc
            ├── models.py
            ├── __pycache__
            │   ├── admin.cpython-310.pyc
            │   ├── apps.cpython-310.pyc
            │   ├── forms.cpython-310.pyc
            │   ├── __init__.cpython-310.pyc
            │   ├── models.cpython-310.pyc
            │   ├── signals.cpython-310.pyc
            │   └── views.cpython-310.pyc
            ├── signals.py
            ├── templates
            │   └── users
            │       ├── login.html
            │       ├── logout.html
            │       ├── password_reset_complete.html
            │       ├── password_reset_confirm.html
            │       ├── password_reset_done.html
            │       ├── password_reset.html
            │       ├── profile.html
            │       └── register.html
            ├── tests.py
            └── views.py


## Features

- The project includes the following sections:
    - User registration, autentication and authorization
    - login and logout
    - creating and updating User profile
    - viewing, creating, updating and deliting posts
    - viewing, creating, updating and deliting category
    - sorting interms of topic, and author
    - proper paginations
    - etc

## Things to include in near Future
    - Read more and less buttons in education and training section
    - Copy to clipboard on click for long links
    - Change picture
    - Add better projects


## Usage

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/Yohannes90/Django-blog
    $ cd Django-blog


Create project virtualenv for project:

    $ python3 -m venv ./venv


Activate the virtualenv for project:

    $ source ./venv/bin/activate


Install project dependencies:

    $ pip install -r requirements.txt


create super user:

    $ django-admin createsuperuser


Then simply apply the migrations:

    $ python manage.py migrate


You can now run the development server:

    $ python manage.py runserver


## Contact
[![Medium](https://img.shields.io/badge/Medium-12100E?logo=medium&logoColor=white)](https://medium.com/@Yohannes90)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/Yohannes90)
[![Discord](https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white)](https://discord.gg/Yohannes90)


## Acknowledgements
### I would like to acknowledge the following sources for their contributions:
-
