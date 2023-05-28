.PHONY: all clean actions

## FLAGS:
LOG_LEVEL = -vv
TRAIN_LOG_LEVEL = -v
RASA_ENDPOINTS = --endpoints
ENDPOINTS = endpoints.yml
RASA_CREDENTIALS = --credentials
CREDENTIALS = credentials.yml

# CLEAN PROJECT
clean:
	sudo rm -rf graph.html \
	       results/ \
	       models/* \
	       *.db* \
	       .*tensorboard* \
	       .rasa

install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

# RUN
shell:
	rasa shell \
		--enable-api\
		-m models/ \
		$(LOG_LEVEL) \
		$(RASA_ENDPOINTS) $(ENDPOINTS) \
		--port 5005

telegram:
	rasa run \
		--enable-api \
		-m models/ \
		$(LOG_LEVEL) \
		$(RASA_ENDPOINTS) $(ENDPOINTS) \
		$(RASA_CREDENTIALS) $(CREDENTIALS) \
		--cors '*' \
		--port 80

# ACTIONS
actions:
	rasa run actions \
		--enable-api \
		$(LOG_LEVEL) \
		--auto-reload \
		--actions actions

# DEVELOPMENT
train-nlu:
	rasa train nlu \
		$(LOG_LEVEL)

train:
	rasa train \
		$(TRAIN_LOG_LEVEL)

test:
	rasa test \
		--out results/

model-report:
	rasa-model-report --output-path results/
