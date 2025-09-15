PROJECT_NAME = "ab-partie-3"

help:
	@echo "Usage:"
	@echo "make [command]"
	@echo ""
	@echo "Commands:"
	@echo "	dev			Run the frontend for development"
	@echo "	add 		Add UI component"
	@echo "	lint		Lint & correct errors"

lint:
	pnpm run lint:fix

dev:
	pnpm run dev

add:
	pnpm dlx shadcn-vue@latest add $(filter-out $@,$(MAKECMDGOALS))