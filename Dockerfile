FROM python:3.10

COPY . .
RUN apt update && apt install -y ffmpeg
RUN pip install -r requirements.txt
RUN chmod +x ./start.sh
EXPOSE 8080
CMD ./start.sh