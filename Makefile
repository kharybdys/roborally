test:
	uv run pytest

check:
	uv run ty check

lint:
	uv run ruff format --check
	uv run ruff check

format:
	uv run ruff format

fix:
	uv run ruff check --fix
