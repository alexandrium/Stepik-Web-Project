# git:    git clone https://github.com/alexandrium/Stepik-Web-Project.git web

sudo ln -fs /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo apt-get update
sudo apt-get install -y python3.5
sudo ln -fs /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade gunicorn
# sudo pip3 install Django==2.2.14
sudo pip3 install Django==2.1


sudo ln -fs /etc/gunicorn.d/hello.py /home/box/web/etc/g_conf.py
# python3.4 /usr/local/bin/gunicorn -b 0.0.0.0:8080 hello:app

cd /home/box/web/ask
# python3.5 /usr/local/bin/gunicorn -b 0.0.0.0:8000 ask.wsgi


# sudo apt-get install -y sqlite3
# sudo pip3 install mysqlclient

# chmod 777 db.sqlite3  # needs for tests or not, I don't know ??



# Полезные ссылки

# https://djbook.ru/rel1.7/topics/forms/index.html              Работа с формами
# https://djbook.ru/rel1.7/ref/contrib/csrf.html                Подделка межсайтового запроса (CSRF)¶
# https://docs.djangoproject.com/en/3.0/topics/auth/default/    Using the Django authentication system¶
# https://djbook.ru/ch12s03.html                                Аутентификация пользователей
# https://docs.djangoproject.com/en/3.0/topics/http/sessions/   How to use sessions
# https://tutorial.djangogirls.org/ru/css/                      CSS — сделай это красиво!
# https://tutorial.djangogirls.org/ru/django_forms/             Формы в Django