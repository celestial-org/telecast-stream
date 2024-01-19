#!/usr/bin/bash

echo "Bắt đầu khởi động..."
gunicorn -b 0.0.0.0:5222 --log-level critical main:app