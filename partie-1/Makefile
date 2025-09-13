# Variables

DOCKER_COMPOSE=docker-compose

# Targets
.PHONY: dev ruff test run build stop

dev:
	uv run uvicorn main:app --reload

ruff:
	uv run ruff check . --fix

build:
	$(DOCKER_COMPOSE) build

run:
	$(DOCKER_COMPOSE) up

stop:
	$(DOCKER_COMPOSE) down

test:
	pytest -v