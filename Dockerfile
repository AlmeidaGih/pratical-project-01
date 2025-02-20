FROM python:3.12-alpine

WORKDIR /opt

COPY /app .

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python", "main.py"]