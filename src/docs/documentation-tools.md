# Documentation Tools

This guide covers all the supported OpenAPI documentation tools and their specific features and customization options.

## Overview

Syneto OpenAPI Themes supports five popular documentation tools, each with its own strengths and use cases:

- **RapiDoc**: Interactive documentation with try-it-out functionality
- **SwaggerUI**: The classic Swagger interface with full OpenAPI support
- **ReDoc**: Clean, responsive documentation with excellent navigation
- **Elements**: Modern, component-based documentation interface
- **Scalar**: Beautiful, fast documentation with excellent UX

## RapiDoc

RapiDoc provides an interactive API documentation experience with built-in try-it-out functionality.

### Features

- Interactive API testing
- Multiple layout options
- Authentication support
- Code generation
- Customizable themes

### Basic Usage

```python
from syneto_openapi_themes import SynetoRapiDoc, get_default_brand_config

brand_config = get_default_brand_config()
rapidoc = SynetoRapiDoc(
    openapi_url="/openapi.json",
    title="My API Documentation",
    brand_config=brand_config
)

html = rapidoc.render()
```

### Configuration Options

```python
rapidoc = SynetoRapiDoc(
    openapi_url="/openapi.json",
    title="API Documentation",
    brand_config=brand_config,
    
    # RapiDoc-specific options
    render_style="read",           # "read", "view", "focused"
    layout="row",                  # "row", "column"
    schema_style="tree",           # "tree", "table"
    default_schema_tab="schema",   # "schema", "example"
    response_area_height="300px",
    show_header=True,
    show_info=True,
    allow_try=True,
    allow_spec_url_load=False,
    allow_spec_file_load=False
)
```

### Authentication Configuration

```python
# JWT Authentication
rapidoc.with_jwt_auth(token_url="/auth/token")

# API Key Authentication
rapidoc.with_api_key_auth(api_key_name="X-API-Key")

# Custom authentication configuration
auth_config = rapidoc.get_authentication_config()
auth_config.update({
    "jwt_header_name": "Authorization",
    "jwt_token_prefix": "Bearer ",
    "api_key_location": "header"
})
```

### Best Use Cases

- APIs that need interactive testing
- Developer-focused documentation
- APIs with complex request/response structures
- Internal APIs where try-it-out is valuable

## SwaggerUI

The classic Swagger interface with comprehensive OpenAPI support and familiar user experience.

### Features

- Familiar Swagger interface
- OAuth2 support
- Request/response examples
- Model documentation
- Download spec functionality

### Basic Usage

```python
from syneto_openapi_themes import SynetoSwaggerUI, get_default_brand_config

brand_config = get_default_brand_config()
swagger = SynetoSwaggerUI(
    openapi_url="/openapi.json",
    title="My API Documentation",
    brand_config=brand_config
)

html = swagger.render()
```

### Configuration Options

```python
swagger = SynetoSwaggerUI(
    openapi_url="/openapi.json",
    title="API Documentation",
    brand_config=brand_config,
    
    # SwaggerUI-specific options
    deep_linking=True,
    display_operation_id=False,
    default_models_expand_depth=1,
    default_model_expand_depth=1,
    default_model_rendering="example",  # "example", "model"
    display_request_duration=False,
    doc_expansion="list",               # "list", "full", "none"
    filter=True,
    max_displayed_tags=None,
    show_extensions=False,
    show_common_extensions=False,
    use_unsafe_markdown=False
)
```

### OAuth2 Configuration

```python
# OAuth2 setup
swagger.with_oauth2(
    client_id="my-client-id",
    client_secret="my-client-secret",  # Optional
    realm="my-realm",                  # Optional
    app_name="My API",                 # Optional
    scope_separator=" ",
    scopes={
        "read": "Read access",
        "write": "Write access"
    },
    additional_query_string_params={
        "audience": "my-api"
    },
    use_basic_authentication_with_access_code_grant=False,
    use_pkce_with_authorization_code_grant=True
)

# API Key authentication
swagger.with_api_key_auth(api_key_name="X-API-Key")
```

### Best Use Cases

- Public APIs with external developers
- APIs requiring OAuth2 authentication
- Teams familiar with Swagger ecosystem
- APIs needing comprehensive model documentation

## ReDoc

Clean, responsive documentation with excellent navigation and professional appearance.

### Features

- Clean, professional design
- Excellent navigation
- Responsive layout
- Search functionality
- Code samples in multiple languages

### Basic Usage

```python
from syneto_openapi_themes import SynetoReDoc, get_default_brand_config

brand_config = get_default_brand_config()
redoc = SynetoReDoc(
    openapi_url="/openapi.json",
    title="My API Documentation",
    brand_config=brand_config
)

html = redoc.render()
```

