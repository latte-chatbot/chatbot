current_dir := $(shell pwd)
user := $(shell whoami)

ENDPOINTS = endpoints.yml
CREDENTIALS = credentials.yml

# CLEAR PROJECT
clean:
	make down
	cd bot/ && make clean

down:
	docker compose down

# RUN
init:
	make build
	make train
	make shell

deploy:
	make build
	make train
	make telegram

logs:
	docker compose logs \
		-f

build:
	docker compose build \
		--no-cache bot

shell:
	docker compose run \
		--rm \
		--service-ports \
		bot \
		make shell ENDPOINTS=$(ENDPOINTS)

actions:
	docker compose run \
		--rm \
		--service-ports \
		bot \
		make actions

telegram:
	docker compose run -d \
		--rm \
		--service-ports \
		bot-telegram \
		make telegram ENDPOINTS=$(ENDPOINTS) CREDENTIALS=$(CREDENTIALS)

# DEVELOPMENT
train:
	docker compose run \
		--rm  \
		bot \
		make train

validate:
	docker compose run \
		--rm bot \
		make validate

test:
	docker compose run \
		--rm bot \
		make test

test-nlu:
	docker compose run \
		--rm \
		bot \
		make test-nlu

test-core:
	docker compose run \
		--rm \
		bot \
		make test-core

model-report:
	docker compose run \
		--rm  \
		bot \
		make model-report