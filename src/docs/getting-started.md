# Getting Started

This guide will help you get up and running with Syneto OpenAPI Themes quickly.

## Installation

### Basic Installation

For basic usage without FastAPI integration:

```bash
pip install syneto-openapi-themes
```

### With FastAPI Integration

If you're using FastAPI and want the integration features:

```bash
pip install syneto-openapi-themes[fastapi]
```

### Full Installation

To install all optional dependencies:

```bash
pip install syneto-openapi-themes[all]
```

### Development Installation

For development or contributing:

```bash
git clone https://github.com/syneto/syneto-openapi-themes.git
cd syneto-openapi-themes
poetry install --with dev
```

## Basic Usage

### 1. Simple Documentation Generation

```python
from syneto_openapi_themes import SynetoRapiDoc, get_default_brand_config

# Get the default Syneto brand configuration
brand_config = get_default_brand_config()

# Create a RapiDoc instance with Syneto branding
rapidoc = SynetoRapiDoc(
    openapi_url="/openapi.json",
    title="My API Documentation",
    brand_config=brand_config
)

# Generate the HTML
html_content = rapidoc.render()

# Save to file or serve via web framework
with open("docs.html", "w") as f:
    f.write(html_content)
```

### 2. Using Different Documentation Tools

```python
from syneto_openapi_themes import (
    SynetoRapiDoc,
    SynetoSwaggerUI,
    SynetoReDoc,
    SynetoElements,
    SynetoScalar,
    get_default_brand_config
)

brand_config = get_default_brand_config()

# Choose your preferred documentation tool
rapidoc = SynetoRapiDoc(openapi_url="/openapi.json", brand_config=brand_config)
swagger = SynetoSwaggerUI(openapi_url="/openapi.json", brand_config=brand_config)
redoc = SynetoReDoc(openapi_url="/openapi.json", brand_config=brand_config)
elements = SynetoElements(openapi_url="/openapi.json", brand_config=brand_config)
scalar = SynetoScalar(openapi_url="/openapi.json", brand_config=brand_config)
```

### 3. Custom Brand Configuration

```python
from syneto_openapi_themes import SynetoBrandConfig, SynetoTheme, SynetoColors

# Create a custom brand configuration
custom_brand = SynetoBrandConfig(
    theme=SynetoTheme.LIGHT,
    primary_color=SynetoColors.ACCENT_BLUE,
    company_name="My Company",
    logo_url="/static/my-logo.svg"
)

# Use with any documentation tool
rapidoc = SynetoRapiDoc(
    openapi_url="/openapi.json",
    brand_config=custom_brand
)
```

## FastAPI Integration

### 1. Basic FastAPI Setup

```python
from fastapi import FastAPI
from syneto_openapi_themes import add_syneto_rapidoc, get_default_brand_config

# Create FastAPI app
app = FastAPI(
    title="My API",
    description="API with Syneto-branded documentation",
    version="1.0.0"
)

# Add Syneto-branded documentation
brand_config = get_default_brand_config()
add_syneto_rapidoc(
    app,
    openapi_url="/openapi.json",
    docs_url="/docs",
    brand_config=brand_config
)

# Your API endpoints
@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

### 2. Multiple Documentation Tools

```python
from fastapi import FastAPI
from syneto_openapi_themes import (
    add_syneto_rapidoc,
    add_syneto_swagger,
    add_syneto_redoc,
    get_default_brand_config
)

app = FastAPI(title="My API")
brand_config = get_default_brand_config()

# Add multiple documentation interfaces
add_syneto_rapidoc(app, docs_url="/docs", brand_config=brand_config)
add_syneto_swagger(app, docs_url="/swagger", brand_config=brand_config)
add_syneto_redoc(app, docs_url="/redoc", brand_config=brand_config)
```

### 3. Using the Documentation Manager

```python
from fastapi import FastAPI
from syneto_openapi_themes import SynetoDocsManager, get_default_brand_config

app = FastAPI(title="My API")
brand_config = get_default_brand_config()

# Create a documentation manager
docs_manager = SynetoDocsManager(app, brand_config=brand_config)

