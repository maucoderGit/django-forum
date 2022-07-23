# The Django forum.

A discussion forum is created with the idea to share opinions and talk about them with other people online.

This project was created with the idea from the most popular forum in the world: **Reddit**.

This project counts with a vote-up system, profile system, and comment system, the most important things in an online forum.

## Requirements

To run this project in debug mode, you must install all the requirements with the command:

```
pip3 install -r requirements.txt
```

Then run this:

```
source venv/bin/activate
cd django_reddit
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

With this, your code will be running in Development mode.

## Endpoints and models.

- Profile model.
    Based on the user abstract model, this model gets a website, biography, and phone number.
- Commentary Model.
    Gets a primary key of a profile and a post.
- Post Model.
    This model contains all the logic of the forum app.
    - number of likes
    - content
    - title
    - profile and user pk

We have two principal endpoints:

1. posts/
    - "/" empty endpoint, this is the feed of the app.
    - "posts/pk/", Display the post detail view.
    - "posts/pk/vote_up", Vote up a post and redirect to them.
    - "posts/create/", Display a form of the fields of a post.
2. users/
    - 'users/p/<str:username>/', display a profile using the username 
    - 'users/login/', to log in a user
    - 'users/logout/', to logout a user
    - 'users/signup/', display a form with all required fields to create a user.
    - 'users/me/profile/', display the user account detail view.