#!/usr/bin/env bash
# Script sets up your web servers for the deployment of web_static

# Install nginx
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Create folders and file
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Hello World!" > /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to user and group
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

conf="\\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "45i $conf" /etc/nginx/sites-available/default

sudo service nginx restart
