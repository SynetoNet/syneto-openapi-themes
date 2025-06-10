# Syneto OpenAPI Themes

[![PyPI version](https://badge.fury.io/py/syneto-openapi-themes.svg)](https://badge.fury.io/py/syneto-openapi-themes)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Test Coverage](https://img.shields.io/badge/coverage-98%25-brightgreen.svg)](./coverage.html)

Syneto-branded themes and utilities for OpenAPI documentation tools, built on top of [OpenAPIPages](https://github.com/syneto/openapipages). This library provides beautiful, consistent Syneto-branded themes for popular OpenAPI documentation tools including RapiDoc, SwaggerUI, ReDoc, Elements, and Scalar.

## Features

- 🎨 **Consistent Syneto Branding**: Official Syneto colors, fonts, and styling
- 🔧 **Multiple Documentation Tools**: Support for RapiDoc, SwaggerUI, ReDoc, Elements, and Scalar
- ⚡ **FastAPI Integration**: Easy integration with FastAPI applications
- 🌙 **Dark/Light Themes**: Support for both dark and light theme variants
- 📱 **Responsive Design**: Mobile-friendly documentation interfaces
- 🎯 **Type Safety**: Full TypeScript-style type hints for Python
- 🧪 **Well Tested**: 98% test coverage with comprehensive test suite

## Quick Start

### Installation

```bash
# Basic installation
pip install syneto-openapi-themes

# With FastAPI integration
pip install syneto-openapi-themes[fastapi]

# With all optional dependencies
pip install syneto-openapi-themes[all]
```

### Basic Usage

```python
from syneto_openapi_themes import SynetoRapiDoc, get_default_brand_config

# Create a Syneto-branded RapiDoc instance
brand_config = get_default_brand_config()
rapidoc = SynetoRapiDoc(
    openapi_url="/openapi.json",
    title="My API Documentation",
    brand_config=brand_config
)

# Render the documentation
html = rapidoc.render()
```

### FastAPI Integration

```python
from fastapi import FastAPI
from syneto_openapi_themes import add_syneto_rapidoc, get_default_brand_config

app = FastAPI(title="My API")
brand_config = get_default_brand_config()

# Add Syneto-branded documentation
add_syneto_rapidoc(
    app,
    openapi_url="/openapi.json",
    docs_url="/docs",
    brand_config=brand_config
)
```

## Documentation Structure

- **[Getting Started](./getting-started.md)** - Installation and basic setup
- **[API Reference](./api-reference.md)** - Complete API documentation
- **[Brand Configuration](./brand-configuration.md)** - Customizing Syneto branding
- **[Documentation Tools](./documentation-tools.md)** - Available documentation tools
- **[FastAPI Integration](./fastapi-integration.md)** - FastAPI-specific features
- **[Examples](./examples.md)** - Code examples and use cases
- **[Migration Guide](./migration-guide.md)** - Upgrading from other solutions
- **[Contributing](./contributing.md)** - Development and contribution guidelines

## Supported Documentation Tools

| Tool | Description | Status |
|------|-------------|--------|
| **RapiDoc** | Interactive API documentation with try-it-out functionality | ✅ Supported |
| **SwaggerUI** | The classic Swagger interface with full OpenAPI support | ✅ Supported |
| **ReDoc** | Clean, responsive documentation with excellent navigation | ✅ Supported |
| **Elements** | Modern, component-based documentation interface | ✅ Supported |
| **Scalar** | Beautiful, fast documentation with excellent UX | ✅ Supported |

## Architecture

The library is built with a modular architecture:

```
syneto-openapi-themes/
├── brand.py              # Brand configuration and theming
├── rapidoc.py            # RapiDoc integration
├── swagger.py            # SwaggerUI integration
├── redoc.py              # ReDoc integration
├── elements.py           # Elements integration
├── scalar.py             # Scalar integration
└── fastapi_integration.py # FastAPI-specific utilities
```

## Key Components

### Brand Configuration
- **SynetoBrandConfig**: Central configuration for all branding
- **SynetoColors**: Official Syneto color palette
- **SynetoTheme**: Theme variants (dark, light, auto)

### Documentation Tools
- **SynetoRapiDoc**: Syneto-branded RapiDoc implementation
- **SynetoSwaggerUI**: Syneto-branded SwaggerUI implementation
- **SynetoReDoc**: Syneto-branded ReDoc implementation
- **SynetoElements**: Syneto-branded Elements implementation
- **SynetoScalar**: Syneto-branded Scalar implementation

### FastAPI Integration
- **SynetoDocsManager**: Centralized documentation management
- **add_syneto_***: Individual tool integration functions
- **add_all_syneto_docs**: Add all documentation tools at once

## Requirements

- Python 3.9+
- OpenAPIPages 0.1.2+
- FastAPI 0.115.12+ (optional, for FastAPI integration)
- Jinja2 3.1.0+ (optional, for template features)

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## Support

- **Documentation**: [https://syneto.github.io/syneto-openapi-themes](https://syneto.github.io/syneto-openapi-themes)
- **Issues**: [GitHub Issues](https://github.com/syneto/syneto-openapi-themes/issues)
- **Email**: [dev@syneto.net](mailto:dev@syneto.net)

## Related Projects

- [OpenAPIPages](https://github.com/syneto/openapipages) - The underlying OpenAPI documentation framework
- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [RapiDoc](https://rapidocweb.com/) - Interactive OpenAPI documentation
- [SwaggerUI](https://swagger.io/tools/swagger-ui/) - Classic OpenAPI documentation interface 