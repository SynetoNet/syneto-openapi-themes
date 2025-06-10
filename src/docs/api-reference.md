# API Reference

Complete API documentation for Syneto OpenAPI Themes.

## Core Classes

### SynetoBrandConfig

Central configuration class for Syneto branding and theming.

```python
@dataclass
class SynetoBrandConfig:
    def __init__(
        self,
        logo_url: str = "/static/syneto-logo.svg",
        favicon_url: str = "/static/favicon.ico", 
        company_name: str = "Syneto",
        theme: SynetoTheme = SynetoTheme.DARK,
        primary_color: str = SynetoColors.PRIMARY_MAGENTA,
        background_color: str = SynetoColors.PRIMARY_DARK,
        text_color: str = SynetoColors.PRIMARY_LIGHT,
        nav_bg_color: str = SynetoColors.SECONDARY_DARK,
        nav_text_color: str = SynetoColors.SECONDARY_LIGHT,
        nav_hover_bg_color: str = SynetoColors.SECONDARY_MEDIUM,
        nav_hover_text_color: str = SynetoColors.PRIMARY_LIGHT,
        nav_accent_color: str = SynetoColors.PRIMARY_MAGENTA,
        nav_accent_text_color: str = SynetoColors.PRIMARY_LIGHT,
        header_color: str = SynetoColors.SECONDARY_MEDIUM,
        regular_font: str = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
        mono_font: str = "'JetBrains Mono', 'Fira Code', 'Monaco', 'Consolas', monospace",
        custom_css_urls: Optional[List[str]] = None,
        custom_js_urls: Optional[List[str]] = None
    )
```

**Parameters:**
- `logo_url` (str): URL to the company logo
- `favicon_url` (str): URL to the favicon
- `company_name` (str): Company name for branding
- `theme` (SynetoTheme): Theme variant (dark, light, auto)
- `primary_color` (str): Primary brand color
- `background_color` (str): Main background color
- `text_color` (str): Primary text color
- `nav_bg_color` (str): Navigation background color
- `nav_text_color` (str): Navigation text color
- `nav_hover_bg_color` (str): Navigation hover background color
- `nav_hover_text_color` (str): Navigation hover text color
- `nav_accent_color` (str): Navigation accent color
- `nav_accent_text_color` (str): Navigation accent text color
- `header_color` (str): Header background color
- `regular_font` (str): Font family for regular text
- `mono_font` (str): Font family for monospace text
- `custom_css_urls` (List[str], optional): Additional CSS files to include
- `custom_js_urls` (List[str], optional): Additional JavaScript files to include

#### Methods

##### to_rapidoc_attributes()

```python
def to_rapidoc_attributes(self) -> Dict[str, str]
```

Convert brand configuration to RapiDoc HTML attributes.

**Returns:** Dictionary of HTML attributes for RapiDoc

##### to_css_variables()

```python
def to_css_variables(self) -> str
```

Convert brand configuration to CSS custom properties.

**Returns:** CSS string with custom properties

##### get_loading_css()

```python
def get_loading_css(self) -> str
```

Get CSS for loading indicators with Syneto branding.

**Returns:** CSS string for loading states

### SynetoColors

Official Syneto color palette constants.

```python
class SynetoColors:
    # Primary colors
    PRIMARY_MAGENTA = "#ad0f6c"
    PRIMARY_DARK = "#07080d"
    PRIMARY_LIGHT = "#fcfdfe"
    
    # Secondary colors
    SECONDARY_DARK = "#0f141f"
    SECONDARY_MEDIUM = "#161c2d"
    SECONDARY_LIGHT = "#c4c6ca"
    
    # Accent colors
    ACCENT_RED = "#f01932"
    ACCENT_BLUE = "#1e3a8a"
    ACCENT_GREEN = "#059669"
    ACCENT_YELLOW = "#d97706"
    
    # Neutral colors
    NEUTRAL_100 = "#f8fafc"
    NEUTRAL_200 = "#e2e8f0"
    NEUTRAL_300 = "#cbd5e1"
    NEUTRAL_400 = "#94a3b8"
    NEUTRAL_500 = "#64748b"
    NEUTRAL_600 = "#475569"
    NEUTRAL_700 = "#334155"
    NEUTRAL_800 = "#1e293b"
    NEUTRAL_900 = "#0f172a"
```

