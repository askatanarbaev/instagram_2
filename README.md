# mini_shop
1) создайте виртуальное окружение активируйте и активируйте
2) python3 -m venv venv
3) . venv/bin/activate
4) pip install -r requairments.txt

5) создайте базу данных postgress 
create user <database user> with password 'your_super_secret_password';
alter role <database user> superuser ;
alter role <database user> with password 'your_super_secret_password';
alter role <database user> createrole createdb;
create database <database name> owner <database user>;  
  
6) python manage.py makemigrations
7) python manage.py migrate
8) python manage.py createsuperuser
9) python manage.py runserver
10) зойдите в админку создате категории, товары, и профиль )