# Add documentation tools with method chaining
docs_manager.add_rapidoc("/docs") \
           .add_swagger("/swagger") \
           .add_redoc("/redoc") \
           .add_elements("/elements") \
           .add_scalar("/scalar") \
           .add_docs_index("/")  # Creates an index page with links to all docs
```

### 4. Add All Documentation Tools at Once

```python
from fastapi import FastAPI
from syneto_openapi_themes import add_all_syneto_docs, get_default_brand_config

app = FastAPI(title="My API")
brand_config = get_default_brand_config()

# Add all documentation tools with default URLs
add_all_syneto_docs(app, brand_config=brand_config)

# This creates:
# /docs - RapiDoc
# /swagger - SwaggerUI  
# /redoc - ReDoc
# /elements - Elements
# /scalar - Scalar
```

## Theme Customization

### 1. Using Built-in Themes

```python
from syneto_openapi_themes import get_default_brand_config, get_light_brand_config

# Dark theme (default)
dark_config = get_default_brand_config()

# Light theme
light_config = get_light_brand_config()
```

### 2. Custom Colors

```python
from syneto_openapi_themes import SynetoBrandConfig, SynetoColors

custom_config = SynetoBrandConfig(
    primary_color=SynetoColors.ACCENT_GREEN,
    background_color=SynetoColors.NEUTRAL_900,
    text_color=SynetoColors.NEUTRAL_100,
    nav_bg_color=SynetoColors.NEUTRAL_800
)
```

### 3. Custom Fonts and Assets

```python
custom_config = SynetoBrandConfig(
    regular_font="'Custom Font', sans-serif",
    mono_font="'Custom Mono', monospace",
    logo_url="/static/custom-logo.svg",
    favicon_url="/static/custom-favicon.ico",
    custom_css_urls=["/static/custom.css"],
    custom_js_urls=["/static/custom.js"]
)
```

## Configuration Options

### Common Parameters

All documentation tools support these common parameters:

```python
tool = SynetoRapiDoc(
    openapi_url="/openapi.json",      # URL to OpenAPI spec
    title="API Documentation",        # Page title
    brand_config=brand_config,        # Syneto brand configuration
    favicon_url="/favicon.ico",       # Custom favicon
    **kwargs                          # Tool-specific options
)
```

### Tool-Specific Options

Each documentation tool has specific configuration methods:

```python
# RapiDoc specific
rapidoc = SynetoRapiDoc(openapi_url="/openapi.json")
rapidoc.with_jwt_auth("/auth/token")
rapidoc.with_api_key_auth("X-API-Key")

# SwaggerUI specific  
swagger = SynetoSwaggerUI(openapi_url="/openapi.json")
swagger.with_oauth2(client_id="my-client")

# ReDoc specific
redoc = SynetoReDoc(openapi_url="/openapi.json")
redoc.with_search_disabled()

# Elements specific
elements = SynetoElements(openapi_url="/openapi.json")
elements.with_sidebar_layout()

# Scalar specific
scalar = SynetoScalar(openapi_url="/openapi.json")
scalar.with_modern_layout()
```

## Next Steps

- **[API Reference](./api-reference.md)** - Detailed API documentation
- **[Brand Configuration](./brand-configuration.md)** - Advanced branding options
- **[Documentation Tools](./documentation-tools.md)** - Tool-specific features
- **[Examples](./examples.md)** - More complex examples and use cases

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure you have the correct optional dependencies installed
   ```bash
   pip install syneto-openapi-themes[fastapi]
   ```

2. **Missing OpenAPI Spec**: Ensure your OpenAPI URL is accessible
   ```python
   # Test your OpenAPI URL
   import requests
   response = requests.get("http://localhost:8000/openapi.json")
   print(response.status_code)  # Should be 200
   ```

3. **Styling Issues**: Check that custom CSS/JS URLs are accessible
   ```python
   brand_config = SynetoBrandConfig(
       custom_css_urls=["http://localhost:8000/static/custom.css"]
   )
   ```

### Getting Help

- Check the [API Reference](./api-reference.md) for detailed documentation
- Look at [Examples](./examples.md) for common use cases
- Open an issue on [GitHub](https://github.com/syneto/syneto-openapi-themes/issues)
- Contact us at [dev@syneto.net](mailto:dev@syneto.net) 