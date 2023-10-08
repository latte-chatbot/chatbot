FROM rasa/rasa-sdk:3.4.0

WORKDIR /bot

COPY ./bot /bot

USER root

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
 && rm -rf /var/lib/apt/lists/*

RUN pip install psycopg2

RUN pip install sqlalchemy


ENTRYPOINT []
CMD []
