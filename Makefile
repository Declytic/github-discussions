.PHONY: help install install-dev test test-cov test-unit test-integration lint format clean build docs pre-commit pre-commit-install pre-commit-run

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

install: ## Install the package
	pip install -e .

install-dev: ## Install the package with development dependencies
	pip install -e ".[dev]"

test: ## Run all tests
	pytest

test-cov: ## Run tests with coverage
	pytest --cov=github_discussions --cov-report=html --cov-report=term

test-unit: ## Run unit tests only
	pytest -m "not integration"

test-integration: ## Run integration tests only
	pytest -m integration

lint: ## Run linting
	flake8 github_discussions tests
	mypy github_discussions

format: ## Format code
	black github_discussions tests examples
	isort github_discussions tests examples

clean: ## Clean up generated files
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: ## Build the package
	python -m build

docs: ## Build documentation
	sphinx-build -b html docs docs/_build/html

pre-commit-install: ## Install pre-commit hooks
	pre-commit install

pre-commit-run: ## Run pre-commit on all files
	pre-commit run --all-files

pre-commit: ## Update pre-commit hooks
	pre-commit autoupdate

check: ## Run all checks (format, lint, test)
	make format
	make lint
	make test

release: ## Build and release (requires twine)
	make clean
	make build
	twine check dist/*
	@echo "Ready to release. Run: twine upload dist/*"
