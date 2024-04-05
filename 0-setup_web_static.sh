#!/usr/bin/env bash
# Script sets up your web servers for the deployment of web_static

# Install nginx
sudo apt-get update
sudo apt-get -y install nginx

# Create folders and file
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "Hello World!" > /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to user and group
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

sudo bash -c 'echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $hostname;
    root /var/www/html;
    index index.html;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html;
    }
    location /redirect_me {
        return 301 http://www.google.com;
    }
    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}" > /etc/nginx/sites-available/default'


sudo service nginx restart