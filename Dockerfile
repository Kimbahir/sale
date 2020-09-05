FROM python:latest
RUN mkdir -p /src
WORKDIR /src
COPY ./requirements.txt .
COPY ./run-flask.py .
COPY ./app ./app/
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["run-flask.py"]
EXPOSE 8000