### SynetoTheme

Theme variant enumeration.

```python
class SynetoTheme(Enum):
    DARK = "dark"
    LIGHT = "light"
    AUTO = "auto"
```

## Documentation Tool Classes

### SynetoRapiDoc

Syneto-branded RapiDoc implementation.

```python
class SynetoRapiDoc(RapiDoc):
    def __init__(
        self,
        openapi_url: str,
        title: str = "API Documentation",
        brand_config: Optional[SynetoBrandConfig] = None,
        **kwargs
    )
```

**Parameters:**
- `openapi_url` (str): URL to the OpenAPI specification
- `title` (str): Page title for the documentation
- `brand_config` (SynetoBrandConfig, optional): Brand configuration
- `**kwargs`: Additional RapiDoc-specific options

#### Methods

##### render()

```python
def render(self, **kwargs) -> str
```

Render the documentation as HTML with Syneto branding.

**Returns:** Complete HTML string

##### get_authentication_config()

```python
def get_authentication_config(self) -> Dict[str, Any]
```

Get authentication configuration for RapiDoc.

**Returns:** Dictionary with authentication settings

##### with_jwt_auth()

```python
def with_jwt_auth(self, token_url: str = "/auth/token") -> "SynetoRapiDoc"
```

Configure JWT authentication.

**Parameters:**
- `token_url` (str): URL for token endpoint

**Returns:** Self for method chaining

##### with_api_key_auth()

```python
def with_api_key_auth(self, api_key_name: str = "X-API-Key") -> "SynetoRapiDoc"
```

Configure API key authentication.

**Parameters:**
- `api_key_name` (str): Name of the API key header

**Returns:** Self for method chaining

### SynetoSwaggerUI

Syneto-branded SwaggerUI implementation.

```python
class SynetoSwaggerUI(SwaggerUI):
    def __init__(
        self,
        openapi_url: str,
        title: str = "API Documentation",
        brand_config: Optional[SynetoBrandConfig] = None,
        **kwargs
    )
```

#### Methods

##### get_oauth_config()

```python
def get_oauth_config(self) -> Dict[str, Any]
```

Get OAuth configuration for SwaggerUI.

**Returns:** Dictionary with OAuth settings

##### with_oauth2()

```python
def with_oauth2(
    self,
    client_id: str,
    client_secret: Optional[str] = None,
    realm: Optional[str] = None,
    app_name: Optional[str] = None,
    scope_separator: str = " ",
    scopes: Optional[Dict[str, str]] = None,
    additional_query_string_params: Optional[Dict[str, str]] = None,
    use_basic_authentication_with_access_code_grant: bool = False,
    use_pkce_with_authorization_code_grant: bool = False
) -> "SynetoSwaggerUI"
```

Configure OAuth2 authentication.

**Returns:** Self for method chaining

##### with_api_key_auth()

```python
def with_api_key_auth(self, api_key_name: str = "X-API-Key") -> "SynetoSwaggerUI"
```

Configure API key authentication.

**Returns:** Self for method chaining

### SynetoReDoc

Syneto-branded ReDoc implementation.

```python
class SynetoReDoc(ReDoc):
    def __init__(
        self,
        openapi_url: str,
        title: str = "API Documentation",
        brand_config: Optional[SynetoBrandConfig] = None,
        **kwargs
    )
```

#### Methods

##### get_theme_config()

```python
def get_theme_config(self) -> Dict[str, Any]
```

Get theme configuration for ReDoc.

**Returns:** Dictionary with theme settings

##### with_custom_theme()

```python
def with_custom_theme(self, theme_config: Dict[str, Any]) -> "SynetoReDoc"
```

Apply custom theme configuration.

**Parameters:**
- `theme_config` (Dict): Custom theme settings

**Returns:** Self for method chaining

##### with_search_disabled()

```python
def with_search_disabled(self) -> "SynetoReDoc"
```

Disable search functionality.

**Returns:** Self for method chaining

### SynetoElements

Syneto-branded Elements implementation.

```python
class SynetoElements(Elements):
    def __init__(
        self,
        openapi_url: str,
        title: str = "API Documentation",
        brand_config: Optional[SynetoBrandConfig] = None,
        **kwargs
    )
```

#### Methods

##### get_layout_config()

