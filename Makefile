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
	sudo docker compose run \
		-d \
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

model-report:
	docker compose run \
		--rm  \
		bot \
		make model-report
