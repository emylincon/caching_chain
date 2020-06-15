#!/usr/bin/env bash

apt update && apt upgrade -y
apt install python3-pip -y
apt install apache2 -y
apt install Libapache2-mod-wsgi-py3 -y
pip3 install flask
pip install flask-restful
