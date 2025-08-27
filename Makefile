.PHONY: format lint test
format:
	black projects
lint:
	ruff projects
test:
	pytest -q
