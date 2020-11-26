# RosSetiBackend

Backend of the RosSeti rationalization activity app

You can check out live project on [Heroku](https://rosseti.herokuapp.com/)

## Project setup 

1. `git clone https://github.com/Zaysevkun/DjangoECommerceAPI`
2.  `create POSTGRESQL db`
3. `cd DjangoECommerceAPI`
4. `python3 -m venv myvenv`
5. `source myvenv/bin/activate`
6. `pip install -r requirements.txt`
7. Add __.env__ file
##### EXAMPLE:
```
SECRET_KEY=qwerty123
DATABASE_URL=postgres://your_db_user_name:user_password@127.0.0.1:5432/your_db_name
ALLOWED_HOSTS=*
DEBUG=0
```
6. `python manage.py migrate`
7. `python manage.py collectstatic`
8. `python manage.py runserver 0.0.0.0:8000`
