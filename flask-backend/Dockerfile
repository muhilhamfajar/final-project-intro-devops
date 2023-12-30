FROM python:3.8

COPY requirement.txt /

RUN pip3 install --upgrade pip

RUN pip3 install -r /requirement.txt

WORKDIR /app

COPY . .

EXPOSE 5000

CMD ["gunicorn","--bind", "0.0.0.0:5000", "app:create_app()"]

# FROM python:3.8

# WORKDIR /app

# COPY . .

# RUN pip install -r requirement.txt

# EXPOSE 5000

# CMD ["python", "main.py"]