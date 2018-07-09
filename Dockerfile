FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app

RUN pip2 install -r requirements.txt

ENTRYPOINT ["python2"]

CMD ["app/main.py"]
