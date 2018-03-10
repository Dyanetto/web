sudo /etc/init.d/mysql start
sudo mysql -u root -e "create database django"
sudo mysql -u root -e "create user djangouser"
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON django.* To 'djangouser'@'localhost' IDENTIFIED BY 'pass'"
sudo python3 /home/box/web/ask/manage.py makemigrations
sudo python3 /home/box/web/ask/manage.py migrate
