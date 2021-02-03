FROM python:3.7

RUN pip install flask flask_accept

EXPOSE 5000

COPY ./app /app

ENTRYPOINT [ "python3" ]

CMD [ "/app/main.py" ]
