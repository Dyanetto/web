sudo ln -fs /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -fs /home/box/web/etc/gunicorn_wsgi.conf   /etc/gunicorn.d/hello.py
sudo ln -fs /home/box/web/etc/gunicorn_django.conf   /etc/gunicorn.d/gunicorn_django.py
sudo /etc/init.d/gunicorn restart
