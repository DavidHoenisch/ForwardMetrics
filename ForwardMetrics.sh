#!/bin/bash

code_path = "/tmp/code/ForwardMetrics"
run_path = "/var/www/html"
req_path = "/tmp/code/ForwardMetrics/requirements.txt"

# copy code to runpath 
cp -r $code_path/app/* $run_path
cp req_path $run_path

apt install python3-pip

python3 -m venv /var/www/html/venv
source /var/www/html/venv/bin/activate

pip3 install -r /var/www/html/requirements.txt

python3 ./app.py
