FROM rasa/rasa:3.4.2-full

WORKDIR /bot
COPY ./bot /bot

USER root
RUN apt-get install make && \
    make install

ENTRYPOINT []
CMD []
