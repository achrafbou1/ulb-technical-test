PROJECT_NAME = "ab-partie-3"
DOCKER_COMPOSE = docker-compose

help:
	@echo "Usage:"
	@echo "make [command]"
	@echo ""
	@echo "Commands:"
	@echo "	dev			Run the frontend for development"
	@echo "	add 		Add UI component"
	@echo "	lint		Lint & correct errors"
	@echo "	build		Build the frontend"
	@echo "	run			Run the frontend"
	@echo "	stop		Stop the frontend"

lint:
	pnpm run lint:fix

dev:
	pnpm run dev

add:
	pnpm dlx shadcn-vue@latest add $(filter-out $@,$(MAKECMDGOALS))

build:
	$(DOCKER_COMPOSE) build

run:
	$(DOCKER_COMPOSE) up

stop:
	$(DOCKER_COMPOSE) down
