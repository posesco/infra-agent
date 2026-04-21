.PHONY: test lint clean build version-patch version-minor version-major

# Variables
PYTHON := python3

help:
	@echo "Available commands:"
	@echo "  test    - Run unit tests"
	@echo "  lint    - Run static analysis"
	@echo "  clean   - Clean build/temp files"

test:
	$(PYTHON) -m unittest discover tests

lint:
	flake8 src tests

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

version-patch:
	bumpversion patch

version-minor:
	bumpversion minor

version-major:
	bumpversion major
