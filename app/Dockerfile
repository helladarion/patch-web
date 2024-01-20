FROM python:3.12.1-alpine
WORKDIR /app
RUN apk update && apk add bash build-base libffi-dev
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --only-binary=:all
COPY . /app
ENTRYPOINT ["python3"]
CMD ["app.py"]
