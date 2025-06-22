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

### Logo Customization

**NEW**: Syneto OpenAPI Themes now includes the official Syneto logo by default! No configuration needed for Syneto projects.

```python
from syneto_openapi_themes import add_syneto_rapidoc

# Default configuration automatically includes the official Syneto logo
add_syneto_rapidoc(app, docs_url="/docs")
```

You can still customize the logo with either external URLs or inline SVG content:

#### Using Logo URLs

```python
from syneto_openapi_themes import get_brand_config_with_custom_logo

# Use a local logo file
config = get_brand_config_with_custom_logo("/static/my-company-logo.svg")

# Use an external logo URL
config = get_brand_config_with_custom_logo("https://example.com/logo.svg")

# Combine with other customizations
config = get_brand_config_with_custom_logo(
    "/static/my-logo.svg",
    theme=SynetoTheme.LIGHT,
    company_name="My Company",
    primary_color="#ff0000"
)
```

#### Using Inline SVG Content (Recommended)

For better performance and reliability, you can embed SVG content directly:

```python
from syneto_openapi_themes import get_brand_config_with_svg_logo, SYNETO_LOGO_SVG

# Option 1: Use your own custom SVG
custom_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 50">
    <rect width="200" height="50" fill="#ad0f6c"/>
    <text x="100" y="30" text-anchor="middle" fill="white" font-family="Arial" font-size="16">
        My Company
    </text>
</svg>'''

config = get_brand_config_with_svg_logo(custom_svg, company_name="My Company")

# Option 2: Use the official Syneto logo constant explicitly
config = get_brand_config_with_svg_logo(
    SYNETO_LOGO_SVG,  # Official Syneto logo (same as default)
    company_name="Syneto"
)

# Combine with other customizations
config = get_brand_config_with_svg_logo(
    custom_svg,
    theme=SynetoTheme.LIGHT,
    company_name="My Company",
    primary_color="#ff0000"
)

# Use with any documentation tool
add_syneto_rapidoc(app, brand_config=config)
```

#### Manual Configuration

```python
from syneto_openapi_themes import SynetoBrandConfig, svg_to_data_uri

# Convert SVG to data URI manually
svg_content = '''<svg>...</svg>'''
data_uri = svg_to_data_uri(svg_content)

# Use in brand config
config = SynetoBrandConfig(
    logo_svg=svg_content,  # Inline SVG takes precedence
    logo_url="/fallback/logo.svg",  # Fallback URL
    company_name="My Company"
)
```

#### Custom Header Slot (Advanced)

For complete control over the header appearance, you can provide custom HTML content that will be placed in RapiDoc's header slot:

```python
from syneto_openapi_themes import add_syneto_rapidoc

# Custom header with logo and additional elements
custom_header = '''
<div style="display: flex; align-items: center; justify-content: space-between; width: 100%;">
    <div style="display: flex; align-items: center;">
        <img src="/static/logo.svg" alt="My API" style="height: 40px; margin-right: 12px;" />
        <span style="color: #bbb; font-weight: 600; font-size: 18px;">My API Documentation</span>
    </div>
    <div style="display: flex; align-items: center; gap: 16px;">
        <span style="color: #999; font-size: 14px;">v1.0.0</span>
        <a href="/health" style="color: #ff53a8; text-decoration: none;">Health Check</a>
    </div>
</div>
'''

add_syneto_rapidoc(
    app,
    docs_url="/docs",
    header_slot_content=custom_header
)
```

**Header Slot Benefits:**
- **Complete Control**: Full control over header layout and content
- **Interactive Elements**: Can include buttons, dropdowns, links, etc.
- **Proper Positioning**: Content appears in the RapiDoc header, not below it
- **Responsive Design**: Your CSS controls the responsive behavior
- **JavaScript Support**: Can include interactive JavaScript functionality

**Logo Requirements:**
- **Format**: SVG recommended for best scaling and quality
- **Size**: Optimal dimensions are approximately 120x32 pixels
- **Colors**: Should work well on dark backgrounds (default theme)
- **Accessibility**: Include proper alt text and contrast ratios
- **Built-in Logo Benefits**: Zero configuration for Syneto projects, consistent branding
- **Inline SVG Benefits**: No external requests, better performance, works offline
- **Still Customizable**: Easy to override when needed

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