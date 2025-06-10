# Contributing to Syneto OpenAPI Themes

Thank you for your interest in contributing to Syneto OpenAPI Themes! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Code Style](#code-style)
- [Submitting Changes](#submitting-changes)
- [Release Process](#release-process)

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you are expected to uphold this code.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment
4. Create a new branch for your changes
5. Make your changes
6. Test your changes
7. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.9 or higher
- Poetry for dependency management
- Git

### Setup Instructions

1. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/syneto-openapi-themes.git
cd syneto-openapi-themes
```

2. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies:
```bash
poetry install
```

4. Activate the virtual environment:
```bash
poetry shell
```

5. Install pre-commit hooks (optional but recommended):
```bash
poetry run pre-commit install
```

## Making Changes

### Branch Naming

Use descriptive branch names:
- `feature/add-new-theme` for new features
- `fix/swagger-ui-styling` for bug fixes
- `docs/update-readme` for documentation updates
- `refactor/theme-config` for refactoring

### Commit Messages

Follow conventional commit format:
- `feat: add new Syneto dark theme`
- `fix: resolve RapiDoc CSS conflicts`
- `docs: update installation instructions`
- `test: add tests for theme configuration`
- `refactor: simplify brand config structure`

## Testing

### Running Tests

Run the full test suite:
```bash
poetry run pytest
```

Run tests with coverage:
```bash
poetry run pytest --cov=syneto_openapi_themes --cov-report=html
```

Run specific test files:
```bash
poetry run pytest tests/test_themes.py
```

Run tests by marker:
```bash
poetry run pytest -m "not slow"
```

### Writing Tests

- Write tests for all new functionality
- Maintain or improve code coverage (target: 85%+)
- Use descriptive test names
- Follow the AAA pattern (Arrange, Act, Assert)
- Use pytest fixtures for common setup

Example test structure:
```python
def test_syneto_rapidoc_theme_configuration():
    # Arrange
    config = SynetoBrandConfig(theme=SynetoTheme.DARK)
    
    # Act
    rapidoc = SynetoRapiDoc(brand_config=config)
    
    # Assert
    assert rapidoc.theme == SynetoTheme.DARK
```

## Code Style

### Formatting and Linting

This project uses:
- **Black** for code formatting
- **Ruff** for linting
- **MyPy** for type checking

Run all checks:
```bash
poetry run black .
poetry run ruff check .
poetry run mypy src/syneto_openapi_themes
```

### Code Standards

- Follow PEP 8 style guidelines
- Use type hints for all functions and methods
- Write docstrings for public APIs
- Keep line length to 120 characters
- Use meaningful variable and function names

### Type Hints

Always include type hints:
```python
from typing import Optional, Dict, Any

def create_theme_config(
    theme: SynetoTheme,
    custom_colors: Optional[Dict[str, str]] = None
) -> Dict[str, Any]:
    """Create theme configuration dictionary."""
    pass
```

### Documentation

- Write clear docstrings for all public functions and classes
- Include examples in docstrings when helpful
- Update README.md for new features
- Add type information to docstrings

Example docstring:
```python
def add_syneto_rapidoc(
    app: FastAPI,
    docs_url: str = "/docs",
    brand_config: Optional[SynetoBrandConfig] = None
) -> None:
    """Add Syneto-branded RapiDoc to FastAPI application.
    
    Args:
        app: FastAPI application instance
        docs_url: URL path for documentation
        brand_config: Optional brand configuration
        
    Example:
        >>> from fastapi import FastAPI
        >>> from syneto_openapi_themes import add_syneto_rapidoc
        >>> 
        >>> app = FastAPI()
        >>> add_syneto_rapidoc(app, docs_url="/docs")
    """
```

## Submitting Changes

### Pull Request Process

1. Ensure all tests pass
2. Update documentation if needed
3. Add entries to CHANGELOG.md
4. Create a pull request with:
   - Clear title and description
   - Reference to related issues
   - Screenshots if UI changes
   - Test coverage information

### Pull Request Template

Use the provided PR template and fill out all relevant sections:
- Description of changes
- Type of change
- Testing performed
- Checklist completion

### Review Process

- All PRs require at least one review
- Address review feedback promptly
- Keep PRs focused and reasonably sized
- Rebase on main before merging

## Release Process

### Version Numbering

This project follows [Semantic Versioning](https://semver.org/):
- `MAJOR.MINOR.PATCH` (e.g., 1.2.3)
- Major: Breaking changes
- Minor: New features (backward compatible)
- Patch: Bug fixes (backward compatible)

### Release Steps

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create a GitHub release
4. Automated workflows will publish to PyPI

## Getting Help

- Check existing issues and discussions
- Create a new issue for bugs or feature requests
- Join our community discussions
- Contact the maintainers

## Recognition

Contributors will be recognized in:
- CHANGELOG.md for significant contributions
- GitHub contributors list
- Release notes for major features

Thank you for contributing to Syneto OpenAPI Themes! 