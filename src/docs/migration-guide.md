# Migration Guide

This guide helps you migrate from other OpenAPI documentation solutions to Syneto OpenAPI Themes.

## Overview

Syneto OpenAPI Themes is designed to be a drop-in replacement for most existing OpenAPI documentation solutions while providing enhanced branding and theming capabilities. This guide covers migration from popular alternatives.

## Migration from FastAPI Default Docs

### Before (FastAPI Default)

```python
from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="API documentation",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

### After (Syneto OpenAPI Themes)

```python
from fastapi import FastAPI
from syneto_openapi_themes import add_syneto_rapidoc, add_syneto_redoc, get_default_brand_config

app = FastAPI(
    title="My API",
    description="API documentation",
    version="1.0.0",
    docs_url=None,  # Disable default docs
    redoc_url=None  # Disable default redoc
)

# Add Syneto-branded documentation
brand_config = get_default_brand_config()
add_syneto_rapidoc(app, docs_url="/docs", brand_config=brand_config)
add_syneto_redoc(app, docs_url="/redoc", brand_config=brand_config)

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

### Key Changes

1. **Disable default documentation**: Set `docs_url=None` and `redoc_url=None`
2. **Add Syneto documentation**: Use `add_syneto_*` functions
3. **Configure branding**: Use `SynetoBrandConfig` for customization

## Migration from Swagger UI

### Before (Manual Swagger UI)

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/docs", response_class=HTMLResponse)
def get_docs():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>API Documentation</title>
        <link rel="stylesheet" type="text/css" href="/static/swagger-ui-bundle.css" />
    </head>
    <body>
        <div id="swagger-ui"></div>
        <script src="/static/swagger-ui-bundle.js"></script>
        <script>
            SwaggerUIBundle({
                url: '/openapi.json',
                dom_id: '#swagger-ui',
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIBundle.presets.standalone
                ]
            });
        </script>
    </body>
    </html>
    """
```

### After (Syneto SwaggerUI)

```python
from fastapi import FastAPI
from syneto_openapi_themes import add_syneto_swagger, get_default_brand_config

app = FastAPI()

# Add Syneto-branded SwaggerUI
brand_config = get_default_brand_config()
add_syneto_swagger(
    app,
    docs_url="/docs",
    brand_config=brand_config,
    deep_linking=True,
    filter=True
)
```

### Benefits of Migration

1. **Automatic branding**: No need to manually customize CSS
2. **Consistent theming**: Syneto colors and fonts applied automatically
3. **Reduced maintenance**: No need to manage static files
4. **Enhanced features**: Additional configuration options

## Migration from ReDoc

### Before (Manual ReDoc)

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/redoc", response_class=HTMLResponse)
def get_redoc():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>API Documentation</title>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">
        <style>
            body { margin: 0; padding: 0; }
        </style>
    </head>
    <body>
        <redoc spec-url='/openapi.json'></redoc>
        <script src="https://cdn.jsdelivr.net/npm/redoc@2.0.0/bundles/redoc.standalone.js"></script>
    </body>
    </html>
    """
```

### After (Syneto ReDoc)

```python
from fastapi import FastAPI
from syneto_openapi_themes import add_syneto_redoc, get_default_brand_config

app = FastAPI()

# Add Syneto-branded ReDoc
brand_config = get_default_brand_config()
add_syneto_redoc(
    app,
    docs_url="/redoc",
    brand_config=brand_config,
    hide_download_button=False,
    expand_responses=["200", "201"]
)
```

## Migration from RapiDoc

### Before (Manual RapiDoc)

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/docs", response_class=HTMLResponse)
def get_rapidoc():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>API Documentation</title>
        <meta charset="utf-8">
        <script type="module" src="https://unpkg.com/rapidoc/dist/rapidoc-min.js"></script>
    </head>
    <body>
        <rapi-doc 
            spec-url="/openapi.json"
            theme="dark"
            render-style="read"
            nav-bg-color="#2d3748"
            primary-color="#667eea"
        ></rapi-doc>
    </body>
    </html>
    """
```

### After (Syneto RapiDoc)

```python
from fastapi import FastAPI
from syneto_openapi_themes import add_syneto_rapidoc, get_default_brand_config

app = FastAPI()

# Add Syneto-branded RapiDoc
brand_config = get_default_brand_config()
add_syneto_rapidoc(
    app,
    docs_url="/docs",
    brand_config=brand_config,
    render_style="read",
    allow_try=True
)
```

