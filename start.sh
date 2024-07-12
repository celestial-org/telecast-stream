#!/usr/bin/bash

echo "Bắt đầu khởi động..."
python -u main.py &
gunicorn -b 0.0.0.0:8080 web:app