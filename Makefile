.PHONY: help install test lint format type-check security clean build publish-test publish docs

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	poetry install

install-dev: ## Install development dependencies
	poetry install --with dev

test: ## Run tests
	poetry run pytest

test-cov: ## Run tests with coverage
	poetry run pytest --cov=syneto_openapi_themes --cov-report=html --cov-report=term-missing

test-fast: ## Run tests without slow tests
	poetry run pytest -m "not slow"

lint: ## Run linting
	poetry run ruff check .

lint-fix: ## Run linting with auto-fix
	poetry run ruff check . --fix

format: ## Format code
	poetry run black .

format-check: ## Check code formatting
	poetry run black --check .

type-check: ## Run type checking
	poetry run mypy src/syneto_openapi_themes

security: ## Run security checks
	poetry run safety check
	poetry run bandit -r src/syneto_openapi_themes/

quality: ## Run all quality checks
	$(MAKE) format-check
	$(MAKE) lint
	$(MAKE) type-check
	$(MAKE) security
	$(MAKE) test-cov

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build: ## Build package
	poetry build

publish-test: ## Publish to TestPyPI
	poetry config repositories.testpypi https://test.pypi.org/legacy/
	poetry publish -r testpypi

publish: ## Publish to PyPI
	poetry publish

docs: ## Generate documentation
	@echo "Documentation generation not yet implemented"

dev-setup: ## Set up development environment
	poetry install --with dev
	poetry run pre-commit install

update: ## Update dependencies
	poetry update

version: ## Show current version
	poetry version

bump-patch: ## Bump patch version
	poetry version patch

bump-minor: ## Bump minor version
	poetry version minor

bump-major: ## Bump major version
	poetry version major 