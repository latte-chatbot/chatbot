FROM python:3.10-slim

RUN apt-get update

RUN pip install pika

RUN pip install elasticsearch

COPY modules/consumer/consumer.py /consumer.py

CMD ["python", "/consumer.py"]