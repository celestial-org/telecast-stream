FROM python:3.10

RUN useradd -u 1000 user
COPY . /home/user
WORKDIR /home/user
RUN apt update && apt install -y ffmpeg
RUN pip install -r requirements.txt
RUN chmod +x ./start.sh
RUN chown user:user /home/user
USER user
EXPOSE 8080
CMD ./start.sh