```python
def get_layout_config(self) -> Dict[str, Any]
```

Get layout configuration for Elements.

**Returns:** Dictionary with layout settings

##### with_sidebar_layout()

```python
def with_sidebar_layout(self) -> "SynetoElements"
```

Use sidebar layout.

**Returns:** Self for method chaining

##### with_stacked_layout()

```python
def with_stacked_layout(self) -> "SynetoElements"
```

Use stacked layout.

**Returns:** Self for method chaining

##### with_try_it_disabled()

```python
def with_try_it_disabled(self) -> "SynetoElements"
```

Disable try-it functionality.

**Returns:** Self for method chaining

### SynetoScalar

Syneto-branded Scalar implementation.

```python
class SynetoScalar(Scalar):
    def __init__(
        self,
        openapi_url: str,
        title: str = "API Documentation",
        brand_config: Optional[SynetoBrandConfig] = None,
        **kwargs
    )
```

#### Methods

##### get_configuration()

```python
def get_configuration(self) -> Dict[str, Any]
```

Get configuration for Scalar.

**Returns:** Dictionary with configuration settings

##### with_modern_layout()

```python
def with_modern_layout(self) -> "SynetoScalar"
```

Use modern layout.

**Returns:** Self for method chaining

##### with_classic_layout()

```python
def with_classic_layout(self) -> "SynetoScalar"
```

Use classic layout.

**Returns:** Self for method chaining

##### with_sidebar_hidden()

```python
def with_sidebar_hidden(self) -> "SynetoScalar"
```

Hide the sidebar.

**Returns:** Self for method chaining

##### with_models_hidden()

```python
def with_models_hidden(self) -> "SynetoScalar"
```

Hide the models section.

**Returns:** Self for method chaining

## FastAPI Integration

### SynetoDocsManager

Centralized documentation management for FastAPI applications.

```python
class SynetoDocsManager:
    def __init__(
        self,
        app: FastAPI,
        brand_config: Optional[SynetoBrandConfig] = None,
        openapi_url: str = "/openapi.json"
    )
```

**Parameters:**
- `app` (FastAPI): FastAPI application instance
- `brand_config` (SynetoBrandConfig, optional): Brand configuration
- `openapi_url` (str): URL to OpenAPI specification

#### Properties

##### endpoints

```python
@property
def endpoints(self) -> Dict[str, str]
```

Get dictionary of registered documentation endpoints.

**Returns:** Dictionary mapping tool names to URLs

#### Methods

##### add_rapidoc()

```python
def add_rapidoc(
    self,
    docs_url: str = "/docs",
    **kwargs
) -> "SynetoDocsManager"
```

Add RapiDoc documentation.

**Parameters:**
- `docs_url` (str): URL path for documentation
- `**kwargs`: Additional RapiDoc options

**Returns:** Self for method chaining

##### add_swagger()

```python
def add_swagger(
    self,
    docs_url: str = "/swagger",
    **kwargs
) -> "SynetoDocsManager"
```

Add SwaggerUI documentation.

**Returns:** Self for method chaining

##### add_redoc()

```python
def add_redoc(
    self,
    docs_url: str = "/redoc",
    **kwargs
) -> "SynetoDocsManager"
```

Add ReDoc documentation.

**Returns:** Self for method chaining

##### add_elements()

```python
def add_elements(
    self,
    docs_url: str = "/elements",
    **kwargs
) -> "SynetoDocsManager"
```

Add Elements documentation.

**Returns:** Self for method chaining

##### add_scalar()

```python
def add_scalar(
    self,
    docs_url: str = "/scalar",
    **kwargs
) -> "SynetoDocsManager"
```

Add Scalar documentation.

**Returns:** Self for method chaining

##### add_all()

```python
def add_all(self, **kwargs) -> "SynetoDocsManager"
```

Add all documentation tools with default URLs.

**Returns:** Self for method chaining

##### add_docs_index()

```python
def add_docs_index(
    self,
    index_url: str = "/",
    title: Optional[str] = None
) -> "SynetoDocsManager"
```

Add an index page with links to all documentation tools.

**Parameters:**
- `index_url` (str): URL for the index page
- `title` (str, optional): Custom title for the index page

**Returns:** Self for method chaining

### Integration Functions

#### add_syneto_rapidoc()

