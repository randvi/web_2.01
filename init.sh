# Nginx
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

#Gunicorn
#sudo rm -rf /etc/gunicorn.d/*
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln	-sf	/home/box/web/etc/gunicorn_ask.conf	/etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart

#sudo /etc/init.d/mysql start

