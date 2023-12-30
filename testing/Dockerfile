FROM python:3.8

RUN apt-get update && apt-get install -y xvfb

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]