## Migration from OpenAPIPages

### Before (OpenAPIPages)

```python
from fastapi import FastAPI
from openapipages import RapiDoc, SwaggerUI

app = FastAPI()

# Manual OpenAPIPages setup
rapidoc = RapiDoc(openapi_url="/openapi.json")
swagger = SwaggerUI(openapi_url="/openapi.json")

@app.get("/docs", response_class=HTMLResponse)
def get_docs():
    return rapidoc.render()

@app.get("/swagger", response_class=HTMLResponse)
def get_swagger():
    return swagger.render()
```

### After (Syneto OpenAPI Themes)

```python
from fastapi import FastAPI
from syneto_openapi_themes import (
    add_syneto_rapidoc,
    add_syneto_swagger,
    get_default_brand_config
)

app = FastAPI()

# Syneto-branded documentation
brand_config = get_default_brand_config()
add_syneto_rapidoc(app, docs_url="/docs", brand_config=brand_config)
add_syneto_swagger(app, docs_url="/swagger", brand_config=brand_config)
```

### Key Advantages

1. **Built-in branding**: Syneto colors and styling applied automatically
2. **Simplified setup**: No need to manually create routes
3. **Consistent theming**: All tools use the same brand configuration
4. **FastAPI integration**: Seamless integration with FastAPI applications

## Configuration Migration

### Environment Variables

If you were using environment variables for configuration:

```python
# Before
import os

DOCS_URL = os.getenv("DOCS_URL", "/docs")
API_TITLE = os.getenv("API_TITLE", "My API")
```

```python
# After
import os
from syneto_openapi_themes import SynetoBrandConfig, SynetoTheme

def get_brand_config():
    return SynetoBrandConfig(
        company_name=os.getenv("COMPANY_NAME", "My Company"),
        theme=SynetoTheme.DARK if os.getenv("THEME") == "dark" else SynetoTheme.LIGHT,
        logo_url=os.getenv("LOGO_URL", "/static/logo.svg")
    )

brand_config = get_brand_config()
```

### Custom CSS Migration

If you had custom CSS:

```css
/* Before - custom.css */
.swagger-ui .topbar {
    background-color: #2d3748;
}

.swagger-ui .info .title {
    color: #667eea;
}
```

```python
# After - using brand configuration
from syneto_openapi_themes import SynetoBrandConfig

brand_config = SynetoBrandConfig(
    nav_bg_color="#2d3748",
    primary_color="#667eea",
    custom_css_urls=["/static/additional-styles.css"]  # For any remaining custom styles
)
```

## Step-by-Step Migration Process

### Step 1: Install Syneto OpenAPI Themes

```bash
pip install syneto-openapi-themes[fastapi]
```

### Step 2: Disable Existing Documentation

```python
# Disable FastAPI default docs
app = FastAPI(
    title="My API",
    docs_url=None,
    redoc_url=None
)
```

### Step 3: Add Syneto Documentation

```python
from syneto_openapi_themes import add_syneto_rapidoc, get_default_brand_config

brand_config = get_default_brand_config()
add_syneto_rapidoc(app, brand_config=brand_config)
```

### Step 4: Customize Branding (Optional)

```python
from syneto_openapi_themes import SynetoBrandConfig, SynetoTheme, SynetoColors

custom_brand = SynetoBrandConfig(
    company_name="Your Company",
    theme=SynetoTheme.LIGHT,
    primary_color=SynetoColors.ACCENT_BLUE,
    logo_url="/static/your-logo.svg"
)

add_syneto_rapidoc(app, brand_config=custom_brand)
```

### Step 5: Test and Validate

```python
# Test that documentation is accessible
from fastapi.testclient import TestClient

client = TestClient(app)

def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200
    assert "Syneto" in response.text
```

## Common Migration Issues

### Issue 1: Static Files Not Loading

**Problem**: Custom logos or CSS files not loading.

**Solution**: Ensure static files are properly mounted:

```python
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")

brand_config = SynetoBrandConfig(
    logo_url="/static/logo.svg",
    custom_css_urls=["/static/custom.css"]
)
```

