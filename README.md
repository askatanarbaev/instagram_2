# mini_shop
1) создайте виртуальное окружение активируйте и активируйте
2) python3 -m venv venv
3) . venv/bin/activate
4) pip install -r requairments.txt

5) создайте базу данных postgress 
6) create user "database user" with password 'your_super_secret_password';
7) alter role "database user" superuser ;
8) alter role "database user" with password 'your_super_secret_password';
9) alter role "database user" createrole createdb;
10) create database "database name" owner <database user>;  
  
11) python manage.py makemigrations
12) python manage.py migrate
13) python manage.py createsuperuser
14) python manage.py runserver
15) зойдите в админку создате категории, товары, и профиль )
