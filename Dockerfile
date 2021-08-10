FROM python:3

WORKDIR /flask-rest-api

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./src ./src

EXPOSE 5000
CMD cd src && python3 run.py