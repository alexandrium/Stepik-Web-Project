# git:    https://github.com/alexandrium/Stepik-Web-Project.git

sudo ln -fs /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart


sudo apt-get update
sudo apt-get install -y python3.5
# sudo apt-get install -y python3.5-dev
# sudo unlink /usr/bin/python3
sudo ln -fs /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install --upgrade pip
# sudo pip3 install --upgrade django==2.1
sudo pip3 install --upgrade gunicorn



### 1.9 Архитектура frontend-backend

sudo ln -fs /etc/gunicorn.d/hello.py /home/box/web/etc/g_conf.py
# cd /home/box/web
# python3.4 /usr/local/bin/gunicorn -b 0.0.0.0:8080 hello:app
# gunicorn -b 0.0.0.0:8080 hello:app

### 2.1 MVC фреймворки

# sudo pip3 install Django==2.2.14
sudo pip3 install Django==2.1
ALLOWED_HOSTS = ['*']

# commands
# django-admin startproject ask
# cd ask
# python3 manage.py startapp qa

# python manage.py runserver       # The development server

# gunicorn ask.wsgi
# gunicorn -b 0.0.0.0:8000 --workers=1 ask.wsgi
# gunicorn -b 0.0.0.0:8000  ask.wsgi
# python3.4 /usr/local/bin/gunicorn -b 0.0.0.0:8080 ask.wsgi

# sudo apt-get install sqlite3
# python3.5 /usr/local/bin/gunicorn -b 0.0.0.0:8080 ask.wsgi