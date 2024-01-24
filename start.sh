#!/usr/bin/bash
export FFMPEG="" VIDEO_QUAL=1920,1080,60 AUDIO_QUAL=20000,2
echo "Bắt đầu khởi động..."
python -u client.py &
gunicorn -b 0.0.0.0:8080 --timeout 100000 --log-level critical main:app