FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . ./

EXPOSE $PORT

CMD gunicorn --bind :$PORT Matcher:app
