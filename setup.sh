#!/usr/bin/env bash

apt update && apt upgrade -y
apt install python3-pip -y
apt install nano -y
apt install net-tools -y
apt install nginx -y
pip3 install flask
pip3 install flask-restful
pip3 install gunicorn

rm /etc/nginx/sites-enabled/default
mv flask_settings /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/flask_settings /etc/nginx/sites-enabled/flask_settings
/etc/init.d/nginx restart