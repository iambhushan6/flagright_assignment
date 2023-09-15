FROM --platform=linux/amd64 python:3.9-slim

WORKDIR / myapp

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python manage.py runserver
