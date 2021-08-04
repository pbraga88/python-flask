FROM python:3

WORKDIR /flask-rest-api

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./api ./api
COPY config.py .
COPY run.py .

EXPOSE 5000
CMD python3 run.py