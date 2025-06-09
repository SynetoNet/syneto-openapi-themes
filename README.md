# Syneto OpenAPI Themes

Syneto-branded themes and utilities for OpenAPI documentation tools, built on top of [OpenAPIPages](https://github.com/hasansezertasan/openapipages).

## Features

- 🎨 **Syneto Branding** - Official Syneto colors, fonts, and styling
- 🚀 **Multiple Documentation Tools** - Support for RapiDoc, SwaggerUI, ReDoc, Elements, and Scalar
- 🔧 **Easy Integration** - Drop-in replacement for custom documentation implementations
- 🎯 **FastAPI Ready** - Seamless integration with FastAPI applications
- 📱 **Responsive Design** - Mobile-friendly documentation interfaces
- 🔐 **Authentication Support** - Built-in JWT and API key authentication handling
- ⚡ **Zero Dependencies** - Lightweight with minimal dependencies

## Installation

```bash
pip install syneto-openapi-themes
```

For FastAPI integration:
```bash
pip install syneto-openapi-themes[fastapi]
```

For all features:
```bash
pip install syneto-openapi-themes[all]
```

## Quick Start

### Basic Usage

```python
from fastapi import FastAPI
from syneto_openapi_themes import add_syneto_rapidoc

app = FastAPI(title="My API")

# Add Syneto-branded RapiDoc
add_syneto_rapidoc(app, docs_url="/docs")
```

### Custom Branding

```python
from syneto_openapi_themes import (
    SynetoBrandConfig, 
    SynetoTheme, 
    add_syneto_rapidoc
)

# Custom brand configuration
brand_config = SynetoBrandConfig(
    theme=SynetoTheme.LIGHT,
    company_name="My Company",
    logo_url="/static/my-logo.svg"
)

add_syneto_rapidoc(app, brand_config=brand_config)
```

### Multiple Documentation Tools

```python
from syneto_openapi_themes import add_all_syneto_docs

# Add all documentation tools
add_all_syneto_docs(
    app,
    rapidoc_url="/docs",
    swagger_url="/swagger", 
    redoc_url="/redoc",
    elements_url="/elements",
    scalar_url="/scalar"
)
```

### Using the Docs Manager (Recommended)

```python
from syneto_openapi_themes import SynetoDocsManager

# Create docs manager
docs_manager = SynetoDocsManager(app)

# Add all documentation tools with index page
docs_manager.add_all().add_docs_index("/documentation")

# Or add specific tools
docs_manager.add_rapidoc("/docs").add_swagger("/swagger")
```

## Documentation Tools

### RapiDoc
Modern, responsive API documentation with interactive features.

```python
from syneto_openapi_themes import SynetoRapiDoc

rapidoc = SynetoRapiDoc(
    openapi_url="/openapi.json",
    title="API Documentation"
)
```

### SwaggerUI
The classic Swagger interface with Syneto theming.

```python
from syneto_openapi_themes import SynetoSwaggerUI

swagger = SynetoSwaggerUI(
    openapi_url="/openapi.json",
    title="API Documentation"
)
```

### ReDoc
Clean, three-panel API documentation.

```python
from syneto_openapi_themes import SynetoReDoc

redoc = SynetoReDoc(
    openapi_url="/openapi.json", 
    title="API Documentation"
)
```

### Elements
Modern API documentation by Stoplight.

```python
from syneto_openapi_themes import SynetoElements

elements = SynetoElements(
    openapi_url="/openapi.json",
    title="API Documentation"
)
```

### Scalar
Beautiful, interactive API documentation.

```python
from syneto_openapi_themes import SynetoScalar

scalar = SynetoScalar(
    openapi_url="/openapi.json",
    title="API Documentation"
)
```

## Brand Configuration

### Default Syneto Theme

```python
from syneto_openapi_themes import SynetoBrandConfig

# Default dark theme
config = SynetoBrandConfig()

# Light theme
config = SynetoBrandConfig(theme=SynetoTheme.LIGHT)
```

### Custom Configuration

```python
config = SynetoBrandConfig(
    # Branding
    company_name="My Company",
    logo_url="/static/logo.svg",
    favicon_url="/static/favicon.ico",
    
    # Theme
    theme=SynetoTheme.DARK,
    primary_color="#ad0f6c",
    background_color="#07080d",
    
    # Typography
    regular_font="'Inter', sans-serif",
    mono_font="'JetBrains Mono', monospace",
    
    # Custom assets
    custom_css_urls=["/static/custom.css"],
    custom_js_urls=["/static/custom.js"]
)
```

### Available Colors

```python
from syneto_openapi_themes import SynetoColors

# Primary colors
SynetoColors.PRIMARY_MAGENTA  # #ad0f6c
SynetoColors.PRIMARY_DARK     # #07080d  
SynetoColors.PRIMARY_LIGHT    # #fcfdfe

# Accent colors
SynetoColors.ACCENT_RED       # #f01932
SynetoColors.ACCENT_BLUE      # #1e3a8a
SynetoColors.ACCENT_GREEN     # #059669
SynetoColors.ACCENT_YELLOW    # #d97706

# Neutral colors (100-900 scale)
SynetoColors.NEUTRAL_100      # #f8fafc
# ... through to ...
SynetoColors.NEUTRAL_900      # #0f172a
```

## Advanced Usage

### Authentication Configuration

```python
# JWT Authentication
rapidoc = SynetoRapiDoc(openapi_url="/openapi.json")
rapidoc.with_jwt_auth(jwt_url="/auth/token")

# API Key Authentication  
rapidoc.with_api_key_auth(api_key_name="X-API-Key")
```

### Custom CSS and JavaScript

```python
config = SynetoBrandConfig(
    custom_css_urls=[
        "/static/custom-theme.css",
        "https://fonts.googleapis.com/css2?family=Custom+Font"
    ],
    custom_js_urls=[
        "/static/analytics.js",
        "/static/custom-behavior.js"
    ]
)
```

### Framework Agnostic Usage

```python
from syneto_openapi_themes import SynetoRapiDoc

# Generate HTML for any framework
rapidoc = SynetoRapiDoc(openapi_url="/openapi.json")
html_content = rapidoc.render()

# Use with Flask, Django, etc.
@app.route('/docs')
def docs():
    return html_content
```

## Migration from Custom Implementation

If you're migrating from a custom RapiDoc implementation:

### Before (Custom Implementation)
```python
@app.get("/docs", response_class=HTMLResponse)
def custom_rapidoc_html():
    return custom_template_with_syneto_branding()
```

### After (Syneto OpenAPI Themes)
```python
from syneto_openapi_themes import add_syneto_rapidoc

add_syneto_rapidoc(app, docs_url="/docs")
```

## Development

### Setup
```bash
git clone <repository-url>
cd syneto-openapi-themes
poetry install
```

### Testing
```bash
poetry run pytest
```

### Code Quality
```bash
poetry run black .
poetry run ruff check .
poetry run mypy .
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run quality checks
6. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Credits

Built on top of [OpenAPIPages](https://github.com/hasansezertasan/openapipages) by Hasan Sezer Tasan. 