### Configuration Options

```python
redoc = SynetoReDoc(
    openapi_url="/openapi.json",
    title="API Documentation",
    brand_config=brand_config,
    
    # ReDoc-specific options
    lazy_rendering=True,
    hide_download_button=False,
    hide_hostname=False,
    hide_loading=False,
    hide_schema_titles=False,
    hide_single_request_sample_tab=False,
    expand_responses=["200", "201"],
    required_props_first=False,
    sort_props_alphabetically=False,
    show_object_schema_examples=False,
    payload_sample_idx=0
)
```

### Theme Customization

```python
# Custom theme configuration
theme_config = {
    "colors": {
        "primary": {
            "main": "#ad0f6c"
        },
        "success": {
            "main": "#059669"
        },
        "warning": {
            "main": "#d97706"
        },
        "error": {
            "main": "#f01932"
        }
    },
    "typography": {
        "fontSize": "14px",
        "lineHeight": "1.5em",
        "code": {
            "fontSize": "13px",
            "fontFamily": "'JetBrains Mono', monospace"
        }
    },
    "sidebar": {
        "width": "260px",
        "backgroundColor": "#0f141f"
    }
}

redoc.with_custom_theme(theme_config)

# Disable search
redoc.with_search_disabled()
```

### Best Use Cases

- Public-facing API documentation
- APIs requiring professional presentation
- Documentation-heavy APIs
- APIs with complex nested schemas

## Elements

Modern, component-based documentation interface with excellent user experience.

### Features

- Modern, component-based design
- Multiple layout options
- Try-it functionality
- Mock server integration
- Excellent mobile experience

### Basic Usage

```python
from syneto_openapi_themes import SynetoElements, get_default_brand_config

brand_config = get_default_brand_config()
elements = SynetoElements(
    openapi_url="/openapi.json",
    title="My API Documentation",
    brand_config=brand_config
)

html = elements.render()
```

### Configuration Options

```python
elements = SynetoElements(
    openapi_url="/openapi.json",
    title="API Documentation",
    brand_config=brand_config,
    
    # Elements-specific options
    layout="sidebar",              # "sidebar", "stacked"
    hide_try_it=False,
    hide_schemas=False,
    hide_export=False,
    try_it_cors_proxy="https://cors-anywhere.herokuapp.com",
    try_it_credentials_policy="omit",  # "omit", "include", "same-origin"
    router="hash",                 # "hash", "memory", "history"
    base_path="/docs"
)
```

### Layout Configuration

```python
# Get layout configuration
layout_config = elements.get_layout_config()

# Use sidebar layout
elements.with_sidebar_layout()

# Use stacked layout
elements.with_stacked_layout()

# Disable try-it functionality
elements.with_try_it_disabled()
```

### Best Use Cases

- Modern web applications
- Mobile-first documentation
- APIs requiring excellent UX
- Component-based design systems

## Scalar

Beautiful, fast documentation with excellent user experience and modern design.

### Features

- Beautiful, modern design
- Fast performance
- Excellent user experience
- Multiple layout options
- Advanced search

### Basic Usage

```python
from syneto_openapi_themes import SynetoScalar, get_default_brand_config

brand_config = get_default_brand_config()
scalar = SynetoScalar(
    openapi_url="/openapi.json",
    title="My API Documentation",
    brand_config=brand_config
)

html = scalar.render()
```

### Configuration Options

```python
scalar = SynetoScalar(
    openapi_url="/openapi.json",
    title="API Documentation",
    brand_config=brand_config,
    
    # Scalar-specific options
    layout="modern",               # "modern", "classic"
    theme="dark",                  # "dark", "light", "auto"
    show_sidebar=True,
    hide_models=False,
    hide_download_button=False,
    dark_mode=True,
    force_theme_mode="dark",       # "dark", "light"
    hide_client_button=False,
    metadata={
        "title": "Custom API Title",
        "description": "Custom description"
    }
)
```

### Layout Configuration

```python
# Get configuration
config = scalar.get_configuration()

# Use modern layout
scalar.with_modern_layout()

# Use classic layout
scalar.with_classic_layout()

# Hide sidebar
scalar.with_sidebar_hidden()

# Hide models section
scalar.with_models_hidden()
```

### Best Use Cases

- Modern APIs requiring beautiful presentation
- Performance-critical documentation
- APIs with complex schemas
- Teams prioritizing user experience

## Comparison Matrix

