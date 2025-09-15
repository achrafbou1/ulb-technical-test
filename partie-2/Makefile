PROJECT_NAME = "ab-partie-2"

help:
	@echo "Usage:"
	@echo "make [command]"
	@echo ""
	@echo "Commands:"
	@echo "	build		Build the script"
	@echo "	run			Run the script"
	@echo "	lint		Lint & correct errors"

lint:
	black .
	uv run ruff check . --fix

build:
	docker build . -t $(PROJECT_NAME)

run:
	docker container rm -f $(PROJECT_NAME)
	docker run --name $(PROJECT_NAME) -d $(PROJECT_NAME)
	@sleep 20
	docker cp $(PROJECT_NAME):/app/bulletin.csv .
	docker cp $(PROJECT_NAME):/app/rapport_anomalies.json .
	docker rm -f $(PROJECT_NAME)