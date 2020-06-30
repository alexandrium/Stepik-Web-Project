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