| Feature | RapiDoc | SwaggerUI | ReDoc | Elements | Scalar |
|---------|---------|-----------|-------|----------|--------|
| **Interactive Testing** | ✅ Excellent | ✅ Good | ❌ No | ✅ Good | ✅ Good |
| **OAuth2 Support** | ✅ Yes | ✅ Excellent | ❌ No | ✅ Yes | ✅ Yes |
| **Mobile Experience** | ⚠️ Fair | ⚠️ Fair | ✅ Good | ✅ Excellent | ✅ Excellent |
| **Performance** | ✅ Good | ⚠️ Fair | ✅ Good | ✅ Good | ✅ Excellent |
| **Customization** | ✅ Excellent | ✅ Good | ✅ Good | ✅ Good | ✅ Good |
| **Search** | ✅ Yes | ✅ Yes | ✅ Excellent | ✅ Yes | ✅ Excellent |
| **Code Samples** | ✅ Yes | ✅ Yes | ✅ Multiple | ✅ Yes | ✅ Yes |
| **Learning Curve** | ⚠️ Medium | ✅ Easy | ✅ Easy | ⚠️ Medium | ✅ Easy |

## Tool Selection Guide

### Choose RapiDoc when:
- Interactive testing is crucial
- You need extensive customization
- Working with complex APIs
- Targeting developer audiences

### Choose SwaggerUI when:
- Team is familiar with Swagger
- Need comprehensive OAuth2 support
- Working with existing Swagger tooling
- Need proven, stable solution

### Choose ReDoc when:
- Professional presentation is important
- Documentation quality is priority
- Need excellent navigation
- Working with complex schemas

### Choose Elements when:
- Modern design is important
- Mobile experience is crucial
- Need component-based architecture
- Want excellent UX

### Choose Scalar when:
- Performance is critical
- Beautiful design is priority
- Need modern user experience
- Want fast loading times

## Integration Examples

### Multiple Tools Setup

```python
from fastapi import FastAPI
from syneto_openapi_themes import (
    add_syneto_rapidoc,
    add_syneto_swagger,
    add_syneto_redoc,
    add_syneto_elements,
    add_syneto_scalar,
    get_default_brand_config
)

app = FastAPI(title="Multi-Tool API")
brand_config = get_default_brand_config()

# Add all documentation tools
add_syneto_rapidoc(app, docs_url="/docs", brand_config=brand_config)
add_syneto_swagger(app, docs_url="/swagger", brand_config=brand_config)
add_syneto_redoc(app, docs_url="/redoc", brand_config=brand_config)
add_syneto_elements(app, docs_url="/elements", brand_config=brand_config)
add_syneto_scalar(app, docs_url="/scalar", brand_config=brand_config)
```

### Tool-Specific Customization

```python
from syneto_openapi_themes import SynetoDocsManager, get_default_brand_config

app = FastAPI(title="Customized API")
brand_config = get_default_brand_config()

docs_manager = SynetoDocsManager(app, brand_config=brand_config)

# Add tools with specific configurations
docs_manager.add_rapidoc(
    "/docs",
    render_style="focused",
    allow_try=True
).add_swagger(
    "/swagger",
    deep_linking=True,
    filter=True
).add_redoc(
    "/redoc",
    hide_download_button=True,
    expand_responses=["200"]
).add_elements(
    "/elements",
    layout="sidebar",
    hide_try_it=False
).add_scalar(
    "/scalar",
    layout="modern",
    show_sidebar=True
)
```

## Performance Considerations

### Loading Speed
1. **Scalar**: Fastest loading and rendering
2. **Elements**: Fast with good caching
3. **ReDoc**: Good performance with lazy loading
4. **RapiDoc**: Good performance, configurable
5. **SwaggerUI**: Slower with large specs

### Bundle Size
1. **Scalar**: Smallest bundle size
2. **Elements**: Small, optimized bundle
3. **ReDoc**: Medium bundle size
4. **RapiDoc**: Medium, configurable features
5. **SwaggerUI**: Largest bundle size

### Memory Usage
1. **Scalar**: Lowest memory usage
2. **Elements**: Low memory usage
3. **ReDoc**: Medium memory usage
4. **RapiDoc**: Medium, depends on features
5. **SwaggerUI**: Highest memory usage

## Troubleshooting

### Common Issues

1. **Tool not loading**: Check OpenAPI URL accessibility
2. **Styling conflicts**: Verify custom CSS doesn't conflict
3. **Authentication not working**: Check authentication configuration
4. **Performance issues**: Consider tool choice and optimization

### Debug Mode

```python
# Enable debug mode for troubleshooting
debug_config = SynetoBrandConfig(
    primary_color="#ff0000",  # Bright red for visibility
    custom_css_urls=["/static/debug.css"]
)

# Test each tool individually
rapidoc = SynetoRapiDoc(openapi_url="/openapi.json", brand_config=debug_config)
print("RapiDoc HTML length:", len(rapidoc.render()))
``` 