### Issue 2: Authentication Not Working

**Problem**: Authentication configuration not carried over.

**Solution**: Configure authentication in the documentation tool:

```python
# For RapiDoc
add_syneto_rapidoc(app, brand_config=brand_config)

# Authentication will be automatically detected from OpenAPI spec
# Or configure manually:
rapidoc = SynetoRapiDoc(openapi_url="/openapi.json", brand_config=brand_config)
rapidoc.with_jwt_auth("/auth/token")
```

### Issue 3: Custom Styling Lost

**Problem**: Custom styling not applied.

**Solution**: Use brand configuration or custom CSS:

```python
brand_config = SynetoBrandConfig(
    primary_color="#your-color",
    background_color="#your-bg",
    custom_css_urls=["/static/custom.css"]
)
```

### Issue 4: Multiple Documentation Tools

**Problem**: Need to maintain multiple documentation interfaces.

**Solution**: Use SynetoDocsManager:

```python
from syneto_openapi_themes import SynetoDocsManager

docs_manager = SynetoDocsManager(app, brand_config=brand_config)
docs_manager.add_rapidoc("/docs") \
           .add_swagger("/swagger") \
           .add_redoc("/redoc")
```

## Performance Considerations

### Before Migration

- Manual HTML generation
- Multiple static file requests
- Inconsistent caching

### After Migration

- Optimized HTML generation
- Built-in performance optimizations
- Consistent caching strategies

```python
# Enable caching for better performance
from functools import lru_cache

@lru_cache(maxsize=1)
def get_brand_config():
    return SynetoBrandConfig(...)

brand_config = get_brand_config()
```

## Testing Migration

### Create Migration Tests

```python
import pytest
from fastapi.testclient import TestClient

def test_migration_compatibility():
    """Test that migrated documentation works correctly."""
    client = TestClient(app)
    
    # Test documentation accessibility
    response = client.get("/docs")
    assert response.status_code == 200
    
    # Test branding is applied
    assert "Syneto" in response.text
    
    # Test OpenAPI spec is still accessible
    response = client.get("/openapi.json")
    assert response.status_code == 200

def test_feature_parity():
    """Test that all previous features still work."""
    client = TestClient(app)
    
    # Test API endpoints still work
    response = client.get("/")
    assert response.status_code == 200
    
    # Test authentication if applicable
    # ... your authentication tests
```

## Rollback Plan

If you need to rollback the migration:

### Quick Rollback

```python
# Temporarily disable Syneto docs and re-enable FastAPI defaults
app = FastAPI(
    title="My API",
    docs_url="/docs",      # Re-enable
    redoc_url="/redoc"     # Re-enable
)

# Comment out Syneto documentation
# add_syneto_rapidoc(app, brand_config=brand_config)
```

### Gradual Migration

```python
# Run both old and new documentation side by side
app = FastAPI(
    title="My API",
    docs_url="/docs-old",    # Keep old docs at different URL
    redoc_url="/redoc-old"   # Keep old redoc at different URL
)

# Add new Syneto documentation
add_syneto_rapidoc(app, docs_url="/docs", brand_config=brand_config)
add_syneto_redoc(app, docs_url="/redoc", brand_config=brand_config)
```

## Migration Checklist

- [ ] Install Syneto OpenAPI Themes
- [ ] Disable existing documentation
- [ ] Add Syneto documentation
- [ ] Configure branding
- [ ] Test documentation accessibility
- [ ] Verify API functionality
- [ ] Update documentation links
- [ ] Test authentication (if applicable)
- [ ] Validate custom styling
- [ ] Performance testing
- [ ] Update deployment scripts
- [ ] Train team on new features

## Getting Help

If you encounter issues during migration:

1. **Check the documentation**: Review the [API Reference](./api-reference.md) and [Examples](./examples.md)
2. **Test incrementally**: Migrate one documentation tool at a time
3. **Use debugging**: Enable debug mode for troubleshooting
4. **Contact support**: Reach out to [dev@syneto.net](mailto:dev@syneto.net)

## Post-Migration Benefits

After successful migration, you'll have:

- **Consistent branding** across all documentation
- **Reduced maintenance** overhead
- **Enhanced user experience** with Syneto design
- **Better performance** with optimized rendering
- **Future-proof** solution with ongoing updates 