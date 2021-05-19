FROM python:latest
LABEL AUTHOR "Kim Bahir Andersen, kim@bahir.dk"
WORKDIR /src
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD ["run-flask.py"]
EXPOSE 8000