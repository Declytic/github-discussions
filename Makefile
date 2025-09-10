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
	python -c "import shutil, os; [shutil.rmtree(d, ignore_errors=True) for d in ['build', 'dist', '.pytest_cache', 'htmlcov'] if os.path.exists(d)]"
	python -c "import os; [os.remove(f) for f in ['.coverage'] if os.path.exists(f)]"
	python -c "import shutil, os, glob; [shutil.rmtree(d, ignore_errors=True) for d in glob.glob('*.egg-info')]"
	python -c "import shutil, os; [shutil.rmtree(os.path.join(root, d), ignore_errors=True) for root, dirs, files in os.walk('.') for d in dirs if d == '__pycache__']"
	python -c "import os; [os.remove(os.path.join(root, f)) for root, dirs, files in os.walk('.') for f in files if f.endswith('.pyc')]"

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
