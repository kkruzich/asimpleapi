FROM python:3.7

RUN pip install flask flask_accept

EXPOSE 5000

COPY ./app /app

ENV FLASK_APP=main
ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /app

ENTRYPOINT FLASK_APP=/app/main.py flask run --host=0.0.0.0
