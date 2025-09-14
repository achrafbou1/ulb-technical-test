help:
	@echo "Usage:"
	@echo "make [command]"
	@echo ""
	@echo "Commands:"
	@echo "	run			Run the script"
	@echo "	ruff		Lint & correct errors"

ruff:
	uv run ruff check . --fix

dev:
	python main.py