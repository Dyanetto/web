sudo /etc/init.d/mysql start
sudo mysql -u root -e "create database django"
sudo mysql -u root -e "create database djangouser"
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON django.* To 'djangouser'@'localhost' IDENTIFIED BY 'pass'"
sudo python /home/box/web/ask/manage.py syncdb
sudo ln -fs /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -fs /home/box/web/etc/gunicorn_wsgi.conf   /etc/gunicorn.d/hello.py
sudo ln -fs /home/box/web/etc/gunicorn_django.conf   /etc/gunicorn.d/gunicorn_django.py
sudo /etc/init.d/gunicorn restart
