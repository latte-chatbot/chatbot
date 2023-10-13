FROM rasa/rasa:3.4.2-full

WORKDIR /bot

COPY ./bot /bot

USER root

RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT []
CMD []
