# git:    git clone https://github.com/alexandrium/Stepik-Web-Project.git web

sudo ln -fs /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo apt-get update
sudo apt-get install -y python3.5
# sudo apt-get install -y python3.5-dev
sudo ln -fs /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade gunicorn
# sudo pip3 install Django==2.2.14
sudo pip3 install Django==2.1



sudo ln -fs /etc/gunicorn.d/hello.py /home/box/web/etc/g_conf.py

# cd /home/box/web
# python3.4 /usr/local/bin/gunicorn -b 0.0.0.0:8080 hello:app


cd /home/box/web/ask
# python3.4 /usr/local/bin/gunicorn -b 0.0.0.0:8080 ask.wsgi
# python3.5 /usr/local/bin/gunicorn -b 0.0.0.0:8080 ask.wsgi


# sudo apt-get install -y sqlite3
# sudo pip3 install mysqlclient