```python
def add_syneto_rapidoc(
    app: FastAPI,
    openapi_url: str = "/openapi.json",
    docs_url: str = "/docs",
    brand_config: Optional[SynetoBrandConfig] = None,
    **kwargs
) -> None
```

Add Syneto-branded RapiDoc to FastAPI application.

#### add_syneto_swagger()

```python
def add_syneto_swagger(
    app: FastAPI,
    openapi_url: str = "/openapi.json",
    docs_url: str = "/swagger",
    brand_config: Optional[SynetoBrandConfig] = None,
    **kwargs
) -> None
```

Add Syneto-branded SwaggerUI to FastAPI application.

#### add_syneto_redoc()

```python
def add_syneto_redoc(
    app: FastAPI,
    openapi_url: str = "/openapi.json",
    docs_url: str = "/redoc",
    brand_config: Optional[SynetoBrandConfig] = None,
    **kwargs
) -> None
```

Add Syneto-branded ReDoc to FastAPI application.

#### add_syneto_elements()

```python
def add_syneto_elements(
    app: FastAPI,
    openapi_url: str = "/openapi.json",
    docs_url: str = "/elements",
    brand_config: Optional[SynetoBrandConfig] = None,
    **kwargs
) -> None
```

Add Syneto-branded Elements to FastAPI application.

#### add_syneto_scalar()

```python
def add_syneto_scalar(
    app: FastAPI,
    openapi_url: str = "/openapi.json",
    docs_url: str = "/scalar",
    brand_config: Optional[SynetoBrandConfig] = None,
    **kwargs
) -> None
```

Add Syneto-branded Scalar to FastAPI application.

#### add_all_syneto_docs()

```python
def add_all_syneto_docs(
    app: FastAPI,
    openapi_url: str = "/openapi.json",
    brand_config: Optional[SynetoBrandConfig] = None,
    rapidoc_url: str = "/docs",
    swagger_url: str = "/swagger",
    redoc_url: str = "/redoc",
    elements_url: str = "/elements",
    scalar_url: str = "/scalar",
    **kwargs
) -> None
```

Add all Syneto-branded documentation tools to FastAPI application.

## Utility Functions

### get_default_brand_config()

```python
def get_default_brand_config() -> SynetoBrandConfig
```

Get the default Syneto brand configuration (dark theme).

**Returns:** Default SynetoBrandConfig instance

### get_light_brand_config()

```python
def get_light_brand_config() -> SynetoBrandConfig
```

Get a light theme Syneto brand configuration.

**Returns:** Light theme SynetoBrandConfig instance

## Type Definitions

### Common Types

```python
from typing import Dict, List, Optional, Any, Union

# Brand configuration type
BrandConfigType = Optional[SynetoBrandConfig]

# CSS/JS URLs type
URLListType = Optional[List[str]]

# Configuration dictionary type
ConfigDictType = Dict[str, Any]

# HTML attributes type
AttributesType = Dict[str, str]
```

## Error Handling

All classes handle errors gracefully and provide meaningful error messages. Common error scenarios:

- **Missing OpenAPI URL**: Returns error page with instructions
- **Invalid brand configuration**: Falls back to default configuration
- **Network errors**: Shows loading state with timeout handling
- **Rendering errors**: Provides fallback HTML with error information

## Examples

### Basic Usage

```python
from syneto_openapi_themes import SynetoRapiDoc, get_default_brand_config

brand_config = get_default_brand_config()
rapidoc = SynetoRapiDoc(
    openapi_url="/openapi.json",
    title="My API",
    brand_config=brand_config
)
html = rapidoc.render()
```

### FastAPI Integration

```python
from fastapi import FastAPI
from syneto_openapi_themes import SynetoDocsManager, get_default_brand_config

app = FastAPI()
brand_config = get_default_brand_config()

docs_manager = SynetoDocsManager(app, brand_config=brand_config)
docs_manager.add_rapidoc("/docs").add_swagger("/swagger").add_docs_index("/")
```

### Custom Configuration

```python
from syneto_openapi_themes import SynetoBrandConfig, SynetoTheme, SynetoColors

custom_config = SynetoBrandConfig(
    theme=SynetoTheme.LIGHT,
    primary_color=SynetoColors.ACCENT_BLUE,
    company_name="Custom Corp",
    custom_css_urls=["/static/custom.css"]
)
``` 