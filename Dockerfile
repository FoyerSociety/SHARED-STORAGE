FROM python:3.7

ADD . /app/
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8080 

CMD python3 manage.py runserver 0.0.0.0:8080
