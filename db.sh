sudo /etc/init.d/mysql start
mysql -u root -e "create database django"
mysql -u root -e "create user djangouser"
mysql -u root -e "GRANT ALL PRIVILEGES ON django.* To 'djangouser'@'localhost' IDENTIFIED BY 'pass'"
python3 /home/box/web/ask/manage.py makemigrations
python3 /home/box/web/ask/manage.py migrate
