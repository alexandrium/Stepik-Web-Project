sudo /usr/local/nginx/sbin/nginx
gunicorn -b 0.0.0.0:8000 --workers=1 /Users/Home/PycharmProjects/Stepik-Web-Project/ask/ask.wsgi

# nginx config
# /usr/local/nginx/conf/nginx.conf

# Завершение nginx

# sudo /usr/local/nginx/sbin/nginx -s quit
# sudo nginx -s quit


# Возможные сигналы

# stop — быстрое завершение
# quit — плавное завершение
# reload — перезагрузка конфигурационного файла
# reopen — переоткрытие лог-файлов


# DataBases

# python3 manage.py makemigrations
# python3 manage.py migrate


# python3 manage.py runserver       # The development server



# GENERATE SECRET_KEY
# python3
# from django.core.management.utils import get_random_secret_key
# get_random_secret_key()


# Тестовый сервер с отдельными данными
# Runs a development server with data from the given fixture(s).
# python3 manage.py dumpdata > mydata.json
# python3 manage.py testserver mydata.json