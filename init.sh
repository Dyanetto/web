sudo /etc/init.d/mysql start
sudo mysql -u root -e "create database django"
sudo mysql -u root -e "create user djangouser"
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON django.* To 'djangouser'@'localhost' IDENTIFIED BY 'pass'"
sudo python3 /home/box/web/ask/manage.py makemigrations
sudo python3 /home/box/web/ask/manage.py migrate
sudo ln -fs /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -fs /home/box/web/etc/gunicorn_wsgi.conf   /etc/gunicorn.d/hello.py
sudo ln -fs /home/box/web/etc/gunicorn_django.conf   /etc/gunicorn.d/gunicorn_django.py
sudo /etc/init.d/gunicorn restart
