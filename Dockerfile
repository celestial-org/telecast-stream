FROM python:3.10

RUN useradd -u 1000 user
COPY . /home/user
WORKDIR /home/user
RUN apt update && apt install -y ffmpeg wget
RUN wget -O lite.gz https://github.com/xxf098/LiteSpeedTest/releases/download/v0.15.0/lite-linux-amd64-v0.15.0.gz && gzip -d lite.gz && chmod +x lite
RUN pip install -r requirements.txt
RUN chmod +x ./start.sh
RUN chown user:user /home/user
USER user
EXPOSE 8080
CMD ./start.sh